# Public Fina tool coverage

Source inventory: 2026-10-06. Not live discovery; grants may expose fewer tools.
All execution results are NOT RUN. Only the owner runs these with synthetic data. This file does not instruct an agent to execute tests.
Inspect the live schema and verify side effects, ownership, retries and annotations for each relevant fixture. Never perform destructive tests on real financial data.

| Operation | Purpose | Result | Private evidence |
| --- | --- | --- | --- |
| `get_setup_status` | Set up or resume your finances | NOT RUN | Pending owner execution |
| `update_profile` | Update financial preferences | NOT RUN | Pending owner execution |
| `list_accounts` | View accounts, debts and assets | NOT RUN | Pending owner execution |
| `create_account` | Add an account, debt or asset | NOT RUN | Pending owner execution |
| `update_account` | Update an account or card | NOT RUN | Pending owner execution |
| `update_account_details` | Update debt conditions or asset characteristics | NOT RUN | Pending owner execution |
| `record_account_observation` | Record a dated debt or asset observation | NOT RUN | Pending owner execution |
| `get_financial_context` | Review your financial position and coverage | NOT RUN | Pending owner execution |
| `update_financial_preferences` | Save declared financial goals and preferences | NOT RUN | Pending owner execution |
| `propose_debt_payment` | Suggest linking an existing credit payment | NOT RUN | Pending owner execution |
| `resolve_debt_payment_suggestion` | Review a possible credit payment | NOT RUN | Pending owner execution |
| `record_debt_payment_evidence` | Record credit payment evidence | NOT RUN | Pending owner execution |
| `get_account_details` | Read selected debt or asset details | NOT RUN | Pending owner execution |
| `estimate_property_value` | Research an estimated property value | NOT RUN | Pending owner execution |
| `simulate_debt_scenario` | Compare an extra principal payment | NOT RUN | Pending owner execution |
| `simulate_fixed_income` | Calculate expected fixed-income flows | NOT RUN | Pending owner execution |
| `get_property_valuation` | Read property valuation research | NOT RUN | Pending owner execution |
| `link_instrument` | Link a physical, virtual or Wallet card | NOT RUN | Pending owner execution |
| `record_balance_snapshot` | Record an observed balance or card debt | NOT RUN | Pending owner execution |
| `record_card_statement` | Record a card statement | NOT RUN | Pending owner execution |
| `list_commitments` | View subscriptions and expected income | NOT RUN | Pending owner execution |
| `upsert_commitment` | Add or update a subscription or expected income | NOT RUN | Pending owner execution |
| `match_commitment` | Match a transaction to a subscription or income | NOT RUN | Pending owner execution |
| `resolve_subscription_suggestion` | Review a suggested subscription | NOT RUN | Pending owner execution |
| `submit_financial_events` | Record financial activity | NOT RUN | Pending owner execution |
| `prepare_import` | Preview a transaction import | NOT RUN | Pending owner execution |
| `get_import_plan` | Read a saved import plan | NOT RUN | Pending owner execution |
| `commit_import` | Confirm a transaction import | NOT RUN | Pending owner execution |
| `resolve_event` | Resolve financial activity needing review | NOT RUN | Pending owner execution |
| `list_events` | View received financial activity | NOT RUN | Pending owner execution |
| `get_event` | Inspect received financial activity | NOT RUN | Pending owner execution |
| `search_transactions` | Search transactions | NOT RUN | Pending owner execution |
| `summarize_spending` | Summarize spending | NOT RUN | Pending owner execution |
| `get_upcoming_card_payments` | View upcoming card payments | NOT RUN | Pending owner execution |
| `get_projection` | View cash-flow projections | NOT RUN | Pending owner execution |
| `correct_transaction` | Correct a transaction | NOT RUN | Pending owner execution |
| `cancel_transaction` | Cancel a transaction | NOT RUN | Pending owner execution |
| `restore_transaction` | Restore a cancelled transaction | NOT RUN | Pending owner execution |
| `link_refund` | Link a refund to a purchase | NOT RUN | Pending owner execution |
| `link_account_transfer` | Link an own-account transfer or card payment | NOT RUN | Pending owner execution |
| `unlink_account_transfer` | Remove an account payment link | NOT RUN | Pending owner execution |
| `dismiss_card_payment_suggestion` | Dismiss a suggested card payment | NOT RUN | Pending owner execution |
| `resolve_transaction_match` | Review a possible duplicate transaction | NOT RUN | Pending owner execution |
| `reprocess_event` | Retry processing financial activity | NOT RUN | Pending owner execution |
| `list_ingest_credentials` | View capture devices | NOT RUN | Pending owner execution |
| `revoke_ingest_credential` | Disconnect a capture device | NOT RUN | Pending owner execution |
| `get_ai_usage` | View backend AI usage | NOT RUN | Pending owner execution |
| `get_service_usage` | View service usage and estimated costs | NOT RUN | Pending owner execution |

Service usage means Fina operating usage/costs, not personal spending. Credential revocation is an actual access change: use only a disposable synthetic capture device. Internal authorization and credential-creation tools are excluded.
