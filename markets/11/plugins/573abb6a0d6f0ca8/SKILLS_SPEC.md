# Skills specification

`skills/sigrank-analyst/SKILL.md` is the single routed analyst skill; its references implement the intended understand, interpret, compare, movement and communication behaviors without duplicating canon. `skills/beta-troubleshooter/SKILL.md` drafts and redacts a report and calls `report_beta_bug` only after explicit approval.

| User intent | Skill behavior |
|---|---|
| Understand SigRank | Explain I/O/W/R, Yield, Leverage, Velocity, Construction, SNR, evidence and limits without a live tool call for stable definitions. |
| Teach the operating ratio | Explain the returned `R/I : 1 : O/I` as cache-read : fresh-input : output, read it in concrete token terms, relate it to Leverage and Velocity, and explain W separately through Construction. Never treat the rounded string as exact inputs. |
| Analyze telemetry and articles | Analyze only returned public aggregate I/O/W/R or explicitly supplied aggregate counts; distinguish them from private session logs. Use current SignalAF methodology and dated articles for explanatory insight with source, cohort and superseded-archetype caveats. |
| Interpret operator | Call `get_operator` for an existing public codename; lead with the distinctive relationship, relevant field context and specific claim limit. The public tool currently returns `archetype: null`; derive a current-rule Build Archetype only from complete I/O/W/R, label it derived, and withhold it if any axis is missing. |
| Compare operators | Keep the first named operator as the anchor. Contrast a second returned codename and the matching Active field distribution along the most informative axes; use homepage four-degree averages only as separately sourced context. Keep windows/populations aligned; qualify returned board-value deltas when observation dates differ. |
| My public profile in Codex | Read the local identity through `scripts/resolve-local-profile.mjs`, use only the returned codename with public `get_operator`; ask for a codename if absent. ChatGPT asks for one directly. |
| Communicate/share | Keep one finding consistent in plain English, technical explanation, unusual-finding analysis, LinkedIn, X, and share-card headline/copy. Reuse actual SignalAF URLs/cards. |
| Default board overview | Make one explicit `get_leaderboard(window=all, view=total)` call for the Active / Total / All-time board; fetch other windows only when requested. Keep seeded archive data separate and dated. |
| Guided token-count preview (beta only) | On an explicit user request, ask for aggregate I/O/W/R, platform and period; calculate supported ratios with visible formulas and null handling. A board-position illustration is hypothetical and requires complete comparable row coverage. This is not an advertised launch calculator or verified measurement. Never scan or submit. |
| Measure SigRank | Deferred to existing Tokenpull/Upsilon systems; this plugin never scans logs or submits counts. |

Skills interpret and communicate. MCP tools provide authoritative facts. A skill cannot make an unavailable historical comparison or verification class real.
