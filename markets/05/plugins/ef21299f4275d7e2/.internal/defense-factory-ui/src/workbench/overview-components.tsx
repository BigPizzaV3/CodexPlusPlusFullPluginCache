import { WorkbenchButton as Button } from "./controls";
import { LoadingIndicator as Spinner } from "@oai/ds/ui/indicator";
import { useId, type ReactNode } from "react";
import { FormattedMessage, FormattedNumber, useIntl } from "react-intl";

export function OverviewMetric({
  label,
  value,
}: {
  label: ReactNode;
  value: number | undefined;
}) {
  const labelId = useId();
  return (
    <div
      role="group"
      aria-labelledby={labelId}
      aria-busy={value === undefined}
      className="df-overview-metric"
    >
      <dl>
        <dt id={labelId}>{label}</dt>
        <dd>
          <OverviewMetricValue value={value} />
        </dd>
      </dl>
    </div>
  );
}

// Keep the card geometry stable without showing a count from a previous scope.
export function OverviewMetricValue({ value }: { value: number | undefined }) {
  return value === undefined ? (
    <span
      aria-hidden
      className="bg-token-bg-tertiary inline-block h-[1em] w-[3ch] rounded align-middle"
    />
  ) : (
    <FormattedNumber value={value} />
  );
}

export function OverviewLoading() {
  return (
    <div
      role="status"
      className="text-token-text-secondary flex min-h-40 items-center justify-center gap-3 text-sm"
    >
      <Spinner className="h-4 w-4" />
      <FormattedMessage
        id="codexSecurity.overview.loading"
        defaultMessage="Loading overview…"
        description="Loading status while an independently loaded Security overview section is being fetched."
      />
    </div>
  );
}

export function OverviewRequestError({
  children,
  isRetrying,
  onRetry,
  asOf,
}: {
  children: ReactNode;
  isRetrying: boolean;
  onRetry: () => void;
  asOf?: string;
}) {
  const intl = useIntl();
  return (
    <div
      role="status"
      className="border-token-border-light text-token-text-secondary flex flex-wrap items-center gap-3 rounded-xl border p-5 text-sm"
    >
      <span>
        {children}
        {asOf ? (
          <span className="text-token-text-tertiary mt-1 block text-xs">
            <FormattedMessage
              id="codexSecurity.overview.section.refresh.error.asOf"
              defaultMessage="Showing data from {date}."
              description="Freshness caption shown when a section refresh fails but its previous authorized data remains visible."
              values={{
                date: intl.formatDate(asOf, {
                  year: "numeric",
                  month: "short",
                  day: "numeric",
                  hour: "numeric",
                  minute: "2-digit",
                  timeZoneName: "short",
                }),
              }}
            />
          </span>
        ) : null}
      </span>
      <Button
        color="outlineSurface"
        loading={isRetrying}
        aria-busy={isRetrying}
        onClick={onRetry}
      >
        {isRetrying ? (
          <FormattedMessage
            id="codexSecurity.overview.retry.label.pending"
            defaultMessage="Retrying…"
            description="Short disabled-button label while retrying one failed overview section."
          />
        ) : (
          <FormattedMessage
            id="codexSecurity.overview.retry.label"
            defaultMessage="Try again"
            description="Button that retries only the failed Security overview section."
          />
        )}
      </Button>
    </div>
  );
}

type DatedQuery = {
  data?: { as_of: string };
  error: unknown;
};

export function overviewAsOf(
  queries: readonly DatedQuery[],
  isRefreshing: boolean,
): number | undefined {
  if (isRefreshing || queries.some((query) => query.error || !query.data)) {
    return undefined;
  }
  const times = queries.map((query) => Date.parse(query.data!.as_of));
  return times.every(Number.isFinite) ? Math.min(...times) : undefined;
}
