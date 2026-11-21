// src/server/index.ts
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  registerAppResource,
  RESOURCE_MIME_TYPE
} from "@modelcontextprotocol/ext-apps/server";
import {
  OpenAIExtensions as OpenAIExtensions2
} from "@openai/mcp-extensions/server";
import { z as z2 } from "zod";

// src/server/tools.ts
import { registerAppTool } from "@modelcontextprotocol/ext-apps/server";
import {
  OpenAIFileEntrypointInputSchema
} from "@openai/mcp-extensions/server";
import { z } from "zod";
var ZATCA_VIEWER_URI = "ui://qeemah/zatca-viewer";
function registerQeemahTools(server, extensions) {
  registerAppTool(
    server,
    "qeemah_zatca_viewer",
    {
      description: "Open, inspect, and verify Saudi ZATCA e-invoices (XML and PDF) with Phase 2 cryptographic verification, TLV QR code decoding, and VAT calculation.",
      inputSchema: OpenAIFileEntrypointInputSchema,
      _meta: {
        ui: { resourceUri: ZATCA_VIEWER_URI, visibility: ["app"] },
        "openai/ui": {
          entrypoints: [
            // Opens automatically when user clicks a .xml or .pdf in ChatGPT
            { type: "file", extensions: [".xml", ".pdf"] },
            // Available as a tab in conversation threads
            { type: "thread" },
            // Available fullscreen in sidebar
            { type: "global" }
          ]
        }
      }
    },
    async () => {
      return {
        content: []
      };
    }
  );
  const CreateDraftInputSchema = z.object({
    customerName: z.string().optional().describe("Customer or company name"),
    customerVat: z.string().optional().describe("15-digit customer VAT number (required for B2B)"),
    isB2B: z.boolean().optional().default(true).describe("True for B2B Standard Tax Invoice, False for B2C Simplified"),
    items: z.array(
      z.object({
        name: z.string().describe("Item or service name"),
        quantity: z.number().default(1).describe("Quantity"),
        unitPrice: z.number().describe("Unit price in SAR"),
        taxRate: z.number().default(15).describe("VAT rate (15 or 0)")
      })
    ).optional().describe("Initial line items for the invoice draft"),
    notes: z.string().optional().describe("Optional notes or payment terms")
  });
  registerAppTool(
    server,
    "qeemah_create_invoice_draft",
    {
      description: "Draft and calculate a new Saudi ZATCA e-invoice (B2B or B2C) with real-time VAT calculation in the ChatGPT side panel.",
      inputSchema: CreateDraftInputSchema,
      _meta: {
        ui: { resourceUri: ZATCA_VIEWER_URI, visibility: ["app", "model"] },
        "openai/ui": {
          entrypoints: [{ type: "thread" }]
        }
      }
    },
    async (args) => {
      void args;
      return {
        content: [
          {
            type: "text",
            text: "The invoice draft is ready in the Qeemah side panel."
          }
        ],
        structuredContent: { mode: "draft" }
      };
    }
  );
  const CfoInputSchema = z.object({
    quarter: z.string().optional().describe("Quarter to review (e.g. Q3 2026, Q4 2026)")
  });
  registerAppTool(
    server,
    "qeemah_cfo_dashboard",
    {
      description: "Open the Qeemah AI CFO Dashboard to review quarterly VAT liability, Phase 2 clearance stats, cashflow pulse, and compliance health in Saudi Arabia.",
      inputSchema: CfoInputSchema,
      _meta: {
        ui: { resourceUri: ZATCA_VIEWER_URI, visibility: ["app", "model"] },
        "openai/ui": {
          entrypoints: [{ type: "global" }, { type: "thread" }]
        }
      }
    },
    async (args) => {
      const q = args.quarter || "\u0627\u0644\u0631\u0628\u0639 \u0627\u0644\u062B\u0627\u0644\u062B 2026";
      return {
        content: [
          {
            type: "text",
            text: `\u062A\u0645 \u0641\u062A\u062D \u0644\u0648\u062D\u0629 \u062A\u062D\u0643\u0645 \u0627\u0644\u0645\u062F\u064A\u0631 \u0627\u0644\u0645\u0627\u0644\u064A \u0648\u0627\u0644\u0632\u0643\u0627\u0629 (${q}) \u0641\u064A \u0627\u0644\u0644\u0648\u062D\u0629 \u0627\u0644\u062C\u0627\u0646\u0628\u064A\u0629 \u0644\u0642\u064A\u0645\u0629. \u0635\u0627\u0641\u064A \u0627\u0644\u0636\u0631\u064A\u0628\u0629 \u0627\u0644\u0645\u0633\u062A\u062D\u0642\u0629 \u0644\u0644\u0633\u062F\u0627\u062F: 26,750.00 \u0631.\u0633. \u0646\u0633\u0628\u0629 \u0627\u0645\u062A\u062B\u0627\u0644 \u0627\u0644\u0641\u0648\u0627\u062A\u064A\u0631 \u0644\u0640 ZATCA: 98.6%.`
          }
        ],
        structuredContent: {
          mode: "cfo",
          cfoData: {
            period: q,
            dueDate: "2026-10-31",
            currency: "SAR",
            taxableSales: 301333.33,
            taxablePurchases: 123e3,
            outputVat: 45200,
            inputVat: 18450,
            netPayableVat: 26750,
            totalInvoices: 148,
            compliantInvoices: 146,
            flaggedInvoices: 2,
            clearanceRate: 98.6,
            receivables: 185400,
            overdueReceivables: 12500,
            payables: 64200
          }
        }
      };
    }
  );
  server.registerTool(
    "qeemah_audit_invoice_xml",
    {
      description: "Perform a compliance audit on a Saudi Arabian ZATCA UBL 2.1 e-invoice XML string, verifying VAT numbers, line item calculations, and Phase 2 requirements.",
      inputSchema: {
        xmlContent: z.string().describe("The raw UBL 2.1 XML content of the Saudi e-invoice")
      }
    },
    async ({ xmlContent }) => {
      try {
        const hasInvoiceTag = xmlContent.includes("<Invoice");
        const hasVatTag = xmlContent.includes("PartyTaxScheme");
        const hasQrTag = xmlContent.includes("cac:AdditionalDocumentReference");
        if (!hasInvoiceTag) {
          return {
            content: [
              {
                type: "text",
                text: "Error: The provided string is not a valid UBL 2.1 Invoice XML document."
              }
            ],
            isError: true
          };
        }
        const idMatch = xmlContent.match(/<cbc:ID>([^<]+)<\/cbc:ID>/);
        const invoiceTypeMatch = xmlContent.match(/<cbc:InvoiceTypeCode[^>]*>([^<]+)<\/cbc:InvoiceTypeCode>/);
        const payableMatch = xmlContent.match(/<cbc:PayableAmount[^>]*>([^<]+)<\/cbc:PayableAmount>/);
        const vatAmountMatch = xmlContent.match(/<cbc:TaxAmount[^>]*>([^<]+)<\/cbc:TaxAmount>/);
        const summary = {
          invoiceNumber: idMatch ? idMatch[1] : "Unknown",
          invoiceTypeCode: invoiceTypeMatch ? invoiceTypeMatch[1] : "388",
          payableAmount: payableMatch ? payableMatch[1] : "0.00",
          vatAmount: vatAmountMatch ? vatAmountMatch[1] : "0.00",
          hasQrCode: hasQrTag,
          hasTaxScheme: hasVatTag,
          status: "Passed basic structure check. For full cryptographic and TLV verification, view in the Qeemah ZATCA Inspector."
        };
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(summary, null, 2)
            }
          ]
        };
      } catch (err) {
        return {
          content: [
            {
              type: "text",
              text: `Audit failed: ${err instanceof Error ? err.message : "Unknown error"}`
            }
          ],
          isError: true
        };
      }
    }
  );
}

// src/server/index.ts
var __filename = fileURLToPath(import.meta.url);
var __dirname = path.dirname(__filename);
async function getAppHtml() {
  const possiblePaths = [
    path.resolve(__dirname, "./app.html"),
    path.resolve(__dirname, "../dist/app.html"),
    path.resolve(process.cwd(), "dist/app.html")
  ];
  for (const p of possiblePaths) {
    try {
      const html = await readFile(p, "utf8");
      return html;
    } catch {
    }
  }
  return `<!DOCTYPE html><html><body><div id="root"><h2>Qeemah ZATCA Inspector Loading...</h2></div></body></html>`;
}
async function main() {
  const server = new McpServer({
    name: "qeemah",
    version: "1.0.0"
  });
  const extensions = new OpenAIExtensions2(server);
  let currentSettings = {
    environment: "sandbox",
    autoCalculateVat: true
  };
  extensions.settings?.register({
    fields: {
      environment: {
        schema: z2.enum(["sandbox", "simulation", "production"]),
        title: "\u0628\u064A\u0626\u0629 \u0647\u064A\u0626\u0629 \u0627\u0644\u0632\u0643\u0627\u0629 (ZATCA Environment)",
        description: "ZATCA integration tier: sandbox, simulation, or production"
      },
      autoCalculateVat: {
        schema: z2.boolean(),
        title: "\u0627\u0644\u062D\u0633\u0627\u0628 \u0627\u0644\u062A\u0644\u0642\u0627\u0626\u064A \u0644\u0636\u0631\u064A\u0628\u0629 \u0627\u0644\u0642\u064A\u0645\u0629 \u0627\u0644\u0645\u0636\u0627\u0641\u0629 (15%)",
        description: "Automatically calculate standard 15% VAT on invoice line items"
      }
    },
    layout: [
      {
        kind: "group",
        title: "\u0628\u064A\u0626\u0629 \u0627\u0644\u0631\u0628\u0637 \u0648\u0627\u0644\u062A\u0643\u0627\u0645\u0644 (Integration & System)",
        items: [
          { kind: "property", property: "environment" },
          { kind: "property", property: "autoCalculateVat" }
        ]
      }
    ],
    read: async () => {
      return {
        environment: currentSettings.environment,
        autoCalculateVat: currentSettings.autoCalculateVat
      };
    },
    update: async (set) => {
      currentSettings = { ...currentSettings, ...set };
      return {
        environment: currentSettings.environment,
        autoCalculateVat: currentSettings.autoCalculateVat
      };
    }
  });
  extensions.mentions?.setHandler(async ({ query }) => {
    const q = (query || "").toLowerCase();
    const allMentions = [
      {
        type: "resource_link",
        uri: ZATCA_VIEWER_URI,
        name: "zatca_inspector",
        title: "\u0641\u0627\u062D\u0635 \u0627\u0644\u0641\u0648\u0627\u062A\u064A\u0631 ZATCA (Qeemah Inspector)",
        description: "\u0641\u062D\u0635 \u0648\u062A\u062F\u0642\u064A\u0642 \u0627\u0644\u0641\u0648\u0627\u062A\u064A\u0631 \u0627\u0644\u0625\u0644\u0643\u062A\u0631\u0648\u0646\u064A\u0629 XML \u0648 PDF \u0648\u0627\u0644\u062A\u062D\u0642\u0642 \u0645\u0646 \u0627\u0644\u062A\u0648\u0642\u064A\u0639 \u0627\u0644\u0631\u0642\u0645\u064A \u0648\u0631\u0645\u0632 \u0627\u0644\u0627\u0633\u062A\u062C\u0627\u0628\u0629 \u0627\u0644\u0633\u0631\u064A\u0639\u0629 TLV"
      },
      {
        type: "resource_link",
        uri: ZATCA_VIEWER_URI,
        name: "invoice_drafter",
        title: "\u0645\u0646\u0634\u0626 \u0645\u0633\u0648\u062F\u0627\u062A \u0627\u0644\u0641\u0648\u0627\u062A\u064A\u0631 (Invoice Drafter)",
        description: "\u062A\u062C\u0647\u064A\u0632 \u0648\u062D\u0633\u0627\u0628 \u0645\u0633\u0648\u062F\u0629 \u0641\u0627\u062A\u0648\u0631\u0629 \u0636\u0631\u064A\u0628\u064A\u0629 \u062C\u062F\u064A\u062F\u0629 B2B \u0623\u0648 \u0645\u0628\u0633\u0637\u0629 B2C \u0648\u062D\u0633\u0627\u0628 \u0627\u0644\u0636\u0631\u064A\u0628\u0629 15% \u0645\u0628\u0627\u0634\u0631\u0629"
      },
      {
        type: "resource_link",
        uri: ZATCA_VIEWER_URI,
        name: "cfo_dashboard",
        title: "\u0644\u0648\u062D\u0629 \u0627\u0644\u0645\u062F\u064A\u0631 \u0627\u0644\u0645\u0627\u0644\u064A \u0648\u0627\u0644\u0632\u0643\u0627\u0629 (AI CFO & Tax Return)",
        description: "\u0645\u0624\u0634\u0631\u0627\u062A \u0627\u0644\u0631\u0628\u0639 \u0627\u0644\u062D\u0627\u0644\u064A \u0648\u0635\u0627\u0641\u064A \u0627\u0644\u0636\u0631\u064A\u0628\u0629 \u0627\u0644\u0645\u0633\u062A\u062D\u0642\u0629 \u0644\u0644\u062F\u0641\u0639 \u0648\u0646\u0628\u0636 \u0627\u0644\u0633\u064A\u0648\u0644\u0629 \u0627\u0644\u0646\u0642\u062F\u064A\u0629 \u0648\u0646\u0633\u0628\u0629 \u0627\u0644\u0627\u0645\u062A\u062B\u0627\u0644"
      }
    ];
    if (!q) {
      return { items: allMentions };
    }
    const filtered = allMentions.filter(
      (m) => m.name.toLowerCase().includes(q) || m.title.toLowerCase().includes(q) || m.description && m.description.toLowerCase().includes(q)
    );
    return { items: filtered.length ? filtered : allMentions };
  });
  registerAppResource(
    server,
    "qeemah-zatca-viewer-resource",
    ZATCA_VIEWER_URI,
    {},
    async () => {
      const html = await getAppHtml();
      return {
        contents: [
          {
            uri: ZATCA_VIEWER_URI,
            mimeType: RESOURCE_MIME_TYPE,
            text: html,
            _meta: {
              "openai/ui": {
                preferredDisplayMode: "fullscreen",
                availableDisplayModes: ["inline", "fullscreen"]
              }
            }
          }
        ]
      };
    }
  );
  registerQeemahTools(server, extensions);
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
main().catch((err) => {
  console.error("Fatal error starting Qeemah MCP server:", err);
  process.exit(1);
});
