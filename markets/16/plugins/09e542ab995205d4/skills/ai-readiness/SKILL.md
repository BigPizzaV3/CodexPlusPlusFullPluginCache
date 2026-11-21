---
name: "ai-readiness"
description: "Turn failed AI Readiness checks into exact website changes, in the order to make them."
---

# AI Readiness fixes

Use this guidance to turn the AI Readiness tab into a short list of website changes.

## Steps

1. Call `get_readiness` for the project and the scan in the request.
2. If `checked` is false, the scan has no check. Say that, and stop. Do not guess the state of the website.
3. Read `status`: `ready`, `not_verified`, or `blocked`. Read `apps_ready` of `apps_total`.
4. Read the five checks: search crawlers allowed, Gemini allowed, home page indexable, home page quotable, and text readable without JavaScript.
5. For each check that fails, copy its evidence and its change from the tool. Make the change exact for this website: name the file, the line, and the new text.
6. Put the changes in this order:
   1. `robots.txt` rules that block an AI app's search crawler. This is first because a blocked crawler cannot read any other fix.
   2. A home page that search engines cannot index.
   3. Text that needs JavaScript to appear.
   4. A home page that has little text to quote.

## Rules

- Use the evidence that the tool returns, such as "robots.txt line 277". Do not invent a rule that the tool does not show.
- `not_verified` means that a check did not run. It is not a failure. Say which check did not run, and do not give a fix for it.
- A search crawler and a training crawler are different. `OAI-SearchBot` lets ChatGPT search read the site. `GPTBot` collects training data. Whether to allow `GPTBot` is the owner's choice. Do not list it as a fix.
- Each AI app shows how many of its answers cite the site. Report the number with its counts. Do not say that a fix will raise it.
- The next scan checks the website again. Tell the person to read the tab after that scan.
- Link the `url` of the AI Readiness tab.

## Never suggest

- `llms.txt` files or "AI schema". Google states that its AI features need no new files and no special markup.
- A change to a file that you did not see evidence for.

## Output

A numbered list in the order above. For each item: the check, the evidence, the exact change, and who usually makes it (the person who manages the website or its host). If nothing fails, say that all checks passed and list the count of AI apps that can use the site.
