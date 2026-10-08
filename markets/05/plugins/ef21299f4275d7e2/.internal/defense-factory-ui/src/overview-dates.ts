const DAY_MS = 86_400_000;
export const MAX_OVERVIEW_RANGE_DAYS = 365;

export type OverviewDateRange = {
  startDate: string;
  endDate: string;
};

export function getOverviewPresetRange(
  days: 7 | 30,
  now = new Date(),
): OverviewDateRange {
  const endDate = now.toISOString().slice(0, 10);
  return {
    startDate: new Date(Date.parse(endDate) - (days - 1) * DAY_MS)
      .toISOString()
      .slice(0, 10),
    endDate,
  };
}

function isDate(value: string | null): value is string {
  if (value == null || !/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    return false;
  }
  const timestamp = Date.parse(value);
  return (
    Number.isFinite(timestamp) &&
    new Date(timestamp).toISOString().slice(0, 10) === value
  );
}

export function getOverviewDateRange(
  search: string,
  now = new Date(),
): OverviewDateRange {
  const params = new URLSearchParams(search);
  const startDate = params.get("start");
  const endDate = params.get("end");
  return (
    parseOverviewDateRange(startDate, endDate) ??
    getOverviewPresetRange(30, now)
  );
}

export function parseOverviewDateRange(
  startDate: string | null,
  endDate: string | null,
): OverviewDateRange | undefined {
  return isDate(startDate) && isDate(endDate) && startDate <= endDate
    ? { startDate, endDate }
    : undefined;
}

export function isOverviewDateRangeTooLong({
  startDate,
  endDate,
}: OverviewDateRange): boolean {
  return (
    (Date.parse(endDate) - Date.parse(startDate)) / DAY_MS + 1 >
    MAX_OVERVIEW_RANGE_DAYS
  );
}

export function getOverviewApiRange({
  startDate,
  endDate,
}: OverviewDateRange): {
  start_at: string;
  end_at: string;
} {
  // Manual refetches can bypass a query's enabled condition.
  if (isOverviewDateRangeTooLong({ startDate, endDate })) {
    throw new RangeError(
      `Overview date range must not exceed ${MAX_OVERVIEW_RANGE_DAYS} days.`,
    );
  }
  return {
    start_at: `${startDate}T00:00:00.000Z`,
    // The UI dates are inclusive; the API interval excludes its end instant.
    end_at: new Date(Date.parse(endDate) + DAY_MS).toISOString(),
  };
}
