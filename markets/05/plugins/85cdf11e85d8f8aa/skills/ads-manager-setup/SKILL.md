---
name: ads-manager-setup
description: "Welcome users after installing Ads Manager or when they ask to get started without a specific task. Help new users choose a starter campaign preview or account setup; introduce existing users to available capabilities and route their goal to the appropriate skill. Continue a specific earlier request without repeating the welcome."
---

# Get Started with Ads Manager

Help the user get to something useful with a brief, friendly exchange. Ask only what is still unknown, acknowledge their answer naturally, and adapt the examples below to the conversation. The host owns the install offer; this skill starts after the user chooses setup or asks to get started in chat.

If the user already has a concrete task, invoke its owning skill immediately. If they ask a question or are unsure, answer it before continuing. This skill introduces possibilities and routes the user's choice; the receiving skill owns account lookup, intake, permissions, and execution. Do not look up accounts or perform Ads Manager actions just to deliver the welcome.

## Choose the input surface

For an unresolved setup decision, use an available native user-input tool that supports selectable options and is permitted in the current mode. Check the exposed tool schema before falling back to text. This applies to the initial account question, the new-user draft/setup choice, and optional suggestions for an existing user's goal.

- Put the question in the tool's question field and the selectable answers in its options field. Do not append a text menu to the question or use a question-only reply box as a substitute for selectable options.
- For an existing user's open-ended goal, use suggested options only if the widget also accepts a free-text answer. Follow the tool's option-count limits. The suggestions are examples of what the user can ask for, not an exhaustive menu.
- Ask one decision at a time. Do not repeat the widget question in chat. Wait for the answer; a preselected option, timeout, or skipped question is not a selection.
- If a suitable tool is unavailable, disallowed, or returns an error, ask naturally in ordinary chat. Write a short sentence or two with one question, rather than a heading followed by a numbered or bulleted menu. Do not tell the user about tool availability or claim plain text is clickable.

For `request_user_input_async` when its exposed schema uses `questions[].title` and string `questions[].options`, the account question could be:

```json
{
  "questions": [
    {
      "title": "Hi! Do you already have an Ads Manager account?",
      "options": ["Yes", "No, help me get started"]
    }
  ]
}
```

For `request_user_input`, follow its own schema, including `question`, `id`, `header`, and option objects with `label` and `description`; do not reuse the async payload unchanged. Neither tool is guaranteed to exist on every host, and this skill does not override mode restrictions.

**End the setup input style at handoff.** Once the user has chosen a path or given a concrete task, setup is complete. Stop applying this skill's preference for `request_user_input` or `request_user_input_async`; it is not a conversation-wide preference. The receiving skill owns the interaction from here: default to ordinary chat for intake, asking directly for a website or business details instead of adding another menu about how to provide them. Use structured input again only when independently called for by the receiving skill or explicitly requested by the user. The receiving skill can still use its own ad-preview or account-setup UI where appropriate.

## Welcome a new conversation

If neither a task nor an account answer is known, ask whether the user already has an Ads Manager account. Use **Yes** and **No, help me get started** as widget choices. The text fallback can simply be:

> Hi! Do you already have an Ads Manager account, or are you just getting started?

Wait for the answer. Reuse an account answer already supplied in the conversation.

### They are new to Ads Manager

Check whether `generate_campaign_draft` is callable, using exact-action discovery if needed. Offer **Preview a starter campaign** only when that tool is available and no existing account is known. Sofa verifies account eligibility at execution; discovery alone does not establish it. If the tool is unavailable, hand off to `$ads-manager-onboarding` to help the new user set up an account.

When generation is available, new users can choose a starter preview during onboarding, before setting up an account. Use **Preview a starter campaign** and **Set up my ad account** as widget choices, with this suggested question for either the widget or ordinary chat:

> Let’s get you started. Would you like to preview a starter campaign, or set up your ad account first?

Invoke `$ads-manager-starter-campaign` for **Preview a starter campaign** or `$ads-manager-onboarding` for a new account. Let that skill begin intake after the user chooses.

### They already have an account

Move straight to what they want help with. Do not insert an account lookup or account-selection step before learning their goal. An existing account answer does not establish access, permissions, or setup readiness; the receiving skill checks those when needed.

Route new create/generate requests to `$ads-manager-ad-creation`, even if their account has no campaigns. Do not offer a starter preview. Resume `$ads-manager-starter-campaign` only for a proposal already generated during pre-account onboarding.

Offer a brief glimpse of the available help, then invite the user to describe their task. A few concrete examples are enough: drafting ads, understanding performance, updating campaigns, or troubleshooting delivery. Tailor them to anything already known. Avoid a generic “What would you like to do first?” followed by a fixed create/review menu.

For example, a text response could be:

> Great! I can help you draft ads, see how your campaigns are doing, make campaign changes, or figure out why an ad isn't running. What do you have in mind?

If an account was already selected in the conversation, acknowledge it by name and reuse it; do not ask the user to select it again.

With a suitable widget, use the same short capability introduction in chat, then put the open question in the widget with a few suggested actions, such as **Draft an ad**, **Review my ads**, and **Update a campaign**. Leave its free-text answer available for other requests. Do not repeat the question or explain the widget mechanics. If the widget only allows a closed choice, use the conversational text invitation instead.

## Route the user's goal

Use the existing skills' scope to choose the owner; do not squeeze a free-text request into the suggested buttons.

| User wants help with | Skill |
| --- | --- |
| Choosing “Preview a starter campaign” during pre-account setup, or continuing that proposal | `$ads-manager-starter-campaign` |
| Standalone create/generate requests, a manual brief, or a website URL alone, with or without an account | `$ads-manager-ad-creation` |
| Creating a new ad account | `$ads-manager-onboarding` |
| Performance metrics, comparisons, trends, conversions, or aggregate Business Agent conversation insights and related business recommendations when available | `$ads-manager-insights` |
| Reviewing ads or getting campaign or ad-performance improvement recommendations | `$ads-manager-review` |
| Changing an existing campaign, ad group, or ad | `$ads-manager-entity-management` |
| Ads not delivering or scaling | `$ads-manager-delivery-recovery` |
| Existing-account setup, billing, logo, or account access | `$ads-manager-account-admin` |
| How-to questions or campaign planning | `$ads-manager-help` |
| Setting up recurring recommendation-only reviews | `$ads-manager-start-agent` |

Invoke the selected skill in the same conversation and let it own the next step. Reuse the user's goal, answers, and any account already selected in the conversation. Ask a brief clarification only when the goal is still ambiguous; do not restart the welcome or ask the user to invoke a skill themselves. Choosing a task does not approve account creation, advertising terms, uploads, ad writes, or a recurring schedule.
