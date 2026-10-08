import {
  isOverviewDateRangeTooLong,
  parseOverviewDateRange,
  type OverviewDateRange,
} from "../overview-dates";

export function getOverviewRepositories(search: string): string[] {
  return Array.from(
    new Set(
      (new URLSearchParams(search).get("repo") ?? "")
        .split(",")
        .map((repo) => repo.trim())
        .filter((repo) => repo && repo.toLowerCase() !== "all"),
    ),
  ).sort();
}

export function getOverviewSearch(
  dateRange: OverviewDateRange,
  repositories: string[],
  search = "",
): string {
  const params = new URLSearchParams(
    getPipelineSearch("", getPipelineDateRange(search)),
  );
  params.set("start", dateRange.startDate);
  params.set("end", dateRange.endDate);
  const selected = Array.from(new Set(repositories.filter(Boolean))).sort();
  if (selected.length > 0) params.set("repo", selected.join(","));
  else params.delete("repo");
  return `?${params}`;
}

// Pipeline discovery dates are independent of the activity charts' date range.
export function getPipelineDateRange(
  search: string,
): OverviewDateRange | undefined {
  const params = new URLSearchParams(search);
  const range = parseOverviewDateRange(
    params.get("pipeline_start"),
    params.get("pipeline_end"),
  );
  return range && !isOverviewDateRangeTooLong(range) ? range : undefined;
}

export function getPipelineSearch(
  search: string,
  range: OverviewDateRange | undefined,
): string {
  const params = new URLSearchParams(search);
  if (range) {
    params.set("pipeline_start", range.startDate);
    params.set("pipeline_end", range.endDate);
  } else {
    params.delete("pipeline_start");
    params.delete("pipeline_end");
  }
  return params.size > 0 ? `?${params}` : "";
}
