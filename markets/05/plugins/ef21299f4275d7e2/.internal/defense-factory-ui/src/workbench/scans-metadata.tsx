import { Clock as ClockIcon } from "@oai/ds/icons/clock";
import { Code as CodeIcon } from "@oai/ds/icons/code";
import { Commit as CommitIcon } from "@oai/ds/icons/commit";
import { Stopwatch as StopwatchIcon } from "@oai/ds/icons/stopwatch";
import { User as UserIcon } from "@oai/ds/icons/user";
import type { ComponentProps } from "react";
import { useIntl } from "react-intl";

import { ExternalLink } from "../link";
import { commitUrl, shortHash } from "./findings-utils";
import { WorkbenchStatusBadge } from "./layout";
import { scanMessages as messages } from "./scans-messages";
import {
  formatDateTime,
  formatDuration,
  getScanCommitHash,
  getScanStartedAt,
  getScanStatus,
  getScanStatusPresentation,
  type WorkbenchScan,
} from "./scans-model";
import Table from "./table";

export function WorkbenchScanStatusBadge({ scan }: { scan: WorkbenchScan }) {
  const intl = useIntl();
  const presentation = getScanStatusPresentation(getScanStatus(scan));
  return (
    <WorkbenchStatusBadge variant={presentation.variant}>
      {intl.formatMessage(presentation.message)}
    </WorkbenchStatusBadge>
  );
}

export function WorkbenchScanStartedBadge({ scan }: { scan: WorkbenchScan }) {
  const intl = useIntl();
  const startedAt = getScanStartedAt(scan);
  return (
    <WorkbenchStatusBadge
      variant="neutral"
      label={intl.formatMessage(messages.started)}
      icon={<ClockIcon aria-hidden className="icon-sm shrink-0" />}
    >
      <time dateTime={startedAt}>{formatDateTime(intl, startedAt)}</time>
    </WorkbenchStatusBadge>
  );
}

export function WorkbenchScanDurationBadge({ scan }: { scan: WorkbenchScan }) {
  const intl = useIntl();
  return (
    <WorkbenchStatusBadge
      variant="neutral"
      label={intl.formatMessage(messages.duration)}
      icon={<StopwatchIcon aria-hidden className="icon-sm shrink-0" />}
    >
      {formatDuration(intl, scan)}
    </WorkbenchStatusBadge>
  );
}

export function WorkbenchScanRepositoryBadge({
  scan,
  rowLinkProps,
}: {
  scan: WorkbenchScan;
  rowLinkProps?: ComponentProps<typeof Table.RowTextLink>;
}) {
  const intl = useIntl();
  const content = scan.repositoryUrl ? (
    <ExternalLink
      href={scan.repositoryUrl}
      target="_blank"
      rel="noopener noreferrer"
      className="min-w-0 truncate text-inherit underline-offset-2 hover:underline"
      title={scan.repositoryName}
    >
      {scan.repositoryName}
    </ExternalLink>
  ) : rowLinkProps ? (
    <Table.RowTextLink
      {...rowLinkProps}
      className="min-w-0 truncate"
      title={scan.repositoryName}
    >
      {scan.repositoryName}
    </Table.RowTextLink>
  ) : (
    <span className="min-w-0 truncate" title={scan.repositoryName}>
      {scan.repositoryName}
    </span>
  );
  return (
    <WorkbenchStatusBadge
      variant="purple"
      label={intl.formatMessage(messages.repository)}
      icon={<CodeIcon aria-hidden className="icon-sm shrink-0" />}
    >
      {content}
    </WorkbenchStatusBadge>
  );
}

export function WorkbenchScanCommitBadge({
  scan,
  rowLinkProps,
}: {
  scan: WorkbenchScan;
  rowLinkProps?: ComponentProps<typeof Table.RowTextLink>;
}) {
  const intl = useIntl();
  const commitHash = getScanCommitHash(scan);
  if (!commitHash) return null;
  const href = commitUrl(scan.repositoryUrl, commitHash);
  return (
    <WorkbenchStatusBadge
      variant="purple"
      label={intl.formatMessage(messages.commit)}
      icon={<CommitIcon aria-hidden className="icon-sm shrink-0" />}
    >
      {href ? (
        <ExternalLink
          href={href}
          target="_blank"
          rel="noopener noreferrer"
          className="font-mono font-normal text-inherit underline-offset-2 hover:underline"
          title={commitHash}
        >
          {shortHash(commitHash)}
        </ExternalLink>
      ) : rowLinkProps ? (
        <Table.RowTextLink
          {...rowLinkProps}
          className="font-mono font-normal"
          title={commitHash}
        >
          {shortHash(commitHash)}
        </Table.RowTextLink>
      ) : (
        <span className="font-mono font-normal" title={commitHash}>
          {shortHash(commitHash)}
        </span>
      )}
    </WorkbenchStatusBadge>
  );
}

export function WorkbenchScanInitiatorBadge({ scan }: { scan: WorkbenchScan }) {
  const intl = useIntl();
  const initiator = scan.workflow
    ? scan.workflow.initiator_name ??
      (scan.workflow.is_owner === false
        ? intl.formatMessage({
            id: "codexSecurity.workbench.scans.detail.initiatedBy.workspaceMember",
            defaultMessage: "Workspace member",
            description:
              "Fallback initiator value when the workspace member's name is unavailable.",
          })
        : intl.formatMessage({
            id: "codexSecurity.workbench.scans.detail.initiatedBy.you",
            defaultMessage: "You",
            description:
              "Short initiator value for a scan started by the current viewer.",
          }))
    : scan.commitScan.triggered_by;
  return (
    <WorkbenchStatusBadge
      variant="info"
      label={intl.formatMessage(messages.initiatedBy)}
      icon={<UserIcon aria-hidden className="icon-sm shrink-0" />}
    >
      {initiator}
    </WorkbenchStatusBadge>
  );
}
