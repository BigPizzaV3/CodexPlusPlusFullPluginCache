import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation, useParams } from "react-router";

import { WorkbenchButton as Button } from "./controls";
import { WorkbenchState, WorkbenchTableFooter } from "./layout";
import { WorkbenchResponsiveTable } from "./responsive-table";
import { WorkbenchScanTypeBadge } from "./scan-type-badge";
import {
  WorkbenchScanCommitBadge,
  WorkbenchScanDurationBadge,
  WorkbenchScanInitiatorBadge,
  WorkbenchScanRepositoryBadge,
  WorkbenchScanStartedBadge,
  WorkbenchScanStatusBadge,
} from "./scans-metadata";
import { scanMessages as messages } from "./scans-messages";
import {
  formatShortRunId,
  type ScanSortField,
  type WorkbenchScan,
} from "./scans-model";
import { WorkbenchSource } from "./source";
import { workbenchStyles } from "./styles";
import Table from "./table";

const scanFields = [
  {
    id: "source",
    label: messages.source,
    sort: "source",
    sortLabel: messages.sortSource,
    headerClassName: "px-4 py-3",
    cellClassName: "flex min-h-[60px] min-w-0 items-center py-1.5",
  },
  {
    id: "status",
    label: messages.status,
    sort: null,
    headerClassName: "px-4 py-3",
    cellClassName: "flex h-[60px] items-center",
  },
  {
    id: "started",
    label: messages.started,
    sort: "started",
    sortLabel: messages.sortStarted,
    headerClassName: "px-4 py-3",
    cellClassName: "flex h-[60px] items-center",
  },
  {
    id: "duration",
    label: messages.duration,
    sort: null,
    headerClassName: "px-4 py-3",
    cellClassName: "flex h-[60px] items-center",
  },
  {
    id: "initiatedBy",
    label: messages.initiatedBy,
    sort: null,
    headerClassName: "px-4 py-3",
    cellClassName: "flex h-[60px] items-center",
  },
] as const;

export function WorkbenchScansTable({
  scans,
  emptyState,
  sort,
  onSort,
  retryAction,
  pagination,
}: {
  scans: readonly WorkbenchScan[];
  emptyState: "loading" | "unavailable" | "filtered" | "unfiltered" | null;
  sort: { field: ScanSortField; descending: boolean };
  onSort: (field: ScanSortField) => void;
  retryAction?: ReactNode;
  pagination: {
    busy: boolean;
    canGoPrevious: boolean;
    canGoNext: boolean;
    onPrevious: () => void;
    onNext: () => void;
  };
}) {
  const intl = useIntl();
  const location = useLocation();
  const { repositoryId } = useParams();
  return (
    <div className={workbenchStyles.table}>
      <WorkbenchResponsiveTable
        fields={scanFields}
        activeSortField={sort.field}
        sortDirection={sort.descending ? "desc" : "asc"}
        onSort={onSort}
      >
        {({ columnCount, renderCells }) => (
          <>
            {emptyState === "loading" ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState variant="table" loading>
                    <FormattedMessage
                      id="codexSecurity.workbench.scans.loading"
                      defaultMessage="Loading scan history…"
                      description="Loading message inside the Security scan-history table."
                    />
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : emptyState === "unavailable" ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState variant="table" action={retryAction}>
                    <FormattedMessage
                      id="codexSecurity.workbench.scans.error"
                      defaultMessage="Scan history could not be loaded."
                      description="Sanitized error shown when authorized scan history cannot be retrieved."
                    />
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : scans.length === 0 ? (
              <Table.Row>
                <Table.Cell colSpan={columnCount} divClassName="w-full">
                  <WorkbenchState variant="table">
                    {emptyState === "filtered" ? (
                      <FormattedMessage
                        id="codexSecurity.workbench.scans.empty.pageFiltered"
                        defaultMessage="No scans on this page match your current filters."
                        description="Empty state when the current scan-history page has no rows matching client-side filters."
                      />
                    ) : (
                      <FormattedMessage
                        id="codexSecurity.workbench.scans.empty.unfiltered"
                        defaultMessage="No scans to show."
                        description="Neutral empty state for an authorized scan-history page without rows."
                      />
                    )}
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : (
              scans.map((scan) => {
                const detailPath = repositoryId
                  ? `/repositories/${encodeURIComponent(
                      repositoryId,
                    )}/scans/${encodeURIComponent(scan.id)}`
                  : `/runs/${encodeURIComponent(scan.id)}`;
                const detailSearch = new URLSearchParams(location.search);
                detailSearch.delete("cursor");
                detailSearch.delete("commit_cursor");
                detailSearch.delete("workflow_exhausted");
                detailSearch.delete("commit_exhausted");
                if (scan.commitScan) {
                  detailSearch.set(
                    "scan_configuration_id",
                    scan.commitScan.scan_configuration_id,
                  );
                  detailSearch.set("repo_id", scan.repositoryId);
                  if (scan.repositoryUrl) {
                    detailSearch.set("repo", scan.repositoryUrl);
                  } else {
                    detailSearch.delete("repo");
                  }
                }
                const scanLinkProps = {
                  to: {
                    pathname: detailPath,
                    search: detailSearch.toString(),
                    hash: location.hash,
                  },
                  state: location.state,
                };
                return (
                  <Table.Row
                    key={scan.id}
                    className={`group/scan ${workbenchStyles.tableRow} text-[14px] leading-5 transition-colors`}
                  >
                    {renderCells({
                      source: (
                        <div className="w-full min-w-0 space-y-0.5 lg:max-w-lg">
                          <div className="text-token-text-secondary flex min-w-0 items-center bg-transparent py-0 font-normal">
                            <WorkbenchSource
                              environmentLabel={scan.environmentLabel}
                              repositoryId={scan.repositoryId}
                              repositoryUrl={scan.repositoryUrl}
                              variant="breadcrumb"
                              isLoading={scan.isEnvironmentLoading}
                            />
                            <span
                              aria-hidden
                              className="text-token-text-tertiary shrink-0 px-1 text-[12px]"
                            >
                              /
                            </span>
                            <Table.RowLink
                              {...scanLinkProps}
                              className="shrink-0 underline-offset-2 hover:underline"
                              title={scan.id}
                              aria-label={intl.formatMessage(
                                {
                                  id: "codexSecurity.workbench.scans.row.open",
                                  defaultMessage: "Open scan {id}",
                                  description:
                                    "Accessible label for an interactive Security scan-history row.",
                                },
                                { id: formatShortRunId(scan.id) },
                              )}
                            >
                              <span>{formatShortRunId(scan.id)}</span>
                            </Table.RowLink>
                          </div>
                          <div className="flex min-w-0 flex-wrap items-center gap-2">
                            <Table.RowTextLink {...scanLinkProps}>
                              <WorkbenchScanTypeBadge scanType={scan.scanType} />
                            </Table.RowTextLink>
                            <div className="max-w-full min-w-0 lg:max-w-72">
                              <WorkbenchScanRepositoryBadge
                                scan={scan}
                                rowLinkProps={scanLinkProps}
                              />
                            </div>
                            <WorkbenchScanCommitBadge
                              scan={scan}
                              rowLinkProps={scanLinkProps}
                            />
                          </div>
                        </div>
                      ),
                      status: (
                        <Table.RowTextLink {...scanLinkProps}>
                          <WorkbenchScanStatusBadge scan={scan} />
                        </Table.RowTextLink>
                      ),
                      started: (
                        <Table.RowTextLink {...scanLinkProps}>
                          <WorkbenchScanStartedBadge scan={scan} />
                        </Table.RowTextLink>
                      ),
                      duration: (
                        <Table.RowTextLink {...scanLinkProps}>
                          <WorkbenchScanDurationBadge scan={scan} />
                        </Table.RowTextLink>
                      ),
                      initiatedBy: (
                        <Table.RowTextLink {...scanLinkProps}>
                          <WorkbenchScanInitiatorBadge scan={scan} />
                        </Table.RowTextLink>
                      ),
                    })}
                  </Table.Row>
                );
              })
            )}
          </>
        )}
      </WorkbenchResponsiveTable>
      <WorkbenchTableFooter
        summary={
          <span aria-live="polite">
            {scans.length > 0 ||
            emptyState === "filtered" ||
            emptyState === "unfiltered" ? (
              <FormattedMessage
                id="codexSecurity.workbench.scans.resultCount"
                defaultMessage="{count, plural, one {# scan} other {# scans}}"
                description="Count of scan rows visible on the current authorized history page."
                values={{ count: scans.length }}
              />
            ) : null}
          </span>
        }
      >
        <Button
          type="button"
          color="outlineSurface"
          disabled={pagination.busy || !pagination.canGoPrevious}
          onClick={pagination.onPrevious}
        >
          {intl.formatMessage(messages.previous)}
        </Button>
        <Button
          type="button"
          color="outlineSurface"
          disabled={pagination.busy || !pagination.canGoNext}
          onClick={pagination.onNext}
        >
          {intl.formatMessage(messages.next)}
        </Button>
      </WorkbenchTableFooter>
    </div>
  );
}
