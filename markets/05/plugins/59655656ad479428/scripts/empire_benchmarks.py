#!/usr/bin/env python3
"""Rank current language models and render a sandboxed Codex chart fragment."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import empire_review_runtime as runtime


class BenchmarkError(RuntimeError):
    """Raised when benchmark evidence cannot be normalized safely."""


PROFILE_WEIGHTS: dict[str, dict[str, float]] = {
    "agentic": {
        "agentic": 0.42,
        "coding": 0.22,
        "intelligence": 0.16,
        "modality": 0.10,
        "speed": 0.05,
        "cost": 0.05,
    },
    "coding": {
        "agentic": 0.22,
        "coding": 0.42,
        "intelligence": 0.16,
        "modality": 0.10,
        "speed": 0.05,
        "cost": 0.05,
    },
    "balanced": {
        "agentic": 0.25,
        "coding": 0.25,
        "intelligence": 0.20,
        "modality": 0.10,
        "speed": 0.10,
        "cost": 0.10,
    },
    "value": {
        "agentic": 0.18,
        "coding": 0.18,
        "intelligence": 0.14,
        "modality": 0.10,
        "speed": 0.15,
        "cost": 0.25,
    },
}
DIMENSIONS = tuple(next(iter(PROFILE_WEIGHTS.values())))
MAX_TOP = 20
MAX_FRAGMENT_BYTES = 1_000_000


def finite_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def nested_number(value: Any, *paths: str) -> float | None:
    for path in paths:
        current = value
        for part in path.split("."):
            if not isinstance(current, dict):
                current = None
                break
            current = current.get(part)
        result = finite_number(current)
        if result is not None:
            return result
    return None


def load_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BenchmarkError(f"Could not read JSON input: {path}") from exc
    if not isinstance(value, dict):
        raise BenchmarkError(f"JSON input must contain an object: {path}")
    return value


def parse_weights(profile: str, overrides: list[str]) -> dict[str, float]:
    weights = dict(PROFILE_WEIGHTS[profile])
    for override in overrides:
        name, separator, raw_value = override.partition("=")
        if not separator or name not in DIMENSIONS:
            raise BenchmarkError(
                "Weights must use agentic|coding|intelligence|modality|speed|cost=VALUE"
            )
        value = finite_number(raw_value)
        if value is None or value < 0 or value > 100:
            raise BenchmarkError(f"Invalid weight for {name}: {raw_value}")
        weights[name] = value
    total = sum(weights.values())
    if total <= 0:
        raise BenchmarkError("At least one scoring weight must be positive")
    return {name: round(value / total, 8) for name, value in weights.items()}


def normalized_modalities(value: Any, direction: str) -> list[str]:
    if isinstance(value, dict):
        candidates = (
            value.get(direction)
            or value.get(f"{direction}_modalities")
            or value.get(f"{direction}s")
            or []
        )
    elif isinstance(value, list):
        candidates = value
    else:
        candidates = []
    if isinstance(candidates, str):
        candidates = [candidates]
    if not isinstance(candidates, list):
        return []
    result: list[str] = []
    for item in candidates:
        if not isinstance(item, str):
            continue
        normalized = item.strip().lower().replace("_", "-")
        if normalized and normalized not in result:
            result.append(normalized)
    return result


def openrouter_index(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return runtime.exact_model_index(payload, "id")


def modality_evidence(
    aa_row: dict[str, Any],
    route: dict[str, Any] | None,
    required_input: list[str],
    required_output: list[str],
) -> dict[str, Any]:
    if route is not None:
        architecture = route.get("architecture")
        architecture = architecture if isinstance(architecture, dict) else {}
        raw_inputs = architecture.get("input_modalities")
        raw_outputs = architecture.get("output_modalities")
        inputs = normalized_modalities(raw_inputs, "input") if isinstance(raw_inputs, list) and all(isinstance(v, str) for v in raw_inputs) else []
        outputs = normalized_modalities(raw_outputs, "output") if isinstance(raw_outputs, list) and all(isinstance(v, str) for v in raw_outputs) else []
        source = "openrouter_exact_model"
    else:
        modalities = aa_row.get("modalities")
        inputs = normalized_modalities(modalities, "input")
        outputs = normalized_modalities(modalities, "output")
        source = "artificial_analysis"
    missing_input = sorted(set(required_input) - set(inputs))
    missing_output = sorted(set(required_output) - set(outputs))
    verified = bool(inputs and outputs)
    compatible = verified and not missing_input and not missing_output
    return {
        "status": "compatible"
        if compatible
        else "incompatible"
        if verified
        else "unverified",
        "source": source,
        "input_modalities": inputs,
        "output_modalities": outputs,
        "missing_input": missing_input,
        "missing_output": missing_output,
    }


def _scale(values: list[float | None], *, reverse: bool = False) -> list[float | None]:
    present = [value for value in values if value is not None]
    if not present:
        return [None for _ in values]
    low, high = min(present), max(present)
    scaled: list[float | None] = []
    for value in values:
        if value is None:
            scaled.append(None)
            continue
        if high == low:
            scaled.append(1.0)
        else:
            score = (value - low) / (high - low)
            scaled.append(1.0 - score if reverse else score)
    return scaled


def _index_score(value: float | None) -> float | None:
    if value is None:
        return None
    return max(0.0, min(1.0, value / 100.0))


def _model_icon(model_id: str, name: str) -> dict[str, Any]:
    icon = runtime.resolve_model_icon(model_id, name)
    return {
        "id": icon.get("icon_id"),
        "svg_path": icon.get("icon_path"),
        "footnote_path": icon.get("icon_footnote_path"),
        "fallback": bool(icon.get("icon_fallback_used")),
    }


def rank_models(
    artificial_analysis: dict[str, Any],
    openrouter: dict[str, Any] | None,
    *,
    profile: str,
    weights: dict[str, float],
    required_input: list[str],
    required_output: list[str],
    include_openai: bool,
    route_qualified_only: bool,
    top: int,
) -> dict[str, Any]:
    if not isinstance(artificial_analysis.get("data"), list):
        raise BenchmarkError("Artificial Analysis payload has no model data")
    route_identity_available = any(
        isinstance(row, dict)
        and isinstance(row.get("openrouter_api_id"), str)
        and bool(row["openrouter_api_id"].strip())
        for row in artificial_analysis["data"]
    )
    if route_qualified_only and artificial_analysis["data"] and not route_identity_available:
        raise BenchmarkError(
            "Exact route qualification requires openrouter_api_id evidence. "
            "Artificial Analysis Free omits this field; use Pro/Commercial access "
            "or omit --route-qualified-only for an unverified research view. "
            "No route has been authorized."
        )
    routes = openrouter_index(openrouter or {})
    aa_routes = runtime.aa_index(artificial_analysis)
    candidates: list[dict[str, Any]] = []
    for row in artificial_analysis["data"]:
        if not isinstance(row, dict):
            continue
        model_id = row.get("id")
        name = row.get("name")
        slug = row.get("slug")
        creator = row.get("model_creator")
        creator = creator if isinstance(creator, dict) else {}
        creator_name = str(creator.get("name") or "Unknown")
        if (
            not isinstance(model_id, str)
            or not model_id.strip()
            or not isinstance(name, str)
            or not name.strip()
            or not isinstance(slug, str)
            or not slug.strip()
        ):
            continue
        is_openai = creator_name.strip().lower() == "openai"
        if is_openai and not include_openai:
            continue
        evaluations = row.get("evaluations")
        evaluations = evaluations if isinstance(evaluations, dict) else {}
        route_id = row.get("openrouter_api_id")
        route_id = route_id if isinstance(route_id, str) else ""
        route = routes.get(route_id) if route_id in aa_routes else None
        modality = modality_evidence(
            row, route, required_input, required_output
        )
        exact_join = route is not None
        route_eligible = bool(
            exact_join and modality["status"] == "compatible" and not is_openai
        )
        if route_qualified_only and not route_eligible:
            continue
        pricing = row.get("pricing")
        pricing = pricing if isinstance(pricing, dict) else {}
        performance = row.get("performance")
        performance = performance if isinstance(performance, dict) else {}
        cost_field = "artificial_analysis_intelligence_index_cost.cost_per_task.total_cost"
        cost = nested_number(row, cost_field)
        if cost is not None and cost < 0:
            cost = None
        speed = nested_number(
            performance,
            "median_output_tokens_per_second",
        )
        if speed is None:
            speed = nested_number(row, "median_output_tokens_per_second")
        candidates.append(
            {
                "aa_id": model_id,
                "name": name,
                "slug": slug,
                "creator": creator_name,
                "release_date": row.get("release_date"),
                "reasoning_model": row.get("reasoning_model"),
                "openrouter_model_id": route_id or None,
                "openrouter_exact_match": exact_join,
                "route_eligible": route_eligible,
                "route_eligibility_reason": "exact_identity_and_modalities"
                if route_eligible
                else "openai_is_codex_lead"
                if is_openai
                else "modality_requirement_failed"
                if modality["status"] == "incompatible"
                else "modality_evidence_unverified"
                if exact_join and modality["status"] == "unverified"
                else "exact_openrouter_identity_unavailable",
                "modality": modality,
                "cost_evidence": {
                    "unit": "USD/task", "source_field": cost_field,
                    "status": "available" if cost is not None else "unavailable",
                },
                "metrics": {
                    "agentic_index": nested_number(
                        evaluations, "artificial_analysis_agentic_index"
                    ),
                    "coding_index": nested_number(
                        evaluations, "artificial_analysis_coding_index"
                    ),
                    "intelligence_index": nested_number(
                        evaluations, "artificial_analysis_intelligence_index"
                    ),
                    "output_tokens_per_second": speed,
                    "cost_per_task_usd": cost,
                    "input_price_per_million_usd": nested_number(
                        pricing, "price_1m_input_tokens"
                    ),
                    "output_price_per_million_usd": nested_number(
                        pricing, "price_1m_output_tokens"
                    ),
                },
                "icon": _model_icon(route_id or f"{creator_name}/{slug}", name),
            }
        )
    if not candidates:
        raise BenchmarkError("No models satisfy the requested benchmark filters")

    speed_scores = _scale(
        [item["metrics"]["output_tokens_per_second"] for item in candidates]
    )
    cost_scores = _scale(
        [item["metrics"]["cost_per_task_usd"] for item in candidates],
        reverse=True,
    )
    for item, speed_score, cost_score in zip(
        candidates, speed_scores, cost_scores, strict=True
    ):
        metrics = item["metrics"]
        dimensions = {
            "agentic": _index_score(metrics["agentic_index"]),
            "coding": _index_score(metrics["coding_index"]),
            "intelligence": _index_score(metrics["intelligence_index"]),
            "modality": 1.0
            if item["modality"]["status"] == "compatible"
            else 0.0
            if item["modality"]["status"] == "incompatible"
            else None,
            "speed": speed_score,
            "cost": cost_score,
        }
        weighted = sum(
            weights[name] * value
            for name, value in dimensions.items()
            if value is not None
        )
        coverage = sum(
            weights[name] for name, value in dimensions.items() if value is not None
        )
        item["dimension_scores"] = {
            name: round(value, 6) if value is not None else None
            for name, value in dimensions.items()
        }
        item["evidence_coverage"] = round(coverage, 6)
        item["weighted_score"] = round(weighted * 100, 2)

    candidates.sort(
        key=lambda item: (
            -item["weighted_score"],
            -item["evidence_coverage"],
            item["name"].lower(),
        )
    )
    for index, item in enumerate(candidates, start=1):
        item["rank"] = index
    visible = candidates[:top]
    aa_source = artificial_analysis.get("_empire_source")
    aa_source = aa_source if isinstance(aa_source, dict) else {}
    return {
        "schema_version": "1.0.0",
        "status": "ranked",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profile": profile,
        "weights": weights,
        "requirements": {
            "input_modalities": required_input,
            "output_modalities": required_output,
            "route_qualified_only": route_qualified_only,
            "openai_partner_candidates": False,
        },
        "source_receipts": {
            "artificial_analysis": {
                "status": "available",
                "endpoint": aa_source.get("endpoint"),
                "tier": artificial_analysis.get("tier"),
                "intelligence_index_version": artificial_analysis.get(
                    "intelligence_index_version"
                ),
                "pages_fetched": aa_source.get("pages_fetched"),
                "model_count": len(artificial_analysis["data"]),
                "route_identity_evidence": "available" if route_identity_available else "unavailable",
                "fetched_at": aa_source.get("fetched_at"),
                "rate_limit": aa_source.get("rate_limit"),
                "attribution_url": "https://artificialanalysis.ai/",
            },
            "openrouter": {
                "status": "available" if openrouter is not None else "unavailable",
                "endpoint": runtime.OPENROUTER_USER_MODELS
                if openrouter is not None
                else None,
                "model_count": len(routes),
                "exact_match_count": sum(
                    item["openrouter_exact_match"] for item in candidates
                ),
            },
        },
        "model_count_considered": len(candidates),
        "models": visible,
        "notes": [
            "Weighted scores are Empire routing inferences, not Artificial Analysis rankings.",
            "Missing evidence reduces the score instead of being treated as zero.",
            "Cost scores compare measured USD/task only; token prices are never substituted.",
            "Only exact Artificial Analysis openrouter_api_id joins can become route eligible.",
            "OpenAI models may be shown as research baselines but are never Empire partner candidates.",
        ],
    }


def fetch_sources(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any] | None]:
    if args.aa_fixture:
        aa = load_object(args.aa_fixture.resolve())
        aa.setdefault(
            "_empire_source",
            {
                "endpoint": "offline_fixture",
                "pages_fetched": 1,
                "model_count": len(aa.get("data", [])),
                "fetched_at": None,
                "rate_limit": None,
            },
        )
    else:
        aa_key, aa_source = runtime.resolve_credential(
            ("ARTIFICIAL_ANALYSIS_API_KEY", "AA_API_KEY"), "artificial-analysis"
        )
        if not aa_key:
            raise BenchmarkError(
                runtime.credential_required_message(
                    "Artificial Analysis",
                    aa_source,
                    "run the Empire settings setup before requesting live benchmarks",
                )
            )
        aa = runtime.fetch_artificial_analysis_models(aa_key, access=args.aa_access)

    if args.no_openrouter:
        return aa, None
    if args.openrouter_fixture:
        return aa, load_object(args.openrouter_fixture.resolve())
    openrouter_key, openrouter_source = runtime.resolve_credential(
        ("OPENROUTER_API_KEY",), "openrouter"
    )
    if not openrouter_key:
        if args.route_qualified_only:
            raise BenchmarkError(
                runtime.credential_required_message(
                    "OpenRouter",
                    openrouter_source,
                    "run the Empire settings setup for route-qualified rankings",
                )
            )
        return aa, None
    return aa, runtime.request_json(
        runtime.OPENROUTER_USER_MODELS, api_key=openrouter_key, timeout=10
    )


def markdown_view(payload: dict[str, Any]) -> str:
    source = payload["source_receipts"]["artificial_analysis"]
    lines = [
        f"## Empire benchmark view · {payload['profile']}",
        "",
        (
            "Live Artificial Analysis data"
            if source.get("endpoint") != "offline_fixture"
            else "Offline fixture data"
        )
        + f" · index v{source.get('intelligence_index_version') or 'unknown'}",
        "",
        "| Rank | Model | Weighted | Agentic | Coding | Intelligence | OpenRouter |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in payload["models"]:
        metrics = item["metrics"]
        route = item.get("openrouter_model_id") or "unverified"
        values = [
            item["rank"],
            item["name"],
            f"{item['weighted_score']:.2f}",
            metrics.get("agentic_index"),
            metrics.get("coding_index"),
            metrics.get("intelligence_index"),
            route,
        ]
        cells = [html.escape(str(value if value is not None else "—")) for value in values]
        lines.append("| " + " | ".join(cells) + " |")
    lines.extend(
        (
            "",
            "Weighted scores are Empire inferences. Benchmark source: "
            "[Artificial Analysis](https://artificialanalysis.ai/).",
        )
    )
    return "\n".join(lines) + "\n"


def icon_data_uri(path_value: Any) -> str | None:
    if not isinstance(path_value, str):
        return None
    path = Path(path_value)
    if not path.is_file() or path.is_symlink():
        return None
    data = path.read_bytes()
    if len(data) > 250_000:
        return None
    mime = "image/png" if path.suffix.lower() == ".png" else "image/svg+xml"
    return f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"


def render_fragment(payload: dict[str, Any]) -> str:
    models = payload.get("models")
    weights = payload.get("weights")
    if not isinstance(models, list) or not models:
        raise BenchmarkError("Benchmark result has no models to render")
    if not isinstance(weights, dict) or set(weights) != set(DIMENSIONS):
        raise BenchmarkError("Benchmark result has invalid weights")
    chart_models: list[dict[str, Any]] = []
    for item in models:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            raise BenchmarkError("Benchmark result contains an invalid model")
        chart_models.append(
            {
                "name": item["name"][:120],
                "creator": str(item.get("creator") or "Unknown")[:80],
                "modelId": str(item.get("openrouter_model_id") or item.get("slug"))[:200],
                "dimensions": item.get("dimension_scores"),
                "metrics": item.get("metrics"),
                "routeEligible": bool(item.get("route_eligible")),
                "modality": item.get("modality", {}).get("status"),
                "icon": icon_data_uri(item.get("icon", {}).get("footnote_path")),
            }
        )
    identity = hashlib.sha256(
        json.dumps(chart_models, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]
    root_id = f"empire-benchmarks-{identity}"
    data_json = json.dumps(
        {"models": chart_models, "weights": weights},
        separators=(",", ":"),
        ensure_ascii=True,
    ).replace("<", "\\u003c")
    profile = html.escape(str(payload.get("profile") or "weighted").title())
    source = payload.get("source_receipts", {}).get("artificial_analysis", {})
    version = html.escape(str(source.get("intelligence_index_version") or "unknown"))
    endpoint = source.get("endpoint")
    if endpoint == "offline_fixture":
        source_label = "Synthetic fixture"
    else:
        tier = str(source.get("tier") or "unknown").strip().title()
        source_label = f"Artificial Analysis {tier}"
    fetched_at = source.get("fetched_at")
    retrieved_label = (
        f" · retrieved {html.escape(str(fetched_at)[:40])}"
        if isinstance(fetched_at, str) and fetched_at.strip()
        else ""
    )
    fragment = f'''<section id="{root_id}">
  <h1>{profile} model benchmark</h1>
  <p class="text-muted">{html.escape(source_label)} · index v{version}{retrieved_label} · Empire weighted score (0–100)</p>
  <div class="viz-controls" aria-label="Scoring weights">
    <label class="form-label">Agentic <output data-value="agentic"></output><input class="form-range" data-weight="agentic" type="range" min="0" max="100" step="1"></label>
    <label class="form-label">Coding <output data-value="coding"></output><input class="form-range" data-weight="coding" type="range" min="0" max="100" step="1"></label>
    <label class="form-label">Intelligence <output data-value="intelligence"></output><input class="form-range" data-weight="intelligence" type="range" min="0" max="100" step="1"></label>
    <label class="form-label">Modality <output data-value="modality"></output><input class="form-range" data-weight="modality" type="range" min="0" max="100" step="1"></label>
    <label class="form-label">Speed <output data-value="speed"></output><input class="form-range" data-weight="speed" type="range" min="0" max="100" step="1"></label>
    <label class="form-label">Cost <output data-value="cost"></output><input class="form-range" data-weight="cost" type="range" min="0" max="100" step="1"></label>
  </div>
  <div class="empire-aa-axis text-small" aria-hidden="true"><span>100</span><span>75</span><span>50</span><span>25</span><span>0</span></div>
  <div class="empire-aa-bars" role="img" aria-label="Vertical bar chart ranking models by the selected weighted score"></div>
  <p class="empire-aa-detail text-small" aria-live="polite"></p>
  <div class="viz-row"><button class="btn" type="button" data-compare>Ask Codex to compare the leaders</button></div>
  <p class="text-small text-muted">Benchmark data © Artificial Analysis. Weighted scores are Empire inferences; exact OpenRouter identity and modality checks determine route eligibility.</p>
  <script type="application/json" data-benchmark-data>{data_json}</script>
  <style>
    #{root_id} {{ position: relative; color: var(--foreground); }}
    #{root_id} .empire-aa-axis {{ position: absolute; inset: 15.1rem auto 5.4rem 0; display: flex; flex-direction: column; justify-content: space-between; color: var(--muted-foreground); }}
    #{root_id} .empire-aa-bars {{ min-height: 22rem; margin-left: 2.25rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(5.5rem, 1fr)); gap: 0.75rem; align-items: end; border-bottom: 1px solid var(--border); }}
    #{root_id} .empire-aa-model {{ min-width: 0; display: grid; grid-template-rows: 15rem auto auto; gap: 0.45rem; align-items: end; text-align: center; }}
    #{root_id} .empire-aa-bar-zone {{ height: 15rem; display: flex; align-items: end; justify-content: center; background: repeating-linear-gradient(to top, transparent 0, transparent calc(25% - 1px), var(--border) 25%); }}
    #{root_id} .empire-aa-bar {{ width: min(3.25rem, 70%); min-height: 2px; background: var(--viz-series-1); transition: height 180ms ease; }}
    #{root_id} .empire-aa-score {{ color: var(--foreground); }}
    #{root_id} .empire-aa-chip {{ justify-self: center; max-width: 100%; overflow-wrap: anywhere; }}
    #{root_id} .empire-aa-chip img {{ width: 14px; height: 14px; flex: none; }}
    #{root_id} .empire-aa-detail {{ min-height: 1.4em; color: var(--muted-foreground); }}
    @media (prefers-reduced-motion: reduce) {{ #{root_id} .empire-aa-bar {{ transition: none; }} }}
    @media (max-width: 420px) {{ #{root_id} .empire-aa-bars {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} #{root_id} .empire-aa-axis {{ display: none; }} }}
  </style>
  <script>
    (() => {{
      const root = document.getElementById('{root_id}');
      const data = JSON.parse(root.querySelector('[data-benchmark-data]').textContent);
      const bars = root.querySelector('.empire-aa-bars');
      const detail = root.querySelector('.empire-aa-detail');
      const sliders = [...root.querySelectorAll('[data-weight]')];
      sliders.forEach((input) => {{ input.value = Math.round(data.weights[input.dataset.weight] * 100); }});
      const currentWeights = () => {{
        const raw = Object.fromEntries(sliders.map((input) => [input.dataset.weight, Number(input.value)]));
        const total = Object.values(raw).reduce((sum, value) => sum + value, 0) || 1;
        return Object.fromEntries(Object.entries(raw).map(([key, value]) => [key, value / total]));
      }};
      const score = (model, weights) => Object.entries(weights).reduce((sum, [key, weight]) => {{
        const value = model.dimensions && model.dimensions[key];
        return sum + (typeof value === 'number' ? value * weight : 0);
      }}, 0) * 100;
      const render = () => {{
        const weights = currentWeights();
        sliders.forEach((input) => {{ root.querySelector(`[data-value="${{input.dataset.weight}}"]`).textContent = `${{Math.round(weights[input.dataset.weight] * 100)}}%`; }});
        const ranked = data.models.map((model) => ({{...model, score: score(model, weights)}})).sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));
        bars.replaceChildren();
        ranked.forEach((model, index) => {{
          const item = document.createElement('article'); item.className = 'empire-aa-model';
          const zone = document.createElement('div'); zone.className = 'empire-aa-bar-zone';
          const bar = document.createElement('div'); bar.className = 'empire-aa-bar'; bar.style.height = `${{Math.max(0, Math.min(100, model.score))}}%`; bar.setAttribute('data-tooltip', `${{model.name}} · ${{model.score.toFixed(2)}} weighted score`); zone.append(bar);
          const value = document.createElement('strong'); value.className = 'empire-aa-score tabular-nums'; value.textContent = model.score.toFixed(1);
          const chip = document.createElement('div'); chip.className = 'viz-badge empire-aa-chip';
          if (model.icon) {{ const image = document.createElement('img'); image.src = model.icon; image.alt = ''; image.setAttribute('aria-hidden', 'true'); chip.append(image); }}
          const label = document.createElement('span'); label.textContent = model.name; chip.append(label);
          item.append(zone, value, chip); bars.append(item);
          if (index === 0) {{ detail.textContent = `Leader: ${{model.name}} · ${{model.score.toFixed(2)}} · ${{model.routeEligible ? 'exact OpenRouter route eligible' : 'benchmark view only'}} · modality ${{model.modality || 'unverified'}}`; }}
        }});
      }};
      sliders.forEach((input) => input.addEventListener('input', render));
      root.querySelector('[data-compare]').addEventListener('click', async () => {{
        const weights = currentWeights();
        const ranked = data.models.map((model) => ({{...model, score: score(model, weights)}})).sort((a, b) => b.score - a.score);
        const leaders = ranked.slice(0, 2).map((model) => `${{model.name}} (${{model.modelId}})`).join(' and ');
        if (window.openai && window.openai.sendFollowUpMessage) {{
          await window.openai.sendFollowUpMessage({{title: 'Compare benchmark leaders', prompt: `Use Empire benchmark evidence to compare ${{leaders}} for my project. Recheck current Artificial Analysis and OpenRouter data before recommending a route; do not dispatch a paid completion.`}});
        }} else {{ detail.textContent = `Compare ${{leaders}} in a Codex task; this surface cannot send a follow-up here.`; }}
      }});
      render();
    }})();
  </script>
</section>
'''
    if len(fragment.encode("utf-8")) > MAX_FRAGMENT_BYTES:
        raise BenchmarkError("Rendered benchmark fragment exceeds the 1 MB ceiling")
    if any(marker in fragment for marker in ("fetch(", "XMLHttpRequest", "WebSocket")):
        raise BenchmarkError("Rendered benchmark fragment attempted network access")
    return fragment


def add_source_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--aa-access", choices=("auto", "free", "pro"), default="auto")
    parser.add_argument("--aa-fixture", type=Path)
    parser.add_argument("--openrouter-fixture", type=Path)
    parser.add_argument("--no-openrouter", action="store_true")
    parser.add_argument("--profile", choices=tuple(PROFILE_WEIGHTS), default="agentic")
    parser.add_argument("--weight", action="append", default=[])
    parser.add_argument("--input-modality", action="append", default=[])
    parser.add_argument("--output-modality", action="append", default=[])
    parser.add_argument("--include-openai", action="store_true")
    parser.add_argument("--route-qualified-only", action="store_true")
    parser.add_argument("--top", type=int, default=8)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    rank = commands.add_parser("rank", help="Fetch and rank current models")
    add_source_arguments(rank)
    rank.add_argument("--view", choices=("json", "markdown"), default="json")
    rank.add_argument("--output", type=Path)
    render = commands.add_parser("render", help="Render ranked JSON as a Codex HTML fragment")
    render.add_argument("--input", type=Path, required=True)
    render.add_argument("--output", type=Path, required=True)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "rank":
            if args.top < 1 or args.top > MAX_TOP:
                raise BenchmarkError(f"--top must be between 1 and {MAX_TOP}")
            weights = parse_weights(args.profile, args.weight)
            aa, openrouter = fetch_sources(args)
            result = rank_models(
                aa,
                openrouter,
                profile=args.profile,
                weights=weights,
                required_input=args.input_modality or ["text"],
                required_output=args.output_modality or ["text"],
                include_openai=args.include_openai,
                route_qualified_only=args.route_qualified_only,
                top=args.top,
            )
            output = (
                markdown_view(result)
                if args.view == "markdown"
                else json.dumps(result, indent=2) + "\n"
            )
            if args.output:
                args.output.resolve().write_text(output, encoding="utf-8")
            else:
                sys.stdout.write(output)
            return 0
        payload = load_object(args.input.resolve())
        fragment = render_fragment(payload)
        args.output.resolve().write_text(fragment, encoding="utf-8")
        print(json.dumps({"status": "rendered", "path": str(args.output.resolve())}))
        return 0
    except (BenchmarkError, runtime.RouterError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
