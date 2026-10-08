import { WorkbenchIcon } from "./icons";
import { DatePicker } from "@oai/ds/ui/date-picker";
import { Popover } from "@oai/ds/ui/popover";
import { useId, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import {
  getOverviewPresetRange,
  isOverviewDateRangeTooLong,
  MAX_OVERVIEW_RANGE_DAYS,
  type OverviewDateRange,
} from "../overview-dates";
import { WorkbenchButton as Button } from "./controls";

export function PipelinePeriodControls({
  value,
  onChange,
}: {
  value: OverviewDateRange | undefined;
  onChange: (range: OverviewDateRange | undefined) => void;
}) {
  const intl = useIntl();
  const fieldId = useId();
  const [open, setOpen] = useState(false);
  const [draft, setDraft] = useState(value ?? getOverviewPresetRange(30));
  const today = new Date().toISOString().slice(0, 10);
  const draftValid =
    draft.startDate <= draft.endDate && !isOverviewDateRangeTooLong(draft);
  const presets = [
    {
      label: intl.formatMessage({
        id: "defenseFactory.pipeline.period.all",
        defaultMessage: "All time",
        description: "Pipeline discovery period without date filtering.",
      }),
      range: undefined,
    },
    {
      label: intl.formatMessage({
        id: "codexSecurity.overview.dateRange.week.label",
        defaultMessage: "Last 7 days",
        description: "Today and the previous six UTC dates.",
      }),
      range: getOverviewPresetRange(7),
    },
    {
      label: intl.formatMessage({
        id: "codexSecurity.overview.dateRange.month.label",
        defaultMessage: "Last 30 days",
        description: "Today and the previous 29 UTC dates.",
      }),
      range: getOverviewPresetRange(30),
    },
  ];
  const selectedPreset = presets.find(
    ({ range }) =>
      range?.startDate === value?.startDate &&
      range?.endDate === value?.endDate,
  );
  const periodLabel =
    selectedPreset?.label ??
    (value
      ? `${formatDate(value.startDate)} – ${formatDate(value.endDate)}`
      : presets[0].label);

  function formatDate(date: string) {
    return intl.formatDate(`${date}T00:00:00.000Z`, {
      month: "short",
      day: "numeric",
      timeZone: "UTC",
    });
  }

  function applyRange(range: OverviewDateRange | undefined) {
    onChange(range);
    setOpen(false);
  }

  return (
    <Popover
      open={open}
      onOpenChange={(nextOpen) => {
        if (nextOpen) setDraft(value ?? getOverviewPresetRange(30));
        setOpen(nextOpen);
      }}
    >
      <Popover.Trigger>
        <Button
          color="outlineSurface"
          radius="small"
          aria-label={intl.formatMessage(
            {
              id: "defenseFactory.pipeline.period.label",
              defaultMessage: "Pipeline discovery period (UTC): {period}",
              description: "Accessible label for the pipeline period picker.",
            },
            { period: periodLabel },
          )}
        >
          {periodLabel}
          <WorkbenchIcon name="chevronDown" />
        </Button>
      </Popover.Trigger>
      <Popover.Content align="end" minWidth={300} width={360}>
        <div className="flex flex-col gap-4 p-4">
          <div className="flex flex-wrap gap-2">
            {presets.map((preset) => (
              <Button
                key={preset.label}
                color="outlineSurface"
                aria-pressed={selectedPreset === preset}
                onClick={() => applyRange(preset.range)}
              >
                {preset.label}
              </Button>
            ))}
          </div>
          <div className="grid grid-cols-2 gap-3">
            {(["startDate", "endDate"] as const).map((field) => (
              <div key={field} className="flex min-w-0 flex-col gap-1.5">
                <label
                  id={`${fieldId}-${field}-label`}
                  htmlFor={`${fieldId}-${field}`}
                  className="text-token-text-secondary text-[14px] leading-5"
                >
                  {field === "startDate" ? (
                    <FormattedMessage
                      id="defenseFactory.plugin.startDate"
                      defaultMessage="Start date"
                      description="First UTC discovery date in the pipeline period."
                    />
                  ) : (
                    <FormattedMessage
                      id="defenseFactory.plugin.endDate"
                      defaultMessage="End date"
                      description="Last UTC discovery date in the pipeline period."
                    />
                  )}
                </label>
                <DatePicker
                  id={`${fieldId}-${field}`}
                  aria-labelledby={`${fieldId}-${field}-label`}
                  valueType="date"
                  value={calendarDate(draft[field])}
                  max={calendarDate(today, true)}
                  locale={intl.locale}
                  pill={false}
                  block
                  triggerDateFormat="MMM d, yyyy"
                  triggerClassName="df-control"
                  triggerShowIcon={false}
                  onChange={(date) => {
                    if (date) {
                      setDraft((current) => ({
                        ...current,
                        [field]: calendarDateString(date),
                      }));
                    }
                  }}
                />
              </div>
            ))}
          </div>
          <p className="text-token-text-tertiary text-xs">
            <FormattedMessage
              id="defenseFactory.pipeline.period.help"
              defaultMessage="Findings discovered during these UTC dates, grouped by current status. Choose up to {maxDays, number} days."
              description="Explains discovery-date filtering and the custom date-range limit."
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
                id="defenseFactory.pipeline.period.apply"
                defaultMessage="Apply"
                description="Apply the custom pipeline discovery period."
              />
            </Button>
          </div>
        </div>
      </Popover.Content>
    </Popover>
  );
}

// The calendar works in local dates; preserve the selected date's digits when
// converting to our UTC date-only API model, rather than shifting its timezone.
function calendarDate(date: string, endOfDay = false): Date {
  return new Date(`${date}T${endOfDay ? "23:59:59.999" : "00:00:00"}`);
}

function calendarDateString(date: Date): string {
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(
    2,
    "0",
  )}-${String(date.getDate()).padStart(2, "0")}`;
}
