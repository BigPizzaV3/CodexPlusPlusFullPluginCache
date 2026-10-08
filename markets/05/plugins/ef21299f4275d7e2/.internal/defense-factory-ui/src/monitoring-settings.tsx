import type { components } from "@oai/aardvark-client/components";
import { Select } from "@oai/ds/ui/select";
import { Textarea } from "@oai/ds/ui/textarea";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { z } from "zod";

import { useCloud } from "./app-context";
import {
  connectGithub,
  logSecurityEvent,
  openEnvironment,
  securityClient,
} from "./client";
import { NotificationRules } from "./notifications";
import {
  canSaveRepositoryEnvironment,
  getRepositoryConnectionState,
  matchesRepositoryEnvironment,
  selectedRepositoryEnvironmentId,
} from "./repository-connector";
import { RequestState, Section } from "./ui";
import {
  WorkbenchButton as Button,
  WorkbenchInput as Input,
} from "./workbench/controls";

export function MonitoringSettings({
  repoId,
  configuration,
  quotaUsed,
  onSaved,
  onDeleted,
}: {
  repoId: string;
  configuration?: components["schemas"]["AardvarkScanConfigurationResponse"];
  quotaUsed: number | undefined;
  onSaved: () => Promise<void>;
  onDeleted: () => Promise<void>;
}) {
  const cloud = useCloud();
  const intl = useIntl();
  const cache = useQueryClient();
  const input: components["schemas"]["ContinuousScanInput"] | undefined =
    configuration?.scan_type === "continuous_scan"
      ? { ...configuration.scan_input, scan_type: "continuous_scan" }
      : undefined;
  const [environmentId, setEnvironmentId] = useState(
    configuration?.scan_input.environment_id ?? "",
  );
  const [enabled, setEnabled] = useState(input?.state ?? "enabled");
  const [lookback, setLookback] = useState(
    input?.lookback_days == null ? "" : String(input.lookback_days),
  );
  const [share, setShare] = useState(
    configuration?.share_targets?.map((target) => target.email).join(", ") ??
      "",
  );
  const initialOverview = input?.project_overview;
  const [overview, setOverview] = useState(
    readProjectOverview(initialOverview).text,
  );
  const [notifications, setNotifications] = useState<
    components["schemas"]["AardvarkScanNotificationRuleResponse"][]
  >(configuration?.notification_rules ?? []);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [saved, setSaved] = useState(false);
  const [attackConcerns, setAttackConcerns] = useState("");
  const [focusAreas, setFocusAreas] = useState("");
  const [additionalContext, setAdditionalContext] = useState("");
  const canWrite =
    !configuration ||
    cloud.identity?.isAdmin ||
    configuration.owner_id === cloud.identity?.userId ||
    configuration.permissions?.can_write;
  const configuredConnectorId = configuration?.scan_input.repo_connector_id;
  const { connectorId, status, canQuery } = getRepositoryConnectionState(
    cloud,
    repoId,
    configuredConnectorId,
  );
  const canConfigureNotifications = cloud.notifications?.canConfigure === true;
  const countLimit = cloud.scanLimits?.count ?? -1;
  const lookbackLimit = cloud.scanLimits?.lookbackDays ?? -1;
  const maxLookback = lookbackLimit < 0 ? 90 : Math.min(90, lookbackLimit);
  const lookbackDays = lookback.trim() === "" ? null : Number(lookback);
  const lookbackValid =
    lookbackDays == null
      ? lookbackLimit < 0
      : Number.isInteger(lookbackDays) &&
        lookbackDays >= 0 &&
        lookbackDays <= maxLookback;
  const quotaExhausted =
    !configuration &&
    countLimit >= 0 &&
    (quotaUsed == null || quotaUsed >= countLimit);
  const rulesValid =
    !canConfigureNotifications ||
    notifications.every(
      (rule) =>
        rule.name.trim() !== "" &&
        rule.destinations.length > 0 &&
        rule.destinations.every(
          (destination) =>
            destination.slack_team_id !== "" &&
            destination.channel_id !== "" &&
            destination.channel_name !== "",
        ),
    );
  const {
    mutate: connect,
    error: connectionError,
    isPending: connecting,
  } = useMutation({
    mutationFn: () => connectGithub(connectorId!),
    onSuccess: () => cache.invalidateQueries({ queryKey: ["bootstrap"] }),
  });
  const { data: repository, error: repositoryError } = useQuery({
    queryKey: ["repository", repoId, connectorId],
    queryFn: () =>
      securityClient.request({
        operation: "github_get",
        parameters: {
          path: { repo_id: repoId },
          query: { connector_id: connectorId ?? undefined },
        },
      }),
    enabled: !configuration && canQuery,
    staleTime: 60_000,
  });
  const {
    data: environments,
    error: environmentsError,
    isPending: environmentsPending,
    isFetching: environmentsFetching,
    refetch: refreshEnvironments,
  } = useQuery({
    queryKey: [
      "monitoring-environments",
      cloud.accountId,
      cloud.identity?.workspaceId,
      cloud.identity?.userId,
      repoId,
      connectorId,
    ],
    queryFn: () => securityClient.request({ operation: "environments_list" }),
    staleTime: 60_000,
  });
  const compatible = environments?.filter((env) =>
    matchesRepositoryEnvironment(env, repoId, connectorId),
  );
  const environmentsReady =
    !environmentsPending && !environmentsFetching && !environmentsError;
  const selectedEnvironmentId = configuration
    ? environmentId
    : selectedRepositoryEnvironmentId(compatible, environmentId);
  const canSaveEnvironment = canSaveRepositoryEnvironment({
    environments: compatible,
    discoveryReady: environmentsReady,
    selectedId: selectedEnvironmentId,
    configuredId: configuration?.scan_input.environment_id,
    canCreate: !configuration && canQuery,
  });
  const {
    mutate: editEnvironment,
    error: editorError,
    isPending: editing,
  } = useMutation({
    mutationFn: (id?: string) => {
      if (!environmentsReady)
        throw new Error("Wait for compatible Cloud environments to load");
      return openEnvironment(id);
    },
    onSuccess: async ({ environmentId: id }) => {
      await refreshEnvironments();
      if (id) setEnvironmentId(id);
    },
  });
  const {
    mutate: save,
    error,
    isPending,
  } = useMutation({
    mutationFn: async () => {
      if (!canSaveEnvironment)
        throw new Error("Choose a compatible Cloud environment");
      if (!configuration && (!repository || !cloud.identity || !canQuery))
        throw new Error("The repository is not ready");
      let savedEnvironmentId = selectedEnvironmentId;
      if (!savedEnvironmentId) {
        const created = await securityClient
          .request({
            operation: "environments_create_default",
            parameters: {
              path: { repo_id: repoId },
              query: { connector_id: connectorId ?? undefined },
            },
          })
          .catch((error: unknown) => {
            // A concurrent creation may leave multiple choices for the user.
            void refreshEnvironments();
            throw error;
          });
        savedEnvironmentId = created.id;
        // Retry monitoring with the existing environment if the next API call fails.
        setEnvironmentId(created.id);
        void refreshEnvironments();
      }
      const shareTargets = [
        ...new Set(
          share
            .split(",")
            .map((email) => email.trim())
            .filter(Boolean),
        ),
      ].map((email) => ({
        type: "user" as const,
        email,
        permission: "editor" as const,
      }));
      const notificationRules = canConfigureNotifications
        ? notifications.map((rule) => ({
            ...rule,
            destinations: rule.destinations.map(
              ({ slack_team_id, channel_id }) => ({
                destination_type: "slack_channel" as const,
                slack_team_id,
                channel_id,
              }),
            ),
          }))
        : undefined;
      if (configuration)
        return securityClient.request({
          operation: "monitoring_update",
          parameters: { path: { id: configuration.hid || configuration.id } },
          requestBody: {
            version: configuration.version,
            environment_id: savedEnvironmentId,
            state: enabled,
            lookback_days: lookbackDays,
            share_targets: shareTargets,
            project_overview:
              overview === readProjectOverview(initialOverview).text
                ? undefined
                : editedProjectOverview(initialOverview, overview),
            notification_rules: notificationRules,
          },
        });
      if (!repository || !cloud.identity || !canQuery)
        throw new Error("The repository is not ready");
      return securityClient.request({
        operation: "monitoring_create",
        requestBody: {
          environment_id: savedEnvironmentId,
          repo_id: repoId,
          repo_url: repository.clone_url,
          repo_connector_id: connectorId,
          owner_id: cloud.identity.userId,
          scan_type: "continuous_scan",
          state: enabled,
          lookback_days: lookbackDays,
          share_targets: shareTargets,
          notification_rules: notificationRules,
          maintainer_attack_concerns: attackConcerns || null,
          maintainer_focus_areas: focusAreas || null,
          maintainer_additional_context: additionalContext || null,
        },
      });
    },
    onSuccess: async () => {
      logSecurityEvent({
        name: "AardvarkScanConfigurationSaved",
        data: {
          repoId,
          scanEnabled: enabled === "enabled",
          isNewConfig: configuration == null,
          lookbackDays: lookbackDays ?? undefined,
        },
      });
      setSaved(true);
      await Promise.all([
        onSaved(),
        cache.invalidateQueries({ queryKey: ["monitoring-metadata"] }),
      ]);
    },
  });
  const {
    mutate: remove,
    error: deleteError,
    isPending: deleting,
  } = useMutation({
    mutationFn: () =>
      securityClient.request({
        operation: "monitoring_delete",
        parameters: {
          path: { id: configuration?.hid || configuration?.id || "" },
        },
      }),
    onSuccess: async () => {
      await Promise.all([
        onDeleted(),
        cache.invalidateQueries({ queryKey: ["monitoring-metadata"] }),
        cache.invalidateQueries({ queryKey: ["deleted-monitoring"] }),
      ]);
    },
  });
  return (
    <form
      className="flex flex-col gap-6"
      onSubmit={(e) => {
        e.preventDefault();
        if (
          canWrite &&
          canSaveEnvironment &&
          lookbackValid &&
          !quotaExhausted &&
          rulesValid &&
          !isPending &&
          !deleting &&
          (!!configuration || (canQuery && !!repository))
        )
          save();
      }}
    >
      {!configuration && !canQuery && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.github"
              defaultMessage="GitHub connection"
              description="GitHub connection setup"
            />
          }
        >
          {status === "connect" ? (
            <>
              <p className="text-sm text-secondary">
                <FormattedMessage
                  id="defenseFactory.plugin.monitoringConnectGithub"
                  defaultMessage="Connect GitHub before configuring repository monitoring"
                  description="A GitHub connection is required to create monitoring"
                />
              </p>
              <Button
                type="button"
                color="outlineSurface"
                loading={connecting}
                onClick={() => connect()}
              >
                <FormattedMessage
                  id="defenseFactory.plugin.connectGithub"
                  defaultMessage="Connect GitHub"
                  description="Open GitHub connection setup"
                />
              </Button>
            </>
          ) : status === "disabled" ? (
            <p role="status" className="text-sm text-secondary">
              <FormattedMessage
                id="defenseFactory.plugin.githubDisabled"
                defaultMessage="Your workspace administrator has disabled GitHub connections"
                description="GitHub cannot be connected under workspace policy"
              />
            </p>
          ) : status === "loading" ? (
            <RequestState />
          ) : (
            <p role="status" className="text-sm text-secondary">
              <FormattedMessage
                id="defenseFactory.plugin.repositoryConnectionUnavailable"
                defaultMessage="This repository's GitHub connection is unavailable. Check its connection and workspace access."
                description="The specific GitHub or Enterprise connection required by this repository is unavailable"
              />
            </p>
          )}
        </Section>
      )}
      <Section
        title={
          <FormattedMessage
            id="defenseFactory.plugin.continuousScanning"
            defaultMessage="Continuous scanning"
            description="Configure automatic scans of new repository commits"
          />
        }
      >
        <p className="text-sm text-secondary">
          <FormattedMessage
            id="defenseFactory.plugin.monitoringDescription"
            defaultMessage="Automatically scan new commits using the selected Cloud environment"
            description="Continuous monitoring runs on the server"
          />
        </p>
        <fieldset
          disabled={
            !canWrite || isPending || deleting || (!configuration && !canQuery)
          }
          className="grid gap-5 md:grid-cols-2"
        >
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.monitoring"
              defaultMessage="Monitoring"
              description="Continuous scanning configuration"
            />
            <Select
              triggerClassName="df-control"
              value={enabled}
              options={[
                {
                  value: "enabled",
                  label: intl.formatMessage({
                    id: "defenseFactory.plugin.enabled",
                    defaultMessage: "Enabled",
                    description: "Monitoring is enabled",
                  }),
                },
                {
                  value: "disabled",
                  label: intl.formatMessage({
                    id: "defenseFactory.plugin.paused",
                    defaultMessage: "Paused",
                    description: "Monitoring is paused",
                  }),
                },
              ]}
              onChange={(option) =>
                setEnabled(option.value as "enabled" | "disabled")
              }
            />
          </label>
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.lookback"
              defaultMessage="Lookback days"
              description="Number of days of commits to include when scanning starts"
            />
            <Input
              type="number"
              min={0}
              max={maxLookback}
              aria-invalid={!lookbackValid}
              value={lookback}
              onChange={(e) => setLookback(e.target.value)}
            />
            <span className="text-sm text-secondary">
              <FormattedMessage
                id="defenseFactory.plugin.lookbackHint"
                defaultMessage="{unlimited, select, yes {Leave blank for all history, or enter 0–{maximum} days} other {Enter 0–{maximum} days}}"
                description="Allowed lookback range for this workspace; some workspaces allow unlimited history"
                values={{
                  unlimited: lookbackLimit < 0 ? "yes" : "no",
                  maximum: maxLookback,
                }}
              />
            </span>
          </label>
          <label className="flex flex-col gap-2 text-[14px] md:col-span-2">
            <FormattedMessage
              id="defenseFactory.plugin.cloudEnvironment"
              defaultMessage="Cloud environment"
              description="Cloud runtime environment for a scan"
            />
            <Select
              triggerClassName="df-control"
              value={selectedEnvironmentId ?? ""}
              loading={environmentsPending || environmentsFetching}
              options={
                compatible?.map((env) => ({
                  value: env.id,
                  label: env.label,
                })) ?? []
              }
              onChange={(option) => setEnvironmentId(option.value)}
              placeholder={intl.formatMessage({
                id: "defenseFactory.plugin.chooseEnvironment",
                defaultMessage: "Choose an environment",
                description: "Choose a compatible Cloud environment",
              })}
            />
          </label>
          <div className="flex gap-2 md:col-span-2">
            <Button
              color="outlineSurface"
              onClick={() => editEnvironment(undefined)}
              disabled={!environmentsReady}
              loading={editing}
            >
              <FormattedMessage
                id="defenseFactory.plugin.createEnvironment"
                defaultMessage="Create environment"
                description="Open the shared Cloud environment creation dialog"
              />
            </Button>
            {selectedEnvironmentId && (
              <Button
                color="ghostSecondary"
                onClick={() => editEnvironment(selectedEnvironmentId)}
                disabled={!environmentsReady}
              >
                <FormattedMessage
                  id="defenseFactory.plugin.editEnvironment"
                  defaultMessage="Edit environment"
                  description="Edit the selected Cloud environment"
                />
              </Button>
            )}
          </div>
          {!configuration && environmentsReady && compatible?.length === 0 && (
            <p className="text-sm text-secondary md:col-span-2">
              <FormattedMessage
                id="defenseFactory.plugin.defaultMonitoringEnvironment"
                defaultMessage="Saving will create a default Cloud environment for this repository"
                description="Monitoring automatically creates its existing default environment when there is no compatible environment"
              />
            </p>
          )}
        </fieldset>
        {environmentsError && (
          <RequestState
            error={environmentsError}
            retry={() => void refreshEnvironments()}
          />
        )}
      </Section>
      <Section
        title={
          <FormattedMessage
            id="defenseFactory.plugin.sharing"
            defaultMessage="Sharing"
            description="Share editing access to repository monitoring"
          />
        }
      >
        <label className="flex flex-col gap-2 text-[14px]">
          <FormattedMessage
            id="defenseFactory.plugin.editorEmails"
            defaultMessage="Editor emails, separated by commas"
            description="Email addresses of workspace members who may edit monitoring"
          />
          <Input
            value={share}
            disabled={!canWrite || isPending || deleting}
            onChange={(e) => setShare(e.target.value)}
          />
        </label>
      </Section>
      {configuration && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.projectContext"
              defaultMessage="Project context"
              description="Additional repository context used for scanning"
            />
          }
        >
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.threatModel"
              defaultMessage="Threat model"
              description="Editable threat model within the repository overview"
            />
            <Textarea
              value={overview}
              disabled={!canWrite || isPending || deleting}
              onChange={(e) => setOverview(e.target.value)}
            />
          </label>
        </Section>
      )}
      {!configuration && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.projectContext"
              defaultMessage="Project context"
              description="Additional repository context used for scanning"
            />
          }
        >
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.attackConcerns"
              defaultMessage="Attack concerns"
              description="Repository maintainer's security concerns for the initial threat model"
            />
            <Textarea
              value={attackConcerns}
              disabled={isPending || deleting}
              onChange={(event) => setAttackConcerns(event.target.value)}
            />
          </label>
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.focusAreas"
              defaultMessage="Focus areas"
              description="Repository areas that need particular attention during security scanning"
            />
            <Textarea
              value={focusAreas}
              disabled={isPending || deleting}
              onChange={(event) => setFocusAreas(event.target.value)}
            />
          </label>
          <label className="flex flex-col gap-2 text-[14px]">
            <FormattedMessage
              id="defenseFactory.plugin.additionalContext"
              defaultMessage="Additional context"
              description="Additional repository maintainer context for the initial threat model"
            />
            <Textarea
              value={additionalContext}
              disabled={isPending || deleting}
              onChange={(event) => setAdditionalContext(event.target.value)}
            />
          </label>
        </Section>
      )}
      {canConfigureNotifications && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.notifications"
              defaultMessage="Notifications"
              description="Security finding notification rules"
            />
          }
        >
          <NotificationRules
            value={notifications}
            onChange={setNotifications}
            disabled={!canWrite || isPending || deleting}
          />
        </Section>
      )}
      {(error ||
        repositoryError ||
        editorError ||
        deleteError ||
        connectionError) && (
        <RequestState
          error={
            error ??
            repositoryError ??
            editorError ??
            deleteError ??
            connectionError
          }
        />
      )}
      <div className="flex flex-wrap items-center justify-between gap-4">
        {quotaExhausted && (
          <p role="status" className="text-sm text-secondary">
            <FormattedMessage
              id="defenseFactory.plugin.monitoringQuota"
              defaultMessage="This workspace has reached its limit of {count, number} monitored repositories"
              description="The workspace cannot create more repository monitoring configurations"
              values={{ count: countLimit }}
            />
          </p>
        )}
        <div>
          {configuration && canWrite && (
            <Button color="danger" onClick={() => setConfirmDelete(true)}>
              <FormattedMessage
                id="defenseFactory.plugin.deleteMonitoring"
                defaultMessage="Delete monitoring"
                description="Remove the monitoring configuration"
              />
            </Button>
          )}
        </div>
        <div className="flex items-center gap-3">
          {saved && (
            <span role="status">
              <FormattedMessage
                id="defenseFactory.plugin.saved"
                defaultMessage="Saved"
                description="Changes were saved"
              />
            </span>
          )}
          <Button
            color="primary"
            type="submit"
            loading={isPending}
            disabled={
              !canWrite ||
              deleting ||
              quotaExhausted ||
              !lookbackValid ||
              !rulesValid ||
              !canSaveEnvironment ||
              (!configuration && (!repository || !canQuery))
            }
          >
            <FormattedMessage
              id="defenseFactory.plugin.save"
              defaultMessage="Save"
              description="Save changes"
            />
          </Button>
        </div>
      </div>
      {confirmDelete && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.deleteConfirm"
              defaultMessage="Delete this monitoring configuration?"
              description="Confirm deleting repository monitoring"
            />
          }
        >
          <p>
            <FormattedMessage
              id="defenseFactory.plugin.recoveryWindow.repositoriesMenu"
              defaultMessage="You can restore it for 30 days from the Repositories menu under Restore deleted monitoring."
              description="Monitoring recovery period and location of the restore action in the repository overflow menu."
            />
          </p>
          <div className="flex gap-3">
            <Button
              color="dangerSolid"
              onClick={() => remove()}
              loading={deleting}
            >
              <FormattedMessage
                id="defenseFactory.plugin.deleteMonitoring"
                defaultMessage="Delete monitoring"
                description="Remove the monitoring configuration"
              />
            </Button>
            <Button
              color="ghostSecondary"
              onClick={() => setConfirmDelete(false)}
            >
              <FormattedMessage
                id="defenseFactory.plugin.cancel"
                defaultMessage="Cancel"
                description="Cancel the current action"
              />
            </Button>
          </div>
        </Section>
      )}
    </form>
  );
}

/** Preserve the machine-generated fields alongside the editable threat model. */
function readProjectOverview(raw: string | null | undefined): {
  text: string;
  record: Record<string, unknown> | null;
} {
  if (!raw) return { text: "", record: null };
  try {
    const result = z
      .looseObject({ threat_model: z.string().nullable().optional() })
      .safeParse(JSON.parse(raw));
    return result.success
      ? { text: result.data.threat_model ?? "", record: result.data }
      : { text: raw, record: null };
  } catch {
    return { text: raw, record: null };
  }
}

function editedProjectOverview(
  raw: string | null | undefined,
  threatModel: string,
): string | null {
  const { record } = readProjectOverview(raw);
  if (
    !threatModel &&
    (!record || Object.keys(record).every((key) => key === "threat_model"))
  )
    return null;
  return JSON.stringify({ ...record, threat_model: threatModel || null });
}
