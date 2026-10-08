import type { paths as AardvarkPaths } from "@oai/aardvark-client/paths";
import type {
  AardvarkScanConfigurationSaved,
  CodexSecurityFindingCopied,
  CodexSecurityFindingShared,
  CodexSecurityPatchViewed,
} from "@oai/analytics/gen/client-events/protobuf_analytics_events/v1/aardvark";
import type { paths as CodexPaths } from "@oai/codex-backend-client";

export type DefenseFactoryBootstrap = {
  access: "denied" | "allowed";
  accountId: string;
  locale: string;
  initialPath: string;
  hostAppUrl?: string;
  webOrigin: string;
  /** Null means setup could not be checked; the receiving APIs still authorize reads. */
  githubConnected?: boolean | null;
  identity?: {
    accountId: string;
    workspaceId: string | null;
    userId: string;
    isAdmin: boolean;
    workflowsEnabled: boolean;
  };
  isEligibleWorkspace?: boolean;
  requiresCodexCloud?: boolean;
  overviewEnabled?: boolean;
  scanLimits?: {
    count: number;
    lookbackDays: number;
  };
  notifications?: {
    maxRules: number;
    maxDestinations: number;
    canConfigure: boolean;
  };
  github?: {
    status: "loading" | "error" | "connected" | "connect" | "disabled";
    connectorId: string;
    reconnect: boolean;
  };
  githubConnections?: Array<DefenseFactoryGithubConnection>;
};

export type DefenseFactoryGithubConnection = NonNullable<
  DefenseFactoryBootstrap["github"]
> & {
  label: string;
  isPublic: boolean;
};

/** Sheep owns access and domain configuration; the host supplies setup presentation. */
export type DefenseFactoryBackendBootstrap = Omit<
  DefenseFactoryBootstrap,
  "locale" | "initialPath" | "hostAppUrl" | "github" | "githubConnections"
>;

/** Choosers need repository membership, not environment settings or secrets. */
type CloudEnvironmentSummary = Pick<
  JsonResponse<CodexPaths["/api/codex/environments"]["get"]>[number],
  "id" | "label" | "repos" | "github_connector_id"
> & {
  repo_map?: Record<string, null> | null;
};

type WithJsonResponse<Operation, Data> = Omit<Operation, "responses"> & {
  responses: { 200: { content: { "application/json": Data } } };
};

/** Existing CSC measurements; no caller-selected schema or user context. */
export type DefenseFactoryProductEvent =
  | {
      name: "AardvarkScanConfigurationSaved";
      data: AardvarkScanConfigurationSaved;
    }
  | { name: "CodexSecurityFindingCopied"; data: CodexSecurityFindingCopied }
  | { name: "CodexSecurityFindingShared"; data: CodexSecurityFindingShared }
  | { name: "CodexSecurityPatchViewed"; data: CodexSecurityPatchViewed };

/** Operations exposed only to the first-party Codex Security Cloud plugin resource. */
export type DefenseFactoryApi = {
  findings_list: AardvarkPaths["/api/aardvark/findings"]["get"];
  findings_get: AardvarkPaths["/api/aardvark/findings/{finding_id}"]["get"];
  findings_export: AardvarkPaths["/api/aardvark/findings/export"]["get"];
  findings_update: AardvarkPaths["/api/aardvark/scan-findings/{id}"]["patch"];
  findings_create_pr: AardvarkPaths["/api/aardvark/scan-findings/{id}/pr"]["post"];
  findings_feedback: AardvarkPaths["/api/aardvark/scan-findings/{id}/feedback"]["post"];
  /** Coordinate the existing finding, Cloud task, and follow-up link APIs. */
  findings_chat: {
    parameters: AardvarkPaths["/api/aardvark/scan-findings/{id}"]["get"]["parameters"];
    requestBody: {
      content: {
        "application/json": { text: string; createdTaskId?: string };
      };
    };
    responses: {
      200: {
        content: {
          "application/json": {
            taskId: string;
            linked: boolean;
            finding: AardvarkPaths["/api/aardvark/scan-findings/{id}"]["get"]["responses"][200]["content"]["application/json"];
          };
        };
      };
    };
  };
  workflow_definition: AardvarkPaths["/api/aardvark/workflow/definitions/{workflow_id}"]["get"];
  workflow_list: AardvarkPaths["/api/aardvark/workflow/runs"]["get"];
  workflow_repositories: AardvarkPaths["/api/aardvark/workflow/runs/repositories"]["get"];
  workflow_get: AardvarkPaths["/api/aardvark/workflow/runs/{run_id}"]["get"];
  workflow_launch: AardvarkPaths["/api/aardvark/workflow/runs"]["post"];
  workflow_cancel: AardvarkPaths["/api/aardvark/workflow/runs/{run_id}/cancel"]["post"];
  workflow_output: AardvarkPaths["/api/aardvark/workflow/runs/{run_id}/outputs/{output_id}"]["get"];
  workflow_artifact: AardvarkPaths["/api/aardvark/workflow/runs/{run_id}/outputs/{output_id}/artifacts/{artifact_id}"]["get"];
  monitoring_list: AardvarkPaths["/api/aardvark/scan_configurations"]["get"];
  monitoring_metadata: AardvarkPaths["/api/aardvark/scan_configurations/metadata"]["get"];
  monitoring_get: AardvarkPaths["/api/aardvark/scan_configurations/{id}"]["get"];
  monitoring_create: AardvarkPaths["/api/aardvark/scan_configurations"]["post"];
  monitoring_update: AardvarkPaths["/api/aardvark/scan_configurations/{id}"]["patch"];
  monitoring_delete: AardvarkPaths["/api/aardvark/scan_configurations/{id}"]["delete"];
  monitoring_recover: AardvarkPaths["/api/aardvark/scan_configurations/{id}/recover"]["post"];
  monitoring_scans: AardvarkPaths["/api/aardvark/scan_configurations/{id}/scans"]["get"];
  monitoring_scan_get: AardvarkPaths["/api/aardvark/scan_configurations/{id}/scans/{scan_id}"]["get"];
  dashboard_repositories: AardvarkPaths["/api/aardvark/dashboard/repositories"]["get"];
  dashboard_findings: AardvarkPaths["/api/aardvark/dashboard/findings"]["get"];
  dashboard_activity: AardvarkPaths["/api/aardvark/dashboard/activity"]["get"];
  dashboard_scans: AardvarkPaths["/api/aardvark/dashboard/scans"]["get"];
  notifications_validate: AardvarkPaths["/api/aardvark/connectors/slack/workspaces/{slack_team_id}/validate-channel"]["post"];
  notifications_test: AardvarkPaths["/api/aardvark/connectors/slack/workspaces/{slack_team_id}/send-test-notification"]["post"];
  /** Only Codex Slack connections needed to configure a notification destination. */
  notifications_connections: {
    responses: {
      200: {
        content: {
          "application/json": {
            disabled: boolean;
            settingsUrl: string;
            workspaces: Array<{ id: string; name: string; reconnect: boolean }>;
          };
        };
      };
    };
  };
  github_repositories: CodexPaths["/api/codex/github/list-repositories"]["get"];
  github_search: CodexPaths["/api/codex/github/repositories/search/all-installations"]["get"];
  github_get: CodexPaths["/api/codex/github/repositories/{repo_id}"]["get"];
  environments_list: WithJsonResponse<
    CodexPaths["/api/codex/environments"]["get"],
    Array<CloudEnvironmentSummary>
  >;
  environments_search: WithJsonResponse<
    CodexPaths["/api/codex/environments/search"]["get"],
    { items: Array<CloudEnvironmentSummary>; cursor?: string | null }
  >;
  /** CSC's existing default environment setup, with the body chosen by the server. */
  environments_create_default: {
    parameters: CodexPaths["/api/codex/github/repositories/{repo_id}"]["get"]["parameters"];
    responses: { 200: { content: { "application/json": { id: string } } } };
  };
};

export type DefenseFactoryOperation = keyof DefenseFactoryApi;

type OperationParameters<T> = T extends { parameters: infer P }
  ? Record<never, never> extends P
    ? { parameters?: P }
    : { parameters: P }
  : { parameters?: never };

type OperationBody<T> = T extends {
  requestBody: { content: { "application/json": infer Body } };
}
  ? { requestBody: Body }
  : T extends {
        requestBody?: { content: { "application/json": infer Body } };
      }
    ? { requestBody?: Body }
    : { requestBody?: never };

export type DefenseFactoryRequest<
  Operation extends DefenseFactoryOperation = DefenseFactoryOperation,
> = {
  [Key in Operation]: { operation: Key } & OperationParameters<
    DefenseFactoryApi[Key]
  > &
    OperationBody<DefenseFactoryApi[Key]> &
    (Key extends "workflow_artifact"
      ? { filename?: string }
      : Record<never, never>);
}[Operation];

type JsonResponse<T> = T extends { responses: infer Responses }
  ? {
      [Status in keyof Responses]: Status extends 200 | 201 | 202
        ? Responses[Status] extends {
            content: { "application/json": infer Body };
          }
          ? Body
          : undefined
        : never;
    }[keyof Responses]
  : never;

/** Small previews are inline; full downloads use a short-lived file grant. */
export type DefenseFactoryFile = {
  contentType: string;
  fileName: string | null;
} & ({ base64: string } | { downloadUrl: string });

export type DefenseFactoryResponse<Operation extends DefenseFactoryOperation> =
  Operation extends "workflow_artifact" | "findings_export"
    ? DefenseFactoryFile
    : JsonResponse<DefenseFactoryApi[Operation]>;

export type DefenseFactoryClient = {
  request<Operation extends DefenseFactoryOperation>(
    request: DefenseFactoryRequest<Operation>,
  ): Promise<DefenseFactoryResponse<Operation>>;
};
