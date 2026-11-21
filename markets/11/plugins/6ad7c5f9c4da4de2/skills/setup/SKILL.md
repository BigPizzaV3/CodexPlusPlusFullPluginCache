---
name: setup
description: Connect the HoreX restaurant plugin and check access, connection status and AI Credit billing. Use for setup and reconnection, not business analysis.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

Use get_profile to check the connected HoreX account and selected restaurant. A successful check is free. If authentication fails, use the host's Connect or Reconnect action and let the user complete HoreX sign-in and consent. Never ask for passwords in chat.

The current pilot is available to Locus. Access also requires the separate Use ChatGPT Plugin permission and the permissions for the requested business data. An unavailable dataset is a permission or configuration boundary; ask an authorized HoreX administrator to review access.

Every successful business-data tool call costs 1 HoreX AI Credit. Profile, catalog, workflow guidance, authentication and failed requests are free. Use get_analysis_catalog to discover the available datasets before composing an analytical query. Use get_horex_workflow to load the relevant business playbook when packaged skills are unavailable in the host.

Report the actual connected account, capabilities and any reconnect requirement. Do not call a restaurant connected merely because the ERP Integrations card says the pilot is ready. Credit balances and usage are in HoreX Subscription / AI account and HPanel AI Usage. Do not invent OpenAI provider-token usage.

Campaign preparation uses campaign-launch and its dedicated Meta / ordinary Google Ads tools. If those tools are absent while the account connects successfully, refresh the existing App's tool catalog in ChatGPT before diagnosing restaurant permissions. Report a refresh failure accurately; do not promise that an unavailable command can execute.
