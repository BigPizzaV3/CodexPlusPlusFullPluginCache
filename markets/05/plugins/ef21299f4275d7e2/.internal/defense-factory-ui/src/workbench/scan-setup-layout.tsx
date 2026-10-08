import { Info as InfoIcon } from "@oai/ds/icons/info";
import { SegmentedControl } from "@oai/ds/ui/segmented-control";
import { Tooltip } from "@oai/ds/ui/tooltip";
import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { WorkbenchButton as Button } from "./controls";
import { WorkbenchPageHeader, WorkbenchState } from "./layout";
import { scanTypeDescriptions, scanTypeLabels } from "./scan-types";
import { workbenchStyles } from "./styles";

export function ScanSetupPage({ children }: { children: ReactNode }) {
  const intl = useIntl();

  return (
    <div
      className={[workbenchStyles.detailPage, "mx-auto max-w-4xl"].join(" ")}
    >
      <WorkbenchPageHeader
        kind="detail"
        title={intl.formatMessage({
          id: "codexSecurity.workbench.scans.launch.title",
          defaultMessage: "New Scan",
          description:
            "Main page heading on the dedicated one-time repository security scan setup page.",
        })}
      />
      {children}
    </div>
  );
}

export function ScanSetupForm({
  children,
  footer,
}: {
  children: ReactNode;
  footer?: ReactNode;
}) {
  return (
    <div className="flex min-h-0 flex-col gap-4">
      <div className={[workbenchStyles.card, "overflow-hidden"].join(" ")}>
        <div className="px-3 py-2">{children}</div>
      </div>
      {footer ? (
        <footer className="flex flex-wrap justify-end gap-2">{footer}</footer>
      ) : null}
    </div>
  );
}

export function ScanSetupFieldRow({
  label,
  value,
}: {
  label: ReactNode;
  value: ReactNode;
}) {
  return (
    <div className="flex min-w-0 flex-col gap-2 py-3 sm:flex-row sm:items-center sm:justify-between sm:gap-4">
      <div className="text-token-text-tertiary flex min-w-0 items-center gap-2 text-[14px] leading-5">
        {label}
      </div>
      <div className="text-token-text-primary min-w-0 text-[14px] leading-5 sm:max-w-[70%] sm:text-end">
        {value}
      </div>
    </div>
  );
}

export type ScanSetupScope = "diff" | "full-commit";

export function ScanSetupScopeFields({
  scope,
  disabled,
  onScopeChange,
}: {
  scope: ScanSetupScope;
  disabled: boolean;
  onScopeChange: (scope: ScanSetupScope) => void;
}) {
  const intl = useIntl();
  const scopeLabel = intl.formatMessage({
    id: "codexSecurity.workbench.scans.launch.scope.label",
    defaultMessage: "What to scan",
    description:
      "Short field label on the Security New Scan page describing what a scan analyzes.",
  });

  const options = {
    diff: {
      label: intl.formatMessage(scanTypeLabels.commit_scan),
      description: intl.formatMessage(scanTypeDescriptions.commit_scan),
      timing: intl.formatMessage({
        id: "codexSecurity.workbench.scans.launch.timing.new_commits",
        defaultMessage: "As new commits arrive",
        description:
          "Read-only timing value when Commit changes is selected. Creating this configuration monitors new commits.",
      }),
    },
    "full-commit": {
      label: intl.formatMessage(scanTypeLabels.repository_scan),
      description: intl.formatMessage(scanTypeDescriptions.repository_scan),
      timing: intl.formatMessage({
        id: "codexSecurity.workbench.scans.launch.timing.once",
        defaultMessage: "Run once now",
        description: "Read-only timing value for a one-time repository scan.",
      }),
    },
  } satisfies Record<
    ScanSetupScope,
    { label: string; description: string; timing: string }
  >;

  return (
    <>
      <ScanSetupFieldRow
        label={
          <Tooltip
            content={
              <div className="space-y-2">
                {(Object.keys(options) as ScanSetupScope[]).map((value) => (
                  <p key={value}>
                    <span className="block font-medium">
                      {options[value].label}
                    </span>
                    {options[value].description}
                  </p>
                ))}
              </div>
            }
            align="start"
          >
            <button
              type="button"
              aria-label={intl.formatMessage({
                id: "codexSecurity.workbench.scans.launch.scope.info",
                defaultMessage: "About scan options",
                description:
                  "Accessible label for help comparing commit-change and repository scans.",
              })}
              className="interactive-button inline-flex items-center gap-1.5 rounded-sm"
            >
              {scopeLabel}
              <InfoIcon className="icon-sm" aria-hidden />
            </button>
          </Tooltip>
        }
        value={
          <div className="puik-root w-fit">
            <SegmentedControl<ScanSetupScope>
              className="df-segmented-control"
              value={scope}
              onChange={onScopeChange}
              aria-label={scopeLabel}
              disabled={disabled}
            >
              <SegmentedControl.Option value="diff">
                {options.diff.label}
              </SegmentedControl.Option>
              <SegmentedControl.Option value="full-commit">
                {options["full-commit"].label}
              </SegmentedControl.Option>
            </SegmentedControl>
          </div>
        }
      />
      <ScanSetupFieldRow
        label={
          <FormattedMessage
            id="codexSecurity.workbench.scans.launch.timing.label"
            defaultMessage="When to scan"
            description="Short label for the read-only timing row on the Security New Scan page."
          />
        }
        value={<span>{options[scope].timing}</span>}
      />
    </>
  );
}

export function ScanSetupNotice({
  children,
  action,
  loading = false,
}: {
  children?: ReactNode;
  action?: ReactNode;
  loading?: boolean;
}) {
  return (
    <div className="my-2">
      <WorkbenchState variant="inline" action={action} loading={loading}>
        {children}
      </WorkbenchState>
    </div>
  );
}

export function ScanSetupRetryNotice({
  children,
  onRetry,
  retrying = false,
}: {
  children: ReactNode;
  onRetry: () => void;
  retrying?: boolean;
}) {
  return (
    <ScanSetupNotice
      action={
        <Button color="outlineSurface" loading={retrying} onClick={onRetry}>
          <FormattedMessage
            id="codexSecurity.workbench.scans.launch.retry"
            defaultMessage="Retry"
            description="Short recovery action on the Security New Scan form."
          />
        </Button>
      }
    >
      {children}
    </ScanSetupNotice>
  );
}
