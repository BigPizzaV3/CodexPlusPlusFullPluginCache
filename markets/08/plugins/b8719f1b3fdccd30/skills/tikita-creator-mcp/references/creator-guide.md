---
name: tikita-story-creator
description: Create, review, and improve Tikita interactive story drafts through Tikita MCP.
---

# Tikita Story Creator Guide

This guide is for AI tools connected to Tikita MCP. Use it when a creator asks you to create, review, or improve an interactive Tikita story draft.

Do not print OAuth access tokens, refresh tokens, authorization codes, raw JWTs, or private user data. Do not publish, delete, hide, or bulk-modify public content unless Tikita MCP explicitly exposes that action and the user explicitly asks for it.

## Connection

- MCP entry: https://mcp.tikita.ai
- MCP endpoint: https://mcp.tikita.ai/mcp
- Category reference: https://mcp.tikita.ai/guides/categories.json
- First MCP calls after login: `get_capabilities`, then read this guide if available as a resource.
- Draft writes should stay private and workspace-backed unless the tool description says otherwise.

## Good Tikita Stories

The creator chooses the premise, genre, pairing, tone, and subject. Do not override the creator's topic just because a different trope is popular.

Your job is to convert the creator's premise into a complete Tikita draft payload. Preserve the user's idea, then fill the fields that make the idea playable in Tikita: character public info, private secrets, episode content, transition conditions, example dialogs, first message, and chat starters.

If the creator has not provided a premise, ask for one before creating. Only choose the premise yourself when the creator explicitly delegates that choice.

Do not silently decide sensitive or identity-shaping axes the creator left open. If gender, romance pairing, age band, safety level, or relationship direction is unspecified and required for the draft, ask. If you can proceed without deciding it, use neutral wording and `gender: "unset"`.

Respect tone constraints literally. If the creator asks for a calm mystery romance, do not escalate into kidnapping, murder, gore, organized crime, or survival thriller just to create stakes. Use softer pressure such as a repeated object, an unsent message, an old promise, a delayed apology, a missing memory, or a private reason to keep returning.

A Tikita story is not a static synopsis. It is an interactive situation that must keep producing playable turns.

Every strong draft needs:

1. A clear user role.
2. A character who wants something from the user.
3. A reason the user cannot simply leave.
4. A secret, pressure, or emotional debt that can surface gradually.
5. A first scene that starts in the middle of a charged moment.
6. Operating rules that help the AI maintain tone, pacing, boundaries, and character consistency.

If a field only summarizes lore but does not help roleplay, shorten it or move it into a playable rule.

## Structural Baselines

Well-formed Tikita drafts vary widely in subject, but their field completeness shows useful operating baselines. Treat these as payload quality targets, not content formulas.

| Field | Practical target for a complete draft |
| --- | --- |
| `firstMessage` | Usually 700-1200 Korean characters; can be longer for ensemble/opening action scenes. It should use multiple short paragraphs, not one bare line. |
| `detailMd` | Often 400-2000 characters. This is the model's operating manual, so it should contain behavior, pacing, relationship, and format rules. |
| `characters` | At least 1. Ensembles commonly need 3-6. Every character needs both `character_intro` and `secret`; do not leave either blank. |
| `character_intro` | Public card text. Aim for 3-4 sentences, roughly 120-600 characters, with appearance, attitude, voice, and relationship to `{{user}}`. |
| `character.secret` | Private model-only card. Aim for 2-5 sentences, roughly 120-1000 characters, with a hidden motive, wound, plan, risk, or contradiction. |
| `episodes` | Complete MCP drafts should include at least 3 beats; strong creator drafts often use 5-8. Do not create empty episodes. |
| `episodes[].body_md` | Public episode content. Aim for 200-900 characters and write playable scene pressure, not chapter summary. |
| `episodes[].secret` | Private episode note. Aim for 100-700 characters and include unrevealed truth/subtext/pacing. |
| `episodes[].transition_condition` | Required for sequential route beats. Natural language, max 200 chars, with `{{user}}` or `{{charX}}` and a concrete action/emotional shift. |
| `dialogs` | 2-5 examples when character voice matters. Each should teach narration + dialogue grammar, not summarize plot. |
| `variables` | Optional. Many strong stories use none. Use 0-2 unless state tracking is central. |
| `images` | Text can be created first, but a publish-ready draft should plan thumbnail, character, scene, and secret images. |

## Category Rules

Use category names exactly as Tikita displays them. Do not use English slugs such as `romance`, `academy`, or `fantasy`. Use at most 3 categories.

| Category | Use when |
| --- | --- |
| 로맨스 판타지 | 초자연 로맨스, 빙의, 계약, 귀족/아카데미 판타지 |
| 일상 드라마 | 현대 일상, 직장, 동네, 감정 현실감, 반복 가능한 생활 공간 |
| 로맨스 | 설렘, 질투, 고백, 재회, 혐관, 관계 변화가 핵심일 때 |
| 학원/스포츠 | 학교, 캠퍼스, 동아리, 선수, 경기, 팀 경쟁 |
| 코믹/액션 | 코미디가 강한 액션, 소동극, 빠른 물리 장면 |
| 시대극/동양풍 | 궁중, 사극, 동양풍, 복고적 공간과 신분 질서 |
| 현대 판타지 | 현대 배경에 마법, 이능, 페로몬, 숨겨진 사회 규칙이 있을 때 |
| 무협 | 무림, 문파, 수련, 무공, 협객 윤리 |
| SF | 미래 기술, 안드로이드, 우주, AI 사회, 사이버펑크 |
| 미스터리/스릴러 | 비밀, 수사, 위험, 스토킹, 범죄, 생존 긴장 |
| 액션/어드벤처 | 임무, 전투, 탈출, 여정, 생존 |
| BL | 남성 간 로맨스가 핵심일 때 |
| GL | 여성 간 로맨스가 핵심일 때 |

Common combinations:

| Story shape | Categories |
| --- | --- |
| 캠퍼스 로맨스, 소꿉친구, 선후배, 삼각관계 | 로맨스, 학원/스포츠, 일상 드라마 |
| 스포츠 스타 또는 F1 로맨스 | 학원/스포츠, 일상 드라마, 로맨스 |
| 동네, 직장, 단골 가게 중심의 일상 슬로우번 | 로맨스, 일상 드라마 |
| 계약, 경호, 위험한 비밀이 있는 현대 로맨스 | 로맨스, 일상 드라마, 미스터리/스릴러 |
| 빙의/아카데미/초자연 규칙이 있는 판타지 로맨스 | 로맨스 판타지, 현대 판타지, 학원/스포츠 |
| 임무, 탈출, 생존 중심의 팀 액션 | 액션/어드벤처, 코믹/액션 |

## Creation Workflow

1. Confirm the creator's intent. Preserve any premise, pairing, safety level, language, and genre constraints they give. If the premise is missing, ask for it instead of inventing one.
2. Call `get_capabilities`. Use `whoami` only for diagnostics or account confirmation.
3. Read this guide and the category reference. Do not invent category slugs or omit required public/private fields.
4. Design the payload before writing: categories, tags, user role, first scene, character public/private cards, episode route beats, optional variables, example dialogs, and image plan.
5. Prefer one complete `story_create_draft` call when available. Do not create a shell draft with empty characters, empty episode bodies, missing secrets, or missing transition conditions.
6. Verify with `workspace_get_draft`. Check title, categories, tags, first message grammar, character public/private info, episode bodies/secrets/transition conditions, and example dialog count.
7. Patch obvious gaps before reporting completion. If the creator only asked for one-shot creation, still fill the full draft; do not ask the creator to manually fill basic system fields.

## Recover saved content and make small edits

If a long ChatGPT conversation no longer exposes earlier text, distinguish the host chat transcript from Tikita's saved story draft. Tikita MCP can retrieve an owned saved draft; it cannot retrieve the complete ChatGPT transcript.

- Locate an existing story with `story_list_my_stories` using `query` for a title/short ID and `offset` for later pages, or pass its Tikita `/create/<short_id>` or `/story/<short_id>` URL in `short_id`. The story list omits full workspace text by default. Use `workspace_list_items` to find saved opening, episode, character, variable, dialog, or applied lorebook ids. Use `workspace_get_item` for one exact item. Do not ask the creator to paste already saved episodes or lorebook entries.
- For one opening, character, episode, variable, or example-dialog change, use `workspace_patch_item` with only the changed fields and the item's id. Pass `expected_updated_at` from `workspace_get_item` when available. On `workspace_changed_retry`, re-read and reconcile before retrying. Use `workspace_update_story_metadata` with `return_mode: "summary"` for one story field.
- For a small wording change inside a long field such as `introHtml`, `detailMd`, an opening body, or a character secret, use `workspace_replace_text` with a unique literal `find` string and a short `replace` string. It rejects zero or multiple matches and returns lengths instead of the full field.
- For a reusable lorebook library entry, call `lorebook_list_library` with `summary_only: true` to find its id, then `lorebook_get_entry` and `lorebook_patch_entry` with only changed fields. Library changes reach live conversations after the creator saves in Studio; an applied workspace copy may remain stale until then.
- `workspace_patch_draft` replaces arrays. Set `return_mode: "summary"` for bulk writes unless full text is needed. It rejects omitted existing episode or lorebook ids unless `confirm_array_drop: true`; other arrays have no omission guard. Reserve it for deliberate bulk changes, read the full section first, and set deletion confirmation only when explicitly requested.
- Before a large edit or after `story_total_length_exceeded`, use `workspace_get_content_budget` to see the current total, maximum, and per-section counts without loading draft text. A size-limit error means Tikita rejected the edit without saving it; report the exact numbers and reduce the relevant content before retrying.
- Never label a summary or partial ChatGPT history as a complete Markdown transcript. A Markdown copy of Tikita content must name the exact retrieved fields and any omissions.

## Cinema (Visual Novel) Stories

Cinema stories play as a visual novel: fullscreen backgrounds, per-character expression sprites, and tap-to-advance beats. They need extra image assets before they can be published.

Create one with `story_create_draft` and `"isCinema": true` inside `story`. Cinema stories never use `story.primary_image_id` (it stays null); display images come from cinema thumbnails instead.

Cinema asset rules:

- Thumbnails: `cinema_set_thumbnails` replaces the draft thumbnail list (max 6). The first item becomes the main thumbnail. Each item references an owned completed `user_image_library.id`.
- Sprites: `cinema_set_character_sprites` replaces one character's expression sprite list. Every sprite needs a non-empty `expression` (unique per character, e.g. 기본, 미소, 분노, 슬픔) and an owned library image (`user_image_id`). Include a neutral 기본 expression first. A cinema story can have at most 200 sprites in total across all characters. `story_create_draft` and `workspace_patch_draft` also reject more than 200 sprites.
- Character ids: pass the workspace character id from `workspace_get_draft` (`characters[].id`).
- Publish gate: a public cinema story needs at least 1 thumbnail and at least 1 sprite for every character. Check readiness with `cinema_get_publish_gate_status` before reporting completion.
- Applying: MCP edits the workspace draft only. Sprites and thumbnails reach the live story when the creator saves the draft in Tikita studio; publishing also happens in studio.
- Do not edit the same draft with MCP while the creator is editing it in Tikita studio.

Recommended cinema workflow: create the cinema draft, upload or import images with `asset_*` tools, set sprites per character with `cinema_set_character_sprites`, set thumbnails with `cinema_set_thumbnails`, verify with `cinema_get_publish_gate_status`, then hand off to the creator for studio review and publishing.

## Field Guide

### title

Keep it short, memorable, and emotionally specific. Avoid generic labels like `로맨스 판타지 이야기`.

Good title shapes:

- Situation with tension: `고백 받던 중 두 번째 고백`
- Contradiction: `좋아하기엔 너무 싫은 사람`
- Role plus hook: `날 지키는 경호원`
- Place as promise: `3번 출구의 남자`

### tagline

The tagline is the click promise. It should create immediate relationship pressure in one sentence, usually 20-80 Korean characters.

Good shapes:

- `택배 말고 직거래 가능하세요?`
- `나 같은 아저씨 쫓아다니지 말고, 당신 또래 만나십시오.`
- `어릴 땐 귀여운 동생이라더니, 지금 그 눈빛은 뭐야?`

Avoid `흥미진진한 이야기가 시작됩니다` and other empty summaries.

### world

`world` is the playable reality, not a lore dump. Include where the story begins, who the user is, what rules matter, why scenes can repeat, and what choices the user can make.

### detailMd

`detailMd` is the operating manual for the roleplay engine. Include narration rules, relationship pacing, character consistency, scene operation, and any required output format such as group chat, SNS, status window, interview, team radio, or command mode.

### introMd

`introMd` is user-facing presentation. Sell the experience in 1-3 short sections. Do not put internal author notes here.

### introHtml

`introHtml` is the rich story detail presentation. Use it when the creator wants a polished detail page, when images are available, or when the premise needs more than plain markdown to sell the experience.

Polished Tikita HTML intros are mobile-first, visual, and substantial enough to make the premise feel playable. A strong rich intro often has 1,500-4,000 visible Korean characters, 5-10 visual or styled blocks, and 3-8 images when assets exist. The exact topic should come from the creator; the structure should support that topic rather than push it toward one genre.

Practical rich-intro lessons:

- They read like a polished story detail page, not a short plain synopsis wrapped in HTML.
- They usually combine hero art, mood images, character cards, short scene/rule blocks, and a final entry prompt.
- They are built with mobile-first `div`/`section`/`span`/`p`/`img` blocks and inline styles. Large tables, long bullet lists, and admin-like comparison grids are uncommon.
- Images do real work: they establish the setting, central relationship, object, world, or cast. Do not show one character with a polished avatar while another central character is text-only by accident.
- Copy layout grammar and completeness, not story content. Do not clone another story's premise, pairing, names, copy, or category mix.
- If the creator only gives a simple premise, keep the premise but make the HTML complete: user role, recurring pressure, cast, choices, mood sample, and first-scene invitation.

Design quality rules:

- Design for Tikita's story detail surface, not a generic marketing landing page. Keep the intro readable inside an existing app screen.
- Use one coherent palette and one accent color. Avoid mixing bright CTA blocks, light cards, dark cards, and multiple accent colors in the same intro.
- Do not dump large cards inside large cards. Prefer full-width sections, hairline separators, compact portrait rows, and short scene blocks.
- Avoid repeating the same hero image immediately after itself. If a cover already establishes the scene, use following images for cast, a different mood, or a specific object.
- Character cards should be balanced. For mobile, compact rows with 80-100px portraits often look better than three huge stacked image cards.
- Keep type restrained: inherit the app font, use 12-13px labels, 14-16px body text, 20-28px section titles, `line-height` around 1.65-1.8, and no negative letter spacing.
- Preview mentally at 390px width. If the intro becomes a long pile of heavy boxes, simplify before writing.

Recommended rich intro flow:

1. Hero hook: one compact, emotionally charged opening block with the title promise, time/place/relationship pressure, and the user's situation.
2. User role: explain who `{{user}}` is and what they can decide. Do not turn this into a synopsis.
3. Rules of the situation: recurring time, location, taboo, contract, mission, secret system, or relationship boundary.
4. Character cards: include every central character shown in the premise. If one character has an avatar card, peer characters should not look accidentally missing.
5. Playable choices: show concrete actions the user may take, preferably as short scenario cards rather than a dry feature list.
6. Mood sample: one short quote or scene fragment that demonstrates the first-message tone without spoiling the hidden truth.
7. Final CTA: a compact final block that points to the exact first scene.

HTML implementation rules:

- Use sanitizer-safe tags: `section`, `article`, `div`, `h2`, `h3`, `h4`, `p`, `ul`, `li`, `blockquote`, `details`, `summary`, `figure`, `img`, `span`, `strong`, `em`.
- Inline styles are allowed, but keep them mobile-safe: `border-radius:8px`, `padding`, `margin`, `display:grid`, `gap`, `background`, `border`, `color`, `font-size`, `line-height`.
- Do not rely on JavaScript, custom data attributes, iframes, forms, buttons, external CSS, or SVG.
- Images must use public Tikita/Supabase Storage URLs, `class="intro-html-img"`, meaningful `alt`, and explicit `width`/`height`.
- If using generated covers with Korean/Japanese/Chinese titles, generate a textless base and overlay exact typography outside the image model.
- Prefer styled cards and short blocks over large tables. Tables are acceptable for direct comparison, but they are uncommon in polished rich intros and can feel administrative.
- Keep spoilers out. The intro should sell pressures and choices, not reveal private character secrets or episode twists.

### firstMessage

The first message must start the story, not introduce the story.

Required format:

- Narration and actions use asterisks: `*비가 유리창을 두드린다.*`
- Character speech uses speaker labels: `{{char1}}: 대사`
- Do not write bare dialogue like `"그 우산, 열지 마."` without a speaker label.
- Use `{{user}}` whenever referring to the user by name. Never invent a user name.
- Use `{{char1}}`, `{{char2}}` placeholders in firstMessage when the speaker is a defined character.
- Avoid quote-only or novel-only prose. Tikita first messages work best as roleplay script: narration block, character line, reaction block, next pressure.

Checklist:

- Starts in a specific place and moment.
- Uses sensory detail.
- Shows at least one character doing something before or after speaking.
- Includes at least one speaker-labeled character line.
- Creates a question, pressure, invitation, or immediate social threat.
- Ends with room for the user to act, answer, hide, follow, refuse, or challenge.
- Uses `{{user}}` and character placeholders.

Suggested structure for Korean drafts:

1. 2-4 sentences of `*scene/action/sensory narration*`.
2. `{{char1}}: ...` one charged line that reveals attitude, not exposition.
3. Another narration block showing distance, gesture, group reaction, danger, or emotional contradiction.
4. A second character line or a concrete object/event that forces the next user action.

Avoid:

- Beginning with an encyclopedia of setting.
- Ending with a flat `무엇을 하시겠습니까?`.
- Bare quoted dialogue with no speaker.
- Dialogue that reveals the central secret immediately.
- Assigning the user a fixed name, personality, or action.

### chatStarters

Provide exactly 3 when possible. They should be concrete actions, not meta commands.

Good examples:

- `봉투의 별자리 문양을 자세히 살펴본다.`
- `무심한 말투 뒤의 속내를 떠본다.`
- `거래를 끝내고 돌아서려는 그를 붙잡는다.`

Avoid `시작하기`, `대화한다`, and `설명을 듣는다`.

## Character Guide

Use one strong lead for focused relationship, mystery, slice-of-life, or intimate drama stories; 3-6 characters for campus/group/reality-show/team stories; and 7-9 only for action or broad sandbox stories where each role is distinct.

Every character must have both public information and private information.

Use these exact payload fields:

- `name`: display name.
- `gender`: `female`, `male`, or `unset`. If the creator specified gender, obey it.
- `age`: integer or null. Respect the creator's age/safety constraints.
- `character_intro`: public character card shown to users.
- `secret`: private model-only information used during chat.

`character_intro` should include:

- Concrete appearance: height/build, hair, eyes, clothing, aura, or visual signature.
- Social role in the premise.
- Speech style and body language.
- Current relationship to `{{user}}`.
- The emotional pressure the user will feel when interacting with them.

If the creator did not specify a character's gender, avoid assigning a binary gender just to fit a trope. Use `gender: "unset"` and write the character in a way that still supports the requested relationship dynamic.

`secret` should include:

- Hidden motive, wound, guilt, debt, plan, or danger.
- What the character wants from `{{user}}` but will not say directly.
- What changes when the secret is discovered.
- Behavior rules for jealousy, threat, rejection, softened mood, or guilt.

Each character should include name, age/gender when relevant, visual signal, social role, speech style, what they want from the user, what they fear, what they hide, and how they behave when jealous, threatened, softened, or rejected.

A useful secret changes behavior and future scenes. `사실 착하다` is not enough.

## Episode Guide

Episodes are route beats, not forced chapters. They describe playable situations the model can move toward.

Recommended counts:

- Quick test: 3-5 episodes.
- Strong creator draft: 5-8 episodes.
- Route-heavy romance, mystery, quest, competition, or ensemble drama: 8-15 episodes.

Use these exact payload fields:

- `title`: max 20 characters. Short scene label.
- `body_md`: public episode content. Use markdown if useful, but keep it readable in the editor.
- `secret`: private episode note. This is required for model-only subtext and hidden reveal control.
- `transition_condition`: max 200 characters. Natural-language unlock/flow condition.

`body_md` should include:

- Where the episode can happen.
- Which characters are active.
- What pressure enters the scene.
- What the user can try.
- How this beat can continue without forcing a single user action.

`secret` should include:

- What is really happening behind the visible episode.
- What a character is hiding, testing, or avoiding.
- Which clue, emotion, or relationship shift should be delayed.
- How the AI should pace the reveal.

Match the creator's requested intensity. For calm, slice-of-life, or low-thriller premises, prefer emotionally grounded secrets over high-crime explanations.

`transition_condition` should be:

- One natural sentence under 50 characters.
- Contains `{{user}}` or `{{charX}}`.
- Mentions a concrete action, choice, trust shift, confrontation, confession, discovery, or refusal.
- No prefix like `조건:` or `전환 조건:`.

Good shapes:

- `{{user}}가 {{char1}}의 거짓말을 직접 추궁함`
- `{{char2}}가 {{user}}에게 숨긴 증거를 건넴`
- `{{user}}가 약속 장소에 혼자 가기로 선택함`

Each episode should have a short title, a scene setup, a conflict or pressure, possible user directions, hidden subtext, and a short transition condition.

## Variable Guide

Variables are optional. Use them only when state improves play: trust, suspicion, jealousy, danger, route, item, evidence, or score. A first draft often needs 0-2 variables.

## Dialog Guide

Example dialogs teach voice and pacing. Use 2-5 short examples. Show character voice, one sensory narration beat, and tension that does not reveal everything too early.

Required grammar:

- Narration: `*...*`
- Speech: `{{char1}}: ...`, `{{char2}}: ...`
- User reference: `{{user}}`, not an invented name.
- Keep examples short enough to be useful as style anchors, usually 80-500 characters each.

A good dialog example should show one reusable interaction pattern: teasing, refusal, jealousy, threat, apology avoidance, secret testing, group pressure, or protection.

Bad dialog examples:

- Pure synopsis with no actual speech.
- Bare quotes without speaker labels.
- Long monologues that reveal the twist.
- Generic flirt lines that fit any character.

## Image Planning

Do not delay a good text draft because images are missing. If image tools are available, use them only when the user wants assets handled.

Current MCP image-library tools are for upload, import, grouping, and workspace attachment. Use `asset_create_upload_slot` + upload bytes + `asset_finalize_upload` for local files, `asset_import_from_url` for external image URLs, and `asset_attach_to_workspace_draft` to attach completed library images to a story workspace.

Signed upload URLs are sensitive temporary credentials. Never print signed upload URLs, raw upload responses, storage tokens, Authorization headers, or raw MCP responses. Upload quietly, then summarize only the final image count, link type, descriptions, and workspace ID.

Recommended image workflow:

1. Finish the text draft first, then decide what images are actually useful: cover/thumbnail, main character avatars, public scene images, and optional secret images.
2. If image generation is paid, complete the cost confirmation flow below before generating. If the creator supplies local files or external URLs, use upload/import without paid generation.
3. For generated covers with Korean/Japanese/Chinese titles, prefer generating a textless image first, then apply exact typography in a deterministic editor or renderer. Do not rely on the image model to spell the title correctly.
4. Upload local files with `asset_create_upload_slot`, PUT bytes to the signed URL without displaying it, then call `asset_finalize_upload`. When the client can inspect the local file, pass exact width, per-frame height, and frame_count to the upload-slot tool so unsupported animations are rejected before upload.
5. An upload slot is not a library image. The library row is created only after `asset_finalize_upload` completes image processing and returns a terminal NSFW level (`sfw`, `soft_nsfw`, or `hard_nsfw`) with distinct original and locked URLs. Never attach or reference an upload-slot id before that success response.
6. If a tool returns `retryable: false`, do not retry the same upload or finalize call. Adjust the source file to the reported constraints and create a new upload slot. For a retryable processing error, retry only the existing finalize arguments instead of creating duplicate slots. If `retry_reason` is `storage_cleanup_failed`, retry finalize at most once after backoff only to complete cleanup.
7. Create groups with `asset_create_group` when the workspace needs organization, then move links with `asset_move_to_group`.
8. Patch references separately: set `story.thumbnail_image_id` and `story.primary_image_id` to the cover's completed `user_image_library.id`; set `characters[].avatar_image_id` to each completed character image's `user_image_library.id`.
9. Verify with `workspace_get_draft` and `asset_list_groups`.

Image group rules:

- Useful group names are concrete and creator-facing: `표지/대표 이미지`, `캐릭터 대표 이미지`, `장면/단서 이미지`, `비공개 단서 이미지`.
- `asset_create_group` returns a workspace-local group id. Reuse that returned id; do not invent ids unless the tool explicitly asks for one.
- `asset_move_to_group` uses workspace image link ids by default. If you only have `user_image_library.id` values, pass `match_by: "user_image_id"`.
- If you patch `characters`, fetch the current full character array first and replace the whole array with edited objects. Do not send only the changed characters unless the tool says it supports partial array merge.
- Secret images should usually stay `link_type: "secret"` and should not be used as the story thumbnail or public character avatar.

Useful image plan:

- Thumbnail: first-click promise.
- Character image: anchors the main relationship.
- Public scene image: shows the recurring environment.
- Secret image: unlockable emotional turn, confession, danger, or hidden side.

## Paid AI Image Generation

AI image generation is a paid creator feature when Tikita exposes it through MCP or when an AI agent uses a Tikita-paid generation endpoint. Do not start paid generation from a vague request like `make some images`.

Before calling any paid AI image generation tool, show the creator a short cost confirmation:

- Tool or model that will be used.
- Number of images, aspect ratio, quality, and whether regenerations are included.
- Cost per image in Tikita's displayed currency or credits.
- Current available balance if the MCP/tool exposes it.
- Maximum total cost for the requested batch.
- A concise prompt summary for each image or image group.

Then ask for explicit final approval and wait. The approval should be a separate user confirmation after the cost summary, such as `승인`, `진행`, or `Generate these 3 images`. If the tool cannot provide price or balance information, do not call the paid generator; ask the creator to confirm in Tikita UI or use upload/import instead.

After paid generation, attach outputs to the image library/workspace as drafts only. If quality is insufficient and another paid regeneration is needed, repeat the cost summary and get approval again.

## Quality Gate

Before calling a write tool, check:

- Title is specific and not generic.
- Tagline creates immediate emotional pressure.
- Categories are exact Tikita category names, max 3.
- Tags are 6-15 concrete discovery promises.
- World defines user role, place, rules, and recurring pressures.
- detailMd gives behavior, pacing, and format rules.
- introMd sells the premise.
- If `introMode` is `html`, `introHtml` is a rich mobile-first presentation with hook, user role, situation rules, character cards, choices, mood sample, and CTA.
- HTML intros are not sparse: if images exist, use them intentionally; if no images exist, compensate with strong styled scene/rule/cast blocks.
- Rich intro character cards include all central characters or intentionally explain omissions; no major character appears as a blank after peers have images.
- firstMessage starts in-scene, uses `*narration*`, uses `{{charX}}: speech`, includes `{{user}}`, and invites action.
- chatStarters are 3 concrete actions.
- Every character has non-empty `name`, `character_intro`, `secret`, `gender`, and age/null.
- Any unspecified gender or pairing axis stays neutral or is clarified before writing.
- `character_intro` is public-facing and includes appearance, voice, role, and relationship to `{{user}}`.
- `secret` is private-facing and contains hidden motive/risk, not a repeat of the public intro.
- Episodes, if present, use exact fields `title`, `body_md`, `secret`, `transition_condition`.
- Episode `body_md` is a playable situation, not only a summary.
- Episode `secret` contains hidden subtext/reveal pacing.
- Episode stakes match the requested tone and do not over-escalate the premise.
- Episode `transition_condition` is non-empty, <=50 characters, and mentions `{{user}}` or `{{charX}}`.
- Variables are only present when useful and use exact fields `name`, `var_type`, `default_value`, `description`.
- Dialogs use `*narration*` and `{{charX}}: speech` grammar.
- Image upload/import tools do not print signed URLs or raw storage responses.
- Upload-slot ids are not treated as library image ids until finalize returns completed plus a terminal NSFW level.
- Deterministic upload constraint errors (`retryable: false`) are not retried with the same source.
- Attached workspace images are grouped when the draft has multiple images.
- Story thumbnail uses `story.thumbnail_image_id`/`story.primary_image_id`, and character avatars use `characters[].avatar_image_id`; these are library image ids, not workspace link ids.
- Paid AI image generation has explicit creator approval after price, balance, and total cost are shown.

## Recommended `story_create_draft` Payload Shape

Use this structure when creating a complete draft. Keep the creator's premise, but fill every field that makes the premise playable. The strings below are shape examples, not valid minimum-length content.

```json
{
  "story": {
    "title": "string",
    "originalLanguage": "ko",
    "tagline": "string",
    "world": "string",
    "detailMd": "markdown string",
    "introMd": "markdown string",
    "introHtml": "optional rich HTML string",
    "introMode": "md|html",
    "firstMessage": "*narration*\n{{char1}}: speech\n*narration with {{user}}*",
    "chatStarters": ["concrete user action", "concrete question", "concrete refusal or probe"],
    "isAdult": false,
    "categories": ["로맨스", "일상 드라마"],
    "tags": ["string"],
    "creatorNotes": "Optional image plan or creator review notes",
    "episodeMode": "sequential",
    "chatImageMode": "background",
    "variableViewMode": "default",
    "monetizationMode": "full"
  },
  "characters": [
    {
      "id": "workspace-local-id",
      "name": "string",
      "gender": "female|male|unset",
      "age": 20,
      "character_intro": "Public card: appearance, role, speech style, relationship to {{user}}.",
      "secret": "Private model note: hidden motive, wound, plan, reveal pacing."
    }
  ],
  "episodes": [
    {
      "id": "workspace-local-id",
      "title": "20 chars max",
      "body_md": "Public playable episode beat.",
      "secret": "Private hidden truth and pacing note.",
      "transition_condition": "{{user}}가 단서를 직접 확인함"
    }
  ],
  "variables": [],
  "dialogs": [
    {
      "id": "workspace-local-id",
      "content": "*narration*\n{{char1}}: speech"
    }
  ],
  "images": [],
  "image_groups": [],
  "metadata": {}
}
```

Do not use alternative keys such as `body`, `setup`, `conflict`, `publicInfo`, `privateInfo`, or `transitionCondition` unless the tool explicitly says it accepts them. For Tikita workspace drafts, prefer exact keys: `character_intro`, `secret`, `body_md`, `transition_condition`.

## Defaults

- `originalLanguage`: `ko` unless the creator asks otherwise.
- `isAdult`: `false` unless the creator explicitly asks for adult content and Tikita policy allows it.
- `episodeMode`: `sequential`.
- `chatImageMode`: `background`.
- `variableViewMode`: `default`.
- `monetizationMode`: `full`.

## Reviewing Existing Drafts

When improving a draft, do not rewrite everything by default. Read the workspace, identify the weakest 3 areas, then patch surgically.

High-impact fixes:

- Replace a vague tagline.
- Rewrite the first message into an active scene.
- Add secrets to characters.
- Add 3 chat starters.
- Add 5 route episodes.
- Convert lore dump in `world` into operating rules in `detailMd`.
- Replace invalid category slugs with exact category names.

## Final Response To Creator

After creating or patching a draft, report the title, draft status, categories/tags, character/episode/dialog counts, and what remains for creator review. Do not expose raw MCP responses unless the creator asks for technical details.
