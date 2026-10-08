import { Info as InfoIcon } from "@oai/ds/icons/info";
import { Select } from "@oai/ds/ui/select";
import { Tooltip } from "@oai/ds/ui/tooltip";
import { useState, type ReactNode } from "react";
import { FormattedMessage, FormattedNumber, useIntl } from "react-intl";

import type { DefenseFactoryResponse } from "../contract";
import { OverviewActivityPlot } from "./overview-activity-plot";
import { overviewSeverityMessages } from "./overview-breakdown-data";
import { OverviewLoading } from "./overview-components";
import Table from "./table";

type DailyActivity =
  DefenseFactoryResponse<"dashboard_activity">["findings"]["daily"];

export function OverviewFindingsActivity({
  daily,
  dateControls,
}: {
  daily: DailyActivity;
  dateControls?: ReactNode;
}) {
  const intl = useIntl();
  const [severity, setSeverity] = useState("all");
  const hasFindings = daily?.some(({ by_severity }) =>
    by_severity.some(
      ({ key, count }) => count > 0 && (severity === "all" || key === severity),
    ),
  );
  const severityColumns = Object.entries(overviewSeverityMessages);
  const allLabel = intl.formatMessage({
    id: "codexSecurity.overview.activityChart.allSeverities",
    defaultMessage: "All severities",
    description: "Show discoveries across all severities in the trend chart.",
  });

  return (
    <section aria-busy={daily === undefined} className="df-overview-chart">
      <div className="df-overview-chart-header">
        <div>
          <div className="flex items-center gap-1.5">
            <h3>
              <FormattedMessage
                id="codexSecurity.overview.activityChart.title"
                defaultMessage="New findings over time"
                description="Heading for daily new findings in the selected Activity period."
              />
            </h3>
            <Tooltip
              content={
                <FormattedMessage
                  id="codexSecurity.overview.activityChart.help_text"
                  defaultMessage="Grouped by discovery date (UTC) and current severity. Includes findings that have since been fixed."
                  description="Explanation of the new-findings daily series."
                />
              }
            >
              <button
                type="button"
                className="interactive-button text-token-text-tertiary inline-flex rounded-sm"
                aria-label={intl.formatMessage({
                  id: "codexSecurity.overview.activityChart.help.label",
                  defaultMessage: "About new findings over time",
                  description:
                    "Accessible label for the information button beside daily finding activity.",
                })}
              >
                <InfoIcon className="icon-sm" aria-hidden />
              </button>
            </Tooltip>
          </div>
          <p>
            <FormattedMessage
              id="codexSecurity.overview.activityChart.subtitle"
              defaultMessage="Daily discoveries · selected period · UTC"
              description="The trend measures new discoveries, not historical open backlog or fixes."
            />
          </p>
        </div>
        {dateControls}
      </div>
      <div className="df-overview-chart-body">
        {daily === undefined ? (
          <OverviewLoading />
        ) : !hasFindings ? (
          <p className="text-token-text-tertiary flex min-h-40 items-center justify-center text-sm">
            <FormattedMessage
              id="codexSecurity.overview.activityChart.empty.label"
              defaultMessage="No new findings in this period"
              description="Empty state after a successful request finds no new findings in the selected period."
            />
          </p>
        ) : (
          <OverviewActivityPlot daily={daily} severity={severity} />
        )}
        <div className="df-chart-legend">
          <span className="df-chart-legend-swatch" aria-hidden />
          <FormattedMessage
            id="codexSecurity.overview.activityChart.foundLegend"
            defaultMessage="Found"
            description="Legend for discoveries in the trend chart."
          />
          <span className="df-chart-legend-scope">
            <Select
              value={severity}
              onChange={({ value }) => setSeverity(value)}
              triggerClassName="df-control df-chart-severity-filter"
              listMinWidth={160}
              aria-label={intl.formatMessage({
                id: "codexSecurity.overview.activityChart.severityFilter",
                defaultMessage: "Chart severity",
                description:
                  "Filter daily new findings by their current severity.",
              })}
              options={[
                { value: "all", label: allLabel },
                ...severityColumns.map(([value, message]) => ({
                  value,
                  label: intl.formatMessage(message),
                })),
              ]}
            />
          </span>
        </div>
      </div>
      {daily && daily.length > 0 ? (
        <div className="sr-only">
          <Table.Root className="overflow-x-auto">
            <caption className="sr-only">
              <FormattedMessage
                id="codexSecurity.overview.activityTable.caption"
                defaultMessage="New findings by UTC discovery date and current severity"
                description="Accessible caption for the daily finding activity table."
              />
            </caption>
            <Table.Header>
              <Table.HeaderCell className="py-3">
                <FormattedMessage
                  id="codexSecurity.overview.activityTable.date"
                  defaultMessage="Date (UTC)"
                  description="Date column in the daily finding activity table."
                />
              </Table.HeaderCell>
              {severityColumns.map(([key, message]) => (
                <Table.HeaderCell key={key} textAlign="right" className="py-3">
                  {intl.formatMessage(message)}
                </Table.HeaderCell>
              ))}
              <Table.HeaderCell textAlign="right" className="py-3">
                <FormattedMessage
                  id="codexSecurity.overview.activityTable.total"
                  defaultMessage="Total"
                  description="Total column in the daily finding activity table."
                />
              </Table.HeaderCell>
            </Table.Header>
            <Table.Body>
              {daily.map((day) => {
                const counts = new Map(
                  day.by_severity.map((item) => [item.key, item.count]),
                );
                const total = day.by_severity.reduce(
                  (sum, item) => sum + item.count,
                  0,
                );
                return (
                  <Table.Row key={day.date}>
                    <Table.Cell
                      className="text-token-text-secondary whitespace-nowrap"
                      divClassName="items-center py-3"
                    >
                      {intl.formatDate(`${day.date}T00:00:00.000Z`, {
                        year: "numeric",
                        month: "short",
                        day: "numeric",
                        timeZone: "UTC",
                      })}
                    </Table.Cell>
                    {severityColumns.map(([key]) => (
                      <Table.Cell
                        key={key}
                        textAlign="right"
                        className="tabular-nums"
                        divClassName="items-center py-3"
                      >
                        <FormattedNumber value={counts.get(key) ?? 0} />
                      </Table.Cell>
                    ))}
                    <Table.Cell
                      textAlign="right"
                      className="font-medium tabular-nums"
                      divClassName="items-center py-3"
                    >
                      <FormattedNumber value={total} />
                    </Table.Cell>
                  </Table.Row>
                );
              })}
            </Table.Body>
          </Table.Root>
        </div>
      ) : null}
    </section>
  );
}
