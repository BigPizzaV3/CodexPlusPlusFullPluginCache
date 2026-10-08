---
name: revensi-connector-catalog
description: Manage named services in a Revensi workspace connector catalog. Use when the user asks to add or remove a connector or inspect which workflows mention one; do not use for connecting or disconnecting an external account.
---

# Revensi Connector Catalog

Revensi's connector catalog records named services used in workflow maps. It is not an OAuth connection manager and does not grant access to those services. The catalog response does not report live access or proposed `read`, `write`, or `act` capabilities.

1. Use `list_connectors` to identify the catalog entry and any workflows that mention it.
2. To add a named service, use `add_connector` with the user's name and only a supported category they actually specified. The server resolves the workspace selected during OAuth; do not supply or guess a workspace ID. Explain that this adds a catalog record, not an external account connection. Do not invent credentials or request access scopes.
3. To remove one, identify its exact connector ID and name from a live `list_connectors` result. Check workflow references. If it is referenced, explain that the v1 removal path must refuse it until those references are handled; do not remove it by guessed name. If unreferenced, use `remove_connector` only after the user has clearly asked to remove that specific entry. Explain that removing a catalog entry does not revoke an external service authorization or erase historical workflow text.
4. Report the returned connector ID and outcome. Never claim an add or removal succeeded based only on a proposed plan.

If a write times out, check the live catalog before retrying or reporting an outcome; the first call may still have completed.

If the authenticated write tools are unavailable, explain that catalog changes are unavailable; do not substitute a web request or another tool.
