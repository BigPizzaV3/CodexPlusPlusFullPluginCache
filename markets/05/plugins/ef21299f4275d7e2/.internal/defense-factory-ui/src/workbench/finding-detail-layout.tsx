import { WorkbenchBadge as Badge } from "./controls";
import { ChevronLeft } from "@oai/ds/icons/chevron-left";
import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation } from "react-router";

import { AppLink } from "../link";
import { DateTime } from "../ui";
import { CRITICALITY_MESSAGES, STATUS_MESSAGES } from "./messages";
import type { FindingCriticality, FindingStatus } from "./types";

import "./finding-detail.css";

export function FindingDetailToolbar({ actions }: { actions?: ReactNode }) {
  const location = useLocation();
  return (
    <div className="df-finding-detail-toolbar">
      <AppLink
        className="df-finding-back"
        to={{
          pathname: location.pathname.replace(/\/[^/]+\/?$/, ""),
          search: location.search,
          hash: location.hash,
        }}
        state={location.state}
      >
        <ChevronLeft className="size-4" aria-hidden />
        <FormattedMessage
          id="defenseFactory.finding.allFindings"
          defaultMessage="All findings"
          description="Return from a finding detail to its findings list."
        />
      </AppLink>
      <div className="df-finding-detail-actions">{actions}</div>
    </div>
  );
}

export function FindingDetailHeading({
  title,
  status,
  updatedAt,
}: {
  title: string;
  status: FindingStatus;
  updatedAt: string;
}) {
  return (
    <header className="df-finding-detail-heading">
      <div className="df-finding-detail-title">
        <h1>{title}</h1>
        <FindingStatusBadge status={status} />
      </div>
      <p className="df-finding-updated">
        <FormattedMessage
          id="defenseFactory.finding.updatedAt"
          defaultMessage="Updated {date}"
          description="The last update time of this finding."
          values={{ date: <DateTime value={updatedAt} /> }}
        />
      </p>
    </header>
  );
}

export function FindingStatusBadge({ status }: { status: FindingStatus }) {
  const intl = useIntl();
  return (
    <Badge
      variant={
        status === "fixed"
          ? "success"
          : status === "triaged"
          ? "warning"
          : "default"
      }
      className={`df-finding-badge df-finding-status-${status}`}
    >
      {intl.formatMessage(STATUS_MESSAGES[status])}
    </Badge>
  );
}

export function FindingSeverityBadge({
  severity,
}: {
  severity: FindingCriticality;
}) {
  const intl = useIntl();
  return (
    <Badge
      variant={
        severity === "critical"
          ? "danger"
          : severity === "high"
          ? "warning"
          : severity === "medium"
          ? "reserve"
          : severity === "low"
          ? "success"
          : "default"
      }
      className={`df-finding-badge df-finding-severity-${severity}`}
    >
      {intl.formatMessage(CRITICALITY_MESSAGES[severity])}
    </Badge>
  );
}

export function FindingMetadataRow({
  label,
  children,
}: {
  label: ReactNode;
  children: ReactNode;
}) {
  return (
    <div className="df-finding-metadata-row">
      <dt>{label}</dt>
      <dd>{children}</dd>
    </div>
  );
}
