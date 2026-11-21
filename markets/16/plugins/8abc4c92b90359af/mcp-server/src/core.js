export const SERVER_INFO = { name: 'wowseru-ai-affiliate-storyboard', version: '0.1.0' };
export const PROTOCOL_VERSION = '2025-03-26';

export const TOOL_DEFINITIONS = [
  {
    name: 'validate_product_brief',
    description: 'Validate a product brief and return missing or weak fields without inventing product facts.',
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    inputSchema: {
      type: 'object',
      properties: {
        brandProductName: { type: 'string' },
        productDetailsUSP: { type: 'string' },
        targetAudience: { type: 'string' },
        narration: { type: 'string', enum: ['yes', 'no', 'Ya', 'Tidak'] },
        wardrobe: { type: 'string' },
        location: { type: 'string' },
        language: { type: 'string' },
        productLink: { type: 'string' },
        mode: { type: 'string', enum: ['Normal', 'Deep Research'] },
        hasCharacterReference: { type: 'boolean' },
        hasProductReference: { type: 'boolean' }
      },
      required: ['brandProductName'],
      additionalProperties: true
    }
  },
  {
    name: 'validate_production_output',
    description: 'Check that a production package contains three six-panel 2x3 storyboards, three connected video prompts, continuity locks, negative prompt, summary, and checklist.',
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    inputSchema: {
      type: 'object',
      properties: {
        storyboards: { type: 'array', items: { type: 'object' } },
        videoPrompts: { type: 'array' },
        characterContinuityLock: { type: 'string' },
        productContinuityLock: { type: 'string' },
        negativePrompt: { type: 'string' },
        storySummary: { type: 'string' },
        productionChecklist: { type: 'array' }
      },
      required: ['storyboards', 'videoPrompts'],
      additionalProperties: true
    }
  },
  {
    name: 'build_production_manifest',
    description: 'Normalize the production brief and deliverable counts into a compact JSON manifest. Does not generate images or video.',
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false },
    inputSchema: {
      type: 'object',
      properties: {
        projectName: { type: 'string' },
        brandProductName: { type: 'string' },
        targetAudience: { type: 'string' },
        language: { type: 'string' },
        aspectRatio: { type: 'string', default: '9:16' },
        sceneDurationSeconds: { type: 'number', default: 10 },
        storyboardCount: { type: 'number', default: 3 },
        panelsPerStoryboard: { type: 'number', default: 6 },
        videoPromptCount: { type: 'number', default: 3 },
        narration: { type: 'boolean', default: true },
        cta: { type: 'string' }
      },
      required: ['brandProductName'],
      additionalProperties: true
    }
  }
];

const textResult = (value) => ({ content: [{ type: 'text', text: JSON.stringify(value, null, 2) }] });
const nonEmpty = (v) => typeof v === 'string' && v.trim().length > 0;

export function validateBrief(brief = {}) {
  const required = [
    ['brandProductName', 'Nama brand dan produk'],
    ['productDetailsUSP', 'Detail produk dan USP'],
    ['targetAudience', 'Target audience'],
    ['language', 'Bahasa narasi']
  ];
  const missing = required.filter(([key]) => !nonEmpty(brief[key])).map(([, label]) => label);
  const optionalMissing = [
    ['narration', 'Preferensi narasi'],
    ['location', 'Lokasi/setting'],
    ['mode', 'Mode Normal atau Deep Research']
  ].filter(([key]) => brief[key] === undefined || brief[key] === null || brief[key] === '').map(([, label]) => label);
  return {
    validForConcept: missing.length === 0,
    missingRequired: missing,
    optionalFollowUps: optionalMissing,
    referenceStatus: {
      character: brief.hasCharacterReference ? 'provided' : 'not provided; define a fictional consistent character if needed',
      product: brief.hasProductReference ? 'provided' : 'not provided; rely only on supplied product facts'
    },
    instruction: 'Do not infer or fabricate product specifications, ingredients, price, certifications, or performance claims.'
  };
}

export function validateOutput(output = {}) {
  const issues = [];
  const stories = Array.isArray(output.storyboards) ? output.storyboards : [];
  const videos = Array.isArray(output.videoPrompts) ? output.videoPrompts : [];
  if (stories.length !== 3) issues.push(`Expected exactly 3 storyboards; received ${stories.length}.`);
  stories.forEach((story, index) => {
    const panels = Array.isArray(story.panels) ? story.panels : [];
    if (story.grid !== '2x3' && story.grid !== '2×3') issues.push(`Storyboard ${index + 1} must explicitly declare a 2x3 grid.`);
    if (panels.length !== 6) issues.push(`Storyboard ${index + 1} must contain exactly 6 panels; received ${panels.length}.`);
    if (story.grid && story.grid !== '2x3' && story.grid !== '2×3') issues.push(`Storyboard ${index + 1} grid must be 2x3.`);
  });
  if (videos.length !== 3) issues.push(`Expected exactly 3 video prompts; received ${videos.length}.`);
  for (const [key, label] of [
    ['characterContinuityLock', 'Character Continuity Lock'],
    ['productContinuityLock', 'Product Continuity Lock'],
    ['negativePrompt', 'Negative Prompt'],
    ['storySummary', 'Story summary']
  ]) if (!nonEmpty(output[key])) issues.push(`${label} is missing.`);
  if (!Array.isArray(output.productionChecklist) || output.productionChecklist.length === 0) issues.push('Production checklist is missing or empty.');
  return { valid: issues.length === 0, issues, checked: { storyboardCount: stories.length, panelCounts: stories.map(s => Array.isArray(s.panels) ? s.panels.length : 0), videoPromptCount: videos.length } };
}

export function buildManifest(input = {}) {
  const scenes = Number.isFinite(input.storyboardCount) ? input.storyboardCount : 3;
  const duration = Number.isFinite(input.sceneDurationSeconds) ? input.sceneDurationSeconds : 10;
  return {
    projectName: input.projectName || input.brandProductName,
    brandProductName: input.brandProductName,
    targetAudience: input.targetAudience || null,
    language: input.language || null,
    format: { aspectRatio: input.aspectRatio || '9:16', sceneCount: scenes, secondsPerScene: duration, totalDurationSeconds: scenes * duration },
    deliverables: { storyboardPrompts: scenes, panelsPerStoryboard: input.panelsPerStoryboard ?? 6, videoPrompts: input.videoPromptCount ?? scenes, narration: input.narration ?? true, negativePrompt: true, continuityLocks: ['character', 'product', 'scene'], storySummary: true, productionChecklist: true },
    cta: input.cta || null,
    generationNote: 'This manifest describes prompts and production planning; it does not represent rendered image or video files.'
  };
}

export async function handleToolCall(name, args = {}) {
  if (name === 'validate_product_brief') return textResult(validateBrief(args));
  if (name === 'validate_production_output') {
    const result = validateOutput(args);
    return { ...textResult(result), isError: !result.valid };
  }
  if (name === 'build_production_manifest') return textResult(buildManifest(args));
  return { ...textResult({ error: `Unknown tool: ${name}` }), isError: true };
}

export function rpcResponse(id, result) { return { jsonrpc: '2.0', id, result }; }
export function rpcError(id, code, message) { return { jsonrpc: '2.0', id: id ?? null, error: { code, message } }; }

export async function handleRpc(message) {
  if (!message || message.jsonrpc !== '2.0' || typeof message.method !== 'string') return rpcError(message?.id, -32600, 'Invalid JSON-RPC request');
  const id = message.id;
  const params = message.params || {};
  if (message.method.startsWith('notifications/')) return null;
  if (message.method === 'initialize') {
    return rpcResponse(id, {
      protocolVersion: params.protocolVersion || PROTOCOL_VERSION,
      capabilities: { tools: {} },
      serverInfo: SERVER_INFO,
      instructions: 'WOWSERU AI Affiliate Storyboard validates briefs and production package structure. Creative story and prompt generation is guided by the plugin skill.'
    });
  }
  if (message.method === 'ping') return rpcResponse(id, {});
  if (message.method === 'tools/list') return rpcResponse(id, { tools: TOOL_DEFINITIONS });
  if (message.method === 'tools/call') {
    if (!params.name || typeof params.name !== 'string') return rpcError(id, -32602, 'Missing tool name');
    const result = await handleToolCall(params.name, params.arguments || {});
    return rpcResponse(id, result);
  }
  return rpcError(id, -32601, `Method not found: ${message.method}`);
}
