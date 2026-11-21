---
title: "TypeScript SDK quickstart"
description: "Set up the Sovara TypeScript SDK and record an agent run."
---

<script src="/assets/sdk-nav.js"></script>

Sovara records supported LLM, MCP, and framework tool calls inside an SDK run.
Use `trace` for important custom operations that are not already captured.

## Install

Use Node.js 18+ (or the version your provider packages require) and
[install the CLI](/cli/install) for local recording. For remote setup, see the
[API reference](/sdks/typescript/api-reference).

Install the example's dependencies:

```bash
npm install @sovara/runner @openai/agents zod
npm install --save-dev tsx
```

Set `OPENAI_API_KEY` in the environment before running the example. The model
calls use your provider account and incur its normal API charges.

## A complete example

Two child agents compare sample temperatures. Sovara records their model and
tool calls; `trace` adds the comparison step. The weather values are demo data.

```ts
import { SovaraClient, trace } from "@sovara/runner"; // [!code ++]
import { Agent, run, tool } from "@openai/agents";
import { z } from "zod";

const sovara_client = new SovaraClient({ projectName: "weather-agent" }); // [!code ++]
const temperature = z.object({ celsius: z.number() });

const getZurichTemperature = tool({
  name: "get_zurich_temperature",
  description: "Return the demo temperature in Zurich in Celsius.",
  parameters: z.object({}),
  execute: async () => 22,
});

const getBostonTemperature = tool({
  name: "get_boston_temperature",
  description: "Return the demo temperature in Boston in Celsius.",
  parameters: z.object({}),
  execute: async () => 27,
});

const zurichAgent = new Agent({
  name: "Zurich weather agent",
  instructions: "Call the weather tool and return the temperature.",
  model: "gpt-5.4-mini",
  tools: [getZurichTemperature],
  outputType: temperature,
});

const bostonAgent = new Agent({
  name: "Boston weather agent",
  instructions: "Call the weather tool and return the temperature.",
  model: "gpt-5.4-mini",
  tools: [getBostonTemperature],
  outputType: temperature,
});

const chooseWarmerCity = trace( // [!code ++]
  async function chooseWarmerCity(zurich: number, boston: number): Promise<string> {
    if (zurich === boston) return `Boston and Zurich are equally warm at ${zurich} C.`;
    const city = zurich > boston ? "Zurich" : "Boston";
    return `${city} is warmer (${boston} C in Boston, ${zurich} C in Zurich).`;
  }, // [!code ++]
  { name: "choose warmer city" }, // [!code ++]
); // [!code ++]

async function main(): Promise<void> {
  const question = "Which city is warmer, Boston or Zurich?";
  await sovara_client.run("compare city weather", async () => { // [!code ++]
    // Attach the user-visible request to the top-level run. // [!code ++]
    await sovara_client.logInput(question); // [!code ++]

    // Each subrun groups one delegated agent's work into an expandable child run. // [!code ++]
    const zurich = await sovara_client.subrun("Zurich weather agent", async () => { // [!code ++]
      const result = await run(zurichAgent, question);
      return result.finalOutput!.celsius;
    }); // [!code ++]

    const boston = await sovara_client.subrun("Boston weather agent", async () => { // [!code ++]
      const result = await run(bostonAgent, question);
      return result.finalOutput!.celsius;
    }); // [!code ++]

    const answer = await chooseWarmerCity(zurich, boston);
    // Attach the final user-visible result to the top-level run. // [!code ++]
    await sovara_client.logOutput(answer); // [!code ++]
    console.log(answer);
  }); // [!code ++]
}

void main();
```

<Note>
Use `trace` for custom operations; supported framework tools and MCP calls are
recorded automatically. Use optional subruns to group child agents.
</Note>

## Verify one run

Save the example as `weather_agent.ts`, then run it normally:

```bash
npx tsx weather_agent.ts
```

Open the `weather-agent` project and select
<strong><Icon icon="play" size={14} /> Runs</strong> to inspect the recording.
Open the run to see both subruns, their model and tool calls, and the comparison
step. Logged input and output also appear in the Runs table.

## Next steps

- [Use the SDK](/sdks/typescript/use-the-sdk) for subruns, durable runs and run IDs, lessons, and metadata.
- [API reference](/sdks/typescript/api-reference) for the exact public surface.
- [Troubleshooting](/sdks/typescript/troubleshooting) for missing runs or steps.
