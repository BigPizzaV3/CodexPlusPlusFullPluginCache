"""Typed internal models for native Meetings settings."""

from __future__ import annotations

import urllib.parse
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal, TypedDict

from helpers import is_json, is_json_array


class AutomationPolicyWire(TypedDict):
    """Recording reminder policy returned to the Meetings app."""

    autoRecordPopupsAllowed: bool


SettingsReadinessStatus = Literal[
    "checking",
    "companion-unavailable",
    "settings-unavailable",
    "update-failed",
    "settings-saving",
    "settings-reconciling",
    "update-deferred",
    "ready",
]


class SettingsReadinessWire(TypedDict):
    """User-actionable readiness returned to the Meetings app."""

    status: SettingsReadinessStatus
    canUpdate: bool
    message: str


class SettingsBootstrapWire(TypedDict):
    """Cold-start state returned while native ownership is unresolved."""

    status: Literal["loading"]


class _OptionalSettingsResponseWire(TypedDict, total=False):
    bootstrap: SettingsBootstrapWire


class CompanionSettingsWire(TypedDict):
    """Companion-owned local recording preferences."""

    available: bool
    calendarRemindersEnabled: bool | None
    soundEffectsEnabled: bool | None
    meetingDetectionEnabled: bool | None
    remindersAvailable: bool
    soundEffectsAvailable: bool
    meetingDetectionAvailable: bool


class CompanionSettingsResponseWire(_OptionalSettingsResponseWire):
    """Account-bound companion protocol v2 preferences exposed to the app."""

    ok: bool
    settings: CompanionSettingsWire
    readiness: SettingsReadinessWire


HostedSettingName = Literal[
    "featureEnabled",
    "autoRecordEnabled",
    "slackNotificationsEnabled",
]

AppConnectionStatus = Literal["connected", "disconnected", "reconnect", "unavailable"]


class AppConnectionWire(TypedDict):
    """Provider connection state; no link, account, or credential identifiers."""

    status: AppConnectionStatus
    setupUrl: str


class CalendarConnectionsWire(TypedDict):
    """Independent hosted calendar connections for Meetings onboarding."""

    google: AppConnectionWire
    outlook: AppConnectionWire


class OnboardingProfileWire(TypedDict):
    """Current-user onboarding details without exposing the profile or email."""

    firstName: str | None
    internalAccountAccess: bool


class ContextConnectionsWire(TypedDict):
    """Optional context tools offered during Meetings onboarding."""

    slack: AppConnectionWire
    teams: AppConnectionWire
    gmail: AppConnectionWire
    outlook_email: AppConnectionWire
    google_drive: AppConnectionWire
    notion: AppConnectionWire
    jira: AppConnectionWire
    linear: AppConnectionWire


def project_app_connections(
    payload: Mapping[str, object], group: Literal["calendars", "context"]
) -> CalendarConnectionsWire | ContextConnectionsWire:
    """Project canonical Apps links into a fixed onboarding provider group.

    Args:
        payload: Authenticated Apps connection-list response.
        group: Calendar providers or optional context tools to project.

    Returns:
        Provider statuses and first-party setup links, excluding private details.

    Raises:
        ValueError: The response does not contain a valid connection list.
    """
    links = payload.get("links")
    if not is_json_array(links) or any(not is_json(link) for link in links):
        raise ValueError("Invalid app connections response.")
    # Canonical IDs from connectors_client/utils/ecosystem.py and the maintained
    # Slack, Teams, and atlassian-rovo/.app.json manifests. The standalone runtime
    # cannot import the monorepo.
    provider_ids = (
        ("connector_947e0d954944416db111db556030eea6", "connector_e6a7394682e24467ac68c60696f275a4")
        if group == "calendars"
        else (
            "asdk_app_69a1d78e929881919bba0dbda1f6436d",
            "connector_246af0940da3457da0e751171dc1ce60",
            "connector_2128aebfecb84f64a069897515042a44",
            "connector_4aaab2856305417b993eca9a216aaf6e",
            "connector_5f3c8c41a1e54ad7a76272c89e2554fa",
            "asdk_app_69c18c28f1188191bf5b8445c4ab0a2e",
            "connector_692de805e3ec8191834719067174a384",
            "asdk_app_69a089a326dc8191b32a3f2553f5be2c",
        )
    )
    connections: list[AppConnectionWire] = []
    for connector_id in provider_ids:
        provider_links = [
            link for link in links if is_json(link) and link.get("connector_id") == connector_id
        ]
        connection_status: AppConnectionStatus = "disconnected"
        if provider_links:
            connection_status = "unavailable"
            if any(
                link.get("auth_status") == "ACTIVE"
                and link.get("connector_status") != "DISABLED_BY_ADMIN"
                for link in provider_links
            ):
                connection_status = "connected"
            elif any(
                link.get("auth_status") == "REAUTH_REQUIRED"
                and link.get("connector_status") != "DISABLED_BY_ADMIN"
                for link in provider_links
            ):
                connection_status = "reconnect"
        # Match Codex's Apps browser fallback. Reconnection opens the existing
        # connection's settings instead of starting a duplicate account link.
        params = {"connector": connector_id, "product-sku": "CODEX", "referrer": "codex"}
        if connection_status == "disconnected":
            params["add-connector-link"] = "true"
        connections.append(
            {
                "status": connection_status,
                "setupUrl": "https://chatgpt.com/#settings/Connectors?"
                + urllib.parse.urlencode(params),
            }
        )
    if group == "calendars":
        return {"google": connections[0], "outlook": connections[1]}
    return {
        "slack": connections[0],
        "teams": connections[1],
        "gmail": connections[2],
        "outlook_email": connections[3],
        "google_drive": connections[4],
        "notion": connections[5],
        "jira": connections[6],
        "linear": connections[7],
    }


class HostedSettingsWire(TypedDict):
    """Validated Record preferences returned through the private app gateway."""

    feature_enabled: bool
    auto_record_enabled: bool
    slack_notifications_enabled: bool
    configured_feature_enabled: bool
    configured_auto_record_enabled: bool
    configured_slack_notifications_enabled: bool
    local_recording_disabled: bool


@dataclass(frozen=True, slots=True)
class HostedSettings:
    """Validated hosted Record preferences and rollout policy."""

    feature_enabled: bool
    auto_record_enabled: bool
    slack_notifications_enabled: bool
    configured_feature_enabled: bool
    configured_auto_record_enabled: bool
    configured_slack_notifications_enabled: bool
    local_recording_disabled: bool
    bot_settings_available: bool

    def confirms(self, setting: HostedSettingName, enabled: bool) -> bool:
        """Check that the backend confirmed one requested preference.

        Args:
            setting: Hosted preference written to the Record backend.
            enabled: Requested preference value.

        Returns:
            Whether the corresponding configured value confirms the write.
        """

        if setting == "featureEnabled":
            configured = self.configured_feature_enabled
        elif setting == "autoRecordEnabled":
            configured = self.configured_auto_record_enabled
        else:
            configured = self.configured_slack_notifications_enabled
        return configured is enabled

    def structured_values(self) -> dict[str, bool]:
        """Return only configured preferences for the desktop settings surface.

        Returns:
            Saved bot preferences for eligible users, otherwise no account controls.
        """

        if not self.bot_settings_available:
            return {}
        return {
            "autoRecordEnabled": self.configured_auto_record_enabled,
            "slackNotificationsEnabled": self.configured_slack_notifications_enabled,
        }

    def to_wire(self) -> HostedSettingsWire:
        """Serialize hosted settings for the private Meetings app gateway.

        Returns:
            The complete validated app-facing settings payload.
        """

        return {
            "feature_enabled": self.feature_enabled,
            "auto_record_enabled": self.auto_record_enabled,
            "slack_notifications_enabled": self.slack_notifications_enabled,
            "configured_feature_enabled": self.configured_feature_enabled,
            "configured_auto_record_enabled": self.configured_auto_record_enabled,
            "configured_slack_notifications_enabled": (self.configured_slack_notifications_enabled),
            "local_recording_disabled": self.local_recording_disabled,
        }


@dataclass(frozen=True, slots=True)
class AutomationPolicy:
    """Validated native policy controlling local recording reminders."""

    auto_record_popups_allowed: bool

    def to_wire(self) -> AutomationPolicyWire:
        """Serialize the policy for the Meetings app.

        Returns:
            The bounded app-facing automation policy.
        """

        return {
            "autoRecordPopupsAllowed": self.auto_record_popups_allowed,
        }
