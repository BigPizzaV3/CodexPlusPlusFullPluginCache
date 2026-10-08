# Library commands

Run Python 3 against `scripts/library.py` at the plugin root. The root is two directories above each bundled skill directory; do not hardcode a machine-specific installation path. Commands emit JSON. They make no network calls. Only `export` writes a file.

```sh
python3 <plugin-root>/scripts/library.py stats
python3 <plugin-root>/scripts/library.py search "bottleneck" --collection core --limit 6
python3 <plugin-root>/scripts/library.py search "accepted outcome" --collection catalog
python3 <plugin-root>/scripts/library.py search "valuation" --collection instruments
python3 <plugin-root>/scripts/library.py search "" --collection disciplines --discipline economics --limit 10
python3 <plugin-root>/scripts/library.py get core:137 concept:137 instrument:J
python3 <plugin-root>/scripts/library.py links BE-00-137
python3 <plugin-root>/scripts/library.py routes
python3 <plugin-root>/scripts/library.py routes geopolitics
python3 <plugin-root>/scripts/library.py practice routing
python3 <plugin-root>/scripts/library.py practice engine
python3 <plugin-root>/scripts/library.py practice quality
python3 <plugin-root>/scripts/library.py export atlas /absolute/output/Business-Engineer-Atlas.html
```

`search` supports `--collection catalog|core|disciplines|instruments|concepts|all`, `--discipline`, `--part`, `--kind`, `--limit` (1–50), and `--offset`. It returns `total` and `next_offset`; request another page only when needed. Shorten or broaden a query with no matches. It is lexical retrieval, not semantic search or an AI answer generator.

`get` takes one or more full IDs or explicit aliases (`core:137`, `concept:137`, `instrument:J`). Bare numbers produce a clear ambiguity error. Redirects retain the requested ID, canonical home, and the full reference context. Read the status and limits fields for earlier concepts.

`links` distinguishes directed source references, reverse citations, typed earlier-ontology relations, shared editorial threads, and title matches. Canonical references are returned separately. Do not interpret any link as causality unless the source actually makes that assertion.

`routes` returns twelve authored decision paths. `practice` returns one of `engine`, `modes`, `routing`, `quality`, or `spine`. Instruments are complete entries retrieved with `get`.

To find numeric core model 137, prefer `get core:137`. Searching a bare number searches text and does not resolve a namespace.

Python unavailable: use an available text/file search facility to locate the entry in `data/complete-library.md`, or inspect only the relevant portion of `data/library.json`. The HTML Atlas can open without Python. State any missing retrieval capability without inventing results.
