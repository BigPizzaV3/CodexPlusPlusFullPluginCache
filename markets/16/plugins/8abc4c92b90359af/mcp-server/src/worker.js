import { createMcpHandler } from 'agents/mcp/server';
import { McpServer } from '@modelcontextprotocol/server';
import { z } from 'zod';
import { SERVER_INFO, validateBrief, validateOutput, buildManifest } from './core.js';

const textResult = (value) => ({
  content: [{ type: 'text', text: JSON.stringify(value, null, 2) }]
});

function createServer() {
  const server = new McpServer({
    name: SERVER_INFO.name,
    version: SERVER_INFO.version
  });

  server.registerTool(
    'validate_product_brief',
    {
      description: 'Validate a product brief and return missing or weak fields without inventing product facts.',
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false
      },
      inputSchema: {
        brandProductName: z.string(),
        productDetailsUSP: z.string().optional(),
        targetAudience: z.string().optional(),
        narration: z.enum(['yes', 'no', 'Ya', 'Tidak']).optional(),
        wardrobe: z.string().optional(),
        location: z.string().optional(),
        language: z.string().optional(),
        productLink: z.string().optional(),
        mode: z.enum(['Normal', 'Deep Research']).optional(),
        hasCharacterReference: z.boolean().optional(),
        hasProductReference: z.boolean().optional()
      }
    },
    async (args) => textResult(validateBrief(args))
  );

  server.registerTool(
    'validate_production_output',
    {
      description: 'Check that a production package contains three six-panel 2x3 storyboards, three connected video prompts, continuity locks, negative prompt, summary, and checklist.',
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false
      },
      inputSchema: {
        storyboards: z.array(z.any()),
        videoPrompts: z.array(z.any()),
        characterContinuityLock: z.string().optional(),
        productContinuityLock: z.string().optional(),
        negativePrompt: z.string().optional(),
        storySummary: z.string().optional(),
        productionChecklist: z.array(z.any()).optional()
      }
    },
    async (args) => {
      const result = validateOutput(args);
      return { ...textResult(result), isError: !result.valid };
    }
  );

  server.registerTool(
    'build_production_manifest',
    {
      description: 'Normalize the production brief and deliverable counts into a compact JSON manifest. Does not generate images or video.',
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false
      },
      inputSchema: {
        projectName: z.string().optional(),
        brandProductName: z.string(),
        targetAudience: z.string().optional(),
        language: z.string().optional(),
        aspectRatio: z.string().optional(),
        sceneDurationSeconds: z.number().optional(),
        storyboardCount: z.number().optional(),
        panelsPerStoryboard: z.number().optional(),
        videoPromptCount: z.number().optional(),
        narration: z.boolean().optional(),
        cta: z.string().optional()
      }
    },
    async (args) => textResult(buildManifest(args))
  );

  return server;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    // OpenAI domain verification challenge
    if (url.pathname === '/.well-known/openai-apps-challenge' && request.method === 'GET') {
      return new Response('8a2MsGKE7kdsxuI3lpKoGk1oWBypoZ5Z6F89v5D0pPQ', {
        status: 200,
        headers: {
          'content-type': 'text/plain; charset=utf-8',
          'cache-control': 'no-store'
        }
      });
    }
    if (url.pathname === '/health') {
      return new Response(JSON.stringify({
        status: 'ok',
        service: 'wowseru-ai-affiliate-storyboard-mcp',
        transport: 'streamable-http'
      }), {
        headers: {
          'content-type': 'application/json; charset=utf-8',
          'cache-control': 'no-store'
        }
      });
    }
    if (url.pathname !== '/mcp') return new Response('Not found', { status: 404 });
    return createMcpHandler(createServer)(request, env, ctx);
  }
};
