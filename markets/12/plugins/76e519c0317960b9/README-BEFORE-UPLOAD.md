# KnowWho CRM plugin package: what to do before uploading

Upload at https://platform.openai.com/plugins ("Upload new or existing plugin").
Zip the CONTENTS of this folder so plugin.json sits at the zip root.

## Must replace before upload

1. assets/icon.png, assets/logo.png, assets/screenshot-1.png
   Placeholders so the package validates. Replace with real ones.
   Icon and logo: square, at least 48x48 (use 512x512), PNG/JPEG/WebP/SVG, under 5 MiB.
   Screenshot: up to 4096px on a side.

2. review.demo_recording_url in plugin.json
   Required for MCP review. A screen recording walking through the five positive test cases
   on the demo account. Unlisted YouTube or Loom is fine. Reviewers want to see the tools run,
   so this is not the launch film.

3. The four listing URLs: websiteURL, supportURL, privacyPolicyURL, termsOfServiceURL
   All required for MCP review. Must be live HTTPS pages. Fix the paths if yours differ.

4. brandColor is a guess at the site orange. Swap for the real accent (2:1 contrast on white).

## Check

- mcp.json URL. Confirm https://mcp.knowwhocrm.com/ is the exact endpoint (some servers want /mcp).
  The URL cannot be changed after submission without contacting support.
- category "Business & Operations" (closest match; OpenAI has no Sales or CRM category).
- publication.countries [] means no country restriction.

## Not in the package (entered in the dashboard)

- Reviewer credentials (demo account email and password). The ZIP rejects test_credentials.
  Enter them under Metadata & Skills > Review information > Review details after upload.
- Reviewer sign-in instructions. Same place. Reuse the Anthropic test notes minus the Claude steps.

## Order of operations in the portal

1. Business verification for Khiliad (Settings > Organization > General). Needs an Owner.
2. Use a project with GLOBAL data residency, not EU.
3. Upload the ZIP. Fix any metadata findings, re-upload.
4. MCPs > Connect. Complete the domain challenge: serve the token as plain text at
   https://mcp.knowwhocrm.com/.well-known/openai-apps-challenge (public, no auth).
5. Authorise with the demo account when prompted (OpenAI keeps the token for review).
6. Wait for the tool scan. Annotations are already in place, so it should pass.
7. Enter reviewer credentials in Review details. Submit for review.

## After approval

Server tool changes are picked up by daily scans, no new ZIP.
Metadata, asset or skill changes need a new ZIP with a bumped version.
