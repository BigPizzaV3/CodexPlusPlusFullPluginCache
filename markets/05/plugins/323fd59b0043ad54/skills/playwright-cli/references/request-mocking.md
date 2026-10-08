# Request Mocking

Intercept, mock, modify, and block network requests only on a public demo or a disposable local synthetic fixture whose exact origin and effect are authorized by the current request. Never intercept a real sign-in, payment, health, education, private-message, admin, or personal-account endpoint. Do not inspect or materialize cookies, authorization headers, passwords, tokens, account identifiers, or an entire request body that may contain them. Reproduce the minimum non-sensitive field in a synthetic endpoint instead.

## CLI Route Commands

```bash
# Mock with custom status
playwright-cli route "**/*.jpg" --status=404

# Mock with JSON body on a synthetic fixture
playwright-cli route "**/api/test-items" --body='[{"id":"TEST_ITEM_1","label":"TEST_LABEL"}]' --content-type=application/json

# Mock with custom headers
playwright-cli route "**/api/data" --body='{"ok":true}' --header="X-Custom: value"

# Remove one synthetic header from the exact test endpoint
playwright-cli route "**/api/test-items" --remove-header=X-TEST-TRACE

# List active routes
playwright-cli route-list

# Remove a route or all routes
playwright-cli unroute "**/*.jpg"
playwright-cli unroute
```

## URL Patterns

```
**/api/test-items      - Exact synthetic path match
**/api/*/details       - Wildcard in path
**/*.{png,jpg,jpeg}    - Match file extensions
**/search?q=*          - Match query parameters
```

## Advanced Mocking with run-code

For conditional responses, narrowly scoped synthetic request-field inspection, response modification, or delays:

### Conditional Response Based on Request

```bash
playwright-cli run-code "async page => {
  await page.route('**/api/test-preferences', route => {
    const body = route.request().postDataJSON();
    if (body.theme === 'TEST_DARK') {
      route.fulfill({ body: JSON.stringify({ applied: true }) });
    } else {
      route.fulfill({ status: 400, body: JSON.stringify({ error: 'TEST_UNSUPPORTED_THEME' }) });
    }
  });
}"
```

### Modify Real Response

```bash
playwright-cli run-code "async page => {
  await page.route('**/api/test-plan', async route => {
    const response = await route.fetch();
    const json = await response.json();
    json.testFeatureEnabled = true;
    await route.fulfill({ response, json });
  });
}"
```

### Simulate Network Failures

```bash
playwright-cli run-code "async page => {
  await page.route('**/api/offline', route => route.abort('internetdisconnected'));
}"
# Options: connectionrefused, timedout, connectionreset, internetdisconnected
```

### Delayed Response

```bash
playwright-cli run-code "async page => {
  await page.route('**/api/slow', async route => {
    await new Promise(r => setTimeout(r, 3000));
    route.fulfill({ body: JSON.stringify({ data: 'loaded' }) });
  });
}"
```
