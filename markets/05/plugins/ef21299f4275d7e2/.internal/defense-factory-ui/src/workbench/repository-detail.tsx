import type { components } from "@oai/aardvark-client/components";
import { Plus as PlusIcon } from "@oai/ds/icons/plus";
import { useState, type ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation } from "react-router";

import { AppLink, ExternalLink } from "../link";
import { DateTime, Report } from "../ui";
import { WorkbenchButton as Button, WorkbenchLink } from "./controls";
import {
  WorkbenchPageHeader,
  WorkbenchState,
  WorkbenchStatusBadge,
} from "./layout";
import { RepositoryScanActivity } from "./repository-scan-activity";
import { workbenchStyles } from "./styles";

type Configuration = components["schemas"]["AardvarkScanConfigurationResponse"];
type ConfigurationSummary =
  components["schemas"]["AardvarkScanConfigurationListItem"];
type RepositorySection = "overview" | "findings" | "scans";

function monitoringState(
  configuration: Configuration | undefined,
  configurationSummary: ConfigurationSummary | undefined,
): "active" | "paused" | "unmonitored" {
  const scanInput =
    configuration?.scan_input ?? configurationSummary?.scan_input;
  if (!scanInput || !("state" in scanInput)) {
    return "unmonitored";
  }
  return scanInput.state === "enabled" ? "active" : "paused";
}

function MonitoringStatusBadge({
  state,
}: {
  state: ReturnType<typeof monitoringState>;
}) {
  return (
    <WorkbenchStatusBadge
      variant={
        state === "active"
          ? "success"
          : state === "paused"
          ? "warning"
          : "muted"
      }
    >
      {state === "active" ? (
        <FormattedMessage
          id="codexSecurity.workbench.repositories.statusActive"
          defaultMessage="Monitoring"
          description="Repository monitoring is enabled."
        />
      ) : state === "paused" ? (
        <FormattedMessage
          id="codexSecurity.workbench.repositories.statusPaused"
          defaultMessage="Paused"
          description="Repository monitoring is paused."
        />
      ) : (
        <FormattedMessage
          id="codexSecurity.workbench.repositories.statusUnmonitored"
          defaultMessage="Not monitored"
          description="Repository does not have continuous monitoring configured."
        />
      )}
    </WorkbenchStatusBadge>
  );
}

function repositoryThreatModel(configuration: Configuration | undefined) {
  if (
    !configuration ||
    !("project_overview" in configuration.scan_input) ||
    !configuration.scan_input.project_overview
  ) {
    return null;
  }
  const raw = configuration.scan_input.project_overview;
  try {
    const value: unknown = JSON.parse(raw);
    if (
      value &&
      typeof value === "object" &&
      "threat_model" in value &&
      typeof value.threat_model === "string"
    ) {
      return value.threat_model;
    }
    return null;
  } catch {
    return raw;
  }
}

function currentStepLabel(
  step: ConfigurationSummary["current_step"],
): ReactNode {
  switch (step) {
    case "initialized":
      return "Initialized";
    case "waiting_for_new_commits":
      return "Waiting for new commits";
    case "generating_threat_model":
      return "Generating threat model";
    case "threat_model_generated":
      return "Threat model ready";
    case "scanning_commit":
      return "Scanning a commit";
    default:
      return "—";
  }
}

export function WorkbenchRepositoryDetail({
  canEditMonitoring,
  children,
  configuration,
  configurationSummary,
  defaultBranch,
  fullName,
  repoId,
  repoUrl,
  section,
  settings,
}: {
  canEditMonitoring: boolean;
  children?: ReactNode;
  configuration?: Configuration;
  configurationSummary?: ConfigurationSummary;
  defaultBranch?: string | null;
  fullName: string;
  repoId: string;
  repoUrl: string;
  section: RepositorySection;
  settings: ReactNode;
}) {
  const intl = useIntl();
  const location = useLocation();
  const [showSettings, setShowSettings] = useState(false);
  const settingsId = "repository-monitoring-settings";
  const state = monitoringState(configuration, configurationSummary);
  const continuousInput =
    configuration && "lookback_days" in configuration.scan_input
      ? configuration.scan_input
      : configurationSummary &&
        "lookback_days" in configurationSummary.scan_input
      ? configurationSummary.scan_input
      : undefined;
  const threatModel = repositoryThreatModel(configuration);
  const repositoryPath = `/repositories/${encodeURIComponent(repoId)}`;
  const repositorySearch = new URLSearchParams(location.search);
  repositorySearch.set("repo", repoUrl);
  repositorySearch.set("repo_id", repoId);
  const configurationId =
    configuration?.hid ||
    configuration?.id ||
    configurationSummary?.hid ||
    configurationSummary?.id;
  if (configurationId) {
    repositorySearch.set("scan_configuration_id", configurationId);
  }
  function sectionHref(nextSection: RepositorySection) {
    const parameters = new URLSearchParams(repositorySearch);
    if (nextSection !== section) {
      // Findings and scans use different cursor formats and pagination state.
      for (const key of [
        "cursor",
        "page",
        "commit_cursor",
        "workflow_exhausted",
        "commit_exhausted",
      ]) {
        parameters.delete(key);
      }
    }
    const path = nextSection === "overview" ? "" : `/${nextSection}`;
    return `${repositoryPath}${path}?${parameters}`;
  }

  return (
    <section className={workbenchStyles.detailPage}>
      <WorkbenchPageHeader
        kind="detail"
        title={fullName}
        titleAdornment={<MonitoringStatusBadge state={state} />}
        description={
          <ExternalLink href={repoUrl} className={workbenchStyles.link}>
            <FormattedMessage
              id="codexSecurity.workbench.repositories.openOnGithub"
              defaultMessage="View on GitHub"
              description="Open the current repository on GitHub."
            />
          </ExternalLink>
        }
        actions={
          <>
            <Button
              color="outlineSurface"
              type="button"
              aria-controls={settingsId}
              aria-expanded={showSettings}
              onClick={() => setShowSettings((visible) => !visible)}
            >
              <FormattedMessage
                id="codexSecurity.workbench.repositories.monitoringSettings.button.label"
                defaultMessage="Monitoring settings"
                description="Show the current repository's continuous monitoring settings."
              />
            </Button>
            <WorkbenchLink
              to={`/scans/new?${repositorySearch}`}
              state={location.state}
            >
              <PlusIcon className="icon-sm" />
              <FormattedMessage
                id="codexSecurity.workbench.repositories.runScan"
                defaultMessage="Run scan"
                description="Run a one-off full repository scan."
              />
            </WorkbenchLink>
          </>
        }
      />

      <nav
        aria-label={intl.formatMessage({
          id: "codexSecurity.workbench.repositories.sectionsAriaLabel",
          defaultMessage: "Repository sections",
          description:
            "Navigation for the overview, findings, and scans of one repository.",
        })}
        className="-m-1 flex items-center gap-1 overflow-x-auto p-1"
      >
        <RepositoryNavigationLink
          active={section === "overview"}
          to={sectionHref("overview")}
        >
          <FormattedMessage
            id="codexSecurity.workbench.repositories.sectionOverview"
            defaultMessage="Overview"
            description="Repository overview tab."
          />
        </RepositoryNavigationLink>
        <RepositoryNavigationLink
          active={section === "findings"}
          to={sectionHref("findings")}
        >
          <FormattedMessage
            id="codexSecurity.workbench.repositories.sectionFindings"
            defaultMessage="Findings"
            description="Repository findings tab."
          />
        </RepositoryNavigationLink>
        <RepositoryNavigationLink
          active={section === "scans"}
          to={sectionHref("scans")}
        >
          <FormattedMessage
            id="codexSecurity.workbench.repositories.sectionScans"
            defaultMessage="Scans"
            description="Repository scans tab."
          />
        </RepositoryNavigationLink>
      </nav>

      {showSettings ? (
        <div id={settingsId} className="space-y-3">
          {!canEditMonitoring && configuration ? (
            <WorkbenchState variant="inline">
              <FormattedMessage
                id="codexSecurity.workbench.repositories.monitoringSettings.readOnly"
                defaultMessage="You can view these monitoring settings, but only the owner or a workspace administrator can change them."
                description="Read-only notice above repository monitoring settings."
              />
            </WorkbenchState>
          ) : null}
          {settings}
        </div>
      ) : null}

      {children ?? (
        <div className="space-y-6">
          <section className={`${workbenchStyles.card} space-y-5 p-6`}>
            <div className="space-y-1">
              <h2 className={workbenchStyles.sectionTitle}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.monitoringHeading"
                  defaultMessage="Continuous monitoring"
                  description="Repository overview heading for continuous commit monitoring."
                />
              </h2>
              <p className={workbenchStyles.description}>
                {state === "paused" ? (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.monitoringPaused.description"
                    defaultMessage="Monitoring is paused. New commits will not be reviewed automatically."
                    description="Repository monitoring is currently paused."
                  />
                ) : (
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.monitoringDescription"
                    defaultMessage="Review new commits automatically as your repository changes."
                    description="Explanation of continuous repository monitoring."
                  />
                )}
              </p>
            </div>
            <dl className="divide-token-border-light divide-y">
              <RepositoryMetadataRow
                label={intl.formatMessage({
                  id: "codexSecurity.workbench.repositories.metadataStatus",
                  defaultMessage: "Status",
                  description: "Repository monitoring status label.",
                })}
                value={<MonitoringStatusBadge state={state} />}
              />
              <RepositoryMetadataRow
                label={intl.formatMessage({
                  id: "codexSecurity.workbench.repositories.metadataBranch",
                  defaultMessage: "Default branch",
                  description: "Repository default branch label.",
                })}
                value={defaultBranch ?? "—"}
              />
              <RepositoryMetadataRow
                label={intl.formatMessage({
                  id: "codexSecurity.workbench.repositories.metadataOwner",
                  defaultMessage: "Monitoring owner",
                  description: "Repository monitoring owner label.",
                })}
                value={
                  configuration?.owner?.email ??
                  configurationSummary?.owner?.email ??
                  "—"
                }
              />
              {configuration?.updated_at || configurationSummary?.updated_at ? (
                <RepositoryMetadataRow
                  label={intl.formatMessage({
                    id: "codexSecurity.workbench.repositories.metadataMonitoringUpdated",
                    defaultMessage: "Monitoring settings updated",
                    description:
                      "Timestamp of the last monitoring-settings update.",
                  })}
                  value={
                    <DateTime
                      value={
                        configuration?.updated_at ??
                        configurationSummary!.updated_at
                      }
                    />
                  }
                />
              ) : null}
              {continuousInput?.lookback_days != null ? (
                <RepositoryMetadataRow
                  label={intl.formatMessage({
                    id: "codexSecurity.workbench.repositories.metadataHistory",
                    defaultMessage: "Commit history",
                    description:
                      "Configured continuous-monitoring lookback period.",
                  })}
                  value={intl.formatMessage(
                    {
                      id: "codexSecurity.workbench.repositories.metadataHistoryValue",
                      defaultMessage:
                        "{days, plural, one {# day} other {# days}}",
                      description:
                        "Number of days of commit history monitored.",
                    },
                    { days: continuousInput.lookback_days },
                  )}
                />
              ) : null}
              {state === "active" && configurationSummary?.current_step ? (
                <RepositoryMetadataRow
                  label={intl.formatMessage({
                    id: "codexSecurity.workbench.repositories.metadataLastReportedActivity",
                    defaultMessage: "Last reported activity",
                    description:
                      "Last activity recorded by continuous monitoring.",
                  })}
                  value={currentStepLabel(configurationSummary.current_step)}
                />
              ) : null}
            </dl>
          </section>

          <RepositoryScanActivity
            configurationId={configurationId}
            configurationRecordIds={[
              configuration?.id,
              configuration?.hid,
              configurationSummary?.id,
              configurationSummary?.hid,
            ].filter((value): value is string => Boolean(value))}
            repoConnectorId={
              configuration?.scan_input.repo_connector_id ??
              configurationSummary?.scan_input.repo_connector_id ??
              null
            }
            repoId={repoId}
            repoUrl={repoUrl}
          />

          {configurationSummary ? (
            <section className={`${workbenchStyles.card} space-y-3 p-6`}>
              <h2 className={workbenchStyles.sectionTitle}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.threatModel.title"
                  defaultMessage="Threat model"
                  description="Repository threat model heading."
                />
              </h2>
              {configuration && threatModel ? (
                <Report>{threatModel}</Report>
              ) : !configuration ? (
                <p className={workbenchStyles.description}>
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.threatModel.unavailable"
                    defaultMessage="Threat model details are unavailable."
                    description="Privacy-preserving message when a monitored repository's threat model cannot be loaded."
                  />
                </p>
              ) : (
                <p className={workbenchStyles.description}>
                  <FormattedMessage
                    id="codexSecurity.workbench.repositories.threatModel.empty"
                    defaultMessage="No threat model is available yet."
                    description="Repository has monitoring but no generated threat model."
                  />
                </p>
              )}
            </section>
          ) : (
            <section className={`${workbenchStyles.card} space-y-2 p-6`}>
              <h2 className={workbenchStyles.sectionTitle}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.setupHeading"
                  defaultMessage="Set up monitoring"
                  description="Heading for an unmonitored repository."
                />
              </h2>
              <p className={workbenchStyles.description}>
                <FormattedMessage
                  id="codexSecurity.workbench.repositories.setupDescription"
                  defaultMessage="Configure continuous monitoring to review new commits and generate a threat model for this repository."
                  description="Explanation of repository monitoring setup."
                />
              </p>
            </section>
          )}
        </div>
      )}
    </section>
  );
}

function RepositoryNavigationLink({
  active,
  children,
  to,
}: {
  active: boolean;
  children: ReactNode;
  to: string;
}) {
  return (
    <AppLink
      aria-current={active ? "page" : undefined}
      className={[
        "df-workbench-navigation-tab rounded-full px-3 py-2 whitespace-nowrap",
        active
          ? "bg-token-bg-secondary text-token-text-primary"
          : "text-token-text-secondary hover:bg-token-bg-tertiary hover:text-token-text-primary",
      ].join(" ")}
      to={to}
    >
      {children}
    </AppLink>
  );
}

function RepositoryMetadataRow({
  label,
  value,
}: {
  label: string;
  value: ReactNode;
}) {
  return (
    <div className="grid min-h-12 gap-1 py-3 sm:grid-cols-[minmax(0,1fr)_minmax(0,2fr)] sm:items-center sm:gap-5">
      <dt className={workbenchStyles.metadataLabel}>{label}</dt>
      <dd
        className={`${workbenchStyles.metadataValue} min-w-0 break-words sm:text-end`}
      >
        {value}
      </dd>
    </div>
  );
}
