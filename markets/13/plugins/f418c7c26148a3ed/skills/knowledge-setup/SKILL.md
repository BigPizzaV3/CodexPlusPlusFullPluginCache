---
name: knowledge-setup
description: Set up and keep up a workspace's Knowledge - company, offer and pricing files, watched website pages, call transcripts, writing style, account tiers and scoring, the Review queue and Knowledge prompts - plus the playbooks for researching a company, reading its website and writing a campaign's qualification and AI variable prompts.
---

# Knowledge setup

Knowledge is what Kenso knows about a workspace: the company, its offer and prices, who it sells to, its proof and competitors, how its people write, and what its calls and website say. Campaigns and agents read it. Every personalization prompt gets the company folder's files and the Instructions; the reply agent and account research cite it; Knowledge prompts add workspace-wide rules to every campaign's qualification, scoring, personalization and replies.

This skill fills Knowledge in and keeps it true. It also holds the four playbooks it replaced, which work with or without Knowledge.

These tools cannot read or write Knowledge, so the person keeps it in the Kenso app, at https://app.ken.so/<workspace id>/demo/knowledge (it opens where the workspace has Knowledge on). You research, draft and check; they create and save the files there. The four campaign playbooks below work with or without Knowledge.

## Playbooks

| Task | Open |
|---|---|
| Research a company and write its company context | `references/client-research.md` |
| Read a company's website into notes | `references/website-scraping.md` |
| Write a campaign's qualification prompt | `references/qualification.md` |
| Write and test a campaign's AI variable prompts | `references/prompt-writer.md` |

Open one with `load_ken_skill` with name `knowledge-setup` and that reference. Each playbook reads on its own and names its own references, which open the same way. The Review queue and Knowledge prompts are worked in the app.

## Rules

- **Extract, never invent.** Every fact in a file comes from a source you can name: the website, a call, a document, or the person's words in this conversation. Never invent a price, a customer, a result or a number. A gap stays a gap: write it as an open question and ask.
- **Cite what people want.** A rule about how the company writes, or a claim about what a client wants, carries its source: who said it, where and when ("Dana, kickoff call, 2026-10-14"). With no source, ask; never fill the gap from a ticket's or an issue's claim.
- **A yes before each write.** Show what you will write, file by file, and save after the person agrees. A yes to the pricing file covers that file, not the folder.
- **Read before you draft a change.** Ask the person to paste the file's current text from the app, so your draft changes only what changed.
- **Edit sections, keep files.** The person changes the one section that changed and leaves the rest. A restructure is a new version of the same file, never a delete and a new file; History keeps every version.
- **Shared files need an admin.** When the app does not let the person change a shared file, a workspace admin saves it.
- **Webhook URLs and email-in addresses are passwords.** Give one only to the person who asked, here, and never write it into a file, a ticket or a shared channel.
- **Vendor names never reach clients.** Kenso's model and data providers stay out of Knowledge and out of what you tell a client.
- This skill never sends, launches, or changes a campaign's schedule or volume. A person approves every send and launch.

## Step 0: Check Knowledge is on

Ask the person to open https://app.ken.so/<workspace id>/demo/knowledge. If it does not open, Knowledge is off for this workspace: say so in one sentence and skip the Knowledge steps. The four campaign playbooks above still work without Knowledge, so offer the one the person needs.

## Step 1: Read what is there

1. Ask the person what is in Knowledge: the files in the company folder (named after the workspace, with Competitors and Proof inside), Instructions, and their own writing style. They paste a file's text when you need it.
2. Ask for the company context, the short company summary campaign prompts read: the Context field on https://app.ken.so/<workspace id>/settings/company.
3. Ask what else they have: the website, call transcripts or recaps, decks, case studies, emails they wrote.

Tell the person in a few lines what is there, what is missing and what you would fill first. Most workspaces need, in order: the company files, the website pages, the voice, then calls and tiers.

## Step 2: Company files

The company folder holds the company-wide files. Kenso seeds none, except a `Company overview` moved from Settings when the workspace had a company context. Aim for:

| File | Holds |
|---|---|
| Company overview | What the company does, for whom, and why it wins, in plain words |
| Ideal customer profile | Industries, sizes, roles, the problems they have, and who is not a fit |
| Pricing | Plans, prices and terms exactly as the company states them, with the source and its date |
| Proof (folder) | One file per case study or result: customer, problem, result, source |
| Competitors (folder) | One file per competitor: what they do, where the company wins, where it loses |

1. Gather: run the client-research playbook (the website, past research, the person's notes), or take what the person pastes or says.
2. For each file, draft it in the chat and get a yes. The person then saves it in the company folder at https://app.ken.so/<workspace id>/demo/knowledge: New file for a new one, or the existing file with that name, changing only the sections that changed. Proof and Competitors files go in those folders. A PDF, deck or document goes in with Upload.
3. Keep the company context in step with Company overview: the person pastes the approved summary into Context on https://app.ken.so/<workspace id>/settings/company and clicks Save.

What the person saves goes live at once and can be undone from the change log. What Ken learns later from the website, calls and mail goes through the review mode, which by default holds pricing and company-wide changes for a person.

## Step 3: The website

Read the pages that say what the company sells and to whom - home, product or service pages, pricing, customers or case studies, about - following the website-scraping playbook: with your own web browsing, or page text the person pastes. Skip blog posts, careers and legal pages. Each fact goes into its file draft with the page and the date you read it as its source; a price goes into Pricing exactly as the page states it. These tools cannot set which pages Kenso watches for changes.

## Step 4: Voice and Instructions

- **Instructions** are workspace rules every campaign follows ("never promise a delivery date", "say workspace, not account"), added to every personalization prompt as rules. Draft one rule per line, each with its source. A workspace admin saves shared ones in the Instructions folder at https://app.ken.so/<workspace id>/demo/knowledge.
- **Writing style** is per person: their You / Writing style file in Knowledge. Draft one `- rule` line each for the person to add there.
- A voice rule needs its source: the person's words, a sample they wrote, or a call. With nothing to learn from, ask for two or three emails they are proud of.

## Step 5: Calls and documents

- **Calls:** a transcript or recap the person pastes is a source like the website. Take out facts, proof, objections and voice rules, each cited by the call's name and date ("Kickoff with Acme, 2026-10-14"). `Name: words` lines tell you who said what: a voice rule comes from the company's own people, not from the prospect. These tools cannot add a transcript to Knowledge or connect a recorder, mailbox or CRM.
- **Documents:** the person uploads a deck, one-pager or case study to Knowledge with Upload, into the company folder or a folder in it. When they paste its text here, read it the same way and cite it by its file name.

## Steps 6 to 8: Review mode, account tiers, Knowledge prompts

These are set in the app; these tools cannot read or change them. The Review queue is https://app.ken.so/<workspace id>/demo/knowledge/review. Help the person decide:

- **Review mode** (a workspace admin's choice): the default holds skills, instructions, pricing and company-wide changes for a person; the others hold everything, or let company-wide changes through with spot checks.
- **Account tiers and scoring:** describe each tier from the Ideal customer profile. Funding is not a buying event: a new round alone never makes an account Tier 1, so weigh it below the signals that show need.
- **Knowledge prompts:** a rule that holds for every campaign (who never qualifies, what replies never say, how to personalize for this company) is written once as a Knowledge prompt. Changing a prompt that synced AI variables use rewrites them; on a live client campaign that changes what it sends, so it needs a yes that names the client.

## Step 9: Check and hand off

1. Read the drafts back the way agents will: overview, offer, pricing, proof, competitors, voice, instructions. Check that nothing is wrong, stale or without a source.
2. Report in a few lines: each file the person saved or still has to save, the company context, and what waits in Review (https://app.ken.so/<workspace id>/demo/knowledge/review). The change log is https://app.ken.so/<workspace id>/demo/knowledge/review/changes.
3. List the open questions you left as gaps: a price you could not confirm, a competitor with no source.

## What this skill cannot do here

- Read or write Knowledge, the company context, watched website pages, sources, the review mode, tiers or Knowledge prompts. You draft; the person saves in the app.
