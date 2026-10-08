import { useQuery } from "@tanstack/react-query";
import { FormattedMessage, useIntl } from "react-intl";

import { useCloud } from "../app-context";
import { securityClient } from "../client";
import { statusLabel } from "../labels";
import { DateTime } from "../ui";
import { WorkbenchButton as Button, WorkbenchLink } from "./controls";
import {
  WorkbenchState,
  WorkbenchStatusBadge,
  type WorkbenchStatusBadgeVariant,
} from "./layout";
import { workbenchStyles } from "./styles";

const ACTIVE_STATUSES = new Set([
  "created",
  "in_progress",
  "queued",
  "preparing",
  "running",
  "validating_output",
  "cancel_requested",
]);

type RepositoryScan = {
  kind: "commit" | "repository";
  status: string;
  startedAt: string;
  href: string;
};

function statusVariant(status: string): WorkbenchStatusBadgeVariant {
  if (status === "completed" || status === "finished") return "success";
  if (status === "failed") return "danger";
  if (ACTIVE_STATUSES.has(status)) return "info";
  return "neutral";
}

export function RepositoryScanActivity({
  configurationId,
  configurationRecordIds = [],
  repoConnectorId,
  repoId,
  repoUrl,
}: {
  configurationId?: string;
  configurationRecordIds?: string[];
  repoConnectorId?: string | null;
  repoId: string;
  repoUrl: string;
}) {
  const intl = useIntl();
  const cloud = useCloud();
  const queryScope = [
    cloud.accountId,
    cloud.identity?.userId ?? "none",
    repoConnectorId ?? "none",
    repoId,
  ];
  const workflowQuery = useQuery({
    queryKey: ["repository-workflow-activity", ...queryScope],
    queryFn: () =>
      securityClient.request({
        operation: "workflow_list",
        parameters: {
          query: { repo_id: repoId, limit: 10, include_ownership: true },
        },
      }),
    staleTime: 15_000,
  });
  const commitQuery = useQuery({
    queryKey: ["repository-commit-activity", ...queryScope, configurationId],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_scans",
        parameters: {
          path: { id: configurationId ?? "" },
          query: { limit: 10 },
        },
      }),
    enabled: Boolean(configurationId),
    staleTime: 15_000,
  });

  // The plugin bridge does not expose an HTTP status with tool errors. Hide a
  // source's cached page after any failed refresh so revoked access cannot
  // leave repository or scan metadata visible.
  const workflowPage = workflowQuery.error ? undefined : workflowQuery.data;
  const commitPage = commitQuery.error ? undefined : commitQuery.data;
  const scans: RepositoryScan[] = [];
  const historyQuery = new URLSearchParams({ repo_id: repoId, repo: repoUrl });
  if (configurationId) {
    historyQuery.set("scan_configuration_id", configurationId);
  }
  for (const run of workflowPage?.items ?? []) {
    if (
      !/^wfr_[0-9a-f]{64}$/.test(run.run_id) ||
      run.repo_id !== repoId ||
      (repoConnectorId != null
        ? (run.repo_connector_id ?? null) !== repoConnectorId
        : run.repo_connector_id
        ? !repoId.startsWith(`github-${run.repo_connector_id}:`)
        : repoId.includes(":"))
    ) {
      continue;
    }
    scans.push({
      kind: "repository",
      status: run.status,
      startedAt: run.created_at,
      href: `/repositories/${encodeURIComponent(
        repoId,
      )}/scans/${encodeURIComponent(run.run_id)}?${historyQuery}`,
    });
  }
  for (const scan of commitPage?.items ?? []) {
    if (
      !configurationId ||
      !configurationRecordIds.includes(scan.scan_configuration_id) ||
      scan.scan_input.repo_id !== repoId ||
      (scan.scan_input.repo_connector_id ?? null) !== (repoConnectorId ?? null)
    ) {
      continue;
    }
    scans.push({
      kind: "commit",
      status:
        scan.status === "finished"
          ? scan.success === true
            ? "completed"
            : scan.success === false
            ? "failed"
            : "result_unknown"
          : scan.status,
      startedAt: scan.started_at,
      href: `/runs/${encodeURIComponent(scan.id)}?${historyQuery}`,
    });
  }
  scans.sort(
    (left, right) => Date.parse(right.startedAt) - Date.parse(left.startedAt),
  );
  const active = scans.find((scan) => ACTIVE_STATUSES.has(scan.status));
  const displayed = active ?? scans[0];
  const isLoading =
    (!workflowQuery.data && workflowQuery.isPending) ||
    (Boolean(configurationId) && !commitQuery.data && commitQuery.isPending);
  const hasError =
    workflowQuery.isError || (Boolean(configurationId) && commitQuery.isError);
  const retry = () => {
    if (workflowQuery.isError) void workflowQuery.refetch();
    if (configurationId && commitQuery.isError) void commitQuery.refetch();
  };

  return (
    <section className={`${workbenchStyles.card} space-y-5 p-6`}>
      <div className="flex flex-wrap items-center justify-between gap-3">
        <h2 className={workbenchStyles.sectionTitle}>
          <FormattedMessage
            id="codexSecurity.workbench.repositories.scanActivity.heading"
            defaultMessage="Scan activity"
            description="Section heading on a repository overview for the current user's visible repository and commit scans."
          />
        </h2>
        <WorkbenchLink
          color="outlineSurface"
          to={`/repositories/${encodeURIComponent(repoId)}/scans?${historyQuery}`}
        >
          <FormattedMessage
            id="codexSecurity.workbench.repositories.scanActivity.viewHistory"
            defaultMessage="View scan history"
            description="Repository overview action that opens scan history scoped to the current repository."
          />
        </WorkbenchLink>
      </div>
      {displayed ? (
        <>
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="space-y-2">
              <div className={workbenchStyles.metadataLabel}>
                {active ? (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.scanActivity.active"
                    defaultMessage="Active scan"
                    description="Label above the current active scan status."
                  />
                ) : (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.scanActivity.latestVisible"
                    defaultMessage="Latest visible scan"
                    description="Label above the newest scan available to the current user."
                  />
                )}
              </div>
              <WorkbenchStatusBadge variant={statusVariant(displayed.status)}>
                {displayed.status === "result_unknown" ? (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.scanActivity.resultUnknown"
                    defaultMessage="Finished, result unknown"
                    description="A finished legacy commit scan has no recorded success result."
                  />
                ) : (
                  statusLabel(intl, displayed.status)
                )}
              </WorkbenchStatusBadge>
            </div>
            <WorkbenchLink
              color="outlineSurface"
              to={displayed.href}
            >
              <FormattedMessage
                id="codexSecurity.workbench.repositories.scanActivity.viewScan"
                defaultMessage="View scan"
                description="Open the visible scan summarized on a repository overview."
              />
            </WorkbenchLink>
          </div>
          <dl className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-1">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.scanActivity.started"
                  defaultMessage="Started"
                  description="Start timestamp for the visible repository scan."
                />
              </dt>
              <dd className={workbenchStyles.metadataValue}>
                <DateTime value={displayed.startedAt} />
              </dd>
            </div>
            <div className="space-y-1">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.scanActivity.type"
                  defaultMessage="Scan type"
                  description="Type of scan summarized on a repository overview."
                />
              </dt>
              <dd className={workbenchStyles.metadataValue}>
                {displayed.kind === "commit" ? (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.scanActivity.commit"
                    defaultMessage="Commit scan"
                    description="Continuous monitoring scan of a repository commit."
                  />
                ) : (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.scanActivity.repository"
                    defaultMessage="Full repository scan"
                    description="On-demand or scheduled full repository scan."
                  />
                )}
              </dd>
            </div>
          </dl>
          {hasError ? (
            <WorkbenchState
              variant="inline"
              action={
                <Button color="outlineSurface" onClick={retry}>
                  Retry
                </Button>
              }
            >
              <FormattedMessage
                id="codexSecurity.workbench.repositories.scanActivity.partial"
                defaultMessage="Some scan history could not be loaded."
                description="Privacy-preserving notice when one repository scan source is unavailable."
              />
            </WorkbenchState>
          ) : null}
        </>
      ) : isLoading ? (
        <WorkbenchState loading variant="inline" />
      ) : hasError ? (
        <WorkbenchState
          variant="inline"
          action={
            <Button color="outlineSurface" onClick={retry}>
              <FormattedMessage
                id="codexSecurity.workbench.repositories.scanActivity.retry"
                defaultMessage="Retry"
                description="Retry loading repository scan activity."
              />
            </Button>
          }
        >
          <FormattedMessage
            id="codexSecurity.workbench.repositories.scanActivity.unavailable"
            defaultMessage="Scan activity could not be loaded."
            description="Privacy-preserving error shown when repository scan activity is unavailable."
          />
        </WorkbenchState>
      ) : (
        <p className={workbenchStyles.description}>
          <FormattedMessage
            id="codexSecurity.workbench.repositories.scanActivity.empty"
            defaultMessage="No scans are visible for this repository yet."
            description="Empty state for repository scan activity."
          />
        </p>
      )}
    </section>
  );
}
