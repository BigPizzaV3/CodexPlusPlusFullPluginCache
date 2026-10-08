import {
  App,
  applyDocumentTheme,
  applyHostFonts,
  applyHostStyleVariables,
} from "@modelcontextprotocol/ext-apps";
import type { DefenseFactoryBridge } from "@oai/first-party-plugin-bridge/defense-factory";
import { createFirstPartyPluginBridge } from "@oai/first-party-plugin-bridge/plugin";
import { z } from "zod";

import type {
  DefenseFactoryBackendBootstrap,
  DefenseFactoryBootstrap,
  DefenseFactoryClient,
  DefenseFactoryFile,
  DefenseFactoryOperation,
  DefenseFactoryProductEvent,
  DefenseFactoryRequest,
  DefenseFactoryResponse,
} from "./contract";

declare const DEFENSE_FACTORY_VERSION: string;
const app = new App(
  { name: "Codex Security Cloud", version: DEFENSE_FACTORY_VERSION },
  { availableDisplayModes: ["inline", "fullscreen"] },
  { autoResize: false, strict: true },
);
type HostContext = ReturnType<App["getHostContext"]>;
const contextListeners = new Set<(context: HostContext) => void>();
let connection: Promise<void> | undefined;
let defenseFactoryBridge: ReturnType<
  typeof createFirstPartyPluginBridge<DefenseFactoryBridge>
>;

function applyContext(context: HostContext): void {
  if (context?.theme != null) applyDocumentTheme(context.theme);
  if (context?.styles?.variables != null) {
    applyHostStyleVariables(context.styles.variables);
  }
  if (context?.styles?.css?.fonts != null) {
    applyHostFonts(context.styles.css.fonts);
  }
  contextListeners.forEach((listener) => listener(context));
}

app.onhostcontextchanged = () => applyContext(app.getHostContext());

function connect(): Promise<void> {
  connection ??= app
    .connect()
    .then(() => {
      defenseFactoryBridge =
        createFirstPartyPluginBridge<DefenseFactoryBridge>(app);
      const context = app.getHostContext();
      applyContext(context);
      if (
        context?.displayMode !== "fullscreen" &&
        context?.availableDisplayModes?.includes("fullscreen")
      ) {
        // Request once so closing fullscreen does not immediately reopen it.
        // A declined display request must not interrupt the app connection.
        void app
          .requestDisplayMode({ mode: "fullscreen" })
          .catch((error: unknown) => {
            console.warn(
              "Codex Security Cloud could not open fullscreen.",
              error,
            );
          });
      }
    })
    .catch(async (error: unknown) => {
      // App.connect starts closing a failed handshake. Wait for transport
      // cleanup before allowing the UI's explicit Try again action to reconnect.
      try {
        await app.close();
      } finally {
        connection = undefined;
        defenseFactoryBridge = undefined;
      }
      throw error;
    });
  return connection;
}

async function callTool<Data>(
  name: string,
  args: Record<string, unknown>,
): Promise<Data> {
  await connect();
  // postMessage preserves nested undefined fields, but MCP arguments must be
  // JSON. Match HTTP serialization so optional query parameters are omitted.
  const jsonArgs: Record<string, unknown> = JSON.parse(JSON.stringify(args));
  const result = await app.callServerTool({ name, arguments: jsonArgs });
  if (result.isError) {
    const detail = result.content
      .filter((item) => item.type === "text")
      .map((item) => item.text)
      .join("\n");
    throw new Error(detail || "The Codex Security Cloud request failed.");
  }
  if (
    result.structuredContent == null ||
    !("data" in result.structuredContent)
  ) {
    throw new Error(
      "The Codex Security Cloud host returned an incomplete response.",
    );
  }
  return result.structuredContent.data as Data;
}

export const securityClient: DefenseFactoryClient = {
  request<Operation extends DefenseFactoryOperation>(
    request: DefenseFactoryRequest<Operation>,
  ): Promise<DefenseFactoryResponse<Operation>> {
    const { operation, ...args } = request;
    return callTool(`defense_factory_${operation}`, args);
  },
};

export async function connectClient(): Promise<DefenseFactoryBootstrap> {
  const access = await callTool<DefenseFactoryBackendBootstrap>(
    "defense_factory_bootstrap",
    {},
  );
  const deepLink = z
    .object({ url: z.string() })
    .safeParse(app.getHostContext()?.["openai/deepLink"]);
  const bootstrap: DefenseFactoryBootstrap = {
    ...access,
    locale: app.getHostContext()?.locale ?? "en",
    initialPath:
      deepLink.success && deepLink.data.url !== "/"
        ? deepLink.data.url
        : "/overview",
  };
  if (access.access !== "allowed" || !access.identity?.workflowsEnabled)
    return bootstrap;

  // Host capabilities are optional; native hosts and previews may omit the bridge.
  const [connections, hostAppUrl] = await Promise.all([
    readGithubConnections().catch(() => ({})),
    getShareUrl("/").catch(() => undefined),
  ]);
  return { ...bootstrap, ...connections, hostAppUrl };
}

async function readGithubConnections() {
  const bridge = await getDefenseFactoryBridge();
  using result = await bridge.getGithubConnections();
  return {
    // Only copy connection fields so host metadata cannot replace backend access.
    github: result.github && {
      status: result.github.status,
      connectorId: result.github.connectorId,
      reconnect: result.github.reconnect,
    },
    githubConnections: result.githubConnections?.map((connection) => ({
      status: connection.status,
      connectorId: connection.connectorId,
      reconnect: connection.reconnect,
      label: connection.label,
      isPublic: connection.isPublic,
    })),
  };
}

export function subscribeToHostContext(
  listener: (context: HostContext) => void,
): () => void {
  contextListeners.add(listener);
  return () => {
    contextListeners.delete(listener);
  };
}

// These operations are explicit host setup and platform capabilities; the iframe never gets
// an arbitrary authenticated URL fetch or account-credential API.
async function getDefenseFactoryBridge() {
  await connect();
  if (defenseFactoryBridge == null)
    throw new Error("Codex Security Cloud is unavailable in this host");
  return defenseFactoryBridge;
}

export async function navigate(path: string): Promise<void> {
  await connect();
  // ChatGPT handles section changes inside the iframe; Codex can also sync its URL.
  if (!app.getHostCapabilities()?.experimental?.["openai/selfDeepLinks"])
    return;
  return openLink(`codex://mcp-app/self/open_defense_factory${path}`);
}

export function openTask(taskId: string, webOrigin: string): Promise<void> {
  return openLink(
    new URL(`/remote/${encodeURIComponent(taskId)}`, webOrigin).href,
  );
}

export async function openEnvironment(
  environmentId?: string,
): Promise<{ environmentId: string | null }> {
  const bridge = await getDefenseFactoryBridge();
  using result = await bridge.openEnvironment({ environmentId });
  return { environmentId: result.environmentId };
}

export async function connectGithub(
  connectorId: string,
): Promise<{ didConnect: boolean }> {
  const bridge = await getDefenseFactoryBridge();
  using result = await bridge.connectGithub({ connectorId });
  return { didConnect: result.didConnect };
}

export async function openLink(url: string): Promise<void> {
  await connect();
  const result = await app.openLink({ url });
  if (result.isError) throw new Error("The link could not be opened.");
}

export async function downloadFile(file: DefenseFactoryFile): Promise<void> {
  if ("downloadUrl" in file) {
    await openLink(file.downloadUrl);
    return;
  }
  const bridge = await getDefenseFactoryBridge();
  await bridge.downloadFile(file);
}

export async function copyText(text: string): Promise<void> {
  const bridge = await getDefenseFactoryBridge();
  await bridge.copyText({ text });
}

export async function getShareUrl(path: string): Promise<string> {
  const bridge = await getDefenseFactoryBridge();
  using result = await bridge.getShareUrl({ path });
  return result.url;
}

/** Product logging must never fail the user's completed action. */
export function logSecurityEvent(event: DefenseFactoryProductEvent): void {
  void getDefenseFactoryBridge()
    .then((bridge) => bridge.logSecurityEvent(event))
    .catch(() => {
      // The host can disappear when an action navigates out of the plugin.
    });
}
