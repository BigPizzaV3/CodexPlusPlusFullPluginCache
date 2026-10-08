import { useId } from "react";
import { FormattedMessage, FormattedNumber, useIntl } from "react-intl";

import type { DefenseFactoryResponse } from "../contract";
import { AppLink } from "../link";
import { overviewSeverityMessages } from "./overview-breakdown-data";
import { OverviewLoading } from "./overview-components";

export function OverviewSeverityChart({
  findings,
  repositories,
}: {
  findings:
    | DefenseFactoryResponse<"dashboard_findings">["findings"]
    | undefined;
  repositories: string[];
}) {
  const intl = useIntl();
  const headingId = useId();
  const counts = new Map(
    findings?.by_severity.map(({ key, count }) => [key, count]),
  );
  const severities = Object.entries(overviewSeverityMessages).map(
    ([key, message]) => ({
      key,
      label: intl.formatMessage(message),
      count: counts.get(key) ?? 0,
    }),
  );
  const maximum = Math.max(0, ...severities.map(({ count }) => count));

  return (
    <section
      className="df-overview-chart"
      aria-labelledby={headingId}
      aria-busy={findings === undefined}
    >
      <div className="df-overview-chart-header">
        <div>
          <h3 id={headingId}>
            <FormattedMessage
              id="codexSecurity.overview.severityChart.title"
              defaultMessage="Open findings by severity"
              description="Title of the chart showing current open findings by severity."
            />
          </h3>
          <p>
            <FormattedMessage
              id="codexSecurity.overview.severityChart.subtitle"
              defaultMessage="Current backlog · all dates"
              description="Clarifies that current open finding counts are not limited by the activity date filter."
            />
          </p>
        </div>
      </div>
      <div className="df-overview-chart-body">
        {findings === undefined ? (
          <OverviewLoading />
        ) : maximum === 0 ? (
          <p className="text-token-text-tertiary">
            <FormattedMessage
              id="codexSecurity.overview.breakdown.empty"
              defaultMessage="No open findings"
              description="Empty state in a current-open-findings breakdown."
            />
          </p>
        ) : (
          <>
            <ul className="df-severity-chart">
              {severities.map(({ key, label, count }) => {
                const params = new URLSearchParams({ sev: key });
                if (repositories.length > 0) {
                  params.set("repo", repositories.join(","));
                }
                return (
                  <li key={key} className="df-severity-chart-row">
                    {key === "unknown" ? (
                      <span className="df-severity-chart-label">{label}</span>
                    ) : (
                      <AppLink
                        to={`/findings?${params}`}
                        className="df-severity-chart-label"
                      >
                        {label}
                      </AppLink>
                    )}
                    <div className="df-severity-chart-track" aria-hidden>
                      <div
                        className={`df-severity-chart-bar df-chart-severity-${key}`}
                        style={{ width: `${(count / maximum) * 100}%` }}
                      />
                    </div>
                    <span className="tabular-nums">
                      <FormattedNumber value={count} />
                    </span>
                  </li>
                );
              })}
            </ul>
            <div className="df-severity-chart-axis" aria-hidden>
              <span>
                <FormattedNumber value={0} />
              </span>
              <span>
                <FormattedNumber value={maximum} />
              </span>
            </div>
          </>
        )}
      </div>
    </section>
  );
}
