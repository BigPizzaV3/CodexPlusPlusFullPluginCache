import { readFileSync } from 'node:fs';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { registerAppResource, registerAppTool, RESOURCE_MIME_TYPE } from '@modelcontextprotocol/ext-apps/server';
import { z } from 'zod';
import { calculate, summary, NOTICE, ASSUMPTION, InputError, INPUT_MAX_LENGTH } from './calculator.mjs';

export const RESOURCE_URI = 'ui://peptide-concentration/calculator-v4.html';
const inputSchema = z.object({
  mass: z.string().max(INPUT_MAX_LENGTH).describe('User-provided mass as a decimal string. Never select an amount for the user.'),
  massUnit: z.enum(['mg', 'mcg']),
  volume: z.string().max(INPUT_MAX_LENGTH).describe('User-provided final total solution volume, not merely liquid added, as a decimal string.'),
  volumeUnit: z.enum(['mL', 'uL'])
}).strict();
const annotations = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false };

export function createCalculatorServer() {
  const server = new McpServer({ name: 'peptide-reconstitution-calculator', version: '0.5.0' });
  const ui = { resourceUri: RESOURCE_URI };
  registerAppResource(server, 'concentration-calculator', RESOURCE_URI, { title: 'Peptide Reconstitution Calculator by Peptara Labs' }, async () => ({
    contents: [{ uri: RESOURCE_URI, mimeType: RESOURCE_MIME_TYPE,
      text: readFileSync(new URL('../dist/calculator.html', import.meta.url), 'utf8'),
      _meta: { ui: { domain: 'https://peptara-calculator.vercel.app', prefersBorder: true, csp: { connectDomains: [], resourceDomains: [] } },
        'openai/widgetDescription': 'An educational concentration calculator using user-supplied mass and final solution volume.' }
    }]
  }));

  registerAppTool(server, 'open_concentration_calculator', {
    title: 'Open Peptide Reconstitution Calculator',
    description: 'Open the blank interactive calculator for educational peptide concentration arithmetic. Does not select amounts, recommend a fluid, or provide dosing or preparation instructions.',
    inputSchema: z.object({}).strict(), annotations,
    _meta: { ui, 'openai/ui': { entrypoints: [{ type: 'thread' }] } }
  }, async () => ({
    content: [{ type: 'text', text: `Enter a mass with units and the final solution volume with units. ${NOTICE} ${ASSUMPTION}` }],
    structuredContent: { mode: 'empty' }
  }));

  registerAppTool(server, 'calculate_concentration', {
    title: 'Calculate educational concentration',
    description: 'Divide a user-supplied peptide mass by the user-supplied final total solution volume. Returns mg/mL and mcg/mL with the formula. Ask for missing or ambiguous values; never infer them or substitute liquid-added volume. Does not calculate doses, administration volumes, or syringe units.',
    inputSchema, annotations, _meta: { ui }
  }, async (input) => {
    try {
      const result = calculate(input);
      return { content: [{ type: 'text', text: summary(result) }], structuredContent: { mode: 'result', result } };
    } catch (error) {
      if (!(error instanceof InputError)) throw error;
      return { isError: true, content: [{ type: 'text', text: error.message }], structuredContent: { mode: 'error', field: error.field, message: error.message } };
    }
  });
  return server;
}
