import type { FindingStatus } from "./types";
import type { WorkbenchStatusBadgeVariant } from "./layout";

export function getFindingStatusBadgeVariant(
  status: FindingStatus,
): WorkbenchStatusBadgeVariant {
  if (status === "fixed") return "success";
  if (status === "in_progress") return "purple";
  if (status === "triaged") return "warning";
  if (status === "new") return "neutral";
  return "muted";
}
