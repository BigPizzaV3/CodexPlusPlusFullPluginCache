const pluginDataVariables = ["CLAUDE_PLUGIN_DATA", "PLUGIN_DATA"];

export function requirePluginData(env = process.env) {
  for (const name of pluginDataVariables) {
    const value = env[name];
    if (typeof value === "string" && value.length > 0) {
      return value;
    }
  }
  throw new TypeError("CLAUDE_PLUGIN_DATA or PLUGIN_DATA is required");
}
