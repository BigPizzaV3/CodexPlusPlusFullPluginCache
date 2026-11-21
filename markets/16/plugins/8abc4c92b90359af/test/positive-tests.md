# Positive Test Cases

These are acceptance scenarios. The automated core checks are in `mcp-server/core.test.js`; the full conversational behavior still requires testing in the target ChatGPT/plugin host.

## PT-01 — Complete product brief
- **Input:** Brand/product, clear USP, target audience, narration preference, wardrobe, location, language, and product details are supplied.
- **Steps:** Start the workflow and submit the brief.
- **Expected:** AI acknowledges supplied facts without repeating them, analyzes product/audience, and proceeds to a coherent three-scene concept.
- **Pass evidence:** No unsupported claims; brief validation returns concept-ready.

## PT-02 — Brief with optional fields absent
- **Input:** Brand/product, USP, target audience, and language supplied; no wardrobe, location, or photos.
- **Steps:** Submit the brief.
- **Expected:** AI asks only useful follow-up questions, may propose a fictional talent and setting, and clearly marks them as creative choices.
- **Pass evidence:** No claim that missing photos were received; no fabricated product facts.

## PT-03 — Character and product reference assets
- **Input:** User supplies a character reference and a product reference.
- **Steps:** Ask for the full three-scene production package.
- **Expected:** Prompts instruct image/video models to preserve visible character and product details across all scenes.
- **Pass evidence:** Reference status is represented accurately; character/product locks remain consistent.

## PT-04 — Language and narration control
- **Input:** Indonesian with light Sundanese flavor; narration enabled. Repeat with narration disabled.
- **Steps:** Generate both variants.
- **Expected:** Natural, audience-appropriate Indonesian/Sundanese narration in the first run; no spoken narration in the second.
- **Pass evidence:** No unrequested language switch; narration toggle respected.

## PT-05 — Three-scene continuity
- **Input:** 30-second vertical affiliate video request.
- **Steps:** Generate final package and validate structure.
- **Expected:** Exactly three storyboard prompts (each 2×3/six panels), three ten-second video prompts, scene handoffs, continuity locks, negative prompt, story summary, and checklist.
- **Pass evidence:** MCP output validator returns valid for a correctly structured package; manual host review confirms scene handoffs.
