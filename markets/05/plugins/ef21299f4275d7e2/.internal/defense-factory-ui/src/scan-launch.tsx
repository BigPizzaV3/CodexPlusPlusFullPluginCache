import { LoadingIndicator } from "@oai/ds/ui/indicator";
import { Select } from "@oai/ds/ui/select";
import {
  useInfiniteQuery,
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useNavigate, useSearchParams } from "react-router";

import { useCloud } from "./app-context";
import { useDebouncedValue } from "./use-debounced-value";
import {
  connectGithub,
  logSecurityEvent,
  openEnvironment,
  securityClient,
} from "./client";
import {
  getRepositoryConnectionState,
  loadRepositoryEnvironments,
  selectedRepositoryEnvironmentId,
} from "./repository-connector";
import { WorkbenchButton as Button, WorkbenchLink } from "./workbench/controls";
import {
  ScanSetupFieldRow,
  ScanSetupForm,
  ScanSetupNotice,
  ScanSetupPage,
  ScanSetupRetryNotice,
  ScanSetupScopeFields,
  type ScanSetupScope,
} from "./workbench/scan-setup-layout";
import { workbenchStyles } from "./workbench/styles";
import {
  retainWorkflowSelections,
  selectedWorkflowOption,
  workflowOptions,
  workflowStepConfigs,
  type WorkflowDefinition,
  type WorkflowSelections,
} from "./workflow-selection";

const modelLabels: Record<string, string> = {
  "gpt-daybreak-blue-latest": "Daybreak",
  "gpt-5.6-luna": "GPT-5.6 Luna",
  "gpt-6-astra": "GPT-6 Astra",
};

export function ScanLaunch() {
  const cloud = useCloud();
  const cache = useQueryClient();
  const intl = useIntl();
  const effortLabels: Record<string, string> = {
    medium: intl.formatMessage({
      id: "defenseFactory.plugin.scanEffortMedium",
      defaultMessage: "Medium",
      description: "Medium reasoning effort option.",
    }),
    high: intl.formatMessage({
      id: "defenseFactory.plugin.scanEffortHigh",
      defaultMessage: "High",
      description: "High reasoning effort option.",
    }),
  };
  const navigate = useNavigate();
  const [search] = useSearchParams();
  const [repoId, setRepoId] = useState(search.get("repo_id") ?? "");
  const [text, setText] = useState("");
  const [scope, setScope] = useState<ScanSetupScope>("full-commit");
  const workflowIdentity = JSON.stringify([
    cloud.accountId,
    cloud.identity?.workspaceId,
    cloud.identity?.userId,
  ]);
  const [previousWorkflowIdentity, setPreviousWorkflowIdentity] =
    useState(workflowIdentity);
  const [workflowSelections, setWorkflowSelections] =
    useState<WorkflowSelections>({});
  const [previousDefinition, setPreviousDefinition] =
    useState<WorkflowDefinition>();
  const debouncedText = useDebouncedValue(text.trim(), 300);
  const [selectedConnectorId, setSelectedConnectorId] = useState<string | null>(
    null,
  );
  const {
    connectorId,
    status: connectionStatus,
    canQuery,
  } = getRepositoryConnectionState(cloud, repoId, selectedConnectorId);
  const [selectedEnvironment, setSelectedEnvironment] = useState<{
    repoId: string;
    id: string;
  } | null>(null);
  const [attempt, setAttempt] = useState<{ key: string; id: string } | null>(
    null,
  );
  const workflowDefinition = useQuery({
    queryKey: [
      "workflow-definition",
      cloud.accountId,
      cloud.identity?.workspaceId,
      cloud.identity?.userId,
      "codex-security.security-scan",
    ],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_definition",
        parameters: { path: { workflow_id: "codex-security.security-scan" } },
      }),
    enabled: canQuery && scope === "full-commit",
  });
  if (
    workflowIdentity !== previousWorkflowIdentity ||
    workflowDefinition.data !== previousDefinition
  ) {
    setPreviousWorkflowIdentity(workflowIdentity);
    setPreviousDefinition(workflowDefinition.data);
    // Clear choices from another account or removed options before rendering.
    setWorkflowSelections(
      workflowIdentity === previousWorkflowIdentity && workflowDefinition.data
        ? retainWorkflowSelections(workflowDefinition.data, workflowSelections)
        : {},
    );
  }
  const workflowSteps = workflowStepConfigs(
    workflowDefinition.data,
    workflowSelections,
  );
  const workflowReady = workflowSteps != null && !workflowDefinition.isError;
  const {
    data: pages,
    error: repositoriesError,
    isPending: repositoriesPending,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    isFetching: repositoriesFetching,
    isFetchNextPageError: repositoriesNextPageError,
    refetch: refreshRepositories,
  } = useInfiniteQuery({
    queryKey: [
      "github-repositories",
      cloud.accountId,
      cloud.identity?.userId,
      connectorId,
      debouncedText,
    ],
    queryFn: ({ pageParam }) =>
      debouncedText
        ? securityClient.request({
            operation: "github_search",
            parameters: {
              query: {
                query: debouncedText,
                page: pageParam,
                limit: 50,
                connector_id: connectorId,
              },
            },
          })
        : securityClient.request({
            operation: "github_repositories",
            parameters: {
              query: {
                page: pageParam,
                per_page: 50,
                connector_id: connectorId,
              },
            },
          }),
    initialPageParam: 1,
    getNextPageParam: (last, _pages, page) =>
      last.repositories.length === 50 ? page + 1 : undefined,
    enabled: canQuery,
    staleTime: 60_000,
  });
  const repositories = pages?.pages.flatMap((page) => page.repositories);
  const {
    data: selectedRepository,
    error: selectedRepositoryError,
    refetch: refreshSelectedRepository,
  } = useQuery({
    queryKey: [
      "repository",
      cloud.accountId,
      cloud.identity?.userId,
      repoId,
      connectorId,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "github_get",
        parameters: {
          path: { repo_id: repoId },
          query: { connector_id: connectorId },
        },
      }),
    enabled:
      canQuery && !!repoId && !repositories?.some((repo) => repo.id === repoId),
    staleTime: 60_000,
  });
  const repository =
    repositories?.find((repo) => repo.id === repoId) ?? selectedRepository;
  const {
    data: environments,
    error: environmentError,
    isPending: environmentsPending,
    isFetching: environmentsFetching,
    refetch: refreshEnvironments,
  } = useQuery({
    queryKey: [
      "environments",
      cloud.accountId,
      cloud.identity?.workspaceId,
      cloud.identity?.userId,
      repoId,
      connectorId,
    ],
    queryFn: () =>
      loadRepositoryEnvironments(securityClient, repoId, connectorId),
    enabled: canQuery && !!repoId,
    staleTime: 60_000,
  });
  const {
    data: configurations,
    error: configurationError,
    isPending: configurationsPending,
    refetch: refreshConfiguration,
  } = useQuery({
    queryKey: [
      "launch-monitoring",
      repoId,
      cloud.accountId,
      cloud.identity?.userId,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: { repo_id: repoId, scan_type: "continuous_scan", limit: 1 },
        },
      }),
    enabled: canQuery && !!repoId,
    staleTime: 15_000,
  });
  const existingConfiguration = configurations?.items.find(
    (configuration) => configuration.scan_input.repo_id === repoId,
  );
  const monitoringLimit = cloud.scanLimits?.count ?? -1;
  const monitoringQuotaExhausted =
    !existingConfiguration &&
    monitoringLimit >= 0 &&
    configurations?.quota_used != null &&
    configurations.quota_used >= monitoringLimit;
  // Monitoring suggests a default environment; it must not block a one-time scan.
  const configuredEnvironmentId =
    configurations?.items[0]?.scan_input.environment_id;
  const environmentsReady =
    !environmentsPending && !environmentsFetching && !environmentError;
  const environmentId = selectedRepositoryEnvironmentId(
    environments,
    selectedEnvironment?.repoId === repoId ? selectedEnvironment.id : undefined,
    configuredEnvironmentId,
  );
  const {
    mutate: editEnvironment,
    error: editorError,
    isPending: editing,
  } = useMutation({
    mutationFn: (id?: string) => {
      if (!environmentsReady)
        throw new Error("Wait for compatible Cloud environments to load");
      return openEnvironment(id);
    },
    onSuccess: async (result) => {
      await refreshEnvironments();
      if (result.environmentId)
        setSelectedEnvironment({ repoId, id: result.environmentId });
    },
  });
  const {
    mutate: connect,
    error: connectionError,
    isPending: connecting,
  } = useMutation({
    mutationFn: () => {
      if (!connectorId) throw new Error("GitHub connection is not available");
      return connectGithub(connectorId);
    },
    onSuccess: () => cache.invalidateQueries({ queryKey: ["bootstrap"] }),
  });
  const {
    mutate: launch,
    error: launchError,
    isPending: launching,
  } = useMutation({
    mutationFn: async () => {
      if (!repository || !environmentId || !canQuery || !environmentsReady)
        throw new Error("Choose a repository and Cloud environment");
      if (!workflowReady || workflowSteps == null)
        throw new Error("Choose the workflow model and reasoning effort");
      const key = JSON.stringify([
        cloud.accountId,
        cloud.identity?.workspaceId,
        cloud.identity?.userId,
        repoId,
        connectorId,
        environmentId,
        workflowSteps,
      ]);
      const idempotencyKey =
        attempt?.key === key ? attempt.id : crypto.randomUUID();
      // An ambiguous response must retry the same launch rather than creating another paid scan.
      setAttempt({ key, id: idempotencyKey });
      return securityClient.request({
        operation: "workflow_launch",
        requestBody: {
          workflow_id: "codex-security.security-scan",
          repo_id: repository.id,
          repo_connector_id: connectorId,
          environment_id: environmentId,
          idempotency_key: idempotencyKey,
          steps: workflowSteps,
        },
      });
    },
    onSuccess: (run) =>
      void navigate(`/runs/${encodeURIComponent(run.run_id)}`),
  });
  const {
    mutate: createMonitoring,
    error: monitoringCreateError,
    isPending: creatingMonitoring,
  } = useMutation({
    mutationFn: async () => {
      if (
        !repository ||
        !environmentId ||
        !cloud.identity ||
        !canQuery ||
        !environmentsReady ||
        configurationError
      )
        throw new Error("Choose a repository and Cloud environment");

      // A fresh authorized lookup prevents a stale picker from creating a
      // second continuous configuration for the same repository.
      const current = await securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: {
            repo_id: repository.id,
            scan_type: "continuous_scan",
            limit: 1,
          },
        },
      });
      const existing = current.items.find(
        (configuration) => configuration.scan_input.repo_id === repository.id,
      );
      if (existing)
        return { kind: "existing" as const, configuration: existing };
      if (
        monitoringLimit >= 0 &&
        current.quota_used != null &&
        current.quota_used >= monitoringLimit
      )
        throw new Error("The monitoring limit has been reached");

      const configuration = await securityClient.request({
        operation: "monitoring_create",
        requestBody: {
          environment_id: environmentId,
          repo_id: repository.id,
          repo_url: repository.clone_url,
          repo_connector_id: connectorId,
          owner_id: cloud.identity.userId,
          scan_type: "continuous_scan",
          state: "enabled",
          lookback_days: null,
          share_targets: [],
          notification_rules: [],
        },
      });
      return { kind: "created" as const, configuration };
    },
    onSuccess: async (result) => {
      const savedRepoId = result.configuration.scan_input.repo_id;
      if (result.kind === "created") {
        logSecurityEvent({
          name: "AardvarkScanConfigurationSaved",
          data: {
            repoId: savedRepoId,
            scanEnabled: true,
            isNewConfig: true,
          },
        });
      }
      await Promise.all([
        cache.invalidateQueries({
          queryKey: ["launch-monitoring", savedRepoId],
        }),
        cache.invalidateQueries({ queryKey: ["monitoring-metadata"] }),
        cache.invalidateQueries({
          queryKey: ["repository-monitoring", savedRepoId],
        }),
      ]);
      void navigate(`/repositories/${encodeURIComponent(savedRepoId)}`);
    },
  });
  const isSubmitting = launching || creatingMonitoring;
  const isCommitMonitoring = scope === "diff";
  return (
    <ScanSetupPage>
      <ScanSetupForm
        footer={
          canQuery ? (
            <Button
              color="primary"
              disabled={
                !repository ||
                !environmentId ||
                !environmentsReady ||
                !canQuery ||
                (!isCommitMonitoring && !workflowReady) ||
                (isCommitMonitoring &&
                  (configurationsPending ||
                    !!configurationError ||
                    !!existingConfiguration ||
                    monitoringQuotaExhausted ||
                    !cloud.identity))
              }
              loading={isSubmitting}
              onClick={() =>
                isCommitMonitoring ? createMonitoring() : launch()
              }
            >
              {isCommitMonitoring ? (
                <FormattedMessage
                  id="codexSecurity.createPanel.create"
                  defaultMessage="Create"
                  description="Primary action that creates continuous commit monitoring."
                />
              ) : (
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.submit"
                  defaultMessage="Start scan"
                  description="Primary action that starts one authorized full-repository Security scan."
                />
              )}
            </Button>
          ) : undefined
        }
      >
        {(cloud.githubConnections?.length ?? 0) > 1 ? (
          <ScanSetupFieldRow
            label={
              <FormattedMessage
                id="defenseFactory.plugin.githubConnection"
                defaultMessage="GitHub connection"
                description="GitHub connection used to browse repositories."
              />
            }
            value={
              <div className="w-full min-w-64 sm:w-80">
                <Select
                  value={connectorId ?? ""}
                  block
                  pill={false}
                  triggerClassName={workbenchStyles.selectControl}
                  options={cloud.githubConnections!.map((item) => ({
                    value: item.connectorId,
                    label: item.label,
                  }))}
                  aria-label={intl.formatMessage({
                    id: "defenseFactory.plugin.githubConnection",
                    defaultMessage: "GitHub connection",
                    description:
                      "Choose the public GitHub or GitHub Enterprise connection to browse and scan.",
                  })}
                  onChange={(option) => {
                    setSelectedConnectorId(option.value);
                    setRepoId("");
                    setText("");
                    setSelectedEnvironment(null);
                  }}
                />
              </div>
            }
          />
        ) : null}

        {connectionStatus === "connect" ? (
          <ScanSetupNotice
            action={
              <Button
                color="primary"
                onClick={() => connect()}
                loading={connecting}
              >
                <FormattedMessage
                  id="defenseFactory.plugin.connectGithub"
                  defaultMessage="Connect GitHub"
                  description="Open GitHub connection setup."
                />
              </Button>
            }
          >
            <FormattedMessage
              id="defenseFactory.plugin.connectPrompt"
              defaultMessage="Connect GitHub to choose a repository and start a scan."
              description="A GitHub connection is required to launch a scan."
            />
          </ScanSetupNotice>
        ) : null}
        {connectionError ? (
          <ScanSetupRetryNotice onRetry={() => connect()}>
            <FormattedMessage
              id="defenseFactory.plugin.connectGithubError"
              defaultMessage="GitHub connection setup could not be completed. Try again."
              description="Sanitized error shown when GitHub connection setup fails."
            />
          </ScanSetupRetryNotice>
        ) : null}
        {connectionStatus === "disabled" ? (
          <ScanSetupNotice>
            <FormattedMessage
              id="defenseFactory.plugin.githubDisabled"
              defaultMessage="Your workspace administrator has disabled GitHub connections."
              description="GitHub cannot be connected under workspace policy."
            />
          </ScanSetupNotice>
        ) : null}
        {!canQuery && connectionStatus === "loading" ? (
          <ScanSetupNotice loading />
        ) : null}
        {!canQuery && connectionStatus === "error" ? (
          <ScanSetupRetryNotice
            onRetry={() =>
              void cache.invalidateQueries({ queryKey: ["bootstrap"] })
            }
          >
            <FormattedMessage
              id="defenseFactory.plugin.githubError"
              defaultMessage="GitHub connection availability could not be loaded."
              description="Sanitized error shown when GitHub connection state cannot be loaded."
            />
          </ScanSetupRetryNotice>
        ) : null}

        {canQuery ? (
          <>
            <ScanSetupFieldRow
              label={
                <FormattedMessage
                  id="defenseFactory.plugin.repository"
                  defaultMessage="Repository"
                  description="Source repository for a Security scan."
                />
              }
              value={
                <div className="flex w-full min-w-64 flex-col gap-2 sm:w-96">
                  <Select
                    value={repoId}
                    block
                    pill={false}
                    searchable
                    triggerClassName={`df-repository-picker ${workbenchStyles.selectControl}`}
                    searchValue={text}
                    onSearchChange={setText}
                    searchPlaceholder={intl.formatMessage({
                      id: "defenseFactory.plugin.searchRepos",
                      defaultMessage: "Search repositories",
                      description: "Search accessible GitHub repositories.",
                    })}
                    // The server filters results; the preserved selection is not a search result.
                    searchPredicate={(option) =>
                      repositories?.some((item) => item.id === option.value) ??
                      false
                    }
                    searchEmptyMessage={
                      repositoriesPending ? (
                        <FormattedMessage
                          id="defenseFactory.plugin.searchReposLoading"
                          defaultMessage="Searching repositories…"
                          description="Status while repository search results load."
                        />
                      ) : (
                        <FormattedMessage
                          id="defenseFactory.plugin.searchReposEmpty"
                          defaultMessage="No matching repositories"
                          description="Empty state for the repository picker."
                        />
                      )
                    }
                    // Select's loading prop disables typing, including during remote searches.
                    endAdornment={
                      repositoriesPending || isFetchingNextPage ? (
                        <LoadingIndicator className="h-4 w-4" />
                      ) : undefined
                    }
                    pagination={{
                      hasNextPage:
                        canQuery &&
                        debouncedText === text.trim() &&
                        !!hasNextPage &&
                        !repositoriesError,
                      isFetching: repositoriesFetching,
                      onLoadMore: () => {
                        void fetchNextPage({ cancelRefetch: false });
                      },
                    }}
                    options={[
                      ...(repository &&
                      !repositories?.some((item) => item.id === repository.id)
                        ? [repository]
                        : []),
                      ...(repositories ?? []),
                    ].map((item) => ({
                      value: item.id,
                      label: item.repository_full_name,
                    }))}
                    aria-label={intl.formatMessage({
                      id: "defenseFactory.plugin.chooseRepo",
                      defaultMessage: "Choose a repository",
                      description: "Choose a repository to scan.",
                    })}
                    onChange={(option) => setRepoId(option.value)}
                    placeholder={intl.formatMessage({
                      id: "defenseFactory.plugin.chooseRepo",
                      defaultMessage: "Choose a repository",
                      description: "Choose a repository to scan.",
                    })}
                  />
                </div>
              }
            />
            {repositoriesError || selectedRepositoryError ? (
              <ScanSetupRetryNotice
                onRetry={() => {
                  if (repositoriesError) {
                    void (repositoriesNextPageError
                      ? fetchNextPage({ cancelRefetch: false })
                      : refreshRepositories());
                  }
                  if (selectedRepositoryError) void refreshSelectedRepository();
                }}
              >
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.repositoriesUnavailable"
                  defaultMessage="Repositories could not be loaded. Try again."
                  description="Sanitized inline error for repository availability on the New Scan form."
                />
              </ScanSetupRetryNotice>
            ) : null}

            <ScanSetupFieldRow
              label={
                <FormattedMessage
                  id="defenseFactory.plugin.cloudEnvironment"
                  defaultMessage="Cloud environment"
                  description="Cloud runtime environment for a scan."
                />
              }
              value={
                repoId ? (
                  <div className="flex w-full min-w-64 flex-col gap-2 sm:w-96">
                    <Select
                      value={environmentId ?? ""}
                      block
                      pill={false}
                      triggerClassName={workbenchStyles.selectControl}
                      options={
                        environments?.map((environment) => ({
                          value: environment.id,
                          label: environment.label,
                        })) ?? []
                      }
                      loading={environmentsPending || environmentsFetching}
                      aria-label={intl.formatMessage({
                        id: "defenseFactory.plugin.chooseEnvironment",
                        defaultMessage: "Choose an environment",
                        description: "Choose a compatible Cloud environment.",
                      })}
                      onChange={(option) =>
                        setSelectedEnvironment({ repoId, id: option.value })
                      }
                      placeholder={intl.formatMessage({
                        id: "defenseFactory.plugin.chooseEnvironment",
                        defaultMessage: "Choose an environment",
                        description: "Choose a compatible Cloud environment.",
                      })}
                    />
                    <div className="flex flex-wrap justify-end gap-2">
                      <Button
                        color="outlineSurface"
                        onClick={() => editEnvironment(undefined)}
                        disabled={!environmentsReady}
                        loading={editing}
                      >
                        <FormattedMessage
                          id="defenseFactory.plugin.createEnvironment"
                          defaultMessage="Create environment"
                          description="Open the shared Cloud environment creation dialog."
                        />
                      </Button>
                      {environmentId ? (
                        <Button
                          color="ghostSecondary"
                          onClick={() => editEnvironment(environmentId)}
                          disabled={!environmentsReady}
                        >
                          <FormattedMessage
                            id="defenseFactory.plugin.editEnvironment"
                            defaultMessage="Edit environment"
                            description="Edit the selected Cloud environment."
                          />
                        </Button>
                      ) : null}
                    </div>
                  </div>
                ) : (
                  <span className="text-token-text-secondary text-[14px] leading-5">
                    <FormattedMessage
                      id="defenseFactory.plugin.chooseRepoFirst"
                      defaultMessage="Choose a repository first"
                      description="A repository must be selected before showing compatible environments."
                    />
                  </span>
                )
              }
            />
            {environmentError ? (
              <ScanSetupRetryNotice onRetry={() => void refreshEnvironments()}>
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.environmentsUnavailable"
                  defaultMessage="Compatible Cloud environments could not be loaded. Try again or choose another repository."
                  description="Sanitized inline error for Cloud environment availability on the New Scan form."
                />
              </ScanSetupRetryNotice>
            ) : null}
            {configurationError ? (
              <ScanSetupRetryNotice onRetry={() => void refreshConfiguration()}>
                {isCommitMonitoring ? (
                  <FormattedMessage
                    id="codexSecurity.workbench.scans.launch.monitoringAvailabilityUnavailable"
                    defaultMessage="Existing monitoring could not be checked. Try again before creating monitoring."
                    description="Sanitized blocking error when duplicate monitoring cannot be checked."
                  />
                ) : (
                  <FormattedMessage
                    id="codexSecurity.workbench.scans.launch.environmentPreferenceUnavailable"
                    defaultMessage="The saved environment preference could not be loaded. Choose an environment or try again."
                    description="Sanitized non-blocking error for the suggested scan environment."
                  />
                )}
              </ScanSetupRetryNotice>
            ) : null}
            {editorError ? (
              <ScanSetupNotice>
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.environmentEditorUnavailable"
                  defaultMessage="Cloud environment setup could not be completed. Try the environment action again."
                  description="Sanitized inline error shown when creating or editing a Cloud environment fails."
                />
              </ScanSetupNotice>
            ) : null}

            <ScanSetupScopeFields
              scope={scope}
              disabled={isSubmitting}
              onScopeChange={setScope}
            />

            {!isCommitMonitoring && workflowDefinition.isError ? (
              <ScanSetupRetryNotice
                onRetry={() => void workflowDefinition.refetch()}
              >
                <FormattedMessage
                  id="defenseFactory.plugin.workflowOptionsError"
                  defaultMessage="Model and reasoning options could not be loaded. Try again."
                  description="Error loading the scan's available workflow settings."
                />
              </ScanSetupRetryNotice>
            ) : !isCommitMonitoring && !workflowDefinition.data ? (
              <ScanSetupNotice loading>
                <FormattedMessage
                  id="defenseFactory.plugin.workflowOptionsLoading"
                  defaultMessage="Loading model and reasoning options…"
                  description="Status while the scan's available workflow settings load."
                />
              </ScanSetupNotice>
            ) : !isCommitMonitoring ? (
              workflowDefinition.data?.steps.flatMap((step) => {
                const fields = [
                  {
                    key: "model" as const,
                    options: workflowOptions(step.agent.model),
                    label: intl.formatMessage({
                      id: "defenseFactory.plugin.model",
                      defaultMessage: "Model",
                      description: "Model used for this scan.",
                    }),
                    placeholder: intl.formatMessage({
                      id: "defenseFactory.plugin.selectModel",
                      defaultMessage: "Select a model",
                      description: "Prompt to choose a scan model.",
                    }),
                  },
                  ...(step.agent.reasoning
                    ? [
                        {
                          key: "effort" as const,
                          options: workflowOptions(step.agent.reasoning.effort),
                          label: intl.formatMessage({
                            id: "defenseFactory.plugin.reasoningEffort",
                            defaultMessage: "Reasoning effort",
                            description: "Reasoning effort used for this scan.",
                          }),
                          placeholder: intl.formatMessage({
                            id: "defenseFactory.plugin.selectEffort",
                            defaultMessage: "Select reasoning effort",
                            description:
                              "Prompt to choose scan reasoning effort.",
                          }),
                        },
                      ]
                    : []),
                ];
                return fields.map((field) => (
                  <ScanSetupFieldRow
                    key={`${step.id}-${field.key}`}
                    label={field.label}
                    value={
                      <div className="w-full min-w-64 sm:w-96">
                        <Select
                          value={
                            selectedWorkflowOption(
                              field.options,
                              workflowSelections[step.id]?.[field.key],
                            ) ?? ""
                          }
                          block
                          pill={false}
                          disabled={isSubmitting || field.options.length === 1}
                          triggerClassName={workbenchStyles.selectControl}
                          options={field.options.map((value) => ({
                            value,
                            label:
                              (field.key === "model"
                                ? modelLabels
                                : effortLabels)[value] ?? value,
                          }))}
                          aria-label={field.label}
                          placeholder={field.placeholder}
                          onChange={(option) =>
                            setWorkflowSelections((previous) => ({
                              ...previous,
                              [step.id]: {
                                ...previous[step.id],
                                [field.key]: option.value,
                              },
                            }))
                          }
                        />
                      </div>
                    }
                  />
                ));
              })
            ) : null}

            {isCommitMonitoring && repoId && configurationsPending ? (
              <ScanSetupNotice loading>
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.checkingMonitoring"
                  defaultMessage="Checking existing monitoring…"
                  description="Status shown while checking whether a repository already has monitoring."
                />
              </ScanSetupNotice>
            ) : null}
            {isCommitMonitoring && existingConfiguration ? (
              <ScanSetupNotice
                action={
                  <WorkbenchLink
                    color="outlineSurface"
                    to={`/repositories/${encodeURIComponent(repoId)}`}
                  >
                    <FormattedMessage
                      id="codexSecurity.createPanel.viewExistingScan"
                      defaultMessage="View monitoring"
                      description="Open this repository's existing continuous monitoring configuration."
                    />
                  </WorkbenchLink>
                }
              >
                <FormattedMessage
                  id="codexSecurity.createPanel.alreadyScannedMessage"
                  defaultMessage="This repository already has continuous monitoring."
                  description="Inline notice that prevents creating duplicate repository monitoring."
                />
              </ScanSetupNotice>
            ) : null}
            {isCommitMonitoring &&
            !configurationsPending &&
            !configurationError &&
            monitoringQuotaExhausted ? (
              <ScanSetupNotice>
                <FormattedMessage
                  id="defenseFactory.plugin.monitoringQuota"
                  defaultMessage="This workspace has reached its limit of {count, number} monitored repositories."
                  description="The workspace cannot create more repository monitoring configurations."
                  values={{ count: monitoringLimit }}
                />
              </ScanSetupNotice>
            ) : null}

            {!isCommitMonitoring && launchError ? (
              <ScanSetupRetryNotice onRetry={() => launch()}>
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.temporarilyUnavailable"
                  defaultMessage="The scan could not be started. Try again."
                  description="Sanitized inline launch error for a one-time repository scan."
                />
              </ScanSetupRetryNotice>
            ) : null}
            {isCommitMonitoring && monitoringCreateError ? (
              <ScanSetupRetryNotice onRetry={() => createMonitoring()}>
                <FormattedMessage
                  id="codexSecurity.workbench.scans.launch.monitoringCreateUnavailable"
                  defaultMessage="Continuous monitoring could not be created. Try again."
                  description="Sanitized inline error after creating continuous monitoring fails."
                />
              </ScanSetupRetryNotice>
            ) : null}
          </>
        ) : null}
      </ScanSetupForm>
    </ScanSetupPage>
  );
}
