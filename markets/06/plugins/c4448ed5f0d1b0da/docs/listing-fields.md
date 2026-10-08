# Soulware directory listing

Release: **0.3.0**, prepared locally. This package and copy have not been uploaded or submitted. The previously recorded 0.2.0 portal draft is a separate artifact; its scan or approval status does not transfer to this release.

## Public fields

| Field | Value |
| --- | --- |
| Display name | Soulware by Honorary Human |
| Publisher / developer name | Nicholas Nabil Hamze |
| Brand / author | Honorary Human |
| Version | 0.3.0 |
| Category | Productivity |
| Short description | Compare and tune AI voices |
| Website | https://honoraryhuman.com/ |
| Privacy policy | https://honoraryhuman.com/privacy |
| Support | https://honoraryhuman.com/support |
| Terms of service | https://honoraryhuman.com/terms |

### Long description

Give your AI a voice of its own.

Compare Flint, Lantern, and Moss on your own question, then choose the personality you want to work with. Flint gets to the decision, Lantern explains with a concrete example, and Moss offers a measured view with occasional dry humor. You can also import a Soul Kit from Honorary Human.

Adjust the selected voice as you work: less humor, warmer wording, shorter answers, or writing only. Ask which voice is active, pause and resume it, reset your adjustments, or switch personalities. These choices apply to the current conversation. Your instructions, facts, and requested format take priority.

When you ask to save lasting changes, Soulware can prepare a revised portable Soul Kit. With file execution available, its bundled helper validates and versions the file while preserving the original. Otherwise it can provide manually inspected JSON to save yourself. Reimport the revised kit to use it in another conversation.

In local Codex, you can also export a reusable voice skill, install it for yourself or a project, and choose whether to make it a default. Inspect, update, or remove installed kits when needed.

The plugin requires no Soulware account or API key. Its bundled helper makes no network requests and does not send your kit or conversations to Honorary Human. ChatGPT and Codex still process the content you give them under their own settings and policies.

Find more Soul Kits or create an original personality at honoraryhuman.com. A personality is a designed communication style. It does not impersonate a real person or change account-wide ChatGPT preferences.

### Conversation starters

1. Compare Flint and Lantern: should I rebuild my whole website because one page is confusing?
2. Import my attached Soul Kit and use its voice for writing only.
3. Try Moss with less humor and help me choose a manageable first step for a new project.

## Prior publisher notes (0.2.0; not newly verified)

### Privacy coverage

The Website task confirmed the public privacy page is live and visually verified, including the plugin-specific addendum. It covers the website's drafts, downloads, and generation alongside the plugin's selected-kit use and optional local setup. The host AI service's own policies still apply to the content it processes.

### Support

The support page is live and visually verified at https://honoraryhuman.com/support. It provides practical setup and troubleshooting guidance. A public support email or direct contact destination is still pending; no address or response guarantee has been invented.

### Terms

Nick approved the Soulware terms, including the personal and commercial use permission and Nicholas Nabil Hamze as the operator behind Honorary Human. The Website task confirmed the approved terms are live and visually verified at https://honoraryhuman.com/terms. The local copy is retained in `drafts/terms-page.md`.

### Manifest URL fields

Both manifests contain `interface.supportURL` and `interface.termsOfServiceURL` (inside `extensions.com.openai.interface` in the portable manifest). These exact keys are documented in the current [submission error reference](https://developers.openai.com/plugins/deploy/submission-errors). The local plugin-creator reference and validator predate `supportURL`; the public directory reference documents it explicitly.

### Publisher identity

Nicholas Nabil Hamze is the verified individual in the plugin portal and the approved operator behind Honorary Human. The portal's public developer name has been saved and visibly confirmed as **Nicholas Nabil Hamze**; both source manifests now match it. The display name remains **Soulware by Honorary Human**, and the author brand remains **Honorary Human**.

### Listing artwork

Logo: `assets/soulware-logo.png` (1254 × 1254). Composer icon: `assets/soulware-icon.svg` (the website's original cobalt/citron compact symbol). Both light and dark listing backgrounds use the opaque cream logo tile. Brand color: `#2447DF`; dark brand color: `#EAF258`. This Skills only package does not declare screenshots because that field is reserved for MCP plugins with custom UI.

## Reviewer scenarios

Use the bounded [ChatGPT acceptance procedure](chatgpt-acceptance.md). It records expected behavior and host prerequisites; pending scenarios are not completed tests.
