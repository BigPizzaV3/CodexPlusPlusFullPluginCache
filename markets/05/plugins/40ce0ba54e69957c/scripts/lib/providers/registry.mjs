import { codexProvider } from "./codex.mjs";

const providers = new Map([["codex", codexProvider]]);

export function getProvider(id) {
  const provider = providers.get(id);
  if (!provider) {
    throw new RangeError(`unsupported provider: ${String(id)}`);
  }
  return provider;
}

export function listProviders() {
  return [...providers.keys()];
}
