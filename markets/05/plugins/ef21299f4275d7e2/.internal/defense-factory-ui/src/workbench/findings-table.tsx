import { WorkbenchBadge as Badge, WorkbenchButton as Button } from "./controls";
import { Select } from "@oai/ds/ui/select";
import { FormattedMessage, FormattedRelativeTime, useIntl } from "react-intl";
import type { ReactNode } from "react";
import { useLocation, useNavigate } from "react-router";
import type { Finding, FindingCriticality, FindingStatus } from "./types";
import { CRITICALITY_MESSAGES, STATUS_MESSAGES } from "./messages";
import {
  getCsvParam,
  parseDateString,
  getRelativeTimeParts,
  getCodexSecurityFindingsClearSearch,
  getCodexSecurityFindingsFilterState,
  getCodexSecurityFindingsStatusSearch,
} from "./findings-utils";
import Table from "./table";
import { WorkbenchState, WorkbenchTableFooter } from "./layout";
import { workbenchStyles } from "./styles";
import { findingSourceLabels } from "./finding-source-types";
import type { FindingSortField } from "./findings-fields";
import { FindingSource } from "./finding-source";
import {
  FindingsResultsTable,
  type FindingsColumnId,
} from "./findings-results-table";
import { AppLink } from "../link";
import { repositoryLabel } from "../ui";
import "./findings-presentation.css";

const ALLOWED_PAGE_SIZES = new Set([10, 20, 50, 100]);
const DEFAULT_PAGE_SIZE = 50;
function isFindingCriticality(
  value: string | null,
): value is FindingCriticality {
  return (
    value === "critical" ||
    value === "high" ||
    value === "medium" ||
    value === "low" ||
    value === "informational"
  );
}

export type FindingTableRow = {
  id: string;
  repo_id: string;
  repo_url: string;
  title: string;
  criticality: string | null;
  status: FindingStatus;
  created_at: string | null;
  commit_hash: string | null;
  scanType: Finding["source"]["kind"];
  environmentSource: {
    kind: "environment" | "workflow_run" | "finding";
    id: string;
  };
};
export type FindingTableQuery = {
  data?: { items: FindingTableRow[]; total: number };
  isLoading: boolean;
  isFetching: boolean;
  error: unknown;
  refetch: () => unknown;
};
export function pageSize(search: string): number {
  const requested = Number(new URLSearchParams(search).get("limit"));
  return ALLOWED_PAGE_SIZES.has(requested) ? requested : DEFAULT_PAGE_SIZE;
}

export function FindingsTableView({
  detailBasePath = "/findings",
  findingsQuery,
  cursor,
  hasPrevious,
  hasNext,
  previousIsFirst = false,
  onPageChange,
  search: controlledSearch,
  onSearchChange,
  emptyMessage,
}: {
  detailBasePath?: string;
  findingsQuery: FindingTableQuery;
  cursor: number;
  hasPrevious?: boolean;
  hasNext?: boolean;
  previousIsFirst?: boolean;
  onPageChange?: (offset: number) => void;
  search?: string;
  onSearchChange?: (search: string) => void;
  emptyMessage?: ReactNode;
}) {
  "use forget";
  const intl = useIntl();
  const location = useLocation();
  const navigate = useNavigate();
  const search = controlledSearch ?? location.search;
  const searchParams = new URLSearchParams(search);
  const limit = pageSize(search);
  const findings = findingsQuery.data?.items ?? [];
  const totalFindings = findingsQuery.data?.total ?? findings.length;
  const { statusView, hasNarrowingFilters } =
    getCodexSecurityFindingsFilterState(search);
  const selectedRepositories = getCsvParam(search, "repo", "").filter(
    (repo) => repo && repo.toLowerCase() !== "all",
  );
  const isEmptyLaterPage = cursor > 0;
  const scansParams = new URLSearchParams();
  const workflowPreview = searchParams.get("workflow_runs_preview");
  if (workflowPreview)
    scansParams.set("workflow_runs_preview", workflowPreview);
  const selectedRepository =
    selectedRepositories.length === 1 ? selectedRepositories[0] : null;
  if (selectedRepository) {
    scansParams.set("repo", selectedRepository);
    const repositoryId = searchParams.get("repo_id");
    if (repositoryId) scansParams.set("repo_id", repositoryId);
  }
  const scansSearch = scansParams.toString();
  const scansPath = `${detailBasePath.replace(/\/findings$/, "/scans")}${
    scansSearch ? `?${scansSearch}` : ""
  }`;
  const sortTokens = (searchParams.get("sort") ?? "sev_desc,date_desc")
    .split(",")
    .map((token) => token.trim());
  const primarySort = sortTokens[0] ?? "sev_desc";
  const activeSortField: FindingSortField = primarySort.startsWith("date")
    ? "detected"
    : "severity";
  const sortDirection = primarySort.endsWith("_asc") ? "asc" : "desc";

  function updateSearch(nextSearchParams: URLSearchParams) {
    const nextSearch = nextSearchParams.toString();
    if (onSearchChange) {
      onSearchChange(nextSearch);
      return;
    }
    navigate(
      {
        search: nextSearch ? `?${nextSearch}` : "",
        hash: location.hash,
      },
      { replace: true },
    );
  }

  function updateSort(field: FindingSortField) {
    const nextDirection =
      activeSortField === field && sortDirection === "desc" ? "asc" : "desc";
    const primaryToken = `${
      field === "severity" ? "sev" : "date"
    }_${nextDirection}`;
    const secondaryToken = field === "severity" ? "date_desc" : "sev_desc";
    const nextSearchParams = new URLSearchParams(search);
    nextSearchParams.set("sort", `${primaryToken},${secondaryToken}`);
    nextSearchParams.delete("cursor");
    nextSearchParams.delete("page");
    updateSearch(nextSearchParams);
  }

  function updateCursor(nextCursor: number) {
    if (onPageChange) {
      onPageChange(nextCursor);
      return;
    }
    const nextSearchParams = new URLSearchParams(search);
    nextSearchParams.set("cursor", String(Math.max(0, nextCursor)));
    updateSearch(nextSearchParams);
  }

  return (
    <div className="df-findings-table">
      <FindingsResultsTable
        activeSortField={activeSortField}
        sortDirection={sortDirection}
        onSort={updateSort}
      >
        {({ columnCount, renderCells }) => (
          <>
            {findingsQuery.isLoading && findings.length === 0 ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState variant="table" loading>
                    <FormattedMessage
                      id="codexSecurity.workbench.findings.table.loading"
                      defaultMessage="Loading findings…"
                      description="Progress message shown with a spinner inside the Codex Security findings table while the first page of authorized vulnerability reports is loading."
                    />
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : findingsQuery.error ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState
                    variant="table"
                    action={
                      <Button
                        type="button"
                        color="secondary"
                        size="toolbar"
                        loading={findingsQuery.isFetching}
                        onClick={() => void findingsQuery.refetch()}
                      >
                        <FormattedMessage
                          id="codexSecurity.workbench.findings.table.retry"
                          defaultMessage="Retry"
                          description="Short recovery button inside the Codex Security findings table after authorized vulnerability reports could not be loaded. Repeats the current server request without changing the user's search, filters, or page."
                        />
                      </Button>
                    }
                  >
                    <FormattedMessage
                      id="codexSecurity.workbench.findings.table.error"
                      defaultMessage="Findings could not be loaded."
                      description="Privacy-preserving error message inside the Codex Security operations findings table when authorized vulnerability findings cannot be retrieved. Does not expose repository existence or access details."
                    />
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : findings.length === 0 ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState
                    variant="table"
                    action={
                      emptyMessage ? null : !isEmptyLaterPage &&
                        !hasNarrowingFilters &&
                        statusView === "all" ? (
                        <AppLink
                          to={scansPath}
                          className="df-control inline-flex items-center bg-surface-secondary px-3"
                        >
                          <FormattedMessage
                            id="codex.security.workbench.findings.empty.view_scans.button.label"
                            defaultMessage="View scans"
                            description="Recovery link in an empty Codex Security Findings table when no finding filters are active. Opens the existing Scans page, preserving a single selected repository when possible, so engineers can inspect available scan history. An empty findings list does not establish whether a scan has run."
                          />
                        </AppLink>
                      ) : (
                        <Button
                          type="button"
                          color="secondary"
                          onClick={() => {
                            const nextSearch = isEmptyLaterPage
                              ? search
                              : hasNarrowingFilters
                              ? getCodexSecurityFindingsClearSearch(search)
                              : getCodexSecurityFindingsStatusSearch(
                                  search,
                                  "all",
                                );
                            const params = new URLSearchParams(nextSearch);
                            params.delete("cursor");
                            params.delete("page");
                            updateSearch(params);
                          }}
                        >
                          <FormattedMessage
                            id="codex.security.workbench.findings.empty.clear.button.label"
                            defaultMessage="{view, select, page {First page} filtered {Clear filters} other {View all findings}}"
                            description="Recovery button in an empty Codex Security Findings table. The enum {view} is page for an empty later page, filtered for a narrowed search, or all for a plain Open or Closed status view. It returns to the first page, clears finding filters, or shows all statuses respectively, while preserving repository scope."
                            values={{
                              view: isEmptyLaterPage
                                ? "page"
                                : hasNarrowingFilters
                                ? "filtered"
                                : "all",
                            }}
                          />
                        </Button>
                      )
                    }
                  >
                    {emptyMessage ??
                      (isEmptyLaterPage ? (
                        <FormattedMessage
                          id="codex.security.workbench.findings.empty.page.message"
                          defaultMessage="No findings on this page."
                          description="Empty-state sentence inside the Codex Security Findings table when a requested later page is empty. The accompanying First page button keeps the current filters; an empty offset page does not prove the full filtered result is empty."
                        />
                      ) : hasNarrowingFilters ? (
                        <FormattedMessage
                          id="codexSecurity.workbench.findings.table.empty"
                          defaultMessage="No findings match your current filters."
                          description="Neutral empty-state sentence shown inside the Codex Security operations findings table when no authorized vulnerability findings match the current search or filters."
                        />
                      ) : (
                        <FormattedMessage
                          id="codex.security.workbench.findings.empty.status.message"
                          defaultMessage="{status, select, open {{repositoryCount, plural, =0 {No open findings.} one {No open findings in the selected repository.} other {No open findings in the selected repositories.}}} closed {{repositoryCount, plural, =0 {No closed findings.} one {No closed findings in the selected repository.} other {No closed findings in the selected repositories.}}} other {{repositoryCount, plural, =0 {No findings available.} one {No findings in the selected repository.} other {No findings in the selected repositories.}}}}"
                          description="Empty-state sentence in the Codex Security Findings table when no filters narrow the selected repository scope beyond the status view. The enum {status} is open, closed, or all; {repositoryCount} is the number of explicitly selected repositories, with zero meaning the global authorized list. Do not imply that a scan succeeded or that a repository has never been scanned."
                          values={{
                            status: statusView,
                            repositoryCount: selectedRepositories.length,
                          }}
                        />
                      ))}
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : (
              findings.map((finding) => {
                const findingLinkProps = {
                  to: {
                    pathname: `${detailBasePath}/${encodeURIComponent(finding.id)}`,
                    search,
                    hash: location.hash,
                  },
                  state: location.state,
                };
                const title = finding.title;
                const severity = finding.criticality;
                const detectedDate = parseDateString(finding.created_at);
                const detectedRelativeTime = getRelativeTimeParts(detectedDate);
                const severityLabel = (
                  <Table.RowTextLink {...findingLinkProps}>
                    {severity && isFindingCriticality(severity) ? (
                      <Badge
                        variant={
                          severity === "critical"
                            ? "danger"
                            : severity === "high"
                            ? "warning"
                            : severity === "medium"
                            ? "reserve"
                            : "default"
                        }
                        className={`df-findings-badge df-findings-severity-${severity}`}
                      >
                        {intl.formatMessage(CRITICALITY_MESSAGES[severity])}
                      </Badge>
                    ) : (
                      <span className="text-token-text-tertiary">
                        <FormattedMessage
                          id="aardvark.placeholder.missing"
                          defaultMessage="—"
                          description="Dash placeholder indicating missing value"
                        />
                      </span>
                    )}
                  </Table.RowTextLink>
                );
                const statusBadge = (
                  <Table.RowTextLink {...findingLinkProps}>
                    <Badge
                      variant={
                        finding.status === "fixed"
                          ? "success"
                          : finding.status === "triaged"
                          ? "warning"
                          : "default"
                      }
                      className={`df-findings-badge df-findings-status-${finding.status}`}
                    >
                      {intl.formatMessage(STATUS_MESSAGES[finding.status])}
                    </Badge>
                  </Table.RowTextLink>
                );
                const detectedLabel = (
                  <Table.RowTextLink {...findingLinkProps}>
                    <span
                      className={workbenchStyles.tableSecondaryValue}
                      title={
                        detectedDate
                          ? intl.formatDate(detectedDate, {
                              year: "numeric",
                              month: "long",
                              day: "numeric",
                              hour: "numeric",
                              minute: "2-digit",
                            })
                          : undefined
                      }
                    >
                      {detectedRelativeTime ? (
                        <FormattedRelativeTime
                          value={detectedRelativeTime.value}
                          unit={detectedRelativeTime.unit}
                          numeric="auto"
                        />
                      ) : (
                        <FormattedMessage
                          id="aardvark.placeholder.missing"
                          defaultMessage="—"
                          description="Dash placeholder indicating missing value"
                        />
                      )}
                    </span>
                  </Table.RowTextLink>
                );
                const fieldValues: Record<FindingsColumnId, ReactNode> = {
                  finding: (
                    <div className="df-findings-title-cell">
                      <Table.RowLink
                        {...findingLinkProps}
                        className={`${workbenchStyles.tableLink} df-findings-title`}
                        aria-label={intl.formatMessage(
                          {
                            id: "codexSecurity.workbench.findings.table.row.open",
                            defaultMessage: "Open finding: {title}",
                            description:
                              "Accessible label for an interactive row in the Codex Security operations findings table. Placeholder {title} is the vulnerability finding's human-readable title.",
                          },
                          { title },
                        )}
                      >
                        <span>{title}</span>
                      </Table.RowLink>
                      <div className="df-findings-row-source">
                        <Table.RowTextLink
                          {...findingLinkProps}
                          className="truncate"
                          title={finding.repo_url}
                        >
                          {repositoryLabel(finding.repo_url)}
                        </Table.RowTextLink>
                        <span aria-hidden>·</span>
                        <FindingSource
                          finding={finding}
                          rowLinkProps={findingLinkProps}
                        />
                        <span aria-hidden>·</span>
                        <Table.RowTextLink {...findingLinkProps}>
                          {intl.formatMessage(
                            findingSourceLabels[finding.scanType],
                          )}
                        </Table.RowTextLink>
                      </div>
                      <div className="df-findings-mobile-metadata">
                        {severityLabel}
                        {statusBadge}
                        {detectedLabel}
                      </div>
                    </div>
                  ),
                  severity: severityLabel,
                  status: statusBadge,
                  detected: detectedLabel,
                };

                return (
                  <Table.Row
                    key={finding.id}
                    className="group df-findings-row"
                  >
                    {renderCells(fieldValues)}
                  </Table.Row>
                );
              })
            )}
          </>
        )}
      </FindingsResultsTable>

      <WorkbenchTableFooter
        summary={
          <FormattedMessage
            id="codexSecurity.workbench.findings.table.pagination.range"
            defaultMessage="{from, number}–{to, number} of {total, number} findings"
            description="Pagination summary below the Codex Security operations findings table. Placeholders {from} and {to} are the first and last one-based row numbers shown, and {total} is the total number of authorized findings matching the current filters. All numbers use the viewer's locale."
            values={{
              from: findings.length > 0 ? cursor + 1 : 0,
              to: Math.min(cursor + findings.length, totalFindings),
              total: totalFindings,
            }}
          />
        }
      >
        <div className="flex flex-wrap items-center gap-2">
          <label
            htmlFor="codex-security-workbench-findings-page-size"
            className="df-findings-page-size-label text-token-text-secondary whitespace-nowrap"
          >
            <FormattedMessage
              id="codexSecurity.workbench.findings.table.pagination.page_size"
              defaultMessage="Rows per page"
              description="Short label beside the page-size selector beneath the Codex Security operations findings table. Controls how many authorized findings the server returns per page."
            />
          </label>
          <Select
            id="codex-security-workbench-findings-page-size"
            triggerClassName="df-control df-findings-page-size"
            listMinWidth={100}
            value={String(limit)}
            onChange={({ value }) => {
              const nextSearchParams = new URLSearchParams(search);
              nextSearchParams.set("limit", value);
              nextSearchParams.delete("cursor");
              nextSearchParams.delete("page");
              updateSearch(nextSearchParams);
            }}
            options={Array.from(ALLOWED_PAGE_SIZES, (pageSize) => ({
              label: intl.formatNumber(pageSize),
              value: String(pageSize),
            }))}
          />
          <Button
            type="button"
            size="toolbar"
            color="outlineSurface"
            disabled={findingsQuery.isFetching || !(hasPrevious ?? cursor > 0)}
            onClick={() => updateCursor(cursor - limit)}
          >
            {previousIsFirst ? (
              <FormattedMessage
                id="codexSecurity.workbench.findings.table.pagination.first"
                defaultMessage="First page"
                description="Button beneath the Security Findings table when the user opens a link to a later results page without previous-page history. Returns to the first page while preserving the current search and filters."
              />
            ) : (
              <FormattedMessage
                id="codexSecurity.workbench.findings.table.pagination.previous"
                defaultMessage="Previous"
                description="Button beneath the Codex Security operations findings table that loads the preceding server-backed page of vulnerability findings. Disabled on the first page."
              />
            )}
          </Button>
          <Button
            type="button"
            size="toolbar"
            color="outlineSurface"
            disabled={
              findingsQuery.isFetching ||
              !(hasNext ?? cursor + findings.length < totalFindings)
            }
            onClick={() => updateCursor(cursor + limit)}
          >
            <FormattedMessage
              id="codexSecurity.workbench.findings.table.pagination.next"
              defaultMessage="Next"
              description="Button beneath the Codex Security operations findings table that loads the next server-backed page of vulnerability findings. Disabled when no later page exists."
            />
          </Button>
        </div>
      </WorkbenchTableFooter>
    </div>
  );
}
