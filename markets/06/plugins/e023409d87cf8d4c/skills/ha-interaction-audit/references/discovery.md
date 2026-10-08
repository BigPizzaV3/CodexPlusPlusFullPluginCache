# Discovery and source parity

## Establish the contract

Infer the target from context before asking questions. Identify symptoms, affected routes, last known good version, device/browser, whether changes are authorized, and excluded systems. Do not turn an audit into a whole-house upgrade.

Inventory needed capabilities: HA read access; dashboard/resource configuration; source files; automation/script definitions if relevant; browser execution; screenshots; configuration validation; logs/traces; recovery facilities. Read tool schemas and applicable HA best-practice guides before matching mutations. Do not assume every HA Admin installation exposes terminal, Browserless, file writes, or config check.

Inspect what an existing test command executes before using it. It may reference an obsolete runner or restart shared infrastructure. Do not infer safety from its name.

## Source manifest

| Field | Evidence needed |
| --- | --- |
| Target | Dashboard path, view/panel/card type and relevant configuration |
| Runtime | HA frontend/core version when available; engine and automation version |
| Mounted chain | Actual custom-element tag, safe loader, child component, shadow roots/iframes |
| Ordered resources | Resource ID, URL without secrets, content hash, type, load order and override role |
| Inline code | Exact extracted code, hash, config location; do not invent a disk filename |
| Dependencies | Loaded library versions, fonts/icons, modules and lazy imports |
| State owners | HA state, server data, local draft, route, storage, timer, restore callback |
| Requests | Observed service, WS command, REST/ingress route, notification/event surface |
| Environment | Viewport, DPR, touch, locale, timezone, theme, reduced motion |
| Transformations | Rewritten URLs, replaced ingress base, fixture shims and omitted dependencies |

Hash bytes, not labels alone. The source fingerprint covers the ordered list, relevant configuration and transformations. Keep separate adapter/suite hashes. Unknown parity prevents certification of the live dashboard.

Inspect the active DOM before choosing selectors. Large bundles may retain obsolete controls and unused patch layers. Prove runtime ownership with mounted tag, ordering, or non-mutating version markers. Do not edit `.storage` directly to bypass configuration tools.

## Capability-dependent execution

| Available | What can be established |
| --- | --- |
| Source only | Static findings and proposed reproductions, not executed interactions |
| Screenshots only | Appearance and some geometry, not typing/touch/focus correctness |
| Isolated browser + copied code | Frontend behavior against stated mock contracts |
| Authorized live browser | Read-only integration rendering and scoped interactions |
| Authorized real device | Specific tested native keyboard, touch, background and OS behavior |

For built-in cards, load the actual HA substrate or use a dedicated non-production HA instance. A handmade stand-in does not validate the real card. Ingress apps may need cookies, service workers, iframes or their own backend. Classify unsupported features as blocked instead of removing isolation.

New dependencies, access routes and account sessions must follow current platform rules. Do not scrape tokens from browser storage or copy credentials into fixtures, payloads, web-served assets, screenshots or logs.
