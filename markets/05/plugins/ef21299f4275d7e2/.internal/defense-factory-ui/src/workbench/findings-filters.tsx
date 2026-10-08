import { WorkbenchButton as Button } from "./controls";
import { Select } from "@oai/ds/ui/select";
import { Code as CodeIcon } from "@oai/ds/icons/code";
import { CheckCircleDashed as StatusIcon } from "@oai/ds/icons/check-circle-dashed";
import { Filter as FilterIcon } from "@oai/ds/icons/filter";
import { Speed as SeverityIcon } from "@oai/ds/icons/speed";
import { X as CloseIcon } from "@oai/ds/icons/x";
import { Menu } from "@oai/ds/ui/menu";
import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation, useNavigate } from "react-router";

import { useMediaQuery } from "../hooks/use-media-query";
import {
  findingFilters,
  getCsvFilterValues,
  getFindingFilterValues,
} from "./findings-fields";
import {
  getCodexSecurityFindingsFilterState,
  getCodexSecurityFindingsStatusSearch,
  CLOSED_FINDING_STATUSES,
  OPEN_FINDING_STATUSES,
} from "./findings-utils";
import { CRITICALITY_MESSAGES, STATUS_MESSAGES } from "./messages";
import {
  parseFindingSource,
  FINDING_SOURCES,
  findingSourceLabels,
  type FindingSourceType,
} from "./finding-source-types";
import { scanTypeMessages } from "./scan-types";
import type { FindingCriticality } from "./types";

const CRITICALITY_OPTIONS: FindingCriticality[] = [
  "critical",
  "high",
  "medium",
  "low",
  "informational",
];

const STATUS_OPTIONS = [...OPEN_FINDING_STATUSES, ...CLOSED_FINDING_STATUSES];

type FilterSection = "severity" | "scanType" | "status";

type ActiveFindingFilter = {
  key: string;
  label: string;
  param: string;
  value?: string;
};

export function FindingsStatusView() {
  const intl = useIntl();
  const location = useLocation();
  const navigate = useNavigate();
  const { statusView } = getCodexSecurityFindingsFilterState(location.search);
  const views = [
    {
      value: "open",
      label: intl.formatMessage({
        id: "defenseFactory.findings.view.open",
        defaultMessage: "Open findings",
        description:
          "Finding view containing new, triaged, and in-progress findings.",
      }),
    },
    {
      value: "closed",
      label: intl.formatMessage({
        id: "defenseFactory.findings.view.closed",
        defaultMessage: "Closed findings",
        description:
          "Finding view containing fixed, won't-fix, duplicate, and false-positive findings.",
      }),
    },
    {
      value: "all",
      label: intl.formatMessage({
        id: "defenseFactory.findings.view.all",
        defaultMessage: "All findings",
        description: "Finding view containing all finding statuses.",
      }),
    },
  ];
  return (
    <Select
      value={statusView}
      aria-label={intl.formatMessage({
        id: "defenseFactory.findings.view.label",
        defaultMessage: "Finding view",
        description: "Accessible label for the finding status view selector.",
      })}
      triggerClassName="df-control df-findings-view"
      options={
        statusView === "custom"
          ? [
              ...views,
              {
                value: "custom",
                label: intl.formatMessage({
                  id: "defenseFactory.findings.view.custom",
                  defaultMessage: "Custom statuses",
                  description:
                    "Finding view with individually selected statuses.",
                }),
              },
            ]
          : views
      }
      onChange={({ value }) => {
        if (value !== "open" && value !== "closed" && value !== "all") return;
        navigate(
          {
            search: getCodexSecurityFindingsStatusSearch(
              location.search,
              value,
            ),
            hash: location.hash,
          },
          { replace: true },
        );
      }}
    />
  );
}

function FindingsFilterChoice({
  checked,
  children,
  onCheckedChange,
}: {
  checked: boolean;
  children: ReactNode;
  onCheckedChange: () => void;
}) {
  return (
    <Menu.CheckboxItem
      checked={checked}
      onCheckedChange={onCheckedChange}
      onSelect={(event: Event) => event.preventDefault()}
    >
      {children}
    </Menu.CheckboxItem>
  );
}

export function FindingsFilterMenu({
  onClearFilters,
}: {
  onClearFilters: () => void;
}) {
  const intl = useIntl();
  const location = useLocation();
  const navigate = useNavigate();
  // Side-by-side menus need room for both the category list and its choices.
  const useSubmenus = useMediaQuery("(min-width: 640px)");
  const activeFilterCount = findingFilters.reduce(
    (count, filter) =>
      count +
      (filter.kind === "keyword"
        ? 0
        : getFindingFilterValues(location.search, filter).length),
    0,
  );
  const selectedCriticalities = new Set(
    getCsvFilterValues(location.search, "criticality"),
  );
  const selectedStatuses = new Set(
    getCsvFilterValues(location.search, "status"),
  );
  const selectedScanType = parseFindingSource(
    new URLSearchParams(location.search).get("source"),
  );

  const sections: Array<{
    id: FilterSection;
    label: string;
    count: number;
    icon: ReactNode;
  }> = [
    {
      id: "severity",
      label: intl.formatMessage(
        findingFilters.find((filter) => filter.kind === "severity")!.label,
      ),
      count: selectedCriticalities.size,
      icon: <SeverityIcon className="icon-sm" aria-hidden />,
    },
    {
      id: "scanType",
      label: intl.formatMessage(scanTypeMessages.label),
      count: selectedScanType ? 1 : 0,
      icon: <CodeIcon className="icon-sm" aria-hidden />,
    },
    {
      id: "status",
      label: intl.formatMessage(
        findingFilters.find((filter) => filter.kind === "status")!.label,
      ),
      count: selectedStatuses.size,
      icon: <StatusIcon className="icon-sm" aria-hidden />,
    },
  ];

  function changeSearch(params: URLSearchParams) {
    params.delete("cursor");
    params.delete("page");
    const nextSearch = params.toString();
    navigate(
      { search: nextSearch ? `?${nextSearch}` : "", hash: location.hash },
      { replace: true },
    );
  }

  function toggleCsvValue(param: string, value: string) {
    const params = new URLSearchParams(location.search);
    const values = new Set(getCsvFilterValues(location.search, param));
    if (values.has(value)) values.delete(value);
    else values.add(value);
    if (values.size > 0) params.set(param, Array.from(values).join(","));
    else if (param === "status") params.set(param, "");
    else params.delete(param);
    if (param === "criticality") params.delete("sev");
    changeSearch(params);
  }

  function changeScanType(scanType: FindingSourceType | "all") {
    const params = new URLSearchParams(location.search);
    if (scanType === "all") params.delete("source");
    else params.set("source", scanType);
    changeSearch(params);
  }

  function sectionChoices(section: FilterSection) {
    return section === "severity" ? (
      <div className="flex flex-col">
        {CRITICALITY_OPTIONS.map((criticality) => (
          <FindingsFilterChoice
            key={criticality}
            checked={selectedCriticalities.has(criticality)}
            onCheckedChange={() => toggleCsvValue("criticality", criticality)}
          >
            {intl.formatMessage(CRITICALITY_MESSAGES[criticality])}
          </FindingsFilterChoice>
        ))}
      </div>
    ) : section === "status" ? (
      <div className="flex flex-col">
        <FindingsFilterChoice
          checked={selectedStatuses.size === 0}
          onCheckedChange={() => {
            const params = new URLSearchParams(location.search);
            params.set("status", "");
            changeSearch(params);
          }}
        >
          <FormattedMessage
            id="codex.security.workbench.findings.filters.allStatuses"
            defaultMessage="All statuses"
            description="Finding filter option that includes findings in every status."
          />
        </FindingsFilterChoice>
        {STATUS_OPTIONS.map((status) => (
          <FindingsFilterChoice
            key={status}
            checked={selectedStatuses.has(status)}
            onCheckedChange={() => toggleCsvValue("status", status)}
          >
            {intl.formatMessage(STATUS_MESSAGES[status])}
          </FindingsFilterChoice>
        ))}
      </div>
    ) : (
      <Menu.RadioGroup<FindingSourceType | "all">
        value={selectedScanType ?? "all"}
        onChange={changeScanType}
      >
        <Menu.RadioItem
          value="all"
          onSelect={(event: Event) => event.preventDefault()}
        >
          {intl.formatMessage(scanTypeMessages.all)}
        </Menu.RadioItem>
        {FINDING_SOURCES.map((scanType) => (
          <Menu.RadioItem
            key={scanType}
            value={scanType}
            onSelect={(event: Event) => event.preventDefault()}
          >
            {intl.formatMessage(findingSourceLabels[scanType])}
          </Menu.RadioItem>
        ))}
      </Menu.RadioGroup>
    );
  }

  return (
    <Menu>
      <Menu.Trigger>
        <Button
          type="button"
          color="outlineSurface"
          size="toolbar"
          aria-label={intl.formatMessage(
            {
              id: "codex.security.workbench.findings.filters.active_aria",
              defaultMessage:
                "Filter findings, {count, plural, one {# active filter} other {# active filters}}",
              description:
                "Accessible label on the Filters button above the Security Findings table. The count includes selected severities, scan type, and statuses, but excludes search and repository scope.",
            },
            { count: activeFilterCount },
          )}
        >
          <FilterIcon className="icon-sm" aria-hidden />
          <FormattedMessage
            id="codex.security.workbench.filters.button.label"
            defaultMessage="Filters"
            description="Short button label above the Security findings table. Opens the table filter categories."
          />
          {activeFilterCount > 0 ? (
            <span
              aria-hidden
              className="bg-token-bg-tertiary text-token-text-primary inline-flex h-5 min-w-5 items-center justify-center rounded px-1 text-xs font-medium"
            >
              {intl.formatNumber(activeFilterCount)}
            </span>
          ) : null}
        </Button>
      </Menu.Trigger>
      <Menu.Content align="end" minWidth={240}>
        {sections.map((section) =>
          useSubmenus ? (
            <Menu.Sub key={section.id}>
              <Menu.SubTrigger>
                {section.icon}
                <span className="min-w-0 flex-1 truncate">{section.label}</span>
                {section.count > 0 ? (
                  <span className="text-token-text-secondary tabular-nums">
                    {section.count}
                  </span>
                ) : null}
              </Menu.SubTrigger>
              <Menu.SubContent minWidth={220} maxHeight={400}>
                {sectionChoices(section.id)}
              </Menu.SubContent>
            </Menu.Sub>
          ) : (
            <div key={section.id} role="group" aria-label={section.label}>
              <div className="text-token-text-secondary px-3 py-2 text-sm font-medium">
                {section.label}
              </div>
              {sectionChoices(section.id)}
              <Menu.Separator />
            </div>
          ),
        )}
        {useSubmenus && <Menu.Separator />}
        <Menu.Item onSelect={onClearFilters}>
          <FormattedMessage
            id="codex.security.workbench.findings.filters.clear"
            defaultMessage="Clear filters"
            description="Button that removes visible Security finding filters."
          />
        </Menu.Item>
      </Menu.Content>
    </Menu>
  );
}

export function ActiveFindingsFilters({
  onClearFilters,
}: {
  onClearFilters: () => void;
}) {
  const intl = useIntl();
  const location = useLocation();
  const navigate = useNavigate();
  const { statusView, hasNarrowingFilters } =
    getCodexSecurityFindingsFilterState(location.search);
  const chips: ActiveFindingFilter[] = [];

  for (const filter of findingFilters) {
    if (
      filter.kind === "status" &&
      (statusView === "open" || statusView === "all")
    ) {
      continue;
    }
    const values =
      filter.kind === "status" && statusView === "closed"
        ? [
            {
              value: undefined,
              label: intl.formatMessage({
                id: "codex.security.workbench.findings.status.closed",
                defaultMessage: "Closed",
                description:
                  "Short label for Security findings in any closed state.",
              }),
            },
          ]
        : getFindingFilterValues(location.search, filter).map((value) => {
            const scanType = parseFindingSource(value);
            const message =
              filter.kind === "severity"
                ? CRITICALITY_MESSAGES[
                    value as keyof typeof CRITICALITY_MESSAGES
                  ]
                : filter.kind === "status"
                  ? STATUS_MESSAGES[value as keyof typeof STATUS_MESSAGES]
                  : filter.kind === "scanType" && scanType
                    ? findingSourceLabels[scanType]
                    : undefined;
            return {
              value: filter.kind === "keyword" ? undefined : value,
              label: message ? intl.formatMessage(message) : value,
            };
          });
    for (const { value, label } of values) {
      chips.push({
        key: `${filter.param}:${value ?? "all"}`,
        param: filter.param,
        value,
        label: intl.formatMessage(
          {
            id: "codex.security.workbench.findings.filter_chip.field",
            defaultMessage: "{field}: {value}",
            description:
              "Removable finding filter showing its field and localized value.",
          },
          { field: intl.formatMessage(filter.label), value: label },
        ),
      });
    }
  }

  const periodParams = new URLSearchParams(location.search);
  const startAt = periodParams.get("start_at");
  const endAt = periodParams.get("end_at");
  if (startAt || endAt) {
    const formatBoundary = (value: string) =>
      Number.isFinite(Date.parse(value))
        ? intl.formatDate(value, {
            year: "numeric",
            month: "short",
            day: "numeric",
            hour: "numeric",
            minute: "2-digit",
            timeZone: "UTC",
          })
        : value;
    // End is exclusive, so say "before" rather than implying an inclusive date.
    for (const [param, value, message] of [
      [
        "start_at",
        startAt,
        {
          id: "codex.security.workbench.findings.filter_chip.discoveredFrom",
          defaultMessage: "Discovered from {date} UTC",
          description: "Inclusive discovery-time filter carried from Pipeline.",
        },
      ],
      [
        "end_at",
        endAt,
        {
          id: "codex.security.workbench.findings.filter_chip.discoveredBefore",
          defaultMessage: "Discovered before {date} UTC",
          description: "Exclusive discovery-time filter carried from Pipeline.",
        },
      ],
    ] as const) {
      if (value)
        chips.push({
          key: param,
          param,
          label: intl.formatMessage(message, { date: formatBoundary(value) }),
        });
    }
  }

  function removeFilter(param: string, value?: string) {
    const next = new URLSearchParams(location.search);
    const remaining =
      value === undefined
        ? []
        : getCsvFilterValues(location.search, param).filter(
            (candidate) => candidate !== value,
          );
    if (remaining.length > 0) next.set(param, remaining.join(","));
    else if (param === "status") next.set(param, "");
    else next.delete(param);
    if (param === "criticality") next.delete("sev");
    next.delete("cursor");
    next.delete("page");
    const nextSearch = next.toString();
    navigate(
      { search: nextSearch ? `?${nextSearch}` : "", hash: location.hash },
      { replace: true },
    );
  }

  if (chips.length === 0) return null;

  return (
    <div
      className="df-findings-active-filters flex flex-wrap items-center gap-2"
      role="group"
      aria-label={intl.formatMessage({
        id: "codex.security.workbench.findings.active_filters.label",
        defaultMessage: "Active filters",
        description:
          "Accessible label for removable active-filter chips above the Security findings table.",
      })}
    >
      {chips.map((chip) => (
        <Button
          key={chip.key}
          type="button"
          color="secondary"
          size="compact"
          className="max-w-full rounded-full"
          aria-label={intl.formatMessage(
            {
              id: "codex.security.workbench.findings.filter_chip.remove",
              defaultMessage: "Remove filter: {filter}",
              description:
                "Accessible label for a removable Security finding filter chip.",
            },
            { filter: chip.label },
          )}
          onClick={() => removeFilter(chip.param, chip.value)}
        >
          <span className="truncate">{chip.label}</span>
          <CloseIcon className="icon-sm shrink-0" aria-hidden />
        </Button>
      ))}
      {hasNarrowingFilters || statusView !== "all" ? (
        <Button
          type="button"
          color="ghostSecondary"
          size="compact"
          onClick={onClearFilters}
        >
          <FormattedMessage
            id="codex.security.workbench.findings.filters.clear"
            defaultMessage="Clear filters"
            description="Button that removes visible Security finding filters."
          />
        </Button>
      ) : null}
    </div>
  );
}
