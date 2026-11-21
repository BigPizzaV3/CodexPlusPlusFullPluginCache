<p align="center"><img src="assets/logo.png" alt="Artispreneur" width="170"></p>

<h1 align="center">Artispreneur: Complete Artist Toolkit</h1>
<p align="center"><b>Art Means Business.</b><br>48 artist skills plus a 42-role record-label team for independent artists and labels.</p>
<p align="center"><a href="https://www.artispreneur.com">artispreneur.com</a> · <a href="https://www.artispreneur.com/directory">Industry directory</a> · <a href="https://www.artispreneur.com/royalty-check">Royalty Health Check</a> · <a href="https://www.artispreneur.com/academy">Academy</a> · <a href="https://www.artispreneur.com/support">Support</a></p>

---

## What this is

An independent artist has to do the work of an entire record label: form a business, register songs so royalties arrive, plan releases, write bios, build a press kit, pitch venues and playlists, post consistently, and keep the money straight. This toolkit gives your AI assistant the playbooks to do that work with you, one finished deliverable at a time.

- **48 artist skills in 12 groups**, from registering songs with a PRO to planning a release, building an EPK, and pitching playlists.
- **A 42-role Label Team** (264 playbooks): label manager, A&R, publicist, marketing, royalty accountant, business affairs and more, each built from real job postings, for anyone running their own label.
- **Works anywhere.** Each skill is a self-contained folder with a `SKILL.md`, so it runs in Claude, ChatGPT, and other tools that read skills. No account needed.
- **Draft-first and honest.** Skills produce checklists, documents, and plans in your conversation. They never claim to have filed, sent, registered, or paid anything, and they never invent facts or numbers. Gaps are marked `[CONFIRM]`.
- **Quality checks built in.** Every skill ends with a checklist it runs before handing work over.
- **Optional live tools.** Connect the Artispreneur MCP server (`https://www.artispreneur.com/mcp`, no sign-in) for computed release plans, readiness checks, and EPK outlines.

## Install

**Claude Code (from GitHub):** `/plugin marketplace add diamitani/artispreneur.com`, then `/plugin install artispreneur@artispreneur`.

**Claude Code (from the zip):** unzip, then run `claude --plugin-dir ./artispreneur`. The skills load automatically.

**Claude, ChatGPT, and other tools:** each folder in `skills/` is a standalone skill. Upload the ones you want, or the whole `skills/` folder, following your tool's instructions for adding skills or plugins. `plugin.json` describes the whole package for tools that read plugin manifests.

**Start here:** ask "What can Artispreneur do?" to run `get-started`, or say "Set up my artist profile." Every other skill reads that profile so you only share facts once.

## The 48 skills

### Career
*Know where you're going.*

| Skill | What it does | Time |
|---|---|---|
| [`artist-profile`](skills/artist-profile/SKILL.md) | Your artist record, set up once. Every other skill reads from it. | ~10 min |
| [`artist-goals`](skills/artist-goals/SKILL.md) | Turn 'I want to blow up' into 1 to 3 dated goals you can actually hit. | ~10 min |
| [`weekly-win-plan`](skills/weekly-win-plan/SKILL.md) | Your top 3 moves this week, ranked by what actually moves the needle. | ~5 min |

### Studio
*Look and sound like a pro.*

| Skill | What it does | Time |
|---|---|---|
| [`create-an-epk`](skills/create-an-epk/SKILL.md) | A press kit built for the person reading it: booker, press, brand, or festival. | ~25 min |
| [`create-an-artist-bio`](skills/create-an-artist-bio/SKILL.md) | One story, told at every length you'll ever need. | ~10 min |
| [`create-brand-logo`](skills/create-brand-logo/SKILL.md) | A logo brief a designer (or Canva) can execute on day one. | ~15 min |
| [`write-brand-guidelines`](skills/write-brand-guidelines/SKILL.md) | Your brand bible: voice, visuals, and rules everyone follows. | ~20 min |
| [`brand-positioning`](skills/brand-positioning/SKILL.md) | The one true thing about you that no other artist in your genre can say. | ~20 min |

### Legal entity
*Make it a real business.*

| Skill | What it does | Time |
|---|---|---|
| [`get-ein`](skills/get-ein/SKILL.md) | Your federal tax ID directly from the IRS, done step by step. | ~15 min |
| [`create-llc`](skills/create-llc/SKILL.md) | Separate your music money from your personal money. | ~25 min |
| [`create-c-corp`](skills/create-c-corp/SKILL.md) | Incorporate for investors, a label, or scale, with eyes open. | ~30 min |
| [`legal-business-checklist`](skills/legal-business-checklist/SKILL.md) | The business basics (entity, copyright, licensing, PRO) in the right order. | ~15 min |

### Contracts
*Put it in writing.*

| Skill | What it does | Time |
|---|---|---|
| [`create-split-sheet-agreement`](skills/create-split-sheet-agreement/SKILL.md) | Everyone's share, in writing, before the song blows up. | ~15 min |
| [`license-music`](skills/license-music/SKILL.md) | Pitch-ready sync briefs and licensing basics, in plain English. | ~20 min |
| [`contract-intake`](skills/contract-intake/SKILL.md) | Understand any music contract in plain English before you sign. | ~20 min |

### Finance
*Know where the money goes.*

| Skill | What it does | Time |
|---|---|---|
| [`open-business-bank-account`](skills/open-business-bank-account/SKILL.md) | Walk into the bank (or app) with everything they'll ask for. | ~15 min |
| [`manage-business-expenses`](skills/manage-business-expenses/SKILL.md) | Know where every dollar goes, and keep the receipts that save you taxes. | ~20 min |
| [`file-business-taxes`](skills/file-business-taxes/SKILL.md) | Get organized for tax season instead of panicking through it. | ~20 min |
| [`track-royalties-on-dsps`](skills/track-royalties-on-dsps/SKILL.md) | Every royalty stream in one tracker, so nothing slips through. | ~20 min |
| [`write-a-business-plan`](skills/write-a-business-plan/SKILL.md) | A real plan with real numbers, for you, a partner, or a lender. | ~30 min |
| [`budget-planning`](skills/budget-planning/SKILL.md) | A plain-language budget and runway for your release, tour, or year. | ~20 min |

### Publishing & PRO
*Get paid when your songs play.*

| Skill | What it does | Time |
|---|---|---|
| [`register-with-pro`](skills/register-with-pro/SKILL.md) | Join ASCAP, BMI, or SESAC the right way, as writer and publisher. | ~20 min |
| [`register-tracks-with-pro`](skills/register-tracks-with-pro/SKILL.md) | Register every song so royalties can actually find you. | ~15 min |
| [`royalty-readiness`](skills/royalty-readiness/SKILL.md) | Make sure every royalty stream you're owed has somewhere to land. | ~15 min |
| [`claim-tracks-with-pro`](skills/claim-tracks-with-pro/SKILL.md) | Find and claim royalties already owed to you. | ~30 min |

### Release & DSP
*Ship music the right way.*

| Skill | What it does | Time |
|---|---|---|
| [`distribution-readiness`](skills/distribution-readiness/SKILL.md) | Everything checked before you upload, and the right distributor for you. | ~20 min |
| [`release-music-with-dsp`](skills/release-music-with-dsp/SKILL.md) | A release plan that works backward from drop day. | ~25 min |
| [`set-up-dsp`](skills/set-up-dsp/SKILL.md) | Claim and polish your artist profiles on every streaming service. | ~25 min |

### Catalogue
*Keep every track organized.*

| Skill | What it does | Time |
|---|---|---|
| [`upload-track-to-catalogue`](skills/upload-track-to-catalogue/SKILL.md) | Every track logged once, reused by every other tool. | ~15 min |
| [`extract-metadata-from-track`](skills/extract-metadata-from-track/SKILL.md) | Clean, complete metadata for every track in your catalog. | ~15 min |
| [`transcribe-lyrics`](skills/transcribe-lyrics/SKILL.md) | Clean, formatted lyrics ready for DSPs, videos, and liner notes. | ~15 min |

### Content & marketing
*Show up consistently.*

| Skill | What it does | Time |
|---|---|---|
| [`create-content-calendar`](skills/create-content-calendar/SKILL.md) | A posting plan you can actually keep up with. | ~20 min |
| [`generate-social-media-content`](skills/generate-social-media-content/SKILL.md) | Platform-native posts in your voice, ready to publish. | ~20 min |
| [`create-lyric-video`](skills/create-lyric-video/SKILL.md) | A kinetic lyric video, ready to render, no editor skills needed. | ~30 min |
| [`write-music-video-treatment`](skills/write-music-video-treatment/SKILL.md) | A shoot-ready treatment a director or friend-with-a-camera can run with. | ~25 min |
| [`upload-music-video-to-youtube`](skills/upload-music-video-to-youtube/SKILL.md) | Everything ready to upload your video to YouTube. | ~20 min |
| [`analyze-social-media-engagement`](skills/analyze-social-media-engagement/SKILL.md) | See what's working, what's not, and what to post next. | ~25 min |

### Merch
*Sell something fans can wear.*

| Skill | What it does | Time |
|---|---|---|
| [`create-merch-designs`](skills/create-merch-designs/SKILL.md) | Merch your fans actually want to wear. | ~25 min |
| [`set-up-merch-drop-shipping`](skills/set-up-merch-drop-shipping/SKILL.md) | Print-on-demand merch with zero inventory risk. | ~25 min |

### Outreach
*Reach the people who can help.*

| Skill | What it does | Time |
|---|---|---|
| [`directory-search`](skills/directory-search/SKILL.md) | Find the right blogs, playlists, radio, podcasts, press and venues for your genre. | ~20 min |
| [`booking-outreach`](skills/booking-outreach/SKILL.md) | Venue and promoter outreach for the cities and dates you want. | ~25 min |
| [`pr-campaign`](skills/pr-campaign/SKILL.md) | A 5-email press sequence built around one real, newsworthy hook. | ~30 min |
| [`media-outreach`](skills/media-outreach/SKILL.md) | Personal pitch emails for every journalist and blog on your list. | ~25 min |
| [`add-music-to-collaborative-playlist`](skills/add-music-to-collaborative-playlist/SKILL.md) | Real playlist curators, honest pitches, no pay-for-play. | ~25 min |
| [`playlist-outreach`](skills/playlist-outreach/SKILL.md) | Short, curator-friendly pitches matched to playlists in your genre. | ~20 min |

### Build your own
*Make the toolkit yours.*

| Skill | What it does | Time |
|---|---|---|
| [`knowledge-ingestion`](skills/knowledge-ingestion/SKILL.md) | Teach your agent: turn your bios, contracts and past EPKs into facts it remembers. | ~20 min |
| [`build-an-agent`](skills/build-an-agent/SKILL.md) | Spin up your own sub-agent for a project, with its own tools and memory. | ~30 min |
| [`build-a-skill`](skills/build-a-skill/SKILL.md) | Turn your workflow into a skill you can reuse or share with your team. | ~20 min |

## The Label Team: 42 roles, 264 playbooks

A full record-label staff as skills. Each role is one real music-industry job, built from the responsibilities in real postings at labels, distributors, and music companies. Switch on the roles for the jobs you cannot staff yet. Ask for `label-team` to see the roster and be routed to the right role. Each role folder holds its playbooks in `references/`, plus the software it uses and the postings it came from.

**Starting solo? Turn these on first:** `label-manager`, `label-release-operations-manager`, `label-marketing-manager`, `label-social-content-creator`, `label-business-affairs-manager`, `label-rights-administrator`, `label-royalty-accountant`.

### Leadership

| Skill | Role | Playbooks |
|---|---|---|
| [`label-manager`](skills/label-manager/SKILL.md) | Label Manager / GM | 7 |
| [`label-artist-relations-manager`](skills/label-artist-relations-manager/SKILL.md) | Artist Relations (Day-to-Day) Manager | 5 |
| [`label-assistant`](skills/label-assistant/SKILL.md) | Label Assistant | 7 |

### Marketing

| Skill | Role | Playbooks |
|---|---|---|
| [`label-head-of-marketing`](skills/label-head-of-marketing/SKILL.md) | Head of Marketing | 6 |
| [`label-marketing-manager`](skills/label-marketing-manager/SKILL.md) | Marketing Manager (Product / Campaign Manager) | 7 |
| [`label-digital-marketing-manager`](skills/label-digital-marketing-manager/SKILL.md) | Digital Marketing Manager | 8 |
| [`label-paid-media-buyer`](skills/label-paid-media-buyer/SKILL.md) | Paid Media Buyer | 7 |
| [`label-fan-crm-manager`](skills/label-fan-crm-manager/SKILL.md) | Fan CRM & Audience Development Manager | 6 |
| [`label-social-media-manager`](skills/label-social-media-manager/SKILL.md) | Social Media & Community Manager | 7 |
| [`label-creator-viral-marketer`](skills/label-creator-viral-marketer/SKILL.md) | Creator & Viral Marketing Manager | 7 |
| [`label-social-content-creator`](skills/label-social-content-creator/SKILL.md) | Social Content Creator | 6 |
| [`label-international-marketing-manager`](skills/label-international-marketing-manager/SKILL.md) | International Marketing Manager | 6 |
| [`label-catalog-marketing-manager`](skills/label-catalog-marketing-manager/SKILL.md) | Catalog Marketing Manager | 6 |
| [`label-youtube-channel-strategist`](skills/label-youtube-channel-strategist/SKILL.md) | YouTube Channel Strategist | 6 |
| [`label-creative-director`](skills/label-creative-director/SKILL.md) | Creative Director | 6 |

### A&R & Creative Development

| Skill | Role | Playbooks |
|---|---|---|
| [`label-ar-manager`](skills/label-ar-manager/SKILL.md) | A&R Manager | 7 |
| [`label-ar-scout-analyst`](skills/label-ar-scout-analyst/SKILL.md) | A&R Scout & Analyst | 6 |
| [`label-ar-administrator`](skills/label-ar-administrator/SKILL.md) | A&R Administrator | 6 |
| [`label-studio-manager`](skills/label-studio-manager/SKILL.md) | Studio Manager | 5 |

### Promotion & Media

| Skill | Role | Playbooks |
|---|---|---|
| [`label-publicist`](skills/label-publicist/SKILL.md) | Publicist | 7 |
| [`label-radio-promoter`](skills/label-radio-promoter/SKILL.md) | Radio Promotions Manager | 5 |
| [`label-street-team-rep`](skills/label-street-team-rep/SKILL.md) | Street Team & College Marketing Rep | 6 |

### Commercial & Partnerships

| Skill | Role | Playbooks |
|---|---|---|
| [`label-dsp-partnerships-manager`](skills/label-dsp-partnerships-manager/SKILL.md) | DSP & Commercial Partnerships Manager | 7 |
| [`label-brand-partnerships-manager`](skills/label-brand-partnerships-manager/SKILL.md) | Brand Partnerships Manager | 5 |
| [`label-sync-licensing-manager`](skills/label-sync-licensing-manager/SKILL.md) | Sync Licensing Manager | 6 |
| [`label-artist-label-acquisitions`](skills/label-artist-label-acquisitions/SKILL.md) | Artist & Label Acquisitions (Business Development) Manager | 5 |

### Direct-to-Fan, Merch & Live

| Skill | Role | Playbooks |
|---|---|---|
| [`label-d2c-ecommerce-manager`](skills/label-d2c-ecommerce-manager/SKILL.md) | D2C & E-Commerce Manager | 6 |
| [`label-merch-brand-manager`](skills/label-merch-brand-manager/SKILL.md) | Merch Brand Manager | 6 |
| [`label-merch-production-manager`](skills/label-merch-production-manager/SKILL.md) | Merch Production Manager | 6 |
| [`label-vip-fan-experiences`](skills/label-vip-fan-experiences/SKILL.md) | VIP & Fan Experiences Manager | 5 |
| [`label-live-touring-manager`](skills/label-live-touring-manager/SKILL.md) | Live & Touring Manager | 6 |

### Operations & Distribution

| Skill | Role | Playbooks |
|---|---|---|
| [`label-release-operations-manager`](skills/label-release-operations-manager/SKILL.md) | Release Operations Manager | 7 |
| [`label-distribution-manager`](skills/label-distribution-manager/SKILL.md) | Distribution Manager | 7 |
| [`label-physical-supply-chain-manager`](skills/label-physical-supply-chain-manager/SKILL.md) | Physical Supply Chain & Fulfillment Manager | 6 |

### Data & Systems

| Skill | Role | Playbooks |
|---|---|---|
| [`label-systems-automation`](skills/label-systems-automation/SKILL.md) | Label Systems & AI Automation Lead | 7 |
| [`label-data-insights-analyst`](skills/label-data-insights-analyst/SKILL.md) | Data & Audience Insights Analyst | 7 |

### Rights, Legal & Business Affairs

| Skill | Role | Playbooks |
|---|---|---|
| [`label-business-affairs-manager`](skills/label-business-affairs-manager/SKILL.md) | Business Affairs & Contracts Manager | 7 |
| [`label-rights-administrator`](skills/label-rights-administrator/SKILL.md) | Rights & Catalog Administrator | 6 |
| [`label-content-protection-specialist`](skills/label-content-protection-specialist/SKILL.md) | Content Protection Specialist | 6 |

### Finance & Royalties

| Skill | Role | Playbooks |
|---|---|---|
| [`label-royalty-accountant`](skills/label-royalty-accountant/SKILL.md) | Royalty Accountant | 7 |
| [`label-finance-manager`](skills/label-finance-manager/SKILL.md) | Label Finance Manager | 7 |
| [`label-deal-valuation-analyst`](skills/label-deal-valuation-analyst/SKILL.md) | Deal & Valuation Analyst | 6 |

## How every skill is built

Every skill, artist or label role, follows the same structure, so they work together and are easy to trust:

1. **When to use**: the situations that trigger it.
2. **Ask first**: only what is missing from your artist or label profile.
3. **Workflow**: numbered steps.
4. **Deliverables**: what you get, and an output template where useful.
5. **Quality checks**: a checklist the assistant runs before handing work over.
6. **Guardrails**: what it will never do.
7. **Hand-offs**: which skill comes next.
8. **Start with**: a sentence that kicks it off.

## What this toolkit will not do

It does not log in to your accounts, file anything, send messages, register works, release music, or give legal, tax, or financial advice. It prepares you to do those things correctly. For anything binding or disputed, work with an entertainment attorney or tax professional.

## OpenAI Directory Compliance, Privacy & Safety

- **Independent product:** Artispreneur is developed by Patrick Diamitani (`pat@artispreneur.com`) and is not affiliated with or endorsed by OpenAI.
- **Audience appropriateness:** Designed for general audiences (ages 13+) working on music-career and record-label operations.
- **Data minimization & Restricted Data prohibition:** Skills and MCP tools operate only on explicit, task-scoped user inputs. They never collect, solicit, or process payment card data (PCI DSS), protected health information (PHI), government identifiers (SSN, ITIN, EIN digits, passport or driver's license numbers), access credentials (passwords, API keys, MFA/OTP codes), precise user location data (street addresses or GPS coordinates), or full conversation transcripts.
- **Read-only, independent MCP tools:** `plan_release`, `check_release_readiness`, and `get_epk_outline` require no authentication (`auth.type: "none"`), operate independently with explicit annotations (`readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`), and return only task-relevant calculation/checklist payloads without telemetry or session identifiers.
- **No digital commerce or upsells:** This plugin does not sell digital goods or subscriptions, does not display pricing plans or promotional upsells, and does not embed or initiate checkout flows.
- **License:** Distributed under the [MIT License](LICENSE).

## More at Artispreneur

- Website: [https://www.artispreneur.com](https://www.artispreneur.com)
- Industry contact directory: [https://www.artispreneur.com/directory](https://www.artispreneur.com/directory)
- Royalty Health Check: [https://www.artispreneur.com/royalty-check](https://www.artispreneur.com/royalty-check)
- Split sheets: [https://www.artispreneur.com/split-sheets](https://www.artispreneur.com/split-sheets) · Contracts: [https://www.artispreneur.com/contracts](https://www.artispreneur.com/contracts)
- Academy: [https://www.artispreneur.com/academy](https://www.artispreneur.com/academy)
- Support: [https://www.artispreneur.com/support](https://www.artispreneur.com/support) · [Privacy](https://www.artispreneur.com/legal/privacy) · [Terms](https://www.artispreneur.com/legal/terms)
- Source: [github.com/diamitani/artispreneur.com](https://github.com/diamitani/artispreneur.com)

<p align="center"><sub>Artispreneur · Art Means Business · Version 2.0.0</sub></p>
