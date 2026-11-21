---
name: reel-checkup
description: Check a reel against Buzzfy's research on what makes reels perform. Use when the user asks why a reel flopped or worked, wants feedback on a posted reel, or wants a reel idea, opening line or caption checked before posting.
---

# Reel checkup

Buzzfy's tools return numbers and the playbook's rules, not a verdict. You make the judgment, and show which number or rule it rests on.

## A reel that is already posted

1. Find it with `ig_posts` (`kind: "reels"`) if the user didn't give an id or link.
2. Call `ig_reel_checkup` with its id. For each reel it returns the skip rate, shares and saves per 100 likes against the playbook's typical and breakout levels, views as a multiple of the creator's normal, and the fix-it step the numbers point to.
3. Call `buzzfy_playbook` for the topic that step points to: `openings` for step 1, `shares_and_saves` for the payoff, `captions` for step 5.
4. Answer in this order: the verdict in one sentence, the two numbers that matter most compared with the creator's normal, then one or two changes to make next time, each tied to a playbook rule.

The checkup cannot see the video. For anything that needs eyes on it (talking without captions, a slow first second, a montage), ask the user to describe the opening or paste the script.

## An idea, opening line or caption before posting

1. Call `buzzfy_playbook` with `openings` for an opening line, `captions` for a caption, or `checklists` for the 60-second pre-post check.
2. For opening alternatives, call it with `swipe_file` and write three rewrites in the creator's voice, each labelled with its family.
3. Judge the draft against the rules you fetched and say which rule each point comes from.

If the user has posted reels before, `ig_reel_checkup` with no ids gives their normal and any hot streak, which makes the advice specific to them.
