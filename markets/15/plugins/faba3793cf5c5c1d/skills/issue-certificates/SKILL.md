---
name: issue-certificates
description: Issue, email and verify certificates with CertSeal. Use when the user wants to give certificates to people who attended a course, event or program, email those certificates, check how many certificates they can still issue, fix a recipient's details, or check whether a certificate is genuine.
---

# Issue certificates with CertSeal

CertSeal issues verifiable certificates for courses, events and programs the user runs. Every tool works in the one CertSeal workspace the user chose when connecting. Certificates are rendered from designs the user made in CertSeal; never describe them as AI-generated.

## Issuing certificates

1. **Find the batch.** A batch groups everyone who gets a certificate from one design, such as the attendees of one workshop. If the user names an existing batch, find it with `list_batches`. To start a new one, find the design with `list_designs`, then use `create_batch`. If the user doesn't say otherwise, the batch title becomes the course name, the organization's name the issuer, and the workspace's default email template is used.
2. **Collect the recipients.** You need each person's name and email address. Use only the names and addresses the user gives you; never guess or invent them. If the list is unclear, ask.
3. **Issue.** Use `issue_certificates`, up to 100 recipients per call. Issuing uses the workspace's certificate allowance; check it with `get_workspace_status` first if the user is issuing many.
4. **Report back** each recipient's certificate ID. Say clearly whether anything was emailed.

## Emailing certificates

- Only email when the user asks to. Issuing and emailing are separate steps.
- Use `list_recipients` to find who hasn't been emailed yet, then `send_certificate_emails`.
- Emails can't be recalled. Before sending, tell the user how many emails will go out and to whom.
- Sending needs the email permission the user chose when connecting. If it's missing, tell the user they can reconnect CertSeal and tick "Email certificates to recipients", or send the emails from the CertSeal app.
- AI apps can send up to 200 certificate emails per organization per day.

## Other tasks

- **Fix a recipient's name, email or details:** `update_recipient`.
- **Check a certificate:** `verify_certificate`, with the certificate ID (such as CERT-2026-003956-000001) or its link. It finds certificates issued from the connected workspace.
- **How many certificates are left:** `get_workspace_status`. Quote `canStillIssue`, the number that actually limits issuing.

## What CertSeal doesn't do

- It doesn't make certificates, diplomas or other documents in the name of an institution the user doesn't run.
- It can't change plans, billing or account settings; those are in the CertSeal app.
- It can't create or edit designs or email templates; the user does that in the CertSeal app.
