// Run in Codex functions.exec only, after reading coordinate/SKILL.md.
// The host owns native tools. This file is not a daemon or standalone API client.
// Define helperPath and stateDir as verified absolute paths before this snippet.
const shellQuote = value => "'" + String(value).replaceAll("'", "'\\''") + "'";
async function cache(operation, payload = {}) {
  const command = `printf %s ${shellQuote(JSON.stringify(payload))} | python3 ${shellQuote(helperPath)} --state-dir ${shellQuote(stateDir)} ${shellQuote(operation)}`;
  const result = await tools.exec_command({cmd: command, shell: '/bin/sh', login: false, workdir: '/', max_output_tokens: 3000});
  if (result.exit_code !== 0) throw new Error('Unicycle cache operation failed; inspect its bounded error result.');
  return JSON.parse(result.output);
}
function nativeData(result) {
  if (result.isError) throw new Error('Native task tool failed; cursor remains unchanged.');
  const block = result.content?.find(item => item.type === 'text');
  if (!block) throw new Error('Native task tool returned no structured text.');
  return JSON.parse(block.text);
}
// Status orders least-recently-read owners first; partial native returns rotate durably.
const state = await cache('status', {offset: 0});
if (state.pendingSignals) {
  text(await cache('signals'));
  exit(); // Classify and persist events before ack-signals, then resume polling.
}
const targets = state.targets.map(({threadId, hostId, afterCursor}) => ({threadId, hostId, ...(afterCursor ? {afterCursor} : {})}));
if (!targets.length) throw new Error('Configure selected existing owners first.');
const snapshot = nativeData(await tools.mcp__codex_app__wait_threads({targets, timeoutMs: 0}));
// Keep only the documented compact poll fields, not full transcripts/tool arguments.
const polls = (snapshot.polls || []).map(p => ({
  thread: p.thread, cursor: p.cursor, latestTurn: p.latestTurn,
  latestAssistantMessage: p.latestAssistantMessage
}));
const result = await cache('ingest', {polls, errors: snapshot.errors || []});
// The model sees only changed compact signals; unchanged cycles remain quiet.
if (result.signals?.length || result.errors?.length) text(result);
