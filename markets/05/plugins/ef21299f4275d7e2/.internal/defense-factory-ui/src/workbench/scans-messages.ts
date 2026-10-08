import { defineMessages } from "react-intl";

export const scanMessages = defineMessages({
  filterScans: {
    id: "codexSecurity.workbench.scans.filters.label",
    defaultMessage: "Filter scans",
    description:
      "Accessible button label and panel heading for repository, scan type, and scan status filters above the Security scans table.",
  },
  activeFiltersLabel: {
    id: "codexSecurity.workbench.scans.filters.active_aria",
    defaultMessage:
      "Filter scans, {count, plural, one {# active filter} other {# active filters}}",
    description:
      "Accessible label for the scan filters button, including the number of non-default filters.",
  },
  clearFilters: {
    id: "codexSecurity.workbench.scans.filters.clear.label",
    defaultMessage: "Clear filters",
    description:
      "Action that resets repository, scan type, and status filters and returns to the first scan-history page.",
  },
  searchScans: {
    id: "codexSecurity.workbench.scans.search",
    defaultMessage: "Search scans",
    description:
      "Accessible label and placeholder for searching the current authorized scan-history page.",
  },
  retryHistory: {
    id: "codexSecurity.workbench.scans.error.retry",
    defaultMessage: "Retry",
    description:
      "Short recovery action that retries loading the current authorized scan-history page.",
  },
  repositoryFilter: {
    id: "codexSecurity.workbench.scans.repositoryFilter",
    defaultMessage: "Repository",
    description: "Label for the repository filter in Security scan history.",
  },
  allRepositories: {
    id: "codexSecurity.workbench.scans.allRepositories",
    defaultMessage: "All repositories",
    description:
      "Repository filter option that shows authorized scan history across repositories.",
  },
  statusFilter: {
    id: "codexSecurity.workbench.scans.statusFilter",
    defaultMessage: "Scan status",
    description: "Label for the execution status filter in scan history.",
  },
  allStatuses: {
    id: "codexSecurity.workbench.scans.allStatuses",
    defaultMessage: "All statuses",
    description: "Status filter option that includes every scan status.",
  },
  active: {
    id: "codexSecurity.workbench.scans.active",
    defaultMessage: "Active",
    description: "Status filter option for queued and running scans.",
  },
  queued: {
    id: "codexSecurity.workbench.scans.status.queued",
    defaultMessage: "Queued",
    description: "Execution status for a scan that has not started yet.",
  },
  running: {
    id: "codexSecurity.workbench.scans.status.running",
    defaultMessage: "Running",
    description: "Execution status for a scan that is running.",
  },
  preparing: {
    id: "codexSecurity.workbench.scans.status.preparing",
    defaultMessage: "Preparing",
    description:
      "Execution status for a scan preparing its approved environment.",
  },
  validatingOutput: {
    id: "codexSecurity.workbench.scans.status.validatingOutput",
    defaultMessage: "Validating output",
    description: "Execution status for a scan whose report is being validated.",
  },
  cancelRequested: {
    id: "codexSecurity.workbench.scans.status.cancelRequested",
    defaultMessage: "Cancel requested",
    description:
      "Execution status for a scan whose owner requested cancellation.",
  },
  completed: {
    id: "codexSecurity.workbench.scans.status.completed",
    defaultMessage: "Completed",
    description: "Execution status for a completed scan.",
  },
  failed: {
    id: "codexSecurity.workbench.scans.status.failed",
    defaultMessage: "Failed",
    description: "Execution status for an unsuccessful scan.",
  },
  canceled: {
    id: "codexSecurity.workbench.scans.status.canceled",
    defaultMessage: "Canceled",
    description: "Execution status for a canceled scan.",
  },
  source: {
    id: "codexSecurity.workbench.scans.column.source",
    defaultMessage: "Source",
    description:
      "Column containing the environment, run identifier, repository, and revision for a Security scan.",
  },
  sortSource: {
    id: "codexSecurity.workbench.scans.sortSource",
    defaultMessage: "Sort by source",
    description:
      "Accessible action for sorting the current scan-history page by environment and revision.",
  },
  status: {
    id: "codexSecurity.workbench.scans.column.status",
    defaultMessage: "Status",
    description: "Column containing the current scan execution status.",
  },
  started: {
    id: "codexSecurity.workbench.scans.column.started",
    defaultMessage: "Started",
    description: "Column containing the start time of a scan.",
  },
  sortStarted: {
    id: "codexSecurity.workbench.scans.sortStarted",
    defaultMessage: "Sort by start time",
    description:
      "Accessible action for sorting the current scan-history page by start time.",
  },
  duration: {
    id: "codexSecurity.workbench.scans.column.duration",
    defaultMessage: "Duration",
    description: "Column containing the elapsed scan duration.",
  },
  initiatedBy: {
    id: "codexSecurity.workbench.scans.detail.initiatedBy",
    defaultMessage: "Initiated by",
    description: "Metadata label for the person who initiated a scan.",
  },
  repository: {
    id: "codexSecurity.workbench.scans.column.repository",
    defaultMessage: "Repository",
    description: "Metadata label for a scan's repository.",
  },
  commit: {
    id: "codexSecurity.workbench.scans.column.commit",
    defaultMessage: "Commit",
    description: "Metadata label for the revision reviewed by a scan.",
  },
  previous: {
    id: "codexSecurity.workbench.scans.previous",
    defaultMessage: "Previous",
    description: "Button that loads the previous scan-history page.",
  },
  next: {
    id: "codexSecurity.workbench.scans.next",
    defaultMessage: "Next",
    description: "Button that loads the next scan-history page.",
  },
  onDemand: {
    id: "codexSecurity.workbench.scans.trigger.manual",
    defaultMessage: "On demand",
    description: "Label for a scan started manually by a user.",
  },
  newCommit: {
    id: "codexSecurity.workbench.scans.trigger.newCommit",
    defaultMessage: "New commit",
    description: "Label for a commit scan started by a newly observed commit.",
  },
  scheduled: {
    id: "codexSecurity.workbench.scans.trigger.schedule",
    defaultMessage: "Scheduled",
    description: "Label for a scan started by a schedule.",
  },
});
