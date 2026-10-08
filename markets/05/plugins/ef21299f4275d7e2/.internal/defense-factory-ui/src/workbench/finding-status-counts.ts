import { useQuery } from "@tanstack/react-query";

import { useCloud } from "../app-context";
import { securityClient } from "../client";
import { getOverviewApiRange, type OverviewDateRange } from "../overview-dates";
import {
  CLOSED_FINDING_STATUSES,
  OPEN_FINDING_STATUSES,
} from "./findings-utils";
import type { FindingStatus } from "./types";

const findingStatuses = [...OPEN_FINDING_STATUSES, ...CLOSED_FINDING_STATUSES];

export function useFindingStatusCounts(
  repo: string,
  dateRange?: OverviewDateRange,
) {
  const { accountId, identity } = useCloud();
  const period = dateRange ? getOverviewApiRange(dateRange) : undefined;

  return useQuery({
    queryKey: [
      "findings",
      "status-counts",
      { accountId, userId: identity?.userId, repo, ...period },
    ],
    queryFn: async (): Promise<Record<FindingStatus, number>> => {
      const counts = await Promise.all(
        findingStatuses.map(async (status) => {
          const result = await securityClient.request({
            operation: "findings_list",
            parameters: {
              query: { status, repo: repo || undefined, ...period, limit: 1 },
            },
          });
          // The filtered total covers every page; the single item is not the count.
          return [status, result.total] as const;
        }),
      );

      return counts.reduce(
        (result, [status, total]) => ({ ...result, [status]: total }),
        {
          new: 0,
          triaged: 0,
          in_progress: 0,
          fixed: 0,
          wontfix: 0,
          duplicate: 0,
          false_positive: 0,
        },
      );
    },
    staleTime: 60_000,
    refetchOnMount: true,
  });
}
