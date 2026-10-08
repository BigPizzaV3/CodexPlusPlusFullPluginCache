import type { components } from "@oai/aardvark-client/components";
import { Checkbox } from "@oai/ds/ui/checkbox";
import { Select } from "@oai/ds/ui/select";
import { useMutation, useQuery } from "@tanstack/react-query";
import { type ReactNode, useId, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { useCloud } from "./app-context";
import { securityClient } from "./client";
import type { DefenseFactoryResponse } from "./contract";
import { RequestState, Section } from "./ui";
import {
  WorkbenchButton as Button,
  WorkbenchInput as Input,
  WorkbenchLink,
} from "./workbench/controls";

export function NotificationRules({
  value,
  onChange,
  disabled,
}: {
  value: Array<components["schemas"]["AardvarkScanNotificationRuleResponse"]>;
  onChange: (
    value: Array<components["schemas"]["AardvarkScanNotificationRuleResponse"]>,
  ) => void;
  disabled: boolean;
}) {
  const cloud = useCloud();
  if (!cloud.notifications?.canConfigure) return null;
  return (
    <NotificationRulesEditor
      value={value}
      onChange={onChange}
      disabled={disabled}
      maxRules={cloud.notifications.maxRules}
      maxDestinations={cloud.notifications.maxDestinations}
    />
  );
}

function NotificationRulesEditor({
  value,
  onChange,
  disabled,
  maxRules,
  maxDestinations,
}: {
  value: Array<components["schemas"]["AardvarkScanNotificationRuleResponse"]>;
  onChange: (
    value: Array<components["schemas"]["AardvarkScanNotificationRuleResponse"]>,
  ) => void;
  disabled: boolean;
  maxRules: number;
  maxDestinations: number;
}) {
  const intl = useIntl();
  const { accountId } = useCloud();
  const { data, error, refetch, isPending } = useQuery({
    queryKey: ["notification-connections", accountId],
    queryFn: () =>
      securityClient.request({ operation: "notifications_connections" }),
    staleTime: 60_000,
    refetchOnWindowFocus: true,
  });
  const cannotEdit = disabled || data?.disabled || !data;
  function update(
    index: number,
    rule: components["schemas"]["AardvarkScanNotificationRuleResponse"],
  ) {
    onChange(
      value.map((item, itemIndex) => (itemIndex === index ? rule : item)),
    );
  }
  return (
    <section className="flex min-w-0 flex-col gap-4">
      {data?.disabled ? (
        <p className="text-sm text-secondary">
          <FormattedMessage
            id="defenseFactory.notifications.disabled"
            defaultMessage="Codex for Slack is disabled by your workspace administrator"
            description="Slack notification configuration is blocked by the workspace administrator"
          />
        </p>
      ) : (
        <WorkbenchLink
          color="ghostSecondary"
          href={data?.settingsUrl}
          aria-disabled={!data}
        >
          <FormattedMessage
            id="defenseFactory.notifications.connect"
            defaultMessage="Manage Slack connections"
            description="Open connected apps settings to add or reconnect Codex for Slack"
          />
        </WorkbenchLink>
      )}
      {isPending || error ? (
        <RequestState error={error} retry={() => void refetch()} />
      ) : null}
      {value.map((rule, index) => (
        <Section key={rule.id ?? index} title={rule.name}>
          <Field
            label={
              <FormattedMessage
                id="defenseFactory.notifications.name"
                defaultMessage="Rule name"
                description="Name identifying a Slack security notification rule"
              />
            }
          >
            {(id) => (
              <Input
                id={id}
                value={rule.name}
                disabled={cannotEdit}
                onChange={(event) =>
                  update(index, { ...rule, name: event.target.value })
                }
              />
            )}
          </Field>
          <Checkbox
            checked={rule.enabled}
            disabled={cannotEdit}
            onCheckedChange={(enabled) => update(index, { ...rule, enabled })}
            label={
              <FormattedMessage
                id="defenseFactory.notifications.enabled"
                defaultMessage="Enabled"
                description="Whether this Slack security notification rule is enabled"
              />
            }
          />
          <fieldset className="flex flex-col gap-3" disabled={cannotEdit}>
            <legend className="mb-2 text-[14px] font-medium">
              <FormattedMessage
                id="defenseFactory.notifications.severity"
                defaultMessage="Severity"
                description="Finding severities that trigger the notification rule"
              />
            </legend>
            <div className="flex flex-wrap gap-3">
              {(
                ["critical", "high", "medium", "low", "informational"] as const
              ).map((severity) => (
                <Checkbox
                  key={severity}
                  checked={rule.criticalities.includes(severity)}
                  disabled={cannotEdit}
                  onCheckedChange={(checked) =>
                    update(index, {
                      ...rule,
                      criticalities: checked
                        ? [...rule.criticalities, severity]
                        : rule.criticalities.filter(
                            (item) => item !== severity,
                          ),
                    })
                  }
                  label={
                    <FormattedMessage
                      id="defenseFactory.notifications.severity.value"
                      defaultMessage="{severity, select, critical {Critical} high {High} medium {Medium} low {Low} other {Informational}}"
                      description="Security severity choice in a notification rule"
                      values={{ severity }}
                    />
                  }
                />
              ))}
            </div>
          </fieldset>
          <Field
            label={
              <FormattedMessage
                id="defenseFactory.notifications.keywords"
                defaultMessage="Keywords"
                description="Comma-separated keywords used to match security findings"
              />
            }
          >
            {(id) => (
              <CommaListInput
                id={id}
                value={rule.keywords}
                disabled={cannotEdit}
                onChange={(keywords) => update(index, { ...rule, keywords })}
              />
            )}
          </Field>
          <Checkbox
            checked={rule.keyword_match_mode === "all"}
            disabled={cannotEdit}
            onCheckedChange={(all) =>
              update(index, {
                ...rule,
                keyword_match_mode: all ? "all" : "any",
              })
            }
            label={
              <FormattedMessage
                id="defenseFactory.notifications.match"
                defaultMessage="Match all keywords"
                description="Require all keywords instead of any keyword in a matching security finding"
              />
            }
          />
          <Field
            label={
              <FormattedMessage
                id="defenseFactory.notifications.paths"
                defaultMessage="Path prefixes"
                description="Comma-separated repository path prefixes that match a security notification"
              />
            }
          >
            {(id) => (
              <CommaListInput
                id={id}
                value={rule.path_prefixes}
                disabled={cannotEdit}
                onChange={(path_prefixes) =>
                  update(index, { ...rule, path_prefixes })
                }
              />
            )}
          </Field>
          {rule.destinations.map((destination, destinationIndex) => (
            <SlackDestination
              key={destinationIndex}
              rule={rule}
              destination={destination}
              workspaces={data?.workspaces ?? []}
              disabled={cannotEdit}
              onChange={(updated) =>
                update(index, {
                  ...rule,
                  destinations: rule.destinations.map((item, itemIndex) =>
                    itemIndex === destinationIndex ? updated : item,
                  ),
                })
              }
              onRemove={() =>
                update(index, {
                  ...rule,
                  destinations: rule.destinations.filter(
                    (_item, itemIndex) => itemIndex !== destinationIndex,
                  ),
                })
              }
            />
          ))}
          <div className="flex flex-wrap gap-3">
            <Button
              type="button"
              color="outlineSurface"
              disabled={
                cannotEdit || rule.destinations.length >= maxDestinations
              }
              onClick={() =>
                update(index, {
                  ...rule,
                  destinations: [
                    ...rule.destinations,
                    { slack_team_id: "", channel_id: "", channel_name: "" },
                  ],
                })
              }
            >
              <FormattedMessage
                id="defenseFactory.notifications.addChannel"
                defaultMessage="Add channel"
                description="Add another destination channel to a notification rule"
              />
            </Button>
            <Button
              type="button"
              color="danger"
              disabled={cannotEdit}
              onClick={() =>
                onChange(
                  value.filter((_rule, itemIndex) => itemIndex !== index),
                )
              }
            >
              <FormattedMessage
                id="defenseFactory.notifications.remove"
                defaultMessage="Remove rule"
                description="Delete this Slack security notification rule when settings are saved"
              />
            </Button>
          </div>
        </Section>
      ))}
      <Button
        type="button"
        color="outlineSurface"
        disabled={cannotEdit || value.length >= maxRules}
        onClick={() =>
          onChange([
            ...value,
            {
              name: intl.formatMessage({
                id: "defenseFactory.notifications.defaultName",
                defaultMessage: "Critical findings",
                description:
                  "Default name for a new Slack notification rule for critical security findings",
              }),
              enabled: true,
              criticalities: ["critical"],
              keywords: [],
              keyword_match_mode: "any",
              path_prefixes: [],
              destinations: [
                { slack_team_id: "", channel_id: "", channel_name: "" },
              ],
            },
          ])
        }
      >
        <FormattedMessage
          id="defenseFactory.notifications.add"
          defaultMessage="Add notification rule"
          description="Add a Slack notification rule for security findings"
        />
      </Button>
    </section>
  );
}

function SlackDestination({
  rule,
  destination,
  workspaces,
  disabled,
  onChange,
  onRemove,
}: {
  rule: components["schemas"]["AardvarkScanNotificationRuleResponse"];
  destination: components["schemas"]["SlackChannelDestination"];
  workspaces: DefenseFactoryResponse<"notifications_connections">["workspaces"];
  disabled: boolean;
  onChange: (
    destination: components["schemas"]["SlackChannelDestination"],
  ) => void;
  onRemove: () => void;
}) {
  const intl = useIntl();
  const [sentTo, setSentTo] = useState<string | null>(null);
  const workspace = workspaces.find(
    (item) => item.id === destination.slack_team_id,
  );
  const destinationKey = JSON.stringify([
    destination.slack_team_id,
    destination.channel_id,
  ]);
  const channelName = destination.channel_name;
  const {
    mutate: validate,
    error: validationError,
    isPending: validating,
  } = useMutation({
    mutationFn: () =>
      securityClient.request({
        operation: "notifications_validate",
        parameters: { path: { slack_team_id: destination.slack_team_id } },
        requestBody: { channel_id: destination.channel_id },
      }),
    onSuccess: (channel) => {
      onChange({
        ...destination,
        channel_id: channel.channel_id,
        channel_name: channel.channel_name,
      });
    },
  });
  const {
    mutate: sendTest,
    error: testError,
    isPending: sending,
  } = useMutation({
    mutationFn: () =>
      securityClient.request({
        operation: "notifications_test",
        parameters: { path: { slack_team_id: destination.slack_team_id } },
        requestBody: {
          channel_id: destination.channel_id,
          criticalities: rule.criticalities,
          keywords: rule.keywords,
          keyword_match_mode: rule.keyword_match_mode,
          path_prefixes: rule.path_prefixes,
        },
      }),
    onSuccess: () => setSentTo(destinationKey),
  });
  const busy = disabled || validating || sending;
  return (
    <div className="flex min-w-0 flex-col gap-3 border-t border-default pt-4">
      <Select
        triggerClassName="df-control"
        value={destination.slack_team_id}
        disabled={busy}
        aria-label={intl.formatMessage({
          id: "defenseFactory.notifications.workspace",
          defaultMessage: "Select a workspace",
          description: "Choose a connected Slack workspace for notifications",
        })}
        placeholder={intl.formatMessage({
          id: "defenseFactory.notifications.workspace",
          defaultMessage: "Select a workspace",
          description: "Choose a connected Slack workspace for notifications",
        })}
        options={workspaces.map((item) => ({
          value: item.id,
          label: item.name,
          disabled: item.reconnect,
        }))}
        onChange={(option) => {
          setSentTo(null);
          onChange({
            destination_type: destination.destination_type,
            slack_team_id: option.value,
            channel_id: destination.channel_id,
            channel_name: "",
          });
        }}
      />
      <Field
        label={
          <FormattedMessage
            id="defenseFactory.notifications.channelId"
            defaultMessage="Slack channel ID"
            description="Identifier of the Slack channel to notify"
          />
        }
      >
        {(id) => (
          <Input
            id={id}
            value={destination.channel_id}
            disabled={busy}
            onChange={(event) => {
              setSentTo(null);
              onChange({
                destination_type: destination.destination_type,
                slack_team_id: destination.slack_team_id,
                channel_id: event.target.value,
                channel_name: "",
              });
            }}
          />
        )}
      </Field>
      {workspace?.reconnect && (
        <p className="text-sm text-secondary">
          <FormattedMessage
            id="defenseFactory.notifications.reconnect"
            defaultMessage="Reconnect this Slack workspace to validate or test notifications"
            description="The Slack connection needs authorization before delivering notifications"
          />
        </p>
      )}
      <div className="flex flex-wrap items-center gap-3">
        {channelName && (
          <span className="text-sm">
            <FormattedMessage
              id="defenseFactory.notifications.channelName"
              defaultMessage="#{channel}"
              description="Display name of a validated Slack channel"
              values={{ channel: channelName }}
            />
          </span>
        )}
        <Button
          type="button"
          color="ghostSecondary"
          disabled={
            busy || !workspace || workspace.reconnect || !destination.channel_id
          }
          loading={validating}
          onClick={() => validate()}
        >
          <FormattedMessage
            id="defenseFactory.notifications.validate"
            defaultMessage="Validate channel"
            description="Check that Codex can deliver messages to this Slack channel"
          />
        </Button>
        <Button
          type="button"
          color="ghostSecondary"
          disabled={busy || !workspace || workspace.reconnect || !channelName}
          loading={sending}
          onClick={() => sendTest()}
        >
          <FormattedMessage
            id="defenseFactory.notifications.test"
            defaultMessage="Send test notification"
            description="Explicitly send a test notification to the selected Slack channel"
          />
        </Button>
        <Button type="button" color="danger" disabled={busy} onClick={onRemove}>
          <FormattedMessage
            id="defenseFactory.notifications.removeChannel"
            defaultMessage="Remove channel"
            description="Remove a destination from this Slack security notification rule"
          />
        </Button>
      </div>
      {validationError || testError ? (
        <RequestState error={validationError ?? testError} />
      ) : sentTo === destinationKey ? (
        <p role="status" className="text-sm text-secondary">
          <FormattedMessage
            id="defenseFactory.notifications.sent"
            defaultMessage="Test notification sent"
            description="A test Slack security notification was sent successfully"
          />
        </p>
      ) : null}
    </div>
  );
}

function Field({
  label,
  children,
}: {
  label: ReactNode;
  children: (id: string) => ReactNode;
}) {
  const id = useId();
  return (
    <div className="flex flex-col gap-2">
      <label className="text-[14px] font-medium" htmlFor={id}>
        {label}
      </label>
      {children(id)}
    </div>
  );
}

/** Preserve commas while typing; the parent receives the parsed list for saving. */
function CommaListInput({
  id,
  value,
  disabled,
  onChange,
}: {
  id: string;
  value: Array<string>;
  disabled: boolean;
  onChange: (value: Array<string>) => void;
}) {
  const [draft, setDraft] = useState<{
    source: Array<string>;
    text: string;
  } | null>(null);
  return (
    <Input
      id={id}
      disabled={disabled}
      value={draft?.source === value ? draft.text : value.join(", ")}
      onChange={(event) => {
        const next = event.target.value
          .split(",")
          .map((item) => item.trim())
          .filter(Boolean);
        setDraft({ source: next, text: event.target.value });
        onChange(next);
      }}
    />
  );
}
