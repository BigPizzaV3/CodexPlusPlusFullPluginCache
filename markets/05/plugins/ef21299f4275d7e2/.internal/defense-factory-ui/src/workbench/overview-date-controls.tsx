import { WorkbenchButton as Button, WorkbenchInput as Input } from "./controls";
import { Popover } from "@oai/ds/ui/popover";
import { useId, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import {
  getOverviewPresetRange,
  isOverviewDateRangeTooLong,
  MAX_OVERVIEW_RANGE_DAYS,
  type OverviewDateRange,
} from "../overview-dates";

export function OverviewDateControls({
  dateRange,
  onChange,
}: {
  dateRange: OverviewDateRange;
  onChange: (range: OverviewDateRange) => void;
}) {
  const intl = useIntl();
  const errorId = useId();
  const [open, setOpen] = useState(false);
  const [draft, setDraft] = useState(dateRange);
  const dateRangeTooLong = isOverviewDateRangeTooLong(dateRange);
  const draftValid =
    draft.startDate <= draft.endDate && !isOverviewDateRangeTooLong(draft);
  const today = new Date().toISOString().slice(0, 10);
  const rangeLabel = `${formatUtcDate(
    intl,
    dateRange.startDate,
  )} – ${formatUtcDate(intl, dateRange.endDate)}`;

  function applyRange(range: OverviewDateRange) {
    if (range.startDate > range.endDate || isOverviewDateRangeTooLong(range)) {
      return;
    }
    setOpen(false);
    onChange(range);
  }

  return (
    <div className="flex flex-col items-end gap-2">
      <Popover
        open={open}
        onOpenChange={(nextOpen) => {
          if (nextOpen) setDraft(dateRange);
          setOpen(nextOpen);
        }}
      >
        <Popover.Trigger>
          <Button
            color="outlineSurface"
            aria-label={intl.formatMessage(
              {
                id: "codexSecurity.overview.activityPeriod.label",
                defaultMessage: "Activity period (UTC): {range}",
                description:
                  "Accessible name for the Activity date-range control.",
              },
              { range: rangeLabel },
            )}
            aria-invalid={dateRangeTooLong || undefined}
            aria-describedby={dateRangeTooLong ? errorId : undefined}
          >
            {rangeLabel}
          </Button>
        </Popover.Trigger>
        <Popover.Content align="end" minWidth={320} width={380}>
          <div className="flex flex-col gap-4 p-4">
            <div className="flex flex-wrap gap-2">
              <Button
                color="outlineSurface"
                onClick={() => applyRange(getOverviewPresetRange(7))}
              >
                <FormattedMessage
                  id="codexSecurity.overview.dateRange.week.label"
                  defaultMessage="Last 7 days"
                  description="Preset for the Activity period covering today and the previous six UTC dates."
                />
              </Button>
              <Button
                color="outlineSurface"
                onClick={() => applyRange(getOverviewPresetRange(30))}
              >
                <FormattedMessage
                  id="codexSecurity.overview.dateRange.month.label"
                  defaultMessage="Last 30 days"
                  description="Preset for the Activity period covering today and the previous 29 UTC dates."
                />
              </Button>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              <label className="text-token-text-secondary flex flex-col gap-1.5 text-[14px] leading-5">
                <FormattedMessage
                  id="defenseFactory.plugin.startDate"
                  defaultMessage="Start date"
                  description="First UTC date in the overview Activity period."
                />
                <Input
                  type="date"
                  value={draft.startDate}
                  max={draft.endDate < today ? draft.endDate : today}
                  onChange={(event) => {
                    const startDate = event.currentTarget.value;
                    if (startDate) {
                      setDraft((current) => ({ ...current, startDate }));
                    }
                  }}
                />
              </label>
              <label className="text-token-text-secondary flex flex-col gap-1.5 text-[14px] leading-5">
                <FormattedMessage
                  id="defenseFactory.plugin.endDate"
                  defaultMessage="End date"
                  description="Last UTC date in the overview Activity period."
                />
                <Input
                  type="date"
                  value={draft.endDate}
                  min={draft.startDate}
                  max={today}
                  onChange={(event) => {
                    const endDate = event.currentTarget.value;
                    if (endDate) {
                      setDraft((current) => ({ ...current, endDate }));
                    }
                  }}
                />
              </label>
            </div>
            <p className="text-token-text-tertiary text-xs">
              <FormattedMessage
                id="codexSecurity.overview.dateRange.limit.message"
                defaultMessage="Choose a date range of {maxDays, plural, one {# day} other {# days}} or less."
                description="Guidance in the Activity date-range control."
                values={{ maxDays: MAX_OVERVIEW_RANGE_DAYS }}
              />
            </p>
            <div className="border-token-border-light flex justify-end border-t pt-3">
              <Button
                color="primary"
                disabled={!draftValid}
                onClick={() => applyRange(draft)}
              >
                <FormattedMessage
                  id="codexSecurity.overview.dateRange.apply"
                  defaultMessage="Apply"
                  description="Apply the custom Security overview Activity period."
                />
              </Button>
            </div>
          </div>
        </Popover.Content>
      </Popover>
      {dateRangeTooLong ? (
        <p
          id={errorId}
          role="alert"
          className="text-token-text-secondary text-sm"
        >
          <FormattedMessage
            id="codexSecurity.overview.dateRange.limit.message"
            defaultMessage="Choose a date range of {maxDays, plural, one {# day} other {# days}} or less."
            description="Error below the Activity date-range control when a saved URL contains too many dates."
            values={{ maxDays: MAX_OVERVIEW_RANGE_DAYS }}
          />
        </p>
      ) : null}
    </div>
  );
}

function formatUtcDate(intl: ReturnType<typeof useIntl>, date: string): string {
  return intl.formatDate(`${date}T00:00:00.000Z`, {
    month: "short",
    day: "numeric",
    timeZone: "UTC",
  });
}
