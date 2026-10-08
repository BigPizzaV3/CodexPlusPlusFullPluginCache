import { WorkbenchBadge as Badge } from "./controls";
import { useId } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import type { DefenseFactoryResponse } from "../contract";
import { overviewSeverityMessages } from "./overview-breakdown-data";
import { OverviewMetricValue } from "./overview-components";

export function OverviewOpenFindings({
  findings,
}: {
  findings:
    | DefenseFactoryResponse<"dashboard_findings">["findings"]
    | undefined;
}) {
  const intl = useIntl();
  const labelId = useId();
  const totalId = useId();
  const counts = new Map(
    findings?.by_severity.map(({ key, count }) => [key, count]),
  );
  const groups = [
    {
      key: "critical",
      count: counts.get("critical") ?? 0,
      label: intl.formatMessage(overviewSeverityMessages.critical),
    },
    {
      key: "high",
      count: counts.get("high") ?? 0,
      label: intl.formatMessage(overviewSeverityMessages.high),
    },
    {
      key: "medium",
      count:
        (counts.get("medium") ?? 0) +
        (counts.get("low") ?? 0) +
        (counts.get("informational") ?? 0),
      label: intl.formatMessage({
        id: "defenseFactory.overview.openFindings.mediumOrLower",
        defaultMessage: "Medium or lower",
        description:
          "Combined medium, low, and informational severity findings.",
      }),
    },
  ];
  const unknownCount = counts.get("unknown") ?? 0;
  if (unknownCount > 0) {
    groups.push({
      key: "unknown",
      count: unknownCount,
      label: intl.formatMessage(overviewSeverityMessages.unknown),
    });
  }

  return (
    <div
      role="group"
      aria-labelledby={labelId}
      aria-describedby={totalId}
      aria-busy={findings === undefined}
      className="df-overview-metric df-overview-open-findings"
    >
      <dl>
        <dt id={labelId}>
          <FormattedMessage
            id="codexSecurity.overview.findings.open.label"
            defaultMessage="Open findings"
            description="Current open security findings across the selected repositories, independent of Activity dates."
          />
        </dt>
        <dd>
          <ul className="df-overview-open-severities">
            {groups.map(({ key, count, label }) => (
              <li key={key}>
                <OverviewMetricValue
                  value={findings === undefined ? undefined : count}
                />
                <Badge
                  variant={
                    key === "critical"
                      ? "danger"
                      : key === "high"
                      ? "warning"
                      : "default"
                  }
                  className={`df-findings-badge df-overview-severity-badge df-findings-severity-${key}`}
                >
                  {label}
                </Badge>
              </li>
            ))}
          </ul>
        </dd>
      </dl>
      <p id={totalId} className="sr-only">
        {findings === undefined ? (
          <FormattedMessage
            id="defenseFactory.overview.openFindings.loading"
            defaultMessage="Loading open findings"
            description="Accessible loading state for the open findings severity summary."
          />
        ) : (
          <FormattedMessage
            id="defenseFactory.overview.openFindings.total"
            defaultMessage="{count, plural, one {# open finding} other {# open findings}} across all severities, all dates."
            description="Accessible total for the current backlog split by severity."
            values={{ count: findings.open_total }}
          />
        )}
      </p>
    </div>
  );
}
