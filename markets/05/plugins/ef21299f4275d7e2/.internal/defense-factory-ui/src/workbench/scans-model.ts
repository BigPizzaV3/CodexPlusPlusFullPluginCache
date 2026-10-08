import type { components } from "@oai/aardvark-client/components";
import type { IntlShape, MessageDescriptor } from "react-intl";

import type { WorkbenchStatusBadgeVariant } from "./layout";
import { scanTypeLabels, type ScanType } from "./scan-types";
import { scanMessages as messages } from "./scans-messages";

export type WorkflowRun =
  | components["schemas"]["WorkflowRunListItem"]
  | components["schemas"]["WorkflowRunResponse"];
export type CommitScanRun = components["schemas"]["AardvarkScanListItem"];

type WorkbenchScanBase = {
  id: string;
  scanType: ScanType;
  repositoryId: string;
  repositoryName: string;
  repositoryUrl: string;
  environmentLabel?: string | null;
  isEnvironmentLoading?: boolean;
};

export type WorkbenchScan = WorkbenchScanBase &
  (
    | { workflow: WorkflowRun; commitScan?: never }
    | { workflow?: never; commitScan: CommitScanRun }
  );

export type ScanStatusFilter =
  | "all"
  | "active"
  | "finished"
  | "failed"
  | "canceled";
export type ScanSortField = "source" | "started";
export type ScanTypeFilter = "all" | ScanType;

const STATUS_PRESENTATIONS = {
  created: { variant: "neutral", message: messages.queued },
  in_progress: { variant: "purple", message: messages.running },
  cancelled: { variant: "muted", message: messages.canceled },
  finished: { variant: "success", message: messages.completed },
  queued: { variant: "neutral", message: messages.queued },
  preparing: { variant: "info", message: messages.preparing },
  running: { variant: "purple", message: messages.running },
  validating_output: {
    variant: "purple",
    message: messages.validatingOutput,
  },
  cancel_requested: {
    variant: "neutral",
    message: messages.cancelRequested,
  },
  completed: { variant: "success", message: messages.completed },
  failed: { variant: "danger", message: messages.failed },
  canceled: { variant: "muted", message: messages.canceled },
} satisfies Record<
  WorkflowRun["status"] | CommitScanRun["status"],
  { variant: WorkbenchStatusBadgeVariant; message: MessageDescriptor }
>;

export function getScanStatus(scan: WorkbenchScan) {
  return scan.workflow ? scan.workflow.status : scan.commitScan.status;
}

export function getScanStatusPresentation(
  status: WorkflowRun["status"] | CommitScanRun["status"],
) {
  return STATUS_PRESENTATIONS[status] ?? STATUS_PRESENTATIONS.queued;
}

export function getScanStartedAt(scan: WorkbenchScan): string {
  return scan.workflow
    ? scan.workflow.running_at ?? scan.workflow.created_at
    : scan.commitScan.started_at;
}

export function getScanFinishedAt(scan: WorkbenchScan): string | null {
  return scan.workflow
    ? scan.workflow.completed_at ??
        scan.workflow.failed_at ??
        scan.workflow.canceled_at ??
        null
    : scan.commitScan.finished_at ?? null;
}

export function getScanCommitHash(scan: WorkbenchScan): string | null {
  return scan.workflow
    ? scan.workflow.target_commit_sha
    : scan.commitScan.scan_input.commit_hash ?? null;
}

export function getScanBranch(scan: WorkbenchScan): string | null {
  return scan.commitScan?.scan_input.branch_name ?? null;
}

export function getScanTriggerMessage(scan: WorkbenchScan) {
  if (scan.workflow) {
    return scan.workflow.trigger === "schedule"
      ? messages.scheduled
      : messages.onDemand;
  }
  return scan.commitScan.trigger === "new_commit"
    ? messages.newCommit
    : messages.onDemand;
}

export function formatDateTime(intl: IntlShape, value: string): string {
  const timestamp = new Date(value);
  return Number.isNaN(timestamp.getTime())
    ? value
    : intl.formatDate(timestamp, { dateStyle: "medium", timeStyle: "short" });
}

export function formatDuration(intl: IntlShape, scan: WorkbenchScan): string {
  const finishedAt = getScanFinishedAt(scan);
  if (!finishedAt) return "—";
  const elapsedSeconds = Math.max(
    0,
    Math.round(
      (new Date(finishedAt).getTime() -
        new Date(getScanStartedAt(scan)).getTime()) /
        1000,
    ),
  );
  if (!Number.isFinite(elapsedSeconds)) return "—";
  if (elapsedSeconds < 60) {
    return intl.formatMessage(
      {
        id: "codexSecurity.workbench.scans.duration.seconds",
        defaultMessage: "{count, number}s",
        description: "Elapsed scan duration expressed in seconds.",
      },
      { count: elapsedSeconds },
    );
  }
  if (elapsedSeconds >= 86_400) {
    const roundedHours = Math.round(elapsedSeconds / 3_600);
    return intl.formatMessage(
      {
        id: "codexSecurity.workbench.scans.duration.daysHours",
        defaultMessage: "{days, number}d {hours, number}h",
        description: "Elapsed scan duration expressed in days and hours.",
      },
      { days: Math.floor(roundedHours / 24), hours: roundedHours % 24 },
    );
  }
  if (elapsedSeconds >= 3_600) {
    const roundedMinutes = Math.round(elapsedSeconds / 60);
    return intl.formatMessage(
      {
        id: "codexSecurity.workbench.scans.duration.hoursMinutes",
        defaultMessage: "{hours, number}h {minutes, number}m",
        description: "Elapsed scan duration expressed in hours and minutes.",
      },
      {
        hours: Math.floor(roundedMinutes / 60),
        minutes: roundedMinutes % 60,
      },
    );
  }
  return intl.formatMessage(
    {
      id: "codexSecurity.workbench.scans.duration.minutes",
      defaultMessage: "{count, number}m",
      description: "Elapsed scan duration expressed in minutes.",
    },
    { count: Math.round(elapsedSeconds / 60) },
  );
}

function matchesStatus(scan: WorkbenchScan, filter: ScanStatusFilter): boolean {
  const status = getScanStatus(scan);
  if (filter === "all") return true;
  if (filter === "active") {
    return (
      status === "created" ||
      status === "in_progress" ||
      status === "queued" ||
      status === "preparing" ||
      status === "running" ||
      status === "validating_output" ||
      status === "cancel_requested"
    );
  }
  if (filter === "finished") {
    return status === "completed" || status === "finished";
  }
  if (filter === "failed") return status === "failed";
  return status === "canceled" || status === "cancelled";
}

export function filterAndSortWorkbenchScans({
  scans,
  searchQuery,
  statusFilter,
  scanTypeFilter,
  sortField,
  sortDescending,
  intl,
}: {
  scans: readonly WorkbenchScan[];
  searchQuery: string;
  statusFilter: ScanStatusFilter;
  scanTypeFilter: ScanTypeFilter;
  sortField: ScanSortField;
  sortDescending: boolean;
  intl: IntlShape;
}): WorkbenchScan[] {
  const normalizedSearch = searchQuery.trim().toLocaleLowerCase();
  return scans
    .filter(
      (scan) =>
        matchesStatus(scan, statusFilter) &&
        (scanTypeFilter === "all" || scan.scanType === scanTypeFilter) &&
        (normalizedSearch === "" ||
          [
            scan.id,
            scan.environmentLabel,
            scan.repositoryId,
            scan.repositoryName,
            scan.repositoryUrl,
            getScanCommitHash(scan),
            getScanBranch(scan),
            scan.commitScan?.triggered_by,
            intl.formatMessage(scanTypeLabels[scan.scanType]),
            intl.formatMessage(
              getScanStatusPresentation(getScanStatus(scan)).message,
            ),
            intl.formatMessage(getScanTriggerMessage(scan)),
          ].some(
            (value) => value?.toLocaleLowerCase().includes(normalizedSearch),
          )),
    )
    .sort((first, second) => {
      const comparison =
        sortField === "source"
          ? (first.environmentLabel ?? "").localeCompare(
              second.environmentLabel ?? "",
            ) ||
            (getScanCommitHash(first) ?? "").localeCompare(
              getScanCommitHash(second) ?? "",
            )
          : getScanStartedAt(first).localeCompare(getScanStartedAt(second));
      return sortDescending ? -comparison : comparison;
    });
}

export function formatShortRunId(id: string): string {
  return id.slice(-8);
}
