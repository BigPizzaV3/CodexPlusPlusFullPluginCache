# Peptide Reconstitution Calculator by Peptara Labs

Educational ChatGPT plugin, version 0.5.0. The canonical calculator website is publicly accessible at https://peptara-calculator.vercel.app/, with its MCP endpoint at https://peptara-calculator.vercel.app/mcp. A genuine private ChatGPT connection has now exercised that remote endpoint, all five positive and three negative review cases, and explicit Share with chat delivery. The actual Peptara Labs logo was visually verified in the private plugin icon, calculator header, and decorative vial. Opus returned HOSTING GO for the hosting changes. The public directory draft is on another account and has not been submitted for review or published.

## Use the local calculator

Open `dist/calculator.html` in a browser, or run the local preview:

```sh
npm ci --ignore-scripts
npm run build
npm start
```

Open http://127.0.0.1:4317. The MCP endpoint is http://127.0.0.1:4317/mcp.
Node.js 24 is required for the server. The standalone HTML needs no installation.

Enter a mass in mg or mcg and a final total solution volume in mL or microliters. Calculate to see mg/mL, mcg/mL, the formula, and rounding status. Changing units converts the value to preserve the quantity. Editing mass or final-volume values clears the prior result. Reset clears both values and the optional syringe-size reference. Choose U-100 (0.3, 0.5, or 1 mL) or mL-marked (1, 3, or 5 mL) to update the syringe reference. These are capacity examples, not device recommendations. Changing scale clears the reference selection. A 1 mL example is shown when no capacity is selected. The vial diagram does not show a preparation procedure.

The interface uses the original Peptara Labs logo, an animated decorative 3D vial, and the brand charcoal, gold, and warm-white palette. Pause motion stops the decorative movement; system reduced-motion preferences take precedence. Logo assets are embedded, so the calculator does not request remote images.

This build calculates concentration only. It does not choose quantities, recommend fluids or doses, convert concentration into syringe markings, or provide preparation or administration instructions. It assumes the entire entered mass is dissolved in the entered final volume. Final solution volume can differ from the amount of liquid added.

## ChatGPT integration

The package contains two read-only MCP tools:

| Tool | Behavior |
| --- | --- |
| `open_concentration_calculator` | Opens an empty interactive component. Declares a conversation-panel entrypoint. |
| `calculate_concentration` | Validates supplied values and returns the formula, concentration, and interactive component. |

The UI uses the official MCP Apps bridge. It can receive tool results and explicitly share a result with the active chat. The calculator still works without a host connection.

The current `mcp.json` targets `https://peptara-calculator.vercel.app/mcp`. The canonical deployment is publicly accessible without Vercel sign-in. The live private ChatGPT connection uses this remote endpoint. Its calculations, embedded interface, syringe references, Reset, and explicit sharing have been exercised. A unique fixture entered only in the component, 17.2 mg / 4 mL = 4.3 mg/mL, was shared with `updateModelContext` and then correctly repeated by ChatGPT. The source has no automatic sharing call before the explicit Share action. The host displayed CSP enforcement as off, so these tests do not establish production directory CSP enforcement or complete public-release integration.

The public v0.5.0 draft and business-verification work belong to the original PeptaraLabs organization on another account, according to Ken. The current ChatGPT account is only for private walkthrough testing. User screenshots show Education & Research, the corrected Peptara Labs website/support URLs, MCP Configured, Metadata No Issues, and skill Checks passed. The domain challenge is publicly served with the exact supplied value. The final manifest supplies `demo_recording_url`: https://peptara-calculator.vercel.app/review/demo-20261004.mp4. This genuine 306.833-second walkthrough is deployed and anonymously accessible as video/mp4, with byte-exact content, range requests, browser playback, and seeking verified. The original public draft will receive this URL when Ken uploads the final ZIP. Ken will upload the final ZIP himself from the original account. Registered PeptaraLabs LLC is user-reported; the official publisher-verification result, submission, approval, and publication remain unconfirmed or pending. See [public submission](docs/PUBLIC-SUBMISSION.md).

## Verification

```sh
npm run verify
```

This builds the component, runs arithmetic and protocol integration tests, and checks package references and source isolation. Real SDK clients test both HTTP and stdio transports. The test values are synthetic arithmetic fixtures, not suggested amounts.

Version 0.5.0 passed 40 tests with zero failures and eight anonymous public checks without authentication or a bypass: root UI hash, health, privacy, support, MCP initialization, tool discovery, calculation, and embedded UI bytes. These public checks are separate from eight earlier authenticated checks of the protected deployment. Ken waived the GLM gate for this release. The independent Opus review returned HOSTING GO with four non-blocking findings; this is not directory approval or a complete production ChatGPT integration test. See the [Opus release review](docs/OPUS-RELEASE-REVIEW.md) and [verification record](docs/VERIFICATION.md) for scope and limitations.

The subsequent domain-challenge deployment passed three anonymous checks: the challenge returned HTTP 200 with the exact 43-character value and no newline, health reported 0.5.0, and MCP discovery returned the two expected tools. These checks established challenge hosting and endpoint availability. Later user screenshots establish the portal's MCP Configured status. The subsequent private ChatGPT tests below add actual remote-host evidence; complete directory testing remains separate.

The subsequent private ChatGPT walkthrough executed five positive and three negative cases against the canonical remote MCP endpoint. Model responses were correct, including 750 mcg / 150 microliters = 5 mg/mL and 13.7 mg / 2.5 mL = 5.48 mg/mL. The 10 mg / 3 mL model response and component values were correct. At the recorded narrow chat width, the last digit of the large 12-significant-digit result wraps onto a second line; the smaller formula remains readable. This is a presentation limitation, not an arithmetic discrepancy. Changing the equipment reference from a 0.5 mL U-100 syringe to a 3 mL marked syringe left the concentration unchanged, and Reset cleared the form. Explicit Share delivery passed the unique-fixture check described above. These synthetic examples establish arithmetic and interaction behavior, not preparation suitability or dosing advice. Remaining checks include production CSP enforcement, mobile layout, motion controls, and CTA destinations in the directory-installed host.

## Package layout

| Location | Purpose |
| --- | --- |
| `plugin.json` | Portable plugin identity and OpenAI display metadata |
| `mcp.json` | Public HTTPS MCP connection target |
| `skills/peptide-concentration/SKILL.md` | Invocation and educational-scope instructions |
| `src/calculator.mjs` | Shared decimal math and input validation |
| `src/mcp-server.mjs` | Tool definitions and embedded UI resource |
| `src/http.mjs`, `src/stdio.mjs` | HTTP and local process transports |
| `web/` | Editable interface source |
| `dist/calculator.html` | Self-contained browser and ChatGPT component |
| `test/` | Arithmetic, validation, and MCP integration tests |

## Privacy and runtime behavior

No accounts, analytics, cookies, persistent calculation history, or model API calls are implemented. The component calculates locally. ChatGPT tool calls contain the supplied numeric inputs. The Share with chat button explicitly sends the displayed result into the conversation. ChatGPT's own data policies still apply.

The local server binds to loopback by default, checks Host and Origin, limits request bodies, and does not log calculation inputs. It is an unauthenticated, stateless numeric service. Public deployment uses the dedicated Vercel project and HTTPS origin allowlist. Vercel runtime logs are retained for 30 days under the verified Pro with Observability Plus configuration. Other provider records follow their applicable policies. Support correspondence follows Peptara Labs' existing purpose-based or legally required retention criteria, followed by deletion or anonymization; no fixed numeric support period is claimed. These distinctions are published in the calculator's `/privacy` notice, and its served content was verified.

## Sources

- [IUPAC: mass concentration](https://goldbook.iupac.org/terms/view/M03713), mass divided by the mixture's volume.
- [OpenAI: MCP server and UI quickstart](https://developers.openai.com/plugins/build/app-quickstart).
- [OpenAI: optional UI](https://developers.openai.com/plugins/build/chatgpt-ui).
- [OpenAI: plugin extensions](https://developers.openai.com/plugins/build/extensions).
- [OpenAI: packaging](https://developers.openai.com/plugins/build/plugins).

Documentation checked October 4, 2026. This calculator has not been medically validated or approved by OpenAI. See the release record for hosting and directory status.
