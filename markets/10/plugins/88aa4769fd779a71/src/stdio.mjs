import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { createCalculatorServer } from './mcp-server.mjs';
await createCalculatorServer().connect(new StdioServerTransport());
