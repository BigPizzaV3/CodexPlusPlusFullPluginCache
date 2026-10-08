import type { FindingStatus } from "./types";
import {
  findingFilters,
  getCsvFilterValues,
  getFindingFilterValues,
  retiredFindingFilterParams,
} from "./findings-fields";

export const CLOSED_FINDING_STATUSES: readonly FindingStatus[] = [
  "fixed",
  "wontfix",
  "duplicate",
  "false_positive",
];

export const OPEN_FINDING_STATUSES: readonly FindingStatus[] = [
  "new",
  "triaged",
  "in_progress",
];

const FINDINGS_FILTER_PARAMS = [
  ...findingFilters.map((filter) => filter.param),
  ...retiredFindingFilterParams,
  "sev",
  "start_at",
  "end_at",
] as const;

export function getCodexSecurityFindingsFilterState(search = "") {
  const params = new URLSearchParams(search);
  if (!params.has("criticality") && params.has("sev")) {
    params.set("criticality", params.get("sev") ?? "");
  }
  const statuses = params.has("status")
    ? getCsvFilterValues(search, "status")
    : [...OPEN_FINDING_STATUSES];
  const matchesStatuses = (expected: readonly FindingStatus[]) =>
    statuses.length === expected.length &&
    expected.every((status) => statuses.includes(status));
  const statusView: "all" | "open" | "closed" | "custom" =
    statuses.length === 0
      ? "all"
      : matchesStatuses(OPEN_FINDING_STATUSES)
      ? "open"
      : matchesStatuses(CLOSED_FINDING_STATUSES)
      ? "closed"
      : "custom";

  return {
    statuses,
    statusView,
    closedOnly:
      statuses.length > 0 &&
      statuses.every((status) =>
        CLOSED_FINDING_STATUSES.some((closedStatus) => closedStatus === status),
      ),
    hasNarrowingFilters:
      statusView === "custom" ||
      params.has("start_at") ||
      params.has("end_at") ||
      findingFilters.some(
        (filter) =>
          filter.kind !== "status" &&
          getFindingFilterValues(params.toString(), filter).length > 0,
      ),
  };
}

export function getCodexSecurityFindingsStatusSearch(
  search: string,
  status: "open" | "all" | "closed",
) {
  const params = new URLSearchParams(search);
  params.set(
    "status",
    status === "open"
      ? OPEN_FINDING_STATUSES.join(",")
      : status === "closed"
      ? CLOSED_FINDING_STATUSES.join(",")
      : "",
  );
  params.delete("cursor");
  params.delete("page");
  return `?${params.toString()}`;
}

export function getCodexSecurityFindingsClearSearch(search: string) {
  const params = new URLSearchParams(search);
  for (const key of FINDINGS_FILTER_PARAMS) params.delete(key);
  return getCodexSecurityFindingsStatusSearch(params.toString(), "all");
}

export function parseDateString(value?: string | null): Date | null {
  if (!value) return null;
  const trimmed = value.trim();
  if (!trimmed) return null;
  const parsed = new Date(trimmed);
  return Number.isNaN(parsed.getTime()) ? null : parsed;
}

export function getRelativeTimeParts(
  date: Date | null,
): { value: number; unit: Intl.RelativeTimeFormatUnit } | null {
  if (!date) return null;
  const diffMs = date.getTime() - Date.now();
  const absMs = Math.abs(diffMs);
  const minute = 60 * 1000;
  const hour = 60 * minute;
  const day = 24 * hour;
  const week = 7 * day;
  const month = 30 * day;
  const year = 365 * day;

  let unit: Intl.RelativeTimeFormatUnit;
  let value: number;

  if (absMs >= year) {
    unit = "year";
    value = diffMs / year;
  } else if (absMs >= month) {
    unit = "month";
    value = diffMs / month;
  } else if (absMs >= week) {
    unit = "week";
    value = diffMs / week;
  } else if (absMs >= day) {
    unit = "day";
    value = diffMs / day;
  } else if (absMs >= hour) {
    unit = "hour";
    value = diffMs / hour;
  } else if (absMs >= minute) {
    unit = "minute";
    value = diffMs / minute;
  } else {
    unit = "second";
    value = diffMs / 1000;
  }

  let rounded = value > 0 ? Math.floor(value) : Math.ceil(value);
  if (rounded === 0) {
    rounded = value < 0 ? -1 : 1;
  }

  return { value: rounded, unit };
}

export function getCsvParam(
  search: string,
  key: string,
  defaultValue: string,
): string[] {
  const params = new URLSearchParams(search);
  const raw = params.get(key);
  if (!raw || raw.trim() === "") return [defaultValue];
  return raw
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
}

export function shortHash(hash: string) {
  return hash.slice(0, 7);
}

export function commitUrl(
  repoUrl: string | null | undefined,
  commitHash: string,
) {
  if (!repoUrl) return null;
  try {
    const u = new URL(repoUrl.replace(/\.git$/, ""));
    if (u.hostname.includes("github.com")) {
      return `${u.origin}${u.pathname}/commit/${commitHash}`;
    }
  } catch {
    // ignore
  }
  return null;
}
