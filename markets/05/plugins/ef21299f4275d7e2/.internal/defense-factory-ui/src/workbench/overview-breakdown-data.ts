import { defineMessages } from "react-intl";

export const overviewSeverityMessages = defineMessages({
  critical: {
    id: "codexSecurity.overview.severity.critical.label",
    defaultMessage: "Critical",
    description: "Critical vulnerability severity in the Security overview.",
  },
  high: {
    id: "codexSecurity.overview.severity.high.label",
    defaultMessage: "High",
    description: "High vulnerability severity in the Security overview.",
  },
  medium: {
    id: "codexSecurity.overview.severity.medium.label",
    defaultMessage: "Medium",
    description: "Medium vulnerability severity in the Security overview.",
  },
  low: {
    id: "codexSecurity.overview.severity.low.label",
    defaultMessage: "Low",
    description: "Low vulnerability severity in the Security overview.",
  },
  informational: {
    id: "codexSecurity.overview.severity.informational.label",
    defaultMessage: "Informational",
    description: "Informational finding severity in the Security overview.",
  },
  unknown: {
    id: "codexSecurity.overview.severity.unknown.label",
    defaultMessage: "Unknown",
    description: "Finding severity is not recorded.",
  },
});
