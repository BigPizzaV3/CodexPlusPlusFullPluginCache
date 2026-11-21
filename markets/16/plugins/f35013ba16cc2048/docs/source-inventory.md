# Source inventory and adaptation notes

Checked 2026-10-09 against the public `main` branch of `morluto/rea`.

| Source | Use in this companion |
| --- | --- |
| `README.md` | Project purpose, supported target families, local execution, setup prerequisites, evidence limitations, model-provider boundary |
| `skill-src/reverse-engineer-anything/SKILL.md` | Target routing, avoid setup on every run, inspect advertised tools, summary-first workflows, preserve evidence and limitations |
| `SECURITY.md` | Local provider/session boundaries, not-a-sandbox warning, untrusted-binary risks, configuration approval, private vulnerability reporting |
| `LICENSE` | MIT attribution and reproduction of upstream notice |
| `package.json` | npm package name/version and Node engine prerequisites, checked only as source metadata |

The repo states `rea-agents` currently requires Node.js 22.19+, 24.11+, or 26+, plus npm. Tool availability and provider support vary by host and release; always inspect the connected server's live tool catalog and the installed version rather than assuming the repository's current `main` documentation matches the user's installation.

The companion intentionally does not reproduce REA's implementation, MCP schemas, binaries, tool catalog, or provider bridges. It is an original workflow guide that points to upstream documentation for changing details.
