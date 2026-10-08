#!/usr/bin/env python3
"""Initialize an empty research run without overwriting files. Python 3.10+."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def create_run(destination, industry, universe=None, horizon=None):
    destination = Path(destination).expanduser().resolve()
    if not isinstance(industry, str) or not industry.strip():
        raise ValueError("industry must be nonempty")
    if destination == PLUGIN_ROOT or PLUGIN_ROOT in destination.parents:
        raise ValueError("Research runs must be outside the plugin installation")
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing path: {destination}")
    if horizon is not None and (type(horizon) not in (int, float) or not 0 < horizon <= 100):
        raise ValueError("horizon must be between 0 and 100 years")
    if universe is not None and (not isinstance(universe, str) or not universe.strip()):
        raise ValueError("universe must be nonempty")
    config = json.loads((PLUGIN_ROOT / "config/defaults.json").read_text(encoding="utf-8"))
    config.update(industry=industry.strip(), created_at=datetime.now(timezone.utc).isoformat(),
                  plugin_version=json.loads((PLUGIN_ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))["version"])
    if universe is not None:
        config["universe"] = universe.strip()
    if horizon is not None:
        config["horizon_years"] = horizon
        config["horizon_sensitivity_years"] = []
    # Read templates before creating anything, so a damaged installation fails cleanly.
    template_files = sorted((PLUGIN_ROOT / "templates").glob("*"))
    if not template_files:
        raise ValueError("No run templates found")
    content = {p.name: p.read_text(encoding="utf-8") for p in template_files if p.is_file()}
    destination.mkdir(parents=True, exist_ok=False)
    (destination / "briefs").mkdir()
    (destination / "mandate.json").write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for name, body in content.items():
        (destination / name).write_text(body, encoding="utf-8")
    (destination / "checkpoint.md").write_text(
        "# Research checkpoint\n\nStage: mandate and plan.\n"
        "Completed: empty run initialized.\n"
        "Next: resolve benchmark, as-of snapshot, assignments and plan; then execute.\n"
        "Evidence: none collected. No ranking or model has been created.\n",
        encoding="utf-8")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="New run directory outside the plugin; must not exist")
    parser.add_argument("--industry", required=True)
    parser.add_argument("--universe")
    parser.add_argument("--horizon", type=float, help="Optional central horizon; review sensitivity horizons in mandate.json")
    args = parser.parse_args()
    try:
        result = create_run(args.output, args.industry, args.universe, args.horizon)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"Unable to initialize run: {exc}\n")
    print(result)


if __name__ == "__main__":
    main()
