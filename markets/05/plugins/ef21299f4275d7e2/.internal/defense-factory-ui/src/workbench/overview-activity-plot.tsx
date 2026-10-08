import { useIntl } from "react-intl";

import type { DefenseFactoryResponse } from "../contract";

type DailyActivity = NonNullable<
  DefenseFactoryResponse<"dashboard_activity">["findings"]["daily"]
>;

export function OverviewActivityPlot({
  daily,
  severity,
}: {
  daily: DailyActivity;
  severity: string;
}) {
  const intl = useIntl();
  const points = daily.map((day) => ({
    date: day.date,
    count: day.by_severity.reduce(
      (total, item) =>
        total + (severity === "all" || item.key === severity ? item.count : 0),
      0,
    ),
  }));
  const step = Math.max(
    1,
    Math.ceil(Math.max(...points.map((p) => p.count)) / 4),
  );
  const maximum = step * 4;
  const coordinates = points.map((point, index) => ({
    x: points.length === 1 ? 50 : (index / (points.length - 1)) * 100,
    y: 100 - (point.count / maximum) * 100,
  }));
  const dateLabel = (date: string) =>
    intl.formatDate(`${date}T00:00:00Z`, {
      month: "short",
      day: "numeric",
      timeZone: "UTC",
    });
  // Percentage geometry resizes with the card. Both shapes use the API values,
  // not the static sample curves exported from Figma.
  const area = `polygon(0% 100%, ${coordinates
    .map(({ x, y }) => `${x}% ${y}%`)
    .join(", ")}, 100% 100%)`;
  const line = `polygon(${[
    ...coordinates.map(({ x, y }) => `${x}% calc(${y}% - 1px)`),
    ...[...coordinates].reverse().map(({ x, y }) => `${x}% calc(${y}% + 1px)`),
  ].join(", ")})`;
  const tickIndices = new Set(
    Array.from({ length: Math.min(4, points.length) }, (_, index) =>
      Math.round(
        (index * (points.length - 1)) / Math.min(3, points.length - 1 || 1),
      ),
    ),
  );

  return (
    <div className="df-activity-chart" aria-hidden>
      <div className="df-activity-chart-scale">
        {[4, 3, 2, 1, 0].map((tick) => (
          <span key={tick}>{intl.formatNumber(tick * step)}</span>
        ))}
      </div>
      <div className="df-activity-chart-plot">
        {[0, 25, 50, 75, 100].map((top) => (
          <div
            key={top}
            className="df-activity-chart-gridline"
            style={{ top: `${top}%` }}
          />
        ))}
        {points.length === 1 ? (
          <div
            className="df-activity-chart-single"
            style={{ height: `${(points[0].count / maximum) * 100}%` }}
          />
        ) : (
          <>
            <div
              className="df-activity-chart-area"
              style={{ clipPath: area }}
            />
            <div
              className="df-activity-chart-line"
              style={{ clipPath: line }}
            />
          </>
        )}
        <div className="df-activity-chart-hover">
          {points.map((point, index) => (
            <span
              key={point.date}
              style={{
                flex: index === 0 || index === points.length - 1 ? 0.5 : 1,
              }}
              title={`${dateLabel(point.date)} (UTC): ${intl.formatNumber(
                point.count,
              )}`}
            />
          ))}
        </div>
      </div>
      <div className="df-activity-chart-dates">
        {points.map((point, index) =>
          tickIndices.has(index) ? (
            <span
              key={point.date}
              style={{
                left: `${coordinates[index].x}%`,
                transform: `translateX(${
                  points.length === 1
                    ? -50
                    : index === 0
                    ? 0
                    : index === points.length - 1
                    ? -100
                    : -50
                }%)`,
              }}
            >
              {dateLabel(point.date)}
            </span>
          ) : null,
        )}
      </div>
    </div>
  );
}
