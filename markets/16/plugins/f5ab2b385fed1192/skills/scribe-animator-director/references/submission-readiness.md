# Submission readiness — cloud draft

Checked 2026-10-05 against [official package format](https://developers.openai.com/plugins/build/plugins), [submission requirements](https://developers.openai.com/plugins/deploy/submission) and [Site tools prerequisites](https://learn.chatgpt.com/docs/webmcp). Reverify before any submission. A package build is not approval or publication.

| Item | Evidence / status / remaining work |
|---|---|
| Portable versioned skills-only package | Root plugin.json, skills/resources and local square icon; automated package tests. No MCP, app mapping or hooks. Ready for local installation testing only. |
| Architecture planning | Official submission page still states an existing skills-only plugin cannot later add MCP. Decide before public submission; this package does not convert the live WebMCP page into a remote server. |
| Publisher/access | Public product legal page and repository identify Ohotech Solutions Private Limited; developerName is sourced from those, not a verified OpenAI identity. Verified developer identity, owning org/project and submission role/access are **UNVERIFIED**. Owner must confirm name and rights. |
| Truthful metadata | Describes editable authoring and separate QA; no universal browser support, automatic finished video, guaranteed quality or token savings. Owner must review directory text against accepted local evidence. |
| Website/privacy/terms | https://scribeanimator.com, /privacy/ and /terms/ were readable on 2026-10-05 and identify the existing product/operator. These product policies may need plugin-specific coverage; owner/legal review remains. No legal terms were accepted. |
| Support | Public policy names support@scribeanimator.com. No verified HTTPS support landing page was found; /support/ and /contact/ did not return a readable page during checking. `supportURL` is deliberately omitted. Confirm a real support destination and maintenance responsibilities before submission; do not invent one. |
| Icon | assets/logo.png copies the existing marketing logo512.png (512×512). Local source hash/dimensions checked. Public logo download returned HTTP 403, so public asset-byte verification is blocked. Owner must confirm redistribution/brand rights. No fabricated logo or screenshot. |
| Scans | Portal metadata and required skill scans **NOT_RUN**. Complete scans and resolve required findings on the actual package before submission; do not claim local tests are portal scans. No remote MCP scan/review applies to this skills-only package. |
| Eligibility/policies | Owner must verify directory eligibility, supported countries/use case, ownership/license/brand rights, truthful identity and privacy/support compliance against current guidelines. No account/security settings changed. |
| Dependencies and rights | Validator includes bundled Ajv and perfect-freehand with notices; generated application code has no new distribution license asserted. Owner must establish project/package distribution rights before public release. |
| Local acceptance | Fresh installation and genuine WebMCP end-to-end checklist is **NOT_RUN**; see local-acceptance.md. Model/client compatibility remains unverified. |
| Full repository CI | Draft-fast and package checks are supporting evidence. Ready/full CI remains deferred until maintainers move the PR to ready. Keep draft during iteration. |

This cloud task creates a draft PR and local package artifact only. Uploading/submitting/publishing, verification, account changes and legal acceptance belong to an explicitly authorized later phase. Initial MCP review cases/recording are not required for skills-only packages under current docs; retain the local acceptance evidence for truthful claims regardless.
