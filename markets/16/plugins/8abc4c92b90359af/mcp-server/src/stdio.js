import readline from 'node:readline';
import { handleRpc } from './core.js';

const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity, terminal: false });
rl.on('line', async (line) => {
  if (!line.trim()) return;
  try {
    const message = JSON.parse(line);
    const response = await handleRpc(message);
    if (response !== null && message.id !== undefined) process.stdout.write(`${JSON.stringify(response)}\n`);
  } catch (error) {
    process.stderr.write(`MCP request error: ${error?.message || String(error)}\n`);
    process.stdout.write(`${JSON.stringify({ jsonrpc: '2.0', id: null, error: { code: -32700, message: 'Parse error' } })}\n`);
  }
});
