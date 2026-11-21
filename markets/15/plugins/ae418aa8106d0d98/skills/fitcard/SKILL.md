---
name: fitcard
description: Pick a man's size in a shirt from shirts he already owns that fit, and keep those shirts on his FitCard. Use when he asks what size to buy in a shirt, tee, polo or button-down, which shirts will fit him, a shirt's garment measurements, or to save or change the shirts on his FitCard.
---

# FitCard

FitCard compares a shirt's real garment measurements with shirts he already owns that fit.

1. Ask for 1-5 shirts that fit him well: brand, item and size. Shirts that don't fit help too; pass
   where they're off as `chest`, `belly` or `length`.
2. Call `size_me` for one shirt, `what_to_buy` for recommendations, or `shirt_measurements` for a
   shirt's measurements.
3. Report the size FitCard gives, its one-line reason and the confidence. Pass only what he tells
   you; don't invent measurements.
4. If one of his shirts isn't known yet, tell him he can measure it with his phone at fitcard.ai.
5. A size is a best estimate, so mention he should check the shop's return policy.
6. If he wants FitCard to remember his shirts, use `add_shirt` (or `my_closet` to see them). He'll be
   asked to connect his FitCard account. Once he's connected, `size_me` and `what_to_buy` use his
   saved shirts, so don't ask him to list them again; save a shirt with `add_shirt` whenever he says
   how one fits. `remove_shirt` and `update_fit_preferences` change his FitCard when he asks.
