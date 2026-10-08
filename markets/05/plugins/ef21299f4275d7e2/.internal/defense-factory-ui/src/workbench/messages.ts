import type { FindingCriticality, FindingStatus } from "./types";
import type { MessageDescriptor } from "react-intl";

export const STATUS_MESSAGES: Record<FindingStatus, MessageDescriptor> = {
  new: {
    id: "aardvark.status.new",
    defaultMessage: "New",
    description: "New status",
  },
  triaged: {
    id: "aardvark.status.triaged",
    defaultMessage: "Triaged",
    description: "Triaged status",
  },
  in_progress: {
    id: "aardvark.status.inProgress",
    defaultMessage: "In Progress",
    description: "In progress status",
  },
  fixed: {
    id: "aardvark.status.fixed",
    defaultMessage: "Fixed",
    description: "Fixed status",
  },
  wontfix: {
    id: "aardvark.status.wontfix",
    defaultMessage: "Won't fix",
    description: "Won't fix status",
  },
  duplicate: {
    id: "aardvark.status.duplicate",
    defaultMessage: "Duplicate",
    description: "Duplicate status",
  },
  false_positive: {
    id: "aardvark.status.falsePositive",
    defaultMessage: "False positive",
    description: "False positive status",
  },
};

export const CRITICALITY_MESSAGES: Record<
  FindingCriticality,
  MessageDescriptor
> = {
  critical: {
    id: "aardvark.crit.critical",
    defaultMessage: "Critical",
    description: "Critical severity",
  },
  high: {
    id: "aardvark.crit.high",
    defaultMessage: "High",
    description: "High severity",
  },
  medium: {
    id: "aardvark.crit.medium",
    defaultMessage: "Medium",
    description: "Medium severity",
  },
  low: {
    id: "aardvark.crit.low",
    defaultMessage: "Low",
    description: "Low severity",
  },
  informational: {
    id: "aardvark.crit.informational",
    defaultMessage: "Informational",
    description: "Informational severity",
  },
};
