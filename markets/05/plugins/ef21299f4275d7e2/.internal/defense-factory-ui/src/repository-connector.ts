import type {
  DefenseFactoryBootstrap,
  DefenseFactoryClient,
  DefenseFactoryResponse,
} from "./contract";

// Matches Codex's NEW_GITHUB_CONNECTOR_ID default in GithubConnectorPluginService.
const PUBLIC_GITHUB_CONNECTOR_ID = "connector_76869538009648d5b282a4bb21c3d157";

/** Qualified Cloud repository IDs carry their GitHub Enterprise connector. */
export function getGithubConnectorIdFromRepositoryId(
  repositoryId: string,
): string | null {
  const separator = repositoryId.indexOf(":");
  return repositoryId.startsWith("github-") && separator > "github-".length
    ? repositoryId.slice("github-".length, separator)
    : null;
}

/** Never silently route a qualified Enterprise repository through another connection. */
export function getRepositoryConnection(
  cloud: DefenseFactoryBootstrap,
  repositoryId?: string | null,
): DefenseFactoryBootstrap["github"] {
  if (!repositoryId) return cloud.github;
  const connectorId = getGithubConnectorIdFromRepositoryId(repositoryId);
  if (connectorId)
    return cloud.githubConnections?.find(
      (connection) => connection.connectorId === connectorId,
    );
  return cloud.githubConnections == null
    ? cloud.github
    : cloud.githubConnections.find((connection) => connection.isPublic);
}

/** Connection summaries are advisory; Codex authorizes each repository request. */
export function getRepositoryConnectionState(
  cloud: DefenseFactoryBootstrap,
  repositoryId?: string | null,
  selectedConnectorId?: string | null,
) {
  const requestedConnectorId =
    getGithubConnectorIdFromRepositoryId(repositoryId ?? "") ??
    selectedConnectorId;
  const connection = requestedConnectorId
    ? cloud.githubConnections?.find(
        (item) => item.connectorId === requestedConnectorId,
      ) ??
      (cloud.github?.connectorId === requestedConnectorId
        ? cloud.github
        : undefined)
    : getRepositoryConnection(cloud, repositoryId);
  const status = connection?.status ?? "error";
  const metadataUnavailable =
    cloud.githubConnections == null &&
    (!cloud.github || cloud.github.status === "error");

  return {
    connection,
    // An omitted connector uses Codex's public GitHub default. Keep an explicit
    // or repository-qualified Enterprise connector even when its summary fails.
    connectorId: requestedConnectorId ?? connection?.connectorId,
    status,
    canQuery:
      status === "connected" ||
      connection?.status === "error" ||
      metadataUnavailable,
  };
}

export function matchesRepositoryEnvironment(
  environment: {
    repos: string[];
    github_connector_id?: string | null;
  },
  repositoryId: string,
  connectorId: string | undefined,
): boolean {
  const expectedConnector = connectorId || PUBLIC_GITHUB_CONNECTOR_ID;
  return (
    environment.repos.includes(repositoryId) &&
    // Only public GitHub environments may omit their connector.
    (environment.github_connector_id || PUBLIC_GITHUB_CONNECTOR_ID) ===
      expectedConnector
  );
}

export async function loadRepositoryEnvironments(
  client: DefenseFactoryClient,
  repositoryId: string,
  connectorId: string | undefined,
): Promise<DefenseFactoryResponse<"environments_list">> {
  const matching: DefenseFactoryResponse<"environments_list"> = [];
  let cursor: string | undefined;
  do {
    const page = await client.request({
      operation: "environments_search",
      parameters: { query: { cursor, limit: 100 } },
    });
    matching.push(
      ...page.items.filter((environment) =>
        matchesRepositoryEnvironment(environment, repositoryId, connectorId),
      ),
    );
    cursor = page.cursor ?? undefined;
  } while (cursor);
  return matching;
}

export function selectedRepositoryEnvironmentId(
  environments: ReadonlyArray<{ id: string }> | undefined,
  ...preferredIds: Array<string | null | undefined>
): string | undefined {
  for (const id of preferredIds) {
    if (id && environments?.some((environment) => environment.id === id))
      return id;
  }
  // Summaries omit configuration details, so multiple choices need a selection.
  return environments?.length === 1 ? environments[0]?.id : undefined;
}

export function canSaveRepositoryEnvironment({
  environments,
  discoveryReady,
  selectedId,
  configuredId,
  canCreate,
}: {
  environments: ReadonlyArray<{ id: string }> | undefined;
  discoveryReady: boolean;
  selectedId: string | undefined;
  configuredId: string | null | undefined;
  canCreate: boolean;
}): boolean {
  // Pausing or editing monitoring must remain possible if its saved environment
  // is no longer visible. The server revalidates environment changes separately.
  if (configuredId && selectedId === configuredId) return true;
  if (!discoveryReady) return false;
  return selectedId
    ? environments?.some((environment) => environment.id === selectedId) ===
        true
    : canCreate && environments?.length === 0;
}
