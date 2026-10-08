import { defineMessages } from "react-intl";

import { scanTypeLabels } from "./scan-types";
import type { Finding } from "./types";

// Finding sources also include PR reviews, which are not launchable scan types.
export type FindingSourceType = Finding["source"]["kind"];
export const FINDING_SOURCES = [
  "commit_scan",
  "repository_scan",
  "pr_review",
] as const;

export const findingSourceLabels = {
  ...scanTypeLabels,
  ...defineMessages({
    pr_review: {
      id: "codexSecurity.workbench.scanType.pullRequest",
      defaultMessage: "Pull request",
      description:
        "Scan type badge for a security finding discovered during a pull request review, distinct from commit monitoring and repository scans.",
    },
  }),
};

export function parseFindingSource(
  value: string | null,
): FindingSourceType | null {
  return FINDING_SOURCES.find((source) => source === value) ?? null;
}
