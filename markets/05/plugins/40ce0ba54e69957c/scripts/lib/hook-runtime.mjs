import { parseHookInput, serializeHookResult } from "./hook-io.mjs";
import { requirePluginData } from "./plugin-data.mjs";

const maxFailureBytes = 480;

async function readStandardInput(stream) {
  stream.setEncoding("utf8");
  let text = "";
  for await (const chunk of stream) {
    text += chunk;
  }
  return text;
}

function boundedFailure(error) {
  const detail =
    error instanceof Error && error.message
      ? error.message.replaceAll(/\s+/g, " ").trim()
      : "unknown error";
  let message = `TokenX hook failed: ${detail}\n`;
  while (Buffer.byteLength(message, "utf8") > maxFailureBytes) {
    message = `${message.slice(0, -2)}\n`;
  }
  return message;
}

export async function runHook(expectedEvent, handler, runtime = {}) {
  const stdin = runtime.stdin ?? process.stdin;
  const stdout = runtime.stdout ?? process.stdout;
  const stderr = runtime.stderr ?? process.stderr;
  const env = runtime.env ?? process.env;

  if (env.TOKENX_SMART_CLASSIFIER_CHILD === "1") {
    return true;
  }

  try {
    const pluginData = requirePluginData(env);
    const input = parseHookInput(await readStandardInput(stdin));
    if (input.hook_event_name !== expectedEvent) {
      throw new RangeError(
        `expected ${expectedEvent}, received ${input.hook_event_name}`,
      );
    }
    const result = await handler({
      input,
      pluginData,
      env,
    });
    if (result !== null && result !== undefined) {
      stdout.write(serializeHookResult(result));
    }
    return true;
  } catch (error) {
    if (typeof runtime.onError === "function") {
      const result = runtime.onError(error);
      stdout.write(serializeHookResult(result));
      return false;
    }
    stderr.write(boundedFailure(error));
    process.exitCode = 1;
    return false;
  }
}
