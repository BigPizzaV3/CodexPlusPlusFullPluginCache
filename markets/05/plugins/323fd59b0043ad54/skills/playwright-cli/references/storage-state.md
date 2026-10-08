# Synthetic Storage-State Testing

Manage cookies, localStorage, sessionStorage, and saved browser state only in a newly created disposable test profile containing synthetic values. Never inspect, list, export, copy, persist, or restore a user's real signed-in browser state, cookies, passwords, tokens, account identifiers, or existing profile.

## Preconditions

Continue only when all of these are true:

- the user requested a storage-specific test;
- the session and profile were created for this test and have never signed in to a real account;
- the origin is a local fixture or an explicitly synthetic `.invalid` placeholder;
- every value is visibly synthetic and begins with `TEST_` where practical;
- the state file is in a task-specific temporary directory outside the plugin, repository, and public outputs.

If any condition is uncertain, use an in-memory session without storage inspection. For profile isolation, read [session-management.md](session-management.md).

## Save and restore one synthetic state

```bash
# Use only after creating synthetic values in the isolated test profile
playwright-cli state-save TEST_SYNTHETIC_STATE.json

# Restore only into another disposable synthetic test session
playwright-cli state-load TEST_SYNTHETIC_STATE.json
playwright-cli open https://example.invalid
```

Never save a state after real authentication. A state file must not be used to transfer login access between sessions, machines, accounts, tools, or people.

## Synthetic state shape

This redacted shape illustrates the fields without supplying real authentication data:

```json
{
  "cookies": [
    {
      "name": "TEST_COOKIE_NAME",
      "value": "TEST_COOKIE_VALUE",
      "domain": "example.invalid",
      "path": "/",
      "expires": 1893456000,
      "httpOnly": true,
      "secure": true,
      "sameSite": "Lax"
    }
  ],
  "origins": [
    {
      "origin": "https://example.invalid",
      "localStorage": [
        { "name": "TEST_THEME", "value": "TEST_DARK" },
        { "name": "TEST_USER", "value": "TEST_USER_VALUE" }
      ]
    }
  ]
}
```

## Synthetic cookies

Create and remove only cookie names generated for the same disposable test. Do not list or retrieve cookies from any pre-existing profile.

```bash
playwright-cli cookie-set TEST_COOKIE_NAME TEST_COOKIE_VALUE --domain=example.invalid --path=/ --httpOnly --secure --sameSite=Lax
playwright-cli cookie-delete TEST_COOKIE_NAME
```

For multiple synthetic cookies:

```bash
playwright-cli run-code "async page => {
  await page.context().addCookies([
    { name: 'TEST_SESSION', value: 'TEST_SESSION_VALUE', domain: 'example.invalid', path: '/', httpOnly: true },
    { name: 'TEST_PREFERENCE', value: 'TEST_DARK', domain: 'example.invalid', path: '/' }
  ]);
}"
```

## Synthetic localStorage

Operate only on explicit `TEST_` keys created by the current test. Avoid `localstorage-list` and broad exports because they can reveal unrelated data. Use `localstorage-clear` only in a confirmed empty disposable profile.

```bash
playwright-cli localstorage-set TEST_THEME TEST_DARK
playwright-cli localstorage-get TEST_THEME
playwright-cli localstorage-delete TEST_THEME
```

For several explicit synthetic values:

```bash
playwright-cli run-code "async page => {
  await page.evaluate(() => {
    localStorage.setItem('TEST_THEME', 'TEST_DARK');
    localStorage.setItem('TEST_USER', 'TEST_USER_VALUE');
    localStorage.setItem('TEST_EXPIRY', String(Date.now() + 3600000));
  });
}"
```

## Synthetic sessionStorage

Use exact keys generated for the current test. Do not list or export all sessionStorage values.

```bash
playwright-cli sessionstorage-set TEST_STEP TEST_3
playwright-cli sessionstorage-get TEST_STEP
playwright-cli sessionstorage-delete TEST_STEP
```

## Roundtrip example

```bash
# Step 1: create one synthetic preference on a synthetic origin
playwright-cli open https://example.invalid
playwright-cli localstorage-set TEST_THEME TEST_DARK
playwright-cli state-save TEST_SYNTHETIC_STATE.json

# Step 2: restore only in a new disposable synthetic session
playwright-cli state-load TEST_SYNTHETIC_STATE.json
playwright-cli open https://example.invalid
playwright-cli localstorage-get TEST_THEME
```

This tests serialization only; it does not represent authentication and must never be relabelled as login reuse.

## Cleanup and reporting

- Never commit, upload, publish, attach, or include the state file in a deliverable.
- Close the disposable test session before cleanup.
- Verify the exact resolved temporary file and profile paths, then remove only those task-specific artifacts with a recoverable deletion mechanism.
- Do not print storage contents in logs or final responses. Report only the tested synthetic key names and whether the roundtrip passed.
- If a real secret appears unexpectedly, stop, avoid copying it, delete the unshared temporary artifact, and report the exposure without repeating the value.
