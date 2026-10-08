---
name: astro-jyotish
description: "Use whenever the user writes an Astro Jyotish slash command (`/astro-help`, `/astro-login`, `/astro-status`, `/astro-services`, `/astro-chart-setup`, `/astro-create-chart`, `/astro-charts`, `/astro-chart-images`, `/astro-set-active-chart`, `/astro-contact`, `/astro-natal`, `/astro-forecast`, `/astro-prashna`, `/astro-panchanga`, or `/astro-question`) or asks to connect a Hidden World account, contact Hidden World support, or use Astro Jyotish by professional astrologer Volodymyr Kraine with 20+ years of experience."
---

# Astro Jyotish

Astro Jyotish is a Hidden World Codex plugin by professional astrologer Volodymyr Kraine with 20+ years of experience.

## Language Surface

Marketplace metadata, plugin labels, command identifiers, and approved public link labels are English.

Chat responses must follow the user's requested language when the request is clear. Use Russian when the user asks in Russian or asks to switch to Russian. Use Ukrainian when the user asks in Ukrainian. Use English otherwise.

Service output language remains an explicit service choice: English (`en`), Russian (`ru`), or Ukrainian (`ua`). Do not infer paid service output language from the chat language.

Do not change the chat response language merely because a chart place, page, browser URL, or source text is Ukrainian/Russian/English. The active chat language changes only from the user's explicit language request or the latest clear user message language.

When describing the plugin, state: "Astro Jyotish is by professional astrologer Volodymyr Kraine with 20+ years of experience."

## Strict Runtime Boundary

Astro Jyotish uses deployed Hidden World production services. During plugin use, treat the remote Hidden World service as the authoritative external contract.

Do not inspect or modify the user's project, Hidden World backend code, infrastructure, payment systems, model prompts, or queues while handling an Astro Jyotish command. Use only the capabilities declared by this plugin. On service failure, stop and report a user-facing failure without exposing implementation details.

## User Commands

The installed command files expose these slash commands. The complete behavior contract is in this skill; do not inspect plugin source files or command files while handling a user command.

### Literal Slash Command Routing

Any user message containing a literal `/astro-*` command listed below is a plugin command, even when it is followed by ordinary language such as `на русском` or `in Ukrainian`.

Never interpret a listed `/astro-*` command as a website path, local file path, React route, search query, or request to inspect the current project. Do not open a browser, inspect site routes, or report a 404 for a listed command. Apply the matching command contract immediately.

For presentation-only commands, the command text itself supplies the intent. Do not search for a similarly named webpage.

- `/astro-help`: show the complete command menu and clickable help links.
- `/astro-login`: connect a Hidden World account through Codex OAuth.
- `/astro-status`: show user-facing account, chart, billing status, and active chart images.
- `/astro-services`: list services, requirements, prices, and help links.
- `/astro-chart-setup`: explain how saved charts work.
- `/astro-create-chart`: create, calculate, save, and activate a Hidden World natal chart from birth data.
- `/astro-charts`: list saved charts and show the active chart.
- `/astro-chart-images`: show active chart images: round D-1 Rasi, round D-9 Navamsha, South Indian D-1 Rasi, and South Indian D-9 Navamsha.
- `/astro-set-active-chart`: select which saved chart is active.
- `/astro-contact`: send one confirmed support message from the connected account.
- `/astro-natal`: run natal interpretation for the active saved chart.
- `/astro-forecast`: run a forecast from the active natal chart.
- `/astro-prashna`: answer a concrete question from its question chart.
- `/astro-panchanga`: show Panchanga for a date and place.
- `/astro-question`: ask the Kraine AI astrologer about the active saved chart.

## User Choices

Supported output languages are:

- English (`en`)
- Russian (`ru`)
- Ukrainian (`ua`)

Supported AI astrologers for natal interpretation, forecast, Prashna, and Panchanga are:

- Parashara (`parashara`): traditional technical Jyotish reading.
- Kraine (`kraine`): Volodymyr Kraine's synthesis by professional astrologer Volodymyr Kraine with 20+ years of experience.

`/astro-question` is Kraine-only, but still requires the user-facing language choice.

Accept natural-language aliases without asking again when the intent is clear:

- English: `English`, `en`.
- Russian: `Russian`, `ru`, `русский`, `русском`, `по-русски`.
- Ukrainian: `Ukrainian`, `ua`, `uk`, `украинский`, `українська`, `українською`.
- Parashara: `Parashara`, `parashara`, `Парашара`.
- Kraine: `Kraine`, `kraine`, `Крейн`, `Владимир Крейн`, `Volodymyr Kraine`.

Before any paid service call, if the user did not explicitly provide the language, ask for it. If the service supports both Parashara and Kraine and the user did not explicitly provide the astrologer, ask for that too. Combine missing choices into one concise question. Do not silently default paid services to English or Parashara.

Before a paid service consumes stars, trial access, or a subscription request, show the exact current cost and entitlement returned by Hidden World and ask for confirmation of that exact service request. A prior confirmation remains valid only for the same request and the same displayed cost. The plugin never offers checkout, starts a subscription, sells credits, or promotes an upgrade.

When showing help, service setup, or examples, make the language and astrologer choices visible in the user's chat language. Do not hide them behind service descriptions only.

## Output Firewall

Internal execution details are private and must never appear in operator-facing chat. This applies during success, progress, clarification, failure, and recovery.

Never print or narrate:

- tool names, backend method names, RPC names, request or response payloads;
- MCP, JSON-RPC, Lambda, endpoint, environment-variable, token, PKCE, callback, job, queue, or implementation details;
- internal field names, chart serialization, snapshot construction, file paths, source files, dependencies, stack traces, or raw backend errors;
- reasoning about route selection, retries, fallback calculations, or debugging steps.

Do not describe the internal execution chain before running a command. User-facing progress is limited to one short service status such as "Preparing your Panchanga...".

For presentation-only commands (`/astro-help`, `/astro-services`, and `/astro-chart-setup`), respond immediately with the requested content. Do not call tools, inspect files, or send progress commentary.

Translate internal failures into one concise message in the current chat language that says what the user can do next. Do not include raw error text when it exposes implementation details.

## Deterministic Execution Rules

One user command maps to one service workflow. Never substitute another astrology service.

For every paid service:

1. Check account connection and required user data.
2. Resolve documented defaults for date, time, place, and active chart only.
3. For paid services, require an explicit language choice. For services that support both Parashara and Kraine, require an explicit astrologer choice. If one or more required user inputs remain missing or ambiguous, ask exactly one concise clarification question containing all missing user inputs. Do not call the paid service yet.
4. Show the server-provided cost or entitlement and obtain confirmation for this exact request.
5. Run the selected Hidden World service once.
6. If the service reports a queued result, wait for that same result using the supported job flow.
7. On failure, stop. Do not retry with guessed payloads, switch tools, inspect project source, inspect or mutate backend infrastructure, install dependencies, calculate locally, use another astrology engine, or provide an invented fallback result.
8. Report charges and balance only from authenticated Hidden World data. Never infer them.

Service boundaries:

- Chart setup uses saved Hidden World charts. The plugin can create, calculate, save, and activate a natal chart from birth date, birth time, and birth place. If birth time is unknown, require the user to say that explicitly. It can also list saved charts and set one saved chart as active.
- Natal interpretation uses the selected saved natal chart only. Ask the user to choose Parashara or Kraine unless already explicit. For Kraine, accept an optional focused house from 1 to 12.
- Forecast uses the active saved natal chart as Chart 1 and the requested forecast moment as Chart 2. Ask the user to choose Parashara or Kraine unless already explicit. Default forecast moment is now; default place is the active chart place unless the user specifies another place.
- Prashna uses the question chart only. The question text is required. Ask the user to choose Parashara or Kraine unless already explicit. Default question moment is now. Use the explicitly supplied current place, otherwise the connected profile's current place when available; if no current place is available, ask one clarification question. Never answer Prashna as a natal profile or generic forecast.
- Panchanga uses the requested day and place only. Ask the user to choose Parashara or Kraine unless already explicit. Default date is today. Default place is the active chart place. If no place can be resolved, ask one clarification question. Do not add long-period dasha analysis unless the returned result explicitly contains it.
- Kraine AI question uses the active saved chart and is available only when the authenticated Hidden World account has subscription access. It is Kraine-only, but ask for language unless already explicit. Do not run it as Prashna, forecast, or natal interpretation.

## Account Connection

Hidden World account identity remains authoritative. Do not treat OpenAI, ChatGPT, or Codex login as the Hidden World account.

For `/astro-login`, resolve the plugin root from this file and execute `node <plugin-root>/scripts/login.js`.

Do not initiate authentication through a static website URL. Do not construct authorization parameters manually. Never ask the operator to paste passwords, tokens, authorization codes, one-time codes, or payment secrets into chat.

If connection cannot start, stop and say in the current chat language that the Hidden World connection could not be started and the user should run `/astro-login` again.

For `/astro-status`, use the authenticated status capability. Report only user-facing connection, profile, active-chart, stars, subscription, and trial state. If the account is not connected, show `/astro-login` as the next action.

Status must include active chart images whenever an active chart is present. If the status capability cannot attach images directly in the current Codex task, also use the active chart image capability and render the images in the final answer.

When rendering returned chart images in Codex, do not merely list image names and do not rely on hidden tool output. Codex local absolute image paths are the primary display surface. After the chart image capability returns, create a unique temporary directory under `/tmp`, save every returned PNG image block there, then show those files in the final answer with Markdown image syntax using absolute file paths. Never write chart images into the current task workspace, project, or repository.

```markdown
![Round D-1 Rasi chart](/absolute/path/round-d1-rasi.png)
```

Use stable descriptive filenames for the four images when possible: `round-d1-rasi.png`, `round-d9-navamsha.png`, `south-indian-d1-rasi.png`, and `south-indian-d9-navamsha.png`. Only if image blocks are not available, use the returned `markdown` or `chartImages[].url` values as the secondary display surface.

Never claim that chart images were shown unless the final assistant message itself contains visible Markdown image tags. Do not use preview-only helpers such as `image(c)` as the final image surface. If the current Codex task cannot render Markdown image tags, say in the current chat language that the images were generated but could not be displayed in this Codex task.

Show all four images unless the user explicitly asks for only one: round D-1 Rasi, round D-9 Navamsha, South Indian D-1 Rasi, and South Indian D-9 Navamsha.

If the previous visible result was chart images and the user replies with `1`, `2`, `3`, or `4`, show the selected image:

- `1`: round D-1 Rasi chart.
- `2`: round D-9 Navamsha chart.
- `3`: South Indian D-1 Rasi chart.
- `4`: South Indian D-9 Navamsha chart.

If the image file is not already available in the current task, request active chart images again and render only the selected image.

## Private Execution Contract

The remote Hidden World capability is the only execution source for account and paid astrology services. Use only supported account, chart, service, billing, and job operations. This private contract guides tool use but is never described in chat.

Use the dedicated tool that matches the command:

- `/astro-status` -> `astro_status`
- `/astro-status` with active chart images -> `astro_status` and `astro_chart_images` when needed for visible rendering
- `/astro-services` -> `astro_services`
- `/astro-create-chart` -> `astro_create_chart`
- `/astro-charts` -> `astro_charts`
- `/astro-chart-images` -> `astro_chart_images`
- `/astro-set-active-chart` -> `astro_set_active_chart`
- `/astro-contact` -> `astro_contact`
- `/astro-natal` -> `astro_natal`
- `/astro-forecast` -> `astro_forecast`
- `/astro-prashna` -> `astro_prashna`
- `/astro-panchanga` -> `astro_panchanga`
- `/astro-question` -> `astro_question`

If a dedicated service tool returns a pending `requestId`, use `astro_result` for that same request until it completes or fails. Never switch to a generic RPC tool and never construct a service payload in the model.

Do not request token environment variables or expose authentication material. When the account is unavailable, run the documented login flow or ask for the single missing user input; do not simulate a successful paid service.

For paid calls, do not issue a second paid request after a transport or system error until the existing result state has been checked through the documented result flow. If the same request is retried by the backend-supported flow, keep it tied to the same user action; do not create a new service order from guesswork.

## Links

Whenever a command displays a web destination, render it as a Markdown link with a human-readable English label. Never put a URL in backticks or a code block. Never show an internal endpoint.

Approved public links:

- [Services](https://hidden-world.space/en/services)
- [Hidden World profile](https://hidden-world.space/en/profile)
- [Hidden World contacts](https://hidden-world.space/en/contacts)
- [Natal interpretation help](https://hidden-world.space/en/articles/site_help_interpretation)
- [Forecast help](https://hidden-world.space/en/articles/site_help_forecast)
- [Prashna help](https://hidden-world.space/en/articles/site_help_prashna)
- [Panchanga help](https://hidden-world.space/en/articles/site_help_panchanga)

## Exact Help Menu

For `/astro-help`, respond immediately with the following Markdown content and nothing else. Use this English menu by default.

For Russian or Ukrainian help, translate every user-facing line, including all headings, command descriptions, plain-language shortcuts, example questions, choice labels, and placeholder labels inside angle brackets such as `<birth date>` and `<your question>`. Preserve only slash command identifiers, Markdown URLs, the product name Astro Jyotish, the proper names Volodymyr Kraine, Parashara, and Kraine, and literal language codes such as `en`, `ru`, and `ua`. English example sentences and English placeholder labels are forbidden in Russian or Ukrainian help output.

Return only the translated menu. Do not paraphrase, summarize, add recommendations, add implementation details, or offer to show more information after the menu.

```markdown
# Astro Jyotish

Astro Jyotish is by professional astrologer Volodymyr Kraine with 20+ years of experience.

## Commands

`/astro-help` - show this command menu
`/astro-login` - connect your Hidden World account
`/astro-status` - check your account, active chart images, stars, and subscription
`/astro-chart-images` - show active chart images: round D-1 Rasi, round D-9 Navamsha, South Indian D-1 Rasi, and South Indian D-9 Navamsha
`/astro-chart-setup` - learn how saved charts work
`/astro-create-chart` - create, save, and activate a natal chart
`/astro-charts` - list saved charts and show the active chart
`/astro-set-active-chart` - select the active saved chart
`/astro-contact` - send a confirmed message to Hidden World support ([Contact support](https://hidden-world.space/en/contacts))
`/astro-services` - view services, requirements, and current prices ([Services](https://hidden-world.space/en/services))
`/astro-natal` - choose language and Parashara/Kraine, then interpret your active natal chart ([How it works](https://hidden-world.space/en/articles/site_help_interpretation))
`/astro-forecast` - choose language and Parashara/Kraine, then create a forecast from your active natal chart ([How it works](https://hidden-world.space/en/articles/site_help_forecast))
`/astro-prashna` - choose language and Parashara/Kraine, then ask a concrete question using a question chart ([How it works](https://hidden-world.space/en/articles/site_help_prashna))
`/astro-panchanga` - choose language and Parashara/Kraine, then view Panchanga for a date and place ([How it works](https://hidden-world.space/en/articles/site_help_panchanga))
`/astro-question` - choose language, then ask the Kraine AI astrologer about your active chart

## Plain-language shortcuts

You can also ask in plain English:

- Connect my Hidden World account.
- Show my Astro Jyotish status.
- Show my active chart images.
- Create and save a new chart for <birth date> at <birth time>, <city>, <country>, and name it <chart name>.
- List my saved Hidden World charts.
- Make the saved chart named "<chart name>" active.
- Contact Hidden World support about <subject>: <your message>.
- Make Kraine Panchanga in Russian for today.
- Make Parashara Panchanga in English for tomorrow in Pirovac, Croatia.
- Create a Kraine forecast in Russian for 2026-09-01.
- Interpret my active natal chart with Kraine in Russian, focus on house 10.
- Create a Kraine Prashna question chart in Russian for this situation: <your question>.
- Ask Kraine AI about my active natal chart in Russian: <your question about my chart>.

## Good Prashna questions

- Should I accept this offer?
- Can I reach an agreement with this partner?
- Is it worth launching this project this month?

## Choices

Languages: English, Russian, Ukrainian.
AI astrologers: Parashara, Kraine.
```

## Exact Chart Setup

For `/astro-chart-setup`, select exactly one finished template below from the explicit user language: Russian, Ukrainian, or English. Emit only the contents of that template, without the surrounding code fence or language label.

Do not translate at runtime, paraphrase, summarize, add notes, add new service rules, add a numbered workflow, inspect a website route, or offer to show more information after the template.

### Russian output

```markdown
# Настройка карт

Astro Jyotish использует сохраненные карты Hidden World.

## Возможности плагина

`/astro-charts` - показать сохраненные карты и активную карту.
`/astro-create-chart` - создать, сохранить и активировать натальную карту по данным рождения.
`/astro-set-active-chart` - выбрать сохраненную карту, которую будут использовать персональные сервисы.

## Создание и сохранение карты

Используйте `/astro-create-chart`, указав дату рождения, время рождения и место рождения. Если время рождения неизвестно, скажите об этом явно.

Созданная карта сохранится в Hidden World и станет активной для персональных сервисов.

## Примеры

- Создай и сохрани карту по данным: <дата рождения>, <время рождения>, <город>, <страна>; назови ее <название карты>.
- Покажи мои сохраненные карты Hidden World.
- Сделай сохраненную карту с названием "<название карты>" активной.
- Покажи мою активную карту перед запуском прогноза.
```

### Ukrainian output

```markdown
# Налаштування карт

Astro Jyotish використовує збережені карти Hidden World.

## Можливості плагіна

`/astro-charts` - показати збережені карти й активну карту.
`/astro-create-chart` - створити, зберегти й активувати натальну карту за даними народження.
`/astro-set-active-chart` - вибрати збережену карту, яку використовуватимуть персональні сервіси.

## Створення та збереження карти

Використовуйте `/astro-create-chart`, указавши дату народження, час народження та місце народження. Якщо час народження невідомий, скажіть про це прямо.

Створена карта збережеться в Hidden World і стане активною для персональних сервісів.

## Приклади

- Створи й збережи карту за даними: <дата народження>, <час народження>, <місто>, <країна>; назви її <назва карти>.
- Покажи мої збережені карти Hidden World.
- Зроби збережену карту з назвою "<назва карти>" активною.
- Покажи мою активну карту перед запуском прогнозу.
```

### English output

```markdown
# Chart Setup

Astro Jyotish uses saved Hidden World charts.

## What the plugin can do

`/astro-charts` - show saved charts and the active chart.
`/astro-create-chart` - create, save, and activate a natal chart from birth data.
`/astro-set-active-chart` - make one saved chart active for personal services.

## Creating or saving a chart

Use `/astro-create-chart` with birth date, birth time, and birth place. If birth time is unknown, say that explicitly.

The created chart is saved to Hidden World and becomes the active chart for personal services.

## Examples

- Create and save a chart for <birth date> at <birth time>, <city>, <country>, and name it <chart name>.
- List my saved Hidden World charts.
- Make the saved chart named "<chart name>" active.
- Show my active chart before starting a forecast.
```
