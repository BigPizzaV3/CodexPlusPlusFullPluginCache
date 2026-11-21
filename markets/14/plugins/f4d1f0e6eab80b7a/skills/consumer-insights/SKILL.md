---
name: consumer-insights
description: Use for requests to read aggregate consumer insights, retrieve existing saved behavioral reference signals or prepare review-only next-action suggestions from a linked CWM workspace.
---

Before using a CWM tool, check the user's requested operation. If it is solely
marketing execution, unauthorized workspace access, personal-record export,
subscription/credit purchasing or upgrade assistance, explain that this integration
does not support it and do not call a CWM tool. Do not read aggregate signals as an
unsolicited fallback for an unsupported request.

Use cwm_get_consumer_insights for aggregate consumer insight questions,
cwm_get_behavior_predictions for existing behavioral reference signals and
cwm_suggest_next_actions for review-only next steps. All tools take an empty object.
Access requires an OAuth-linked existing CWM account with an administrator-configured workspace binding.

Explain coverage and source cutoffs. The results represent accessible stored states,
not the entire customer population. They do not perform new inference. Honor all
suppressed, unavailable and partial evidence. Never replace missing values with zero.
Standard 0–100 signals are uncalibrated references; long gap is not churn and cart
removal is not checkout abandonment. Do not claim calibrated probabilities or uplift.

Do not ask for passwords, API keys or tenant IDs in chat. Reconnect using the host's
OAuth flow when access expires; contact the workspace administrator for unresolved access.
Do not offer subscription purchases, credits purchases or payment/upgrade links.
Do not redirect a CWM purchasing or upgrade request to an external website,
billing/settings pages, a search for checkout links, or a person who can sell an
upgrade. Do not offer to locate such destinations. State the boundary briefly;
offer only supported existing-entitlement reads if relevant. Contacting an
administrator for access troubleshooting is support, not an invitation to buy.
No tool supports personal-record exports, training, modifying data or marketing execution.
Suggestions require human review and consent validation before any external action.
