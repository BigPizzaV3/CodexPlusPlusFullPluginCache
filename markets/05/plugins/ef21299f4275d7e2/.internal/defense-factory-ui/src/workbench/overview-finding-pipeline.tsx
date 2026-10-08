import { useId, type ReactNode } from "react";
import { FormattedMessage, FormattedNumber, useIntl } from "react-intl";

import { AppLink } from "../link";
import { STATUS_MESSAGES } from "./messages";
import { OverviewLoading } from "./overview-components";
import { getOverviewApiRange, type OverviewDateRange } from "../overview-dates";
import { PipelinePeriodControls } from "./pipeline-period-controls";
import type { FindingStatus } from "./types";

import "./overview-finding-pipeline.css";

const MAIN_STATUSES: FindingStatus[] = [
  "new",
  "triaged",
  "in_progress",
  "fixed",
];
const OTHER_STATUSES: FindingStatus[] = [
  "duplicate",
  "false_positive",
  "wontfix",
];

// Counts are measured at column centers. Sample a smooth curve between them so
// adjacent colored segments meet at the same thickness and slope. Percentages
// keep the ribbon responsive without measuring the DOM or drawing static assets.
function ribbonClipPath(previous: number, current: number, next: number) {
  const points = Array.from({ length: 33 }, (_, index) => {
    const x = index / 32;
    const t = x < 0.5 ? x + 0.5 : x - 0.5;
    const start = x < 0.5 ? previous : current;
    const end = x < 0.5 ? current : next;
    const thickness = start + (end - start) * t * t * (3 - 2 * t);
    return { x: x * 100, top: 50 - thickness * 50 };
  });
  return `polygon(${[
    ...points.map(({ x, top }) => `${x}% ${top.toFixed(3)}%`),
    ...[...points]
      .reverse()
      .map(({ x, top }) => `${x}% ${(100 - top).toFixed(3)}%`),
  ].join(", ")})`;
}

export function OverviewFindingPipeline({
  counts,
  repositories,
  dateRange,
  onDateRangeChange,
  error,
}: {
  counts: Record<FindingStatus, number> | undefined;
  repositories: string[];
  dateRange: OverviewDateRange | undefined;
  onDateRangeChange: (range: OverviewDateRange | undefined) => void;
  error?: ReactNode;
}) {
  const intl = useIntl();
  const headingId = useId();
  const descriptionId = useId();
  const largestCount = counts
    ? Math.max(1, ...MAIN_STATUSES.map((status) => counts[status]))
    : 1;

  function findingUrl(status: FindingStatus) {
    const params = new URLSearchParams({ status });
    if (dateRange) {
      const { start_at, end_at } = getOverviewApiRange(dateRange);
      params.set("start_at", start_at);
      params.set("end_at", end_at);
    }
    if (repositories.length > 0) {
      params.set("repo", repositories.join(","));
    }
    return `/findings?${params}`;
  }

  return (
    <section
      className="df-finding-pipeline"
      aria-labelledby={headingId}
      aria-describedby={descriptionId}
      aria-busy={counts === undefined && !error}
    >
      <div className="df-finding-pipeline-header">
        <h3 id={headingId}>
          <FormattedMessage
            id="codexSecurity.overview.findingPipeline.title"
            defaultMessage="Pipeline"
            description="Title of the flow diagram of current finding statuses."
          />
        </h3>
        <div className="df-finding-pipeline-controls">
          <p>
            <FormattedMessage
              id="codexSecurity.overview.findingPipeline.discoveryScope"
              defaultMessage="Discovered (UTC)"
              description="The pipeline period filters finding discovery dates, not status-change dates."
            />
          </p>
          <PipelinePeriodControls
            value={dateRange}
            onChange={onDateRangeChange}
          />
        </div>
      </div>
      <p id={descriptionId} className="sr-only">
        <FormattedMessage
          id="codexSecurity.overview.findingPipeline.description"
          defaultMessage="Current status of findings discovered in the selected period, not transition history. Select a status to view its findings."
          description="Accessible explanation of the finding pipeline links and their current-state semantics."
        />
      </p>
      {error}
      {counts === undefined ? (
        error ? null : (
          <OverviewLoading />
        )
      ) : (
        <div className="df-finding-pipeline-scroll">
          <div className="df-finding-pipeline-track">
            <ul className="df-finding-pipeline-main">
              {MAIN_STATUSES.map((status, index) => {
                const previousStatus = MAIN_STATUSES[index - 1] ?? status;
                const nextStatus = MAIN_STATUSES[index + 1] ?? status;
                return (
                  <li
                    key={status}
                    className={`df-finding-pipeline-stage df-finding-pipeline-${status}`}
                  >
                    <AppLink to={findingUrl(status)}>
                      <span className="df-finding-pipeline-stage-label">
                        <span className="df-finding-pipeline-count">
                          <FormattedNumber value={counts[status]} />
                        </span>
                        <span className="df-finding-pipeline-label">
                          {intl.formatMessage(STATUS_MESSAGES[status])}
                        </span>
                      </span>
                      <span
                        className="df-finding-pipeline-ribbon"
                        aria-hidden="true"
                        style={{
                          clipPath: ribbonClipPath(
                            counts[previousStatus] / largestCount,
                            counts[status] / largestCount,
                            counts[nextStatus] / largestCount,
                          ),
                        }}
                      />
                    </AppLink>
                  </li>
                );
              })}
            </ul>
            <ul className="df-finding-pipeline-other">
              {OTHER_STATUSES.map((status) => (
                <li key={status}>
                  <AppLink to={findingUrl(status)}>
                    <span className="df-finding-pipeline-count">
                      <FormattedNumber value={counts[status]} />
                    </span>
                    <span className="df-finding-pipeline-label">
                      {intl.formatMessage(STATUS_MESSAGES[status])}
                    </span>
                  </AppLink>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </section>
  );
}
