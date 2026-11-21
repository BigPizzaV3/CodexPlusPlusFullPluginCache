<!-- Generated from DESIGN.md by pnpm design:generate. Do not edit. -->
# Zatsu Diet GPT design guide

This guide is bundled with the MCP food-journal Skill. Browser CSS and fonts are not inherited by ChatGPT.

## Chart tokens

| Role | Value |
| --- | --- |
| background | `#FFF8F3` |
| text | `#2D2D2D` |
| normal | `#F4B400` |
| attention | `#EC6F51` |
| unknown | `#F3EEEA` |
| line | `#D9CEC7` |
| annotation | `#6F6762` |

Use `Noto Sans CJK JP` → `Noto Sans JP` → `Yu Gothic` → `sans-serif`, choosing the first installed Japanese-capable font. If none works, explain the constraint and use a text/table fallback rather than mojibake.

## Chart behavior

- Use golden yellow for normal known values and terracotta/coral only for a value strictly beyond the user's threshold. Purple is an AI accent or meal-category color, not a warning. Label every distinction; color alone is insufficient.
- Start quantitative axes at zero, retain units, and write important values directly. Keep one main chart per answer and reduce decorative axes, legends, and grid lines.
- Never turn missing or unknown nutrition into zero. Write 「記録なし」「一部不明」 or 「既知分の小計＋不明分」 as appropriate. Distinguish zero, unrecorded, estimated, and unknown.
- Use normal/attention fill for known estimates and qualify them with 「約」; reserve the unknown fill for missing values. Add 「記録した分の目安だよ」 below nutrition charts.
- Prefer a compact horizontal bar chart when mobile width makes labels cramped. Generated image layout remains model-dependent.

## Editorial tone

Friendly and non-judgmental: 「雑でOK」「記録した分の目安だよ」. Prefer 「記録上は少し高め」 over 「食べすぎ」 and 「まだ記録なし」 over 「記録を忘れています」. Do not imply complete daily intake or reinterpret a user threshold as a recommendation.
