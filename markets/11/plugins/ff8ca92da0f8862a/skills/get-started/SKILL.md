---
name: get-started
description: Set a person up on HyperOrbs after they connect it. Checks where their account is, then either sets up their workspace, profile and Public Agent or sends their application, and finishes with their invite code when it arrives.
---

# Get started with HyperOrbs

Use this right after the person connects HyperOrbs, or whenever they ask to set it up.

1. Call `get_account`. Its `next_step` says where they are:
   - `ready`: they are set up. Tell them in one line what they can ask for (their agent, their AI team, memory, apps) and stop.
   - `set_up`: they have access but no workspace or agent yet. Go to step 2.
   - `apply`: HyperOrbs is invite-only and they have not applied. Go to step 2; `set_up_hyperorbs` sends their application.
   - `wait_review`: their application is in review. Say they'll get an invite code by email and can give it to you.
   - `redeem_code`: they were approved. Ask for the code from their email and call `redeem_invite_code`.
2. Ask what you need for `set_up_hyperorbs`, in plain questions, a few at a time:
   - what they run (startup, company, creator, freelancer, student or individual) and its name;
   - a website, or a sentence or two on what it does;
   - what they want from HyperOrbs (for example customers, investors, partners, an AI team);
   - its stage;
   - optionally the topics they work on, and a name for their Public Agent.
   Use only what the person tells you in this conversation. Never guess or fill in a field they did not give, and never ask for health details, ID numbers, payment card or bank details, or passwords.
3. Show them a short summary of what you will send and ask them to confirm. Then call `set_up_hyperorbs`.
4. If it reports missing or invalid fields, ask for those fields only and try again.
5. When it succeeds, tell them what was created, or that their application was sent.
6. Offer to save a few facts about their work to their team's memory with `remember`, and save only the work facts they approve.
