#!/usr/bin/env python3
"""Guard against GATHER_MCP_GUIDE.md drifting from the actual Gather MCP tool surface.

Parses the tool table in GATHER_MCP_GUIDE.md's "Available MCP Tools" section (tool names
and the param names listed in its "Params" column) and diffs that against the mock
server's TOOLS registry (tests/harness/mock_gather_server.py) - the local source of truth
this repo's tests exercise against. Reports names present in one but not the other, and
param names present in one but not the other for tools both sides know about.

Optional --live: if GATHER_MCP_TOKEN is set, also fetches tools/list from the real Gather
MCP endpoint over HTTP and diffs that too. Degrades gracefully (prints a note, does not
fail the run) when no token is set or the request fails - this flag is for opportunistic
local/CI use, not a hard dependency.

Exit 0: no drift. Exit 1: drift found (message says exactly what and where).
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE_PATH = ROOT / "GATHER_MCP_GUIDE.md"
MOCK_PATH = ROOT / "tests" / "harness" / "mock_gather_server.py"
LIVE_URL = "https://app.gatherinsights.com/public/api/v1/mcp"

# Words that show up in the guide's Params column prose but are never real param names.
_PARAM_NOISE = {
    "project", "workspace", "shift", "record", "asset", "or", "not", "a", "an", "the",
    "only", "ISO", "8601", "YYYY-MM-DD", "≤100", "≤25", "params",
}


def parse_guide_tools(text: str) -> dict[str, set[str]]:
    """Extract {tool_name: {param_names}} from the guide's tool table.

    Table rows look like:
      | 1 | `getProjects` | `limit`≤100, `page`, `search`, `tags`, `modifiedSince` (...) | ... |
    """
    tools: dict[str, set[str]] = {}
    in_table = False
    for line in text.splitlines():
        if line.startswith("| #") and "Tool" in line and "Params" in line:
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 3:
                continue
            if set(cells[0]) <= {"-", " "}:
                continue  # markdown header separator row
            name_match = re.search(r"`(\w+)`", cells[1])
            if not name_match:
                continue
            name = name_match.group(1)
            params_cell = cells[2]
            params = set()
            for m in re.finditer(r"`([a-zA-Z][a-zA-Z0-9]*)`", params_cell):
                p = m.group(1)
                if p not in _PARAM_NOISE and p != name:
                    params.add(p)
            tools[name] = params
    return tools


def _top_level_keys(blob: str) -> set[str]:
    """Given the inside of a JSON-ish `properties: { ... }` object, return only the keys
    at nesting depth 0 (so a nested-array param's own `items.properties` sub-fields, e.g.
    getProjects' nested filter fields, are not mistaken for top-level params)."""
    keys = set()
    depth = 0
    i = 0
    n = len(blob)
    while i < n:
        ch = blob[i]
        if depth == 0:
            m = re.match(r'"(\w+)":\s*\{', blob[i:])
            if m:
                keys.add(m.group(1))
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        i += 1
    return keys


def parse_mock_tools(text: str) -> dict[str, set[str]]:
    """Extract {tool_name: {param_names}} from mock_gather_server.py's TOOLS list via AST-free
    regex parsing: each tool entry has a "name" and an inputSchema.properties dict. Only
    depth-0 keys of that dict count as params - nested schema (array item shapes) is not
    flattened into the tool's own param list."""
    tools: dict[str, set[str]] = {}
    for m in re.finditer(r'\{"name":\s*"(\w+)"', text):
        name = m.group(1)
        start = text.find('"properties":', m.end())
        if start == -1:
            continue
        brace_start = text.find("{", start)
        depth = 0
        j = brace_start
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        props_blob = text[brace_start + 1:j]
        tools[name] = _top_level_keys(props_blob)
    return tools


def diff_report(label_a: str, a: dict[str, set[str]], label_b: str, b: dict[str, set[str]]) -> list[str]:
    problems = []
    names_a, names_b = set(a), set(b)
    only_a = names_a - names_b
    only_b = names_b - names_a
    if only_a:
        problems.append(f"tools in {label_a} but not {label_b}: {sorted(only_a)}")
    if only_b:
        problems.append(f"tools in {label_b} but not {label_a}: {sorted(only_a) and sorted(only_b) or sorted(only_b)}")
    for name in sorted(names_a & names_b):
        pa, pb = a[name], b[name]
        only_pa = pa - pb
        only_pb = pb - pa
        if only_pa:
            problems.append(f"{name}: params in {label_a} but not {label_b}: {sorted(only_pa)}")
        if only_pb:
            problems.append(f"{name}: params in {label_b} but not {label_a}: {sorted(only_pb)}")
    return problems


def fetch_live_tools(token: str) -> dict[str, set[str]] | None:
    req_body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {},
    }).encode("utf-8")
    req = urllib.request.Request(
        LIVE_URL, data=req_body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            payload = json.loads(resp.read())
    except Exception as e:  # noqa: BLE001 - any network/parse failure degrades gracefully
        print(f"note: --live fetch failed, skipping live diff ({e})")
        return None
    tools = payload.get("result", {}).get("tools", [])
    out: dict[str, set[str]] = {}
    for t in tools:
        props = t.get("inputSchema", {}).get("properties", {})
        out[t["name"]] = set(props.keys())
    return out


def main() -> int:
    live = "--live" in sys.argv

    guide_tools = parse_guide_tools(GUIDE_PATH.read_text(encoding="utf-8"))
    mock_tools = parse_mock_tools(MOCK_PATH.read_text(encoding="utf-8"))

    if not guide_tools:
        print(f"error: found no tool table rows in {GUIDE_PATH}")
        return 1
    if not mock_tools:
        print(f"error: found no TOOLS entries in {MOCK_PATH}")
        return 1

    problems = diff_report("GATHER_MCP_GUIDE.md", guide_tools, "mock_gather_server.py", mock_tools)

    if live:
        token = os.environ.get("GATHER_MCP_TOKEN")
        if not token:
            print("note: --live passed but GATHER_MCP_TOKEN not set, skipping live diff")
        else:
            live_tools = fetch_live_tools(token)
            if live_tools is not None:
                problems += diff_report("GATHER_MCP_GUIDE.md", guide_tools, "live tools/list", live_tools)

    if problems:
        print(f"MCP guide drift detected ({len(problems)} issue(s)):")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"No drift: {len(guide_tools)} tools match between GATHER_MCP_GUIDE.md and mock_gather_server.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
