"""Regression checks for the Public Equity Investing deliverable framework."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from shared.dashboard.qa import validate_payload  # noqa: E402
from shared.dashboard.renderer import render_dashboard  # noqa: E402

DASHBOARD_SAMPLE_PAYLOADS = [
    "comps-valuation-sample.json",
    "initiating-coverage-sample.json",
    "idea-generation-sample.json",
    "portfolio-sizing-mode-sample.json",
    "scenario-sensitivity-sample.json",
    "portfolio-hedge-mode-sample.json",
    "deck-report-qc-sample.json",
    "hero-citations-sample.json",
    "production-complete-sample.json",
]


INTERNAL_SUPPORT_PLAYBOOKS = {
    "daloopa-provider-guide",
    "dashboard-builder",
    "excel-data-cleaner",
    "financial-source-of-truth",
    "quartr-provider-guide",
    "sector-context-overlay",
    "style-guide-adapter",
}
INTERNAL_SUPPORT_PATH = "skills/public-equity-investing/internal-support"


def read(relative_path: str | Path) -> str:
    path = Path(relative_path)
    if not path.is_absolute():
        path = ROOT / path
    return path.read_text(encoding="utf-8")


def load_json(relative_path: str) -> dict[str, object]:
    return json.loads(read(relative_path))


def minimal_dashboard_payload() -> dict[str, object]:
    return {
        "kind": "public_equity_investing_dashboard.v1",
        "title": "Issuer dashboard",
        "issuer": {"ticker": "ACME"},
        "tabs": [
            {
                "id": "overview",
                "label": "Overview",
                "modules": [
                    {"type": "decision_box", "data": {"stance": "Watch"}},
                ],
            }
        ],
        "sources": [{"id": "S1", "title": "Company release"}],
    }


def _payload_has_module(payload: dict[str, object], module_type: str) -> bool:
    tabs = payload.get("tabs")
    if not isinstance(tabs, list):
        return False
    for tab in tabs:
        if not isinstance(tab, dict):
            continue
        modules = tab.get("modules")
        if not isinstance(modules, list):
            continue
        for module in modules:
            if isinstance(module, dict) and module.get("type") == module_type:
                return True
    return False


class DeliverableFrameworkTests(unittest.TestCase):
    def test_implicit_invocation_is_limited_to_the_guarded_router(self) -> None:
        skill_names = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        yaml_paths = sorted((ROOT / "skills").glob("*/agents/openai.yaml"))
        self.assertEqual(skill_names, {path.parents[1].name for path in yaml_paths})
        for path in yaml_paths:
            skill = path.parents[1].name
            expected = skill == "public-equity-investing"
            with self.subTest(skill=skill):
                self.assertIn(
                    f"allow_implicit_invocation: {str(expected).lower()}",
                    read(path),
                )

    def test_internal_support_playbooks_are_packaged_but_not_visible_skills(self) -> None:
        visible = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}

        for skill in INTERNAL_SUPPORT_PLAYBOOKS:
            self.assertNotIn(skill, visible)
            self.assertTrue((ROOT / INTERNAL_SUPPORT_PATH / skill / "INTERNAL.md").exists())
            self.assertFalse((ROOT / "skills" / skill / "SKILL.md").exists())

    def test_dashboard_sample_payloads_validate_in_strict_mode(self) -> None:
        payload_dir = "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads"
        for filename in DASHBOARD_SAMPLE_PAYLOADS:
            relative_path = f"{payload_dir}/{filename}"
            payload = load_json(relative_path)
            report = validate_payload(payload)

            self.assertEqual("strict", payload["metadata"]["citation_policy"], relative_path)
            self.assertEqual("failed" if report["hard_failures"] else "passed", report["status"])
            self.assertEqual([], report["hard_failures"], f"{relative_path}: {report}")
            self.assertTrue(payload.get("sources"), relative_path)
            self.assertTrue(_payload_has_module(payload, "missing_evidence"), relative_path)

    def test_strict_financial_chart_requires_render_ready_rows(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/financial-trend-incomplete-sample.json"
        )

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "financial_trend_chart has fewer than 2 chart-ready rows" in failure
                and "add missing_evidence" in failure
                for failure in report["hard_failures"]
            ),
            report,
        )

    def test_non_strict_financial_chart_warns_on_incomplete_rows(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/financial-trend-incomplete-sample.json"
        )
        payload["metadata"]["citation_policy"] = "warn"
        payload["metadata"]["payload_stage"] = "draft"
        payload["metadata"]["readiness_posture"] = "working_draft"

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"])
        self.assertEqual([], report["hard_failures"])

    def test_production_profile_requires_complete_dashboard_contract(self) -> None:
        payload = minimal_dashboard_payload()

        report = validate_payload(payload, profile="production")
        failures = "\n".join(report["hard_failures"])

        self.assertEqual("failed", report["status"])
        for expected in [
            "payload.mode must be a non-empty string",
            "production dashboards must include layout",
            "production dashboards must include metadata",
            "production dashboards must include a non-empty hero",
            "production dashboards must include non-empty snapshot tiles",
        ]:
            self.assertIn(expected, failures)

    def test_production_profile_complete_fixture_passes(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/production-complete-sample.json"
        )

        report = validate_payload(payload, profile="production")

        self.assertEqual("passed", report["status"], report)
        self.assertEqual([], report["hard_failures"], report)

    def test_production_profile_fails_missing_source_ledger(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/production-missing-source-fails-sample.json"
        )

        report = validate_payload(payload, profile="production")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "strict dashboards must include a source ledger" in failure
                for failure in report["hard_failures"]
            ),
            report,
        )

    def test_production_profile_fails_unresolved_citation(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/production-unresolved-citation-fails-sample.json"
        )

        report = validate_payload(payload, profile="production")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any("unknown source id 'S99'" in failure for failure in report["hard_failures"]),
            report,
        )

    def test_warn_mode_support_payload_allows_source_and_numeric_gaps_as_warnings(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/draft-support-source-gap-sample.json"
        )

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"], report)
        self.assertEqual([], report["hard_failures"], report)
        self.assertTrue(
            any(
                "final dashboards should include a source ledger" in warning
                for warning in report["warnings"]
            )
        )
        self.assertTrue(
            any("numeric material without citations" in warning for warning in report["warnings"])
        )

    def test_warn_mode_support_payload_allows_incomplete_chart_as_warning(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/draft-incomplete-chart-support-sample.json"
        )

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"], report)
        self.assertEqual([], report["hard_failures"], report)
        self.assertTrue(
            any(
                "financial_trend_chart has fewer than 2 chart-ready rows" in warning
                for warning in report["warnings"]
            ),
            report,
        )

    def test_client_ready_posture_forces_production_validation(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {
            "payload_stage": "draft",
            "citation_policy": "warn",
            "readiness_posture": "client_ready",
            "readiness_label": "Client ready",
        }

        report = validate_payload(payload, profile="draft")
        failures = "\n".join(report["hard_failures"])

        self.assertEqual("failed", report["status"])
        self.assertIn(
            "production dashboards must set metadata.citation_policy to 'strict'", failures
        )
        self.assertIn("production dashboards must include a non-empty hero", failures)

    def test_dashboard_render_script_defaults_to_production_profile(self) -> None:
        payload = (
            ROOT
            / "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/draft-support-source-gap-sample.json"
        )
        script = (
            ROOT
            / "skills/public-equity-investing/internal-support/dashboard-builder/scripts/render_dashboard.py"
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            output = Path(tmp_dir) / "dashboard.html"

            default_result = subprocess.run(
                [sys.executable, str(script), str(payload), str(output)],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(0, default_result.returncode)
            self.assertIn("production dashboards must include layout", default_result.stderr)

            draft_result = subprocess.run(
                [sys.executable, str(script), str(payload), str(output), "--profile", "draft"],
                cwd=str(ROOT),
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(0, draft_result.returncode, draft_result.stderr + draft_result.stdout)
            self.assertTrue(output.exists())

    def test_render_dashboard_default_uses_production_validation(self) -> None:
        payload = minimal_dashboard_payload()

        with self.assertRaisesRegex(ValueError, "production dashboards must include layout"):
            render_dashboard(payload)

        html = render_dashboard(payload, validation_profile="draft")
        self.assertIn("Issuer dashboard", html)

    def test_dashboard_renders_reader_actions_bar_with_print_control(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/production-complete-sample.json"
        )

        html = render_dashboard(payload)

        self.assertIn("dashboard-utility-bar", html)
        self.assertIn("Reader actions", html)
        self.assertIn("Copy Full Report", html)
        self.assertIn("data-copy-full-report", html)
        self.assertIn("data-print-dashboard", html)
        self.assertIn("Print / Save PDF", html)
        self.assertIn("data-report-copy-root", html)
        self.assertNotIn("print-action", html)
        self.assertNotIn("Open workbook", html)
        self.assertNotIn("Copy executive summary", html)
        self.assertNotIn('<p class="eyebrow"></p>', html)

    def test_dashboard_css_uses_flat_light_surface(self) -> None:
        css = read("shared/dashboard/assets/dashboard.css")

        self.assertIn("--page: #ffffff;", css)
        self.assertIn("--surface-muted: #f8fafc;", css)
        self.assertIn("--data-accent:", css)
        self.assertIn("--status-positive:", css)
        self.assertIn("--narrative-width: 72ch;", css)
        self.assertIn("font-variant-numeric: tabular-nums lining-nums;", css)
        self.assertIn(".dense-table th", css)
        self.assertIn("min-height: 18px;", css)
        for elevated_effect in (
            "box-shadow",
            "linear-gradient",
            "radial-gradient",
            "backdrop-filter",
        ):
            self.assertNotIn(elevated_effect, css)

    def test_single_page_deduplicates_heading_and_aligns_numeric_columns(self) -> None:
        payload = minimal_dashboard_payload()
        payload["layout"] = "single_page"
        payload["tabs"][0]["modules"] = [
            {
                "type": "table",
                "title": "Overview",
                "data": {
                    "columns": [
                        "metric",
                        "revenue",
                        {"key": "delta", "label": "Change", "type": "percent"},
                    ],
                    "rows": [{"metric": "Revenue", "revenue": "$120M", "delta": "12%"}],
                },
            }
        ]

        html = render_dashboard(payload, validate=False)

        self.assertEqual(1, html.count("<h2>Overview</h2>"))
        self.assertIn('<th class="is-numeric">Revenue</th>', html)
        self.assertIn('<th class="is-numeric">Change</th>', html)
        self.assertIn('<td class="is-numeric" data-label="Revenue">', html)

    def test_dashboard_rejects_empty_scenario_cases(self) -> None:
        payload = minimal_dashboard_payload()
        payload["tabs"][0]["modules"] = [
            {"type": "scenario_map", "data": {"cases": [{"label": "Bull", "citations": ["S1"]}]}}
        ]

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any("omit empty scenario cards" in failure for failure in report["hard_failures"]),
            report,
        )

    def test_dashboard_renders_scenario_summary_fields(self) -> None:
        payload = minimal_dashboard_payload()
        payload["tabs"][0]["modules"] = [
            {
                "type": "scenario_map",
                "data": {
                    "cases": [
                        {
                            "label": "Bear",
                            "status": "bear",
                            "summary": "Underlying growth remains pressured.",
                            "citations": ["S1"],
                        }
                    ]
                },
            }
        ]

        html = render_dashboard(payload, validate=False)

        self.assertIn('<article class="scenario-card bear">', html)
        self.assertIn("Bear", html)
        self.assertIn("Underlying growth remains pressured.", html)

    def test_market_events_resolve_visible_source_from_citation_ledger(self) -> None:
        payload = minimal_dashboard_payload()
        payload["sources"] = [
            {"id": "S1", "title": "Company release", "url": "https://example.com/release"}
        ]
        payload["tabs"][0]["modules"] = [
            {
                "type": "market_events",
                "data": {
                    "events": [
                        {
                            "date": "May 27, 2026",
                            "event": "Fiscal Q1 results",
                            "impact": "Updated growth debate",
                            "investor_read": "Monitor forward guidance",
                            "citations": ["S1"],
                        }
                    ]
                },
            }
        ]

        html = render_dashboard(payload, validate=False)

        self.assertIn("Company release", html)
        self.assertIn("https://example.com/release", html)
        self.assertNotIn('data-label="Source">Not sourced', html)

    def test_strict_complete_financial_chart_passes(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload["tabs"][0]["modules"] = [
            {
                "type": "financial_trend_chart",
                "data": {
                    "periods": [
                        {
                            "period": "Q1 FY2026",
                            "revenue": "100",
                            "gross_profit": "60",
                            "net_income": "20",
                            "net_margin": "20%",
                            "citations": ["S1"],
                        },
                        {
                            "period": "Q2 FY2026",
                            "revenue": "110",
                            "gross_profit": "66",
                            "net_income": "22",
                            "net_margin": "20%",
                            "citations": ["S1"],
                        },
                    ]
                },
            }
        ]

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"])
        self.assertEqual([], report["hard_failures"])

    def test_strict_incomplete_chart_intent_passes_when_chart_is_omitted(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload["tabs"][0]["modules"] = [
            {"type": "decision_box", "data": {"stance": "Watch", "citations": ["S1"]}},
            {
                "type": "missing_evidence",
                "data": {
                    "items": [
                        "Financial trend chart omitted because revenue, gross profit, net income, and margin history are incomplete."
                    ]
                },
            },
        ]

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"])
        self.assertEqual([], report["hard_failures"])

    def test_chart_readiness_covers_eps_and_price_event_charts(self) -> None:
        cases = [
            (
                "eps_actual_vs_estimate_chart",
                {
                    "periods": [
                        {
                            "period": "Q1",
                            "estimated_eps": "1.00",
                            "actual_eps": "1.10",
                            "citations": ["S1"],
                        },
                        {
                            "period": "Q2",
                            "estimated_eps": "1.20",
                            "actual_eps": "",
                            "citations": ["S1"],
                        },
                    ]
                },
                "fewer than 2 chart-ready rows",
            ),
            (
                "equity_price_event_chart",
                {
                    "prices": [
                        {"date": "2026-01-01", "price": "10.00", "citations": ["S1"]},
                        {"date": "2026-01-02", "price": "", "citations": ["S1"]},
                    ],
                    "events": [{"date": "2026-01-01", "event": "Launch", "citations": ["S1"]}],
                },
                "needs at least 10 daily chart-ready price rows; got 1",
            ),
        ]

        for module_type, data, expected in cases:
            payload = minimal_dashboard_payload()
            payload["metadata"] = {"citation_policy": "strict"}
            payload["tabs"][0]["modules"] = [{"type": module_type, "data": data}]

            report = validate_payload(payload, profile="draft")

            self.assertEqual("failed", report["status"], module_type)
            self.assertTrue(
                any(expected in failure for failure in report["hard_failures"]),
                f"{module_type}: {report}",
            )

    def test_price_event_chart_rejects_three_point_daily_reaction_tape(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload["tabs"][0]["modules"] = [
            {
                "type": "equity_price_event_chart",
                "data": {
                    "price_granularity": "daily",
                    "prices": [
                        {"date": "2026-04-30", "price": 384.94, "citations": ["S1"]},
                        {"date": "2026-05-13", "price": 402.62, "citations": ["S1"]},
                        {"date": "2026-05-19", "price": 399.00, "citations": ["S1"]},
                    ],
                    "events": [
                        {
                            "date": "2026-04-30",
                            "event": "Post-print close",
                            "citations": ["S1"],
                        }
                    ],
                },
            }
        ]

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "needs at least 10 daily chart-ready price rows; got 3" in failure
                for failure in report["hard_failures"]
            ),
            report,
        )

    def test_price_event_chart_accepts_substantive_daily_reaction_tape(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload["tabs"][0]["modules"] = [
            {
                "type": "equity_price_event_chart",
                "data": {
                    "price_granularity": "daily",
                    "prices": [
                        {"date": f"2026-01-{day:02d}", "price": 100 + day, "citations": ["S1"]}
                        for day in range(1, 11)
                    ],
                    "events": [
                        {"date": "2026-01-05", "event": "Earnings print", "citations": ["S1"]}
                    ],
                },
            }
        ]

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"])
        self.assertEqual([], report["hard_failures"])

    def test_renderer_omits_thin_price_event_chart_when_validation_is_bypassed(self) -> None:
        payload = minimal_dashboard_payload()
        payload["tabs"][0]["modules"] = [
            {
                "type": "equity_price_event_chart",
                "title": "Thin Price Tape",
                "data": {
                    "prices": [{"date": "2026-04-30", "price": 100, "citations": ["S1"]}],
                    "events": [{"date": "2026-04-30", "event": "Earnings", "citations": ["S1"]}],
                },
            }
        ]

        html = render_dashboard(payload, validate=False)

        self.assertNotIn("Thin Price Tape", html)
        self.assertNotIn("price-event-chart", html)

    def test_hero_dek_and_callout_render_citation_links(self) -> None:
        payload = load_json(
            "skills/public-equity-investing/internal-support/dashboard-builder/assets/example_payloads/hero-citations-sample.json"
        )

        html = render_dashboard(payload)

        dek_index = html.index("The hero dek should append a source chip")
        dek_chip_index = html.find("citation-chip", dek_index)
        self.assertGreater(dek_chip_index, dek_index)
        self.assertLess(dek_chip_index, dek_index + 600)

        callout_index = html.index("Revenue grew")
        numeric_link_index = html.find('class="citation-link"', callout_index)
        linked_number_index = html.find("24.5%", callout_index)
        self.assertGreater(numeric_link_index, callout_index)
        self.assertLess(numeric_link_index, callout_index + 600)
        self.assertGreater(linked_number_index, numeric_link_index)
        self.assertLess(linked_number_index, numeric_link_index + 200)

    def test_strict_dashboard_requires_source_ledger(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload["sources"] = []

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "strict dashboards must include a source ledger" in failure
                for failure in report["hard_failures"]
            )
        )
        self.assertFalse(any("source ledger" in warning for warning in report["warnings"]))

    def test_strict_dashboard_missing_sources_requires_source_ledger(self) -> None:
        payload = minimal_dashboard_payload()
        payload["metadata"] = {"citation_policy": "strict"}
        payload.pop("sources")

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "strict dashboards must include a source ledger" in failure
                for failure in report["hard_failures"]
            )
        )

    def test_top_level_strict_dashboard_requires_source_ledger(self) -> None:
        payload = minimal_dashboard_payload()
        payload["citation_policy"] = "strict"
        payload["sources"] = []

        report = validate_payload(payload, profile="draft")

        self.assertEqual("failed", report["status"])
        self.assertTrue(
            any(
                "strict dashboards must include a source ledger" in failure
                for failure in report["hard_failures"]
            )
        )

    def test_non_strict_dashboard_warns_on_missing_source_ledger(self) -> None:
        payload = minimal_dashboard_payload()
        payload["sources"] = []

        report = validate_payload(payload, profile="draft")

        self.assertEqual("passed", report["status"])
        self.assertTrue(
            any(
                "final dashboards should include a source ledger" in warning
                for warning in report["warnings"]
            )
        )
        self.assertEqual([], report["hard_failures"])


if __name__ == "__main__":
    unittest.main()
