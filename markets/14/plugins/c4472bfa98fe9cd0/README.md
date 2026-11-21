# TabStickers — private preview draft

Publisher identity: select the verified **Business — TabStickers** identity in
the OpenAI upload dialog. Manifest text alone does not establish verification.

This package is for draft validation and controlled testing. Uploading it is not
submission for review or publication. It does not enable public subscriber access.

## What it connects

TabStickers is a CRM for real estate professionals. This connection supports
explicitly requested client/profile updates, notes, personal and client-linked
tasks, professional Contacts, client Resources and read-only briefings.

Google Calendar is optional and must be separately connected in TabStickers
Settings. With the user's approval, the connection reads, creates and edits
events on the linked account's primary calendar. Overlaps require confirmation.
Ordinary CRM task edits never modify Google Calendar automatically.

Client and note deletion, Calendar deletion, guest changes, outbound messages,
payments and bulk-client actions are not exposed.

## Sign-in and permissions

The package preconfigures the public OAuth client and endpoints. No client
secret, access token, password, customer record, identity document or private
verification code is included. Sign in through the TabStickers authorization
page; users should not manually enter OAuth settings.

Only the owner and explicitly approved private testers can authorize access.
Each connection is limited to the signed-in user's authorized account data.
Host plan and installation availability are controlled by OpenAI.

## Before submission

Complete the dashboard's MCP connection, domain challenge and automated checks.
Use only the exact domain challenge provided by OpenAI; this ZIP contains none.
Reviewer account access must be entered in the portal's secure review fields,
never in this package. Use dedicated synthetic review data, not customer data.

The package includes five positive and three negative review scenarios in its
review metadata. They describe prompts, tools, prerequisites and expected
outcomes, not completed-test results. Only run them against dedicated fictional
review data. The Calendar case explicitly creates and moves a test event; the
overlap negative case then refers to that event and requires the reviewer to
decline the confirmation. These actions are not performed by uploading the ZIP.

An accessible functional walkthrough is still required. The Google Calendar
verification video is not automatically a complete OpenAI plugin-review
walkthrough. No video URL or unverified test-completion claim is supplied here.

Google Calendar review and public subscriber readiness remain separate from
OpenAI business identity verification. Do not submit or publish until the
remaining readiness checks have been completed.

Website: https://tabstickers.com

Privacy and contact information: https://tabstickers.com/privacy

Terms: https://tabstickers.com/terms

Support: help@tabstickers.com
