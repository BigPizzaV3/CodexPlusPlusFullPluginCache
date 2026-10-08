import type { components } from "@oai/aardvark-client/components";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useState, type ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation, useParams, useSearchParams } from "react-router";

import { useCloud } from "./app-context";
import { securityClient } from "./client";
import { ContinuousScanDetail } from "./continuous-scans";
import { ScanLaunch } from "./scan-launch";
import { repositoryLabel } from "./ui";
import {
  WorkbenchButton as Button,
  WorkbenchSearchInput,
} from "./workbench/controls";
import {
  ScanCancelConfirmation,
  ScanDetailPresentation,
  ScanFindingsUnavailable,
} from "./workbench/scan-detail-presentation";
import { ScanFindings } from "./workbench/scan-findings";
import { ScanWorkflowOutput } from "./workbench/scan-workflow-output";
import { ScansFilterMenu } from "./workbench/scans-filters";
import { scanMessages } from "./workbench/scans-messages";
import {
  filterAndSortWorkbenchScans,
  type ScanSortField,
  type ScanStatusFilter,
  type ScanTypeFilter,
  type WorkbenchScan,
} from "./workbench/scans-model";
import { WorkbenchScansTable } from "./workbench/scans-table";
import { WorkbenchState, WorkbenchToolbar } from "./workbench/layout";
import { workbenchStyles } from "./workbench/styles";

const running = new Set([
  "queued",
  "preparing",
  "running",
  "validating_output",
  "cancel_requested",
]);

type ScanConfiguration =
  components["schemas"]["AardvarkScanConfigurationListItem"];
type WorkflowRepository =
  components["schemas"]["WorkflowRunRepositoryMetadataItem"];

type RepositoryScope = {
  configuration?: ScanConfiguration;
  repoConnectorId: string | null;
  repoId: string;
  repoUrl?: string;
};

const PAGINATION_PARAMETERS = [
  "cursor",
  "commit_cursor",
  "workflow_exhausted",
  "commit_exhausted",
] as const;

function clearPagination(parameters: URLSearchParams) {
  for (const parameter of PAGINATION_PARAMETERS) parameters.delete(parameter);
}

function paginationKey(parameters: URLSearchParams) {
  return PAGINATION_PARAMETERS.map(
    (parameter) => `${parameter}:${parameters.get(parameter) ?? ""}`,
  ).join("|");
}

function isContinuousConfiguration(configuration: ScanConfiguration) {
  return (
    configuration.scan_type === "continuous_scan" &&
    !configuration.soft_deleted_at
  );
}

function normalizedRepositoryUrl(repositoryUrl?: string | null) {
  return repositoryUrl?.replace(/\.git$/, "");
}

function configurationMatchesScope(
  configuration: ScanConfiguration,
  repoId?: string,
  repoUrl?: string,
) {
  return (
    isContinuousConfiguration(configuration) &&
    (!repoId || configuration.scan_input.repo_id === repoId) &&
    (!repoUrl ||
      normalizedRepositoryUrl(configuration.scan_input.repo_url) ===
        normalizedRepositoryUrl(repoUrl))
  );
}

function publicRepositoryUrl(repository: WorkflowRepository) {
  return repository.repo_connector_id == null
    ? `https://github.com/${repository.repository_full_name}`
    : undefined;
}

function repositoryIdentityKey(repository: {
  repo_id: string;
  repo_connector_id?: string | null;
}) {
  return `${repository.repo_id}:${repository.repo_connector_id ?? "public"}`;
}

export function Scans() {
  const { id, repositoryId } = useParams();
  const location = useLocation();
  const [search] = useSearchParams();
  const configurationId = search.get("scan_configuration_id");
  const isWorkflowRunId = Boolean(id && /^wfr_[0-9a-f]{64}$/.test(id));
  if (id && !isWorkflowRunId) {
    return (
      <ContinuousScanDetail
        key={id}
        configurationId={configurationId}
        repositoryId={repositoryId}
        scanId={id}
      />
    );
  }
  return location.pathname === "/scans/new" ? (
    <ScanLaunch key={search.get("repo_id") ?? ""} />
  ) : id ? (
    <ScanDetail key={id} id={id} />
  ) : (
    <ScanList />
  );
}

function ScanList() {
  const intl = useIntl();
  const { repositoryId: routeRepositoryId } = useParams();
  const { accountId, identity } = useCloud();
  const [search, setSearch] = useSearchParams();
  const [previousPages, setPreviousPages] = useState<Record<string, string>>(
    {},
  );
  const [text, setText] = useState("");
  const [status, setStatus] = useState<ScanStatusFilter>("all");
  const [scanType, setScanType] = useState<ScanTypeFilter>("all");
  const [sortField, setSortField] = useState<ScanSortField>("started");
  const [sortDescending, setSortDescending] = useState(true);
  const configurationId = search.get("scan_configuration_id");
  const hasRepoIdParameter = search.has("repo_id");
  const hasRepoUrlParameter = search.has("repo");
  const repoIdParameter = search.get("repo_id") ?? undefined;
  const repoUrlParameter = search.get("repo") ?? undefined;
  const requestedRepoId = routeRepositoryId ?? repoIdParameter;
  const requestedRepoUrl = repoUrlParameter;
  const hintsConflict = Boolean(
    (routeRepositoryId &&
      repoIdParameter &&
      routeRepositoryId !== repoIdParameter) ||
      (hasRepoIdParameter && !repoIdParameter?.trim()) ||
      (hasRepoUrlParameter && !repoUrlParameter?.trim()),
  );
  const hasExplicitRepositoryScope = Boolean(
    routeRepositoryId ||
      hasRepoIdParameter ||
      hasRepoUrlParameter ||
      configurationId,
  );
  const selectedScanType =
    !hasExplicitRepositoryScope && scanType === "commit_scan"
      ? "all"
      : scanType;

  const repositories = useQuery({
    queryKey: [
      "scan-filter-repositories",
      accountId,
      identity?.userId ?? "none",
    ],
    queryFn: () =>
      securityClient.request({ operation: "workflow_repositories" }),
    refetchOnMount: "always",
    staleTime: 60_000,
  });
  const configurationById = useQuery({
    queryKey: [
      "scan-configuration-scope",
      accountId,
      identity?.userId ?? "none",
      configurationId,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_get",
        parameters: { path: { id: configurationId ?? "" } },
      }),
    enabled: Boolean(configurationId && !hintsConflict),
    refetchOnMount: "always",
    staleTime: 15_000,
  });
  const configurationsForScope = useQuery({
    queryKey: [
      "scan-configurations-for-scope",
      accountId,
      identity?.userId ?? "none",
      requestedRepoId,
      requestedRepoUrl,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: {
            repo_id: requestedRepoId,
            repo_url: requestedRepoId ? undefined : requestedRepoUrl,
            scan_type: "continuous_scan",
            limit: 2,
          },
        },
      }),
    enabled: Boolean(
      !configurationId &&
        !hintsConflict &&
        (requestedRepoId || requestedRepoUrl),
    ),
    refetchOnMount: "always",
    staleTime: 15_000,
  });

  const authorizedRepositories =
    repositories.isFetchedAfterMount && !repositories.error
      ? repositories.data
      : undefined;
  const authorizedConfigurationById =
    configurationById.isFetchedAfterMount && !configurationById.error
      ? configurationById.data
      : undefined;
  const authorizedConfigurationsForScope =
    configurationsForScope.isFetchedAfterMount && !configurationsForScope.error
      ? configurationsForScope.data
      : undefined;
  const matchingConfigurations = (
    authorizedConfigurationsForScope?.items ?? []
  ).filter((configuration) =>
    configurationMatchesScope(configuration, requestedRepoId, requestedRepoUrl),
  );
  const configurationScopeConflicts = Boolean(
    requestedRepoId &&
      requestedRepoUrl &&
      authorizedConfigurationsForScope?.items.some(isContinuousConfiguration) &&
      matchingConfigurations.length === 0,
  );
  const matchingWorkflowRepositories = Array.from(
    new Map(
      (authorizedRepositories?.items ?? [])
        .filter(
          (repository) =>
            (!requestedRepoId || repository.repo_id === requestedRepoId) &&
            (!requestedRepoUrl ||
              normalizedRepositoryUrl(publicRepositoryUrl(repository)) ===
                normalizedRepositoryUrl(requestedRepoUrl) ||
              // Nested repository pages render this child only after their
              // wrapper resolves and normalizes the requested repository URL.
              // That lets connector-scoped repositories use the matching
              // authorized repository identity without inventing a public URL.
              Boolean(routeRepositoryId && repository.repo_connector_id)),
        )
        .map((repository) => [repositoryIdentityKey(repository), repository]),
    ).values(),
  );

  let resolvedScope: RepositoryScope | null = null;
  let scopeIsPending = false;
  let scopeIsUnavailable = hintsConflict;
  if (!scopeIsUnavailable && configurationId) {
    if (configurationById.isPending || !configurationById.isFetchedAfterMount) {
      scopeIsPending = true;
    } else if (
      configurationById.error ||
      !authorizedConfigurationById ||
      (authorizedConfigurationById.id !== configurationId &&
        authorizedConfigurationById.hid !== configurationId) ||
      !configurationMatchesScope(
        authorizedConfigurationById,
        requestedRepoId,
        requestedRepoUrl,
      )
    ) {
      scopeIsUnavailable = true;
    } else {
      resolvedScope = {
        configuration: authorizedConfigurationById,
        repoConnectorId:
          authorizedConfigurationById.scan_input.repo_connector_id ?? null,
        repoId: authorizedConfigurationById.scan_input.repo_id,
        repoUrl: authorizedConfigurationById.scan_input.repo_url,
      };
    }
  } else if (!scopeIsUnavailable && hasExplicitRepositoryScope) {
    if (
      configurationsForScope.isPending ||
      !configurationsForScope.isFetchedAfterMount ||
      repositories.isPending ||
      !repositories.isFetchedAfterMount
    ) {
      scopeIsPending = true;
    } else if (configurationScopeConflicts) {
      // A repository ID with an active configuration for another URL is an
      // explicit identity conflict. Do not fall back to workflow history.
      scopeIsUnavailable = true;
    } else if (
      matchingConfigurations.length > 1 ||
      authorizedConfigurationsForScope?.next_cursor
    ) {
      scopeIsUnavailable = true;
    } else if (matchingConfigurations.length === 1) {
      const configuration = matchingConfigurations[0];
      resolvedScope = {
        configuration,
        repoConnectorId: configuration.scan_input.repo_connector_id ?? null,
        repoId: configuration.scan_input.repo_id,
        repoUrl: configuration.scan_input.repo_url,
      };
    } else if (matchingWorkflowRepositories.length === 1) {
      const repository = matchingWorkflowRepositories[0];
      resolvedScope = {
        repoConnectorId: repository.repo_connector_id ?? null,
        repoId: repository.repo_id,
        repoUrl: publicRepositoryUrl(repository),
      };
    } else {
      scopeIsUnavailable = true;
    }
  }

  const workflowCursor = search.get("cursor") || undefined;
  const commitCursor = search.get("commit_cursor") || undefined;
  const workflowPageIsExhausted = search.get("workflow_exhausted") === "true";
  // Old workflow-only deep links do not have a paired commit cursor. Do not
  // repeat the first commit page alongside a later workflow page.
  const commitPageIsExhausted =
    search.get("commit_exhausted") === "true" ||
    Boolean(
      workflowCursor &&
        !search.has("commit_cursor") &&
        !search.has("commit_exhausted"),
    );
  const canQueryHistory = !hasExplicitRepositoryScope || Boolean(resolvedScope);
  const workflowQuery = useQuery({
    queryKey: [
      "scans",
      accountId,
      identity?.userId ?? "none",
      resolvedScope?.repoId,
      workflowCursor,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_list",
        parameters: {
          query: {
            repo_id: resolvedScope?.repoId,
            cursor: workflowCursor,
            limit: 50,
            include_ownership: true,
          },
        },
      }),
    enabled: canQueryHistory && !scopeIsPending && !workflowPageIsExhausted,
    refetchOnMount: "always",
    staleTime: 4_000,
    refetchInterval: (query) =>
      query.state.data?.items.some((run) => running.has(run.status))
        ? 4_000
        : false,
  });
  const configuration = resolvedScope?.configuration;
  const configurationRequestId = configuration
    ? configuration.hid || configuration.id
    : undefined;
  const commitQuery = useQuery({
    queryKey: [
      "continuous-scans",
      accountId,
      identity?.userId ?? "none",
      configurationRequestId,
      commitCursor,
      search.get("include_deleted") === "true",
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_scans",
        parameters: {
          path: { id: configurationRequestId ?? "" },
          query: {
            limit: 25,
            cursor: commitCursor,
            include_deleted: search.get("include_deleted") === "true",
          },
        },
      }),
    enabled: Boolean(
      canQueryHistory &&
        !scopeIsPending &&
        configurationRequestId &&
        !commitPageIsExhausted,
    ),
    refetchOnMount: "always",
    staleTime: 4_000,
    refetchInterval: (query) =>
      query.state.data?.items.some(
        (scan) => scan.status === "created" || scan.status === "in_progress",
      )
        ? 4_000
        : false,
  });
  const environments = useQuery({
    queryKey: ["scan-environments", accountId, identity?.userId ?? "none"],
    queryFn: () => securityClient.request({ operation: "environments_list" }),
    refetchOnMount: "always",
    staleTime: 60_000,
  });
  const environmentLabels = new Map(
    (environments.isFetchedAfterMount && !environments.error
      ? environments.data ?? []
      : []
    ).map((environment) => [environment.id, environment.label]),
  );
  const environmentsAreLoading =
    environments.isPending || !environments.isFetchedAfterMount;
  const workflowPage =
    canQueryHistory &&
    !scopeIsPending &&
    workflowQuery.isEnabled &&
    !workflowPageIsExhausted &&
    workflowQuery.isFetchedAfterMount &&
    !workflowQuery.error
      ? workflowQuery.data
      : undefined;
  const commitPage =
    canQueryHistory &&
    !scopeIsPending &&
    commitQuery.isEnabled &&
    !commitPageIsExhausted &&
    commitQuery.isFetchedAfterMount &&
    !commitQuery.error
      ? commitQuery.data
      : undefined;
  const workflowScans: WorkbenchScan[] = (workflowPage?.items ?? [])
    .filter(
      (workflow) =>
        !resolvedScope ||
        (workflow.repo_id === resolvedScope.repoId &&
          (workflow.repo_connector_id ?? null) ===
            resolvedScope.repoConnectorId),
    )
    .map((workflow) => {
      const scopedConfiguration =
        configuration?.scan_input.repo_id === workflow.repo_id &&
        (configuration.scan_input.repo_connector_id ?? null) ===
          (workflow.repo_connector_id ?? null)
          ? configuration
          : undefined;
      const repositoryUrl =
        workflow.repository_url ??
        scopedConfiguration?.scan_input.repo_url ??
        (workflow.repo_connector_id == null && workflow.repository_full_name
          ? `https://github.com/${workflow.repository_full_name}`
          : "");
      const environmentId =
        workflow.environment_id ??
        scopedConfiguration?.scan_input.environment_id;
      return {
        id: workflow.run_id,
        workflow,
        scanType: "repository_scan",
        repositoryId: workflow.repo_id,
        repositoryName:
          workflow.repository_full_name ??
          (repositoryUrl ? repositoryLabel(repositoryUrl) : workflow.repo_id),
        repositoryUrl,
        environmentLabel: environmentId
          ? environmentLabels.get(environmentId)
          : null,
        isEnvironmentLoading: Boolean(environmentId) && environmentsAreLoading,
      };
    });
  const commitScans: WorkbenchScan[] = (commitPage?.items ?? [])
    .filter(
      (scan) =>
        configuration &&
        (scan.scan_configuration_id === configuration.id ||
          scan.scan_configuration_id === configuration.hid) &&
        scan.scan_input.repo_id === configuration.scan_input.repo_id &&
        normalizedRepositoryUrl(scan.scan_input.repo_url) ===
          normalizedRepositoryUrl(configuration.scan_input.repo_url) &&
        (scan.scan_input.repo_connector_id ?? null) ===
          (configuration.scan_input.repo_connector_id ?? null),
    )
    .map((commitScan) => {
      const environmentId =
        commitScan.scan_input.environment_id ||
        configuration?.scan_input.environment_id;
      const repositoryUrl = commitScan.scan_input.repo_url;
      return {
        id: commitScan.id,
        commitScan,
        scanType: "commit_scan",
        repositoryId: commitScan.scan_input.repo_id,
        repositoryName:
          repositoryLabel(repositoryUrl) || commitScan.scan_input.repo_id,
        repositoryUrl,
        environmentLabel: environmentId
          ? environmentLabels.get(environmentId)
          : null,
        isEnvironmentLoading: Boolean(environmentId) && environmentsAreLoading,
      };
    });
  const scans = [...workflowScans, ...commitScans];
  const filteredScans = filterAndSortWorkbenchScans({
    scans,
    searchQuery: text,
    statusFilter: status,
    scanTypeFilter: selectedScanType,
    sortField,
    sortDescending,
    intl,
  });
  const repositoriesById = new Map<string, Map<string, WorkflowRepository>>();
  for (const repository of authorizedRepositories?.items ?? []) {
    const identities = repositoriesById.get(repository.repo_id) ?? new Map();
    identities.set(repositoryIdentityKey(repository), repository);
    repositoriesById.set(repository.repo_id, identities);
  }
  const repositoryOptions = new Map<
    string,
    { value: string; label: string; url?: string }
  >();
  for (const [repoId, identities] of repositoriesById) {
    if (identities.size !== 1) continue;
    const repository = Array.from(identities.values())[0];
    const selectedConfigurationUrl =
      configuration?.scan_input.repo_id === repoId &&
      (configuration.scan_input.repo_connector_id ?? null) ===
        (repository.repo_connector_id ?? null)
        ? configuration.scan_input.repo_url
        : undefined;
    repositoryOptions.set(repoId, {
      value: repoId,
      label: repository.repository_full_name,
      url: selectedConfigurationUrl ?? publicRepositoryUrl(repository),
    });
  }

  function replaceSearch(parameters: URLSearchParams) {
    const value = parameters.toString();
    setSearch(value ? `?${value}` : "", { replace: true });
  }

  function resetPagination() {
    setPreviousPages({});
    const parameters = new URLSearchParams(search);
    const hadPagination = PAGINATION_PARAMETERS.some((parameter) =>
      parameters.has(parameter),
    );
    if (!hadPagination) return;
    clearPagination(parameters);
    replaceSearch(parameters);
  }

  function selectRepository(nextRepositoryId: string) {
    const parameters = new URLSearchParams(search);
    clearPagination(parameters);
    setPreviousPages({});
    if (nextRepositoryId === "__all_repositories__") {
      if (scanType === "commit_scan") setScanType("all");
      parameters.delete("repo_id");
      parameters.delete("repo");
      parameters.delete("scan_configuration_id");
      replaceSearch(parameters);
      return;
    }
    const repository = repositoryOptions.get(nextRepositoryId);
    parameters.set("repo_id", nextRepositoryId);
    if (repository?.url) parameters.set("repo", repository.url);
    else parameters.delete("repo");
    // Resolve the matching configuration after selection. A configuration
    // from the previous repository is never carried into the new scope.
    parameters.delete("scan_configuration_id");
    replaceSearch(parameters);
  }

  function clearFilters() {
    setText("");
    setStatus("all");
    setScanType("all");
    const parameters = new URLSearchParams(search);
    if (!routeRepositoryId) {
      parameters.delete("repo_id");
      parameters.delete("repo");
      parameters.delete("scan_configuration_id");
    }
    clearPagination(parameters);
    setPreviousPages({});
    replaceSearch(parameters);
  }

  function toggleSort(nextField: ScanSortField) {
    if (sortField === nextField) {
      setSortDescending((value) => !value);
      return;
    }
    setSortField(nextField);
    setSortDescending(nextField === "started");
  }

  const hasClientFilters =
    text.trim() !== "" || status !== "all" || selectedScanType !== "all";
  const configurationLookupError =
    Boolean(configurationId && configurationById.error) ||
    Boolean(!configurationId && configurationsForScope.error);
  const scanHistoryError =
    scopeIsUnavailable ||
    Boolean(workflowQuery.error) ||
    Boolean(commitQuery.error) ||
    configurationLookupError ||
    Boolean(
      hasExplicitRepositoryScope &&
        !resolvedScope?.configuration &&
        repositories.error,
    );
  const isPending =
    scopeIsPending ||
    (workflowQuery.isEnabled &&
      (workflowQuery.isPending || !workflowQuery.isFetchedAfterMount)) ||
    (commitQuery.isEnabled &&
      (commitQuery.isPending || !commitQuery.isFetchedAfterMount));
  const isFetching =
    configurationById.isFetching ||
    configurationsForScope.isFetching ||
    (hasExplicitRepositoryScope && repositories.isFetching) ||
    workflowQuery.isFetching ||
    commitQuery.isFetching;
  const retry = () => {
    if (configurationById.error) void configurationById.refetch();
    if (configurationsForScope.error) void configurationsForScope.refetch();
    if (repositories.error) void repositories.refetch();
    if (workflowQuery.error) void workflowQuery.refetch();
    if (commitQuery.error) void commitQuery.refetch();
  };
  const retryAction =
    configurationLookupError ||
    repositories.error ||
    workflowQuery.error ||
    commitQuery.error ? (
      <Button
        type="button"
        color="outlineSurface"
        loading={isFetching}
        onClick={retry}
      >
        {intl.formatMessage(scanMessages.retryHistory)}
      </Button>
    ) : undefined;

  return (
    <section className={workbenchStyles.collectionPage}>
      <WorkbenchToolbar>
        <WorkbenchSearchInput
          id="scan-search"
          searchQuery={text}
          onSearchQueryChange={(value) => {
            resetPagination();
            setText(value);
          }}
          label={intl.formatMessage(scanMessages.searchScans)}
          placeholder={intl.formatMessage(scanMessages.searchScans)}
        />
        <div className="flex min-w-0 items-center gap-2 max-sm:w-full">
          <ScansFilterMenu
            repositoryFilter={
              routeRepositoryId
                ? undefined
                : {
                    value: resolvedScope?.repoId ?? "__all_repositories__",
                    options: [
                      {
                        value: "__all_repositories__",
                        label: intl.formatMessage(scanMessages.allRepositories),
                      },
                      ...Array.from(repositoryOptions.values())
                        .sort((first, second) =>
                          first.label.localeCompare(second.label),
                        )
                        .map(({ value, label }) => ({ value, label })),
                    ],
                    onChange: selectRepository,
                  }
            }
            scanType={selectedScanType}
            commitScansRequireRepository={!hasExplicitRepositoryScope}
            status={status}
            onScanTypeChange={(value) => {
              resetPagination();
              setScanType(value);
            }}
            onStatusChange={(value) => {
              resetPagination();
              setStatus(value);
            }}
            onClearFilters={clearFilters}
          />
        </div>
      </WorkbenchToolbar>
      {scanHistoryError && scans.length > 0 ? (
        <WorkbenchState variant="inline" action={retryAction}>
          <FormattedMessage
            id="codexSecurity.workbench.scans.error"
            defaultMessage="Scan history could not be loaded."
            description="Sanitized error shown when authorized scan history cannot be retrieved."
          />
        </WorkbenchState>
      ) : null}
      <WorkbenchScansTable
        scans={filteredScans}
        emptyState={
          filteredScans.length > 0
            ? null
            : isPending
            ? "loading"
            : scanHistoryError
            ? "unavailable"
            : hasClientFilters
            ? "filtered"
            : "unfiltered"
        }
        sort={{ field: sortField, descending: sortDescending }}
        onSort={toggleSort}
        retryAction={retryAction}
        pagination={{
          busy: isFetching,
          canGoPrevious: Object.hasOwn(previousPages, paginationKey(search)),
          canGoNext:
            !scanHistoryError &&
            Boolean(workflowPage?.next_cursor || commitPage?.next_cursor),
          onPrevious: () => {
            const previous = previousPages[paginationKey(search)];
            if (previous == null) return;
            setSearch(previous ? `?${previous}` : "", { replace: true });
          },
          onNext: () => {
            const parameters = new URLSearchParams(search);
            const nextWorkflowCursor = workflowPage?.next_cursor;
            const nextCommitCursor = commitPage?.next_cursor;
            if (!nextWorkflowCursor && !nextCommitCursor) return;
            if (workflowQuery.isEnabled) {
              if (nextWorkflowCursor) {
                parameters.set("cursor", nextWorkflowCursor);
                parameters.delete("workflow_exhausted");
              } else {
                parameters.set("workflow_exhausted", "true");
              }
            }
            if (commitQuery.isEnabled) {
              if (nextCommitCursor) {
                parameters.set("commit_cursor", nextCommitCursor);
                parameters.delete("commit_exhausted");
              } else {
                parameters.set("commit_exhausted", "true");
              }
            }
            const nextPageKey = paginationKey(parameters);
            setPreviousPages((pages) => ({
              ...pages,
              [nextPageKey]: search.toString(),
            }));
            replaceSearch(parameters);
          },
        }}
      />
    </section>
  );
}

function ScanDetail({ id }: { id: string }) {
  const { repositoryId: routeRepositoryId } = useParams();
  const { accountId, identity } = useCloud();
  const [confirmCancel, setConfirmCancel] = useState(false);
  const {
    data: run,
    error,
    isPending,
    isFetching,
    isFetchedAfterMount,
    refetch,
  } = useQuery({
    queryKey: ["scan", accountId, identity?.userId ?? "none", id],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_get",
        parameters: {
          path: { run_id: id },
          query: { include_ownership: true },
        },
      }),
    refetchOnMount: "always",
    staleTime: 4_000,
    refetchInterval: (query) =>
      query.state.data && running.has(query.state.data.status) ? 4_000 : false,
  });
  const authorizedRun = isFetchedAfterMount && !error ? run : undefined;
  const repositories = useQuery({
    queryKey: [
      "scan-detail-repositories",
      accountId,
      identity?.userId ?? "none",
    ],
    queryFn: () =>
      securityClient.request({ operation: "workflow_repositories" }),
    refetchOnMount: "always",
    staleTime: 60_000,
  });
  const repositoryRuns = useQuery({
    queryKey: [
      "scan-detail-repository-runs",
      accountId,
      identity?.userId ?? "none",
      authorizedRun?.repo_id,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_list",
        parameters: {
          query: {
            repo_id: authorizedRun?.repo_id,
            limit: 50,
            include_ownership: true,
          },
        },
      }),
    enabled: Boolean(authorizedRun?.repo_id),
    refetchOnMount: "always",
    staleTime: 15_000,
  });
  const monitoring = useQuery({
    queryKey: [
      "scan-detail-monitoring",
      accountId,
      identity?.userId ?? "none",
      authorizedRun?.repo_id,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: {
            repo_id: authorizedRun?.repo_id,
            scan_type: "continuous_scan",
            limit: 25,
          },
        },
      }),
    enabled: Boolean(authorizedRun?.repo_id),
    refetchOnMount: "always",
    staleTime: 15_000,
  });
  const environments = useQuery({
    queryKey: ["scan-environments", accountId, identity?.userId ?? "none"],
    queryFn: () => securityClient.request({ operation: "environments_list" }),
    refetchOnMount: "always",
    staleTime: 60_000,
  });
  const {
    mutate: cancel,
    error: cancelError,
    isPending: canceling,
    reset: resetCancel,
  } = useMutation({
    mutationFn: () =>
      securityClient.request({
        operation: "workflow_cancel",
        parameters: { path: { run_id: id } },
      }),
    onSuccess: async () => {
      setConfirmCancel(false);
      await refetch();
    },
  });
  if (isPending || !isFetchedAfterMount) {
    return <WorkbenchState loading />;
  }
  if (error || !run) {
    return (
      <ScanDetailUnavailable
        retryAction={
          <Button
            color="outlineSurface"
            loading={isFetching}
            onClick={() => void refetch()}
          >
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.retry"
              defaultMessage="Retry"
              description="Retries loading the selected authorized scan."
            />
          </Button>
        }
      />
    );
  }
  if (routeRepositoryId && routeRepositoryId !== run.repo_id) {
    return <ScanDetailUnavailable />;
  }

  const repositoryMetadata = (
    repositories.isFetchedAfterMount && !repositories.error
      ? repositories.data?.items
      : undefined
  )?.find(
    (repository) =>
      repository.repo_id === run.repo_id &&
      (repository.repo_connector_id ?? null) ===
        (run.repo_connector_id ?? null),
  );
  const repositoryRun = (
    repositoryRuns.isFetchedAfterMount && !repositoryRuns.error
      ? repositoryRuns.data?.items
      : undefined
  )?.find(
    (candidate) =>
      candidate.run_id === run.run_id &&
      candidate.repo_id === run.repo_id &&
      (candidate.repo_connector_id ?? null) === (run.repo_connector_id ?? null),
  );
  const repositoryConfiguration = (
    monitoring.isFetchedAfterMount && !monitoring.error
      ? monitoring.data?.items
      : undefined
  )?.find(
    (configuration) =>
      configuration.scan_input.repo_id === run.repo_id &&
      (configuration.scan_input.repo_connector_id ?? null) ===
        (run.repo_connector_id ?? null),
  );
  const repositoryUrl =
    repositoryRun?.repository_url ??
    repositoryConfiguration?.scan_input.repo_url ??
    (run.repo_connector_id == null && repositoryMetadata?.repository_full_name
      ? `https://github.com/${repositoryMetadata.repository_full_name}`
      : "");
  const repositoryName =
    repositoryRun?.repository_full_name ??
    repositoryMetadata?.repository_full_name ??
    (repositoryUrl ? repositoryLabel(repositoryUrl) : run.repo_id);
  const environmentLabel =
    environments.isFetchedAfterMount && !environments.error
      ? environments.data?.find(
          (environment) => environment.id === run.environment_id,
        )?.label
      : undefined;
  const scan: WorkbenchScan = {
    id: run.run_id,
    workflow: run,
    scanType: "repository_scan",
    repositoryId: run.repo_id,
    repositoryName,
    repositoryUrl,
    environmentLabel,
    isEnvironmentLoading:
      environments.isPending || !environments.isFetchedAfterMount,
  };
  const findingsPath = routeRepositoryId
    ? `/repositories/${encodeURIComponent(routeRepositoryId)}/findings`
    : "/findings";
  const outputs = run.output_ids?.length ? (
    <div className="space-y-6">
      {run.output_ids.map((outputId) => (
        <div key={outputId} className="min-h-[28rem]">
          <ScanWorkflowOutput runId={id} outputId={outputId} />
        </div>
      ))}
    </div>
  ) : undefined;

  return (
    <ScanDetailPresentation
      scan={scan}
      outputs={outputs}
      findings={
        repositoryUrl ? (
          <ScanFindings
            detailBasePath={findingsPath}
            repositoryId={run.repo_id}
            repositoryUrl={repositoryUrl}
            scanId={run.run_id}
            scanStatus={run.status}
            source="repository_scan"
          />
        ) : (
          <ScanFindingsUnavailable />
        )
      }
      failureMessage={run.failure_message}
      isCanceling={canceling}
      onRequestCancel={() => {
        resetCancel();
        setConfirmCancel(true);
      }}
      cancelConfirmation={
        <ScanCancelConfirmation
          open={confirmCancel}
          canceling={canceling}
          failed={Boolean(cancelError)}
          onOpenChange={(open) => {
            setConfirmCancel(open);
            if (!open) resetCancel();
          }}
          onConfirm={() => cancel()}
        />
      }
    />
  );
}

function ScanDetailUnavailable({ retryAction }: { retryAction?: ReactNode }) {
  return (
    <WorkbenchState action={retryAction}>
      <FormattedMessage
        id="codexSecurity.workbench.scans.detail.unavailable"
        defaultMessage="This scan is unavailable or you do not have access to it."
        description="Privacy-preserving notice when a scan cannot be loaded or accessed."
      />
    </WorkbenchState>
  );
}
