---
name: get-started
description: Use this when the user wants a public website checked for accessibility issues ("check https://example.com for wcag accessibility issues", "Ist unsere Website barrierefrei nach BFSG?", "barrierefreiheit prüfen", "ready for the European Accessibility Act?") or rescanned after fixes. The tool loads the page in a real browser and returns the actual WCAG 2.2 failures with the affected elements and fixes.
---

1. Ask only for what is missing: the public URL of the page to check. If they want "the whole site", use `maxPages` 3 to 5 (the URL plus pages linked from it).
2. Call `check_accessibility`. If a page could not be checked (bot protection, timeout, private address), say why and suggest the free axe DevTools or WAVE browser extension for that page.
3. Lead with the three most important fixes in plain words, in the user's language: what is wrong, where (selector or example), and how to fix it. Then the counts by severity.
4. Always mention the manual checks (keyboard, alt-text quality, forms, captions, zoom), and that automated checks find only part of all issues.
5. Never say the site is compliant, certified or safe from complaints or lawsuits. The report is not a legal conformity assessment. Do not recommend overlay widgets as a fix.
6. When the user has fixed things and asks to rescan, call the tool again with `compareWith` set to the `compareKey` from the earlier result, and summarise what was fixed, what is new and what changed.
7. Pages behind a login, localhost, intranets, PDFs and mobile apps cannot be checked. Say so instead of guessing.
