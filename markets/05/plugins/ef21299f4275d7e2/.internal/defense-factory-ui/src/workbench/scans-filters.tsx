import { Book as BookIcon } from "@oai/ds/icons/book";
import { CheckCircleDashed as StatusIcon } from "@oai/ds/icons/check-circle-dashed";
import { ChevronLeft as ChevronLeftIcon } from "@oai/ds/icons/chevron-left";
import { ChevronRight as ChevronRightIcon } from "@oai/ds/icons/chevron-right";
import { Code as CodeIcon } from "@oai/ds/icons/code";
import { Filter as FilterIcon } from "@oai/ds/icons/filter";
import { Popover } from "@oai/ds/ui/popover";
import { RadioGroup } from "@oai/ds/ui/radio-group";
import { useEffect, useRef, useState, type ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { WorkbenchButton as Button } from "./controls";
import { scanTypeLabels, scanTypeMessages, SCAN_TYPES } from "./scan-types";
import { scanMessages as messages } from "./scans-messages";
import type { ScanStatusFilter, ScanTypeFilter } from "./scans-model";
import { workbenchStyles } from "./styles";

const STATUS_OPTIONS: Array<{
  value: ScanStatusFilter;
  message: (typeof messages)[
    | "allStatuses"
    | "active"
    | "completed"
    | "failed"
    | "canceled"];
}> = [
  { value: "all", message: messages.allStatuses },
  { value: "active", message: messages.active },
  { value: "finished", message: messages.completed },
  { value: "failed", message: messages.failed },
  { value: "canceled", message: messages.canceled },
];

type FilterSection = "repository" | "scanType" | "status";

export type ScanRepositoryFilter = {
  value: string;
  options: Array<{ value: string; label: string }>;
  onChange: (value: string) => void;
};

export function ScansFilterMenu({
  repositoryFilter,
  commitScansRequireRepository,
  scanType,
  status,
  onScanTypeChange,
  onStatusChange,
  onClearFilters,
}: {
  repositoryFilter?: ScanRepositoryFilter;
  commitScansRequireRepository: boolean;
  scanType: ScanTypeFilter;
  status: ScanStatusFilter;
  onScanTypeChange: (value: ScanTypeFilter) => void;
  onStatusChange: (value: ScanStatusFilter) => void;
  onClearFilters: () => void;
}) {
  const intl = useIntl();
  const [open, setOpen] = useState(false);
  const [activeSection, setActiveSection] = useState<FilterSection | null>(
    null,
  );
  const detailBackButtonRef = useRef<HTMLButtonElement>(null);
  const sectionTriggerRef = useRef<HTMLButtonElement | null>(null);
  const pendingFocusRef = useRef<"back" | "trigger" | null>(null);
  const sections: Array<{
    id: FilterSection;
    label: string;
    count: number;
    icon: ReactNode;
  }> = [
    ...(repositoryFilter
      ? [
          {
            id: "repository" as const,
            label: intl.formatMessage(messages.repositoryFilter),
            count: Number(repositoryFilter.value !== "__all_repositories__"),
            icon: <CodeIcon className="icon-sm" aria-hidden />,
          },
        ]
      : []),
    {
      id: "scanType",
      label: intl.formatMessage(scanTypeMessages.label),
      count: Number(scanType !== "all"),
      icon: <BookIcon className="icon-sm" aria-hidden />,
    },
    {
      id: "status",
      label: intl.formatMessage(messages.statusFilter),
      count: Number(status !== "all"),
      icon: <StatusIcon className="icon-sm" aria-hidden />,
    },
  ];
  const activeFilterCount = sections.reduce(
    (count, section) => count + section.count,
    0,
  );
  const activeSectionLabel = sections.find(
    (section) => section.id === activeSection,
  )?.label;

  useEffect(() => {
    if (!open) return;
    if (pendingFocusRef.current === "back" && activeSection) {
      detailBackButtonRef.current?.focus();
      pendingFocusRef.current = null;
    } else if (pendingFocusRef.current === "trigger" && !activeSection) {
      sectionTriggerRef.current?.focus();
      pendingFocusRef.current = null;
    }
  }, [activeSection, open]);

  const detailPanel = activeSection ? (
    <div className="flex max-h-[min(28rem,70vh)] flex-col overflow-y-auto p-1 text-[14px] leading-5">
      <div className="border-token-border-light mb-1 flex items-center gap-2 border-b px-1 pb-2 font-medium">
        <Button
          ref={detailBackButtonRef}
          type="button"
          color="ghostSecondary"
          size="compact"
          uniform
          className="lg:hidden"
          aria-label={intl.formatMessage({
            id: "codex.security.workbench.scans.filters.back",
            defaultMessage: "Back to filter categories",
            description:
              "Accessible label for returning to the scan filter category list.",
          })}
          onClick={() => {
            pendingFocusRef.current = "trigger";
            setActiveSection(null);
          }}
        >
          <ChevronLeftIcon className="icon-sm" aria-hidden />
        </Button>
        <span>{activeSectionLabel}</span>
      </div>
      {activeSection === "repository" && repositoryFilter ? (
        <RadioGroup<string>
          value={repositoryFilter.value}
          onChange={repositoryFilter.onChange}
          direction="col"
          aria-label={intl.formatMessage(messages.repositoryFilter)}
          className="gap-1"
        >
          {repositoryFilter.options.map((option) => (
            <RadioGroup.Item
              key={option.value}
              value={option.value}
              block
              className="px-2 py-2"
            >
              <span className="truncate" title={option.label}>
                {option.label}
              </span>
            </RadioGroup.Item>
          ))}
        </RadioGroup>
      ) : activeSection === "scanType" ? (
        <RadioGroup<ScanTypeFilter>
          value={scanType}
          onChange={onScanTypeChange}
          direction="col"
          aria-label={intl.formatMessage(scanTypeMessages.label)}
          className="gap-1"
        >
          <RadioGroup.Item value="all" block className="px-2 py-2">
            {intl.formatMessage(scanTypeMessages.all)}
          </RadioGroup.Item>
          {SCAN_TYPES.map((value) => (
            <RadioGroup.Item
              key={value}
              value={value}
              disabled={value === "commit_scan" && commitScansRequireRepository}
              block
              className="px-2 py-2"
            >
              {intl.formatMessage(scanTypeLabels[value])}
            </RadioGroup.Item>
          ))}
          {commitScansRequireRepository ? (
            <p className="px-2 py-2 text-secondary">
              <FormattedMessage
                id="codexSecurity.workbench.scans.filters.commitRepositoryRequired"
                defaultMessage="Select a repository to view commit changes."
                description="Explains why commit scan history is unavailable while All repositories is selected."
              />
            </p>
          ) : null}
        </RadioGroup>
      ) : (
        <RadioGroup<ScanStatusFilter>
          value={status}
          onChange={onStatusChange}
          direction="col"
          aria-label={intl.formatMessage(messages.statusFilter)}
          className="gap-1"
        >
          {STATUS_OPTIONS.map((option) => (
            <RadioGroup.Item
              key={option.value}
              value={option.value}
              block
              className="px-2 py-2"
            >
              {intl.formatMessage(option.message)}
            </RadioGroup.Item>
          ))}
        </RadioGroup>
      )}
    </div>
  ) : null;

  const rootPanel = (
    <div className="flex max-h-[min(28rem,70vh)] flex-col overflow-y-auto p-1 text-[14px] leading-5">
      <div className="px-3 py-2 font-medium">
        {intl.formatMessage(messages.filterScans)}
      </div>
      {sections.map((section) => (
        <button
          key={section.id}
          type="button"
          className="hover:bg-token-interactive-bg-tertiary-hover flex min-h-10 w-full items-center gap-3 rounded-lg px-3 py-2 text-start"
          onClick={(event) => {
            sectionTriggerRef.current = event.currentTarget;
            pendingFocusRef.current = "back";
            setActiveSection(section.id);
          }}
        >
          {section.icon}
          <span className="min-w-0 flex-1 truncate">{section.label}</span>
          {section.count > 0 ? (
            <span className="text-token-text-secondary tabular-nums">
              {section.count}
            </span>
          ) : null}
          <ChevronRightIcon className="icon-sm" aria-hidden />
        </button>
      ))}
      <div className="border-token-border-light mt-1 border-t pt-1">
        <button
          type="button"
          className="hover:bg-token-interactive-bg-tertiary-hover min-h-10 w-full rounded-lg px-3 py-2 text-start"
          onClick={() => {
            onClearFilters();
            setActiveSection(null);
          }}
        >
          {intl.formatMessage(messages.clearFilters)}
        </button>
      </div>
    </div>
  );

  return (
    <Popover
      open={open}
      onOpenChange={(nextOpen) => {
        setOpen(nextOpen);
        if (!nextOpen) setActiveSection(null);
      }}
    >
      <Popover.Trigger>
        <Button
          type="button"
          color="outlineSurface"
          className={workbenchStyles.control}
          aria-label={
            activeFilterCount > 0
              ? intl.formatMessage(messages.activeFiltersLabel, {
                  count: activeFilterCount,
                })
              : intl.formatMessage(messages.filterScans)
          }
        >
          <FilterIcon className="icon-sm" aria-hidden />
          <FormattedMessage
            id="codex.security.workbench.filters.button.label"
            defaultMessage="Filters"
            description="Short button label that opens Security table filters."
          />
          {activeFilterCount > 0 ? (
            <span
              aria-hidden
              className="bg-token-bg-tertiary text-token-text-primary inline-flex h-5 min-w-5 items-center justify-center rounded px-1 text-[12px] font-medium"
            >
              {intl.formatNumber(activeFilterCount)}
            </span>
          ) : null}
        </Button>
      </Popover.Trigger>
      <Popover.Content
        align="end"
        minWidth="auto"
        width="auto"
        className={[
          "max-w-[calc(100vw-32px)]",
          activeSection ? "w-[280px] lg:w-[568px]" : "w-[280px]",
        ].join(" ")}
      >
        <div
          className={
            activeSection ? "lg:grid lg:grid-cols-2 lg:gap-2" : undefined
          }
        >
          <div
            className={activeSection ? "hidden lg:order-2 lg:block" : undefined}
          >
            {rootPanel}
          </div>
          {detailPanel ? <div className="lg:order-1">{detailPanel}</div> : null}
        </div>
      </Popover.Content>
    </Popover>
  );
}
