import { WorkbenchIcon } from "./workbench/icons";
import { DotsHorizontal as DotsHorizontalIcon } from "@oai/ds/icons/dots-horizontal";
import { Menu } from "@oai/ds/ui/menu";
import { Select } from "@oai/ds/ui/select";
import { Tooltip } from "@oai/ds/ui/tooltip";
import {
  useInfiniteQuery,
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { useEffect, useRef, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { Navigate, useLocation, useParams } from "react-router";

import { useCloud } from "./app-context";
import { connectGithub, securityClient } from "./client";
import { Findings } from "./findings";
import { AppLink } from "./link";
import { MonitoringSettings } from "./monitoring-settings";
import { getRepositoryConnectionState } from "./repository-connector";
import { Scans } from "./scans";
import { Empty, repositoryLabel, RequestState, Status } from "./ui";
import { useDebouncedValue } from "./use-debounced-value";
import {
  WorkbenchButton as Button,
  WorkbenchSearchInput,
} from "./workbench/controls";
import { InfiniteScroll } from "./workbench/infinite-scroll";
import {
  WorkbenchState,
  WorkbenchTableFooter,
  WorkbenchToolbar,
} from "./workbench/layout";
import { WorkbenchRepositoryDetail } from "./workbench/repository-detail";
import { workbenchStyles } from "./workbench/styles";

export function Repositories() {
  const { id, repositoryId, section } = useParams();
  const selectedRepositoryId = repositoryId ?? id;
  const repositorySection =
    section === "findings" || section === "scans" ? section : "overview";
  return selectedRepositoryId ? (
    <RepositoryDetail
      key={selectedRepositoryId}
      id={selectedRepositoryId}
      section={repositorySection}
    />
  ) : (
    <RepositoryList />
  );
}

function RepositoryList() {
  const cloud = useCloud();
  const intl = useIntl();
  const cache = useQueryClient();
  const [text, setText] = useState("");
  const [deleted, setDeleted] = useState(false);
  const searchInputRef = useRef<HTMLInputElement>(null);
  const focusSearchOnReturn = useRef(false);
  useEffect(() => {
    if (!deleted && focusSearchOnReturn.current) {
      searchInputRef.current?.focus();
      focusSearchOnReturn.current = false;
    }
  }, [deleted]);
  const term = useDebouncedValue(text.trim(), 300);
  const [selectedConnectorId, setSelectedConnectorId] = useState<string>();
  const { connectorId, status, canQuery } = getRepositoryConnectionState(
    cloud,
    undefined,
    selectedConnectorId,
  );
  const {
    data: metadata,
    error,
    isPending,
    isFetching: refreshingMetadata,
    refetch,
  } = useQuery({
    queryKey: ["monitoring-metadata"],
    queryFn: () => securityClient.request({ operation: "monitoring_metadata" }),
    staleTime: 15_000,
  });
  const {
    data: repositories,
    error: discoveryError,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
    isFetchNextPageError: discoveryNextPageError,
    isPending: discovering,
    isFetching: refreshingDiscovery,
    refetch: refreshDiscovery,
  } = useInfiniteQuery({
    queryKey: ["repository-catalog", connectorId, term],
    queryFn: ({ pageParam }) =>
      term
        ? securityClient.request({
            operation: "github_search",
            parameters: {
              query: {
                query: term,
                connector_id: connectorId,
                page: pageParam,
                limit: 50,
              },
            },
          })
        : securityClient.request({
            operation: "github_repositories",
            parameters: {
              query: {
                connector_id: connectorId,
                page: pageParam,
                per_page: 50,
              },
            },
          }),
    initialPageParam: 1,
    getNextPageParam: (page, _pages, index) =>
      page.repositories.length === 50 ? index + 1 : undefined,
    enabled: canQuery,
    staleTime: 60_000,
  });
  const {
    data: removed,
    error: deletedError,
    fetchNextPage: loadMoreDeleted,
    hasNextPage: hasMoreDeleted,
    isPending: deletedPending,
    isFetching: refreshingDeleted,
    isFetchingNextPage: loadingMoreDeleted,
    isFetchNextPageError: deletedNextPageError,
    refetch: refreshDeleted,
  } = useInfiniteQuery({
    queryKey: ["deleted-monitoring"],
    queryFn: ({ pageParam }) =>
      securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: {
            scan_type: "continuous_scan",
            recently_deleted: true,
            limit: 50,
            cursor: pageParam,
          },
        },
      }),
    initialPageParam: undefined as string | undefined,
    getNextPageParam: (page) => page.next_cursor ?? undefined,
    enabled: deleted,
    staleTime: 15_000,
  });
  const {
    mutate: restore,
    error: restoreError,
    isPending: restoring,
  } = useMutation({
    mutationFn: (id: string) =>
      securityClient.request({
        operation: "monitoring_recover",
        parameters: { path: { id } },
      }),
    onSuccess: () =>
      Promise.all([
        cache.invalidateQueries({ queryKey: ["deleted-monitoring"] }),
        cache.invalidateQueries({ queryKey: ["monitoring-metadata"] }),
      ]),
  });
  const rows = new Map<
    string,
    { id: string; name: string; state: string; owner: string | null }
  >();
  const {
    mutate: connect,
    error: connectError,
    isPending: connecting,
  } = useMutation({
    mutationFn: () => connectGithub(connectorId!),
    onSuccess: () => cache.invalidateQueries({ queryKey: ["bootstrap"] }),
  });
  for (const repo of repositories?.pages.flatMap((page) => page.repositories) ??
    [])
    rows.set(repo.id, {
      id: repo.id,
      name: repo.repository_full_name,
      state: "unmonitored",
      owner: null,
    });
  for (const config of metadata?.items ?? [])
    rows.set(config.repo_id, {
      id: config.repo_id,
      name: repositoryLabel(config.repo_url),
      state: config.state ?? "unmonitored",
      owner: config.owner_email,
    });
  const filtered = [...rows.values()].filter((row) =>
    row.name.toLowerCase().includes(term.toLowerCase()),
  );
  const removedConfigurations =
    removed?.pages.flatMap((page) => page.items) ?? [];
  const searchLabel = intl.formatMessage({
    id: "defenseFactory.plugin.searchRepos",
    defaultMessage: "Search repositories",
    description: "Search accessible GitHub repositories",
  });
  const refreshLabel = intl.formatMessage({
    id: "defenseFactory.plugin.refresh",
    defaultMessage: "Refresh",
    description: "Reload the current data",
  });
  const isRefreshing = deleted
    ? refreshingDeleted
    : refreshingMetadata || (canQuery && refreshingDiscovery);
  return (
    <div className={`${workbenchStyles.collectionPage} df-repositories-page`}>
      <WorkbenchToolbar>
        {deleted ? (
          <div className="flex min-w-0 flex-1 flex-wrap items-center gap-3">
            <Button
              color="ghostSecondary"
              onClick={() => {
                focusSearchOnReturn.current = true;
                setDeleted(false);
              }}
            >
              <FormattedMessage
                id="defenseFactory.plugin.backToRepositories"
                defaultMessage="Back to repositories"
                description="Return from deleted monitoring to the repository list."
              />
            </Button>
            <h2 className="text-[16px] font-medium leading-6">
              <FormattedMessage
                id="defenseFactory.plugin.deletedMonitoring"
                defaultMessage="Deleted monitoring"
                description="Heading for monitoring configurations that can be restored."
              />
            </h2>
          </div>
        ) : (
          <WorkbenchSearchInput
            id="repository-search"
            inputRef={searchInputRef}
            searchQuery={text}
            onSearchQueryChange={setText}
            label={searchLabel}
            placeholder={searchLabel}
          />
        )}
        {!deleted && (cloud.githubConnections?.length ?? 0) > 1 && (
          <Select
            block={false}
            triggerClassName={`${workbenchStyles.selectControl} df-repository-provider`}
            value={connectorId ?? ""}
            options={cloud.githubConnections!.map((item) => ({
              value: item.connectorId,
              label: item.label,
            }))}
            onChange={(option) => setSelectedConnectorId(option.value)}
            aria-label={intl.formatMessage({
              id: "defenseFactory.plugin.githubConnectionChoice",
              defaultMessage: "GitHub connection",
              description:
                "Choose the public GitHub or GitHub Enterprise connection to browse",
            })}
          />
        )}
        <Tooltip content={refreshLabel}>
          <Button
            color="outlineSurface"
            uniform
            loading={isRefreshing}
            aria-busy={isRefreshing}
            aria-label={refreshLabel}
            onClick={() =>
              void (deleted
                ? refreshDeleted()
                : Promise.all([
                    refetch(),
                    ...(canQuery ? [refreshDiscovery()] : []),
                  ]))
            }
          >
            <WorkbenchIcon name="refresh" />
          </Button>
        </Tooltip>
        <Menu>
          <Menu.Trigger>
            <Button
              color="outlineSurface"
              uniform
              aria-label={intl.formatMessage({
                id: "defenseFactory.plugin.moreRepositoryActions",
                defaultMessage: "More repository actions",
                description:
                  "Accessible label for the repository overflow menu.",
              })}
            >
              <DotsHorizontalIcon className="icon-sm" aria-hidden />
            </Button>
          </Menu.Trigger>
          <Menu.Content align="end" minWidth={240}>
            <Menu.Item disabled={deleted} onSelect={() => setDeleted(true)}>
              <FormattedMessage
                id="defenseFactory.plugin.restoreDeletedMonitoring"
                defaultMessage="Restore deleted monitoring…"
                description="Open the list of deleted monitoring configurations available to restore."
              />
            </Menu.Item>
          </Menu.Content>
        </Menu>
      </WorkbenchToolbar>
      {!deleted && status === "connect" && (
        <div className="flex flex-wrap items-center gap-3 text-[14px] text-secondary">
          <p>
            <FormattedMessage
              id="defenseFactory.plugin.connectRepositoryDiscovery"
              defaultMessage="Connect GitHub to discover repositories and configure monitoring"
              description="A GitHub connection is needed to discover unmonitored repositories"
            />
          </p>
          <Button
            color="outlineSurface"
            loading={connecting}
            onClick={() => connect()}
          >
            <FormattedMessage
              id="defenseFactory.plugin.connectGithub"
              defaultMessage="Connect GitHub"
              description="Open GitHub connection setup"
            />
          </Button>
          {connectError && <RequestState error={connectError} />}
        </div>
      )}
      {!deleted && status === "disabled" && (
        <p role="status" className="text-[14px] text-secondary">
          <FormattedMessage
            id="defenseFactory.plugin.githubDisabled"
            defaultMessage="Your workspace administrator has disabled GitHub connections"
            description="GitHub cannot be connected under workspace policy"
          />
        </p>
      )}
      {deleted ? (
        <div className="flex flex-col gap-3">
          {(deletedPending ||
            (deletedError && !deletedNextPageError) ||
            restoreError) && (
            <RequestState
              error={deletedError ?? restoreError}
              retry={() => void refreshDeleted()}
            />
          )}
          {!deletedPending &&
            !deletedError &&
            !removedConfigurations.length && (
              <Empty>
                <FormattedMessage
                  id="defenseFactory.plugin.noDeletedMonitoring"
                  defaultMessage="No recently deleted monitoring configurations"
                  description="There are no monitoring configurations available to restore"
                />
              </Empty>
            )}
          {removedConfigurations.map((config) => (
            <div
              key={config.hid}
              className="flex items-center justify-between rounded-xl border border-default p-4"
            >
              <span>{repositoryLabel(config.scan_input.repo_url)}</span>
              <Button
                color="outlineSurface"
                loading={restoring}
                disabled={
                  !cloud.identity?.isAdmin &&
                  config.owner_id !== cloud.identity?.userId &&
                  !config.permissions?.can_write
                }
                onClick={() => restore(config.hid || config.id)}
              >
                <FormattedMessage
                  id="defenseFactory.plugin.restore"
                  defaultMessage="Restore"
                  description="Restore a deleted monitoring configuration"
                />
              </Button>
            </div>
          ))}
          {(removedConfigurations.length > 0 || hasMoreDeleted) && (
            <WorkbenchTableFooter
              summary={
                <FormattedMessage
                  id="defenseFactory.plugin.deletedMonitoringLoadedCount"
                  defaultMessage="{count, plural, one {# configuration loaded} other {# configurations loaded}}"
                  description="Number of recently deleted monitoring configurations loaded so far."
                  values={{ count: removedConfigurations.length }}
                />
              }
            >
              <InfiniteScroll
                key={removed?.pages.length}
                enabled={
                  !!hasMoreDeleted && !refreshingDeleted && !deletedError
                }
                loading={loadingMoreDeleted}
                onLoadMore={() => {
                  void loadMoreDeleted({ cancelRefetch: false });
                }}
              />
            </WorkbenchTableFooter>
          )}
          {deletedNextPageError && (
            <RequestState
              error={deletedError}
              retry={() => void loadMoreDeleted({ cancelRefetch: false })}
            />
          )}
        </div>
      ) : isPending ||
        error ||
        (canQuery && discovering && !filtered.length) ? (
        <RequestState error={error} retry={() => void refetch()} />
      ) : (
        <>
          {discoveryError && !discoveryNextPageError && (
            <p role="status" className="text-[14px] text-secondary">
              <FormattedMessage
                id="defenseFactory.plugin.repoDiscoveryError"
                defaultMessage="Repository discovery is unavailable. Configured repositories are shown below."
                description="GitHub discovery failed but authorized monitoring remains visible"
              />
            </p>
          )}
          <div className={workbenchStyles.table}>
            <div className="overflow-x-auto">
              <table className="w-full table-fixed text-left text-[14px] leading-5 sm:table-auto">
                <thead className="bg-surface-secondary text-secondary">
                  <tr>
                    <th className="border-b border-default px-4 py-3">
                      <FormattedMessage
                        id="defenseFactory.plugin.repository"
                        defaultMessage="Repository"
                        description="Source repository"
                      />
                    </th>
                    <th className="hidden border-b border-default px-4 py-3 sm:table-cell">
                      <FormattedMessage
                        id="defenseFactory.plugin.monitoring"
                        defaultMessage="Monitoring"
                        description="Continuous scanning configuration"
                      />
                    </th>
                    <th className="hidden border-b border-default px-4 py-3 sm:table-cell">
                      <FormattedMessage
                        id="defenseFactory.plugin.owner"
                        defaultMessage="Owner"
                        description="Monitoring configuration owner"
                      />
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {filtered.map((row) => (
                    <tr
                      key={row.id}
                      className={`${workbenchStyles.tableRow} hover:bg-surface-secondary`}
                    >
                      <td className="border-b border-default px-4 py-3">
                        <AppLink
                          className={`${workbenchStyles.tableLink} [overflow-wrap:anywhere]`}
                          to={`/repositories/${encodeURIComponent(row.id)}`}
                        >
                          {row.name}
                        </AppLink>
                        <dl className="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1 text-[12px] text-secondary sm:hidden">
                          <div>
                            <dt className="sr-only">
                              <FormattedMessage
                                id="defenseFactory.plugin.monitoring"
                                defaultMessage="Monitoring"
                                description="Continuous scanning configuration"
                              />
                            </dt>
                            <dd>
                              <Status value={row.state} />
                            </dd>
                          </div>
                          <div className="min-w-0">
                            <dt className="sr-only">
                              <FormattedMessage
                                id="defenseFactory.plugin.owner"
                                defaultMessage="Owner"
                                description="Monitoring configuration owner"
                              />
                            </dt>
                            <dd className="[overflow-wrap:anywhere]">
                              {row.owner ?? "—"}
                            </dd>
                          </div>
                        </dl>
                      </td>
                      <td className="hidden border-b border-default px-4 py-3 sm:table-cell">
                        <Status value={row.state} />
                      </td>
                      <td
                        className={`hidden border-b border-default px-4 py-3 text-[12px] sm:table-cell ${workbenchStyles.tableSecondaryValue}`}
                      >
                        {row.owner ?? "—"}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            {!filtered.length && (
              <Empty>
                <FormattedMessage
                  id="defenseFactory.plugin.noRepos"
                  defaultMessage="No repositories match this search"
                  description="Empty repository list"
                />
              </Empty>
            )}
            <WorkbenchTableFooter
              summary={
                <FormattedMessage
                  id="defenseFactory.plugin.repositoriesLoadedCount"
                  defaultMessage="{count, plural, one {# repository loaded} other {# repositories loaded}}"
                  description="Number of repositories currently displayed after filtering. More may remain on the server."
                  values={{ count: filtered.length }}
                />
              }
            >
              <InfiniteScroll
                key={repositories?.pages.length}
                enabled={
                  canQuery &&
                  term === text.trim() &&
                  !!hasNextPage &&
                  !refreshingDiscovery &&
                  !discoveryError
                }
                loading={isFetchingNextPage}
                onLoadMore={() => {
                  void fetchNextPage({ cancelRefetch: false });
                }}
              />
            </WorkbenchTableFooter>
            {discoveryNextPageError && (
              <RequestState
                error={discoveryError}
                retry={() => void fetchNextPage({ cancelRefetch: false })}
              />
            )}
          </div>
        </>
      )}
    </div>
  );
}

function RepositoryDetail({
  id,
  section,
}: {
  id: string;
  section: "overview" | "findings" | "scans";
}) {
  const cloud = useCloud();
  const location = useLocation();
  const { connectorId, canQuery } = getRepositoryConnectionState(cloud, id);
  const { data, error, isPending, refetch } = useQuery({
    queryKey: ["repository-monitoring", id],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_list",
        parameters: {
          query: { repo_id: id, scan_type: "continuous_scan", limit: 25 },
        },
      }),
    staleTime: 15_000,
  });
  const selected = data?.items.find(
    (config) => config.scan_input.repo_id === id,
  );
  const {
    data: workflowRepositoryData,
    error: workflowRepositoryError,
    isPending: workflowRepositoryPending,
    refetch: refreshWorkflowRepository,
  } = useQuery({
    queryKey: [
      "repository-workflow-metadata",
      cloud.accountId,
      cloud.identity?.userId,
      id,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_list",
        parameters: {
          query: { repo_id: id, limit: 1, include_ownership: true },
        },
      }),
    enabled: !isPending && !selected,
    staleTime: 15_000,
  });
  const workflowRepository = workflowRepositoryData?.items.find((run) => {
    if (run.repo_id !== id) return false;
    return run.repo_connector_id
      ? id.startsWith(`github-${run.repo_connector_id}:`)
      : !id.includes(":");
  });
  const {
    data: repository,
    error: repositoryError,
    isPending: repositoryPending,
    refetch: refreshRepository,
  } = useQuery({
    queryKey: ["repository", id, connectorId],
    queryFn: () =>
      securityClient.request({
        operation: "github_get",
        parameters: {
          path: { repo_id: id },
          query: { connector_id: connectorId },
        },
      }),
    enabled: !isPending && canQuery && (!selected || section === "overview"),
    staleTime: 60_000,
  });
  const {
    data: detail,
    isPending: detailPending,
    refetch: refreshDetail,
  } = useQuery({
    queryKey: ["monitoring", selected?.hid],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_get",
        parameters: { path: { id: selected?.hid || selected?.id || "" } },
      }),
    enabled: Boolean(selected),
    staleTime: 15_000,
  });

  const loading =
    isPending ||
    (section === "overview" && Boolean(selected) && detailPending) ||
    (!selected &&
      !repository &&
      !workflowRepository &&
      ((canQuery && repositoryPending) || workflowRepositoryPending));
  // A configured repository remains usable when optional GitHub metadata
  // or configuration detail refresh fails. The list response still provides
  // the repository scope required by nested findings and scans.
  const requestError =
    error ??
    (!selected && !repository && !workflowRepository
      ? (repositoryError ?? workflowRepositoryError)
      : null);
  if (loading) {
    return <WorkbenchState loading variant="panel" />;
  }
  if (requestError) {
    return (
      <WorkbenchState
        variant="panel"
        action={
          <Button
            color="outlineSurface"
            onClick={() =>
              void Promise.all([
                refetch(),
                ...(selected
                  ? [refreshDetail()]
                  : [refreshRepository(), refreshWorkflowRepository()]),
              ])
            }
          >
            <FormattedMessage
              id="codexSecurity.workbench.repositories.retry"
              defaultMessage="Retry"
              description="Retry loading a repository detail page."
            />
          </Button>
        }
      >
        <FormattedMessage
          id="codexSecurity.workbench.repositories.unavailableDescription"
          defaultMessage="This repository could not be found or is no longer accessible."
          description="Privacy-preserving repository unavailable message."
        />
      </WorkbenchState>
    );
  }

  const repoUrl = (
    selected?.scan_input.repo_url ??
    repository?.clone_url ??
    workflowRepository?.repository_url ??
    (workflowRepository?.repo_connector_id == null &&
    workflowRepository?.repository_full_name
      ? `https://github.com/${workflowRepository.repository_full_name}`
      : undefined)
  )?.replace(/\.git$/, "");
  if (!repoUrl) {
    return (
      <WorkbenchState
        variant="panel"
        title={
          <FormattedMessage
            id="codexSecurity.workbench.repositories.unavailableHeading"
            defaultMessage="Repository unavailable"
            description="Heading when a repository cannot be loaded."
          />
        }
      >
        <FormattedMessage
          id="codexSecurity.workbench.repositories.unavailableDescription"
          defaultMessage="This repository could not be found or is no longer accessible."
          description="Privacy-preserving repository unavailable message."
        />
      </WorkbenchState>
    );
  }

  const expectedSearch = new URLSearchParams(location.search);
  const selectedConfigurationId = selected?.hid || selected?.id || null;
  if (
    expectedSearch.get("repo") !== repoUrl ||
    expectedSearch.get("repo_id") !== id ||
    expectedSearch.get("scan_configuration_id") !== selectedConfigurationId
  ) {
    expectedSearch.set("repo", repoUrl);
    expectedSearch.set("repo_id", id);
    if (selectedConfigurationId)
      expectedSearch.set("scan_configuration_id", selectedConfigurationId);
    else expectedSearch.delete("scan_configuration_id");
    return (
      <Navigate
        replace
        to={{
          pathname: location.pathname,
          search: expectedSearch.toString(),
          hash: location.hash,
        }}
      />
    );
  }

  const canEditMonitoring = selected
    ? Boolean(detail) &&
      (cloud.identity?.isAdmin === true ||
        detail?.owner_id === cloud.identity?.userId ||
        detail?.permissions?.can_write === true)
    : true;
  const child =
    section === "findings" ? (
      <Findings />
    ) : section === "scans" ? (
      <Scans />
    ) : undefined;

  return (
    <WorkbenchRepositoryDetail
      canEditMonitoring={canEditMonitoring}
      configuration={selected ? detail : undefined}
      configurationSummary={selected}
      defaultBranch={repository?.default_branch}
      fullName={repositoryLabel(repoUrl)}
      repoId={id}
      repoUrl={repoUrl}
      section={section}
      settings={
        selected && !detail ? (
          <WorkbenchState
            variant="inline"
            action={
              <Button
                color="outlineSurface"
                onClick={() => void refreshDetail()}
              >
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.monitoringSettings.retry"
                  defaultMessage="Retry"
                  description="Retry loading repository monitoring settings."
                />
              </Button>
            }
          >
            <FormattedMessage
              id="codexSecurity.workbench.repositories.monitoringSettings.unavailable"
              defaultMessage="Monitoring settings are unavailable."
              description="Privacy-preserving message when repository monitoring settings cannot be loaded."
            />
          </WorkbenchState>
        ) : (
          <MonitoringSettings
            key={`${detail?.hid ?? id}:${detail?.version ?? 0}`}
            repoId={id}
            configuration={selected ? detail : undefined}
            quotaUsed={data?.quota_used}
            onSaved={async () => {
              await refetch();
              if (selected) await refreshDetail();
            }}
            onDeleted={async () => {
              await refetch();
            }}
          />
        )
      }
    >
      {child}
    </WorkbenchRepositoryDetail>
  );
}
