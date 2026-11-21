---
name: bulk-operations
description: Safely performs bulk CrumbPass restaurant menu price and availability changes. Use when an owner asks to increase or decrease prices across a category or set of dishes, or mark multiple dishes available or unavailable.
---

# Bulk operations

1. Read `get_menu` first. Match the owner's request to exact category and dish names; clarify any ambiguity.
2. For price changes, call `adjust_menu_prices` without `confirm`. It returns every affected old and new price without changing the menu.
3. Present the full change list and currency to the owner. Ask for explicit approval.
4. Re-call `adjust_menu_prices` with exactly the approved targeting and `confirm: true`.
5. For availability changes, state the exact dishes affected from `get_menu`, obtain explicit approval, then call `set_menu_availability` with `confirm: true`.

## Guardrails

- Do not silently round prices; explain the requested rounding rule before applying it.
- Do not use an empty category or guessed dish name.
- If the owner asks to change “everything,” show the scope and ask them to confirm the full list first.
