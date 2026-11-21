# Qeemah Accounting & ZATCA E-Invoicing (ChatGPT Plugin Extension)

A Qeemah plugin package with a local stdio UI and an authenticated remote MCP endpoint. Marketplace approval and production OAuth validation are separate release requirements.

The remote server reads permitted organization data, audits supplied XML, and calculates invoice drafts. It does not save, send, file, or submit invoices, and does not serve the local package's custom UI.

## Remote Account Connection

The public configuration in `mcp.json` points to `https://api.qeemahcloud.com/api/v1/mcp`. Better Auth supplies OAuth discovery, S256 PKCE, client metadata discovery (CIMD), consent, token issuance, and refresh. Do not add a password or access token to the plugin manifest.

Users connect from the ChatGPT/Codex host, sign in on Qeemah, and approve read-only access. ChatGPT then sends an access token on each MCP request. The backend verifies its signature, issuer, MCP audience, expiry, and `mcp:read` scope, checks account availability, and resolves organization membership for private tools. The profile tool identifies the connected account using its existing immutable user ID.

Before enabling this in production:

1. Deploy the generated backend OAuth migration through the normal release process. Do not use schema push on production.
2. Deploy the backend and frontend changes together. The frontend must serve `/oauth/continue` and `/oauth/consent` as SPA routes.
3. Keep `BETTER_AUTH_URL` set to the canonical API origin and `BETTER_AUTH_SECRET` stable. The first `CORS_ORIGIN` entry must be the Qeemah application origin, such as `https://app.qeemahcloud.com`. The frontend's `VITE_BETTER_AUTH_URL` must address the API's `/api/auth` endpoint, and `VITE_API_URL` must address the same API.
4. Refresh the MCP connection or run Scan Tools again in the plugin builder. Select OAuth and CIMD when the builder asks for authentication/client identification. OAuth linking is provided by the host, not a button embedded in `plugin.json`.

Discovery URLs on the production API:

- `/.well-known/oauth-protected-resource`
- `/.well-known/oauth-protected-resource/api/v1/mcp`
- `/.well-known/oauth-authorization-server/api/auth`
- `/api/auth/.well-known/openid-configuration`
- `/api/auth/jwks`

Unauthenticated MCP requests return `401` with `WWW-Authenticate` discovery information; insufficient scope returns `403` with a scope challenge. This release requires authentication for the whole endpoint, including XML audits. CIMD is enabled; unauthenticated dynamic registration is not enabled.

Access tokens expire after five minutes. Refresh-token rotation is handled by Better Auth. Published tool names remain unchanged, and `qeemah_get_profile` is added for account identification. Runtime OAuth, MCP Inspector, and production connection testing remain required before submission.

---

## Architecture & Surface Entrypoints

```
               ┌────────────────────────────────────────────────────────┐
               │              ChatGPT Native Host Surfaces              │
               └───────┬───────────────────┬────────────────────┬───────┘
                       │                   │                    │
              [type: "file"]      [type: "thread"]     [type: "global"]
             (.xml / .pdf click) (Composer / Drafter)  (Sidebar CFO tab)
                       │                   │                    │
                       └───────────────────┼────────────────────┘
                                           ▼
               ┌────────────────────────────────────────────────────────┐
               │    Qeemah UI Client (React 19 • RTL/LTR • Dark Mode)   │
               │   dist/app.html (Inlined bundle served via MCP App)    │
               │                                                        │
               │  [🔍 ZATCA Inspector] [✏️ Drafter] [📊 AI CFO Pulse]    │
               └───────────────────────────┬────────────────────────────┘
                                           │ JSON-RPC PostMessage / Stdio
                                           ▼
               ┌────────────────────────────────────────────────────────┐
               │         Qeemah Stdio MCP Server (dist/server.js)       │
               │                                                        │
               │  • qeemah_zatca_viewer       (File / Thread / Global)  │
               │  • qeemah_create_invoice_draft (Live Drafter & XML)    │
               │  • qeemah_cfo_dashboard      (Quarterly VAT Pulse)     │
               │  • qeemah_audit_invoice_xml  (Headless Direct Audit)   │
               │  • settings.read / update    (Structured Settings)     │
               │  • search_mentions           (Composer @qeemah)        │
               └────────────────────────────────────────────────────────┘
```

---

## Key Features by Phase

### Phase 1: ZATCA E-Invoice Inspector & Cryptographic Validator
- **File Extension Handler (`type: "file"`, `.xml`, `.pdf`)**: Opens automatically whenever a user clicks a ZATCA XML invoice or PDF in ChatGPT.
- **Phase 2 Cryptographic Audit & Validation**:
  - **BR-KSA-01**: Verifies 15-digit KSA VAT numbers (`^3\d{13}3$`).
  - **BR-KSA-02**: Validates invoice document types (`388` = Tax Invoice, `381` = Credit Note, `383` = Debit Note).
  - **BR-KSA-03**: Currency validation (must be `SAR` for domestic transactions).
  - **BR-KSA-04**: Decodes Base64 TLV QR codes across Phase 1 (Tags 1–5) and Phase 2 (Tags 6–8: SHA-256 Digest, Digital Signature, ECDSA Public Key).
  - **BR-KSA-06 & 07**: Strict arithmetic consistency checking between line extensions, 15% VAT sub-totals, invoice payable amounts, and QR code payloads.
  - **BR-KSA-08**: Verifies Hash Chains (Previous Invoice Hash - PIH) and X.509 digital certificates.
- **Bilingual UI (Arabic & English)**: Responsive RTL/LTR layouts matching ChatGPT's design system and dark/light themes. Tabs for *Summary*, *Line Items*, *QR & Cryptography*, and *Raw UBL 2.1 XML*.
- **Bidirectional ChatGPT Model Context Sync (`ui/update-model-context`)**: "Sync to Chat" attaches structured invoice metadata to the ChatGPT composer.
- **Headless Chat Tool (`qeemah_audit_invoice_xml`)**: Direct XML string audits directly in conversation flows.

### Phase 2: Live Thread Invoice Drafter & Quote Builder
- **Thread Entrypoint (`type: "thread"`)**: ChatGPT can programmatically launch and pre-fill invoice drafts from prompts (e.g. *"Quote ABC Corp for SAR 8,000 consulting"*).
- **Interactive In-App Drafter**:
  - B2B Standard Tax Invoice (`0100000`) vs B2C Simplified Tax Invoice (`0200000`) toggle.
  - Live customer 15-digit VAT number format verification.
  - Dynamic line item addition, deletion, and recalculation.
  - Real-time 15% VAT calculations (Subtotal, VAT, Grand Total).
- **Compliant UBL 2.1 XML Generator**:
  - Encodes mandatory KSA-5 supply date (`<cbc:ActualDeliveryDate>`).
  - Generates valid Phase 2 TLV QR codes with tags 1–5 (and cryptographic stamps if signed).
- **Bidirectional Actions**:
  - **⚡ Sync Draft to Chat**: Passes live draft summary and JSON to ChatGPT's model context.
  - **💬 Ask ChatGPT to Review**: Sends an automated audit prompt to the active thread.
  - **📄 Generate & Inspect XML**: Directly loads generated UBL XML into the ZATCA Inspector tab.

### Phase 3: AI CFO Dashboard, Settings & Composer Mentions
- **Global Entrypoint (`type: "global"`)**: Full-screen and sidebar AI CFO dashboard available across all conversations.
- **Quarterly VAT Liability Return Pulse**:
  - Live Output VAT vs Deductible Input VAT vs Net Payable to ZATCA.
  - Tax period return countdown (due on the last day of the following month).
  - Phase 2 clearance rate percentage (e.g. 98.6% compliant).
  - Accounts receivable, overdue balances, and working capital indicators.
- **Structured Settings (`openai/settings`)**:
  - Server-managed configuration for Organization ID, Tax Registration Number, ZATCA Environment (`sandbox`, `simulation`, `production`), and VAT calculation toggles.
  - Native ChatGPT settings layout with grouped preferences.
- **Desktop Composer At-Mentions (`mentions/search`)**:
  - Type `@qeemah` in ChatGPT to directly link or open the Inspector, Drafter, or CFO Dashboard.

---

## Directory Structure

```
qeemah-chatgpt-plugin/
├── .codex-plugin/
│   └── plugin.json             # OpenAI Agent Plugins manifest (fallback)
├── assets/
│   ├── icon.svg                # 20x20 transparent monochrome SVG (light theme)
│   └── icon-dark.svg           # Monochrome SVG (dark theme)
├── dist/
│   ├── app.html                # Self-contained React 19 UI bundle (1.0MB, inlined CSS/JS)
│   └── server.js               # MCP Server bundle (NodeNext ESM)
├── scripts/
│   └── build.mjs               # Production builder (Vite + esbuild)
├── skills/
│   ├── zatca-auditor/
│   │   └── SKILL.md            # Auditor skill and system prompt for ZATCA inspection
│   ├── invoice-drafter/
│   │   └── SKILL.md            # Drafter skill for quoting and invoice building
│   └── cfo-advisor/
│       └── SKILL.md            # CFO advisory and VAT return filing instructions
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   ├── Header.tsx
│   │   │   ├── SummaryCards.tsx
│   │   │   ├── ComplianceBadge.tsx
│   │   │   ├── PartiesSection.tsx
│   │   │   ├── LineItemsTable.tsx
│   │   │   ├── CryptographySection.tsx
│   │   │   ├── RawXmlViewer.tsx
│   │   │   ├── InvoiceDrafter.tsx
│   │   │   └── CfoDashboard.tsx
│   │   ├── lib/
│   │   │   ├── tlv-decoder.ts
│   │   │   ├── zatca-parser.ts
│   │   │   ├── zatca-rules.ts
│   │   │   └── zatca-generator.ts
│   │   ├── index.html          # Host HTML template
│   │   ├── index.tsx           # React 19 app + MCP App connection + 3-mode switcher
│   │   └── styles.css          # Bilingual RTL/LTR styles adhering to ChatGPT design
│   └── server/
│       ├── index.ts            # McpServer + OpenAIExtensions + Stdio + Settings + Mentions
│       └── tools.ts            # App tools (viewer, drafter, cfo, audit)
├── tests/
│   ├── unit.test.ts            # Unit tests (TLV decoder, compliance rules, XML generator)
│   └── stdio.test.ts           # End-to-end JSON-RPC stdio protocol tests
├── .mcp.json                   # MCP Server definition
├── package.json
└── tsconfig.json
```

---

## Commands

Run from inside `qeemah-chatgpt-plugin/`:

| Command | Action |
| :--- | :--- |
| `pnpm install` | Install dependencies |
| `pnpm build` | Compile the self-contained UI bundle (`dist/app.html`) and server (`dist/server.js`) |
| `pnpm typecheck` | Run TypeScript validation (`tsc --noEmit`) |
| `pnpm test` | Run unit & stdio integration tests (`tsx tests/unit.test.ts && tsx tests/stdio.test.ts`) |
| `pnpm start` | Launch the MCP server over standard I/O |

---

## Verification & Test Results

```
✔ ZATCA TLV Decoder: decodes valid Phase 2 QR code (0.76ms)
✔ ZATCA TLV Decoder: rejects invalid base64 (0.09ms)
✔ ZATCA Compliance Rules: flags invalid VAT number and non-SAR currency (0.31ms)
✔ ZATCA Compliance Rules: passes fully compliant Phase 2 invoice (0.11ms)
✔ ZATCA XML Generator: generates compliant B2B UBL 2.1 XML with valid TLV QR (3.20ms)
✔ Stdio MCP Server Protocol & Tools Verification (178.46ms)
  - initialize: serverInfo "qeemah", tools & resources capabilities verified
  - tools/list: viewer, drafter, cfo, audit, settings.read, settings.update, search_mentions
  - resources/list: ui://qeemah/zatca-viewer (text/html;profile=mcp-app)
  - tools/call (qeemah_create_invoice_draft): returns mode: "draft" and structured lines
  - tools/call (qeemah_cfo_dashboard): returns mode: "cfo" and quarterly VAT pulse
  - tools/call (settings.read & update): reads and persists tenant preferences
  - tools/call (search_mentions): filters and returns @qeemah composer items
  - tools/call (qeemah_audit_invoice_xml): audits raw XML tags headlessly
```

---

## How to Install Locally in Codex

1. Build the plugin:
   ```bash
   cd qeemah-chatgpt-plugin
   pnpm build
   ```
2. From the repository root, register the included local marketplace and install Qeemah:
   ```bash
   codex plugin marketplace add /Users/mohaosman/project/qeemah-accounting
   codex plugin add qeemah --marketplace qeemah-local
   ```
3. Restart Codex, then ask it to audit a Saudi e-invoice or draft an invoice. The plugin's skills are available automatically; its local MCP server starts when a tool is needed.

The local stdio server in `.mcp.json` runs in Codex Desktop/CLI. The public `mcp.json` already points to the remote HTTPS endpoint. Local UI behavior and demo data must not be treated as production remote capabilities.
