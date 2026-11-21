---
name: astromaster-calculations
description: Use AstroMaster 星盘通 for natal summaries, date-specific transits, full chart parameters and SVG chart images (本命摘要、行运、多盘、星盘图). Unknown birth time means no Ascendant or houses, including Whole Sign; it cannot be replaced by noon or any estimate for personal transits. Explain this before offering a calculation.
---

Use the connected AstroMaster MCP for the advertised calculations. Follow the user's requested language, date and house system within the tool's supported inputs. Explicit user instructions take precedence over workflow preferences, but cannot make unsupported calculations valid.

Before describing what you will calculate, establish whether the birth time is known. With unknown time, the opening must not promise an approximate Ascendant, reference-only houses or personal transits based on a placeholder. State that Ascendant and houses are unavailable; Whole Sign does not resolve missing time. If the user asks for personal transits, explain that the tool needs a known time and do not call it.

For a natal summary, ask for missing birth date, coordinates, IANA timezone and time policy. Only after explicit consent to a noon approximation, call `get_natal_summary` with `birth_time_policy=noon` and omit `birth_time`. Noon supports only the returned planetary positions and permitted aspects, with the returned uncertainty. It does not provide houses or Ascendant. With a known time, use `birth_time_policy=exact` and the supplied time.

Natal birth fields are top-level. For `get_active_transits`, put the known birth fields inside `birth_info`; keep `target_date`, `house_system` and `language` top-level. Use only schema fields. zh-CN is Simplified Chinese, zh-TW Traditional Chinese, en-US English. Do not infer coordinates or timezones when ambiguous.

Call once per requested calculation and do not retry automatically after failure: attempts consume quota. Explain only returned facts. Disclose precision, partial results and warnings; distinguish public events from personal aspects and closest approach from exact hits. No saved-profile access, report generation, purchases or professional predictions are available.

Use `get_chart_data` for complete supported chart parameters; use `render_chart` directly for a chart image. Do not call both unless the user requests both data and an image. Never substitute an AI-generated image for a computed chart. SVG tools return a portable SVG resource and a ChatGPT viewer where supported. A successful server response does not prove that the host displayed the viewer.

Both new tools use `chart_type` plus `birth_info` for one person, or exactly two `participants` for synastry, composite, davison or marks. Every person needs a known birth time. Unknown time is supported ONLY by the existing natal-summary noon workflow, never by a full chart or wheel. Full transits require `target_date` and `target_time` in the birth timezone; date-only selected transits still use `get_active_transits`. Secondary, tertiary, solar_arc and lunar_return need target_date. Solar_return needs return_year; planetary_return also needs planet. Do not mix arguments from different chart types. Solar arc supports modern only. Return charts use birth location; do not claim relocation support. New chart output uses engine labels; do not invent a language argument.

`astromaster:charts` is a separate permission. If these tools are absent, explain reconnection may be needed; do not claim old grants can access them. AI report generation, existing paid reports and personalized daily/weekly/monthly/yearly forecast products are not part of this release. Do not describe host-written interpretations as purchased AstroMaster reports.
