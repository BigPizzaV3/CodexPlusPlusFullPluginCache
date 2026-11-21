# Exness MCP tools — 0.2.3

Endpoint: https://api.exness.com/mcp

OAuth sign-in is required. Tokens are managed by the host. No credentials belong in the ZIP. Trading calls require an authorized account_id; available tools depend on scopes.

## Documentation

### docs_get_page

Read-only.

Read the complete original Markdown for a page_id returned by docs_search. Uses an offline documentation snapshot; never accesses accounts or executes trades. Unknown pages return PAGE_NOT_FOUND; oversized pages return PAGE_TOO_LARGE.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "page_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 512
    }
  },
  "required": [
    "page_id"
  ]
}
```

### docs_search

Read-only.

Search public Exness API documentation by topic, API term or error. Returns relevant sections and page IDs; use docs_get_page to read a full page. Uses an offline snapshot; never accesses accounts or executes trades.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "query": {
      "type": "string",
      "minLength": 1,
      "maxLength": 500
    },
    "product": {
      "type": "string",
      "enum": [
        "all",
        "trading",
        "partnership",
        "payments",
        "reference",
        "general"
      ],
      "default": "all"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 10,
      "default": 5
    }
  },
  "required": [
    "query"
  ]
}
```

## Trading (read-only)

### trading.get_account_overview

Read-only.

Read account settings and current balance, equity, margin, positions and orders from the Public API.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    }
  }
}
```

### trading.get_api_limits

Read-only.

Read the published REST and WebSocket limits for one account.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    }
  }
}
```

### trading.get_candles

Read-only.

Read bounded historical candles for one instrument and timeframe.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id",
    "instrument",
    "timeframe",
    "from",
    "to"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    },
    "timeframe": {
      "type": "string",
      "enum": [
        "S1",
        "S5",
        "S15",
        "M1",
        "M3",
        "M5",
        "M10",
        "M15",
        "M30",
        "H1",
        "H2",
        "H4",
        "D1",
        "W1",
        "MN"
      ]
    },
    "from": {
      "type": "string",
      "format": "date-time"
    },
    "to": {
      "type": "string",
      "format": "date-time"
    },
    "price_type": {
      "type": "string",
      "enum": [
        "bid",
        "ask",
        "both"
      ],
      "default": "bid"
    }
  }
}
```

### trading.get_deals_history

Read-only.

Read one page of historical deals. Continue with the returned cursor when has_more is true.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "from": {
      "type": "string",
      "format": "date-time"
    },
    "to": {
      "type": "string",
      "format": "date-time"
    },
    "cursor": {
      "type": "string",
      "minLength": 1
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 200,
      "default": 100
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    },
    "deal_type": {
      "type": "string",
      "enum": [
        "open",
        "close",
        "balance",
        "null_compensation",
        "admin_fee",
        "swap_fee",
        "dividend",
        "exness_dollar"
      ]
    }
  },
  "oneOf": [
    {
      "required": [
        "from"
      ],
      "not": {
        "required": [
          "cursor"
        ]
      }
    },
    {
      "required": [
        "cursor"
      ],
      "not": {
        "anyOf": [
          {
            "required": [
              "from"
            ]
          },
          {
            "required": [
              "to"
            ]
          },
          {
            "required": [
              "instrument"
            ]
          },
          {
            "required": [
              "deal_type"
            ]
          }
        ]
      }
    }
  ]
}
```

### trading.get_exposure_summary

Read-only.

Summarize current buy, sell, gross and net position volume by instrument. Pending entry orders can be included separately.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "include_pending_orders": {
      "type": "boolean",
      "default": false
    }
  }
}
```

### trading.get_instrument_conditions

Read-only.

Read the account-specific trading conditions for one instrument.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id",
    "instrument"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    }
  }
}
```

### trading.get_instruments

Read-only.

Read the instruments configured for one authorized account through the Exness Public API. Performs host discovery for each call and returns the instrument names from GET /v1/configuration/accounts/{account_id}/instruments.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    }
  }
}
```

### trading.get_open_positions

Read-only.

Read open positions and their placed SL/TP orders for one authorized account. Optional instrument and direction filters combine with AND. Uses one account snapshot after host discovery. An empty protection list only means no matching placed SL/TP in this snapshot; it does not describe in-flight changes. Does not provide per-position P&L.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    },
    "direction": {
      "type": "string",
      "enum": [
        "buy",
        "sell"
      ]
    }
  }
}
```

### trading.get_operation_status

Read-only.

Read the status of a known asynchronous trading operation.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id",
    "operation_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "operation_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    }
  }
}
```

### trading.get_orders_history

Read-only.

Read one page of historical orders. Continue with the returned cursor when has_more is true.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "from": {
      "type": "string",
      "format": "date-time"
    },
    "to": {
      "type": "string",
      "format": "date-time"
    },
    "cursor": {
      "type": "string",
      "minLength": 1
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 200,
      "default": 100
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    },
    "order_state": {
      "type": "string",
      "enum": [
        "filled",
        "cancelled",
        "rejected"
      ]
    }
  },
  "oneOf": [
    {
      "required": [
        "from"
      ],
      "not": {
        "required": [
          "cursor"
        ]
      }
    },
    {
      "required": [
        "cursor"
      ],
      "not": {
        "anyOf": [
          {
            "required": [
              "from"
            ]
          },
          {
            "required": [
              "to"
            ]
          },
          {
            "required": [
              "instrument"
            ]
          },
          {
            "required": [
              "order_state"
            ]
          }
        ]
      }
    }
  ]
}
```

### trading.get_pending_orders

Read-only.

List placed limit and stop entry orders for one account. SL/TP protection orders are excluded.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "account_id"
  ],
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 20,
      "pattern": "^[0-9]+$"
    },
    "instrument": {
      "type": "string",
      "minLength": 1,
      "maxLength": 11,
      "pattern": "^[A-Za-z0-9._-]+$"
    },
    "direction": {
      "type": "string",
      "enum": [
        "buy",
        "sell"
      ]
    },
    "order_type": {
      "type": "string",
      "enum": [
        "limit",
        "stop"
      ]
    }
  }
}
```

## Partnership

### partner.build_exd_transfer_link

Read-only; EXD link creation does not execute a transfer.

Build a Partner Area EXD transfer link for client account numbers and an amount. Use this after identifying eligible clients and confirming the transfer amount. This tool only creates a link; it does not initiate a transfer. The partner reviews and completes the transfer in Partner Area.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "client_accounts": {
      "description": "Client trading account numbers to prefill as recipients.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "amount": {
      "description": "Positive EXD transfer amount as a decimal string.",
      "gt": 0,
      "pattern": "^-?\\d+(\\.\\d+)?$",
      "type": "string"
    }
  },
  "required": [
    "client_accounts",
    "amount"
  ]
}
```

### partner.check_client_affiliation

Read-only.

Check whether the client email belongs to the authenticated partner. Return whether the client is affiliated with the partner, the client account numbers under this partner, and the full client UID.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "email": {
      "description": "Client email address to check.",
      "format": "email",
      "type": "string"
    }
  },
  "required": [
    "email"
  ]
}
```

### partner.create_partner_link_code

Changes data. Review and confirm the intended operation.

Create a custom Revenue Share partner link code and return the created link record, including its code, reward schema, and blocking and custom flags. This tool does not create CPA codes.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "partner_code": {
      "description": "Revenue Share link code to create.",
      "minLength": 1,
      "type": "string"
    },
    "account": {
      "description": "Partner account number to be associated with the link code",
      "pattern": "^\\d+$",
      "type": "string"
    }
  },
  "required": [
    "partner_code"
  ]
}
```

### partner.get_client_orders

Read-only.

Return closed client-order rows used to calculate first-level partner rewards. date_from and date_to filter inclusive reward-credit dates; their difference must not exceed 32 days. The returned date is the reward-credit date, while open_date and close_date are trade timestamps. Returned order_id uses <server_code>:<order_number>; the filter accepts only its numeric order number.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "client_account": {
      "description": "Filter by referred client trading account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "date_from": {
      "description": "Start of the inclusive reward-credit date range; not the trade open or close date.",
      "format": "date",
      "type": "string"
    },
    "date_to": {
      "description": "End of the inclusive reward-credit date range; not the trade open or close date.",
      "format": "date",
      "type": "string"
    },
    "order_id": {
      "description": "Filter by numeric order number only; omit the server_code prefix from the returned order_id.",
      "minimum": 0,
      "type": "integer"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of report rows to return.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Optional comma-separated sort fields; prefix a field with - for descending. Supported fields: symbol, open_spread, volume_lots, volume_mln_usd, date, close_date, open_date, client_account, reward, reward_usd.",
      "type": "string"
    }
  },
  "required": [
    "date_from",
    "date_to"
  ]
}
```

### partner.get_client_registrations

Read-only.

Return referred-client registration counts grouped by day for the requested date range. reg_date is the Personal Area registration date; both date boundaries are inclusive, and the range cannot exceed 366 days. This is not an account-opening or trading report. Use totals.amount for the complete period instead of summing individual rows or pages.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "reg_date_from": {
      "description": "Earliest Personal Area registration date to include, inclusive.",
      "format": "date",
      "type": "string"
    },
    "reg_date_to": {
      "description": "Latest Personal Area registration date to include, inclusive.",
      "format": "date",
      "type": "string"
    }
  },
  "required": [
    "reg_date_from",
    "reg_date_to"
  ]
}
```

### partner.get_ib_performance_report

Read-only.

Return revenue-share IB acquisition and trading metrics grouped by one or two required dimensions. Each row includes group_fields in the requested order, clicks, registrations, KYC passes, first deposits, demo and real trading starts, trading volume in lots and millions of USD, and reward_usd. link_clicked_from and link_clicked_to filter partner-link click dates. When group_by includes day, the grouped day is the event date, not the click date. Events may happen after the click and on different days: for example, registration on one day, first deposit on another, and demo or real trading later. Therefore, grouped event dates may fall outside the click-date filter range.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "group_by": {
      "description": "One or two dimensions used to group the report rows, in output order.",
      "items": {
        "enum": [
          "day",
          "week",
          "month",
          "year",
          "country",
          "campaign_title",
          "partner_code",
          "referrer_domain",
          "track1",
          "track2",
          "track3",
          "track4",
          "track5",
          "utm_source",
          "utm_medium",
          "utm_campaign",
          "utm_term",
          "utm_content"
        ],
        "type": "string"
      },
      "maxItems": 2,
      "minItems": 1,
      "type": "array"
    },
    "link_clicked_from": {
      "description": "Start of the partner-link click-date filter, inclusive.",
      "format": "date",
      "type": "string"
    },
    "link_clicked_to": {
      "description": "End of the partner-link click-date filter, inclusive.",
      "format": "date",
      "type": "string"
    },
    "country": {
      "description": "Filter by client countries.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "partner_code": {
      "description": "Filter by partner link codes.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "campaign_title": {
      "description": "Filter by campaign titles.",
      "items": {
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 1,
      "type": "array"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of grouped report rows to return.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Optional comma-separated sort fields; prefix a field with - for descending. Supported fields: day, week, month, year, country, campaign_title, partner_code, referrer_domain, track1, track2, track3, track4, track5, utm_source, utm_medium, utm_campaign, utm_term, utm_content, click_count, registration_count, kyc_passed, first_deposit_count, trade_starting_trial_count, trade_starting_real_count, volume_mln_usd, reward_usd, volume_lots.",
      "type": "string"
    }
  },
  "required": [
    "group_by"
  ]
}
```

### partner.get_partner_client_accounts_first_level

Read-only.

List of first level client trading accounts with partner accounts, currencies, account dates, volumes, rewards and comments. Return one row per referred client trading account, including the partner link code through which the client was attributed, account type, platform, activity dates, volume, reward, and partner comment. Use this report for individual client trading accounts analysis. reward is in the partner account currency; use reward_usd for cross-currency comparisons.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "partner_account_name": {
      "description": "Filter by partner account names.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 1,
      "type": "array"
    },
    "partner_account": {
      "description": "Filter by partner account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_uid": {
      "description": "Filter by client UUIDs.",
      "items": {
        "format": "uuid",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_country": {
      "description": "Filter by client countries.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "platform": {
      "description": "Filter by trading platforms.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "maxItems": 64,
      "minItems": 1,
      "type": "array"
    },
    "client_account_created_from": {
      "description": "Start of the account creation-date range.",
      "format": "date",
      "type": "string"
    },
    "client_account_created_to": {
      "description": "End of the account creation-date range.",
      "format": "date",
      "type": "string"
    },
    "client_account_last_trade_from": {
      "description": "Start of the account last-trade-date range.",
      "format": "date",
      "type": "string"
    },
    "client_account_last_trade_to": {
      "description": "End of the account last-trade-date range.",
      "format": "date",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "partner_code": {
      "description": "Filter by partner link codes.",
      "items": {
        "maxLength": 12,
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_account": {
      "description": "Filter by client account numbers. Only available for direct clients.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_account_type": {
      "description": "Filter by displayed account-type names, not internal account-type codes.",
      "items": {
        "enum": [
          "ECN",
          "Standard Cent",
          "Standard",
          "Standard Plus",
          "Pro",
          "Raw Spread",
          "Zero",
          "Institutional",
          "Social Standard",
          "Social Pro",
          "Social hmr Pro",
          "ST-Investment",
          "ST Inv mini",
          "ST Inv classic"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "comment": {
      "description": "Filter by partner comment.",
      "minLength": 1,
      "type": "string"
    },
    "ordering": {
      "description": "Comma-separated sort fields; prefix '-' for descending. Default: -client_account_last_trade. Supported fields: partner_account_name, partner_account, partner_code, client_uid, client_country, platform, client_account, client_account_type, client_account_created, client_account_last_trade, volume_lots, volume_mln_usd, reward, reward_usd, comment.",
      "type": "string"
    }
  }
}
```

### partner.get_partner_clients

Read-only.

List the authenticated IB partner's clients with registration, relationship and contact-sharing statuses, onboarding progress, trading volumes, USD rewards and rebate data. Use this report for client-level analysis. Balance, equity and deposit fields are ranges, not exact amounts.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "partner_account": {
      "description": "Filter by partner account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_uid": {
      "description": "Filter by client UUIDs.",
      "items": {
        "format": "uuid",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_country": {
      "description": "Filter by client countries.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "reg_date_from": {
      "description": "Include clients registered on or after this date.",
      "format": "date",
      "type": "string"
    },
    "reg_date_to": {
      "description": "Include clients registered on or before this date.",
      "format": "date",
      "type": "string"
    },
    "trade_fn_from": {
      "description": "Start date of the last-reward date range, not the account's last-trade date. Using trade_fn_from or trade_fn_to returns only clients with a positive reward.",
      "format": "date",
      "type": "string"
    },
    "trade_fn_to": {
      "description": "End date of the last-reward date range. Using trade_fn_from or trade_fn_to returns only clients with a positive reward.",
      "format": "date",
      "type": "string"
    },
    "client_status": {
      "description": "Filter by relationship status.",
      "items": {
        "enum": [
          "ACTIVE",
          "INACTIVE",
          "LEFT",
          "CHANGING"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_contact_sharing_status": {
      "description": "Contact-sharing UI filter values differ from response status values.",
      "items": {
        "enum": [
          "SHARED",
          "NOT_SHARED",
          "PENDING"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "contact_sharing_progress_status": {
      "description": "Filter by KYC, first-deposit or first-trade progress.",
      "items": {
        "enum": [
          "kyc_not_passed",
          "ftt_not_made",
          "ftd_not_received",
          "kyc_passed",
          "ftt_made",
          "ftd_received"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "last_client_contact_sharing_dt_from": {
      "description": "Start date for the client's last contact-sharing event.",
      "format": "date",
      "type": "string"
    },
    "last_client_contact_sharing_dt_to": {
      "description": "End date for the client's last contact-sharing event.",
      "format": "date",
      "type": "string"
    },
    "limit": {
      "default": 100,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Comma-separated sort fields; prefix '-' for descending. Omit to retain backend default newest registration first. Supported fields: partner_account, client_uid, reg_date, client_country, volume_mln_usd, reward_usd, trade_fn, client_status, rebate_amount_usd, last_client_contact_sharing_dt, client_balance, client_equity, deposit_amount, ftd_amount, last_week_failed_deposit_count.",
      "type": "string"
    }
  }
}
```

### partner.get_partner_links

Read-only.

Retrieve existing partner links with their full URLs and associated metadata. Each link includes its code, status, partner account number when available, and reward scheme. The URL is constructed using the partner default-link domain. Optionally filter the link list only by blocked state using is_blocked.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "is_blocked": {
      "description": "Filter link records by blocked state.",
      "type": "boolean"
    }
  }
}
```

### partner.get_partner_overview

Read-only.

Returns the authenticated partner's profile summary together with the current partner tier

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {}
}
```

### partner.get_partner_rewards_first_level

Read-only.

Return first-level credited partner-reward data with client, trading-account, partner-account, partner link code, volume, currency, and reward details. reward_date_from and reward_date_to filter reward-credit dates, not trade dates. The required aggregate_by parameter selects the time aggregation interval: year, month, week, day, or raw for unaggregated rows. Use filters and totals to reconcile the reporting period; totals cover all matching rows, not only the current page.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "aggregate_by": {
      "enum": [
        "year",
        "month",
        "week",
        "day",
        "raw"
      ],
      "type": "string",
      "description": "Time aggregation interval: year, month, week, day, or raw for unaggregated rows."
    },
    "partner_account": {
      "description": "Filter by partner account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "partner_account_name": {
      "description": "Filter by partner account names.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 1,
      "type": "array"
    },
    "link_code": {
      "description": "Filter by partner link codes.",
      "items": {
        "maxLength": 12,
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_uid": {
      "description": "Filter by client UUIDs.",
      "items": {
        "format": "uuid",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "country": {
      "description": "Filter by client countries.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "platform": {
      "description": "Filter by trading platforms.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "maxItems": 64,
      "minItems": 1,
      "type": "array"
    },
    "client_account": {
      "description": "Filter by client account numbers. Only available for direct clients.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_account_type": {
      "description": "Filter by displayed account-type names, not internal account-type codes.",
      "items": {
        "enum": [
          "ECN",
          "Standard Cent",
          "Standard",
          "Standard Plus",
          "Pro",
          "Raw Spread",
          "Zero",
          "Institutional",
          "Social Standard",
          "Social Pro",
          "Social hmr Pro",
          "ST-Investment",
          "ST Inv mini",
          "ST Inv classic"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "currency": {
      "description": "Filter by partner account currency.",
      "minLength": 1,
      "type": "string"
    },
    "reward_date_from": {
      "description": "Start of the reward-credit date range; not the trade date.",
      "format": "date",
      "type": "string"
    },
    "reward_date_to": {
      "description": "End of the reward-credit date range; not the trade date.",
      "format": "date",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Comma-separated sort fields; prefix '-' for descending. Supported fields: client_account, client_account_type, client_uid, country, platform, currency, link_code, orders_count, partner_account, partner_account_name, reward, reward_date, reward_usd, volume_lots, volume_mln_usd.",
      "type": "string"
    }
  },
  "required": [
    "aggregate_by"
  ]
}
```

### partner.get_partner_tier

Read-only.

Return the partner's current tier state and tier conditions. Include tier names, named qualification thresholds, Boolean requirements, ordering, and commission fields as returned. Do not infer eligibility, combine alternative conditions, or calculate a promotion decision.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {}
}
```

### partner.get_rebate_clients_report

Read-only.

List persistent rebate settings for referred clients and their account metrics. date_from and date_to filter by client registration date; they do not define a trading or rebate-payment period. Native-currency and USD metrics are returned separately.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "client_account_type": {
      "description": "Filter by client account type display name, as shown in the client_account_type field. Known values: Standard Cent, Standard, Standard Plus, Pro, Raw Spread, Zero, Institutional.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "partner_account": {
      "description": "Filter by partner account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "partner_code": {
      "description": "Filter by partner link codes.",
      "items": {
        "maxLength": 12,
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "group_id": {
      "description": "Filter by rebate group IDs.",
      "items": {
        "type": "integer"
      },
      "minItems": 1,
      "type": "array"
    },
    "country": {
      "description": "Filter by client countries.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_account": {
      "description": "Filter by client account numbers.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "client_uid": {
      "description": "Filter by client UUIDs.",
      "items": {
        "format": "uuid",
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "date_from": {
      "description": "Start of the client registration date range; not a trading or rebate-payment period.",
      "format": "date",
      "type": "string"
    },
    "date_to": {
      "description": "End of the client registration date range; not a trading or rebate-payment period.",
      "format": "date",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Single sort field; prefix '-' for descending. Set it for stable offset pagination. Supported fields: partner_account, client_account, client_uid, client_account_type, partner_code, country, reg_date, group_title, rebate_percent, volume_lots, volume_usd, reward_usd, processed_rebate_usd, destination_client_account, rebate_size.",
      "type": "string"
    }
  }
}
```

### partner.get_rebate_details

Read-only.

List calculated rebate rows for individual rewards, including row IDs, destination account numbers, errors, and amounts in the partner account currency and USD. These are calculated entries, not persistent client rebate settings. rebate_id comes from get_rebates. totals cover the whole rebate, not just the current page. This operation is read-only.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "rebate_id": {
      "description": "Rebate identifier, as returned by get_rebates.",
      "type": "integer"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Single sort field; prefix '-' for descending. Supported fields: partner_account, client_account, volume_lots, reward, reward_usd, rebate, rebate_usd, rebate_percent, status, error_code, destination_client_account, group_id, group_title, processed_date, reward_date.",
      "type": "string"
    }
  },
  "required": [
    "rebate_id"
  ]
}
```

### partner.get_rebate_group_rules

Read-only.

List all active rules for the specified rebate group, including active and default flags, account types, reward-volume bounds, rebate size and priority. The API is unpaginated; totals.count is the number of rules. Do not infer the priority ordering or the unit of rebate_size.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "group_id": {
      "description": "Rebate group ID, as returned by get_rebate_groups.",
      "type": "integer"
    }
  },
  "required": [
    "group_id"
  ]
}
```

### partner.get_rebate_groups

Read-only.

List rebate group configuration, client counts, percentage bounds and current payment-period dates. Only active groups are returned, and the default group always comes first. totals cover all matching groups, not just the current page. This operation does not return group clients or rules.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "group_type": {
      "description": "Filter by group type. Known values: MANUAL, AUTO.",
      "items": {
        "enum": [
          "MANUAL",
          "AUTO"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "group_id": {
      "description": "Filter by rebate group IDs.",
      "items": {
        "type": "integer"
      },
      "minItems": 1,
      "type": "array"
    },
    "rebate_period": {
      "description": "Filter by rebate period. Known values: DAILY, WEEKLY, MONTHLY.",
      "items": {
        "enum": [
          "DAILY",
          "WEEKLY",
          "MONTHLY"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "link_code": {
      "description": "Filter by partner link codes.",
      "items": {
        "maxLength": 12,
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Single sort field; prefix '-' for descending. Supported fields: group_title, clients_count, created, group_type, rebate_period, link_code.",
      "type": "string"
    }
  }
}
```

### partner.get_rebates

Read-only.

List calculated rebates with client counts, reward and rebate amounts, processing status, and rebate-period dates. Filter by date range, group, status, or rebate period. totals summarizes all matching rebates, including those on other pages. This operation only lists rebates; it does not approve or reject them.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "date_from": {
      "description": "Start of the date range.",
      "format": "date",
      "type": "string"
    },
    "date_to": {
      "description": "End of the date range.",
      "format": "date",
      "type": "string"
    },
    "group_id": {
      "description": "Filter by rebate group IDs.",
      "items": {
        "type": "integer"
      },
      "minItems": 1,
      "type": "array"
    },
    "status": {
      "description": "Filter by processing status. Known values: PENDING, APPROVED, PROCESSING, PROCESSED, PROCESSED_PARTIAL, ERROR, REJECTED.",
      "items": {
        "minLength": 1,
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "rebate_period": {
      "description": "Filter by rebate period. Known values: DAILY, WEEKLY, MONTHLY.",
      "items": {
        "enum": [
          "DAILY",
          "WEEKLY",
          "MONTHLY"
        ],
        "type": "string"
      },
      "minItems": 1,
      "type": "array"
    },
    "limit": {
      "default": 10,
      "description": "Page size, 0-1000. Zero has backend-defined behavior; do not assume it requests all records.",
      "maximum": 1000,
      "minimum": 0,
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of matching rows to skip.",
      "minimum": 0,
      "type": "integer"
    },
    "ordering": {
      "description": "Single sort field; prefix '-' for descending. Supported fields: period_end_date, clients_count, clients_approved_count, reward_usd, topay_rebate_usd, status, group_name.",
      "type": "string"
    }
  }
}
```

### partner.manage_rebate_group

Changes data. Review and confirm the intended operation.

Create a manual rebate group when group_id is omitted, or update an existing group when group_id is given. For creation, provide group_title and is_default. After creation, the tool uses the returned group ID. A rebate group cannot be created for a partner who has not referred any clients yet. For an existing group, group_title and is_default are optional updates. It updates rebate_period_value, rebate_period, and link_code when provided. When rebate_percent is provided, it finds and updates the group's default rule. The response includes the latest group and default rule values available and any operation errors. Creation and initial group lookup failures return a tool error. If a later operation fails, the tool attempts to reload current group and rule values before returning.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "group_id": {
      "description": "Existing group ID to update. Omit to create a new group.",
      "type": "integer"
    },
    "group_title": {
      "description": "Group title to set. Required on creation; optional when updating.",
      "maxLength": 256,
      "minLength": 1,
      "type": "string"
    },
    "is_default": {
      "description": "Whether this should be the default group. Required on creation; optional when updating.",
      "type": "boolean"
    },
    "rebate_period_value": {
      "description": "Period start value to set on the group, if changing it.",
      "type": "integer"
    },
    "rebate_period": {
      "enum": [
        "DAILY",
        "WEEKLY",
        "MONTHLY"
      ],
      "type": "string",
      "description": "Payout period to set on the group: DAILY, WEEKLY, or MONTHLY."
    },
    "link_code": {
      "description": "Partner link code to associate with the group, up to 12 characters, if changing it.",
      "maxLength": 12,
      "minLength": 1,
      "type": "string"
    },
    "rebate_percent": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
          "type": "string"
        }
      ],
      "decimal_places": 1,
      "description": "Rebate percentage for the group's default rule. When provided, updates that rule.",
      "ge": 0,
      "max_digits": 15
    }
  }
}
```

### partner.manage_rebate_rule

Changes data. Review and confirm the intended operation.

Create, update, or delete a rebate group rule. For create, provide group_id and settings.name; omit rule_id. Creation sends the name first, then applies any other settings in a separate update. Creation can succeed even if that update fails: the response then includes the created rule and errors. Do not retry creation to fix a settings error; update the returned rule ID instead. For update, provide rule_id and at least one field in settings; omit group_id. For delete, provide rule_id and omit group_id and settings. Omitted settings remain unchanged. Explicit null bounds clear those bounds; never treat null as zero. Do not infer the unit of rebate_size or the priority ordering. Initial creation, standalone update, and deletion failures return a tool error. A request error may leave the operation outcome unknown.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "action": {
      "enum": [
        "create",
        "update",
        "delete"
      ],
      "type": "string",
      "description": "Operation to perform: create, update, or delete."
    },
    "group_id": {
      "description": "Group ID. Required for create; omit for update and delete.",
      "type": "integer"
    },
    "rule_id": {
      "description": "Rule ID. Required for update and delete; omit for create.",
      "type": "integer"
    },
    "settings": {
      "properties": {
        "name": {
          "description": "Rule name. Required for creation; omit to keep on update.",
          "maxLength": 100,
          "minLength": 1,
          "type": "string"
        },
        "rebate_size": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
              "type": "string"
            }
          ],
          "decimal_places": 1,
          "description": "Rule rebate_size value. The unit is not specified; do not infer it. Omit to keep unchanged.",
          "max_digits": 15
        },
        "account_types": {
          "description": "Account types to which the rule applies. Omit to keep unchanged.",
          "items": {
            "enum": [
              "Standard Cent",
              "Standard",
              "Standard Plus",
              "Pro",
              "Raw Spread",
              "Zero",
              "Institutional"
            ],
            "type": "string"
          },
          "type": "array"
        },
        "min_reward_tv_usd": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
                  "type": "string"
                }
              ],
              "decimal_places": 2,
              "max_digits": 15
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Minimum reward trading volume in USD. Null clears the bound; omit to keep unchanged."
        },
        "max_reward_tv_usd": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
                  "type": "string"
                }
              ],
              "decimal_places": 2,
              "max_digits": 15
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Maximum reward trading volume in USD. Null clears the bound; omit to keep unchanged."
        },
        "min_reward_tv_lots": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
                  "type": "string"
                }
              ],
              "decimal_places": 2,
              "max_digits": 15
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Minimum reward trading volume in lots. Null clears the bound; omit to keep unchanged."
        },
        "max_reward_tv_lots": {
          "anyOf": [
            {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
                  "type": "string"
                }
              ],
              "decimal_places": 2,
              "max_digits": 15
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Maximum reward trading volume in lots. Null clears the bound; omit to keep unchanged."
        },
        "priority": {
          "description": "Rule priority. Ordering is not specified; do not infer it. Omit to keep unchanged.",
          "type": "integer"
        }
      },
      "type": "object",
      "description": "Rule settings. Create requires name; update requires at least one field; omit for delete. Explicit null bounds are preserved."
    }
  },
  "required": [
    "action"
  ]
}
```

### partner.update_client_rebate_settings

Changes data. Review and confirm the intended operation.

Set the same rebate percentage (0-100) for the specified client account numbers. This removes their rebate-group membership and updates persistent client settings. The operation may partially complete and does not modify calculated rebate rows. A successful response confirms the request succeeded, without individual account outcomes. Request failures return a tool error. A request error may leave the outcome unknown; some changes may already have been applied.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "client_accounts": {
      "description": "Client account numbers as integer strings to apply the same rebate percentage to. Removes their rebate-group membership.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 1,
      "type": "array"
    },
    "rebate_percent": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "pattern": "^(?!^[-+.]*$)[+-]?0*\\d*\\.?\\d*$",
          "type": "string"
        }
      ],
      "decimal_places": 1,
      "description": "Rebate percentage from 0 to 100, with at most one decimal place, to set for every specified account. Updates persistent client settings; calculated rebate rows are unchanged.",
      "ge": 0,
      "le": 100,
      "max_digits": 15
    }
  },
  "required": [
    "client_accounts",
    "rebate_percent"
  ]
}
```

### partner.update_rebate_group_members

Changes data. Review and confirm the intended operation.

Add client account numbers to or remove them from a rebate group. Adding or removing an account resets its individual rebate percentage to zero. Adding accounts to a non-default AUTO group changes it to MANUAL. Provide group_id and at least one non-empty list: client_accounts_add or client_accounts_remove. An account number cannot appear in both lists. Additions and removals use separate requests and are not atomic: add is attempted first, then remove, even if the add request fails. The tool reports request outcomes, which do not guarantee success for every account. A request error may leave the outcome unknown.

Input schema (from the production MCP catalog):

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "group_id": {
      "description": "Identifier of the rebate group whose membership to change.",
      "type": "integer"
    },
    "client_accounts_add": {
      "description": "Client account numbers as integer strings to add. Resets their individual rebate percentages to zero. An account cannot also appear in client_accounts_remove. Omit or pass an empty list to skip adding.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 0,
      "type": "array"
    },
    "client_accounts_remove": {
      "description": "Client account numbers as integer strings to remove. Resets their individual rebate percentages to zero. An account cannot also appear in client_accounts_add. Omit or pass an empty list to skip removing.",
      "items": {
        "pattern": "^\\d+$",
        "type": "string"
      },
      "maxItems": 100,
      "minItems": 0,
      "type": "array"
    }
  },
  "required": [
    "group_id"
  ]
}
```

