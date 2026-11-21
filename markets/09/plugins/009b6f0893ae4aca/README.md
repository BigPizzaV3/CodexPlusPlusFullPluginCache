![Citation Checker icon](./assets/icon.png)

# Citation Checker

Version 0.1.3. Use this when checking a bibliography for DOI/title mismatches and recorded retraction or correction notices in public Crossref metadata.

[Product homepage](https://citehealth-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://citehealth-mcp.sunrysetech.com/mcp](https://citehealth-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://citehealth-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://citehealth-mcp.sunrysetech.com/support) · [Privacy policy](https://citehealth-mcp.sunrysetech.com/privacy) · [Terms](https://citehealth-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Citation Checker. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://citehealth-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://citehealth-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `search`: Find public citation metadata. Use this when finding up to five Crossref metadata candidates from a public paper title or bibliography phrase. Candidates do not establish a correct citation or valid research. Select a DOI and fetch or audit it. The query is sent to Crossref and is not retained by this service; do not send unpublished or personal content.
- `fetch`: Read DOI metadata and update notices. Use this when reading a selected DOI's public title, date and recorded updates. updated-by describes updates to this work; update-to is a separate reverse relation. Missing update records do not prove the work is unretracted or valid. One bounded Crossref request, no full-text retrieval or stored inputs.
- `audit_citations`: Check DOI and title pairs. Use this when checking up to four public DOI/claimed-title pairs for exact normalized title agreement and recorded updates. Distinguishes malformed DOI, Crossref not-found, source errors and title mismatch. Does not infer research quality, clinical validity or approximate title equivalence. At most four parallel bounded public metadata requests; no inputs are retained.

## Inputs, sources and privacy

Public lookup queries and identifiers are sent only to the fixed public providers described below. In this suite, those provider API hosts are saferproducts.gov (CPSC), api.crossref.org (Crossref) and federalregister.gov (Federal Register); a dedicated workflow uses only its own stated provider. Public providers have their own policies.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)
- [Crossref Retraction Watch documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/)

## Bounds and limitations

Search returns at most 5 metadata candidates. Audit accepts at most 4 DOI/title pairs and makes at most 4 parallel unique DOI requests, each limited to 8 seconds and 1 MiB. No full text is fetched.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- A DOI/title match checks metadata identity only. It does not validate methods, findings, clinical usefulness or research quality.
- No update recorded in this response does not establish that a work is valid or unretracted. Crossref and Retraction Watch coverage can be incomplete or delayed, especially for corrections and expressions of concern.
- Only updated-by notices concern updates to the selected work. update-to entries describe works updated by this record and are reported separately.
- Title matching is exact after HTML entity/markup cleanup, Unicode NFKC normalization, case folding and whitespace collapse. Punctuation and wording differences require review; no approximate match is asserted.
- At most four unique DOI requests per audit, in parallel, each bounded to eight seconds and 1 MiB. Search makes one request for at most five metadata candidates. No full text is retrieved or retained.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "search",
    "arguments": {
      "query": "chitosan hydrogel nano ZnO composite bandages"
    }
  },
  {
    "name": "fetch",
    "arguments": {
      "id": "10.1021/am300292v"
    }
  },
  {
    "name": "audit_citations",
    "arguments": {
      "citations": [
        {
          "doi": "10.1021/am300292v",
          "claimedTitle": "Flexible and Microporous Chitosan Hydrogel/Nano ZnO Composite Bandages for Wound Dressing: In Vitro and In Vivo Evaluation",
          "referenceId": "public-example"
        }
      ]
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
