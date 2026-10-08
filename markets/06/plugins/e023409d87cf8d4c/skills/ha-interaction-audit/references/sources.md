# Official references

Core references checked September 9, 2026; actionability, clock control, and HA WebSocket references rechecked during the September 10 expansion. Recheck the relevant APIs against installed versions before execution. These sources explain APIs and testing mechanics; they do not prove any particular dashboard passes.

- [Home Assistant custom cards](https://developers.home-assistant.io/docs/frontend/custom-ui/custom-card/): custom element configuration, HA property updates and editor integration.
- [Home Assistant frontend data](https://developers.home-assistant.io/docs/frontend/data/): `hass` data and service/WebSocket/REST access surfaces to model.
- [Home Assistant WebSocket API](https://developers.home-assistant.io/docs/api/websocket/): message types, service calls, subscriptions and results.
- [Browserless Function API](https://docs.browserless.io/rest-apis/function): executable function, context payload and structured return shape. Confirm local add-on version and limits independently.
- [Playwright actionability](https://playwright.dev/docs/actionability): actionability checks and limitations of forced actions.
- [Playwright network](https://playwright.dev/docs/network): HTTP mocking and the service-worker interception caveat.
- [Playwright emulation](https://playwright.dev/docs/emulation): viewport, touch, locale and other emulated settings.
- [Playwright BrowserContext](https://playwright.dev/docs/api/class-browsercontext): context isolation and version-specific WebSocket routing facilities.
- [Playwright Clock](https://playwright.dev/docs/clock): fixed time, installed timer control, elapsed advancement, suspension-style jumps and installation order. Use a real-time smoke test as separate evidence.
- [Playwright Trace Viewer](https://playwright.dev/docs/trace-viewer): action traces and snapshots as diagnostic evidence, with sensitive-data handling appropriate to their contents.

Follow the current environment's browser-control instructions even when a documentation example uses another executable surface. Do not introduce credentials, dependencies or live actions merely to match a tutorial.
