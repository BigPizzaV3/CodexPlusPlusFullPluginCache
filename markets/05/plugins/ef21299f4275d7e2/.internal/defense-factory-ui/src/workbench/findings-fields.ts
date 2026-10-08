import { defineMessage, type MessageDescriptor } from "react-intl";
import { parseFindingSource } from "./finding-source-types";
import { scanTypeMessages } from "./scan-types";

type FindingFilter =
  | { kind: "keyword"; param: "q" }
  | { kind: "severity"; param: "criticality" }
  | { kind: "status"; param: "status" }
  | { kind: "scanType"; param: "source" };

// Share labels and filter parameters between the table and filter controls.
export const findingFields = [
  {
    id: "finding",
    label: defineMessage({
      id: "codexSecurity.workbench.findings.table.column.finding",
      defaultMessage: "Finding",
      description:
        "Field label for a vulnerability finding's title in the Security findings table and filters.",
    }),
    filter: { kind: "keyword", param: "q" },
    sort: null,
  },
  {
    id: "scanType",
    label: scanTypeMessages.label,
    filter: { kind: "scanType", param: "source" },
    sort: null,
  },
  {
    id: "severity",
    label: defineMessage({
      id: "codexSecurity.workbench.findings.table.column.severity",
      defaultMessage: "Severity",
      description:
        "Field label for security severity, shared by the findings table heading and filter category.",
    }),
    filter: { kind: "severity", param: "criticality" },
    sort: "severity",
  },
  {
    id: "status",
    label: defineMessage({
      id: "codexSecurity.workbench.findings.table.column.status",
      defaultMessage: "Status",
      description:
        "Field label for finding triage status, shared by the findings table heading and filter category.",
    }),
    filter: { kind: "status", param: "status" },
    sort: null,
  },
  {
    id: "detected",
    label: defineMessage({
      id: "codexSecurity.workbench.findings.table.column.detected",
      defaultMessage: "Detected",
      description:
        "Field label for detection time in the Security findings table. This field supports sorting, but not date filtering.",
    }),
    filter: null,
    sort: "detected",
  },
] as const;

export type FindingSortField = NonNullable<
  (typeof findingFields)[number]["sort"]
>;

export const findingFilters = findingFields.flatMap<
  FindingFilter & { label: MessageDescriptor }
>((field) => (field.filter ? [{ ...field.filter, label: field.label }] : []));

export const findingSearchMessage = defineMessage({
  id: "codex.security.workbench.findings.search.placeholder",
  defaultMessage: "Search findings",
  description:
    "Placeholder and accessible label for the keyword search field above the Security findings table.",
});

export function getFindingFilterValues(search: string, filter: FindingFilter) {
  const value = new URLSearchParams(search).get(filter.param)?.trim() ?? "";
  if (filter.kind === "keyword") return value ? [value] : [];
  if (filter.kind === "scanType") {
    const scanType = parseFindingSource(value);
    return scanType ? [scanType] : [];
  }
  return getCsvFilterValues(search, filter.param);
}

export function getCsvFilterValues(search: string, param: string): string[] {
  const value = new URLSearchParams(search).get(param) ?? "";
  return Array.from(
    new Set(
      value
        .split(",")
        .map((item) => item.trim())
        .filter((item) => item && item.toLowerCase() !== "all"),
    ),
  );
}

// Old workbench URLs must not keep applying filters with no visible control.
// Repository scope and sorting are retained separately from these filters.
export const retiredFindingFilterParams = [
  "assignee",
  "assignee_email",
  "recommended",
  "path_prefix",
  "author",
  "validated",
  "has_patch",
] as const;
