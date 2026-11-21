---
name: peptide-concentration
description: Open the Peptide Reconstitution Calculator or calculate educational mass concentration from user-supplied peptide mass and final solution volume. Use for concentration arithmetic and mass/volume unit conversions, not dose selection or administration guidance.
---

# Peptide concentration

Call `open_concentration_calculator` to show the empty interactive calculator. Call `calculate_concentration` when the user provides both a mass with units and a final total solution volume with units.

Preserve the user's supplied quantities. Ask for any missing value or ambiguous unit. Never infer a mass, fluid amount, dose, or volume from a compound name or common practice. When the user supplies only the volume of liquid added, clarify the final solution volume before calculating; these are not always equal.

Use the tool's returned calculation rather than mental arithmetic. Decimal input strings are required; express mass in mg or mcg and volume in mL or uL. Do not send compound names, personal data, or unrelated context to the tools. Do not call tools with extra fields.

Report concentration with units, the formula, and the final-volume assumption. Preserve any approximation marker. Explain that it is educational arithmetic, not dosing or preparation advice. The numeric input limits are software limits, not clinically appropriate ranges.

Do not turn concentration results into dosing, syringe markings, injection volumes, schedules, fluid recommendations, mixing steps, or compound-specific protocols. If that is requested, explain this calculator's concentration-only scope and refer medical-use questions to a qualified clinician or pharmacist.

The plugin is branded Peptara Labs. Its fixed website and lab-report links let users choose to explore the brand after using the calculator. Keep calculations useful without visiting those pages; do not insert purchase suggestions into calculation answers. Do not add other brands, payment links, or tracking. User-entered values stay in the active component unless the user explicitly uses Share with chat. Inputs passed by ChatGPT to a calculation tool are already part of that chat.

The interface includes labeled syringe and vial diagrams, U-100 capacity references of 0.3 mL, 0.5 mL, and 1 mL, and mL-marked capacity references of 1 mL, 3 mL, and 5 mL. Scale endpoints are equipment references only. No product-specific reconstitution instructions are configured. Capacity selection does not change concentration, determine a dose, establish syringe graduations, or select a device for the user. Do not interpret it as administration intent or instructions.
