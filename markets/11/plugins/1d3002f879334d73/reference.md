# eonik: the tools

The live list comes from the person's eonik connection (`tools/list`); this map is rendered from it by `python -m ops.mcp_skill`, never written by hand.

## The work (in the person's eonik app, signed in to this connection's account)

| Tool | What it does |
|---|---|
| `get_adapts_status` | Show the status of the person's adapts for this brand: what needs their decision, what is being made, what the client sent back, what was delivered, and which of their computers has eonik open. |
| `find_creatives` | Find creatives by name or project: the person's own design files and eonik projects on their computer, and every creative saved to this brand in eonik, whoever made it, with each one's size, project, where it is and the sizes already made from it. |
| `get_creative` | Look at one creative as it stands: every size of it with the words on each and what each line is for, whether its end block says the project's current facts, its recent saved states, and one picture of the whole set. |
| `check_package` | Check a finished package, a zip or a folder of files, against what it is for: every size the media plan asked for is in it, and each file's size, format and weight meets the published limits of the channel its size belongs to, such as Google Display's 150 KB. |
| `compare_versions` | Compare a creative with an earlier saved state of it, by default the state before its most recent change: what changed on each size in words, and one picture of every size before and after. |
| `make_ad` | Make a new ad in eonik from what the person wants said. |
| `recreate_ad` | Recreate an ad in eonik: keep its film, its shots and timing, and put the brand's product, person or place in it. |
| `make_versions` | Make versions of one creative that differ in one thing: the person shown, the setting, the language of its words, or one line's words, such as a price or an offer. |
| `onboard_brand` | Bring a brand's handover files into eonik: a folder on the person's computer or a zip they attached, with content sheets, brand guidelines, typefaces, logos and project facts. |
| `find_brand_pictures` | Find the brand's own pictures by what they are called or show: its photos, logos and lockups, people, places and products, with one picture of them to look at. |
| `change_creative` | Change named pieces of one creative precisely, on one size, several or every size: new words, bigger or smaller, moved to a side or corner, a colour for words, shown or hidden, another of the brand's pictures in the photo or the logo, or how a piece moves as the ad plays and how long it plays. |
| `undo_change` | Put a creative back to one of its saved states, such as the state before a change: every size as it was then, with its present state saved first so it can be brought back. |
| `make_adapts` | Make adapts, which are new sizes of a creative for a media plan, in the person's eonik app, with the brand's fonts, rules and layout kept the same way on every size. |
| `revise_adapts` | Prepare a change to adapts already made that needs judgement, such as a client's note in their own words, made by eonik's assistant in the person's eonik app (it uses eonik credits). |
| `check_before_sending` | Check every size of the named creatives against the brand's rules in the person's eonik app: the legal line for the project and its state, the mark, the typeface and the smallest text. |
| `send_for_approval` | Share the adapts of the named creatives to the brand's review room, where the client can comment on each size and approve or ask for changes, and return the review link. |
| `get_client_notes` | Read what reviewers said in eonik's review room for this brand: for each shared creative, whether it is waiting, approved or sent back, and each open note with who wrote it and the size it is on. |
| `answer_client_note` | Answer one reviewer's note in eonik's review room, where they will read it: a reply under their note in the person's name, and the note marked done once the change is made. |
| `deliver_set` | Export every adapt of the named creatives into the person's delivery folder, one file per size named by its size, and zip them for the client or the media team. |
| `update_project_facts` | Save a change to one product's facts (a price, an offer, a registration number, an address: each a label and the exact words a creative prints) as a new dated version. |
| `check_copy` | Check ad copy against the brand's rules before it is used: each line's length against the limit the brand's brief or content sheet sets, another project's legal line appearing by mistake, figures no project fact supports, and legal lines the creative must carry. |

## The brand and research

| Tool | What it does |
|---|---|
| `get_brand_overview` | Read who this brand is: name, category, audience, positioning, the rules it keeps, what the marketer has told eonik to do and not do (in their own words), the competitors it watches, and what changed among them recently. |
| `search_brand_memory` | Search what the marketer has told eonik about this brand (notes, brand truths, dated plans and recorded decisions) and return the matches with their original wording, the date, and whether each still holds. |
| `save_brand_note` | Save something the marketer wants eonik to remember about the brand, such as a rule, preference, decision or correction, exactly as they said it, and return the saved wording. |
| `save_dated_plan` | Save an upcoming dated event for the brand, such as a sale, launch or seasonal moment, with its dates. |
| `list_watched_competitors` | List the competitors eonik watches for this brand, with each one's id and how many of their ads have been captured on each channel (Meta, TikTok, Google/YouTube, Instagram). |
| `list_competitor_ads` | List the ads that watched competitors are running, newest first, with each ad's id, competitor, channel, the date the platform says it started, how many days it had been live when eonik last checked, its copy, and whether a scene-by-scene breakdown exists. |
| `get_competitor_activity` | List what changed among watched competitors in a recent window: new ads, stopped ads, ads that passed 30 days running, landing-page changes, discount emails and standout organic posts, each with its date and a one-line description. |
| `list_ad_breakdowns` | List the watched competitors' ads that already have a scene-by-scene breakdown, with each ad's id, competitor and channel. |
| `get_ad_breakdown` | Read the scene-by-scene breakdown of one competitor ad: transcript, scenes with timing, each shot's role and framing, and the hook. |
| `request_ad_breakdown` | Start a scene-by-scene breakdown of one competitor ad that does not have one yet; it is ready a few minutes later through get_ad_breakdown. |
| `list_my_ads` | List the brand's own Meta ads with their spend, click-through rate, status and creative traits over a recent window, highest spend first. |
| `get_my_ad_performance` | Read one of the brand's own Meta ads by name or id: total spend, impressions, clicks, click-through rate, cost per click and frequency over a recent window, with its creative traits. |
| `get_my_tested_history` | Read what the brand's own ad account has tried, grouped by creative trait (hook, format, length and more), with spend per trait and each ad's click-through rate compared to the account's own median. |
| `search_ad_library` | Search eonik's library of public ads from any advertiser, including brands this workspace does not watch, by advertiser, industry, opening style or creative style. |

## The team

| Tool | What it does |
|---|---|
| `get_activity` | Show what assistants did for this brand in eonik over a recent window: each request with when it was made, who made it, from which assistant, what was asked, how it ended and whether its result was checked. |

## Prompts

`adapts` · `where-are-we` · `facts-change` · `package` · `client-notes` · `check-package` · `versions` · `onboard` · `change` · `reel`: starts that need no typing.

## Guides

- `eonik://guide/where-are-we`: Where things stand
- `eonik://guide/adapts`: Adapts for a media plan
- `eonik://guide/change`: An exact change to a creative
- `eonik://guide/reel`: A static made into a reel
- `eonik://guide/versions`: Versions of one creative
- `eonik://guide/ads`: A new ad
- `eonik://guide/recreate`: An ad recreated with the brand's own
- `eonik://guide/client-notes`: The client's notes
- `eonik://guide/package`: Check, approve and deliver
- `eonik://guide/check-package`: A finished package checked
- `eonik://guide/facts-change`: A product's facts changed
- `eonik://guide/copy`: Ad copy
- `eonik://guide/onboard`: A brand's handover files
- `eonik://guide/brand-and-research`: The brand and what competitors run
- `eonik://guide/activity`: What assistants did

## Decisions

Making the sizes, keeping a change, approving, answering eonik's questions: these are the person's. They reach eonik as clicks in its panel (`answer_change`, `open_in_eonik`, `read_job`, `send_choice`, which a host shows only to the panel) or as forms your host shows. You cannot make them.
