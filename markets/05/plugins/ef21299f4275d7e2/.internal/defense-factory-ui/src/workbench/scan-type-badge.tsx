import { scanTypeMessages } from "./scan-types";
import {
  findingSourceLabels,
  type FindingSourceType,
} from "./finding-source-types";
import { WorkbenchStatusBadge } from "./layout";
import { Book as BookIcon } from "@oai/ds/icons/book";
import { Commit as CommitIcon } from "@oai/ds/icons/commit";
import { Branch as BranchIcon } from "@oai/ds/icons/branch";
import { useIntl } from "react-intl";

const scanTypeIcons = {
  pr_review: BranchIcon,
  commit_scan: CommitIcon,
  repository_scan: BookIcon,
} satisfies Record<FindingSourceType, typeof CommitIcon>;

export const WorkbenchScanTypeBadge = ({
  scanType,
}: {
  scanType: FindingSourceType;
}) => {
  "use forget";
  const intl = useIntl();
  const Icon = scanTypeIcons[scanType];

  return (
    <WorkbenchStatusBadge
      variant="neutral"
      label={intl.formatMessage(scanTypeMessages.label)}
      icon={<Icon className="icon-sm" aria-hidden />}
    >
      {intl.formatMessage(findingSourceLabels[scanType])}
    </WorkbenchStatusBadge>
  );
};
