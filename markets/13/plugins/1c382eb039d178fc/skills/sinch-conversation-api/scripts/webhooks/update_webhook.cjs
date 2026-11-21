#!/usr/bin/env node
/*
 * EXECUTION TOOL — not a schema reference.
 * Run this script as-is to PERFORM this task when you do not need to write
 * application code; side-effect rules still apply (billable/destructive calls
 * need explicit user approval). Do NOT copy its payload literals or logic into
 * a new codebase as if they were the API spec — for payload shape, load the
 * canonical developers.sinch.com docs linked from ../../SKILL.md instead.
 */
/**
 * Update an existing webhook.
 *
 * Usage:
 *   node update_webhook.js --webhook-id WEBHOOK_ID [options]
 *
 * Environment variables:
 *   SINCH_PROJECT_ID  - Your Sinch project ID (required)
 *   SINCH_KEY_ID      - Your access key ID (required)
 *   SINCH_KEY_SECRET  - Your access key secret (required)
 *   SINCH_REGION      - API region: us, eu, or br (default: us)
 *   SINCH_WEBHOOK_SECRET - New HMAC secret (used only with --set-secret)
 *   SINCH_WEBHOOK_OAUTH_CLIENT_SECRET - New OAuth2 client secret (required with --oauth-client-id)
 *
 * Secrets are read only from the environment so they never appear in process
 * arguments or shell history.
 *
 * Options:
 *   --webhook-id      - Webhook ID to update (required)
 *   --target          - New webhook target URL (HTTPS required, max 742 chars)
 *   --triggers        - New comma-separated list of triggers
 *   --set-secret      - Replace the HMAC secret with SINCH_WEBHOOK_SECRET (flag, no value)
 *   --clear-secret    - Remove the HMAC secret (flag, no value)
 *   --oauth-client-id - New OAuth2 client ID
 *   --oauth-endpoint  - New OAuth2 token endpoint URL
 *   --clear-oauth     - Remove OAuth2 configuration (flag, no value)
 *
 * Example:
 *   node update_webhook.js \
 *     --webhook-id 01WEBHOOK123456789 \
 *     --target https://new-url.com/webhook \
 *     --triggers MESSAGE_INBOUND,MESSAGE_DELIVERY,EVENT_INBOUND
 */

const client = require("../common/sinch_client.cjs");
const { parseArgs } = require("node:util");

const projectId = client.getEnv("SINCH_PROJECT_ID");
const keyId = client.getEnv("SINCH_KEY_ID");
const keySecret = client.getEnv("SINCH_KEY_SECRET");
const region = client.getEnv("SINCH_REGION", "us");

function parseArguments() {
  const { values } = parseArgs({
    options: {
      "webhook-id":          { type: "string" },
      "target":              { type: "string" },
      "triggers":            { type: "string" },
      "set-secret":          { type: "boolean", default: false },
      "clear-secret":        { type: "boolean", default: false },
      "oauth-client-id":     { type: "string" },
      "oauth-endpoint":      { type: "string" },
      "clear-oauth":         { type: "boolean", default: false },
      "help":                { type: "boolean" },
    },
  });

  if (values.help) {
    console.log("Usage: node update_webhook.cjs --webhook-id WEBHOOK_ID [--target URL] [--triggers TRIGGERS] [--set-secret | --clear-secret] [--oauth-client-id ID --oauth-endpoint URL | --clear-oauth]");
    console.log("Secrets come from SINCH_WEBHOOK_SECRET and SINCH_WEBHOOK_OAUTH_CLIENT_SECRET.");
    process.exit(0);
  }

  if (values["set-secret"]) {
    values.secret = process.env.SINCH_WEBHOOK_SECRET;
    if (!values.secret) {
      console.error("Error: --set-secret requires SINCH_WEBHOOK_SECRET in the environment");
      process.exit(1);
    }
  }
  if (values["oauth-client-id"]) {
    values["oauth-client-secret"] = process.env.SINCH_WEBHOOK_OAUTH_CLIENT_SECRET;
    if (!values["oauth-client-secret"] || !values["oauth-endpoint"]) {
      console.error("Error: --oauth-client-id requires --oauth-endpoint and SINCH_WEBHOOK_OAUTH_CLIENT_SECRET");
      process.exit(1);
    }
  }

  if (!values["webhook-id"]) {
    console.error("Error: --webhook-id is required");
    process.exit(1);
  }

  if (values.target && values.target.length > 742) {
    console.error("Error: --target URL exceeds 742 character limit");
    process.exit(1);
  }

  if (values.target && !values.target.startsWith("https://")) {
    console.error("Error: --target must use HTTPS protocol");
    process.exit(1);
  }

  return values;
}

function buildUpdatePayloadAndMask(params) {
  const payload = {};
  const updateMask = [];

  if (params.target) {
    payload.target = params.target;
    updateMask.push("target");
  }

  if (params.triggers) {
    payload.triggers = params.triggers.split(",").map((t) => t.trim());
    updateMask.push("triggers");
  }

  if (params.secret) {
    payload.secret = params.secret;
    updateMask.push("secret");
  } else if (params["clear-secret"]) {
    payload.secret = "";
    updateMask.push("secret");
  }

  if (
    params["oauth-client-id"] &&
    params["oauth-client-secret"] &&
    params["oauth-endpoint"]
  ) {
    payload.client_credentials = {
      client_id: params["oauth-client-id"],
      client_secret: params["oauth-client-secret"],
      endpoint: params["oauth-endpoint"],
      token_request_type: "BASIC",
    };
    updateMask.push("client_credentials");
  } else if (params["clear-oauth"]) {
    payload.client_credentials = null;
    updateMask.push("client_credentials");
  }

  if (updateMask.length === 0) {
    console.error("Error: No fields specified to update");
    console.error(
      "Use one or more of: --target, --triggers, --set-secret, --oauth-*, or --clear-*",
    );
    process.exit(1);
  }

  return { payload, updateMask };
}

async function updateWebhook() {
  try {
    const params = parseArguments();
    const update = buildUpdatePayloadAndMask(params);

    console.log("Updating webhook:", params["webhook-id"]);
    console.log("Fields to update:", update.updateMask.join(", "));

    const token = await client.getAccessToken(keyId, keySecret);
    const baseUrl = client.apiUrl(
      region,
      projectId,
      `webhooks/${params["webhook-id"]}`,
    );
    const url = `${baseUrl}?update_mask=${update.updateMask.join(",")}`;
    const body = JSON.stringify(update.payload);

    const result = await client.httpRequest(
      url,
      {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      },
      body,
    );

    console.log("\nWebhook updated successfully!");
    console.log("Full response:", JSON.stringify(client.redact(result), null, 2));
  } catch (error) {
    console.error("\nError updating webhook:");
    console.error(error.message);
    process.exit(1);
  }
}

updateWebhook();
