# Proposed obligacje.io walkthrough

**Status: not executed.** This is a public, reusable recording outline, not a
record of observed behavior. Version 0.1.6 uses the current catalog scope and
generic bond-data service description. Run and record these checks for the
release under review; historical protocol checks or an existing listing do not
prove acceptance of a new revision. No recording URL is bundled here.

Use an ordinary obligacje.io account and the host application's standard
connection flow, without operator grants, special entitlements or an auth
bypass. Use public bond information and a focused sample question. Keep
passwords, verification codes, OAuth authorization codes, access/refresh tokens,
cookies, email addresses and unrelated conversations out of the recording.
Dedicated reviewer-account access, if required later, belongs only in the
provider's secure review form, never in a distributed file or public video.

1. Open the public [setup guide](https://www.obligacje.io/en/integrations).
   Explain account sign-in, consent and existing usage limits. Show
   the connection flow documented for the selected client. State the exact
   host and version actually tested; do not infer acceptance for other clients.
2. Sign in through the browser and show the consent screen without revealing
   credentials or codes. Explain the separate catalog-read and assistant-turn
   permissions. Record the real consent outcome and connected-app entry in
   obligacje.io account controls.
3. Run the first four positive cases in [review-cases.json](./review-cases.json):
   a filtered catalog query with full-match statistics and a matching website
   link; issuer discovery and selected series detail; cached document evidence
   with source/page citations; and published knowledge text. For the English
   knowledge case, show `locale: en` on search, read and pagination and the
   returned direct English article link. Show real tool
   invocations and results, including missing values, truncation, source gaps
   or failures. Counts and sample bonds may change; never substitute fabricated
   fixed results.
4. Run the focused `ask_assistant` case once, in Polish. Show the informational
   answer, citations or explicit source limitations, and its private account
   conversation. Explain that this request consumes the existing assistant
   allowance and should not be automatically retried after a timeout. Mask
   unrelated account details.
5. Run the three proposed negative cases. Show that unrelated writing,
   personalized investment/trading and unsupported brokerage-account
   creation requests do not
   invoke the integration. Record unexpected activation as a failed case,
   not as a pass.
6. Revoke the demonstrated connection in obligacje.io account controls. Use
   the previous connection for a harmless catalog read and show the resulting
   denial. Reconnect only through the normal host consent flow if another
   test is needed. Do not bypass denied access or expose token values.
7. Close with the scope established by the returned catalog data,
   cited source facts and explicit gaps; answers may contain errors and
   are not investment advice. Show the [support page](https://www.obligacje.io/en/integrations#support),
   [privacy policy](https://www.obligacje.io/en/privacy-policy) and
   [terms](https://www.obligacje.io/en/terms).

After execution, record the tested host, date, package version, individual
observed outcomes and any failures in the actual acceptance record. Only then
prepare reviewer-accessible evidence and a real accessible walkthrough URL.
Keep the proposed cases marked pending until that evidence exists. A ZIP upload
or repository publication alone is not acceptance of the OAuth flow or evidence
of a live directory listing.
