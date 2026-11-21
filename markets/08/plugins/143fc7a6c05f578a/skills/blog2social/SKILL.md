---
name: blog2social
description: Use this skill when users want to inspect supported social networks, view connected Blog2Social accounts, check network-specific publishing requirements, connect or disconnect social accounts, publish social media content immediately, retrieve available performance insights for their own published posts, or check account usage and credit balances.
---

# Blog2Social workflow

Use the user's individual OAuth connection. Let the host manage OAuth and credentials. Never ask for passwords or copy access tokens into tool arguments or messages.

On authentication errors, guide the user to reconnect using the host's supported account authorization flow.

Use only discovered MCP tools and their actual schemas. Never invent tool names, parameters, IDs, or response fields.

Select the account the user intended, asking for clarification when the target is ambiguous.

## Supported networks and connected accounts

Use `networks.list` to retrieve social networks available to the authenticated Blog2Social API user.

This tool returns available network IDs and supported account types, including profiles, pages, and groups.

Use `connections.list` to retrieve the user's connected social media accounts.

Identify the correct account using the returned network, account type, display name, and `client_user_network_id`.

Do not confuse available networks with connected accounts. Do not guess network IDs, account IDs, or account types.

## Connecting and disconnecting accounts

Use `connections.add` when the user wants to connect an account.

First call `networks.list` to obtain the required `network_id` and `network_type_id`.

The supported network types are:
- 0 for profile
- 1 for page
- 2 for group

The tool starts OAuth authorization and returns an `auth_link` and its expiration time.

The user must open the link and complete authorization. Do not claim that an account is connected before authorization has been completed and the connection is confirmed.

Pinterest also requires an active custom app assigned to the API service.

Use `connections.remove` only when the user explicitly requests disconnection of a specific account.

First call `connections.list` to identify the intended connection and its `client_user_network_id`.

Disconnecting an account is a destructive action. Confirm the intended account when necessary. Explain that the account must be connected again before it can be used for publishing.

## Publishing requirements

Use `networks.properties` before publishing to inspect the requirements and capabilities of the selected social network and account type.

Returned properties may include supported media formats, video support, and character limits.

Capabilities and restrictions vary by network and account type. Follow the actual returned properties. Do not assume that a format supported by one network is supported by another.

This tool does not publish content or guarantee acceptance by the social network.

## Publishing posts

Publishing content requires explicit user authorization for the concrete content and destination.

Use `posts.publish_post` when the user explicitly asks to publish content immediately.

This tool publishes content directly to the connected social account identified by `client_user_network_id`. It does not create a draft or schedule a post for later publication.

Use the actual tool schema and the following post format values:

- `postFormat` 0 for text or link.
- `postFormat` 1 for image.
- `postFormat` 2 for video.

Image and video posts require `mediaObjects` with the matching `IMAGE` or `VIDEO` type and a publicly accessible HTTP or HTTPS URL.

Do not invent media URLs, account details, or unsupported arguments.

Every publishing request targets the account identified by its `client_user_network_id`.

Use separate publishing calls for separate accounts only when the user has explicitly selected and authorized each destination.

Before publishing:

1. Verify the intended connected account with `connections.list`.
2. Check the network and account type requirements with `networks.properties`.
3. Check available credits with `credits.balance` when necessary.
4. Verify that the user has explicitly authorized the exact content and destination.

Do not publish immediately when the user requests publication at a future date or time.

## Published post insights and analytics

Use `posts.insights` when the user requests performance insights for their own published social media posts.

This tool retrieves the latest available performance insights for a specific published post. It requires the public `publish_url` returned after a successful `posts.publish_post` operation.

Only retrieve insights for posts belonging to the authenticated user's own Blog2Social account. Do not retrieve or report insights for posts belonging to other users.

Insights are available only for supported social networks and account types with tracking enabled.

Available metrics depend on the social network, account type, published post, tracking availability, and data returned by Blog2Social.

Depending on the network and post, returned metrics may include:

- Impressions and reach.
- Likes and reactions.
- Comments and shares.
- Engagement metrics.

Not all metrics are available for every network or post. Do not promise that a particular metric will be returned.

Follow the actual `posts.insights` input schema. Use the `publish_url` from the successful publishing response. Do not invent filters, parameters, or response fields.

Report only metrics and credit information actually returned by the endpoint.

Identify the social network and published post whenever this information is available.

Do not interpret missing metrics as zero. Do not calculate or invent missing performance data.

The request may consume API credits. Consider the potential credit cost before requesting insights and avoid unnecessary repeated requests.

If the endpoint returns an error or no data, explain the limitation accurately without fabricating results.

## Video publishing status

When `posts.publish_post` returns a `video_token`, use `videos.status` with that token to check the publication status.

Possible statuses are:

- `pending`
- `failed`
- `successful`

The response may include a `publish_url` after successful publication.

If the status is `pending`, check again later. Do not report successful publication until the returned status confirms it.

Only use `posts.insights` after successful publication has been confirmed and a valid `publish_url` is available.

## Account usage and credits

Use `credits.balance` to retrieve the current credit balance of the authenticated Blog2Social API account.

Report the returned balance accurately. Do not describe it as a personal balance unless the server establishes ownership.

Use `account.overview` when the user asks for an account-level overview of Blog2Social credit usage.

This tool returns the current balance and aggregated usage totals grouped by day, endpoint, and network.

The optional `days` parameter must be an integer between 1 and 30. If omitted, the endpoint default applies.

The results describe aggregated account usage. They do not provide performance metrics for individual published posts. Use `posts.insights` for individual post performance.

Do not confuse account usage statistics with social media performance analytics.

## Future publishing requests

The current MCP `posts.publish_post` tool publishes immediately and does not provide a scheduling parameter.

For future publishing requests, use available ChatGPT scheduling features only when the environment supports them and can invoke the authorized Blog2Social connection when the task runs.

Establish the content, destination, date, time, and timezone from the user's request.

Do not invent a scheduling parameter or call `posts.publish_post` immediately for a future request.

Report scheduling success only after the host confirms task creation. Distinguish a scheduled reminder from an automatic publishing task.

If automatic scheduled publishing is not supported, explain the limitation and offer a draft or reminder where supported.

## Publication result verification

Check every publishing result, including all returned error fields and `b2s_error_code`.

Summarize partial successes and failures separately.

Use returned `publish_url` and `video_token` only when present and relevant.

Do not claim publication based on HTTP success alone.

Do not automatically retry publishing after uncertain outcomes, as this may create duplicate posts.

For video posts, verify the final publication status using `videos.status` and the returned `video_token`.

## Unsupported operations

The current tool set does not expose private messaging, editing published posts, or deleting published posts.

Do not claim that these actions have been completed.

Video uploading is handled through `posts.publish_post` with the required video media object. `videos.status` checks the publication status of an existing video submission; it does not upload videos independently.

Payments and credit purchases are not handled through the MCP tools. Users manage subscriptions and purchases separately through Blog2Social.

Never request payment card details or claim to process purchases through this integration.