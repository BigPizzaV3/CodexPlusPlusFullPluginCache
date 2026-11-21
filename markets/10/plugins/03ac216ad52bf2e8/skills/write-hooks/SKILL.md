---
name: write-hooks
description: Write new opening lines (hooks) for a user's ad, Reel or UGC video, grounded in real examples from the Hookest library. Use when the user asks for hook ideas, ad openers, first lines or scroll-stoppers for their product.
---

# Writing hooks with Hookest

Goal: hand the user a short list of hooks they can film today, each one tied to
a real pattern from the library rather than generic advice.

## Steps

1. **Understand the brief.** You need the product, the audience and the
   language of the video. Ask only for what is missing, in one question.

2. **Ground it in real examples.** If you have not done it yet in this
   conversation, run the `hook-research` steps first (`list_filters`, then
   `find_hooks`). Pick 3 strong examples to write from.

3. **Write the hooks yourself.** Write 5 to 8 hooks. For each one:
   - the hook line itself, short enough to say in about 3 seconds
   - one line on which library example or angle it borrows from
   - a suggested first on-screen visual

4. **Check the length.** Run `score_hook_text` on each draft and drop or trim
   any that take too long to say. Only score text you or the user wrote, never
   a library caption.

5. **Optional: Hookest's generator.** `generate_hooks` writes hooks on
   Hookest's side, but it uses the user's daily generation quota. Do not call
   it unless the user asks for it or agrees when you offer. Call `get_account`
   first if you are unsure how much quota is left. Never quote prices; if a
   limit is hit, tell the user when it resets.

## Output

A numbered list of hooks with the notes above, the 3 source examples with their
Hookest links, and one line suggesting which hook to test first and why.
