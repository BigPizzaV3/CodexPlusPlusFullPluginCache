import { DotsHorizontal as DotsHorizontalIcon } from "@oai/ds/icons/dots-horizontal";
import { Download as DownloadIcon } from "@oai/ds/icons/download";
import { Menu } from "@oai/ds/ui/menu";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useDeferredValue, useEffect, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import {
  Navigate,
  useLocation,
  useNavigate,
  useParams,
  useSearchParams,
} from "react-router";

import { downloadFile, securityClient } from "./client";
import type { DefenseFactoryRequest } from "./contract";
import { FindingDetail } from "./finding-detail";
import { useCloud } from "./app-context";
import {
  ActiveFindingsFilters,
  FindingsFilterMenu,
  FindingsStatusView,
} from "./workbench/findings-filters";
import {
  FindingsTableView,
  pageSize,
  type FindingTableRow,
} from "./workbench/findings-table";
import type { Finding } from "./workbench/types";
import { WorkbenchState, WorkbenchToolbar } from "./workbench/layout";
import {
  WorkbenchButton as Button,
  WorkbenchSearchInput,
} from "./workbench/controls";
import { workbenchStyles } from "./workbench/styles";
import {
  getCodexSecurityFindingsClearSearch,
  OPEN_FINDING_STATUSES,
} from "./workbench/findings-utils";
import {
  findingSearchMessage,
  retiredFindingFilterParams,
} from "./workbench/findings-fields";
import { parseFindingSource } from "./workbench/finding-source-types";
import { FindingsSankey } from "./workbench/findings-sankey";
import { WorkbenchNavigation } from "./workbench/navigation";
import { WorkbenchRefreshControls } from "./workbench/refresh-controls";
import "./workbench/findings-presentation.css";

function combinedFindingRow(finding: Finding): FindingTableRow {
  return {
    id: finding.id,
    repo_id: finding.repo_id,
    repo_url: finding.repo_url,
    title: finding.title,
    criticality: finding.criticality,
    status: finding.status,
    created_at: finding.created_at,
    scanType: finding.source.kind,
    commit_hash:
      finding.source.kind === "commit_scan"
        ? finding.observed_revision ?? null
        : null,
    environmentSource:
      finding.source.kind === "repository_scan"
        ? { kind: "workflow_run", id: finding.source.workflow_run_id }
        : { kind: "finding", id: finding.id },
  };
}

type FindingPageHistory = {
  scopeKey: string;
  cursors: Array<string | null>;
};

function isFindingPageHistory(value: unknown): value is FindingPageHistory {
  return (
    value != null &&
    typeof value === "object" &&
    "scopeKey" in value &&
    typeof value.scopeKey === "string" &&
    "cursors" in value &&
    Array.isArray(value.cursors) &&
    value.cursors.every(
      (cursor) => cursor == null || typeof cursor === "string",
    )
  );
}

export function Findings() {
  const { id, repositoryId } = useParams();
  const [search] = useSearchParams();
  const searchRepositoryIds = (search.get("repo_id") ?? "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);
  const searchRepositoryUrls = (search.get("repo") ?? "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);
  const scopedRepositoryId =
    repositoryId ??
    (searchRepositoryIds.length === 1 ? searchRepositoryIds[0] : null);
  const scopedRepositoryUrl = repositoryId
    ? null
    : searchRepositoryUrls.length === 1
    ? searchRepositoryUrls[0]
    : null;
  return id ? (
    <FindingDetail
      key={`${id}:${scopedRepositoryId ?? scopedRepositoryUrl ?? "all"}`}
      id={id}
      repositoryId={scopedRepositoryId}
      repositoryUrl={scopedRepositoryUrl}
    />
  ) : (
    <FindingsList />
  );
}

function FindingsList() {
  const location = useLocation();
  const normalizedSearch = normalizeFindingsSearch(location.search);
  if (normalizedSearch !== location.search) {
    return (
      <Navigate
        replace
        state={location.state}
        to={{
          pathname: location.pathname,
          search: normalizedSearch,
          hash: location.hash,
        }}
      />
    );
  }
  return <FindingsCollection />;
}

function normalizeFindingsSearch(search: string) {
  const params = new URLSearchParams(search);
  let changed = false;
  let resetPaging = false;
  if (!params.has("status")) {
    params.set("status", OPEN_FINDING_STATUSES.join(","));
    changed = true;
    resetPaging = true;
  } else if (params.get("status")?.trim().toLowerCase() === "all") {
    params.set("status", "");
    changed = true;
  }
  if (params.has("sev")) {
    if (!params.has("criticality")) {
      params.set("criticality", params.get("sev") ?? "");
      resetPaging = true;
    }
    params.delete("sev");
    changed = true;
  }
  for (const key of retiredFindingFilterParams) {
    if (params.has(key)) {
      params.delete(key);
      changed = true;
      resetPaging = true;
    }
  }
  if (params.has("source") && !parseFindingSource(params.get("source"))) {
    params.delete("source");
    changed = true;
    resetPaging = true;
  }
  if (resetPaging) {
    params.delete("cursor");
    params.delete("page");
  }
  const nextSearch = params.toString();
  return changed ? (nextSearch ? `?${nextSearch}` : "") : search;
}

function FindingsCollection() {
  const intl = useIntl();
  const [search] = useSearchParams();
  const location = useLocation();
  const navigate = useNavigate();
  const { repositoryId } = useParams();
  const { accountId, identity } = useCloud();
  const requestedCursor = search.get("cursor");
  const currentCursor =
    requestedCursor && !/^\d+$/.test(requestedCursor) ? requestedCursor : null;
  const limit = pageSize(location.search);
  const scopeParams = new URLSearchParams(search);
  scopeParams.delete("cursor");
  scopeParams.delete("page");
  scopeParams.set("limit", String(limit));
  scopeParams.sort();
  const scopeKey = JSON.stringify([
    accountId,
    identity?.userId,
    scopeParams.toString(),
  ]);
  // Router state survives opening a finding and going Back.
  const history = isFindingPageHistory(location.state) ? location.state : null;
  const cursors = history?.scopeKey === scopeKey ? history.cursors : [];
  const keywordQuery = search.get("q") ?? "";
  const [keywordDraft, setKeywordDraft] = useState(keywordQuery);
  const deferredText = useDeferredValue(keywordQuery);
  useEffect(() => setKeywordDraft(keywordQuery), [keywordQuery]);
  useEffect(() => {
    const normalizedKeyword = keywordDraft.trim();
    if (normalizedKeyword === keywordQuery) return;
    const timeout = window.setTimeout(() => {
      const params = new URLSearchParams(location.search);
      if (normalizedKeyword) params.set("q", normalizedKeyword);
      else params.delete("q");
      params.delete("cursor");
      params.delete("page");
      const nextSearch = params.toString();
      navigate(
        { search: nextSearch ? `?${nextSearch}` : "", hash: location.hash },
        { replace: true },
      );
    }, 300);
    return () => window.clearTimeout(timeout);
  }, [keywordDraft, keywordQuery, location.hash, location.search, navigate]);
  const query: NonNullable<
    DefenseFactoryRequest<"findings_list">["parameters"]
  >["query"] = {
    q: deferredText || undefined,
    repo: search.get("repo") || undefined,
    status:
      search.get("status") === "all"
        ? ""
        : search.get("status") ?? "new,triaged,in_progress",
    criticality: search.get("criticality") || search.get("sev") || undefined,
    start_at: search.get("start_at") || undefined,
    end_at: search.get("end_at") || undefined,
    source: parseFindingSource(search.get("source")) ?? undefined,
    sort: search.get("sort") ?? "sev_desc,date_desc",
    cursor: currentCursor ?? undefined,
    limit,
  };
  const { data, dataUpdatedAt, error, isPending, isFetching, refetch } = useQuery({
    queryKey: ["findings", accountId, query],
    queryFn: () =>
      securityClient.request({
        operation: "findings_list",
        parameters: { query },
      }),
    staleTime: 15_000,
  });
  const {
    mutate: exportFindings,
    isPending: exporting,
    error: exportError,
  } = useMutation({
    mutationFn: async () =>
      downloadFile(
        await securityClient.request({
          operation: "findings_export",
          // Export the complete filtered result, independently of the visible
          // cursor page and its user-selected page size.
          parameters: {
            query: { ...query, cursor: undefined, limit: undefined },
          },
        }),
      ),
  });
  const offset = data?.offset ?? 0;
  function changePage(nextOffset: number) {
    const forward = nextOffset > offset;
    const nextCursor = forward ? data?.next_cursor : cursors.at(-1);
    if (forward && !nextCursor) return;
    const params = new URLSearchParams(search);
    if (nextCursor) params.set("cursor", nextCursor);
    else params.delete("cursor");
    params.delete("page");
    navigate(
      { search: params.toString() ? `?${params}` : "", hash: location.hash },
      {
        replace: true,
        state: {
          scopeKey,
          cursors: forward ? [...cursors, currentCursor] : cursors.slice(0, -1),
        } satisfies FindingPageHistory,
      },
    );
  }
  function clearFilters() {
    setKeywordDraft("");
    const nextSearch = getCodexSecurityFindingsClearSearch(location.search);
    navigate({ search: nextSearch, hash: location.hash }, { replace: true });
  }
  return (
    <section className={workbenchStyles.collectionPage}>
      {!repositoryId ? (
        <WorkbenchNavigation
          actions={
            <WorkbenchRefreshControls
              asOf={data && !error && !isFetching ? dataUpdatedAt : undefined}
              showRefresh={data != null}
              isRefreshing={isFetching}
              onRefresh={() => void refetch({ cancelRefetch: false })}
            />
          }
        />
      ) : null}
      <WorkbenchToolbar>
        <WorkbenchSearchInput
          id="finding-search"
          searchQuery={keywordDraft}
          onSearchQueryChange={setKeywordDraft}
          label={intl.formatMessage(findingSearchMessage)}
          placeholder={intl.formatMessage(findingSearchMessage)}
        />
        <div className="df-findings-toolbar-actions">
          <FindingsStatusView />
          <FindingsFilterMenu onClearFilters={clearFilters} />
          <Menu>
            <Menu.Trigger>
              <Button
                type="button"
                color="outlineSurface"
                size="toolbar"
                uniform
                loading={exporting}
                aria-label={intl.formatMessage({
                  id: "codex.security.workbench.findings.actions.more.label",
                  defaultMessage: "More finding actions",
                  description:
                    "Accessible label for the ellipsis menu beside Filters above the Security Findings table.",
                })}
              >
                <DotsHorizontalIcon className="icon-sm" aria-hidden />
              </Button>
            </Menu.Trigger>
            <Menu.Content align="end" minWidth={180}>
              <Menu.Item disabled={exporting} onSelect={() => exportFindings()}>
                <DownloadIcon className="icon-sm" aria-hidden />
                <FormattedMessage
                  id="codex.security.workbench.findings.export.button.label"
                  defaultMessage="Export CSV"
                  description="Action that downloads all Security findings matching the current filters."
                />
              </Menu.Item>
              {repositoryId ? (
                <Menu.Item disabled={isFetching} onSelect={() => void refetch()}>
                  <FormattedMessage
                    id="defenseFactory.plugin.refresh"
                    defaultMessage="Refresh"
                    description="Reload the current Security data"
                  />
                </Menu.Item>
              ) : null}
            </Menu.Content>
          </Menu>
        </div>
      </WorkbenchToolbar>
      <ActiveFindingsFilters onClearFilters={clearFilters} />
      {data && !error && data.items.length > 0 ? (
        <FindingsSankey findings={data.items} total={data.total} />
      ) : null}
      {exportError ? (
        <WorkbenchState
          variant="inline"
          action={
            <Button
              color="outlineSurface"
              size="toolbar"
              onClick={() => exportFindings()}
            >
              <FormattedMessage
                id="defenseFactory.plugin.retry"
                defaultMessage="Try again"
                description="Retry exporting Security findings"
              />
            </Button>
          }
        >
          <FormattedMessage
            id="codex.security.workbench.findings.export.error"
            defaultMessage="Findings could not be exported."
            description="Error shown when exporting filtered Security findings fails."
          />
        </WorkbenchState>
      ) : null}
      <FindingsTableView
        detailBasePath={
          repositoryId
            ? `/repositories/${encodeURIComponent(repositoryId)}/findings`
            : "/findings"
        }
        cursor={offset}
        hasPrevious={Boolean(currentCursor)}
        previousIsFirst={Boolean(currentCursor) && cursors.length === 0}
        hasNext={Boolean(data?.next_cursor)}
        onPageChange={changePage}
        findingsQuery={{
          data: data && {
            items: data.items.map(combinedFindingRow),
            total: data.total,
          },
          error,
          isLoading: isPending,
          isFetching,
          refetch,
        }}
      />
    </section>
  );
}
