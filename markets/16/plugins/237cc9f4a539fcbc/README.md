# CalcIng Engineering

Mechanical engineering calculations from a conversation in ChatGPT. The plugin connects ChatGPT to
the calculation apps of [saas.calcing.de](https://saas.calcing.de/) and adds two skills that tell the
model how to use them: find the right app, clarify missing inputs and units with you, let the app
check the inputs, calculate, and report the app's result together with its warnings and provenance.

The numbers come from the calcing apps on our server, not from the model. If a calculation cannot run
(not signed in, no access, invalid input, server error), the skills tell the model to report the
error and not to replace the result with an estimate of its own.

## What is included

- **MCP server** `calcing`: the remote MCP server `https://saas.calcing.de/mcp/openai` (Streamable
  HTTP). The list of apps and their input schemas are available without sign-in; every other tool
  asks you to sign in with your calcing account (OAuth 2.1).
- **Skill `engineering-calculation`**: guided calculation with any calcing app the server lists. At
  the time of writing these are shafts and axles (DIN 743), parallel keys (DIN 6885 / DIN 6892),
  interference fits (DIN 7190-1), ISO fits (ISO 286), bolted joints (VDI 2230), rolling bearing life
  (ISO 281) and detailed rolling-bearing analysis (DIN 26281), shaft-bearing systems, rolling
  contacts, planetary gear stages (DIN 3990 Part 21), FKM strength assessment, district-heating
  branches (EN 13941-1), axial fans, horizontal- and vertical-axis wind turbines, plus material
  lookup. The skill reads the current list from the server instead of relying on a fixed set.
- **Skill `result-handoff`**: passes the result of one app on as the input of the next app
  (dry run first, then execute).

## Setup

Install the plugin in ChatGPT and connect the `calcing` server when ChatGPT asks for it. The first
tool that needs your account starts the sign-in.

### Signing in (what you see)

Connecting opens saas.calcing.de in your browser. Sign in with your calcing account (or register).
A consent page then asks whether to allow access for the platform, shows the provider, your account
and the list of actions the platform may perform on your behalf (for example "check inputs" or
"calculate" per app). Select **Allow** to finish; you are returned to ChatGPT.

### Who can use it

- Calculations need a calcing account on saas.calcing.de; you sign in when you connect.
- Calculations through ChatGPT require a calcing plan Basic or higher; new accounts can also use
  them with the sign-up credit of the account while it is valid. They use no credits. The terms are set
  out in the calcing terms of service, section 10
  ([saas.calcing.de/rechtliches/terms.en.html](https://saas.calcing.de/rechtliches/terms.en.html)).
- If the account has no access, the tool answers with the error `trial_exhausted` and a link to the
  plan overview, and the model reports it; nothing is calculated or estimated.

## Example requests

This request contains everything the app needs:

- "Deep groove ball bearing 6206 (C = 21.4 kN, C0 = 11.3 kN), purely radial 5 kN at 1500 rpm,
  reliability 90 %. How long does it last?"

The following start a calculation but **need further inputs**. The model will ask for them before the
app can calculate, for example the material from the app's material list and the effective diameter
(shaft), chamfers and fit details (key), further joint and thread data (bolt) or tool and geometry
data (planetary stage). With other values than the full worked example, the result differs from it:

- "Check my key connection: shaft Ø 120 mm of C60+N, key form A 32 × 18 × 125 of C45+C, hub of
  EN-GJL-250 (Ø 200/270 mm), nominal torque 4 kNm, peak torque 15 kNm in both directions, application
  factor 1.5. Does the surface pressure hold?"
- "Strength assessment of a stepped shaft: D = 50 mm, d = 42 mm, fillet radius 5 mm, 34CrMo4 quenched
  and tempered (σB = 1000 N/mm², σS = 800 N/mm²), Rz 5 µm, bending 500 ± 50 N/mm², torsion
  100 ± 30 N/mm². What are the safety factors?"
- "Bolt on a hydraulic cylinder: socket head cap screw M12 × 60, 10.9, screwed into C45, clamped part
  16MnCr5 with 42 mm clamp length, pulsating axial working load up to 24.9 kN, minimum clamp load 1 kN,
  friction coefficients 0.10, tightening factor 1.8. Which tightening torque, which safety factors?"
- "Planetary stage behind a steam turbine: 5000 kW, sun 12 477 rpm, fixed carrier, 3 planets, double
  helical mn = 3.5 mm, β = 31.01°, tooth numbers sun 22, planet 69, ring −161, face width 180 mm,
  application factor 1.25, load sharing 1.25. Tangential force and contact ratios at planet and ring
  gear?"

## Data

The plugin itself contains only instructions and the server address; it runs no code on your device
and stores nothing. When the model calls a calcing tool, the inputs of that call (for example
dimensions, loads, materials) go to saas.calcing.de over HTTPS, together with the access granted at
sign-in. If ChatGPT asks for your e-mail address when you connect (the consent page lists it), the
server gives ChatGPT your e-mail address, whether it is verified, and a persistent account identifier.
The server returns the result, notes and error messages. Our server logs each call (time,
app, action, result). Details: privacy policy, section 2.8
([saas.calcing.de/rechtliches/privacy.en.html](https://saas.calcing.de/rechtliches/privacy.en.html)); terms, section 10
([saas.calcing.de/rechtliches/terms.en.html](https://saas.calcing.de/rechtliches/terms.en.html)). ChatGPT processes your
conversation under OpenAI's terms.

You remain responsible for your inputs and for checking every result professionally before use.

## Revoking access

In saas.calcing.de, open **API & Skills → Connected AI platforms → Revoke access**, or disconnect
the plugin in ChatGPT.

## Support

- Documentation: [saas.calcing.de/?ki](https://saas.calcing.de/?ki)
- E-mail: info@calcing.de (also for security reports)
- Provider: CalcIng - Müller Engineering Solutions GmbH, Gewerbepark 10a, 36160 Dipperz, Germany
  ([imprint](https://saas.calcing.de/?legal=imprint))

## License

The plugin files (instructions, manifest, MCP configuration) are licensed under the
[MIT License](LICENSE). The calcing service on saas.calcing.de is not part of this license; its use
is governed by the terms of saas.calcing.de.

**Trademarks:** the name and logo "CalcIng" / "calcing" (including `assets/icon.png`) are not
licensed under the MIT License. They may not be used to identify other products or services without
written permission of CalcIng - Müller Engineering Solutions GmbH.

---

## Kurzfassung (Deutsch)

Das Plugin verbindet ChatGPT mit den Berechnungs-Apps von saas.calcing.de. Das Modell ermittelt die
passende App, klärt fehlende Eingaben und Einheiten mit Ihnen, lässt die App prüfen und rechnen und
gibt deren Ergebnis mit Warnungen und Herkunft wieder — ohne eigene Schätzwerte. Ohne Anmeldung sind
nur die App-Liste und die Eingabeschemata abrufbar; gerechnet wird mit Ihrem calcing-Konto (OAuth) und
einem Tarif ab „Basic“ (neue Konten auch mit dem gültigen Erstanmeldungs-Guthaben), zu den Bedingungen
der AGB, § 10. Lizenz der Plugin-Dateien: MIT; Name und Logo „CalcIng“ sind nicht
Teil der Lizenz. Widerruf unter **API & Skills → Verbundene KI-Plattformen**. Datenschutz:
Abschnitt 2.8, AGB: § 10. Kontakt: info@calcing.de.
