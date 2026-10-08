import {
  defineMessages,
  type IntlShape,
  type MessageDescriptor,
} from "react-intl";

const messages: Record<string, MessageDescriptor> = defineMessages({
  critical: {
    id: "defenseFactory.plugin.value.critical",
    defaultMessage: "Critical",
    description: "Security severity, finding, or scan status: Critical",
  },
  high: {
    id: "defenseFactory.plugin.value.high",
    defaultMessage: "High",
    description: "Security severity, finding, or scan status: High",
  },
  medium: {
    id: "defenseFactory.plugin.value.medium",
    defaultMessage: "Medium",
    description: "Security severity, finding, or scan status: Medium",
  },
  low: {
    id: "defenseFactory.plugin.value.low",
    defaultMessage: "Low",
    description: "Security severity, finding, or scan status: Low",
  },
  informational: {
    id: "defenseFactory.plugin.value.informational",
    defaultMessage: "Informational",
    description: "Security severity, finding, or scan status: Informational",
  },
  new: {
    id: "defenseFactory.plugin.value.new",
    defaultMessage: "New",
    description: "Security severity, finding, or scan status: New",
  },
  triaged: {
    id: "defenseFactory.plugin.value.triaged",
    defaultMessage: "Triaged",
    description: "Security severity, finding, or scan status: Triaged",
  },
  in_progress: {
    id: "defenseFactory.plugin.value.in_progress",
    defaultMessage: "In progress",
    description: "Security severity, finding, or scan status: In progress",
  },
  fixed: {
    id: "defenseFactory.plugin.value.fixed",
    defaultMessage: "Fixed",
    description: "Security severity, finding, or scan status: Fixed",
  },
  wontfix: {
    id: "defenseFactory.plugin.value.wontfix",
    defaultMessage: "Won’t fix",
    description: "Security severity, finding, or scan status: Won’t fix",
  },
  duplicate: {
    id: "defenseFactory.plugin.value.duplicate",
    defaultMessage: "Duplicate",
    description: "Security severity, finding, or scan status: Duplicate",
  },
  false_positive: {
    id: "defenseFactory.plugin.value.false_positive",
    defaultMessage: "False positive",
    description: "Security severity, finding, or scan status: False positive",
  },
  queued: {
    id: "defenseFactory.plugin.value.queued",
    defaultMessage: "Queued",
    description: "Security severity, finding, or scan status: Queued",
  },
  preparing: {
    id: "defenseFactory.plugin.value.preparing",
    defaultMessage: "Preparing",
    description: "Security severity, finding, or scan status: Preparing",
  },
  running: {
    id: "defenseFactory.plugin.value.running",
    defaultMessage: "Running",
    description: "Security severity, finding, or scan status: Running",
  },
  validating_output: {
    id: "defenseFactory.plugin.value.validating_output",
    defaultMessage: "Validating output",
    description:
      "Security severity, finding, or scan status: Validating output",
  },
  completed: {
    id: "defenseFactory.plugin.value.completed",
    defaultMessage: "Completed",
    description: "Security severity, finding, or scan status: Completed",
  },
  failed: {
    id: "defenseFactory.plugin.value.failed",
    defaultMessage: "Failed",
    description: "Security severity, finding, or scan status: Failed",
  },
  canceled: {
    id: "defenseFactory.plugin.value.canceled",
    defaultMessage: "Canceled",
    description: "Security severity, finding, or scan status: Canceled",
  },
  cancelled: {
    id: "defenseFactory.plugin.value.cancelled",
    defaultMessage: "Canceled",
    description: "Security severity, finding, or scan status: Canceled",
  },
  cancel_requested: {
    id: "defenseFactory.plugin.value.cancel_requested",
    defaultMessage: "Cancel requested",
    description: "Security severity, finding, or scan status: Cancel requested",
  },
  started: {
    id: "defenseFactory.plugin.value.started",
    defaultMessage: "Started",
    description: "Security severity, finding, or scan status: Started",
  },
  finished: {
    id: "defenseFactory.plugin.value.finished",
    defaultMessage: "Finished",
    description: "Security severity, finding, or scan status: Finished",
  },
  manual: {
    id: "defenseFactory.plugin.value.manual",
    defaultMessage: "Manual",
    description: "Security severity, finding, or scan status: Manual",
  },
  automatic: {
    id: "defenseFactory.plugin.value.automatic",
    defaultMessage: "Automatic",
    description: "Security severity, finding, or scan status: Automatic",
  },
  scheduled: {
    id: "defenseFactory.plugin.value.scheduled",
    defaultMessage: "Scheduled",
    description: "Security severity, finding, or scan status: Scheduled",
  },
  continuous_scan: {
    id: "defenseFactory.plugin.value.continuous_scan",
    defaultMessage: "Continuous scan",
    description: "Security severity, finding, or scan status: Continuous scan",
  },
  pending: {
    id: "defenseFactory.plugin.value.pending",
    defaultMessage: "Pending",
    description: "Security severity, finding, or scan status: Pending",
  },
  succeeded: {
    id: "defenseFactory.plugin.value.succeeded",
    defaultMessage: "Succeeded",
    description: "Security severity, finding, or scan status: Succeeded",
  },
});

export function statusLabel(intl: IntlShape, value: string) {
  return messages[value]
    ? intl.formatMessage(messages[value])
    : value.replaceAll("_", " ");
}
