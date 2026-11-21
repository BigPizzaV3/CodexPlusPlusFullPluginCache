---
name: featpaper-mobile-summary
description: Use when the user wants a FeatPaper (피트페이퍼) mobile summary page (모바일 요약 페이지) made, added or changed for a document in their own FeatPaper account, given by a FeatPaper link (featpaper.com/u/…, /v/…, /l/…, /n/…) or just registered, including the question offering it right after a user's PDF is registered, the "모바일 요약 추가하기" choice and the "피트페이퍼 모바일 요약 — …" form message. Only for that phone page; not for reading or summarizing a FeatPaper link in the chat, and not for summaries that have nothing to do with FeatPaper.
---

# FeatPaper mobile summary page

Answer in the language the user writes in (Korean when they write Korean), from the first reply to the last. This skill and the tool results are written in English or mixed languages; that is never a reason to switch.

A mobile summary page sits on top of a document already in FeatPaper (registered with the featpaper skill): phone readers of the same link see it first and open the PC pages from it. It has no link of its own. Right after a user's PDF is registered without a summary (and, for an image-only PDF, after the featpaper skill's section 5 A has read its pages and attached the source), the answer shows its link once and ends with ChatGPT's built-in choice question "모바일 요약도 공유 링크에 추가할까요?" ("모바일 요약 추가하기" first and preselected / "지금 유지하기"), as the featpaper skill's section 5 A says; never skip it. Registering a user's PDF (counting its page text and, when more than half the pages have little or no text, reading them and attaching the source before answering) follows the featpaper skill's section 5 A: read that skill first. A document made in this chat and not yet in FeatPaper is registered first, as the featpaper skill says (read that skill for it). Before building one, call `get_mobile_summary(linkKey=<documentId>)` once: its "preset" (F) and "pageMedia" (D) shape the summary.

When this conversation already attached a source to the document (a document made here, an AI hub request, a PDF with little or no text read at registration, or the AI-made PDF case of the featpaper skill), skip step B and the page-source step of C3 and build the mobile summary from that source (for a document made here, from the latest content). If the summary is then refused for the page source, add one line for each photo or figure to that same source, attach it again the same way, and never replace it with a source from B.

## Reading the pages

B) Reading every page once with vision (the AI hub source; it replaces the text FeatPaper extracted on its own): do it once for every PDF, at registration when its pages carry little or no text (featpaper skill, section 5 A), otherwise in the mobile summary turn after the form. Never use OCR tools. Render every page to an image with code (about 100–150 dpi, 1–2 pages per image so small text stays legible) and look at each one; use the PDF's own text layer only to check spelling and numbers. For each page write `## p.N title`, then transcribe what the page shows, never a one-line description: headings, body text and captions, every table as a Markdown table with all its cells, every chart's title, axis labels, legend and values, and one short line for each photo or illustration. Keep each page under 1,400 characters outside ```json blocks, and start the file with the provenance line in the document's language (`> FeatPaper: 이 원본은 올린 PDF를 AI가 읽어 옮긴 것입니다. 원문은 PDF입니다.`). Upload it with upload_conversation_files(source_file, source_origin=reconstructed_from_pdf) and call attach_document_source(linkKey=<documentId>, fileId=sourceFileId); if pageCheck reports an unknown page count, attach the same fileId again in this same turn, before answering. Never skip pages to save time. In the mobile summary turn: show the form (C1) first without reading; after the form's message, do B and then C2–C4 in the same turn.

## Building and attaching the summary

C) Mobile summary page.

C1) Ask once, before reading or writing anything, with ChatGPT's built-in form UI, not a text list: checkboxes for sections (several can be picked), single-choice options for images and for length, a text field for extra requests, and a submit button. Our recommendations are preselected so the user can submit it as is: Sections: 3–6 candidate sections drawn from this document (for example cover/intro, each main project or topic, key numbers, contact/next step). Mark the ones you recommend and say in a few words why (what a phone reader needs first). Images: "이미지 크게" (page images lead each section) / "이미지 적당히" (one image per section) / "글 위주" (text first, images small). Recommend one that fits the document: image-heavy documents such as portfolios lead with images. Length: "짧게" (about 1 minute) / "보통" (about 3 minutes) / "자세히" (about 5 minutes). Let the user add sections of their own: a text field "추가할 섹션" (for example "가격표, 문의처"). Extra requests: a text field (for example "연락처 꼭 넣어줘"). The message the form sends is only the picks and starts with the app's name (ChatGPT gives FeatPaper's tools only to turns that name it), in this shape: "피트페이퍼 모바일 요약 — 섹션: 표지, 프로젝트 A, 연락처 (+ 가격표) · 이미지 크게 · 보통 · 추가 요청: 없음". Nothing else goes into it: no sentence asking for a preview, an HTML file or editing, and nothing about attaching or not attaching. What happens next is this skill's job, not the user's words.

C2) First call get_mobile_summary(linkKey=<documentId>) once and follow its preset if it has one (F). Do not call featpaper_guide for the summary: most of its text is a preview kit for previews this flow never makes, and it fills the conversation so the user can no longer ask for changes. Use the markup in C5 and build the final file at once. Build it from step B (never read all the pages again); look again only at the cover and 2–3 key page images for the look, and carry the document's own identity into the brand tokens in C5: its typeface (load the closest Google web font over https, never fall back to Arial or system fonts when the document uses a distinct face), paper color, accent color, corner radius and mood. The form only decides what goes in; the look is your judgment from the document, exactly as when no form is used. Then: FeatPaper markup, PC page numbers per section, real page images from the document through the image block in C5 (an empty <img> in the fpx-crop button with data-fp-open-page and a 0–1 data-fp-crop: FeatPaper fills in that page's own image; never write an image address, a CloudFront path or a data: image yourself), and no preview kit, <script>, event attribute or iframe. Captions say what the image shows in a few words; never generic captions such as "원본 7쪽의 광고 이미지와 설명". Write the summary in the document's own language (an English document gets an English summary), unless the user asks for another language; the form, questions and answers to the user stay in the user's language. Color the first screen only through the mood class and the theme-color meta (FeatPaper turns theme-color into its accent; for a black cover, theme-color is that black). mood-bold puts white text on theme-color, so with mood-bold theme-color must be a strong color white text reads on (contrast 4.5:1 or more, such as the brand's deep green rather than a pale mint); when the document's color is pale, use mood-soft with that pale color instead; never set background or text colors on `.fpx-*` classes in your own CSS: on the link FeatPaper's styles load after yours, so a dark cover turns white with white text there while the preview still looks right. Page images exist only after FeatPaper finishes converting the PDF: if the document panel cannot show a page image yet, wait and check again before attaching.

C3) Attach the page source (step B) before the summary: FeatPaper refuses a summary for a document without a vision-read source. Do not preview it inside ChatGPT (ChatGPT's own preview cannot load FeatPaper page images and often never appears): write the summary to an .html file with code (for example /mnt/data/summary.html) and pass that file as the mobile_summary_file file argument of upload_conversation_files, exactly as the source file is passed: never put HTML text, a name or a made-up path in the argument (FeatPaper's tools only take files that exist in the conversation, and text in the argument is refused). Then call attach_mobile_summary(linkKey=<documentId>, fileId) right away. If a check refuses it, fix only what the check names, in the same turn, and attach again; if it refuses for the page source, do B properly on every page right away (never a short or partial source) and fix it in the same turn; tell the user only if it still fails. If the attach is refused because the monthly uploads are used up, say so in one sentence with the link the refusal gives and stop. Then answer in two short sentences at most, and nothing else: the summary is on the same link and shows first when that link is opened on a phone (for example "모바일 요약을 붙였어요. 같은 링크를 휴대폰에서 열면 먼저 보여요."). Do not write the link again and do not add a sentence about asking for changes: the choice below already offers that. No check results, numbers, file or section lists, and never put editing controls in the file (no edit bar, save button or contenteditable).

C4) With the answer, ask once with the built-in choice UI: "이대로 둘게요" preselected / "피트페이퍼 요약 더 수정하기" (the option names the app for the same reason). The choice sends only itself. On "피트페이퍼 요약 더 수정하기" or any change request: change only what was asked in the same file, upload it and attach it again (attaching replaces the previous summary), and answer again in one sentence.

C5) Summary markup: follow FeatPaper's mobile-summary rules below exactly (they are the featpaper_guide(topic=mobile-summary) rules without its preview kit, which this flow does not use). Videos and GIFs from pageMedia follow D instead of the image block.

#### 0. 한 줄 요약

원본 문서의 **내용과 브랜드**(언어 · 색 · 라운드 · 글꼴 · 분위기)는 그대로 가져오고, **읽는 구조와 크기 · 여백**은
아래 FeatPaper 규칙(정해진 클래스)으로만 짠다. 섹션 구성은 정해져 있지 않다 — **그 문서의 흐름대로** 나눈다.

#### 1. 결과물 (ChatGPT, 미리보기 없음)
- HTML 파일 하나. 섹션마다 단 `data-page` 가 FeatPaper 뷰어에서 원본 쪽 구분과 원본으로 넘어가는 길이 된다(섹션 끝 [원문 보기]). 원본 순서대로, 그 섹션이 다룬 쪽 번호를 정확히 단다.
- `<script>` · 이벤트 속성(`onclick` 등) · `<iframe>` · 미리보기 키트를 넣지 않는다. 글꼴은 `https://` 주소만.
- 쪽 그림은 주소를 쓰지 않는다 — 3-3 의 그림 블록처럼 `img` 를 비워 두면 뷰어가 그 문서의 쪽 그림(파워포인트 플러그인 문서 포함)을 채우고 `data-fp-crop`(0~1) 만큼 잘라 휴대폰 폭에 맞춘다. 주소를 만들어 넣으면 깨지거나 흐려진다.

#### 2. 원본에서 가져오는 것 (브랜드 토큰)

`<head>` 에 아래 두 가지만 쓴다. **값은 원본 문서에서 읽는다** — 예시 값을 그대로 쓰지 않는다.

```html
<html lang="ko">                         <!-- 원본 문서의 언어(ko · en · ja …). 본문도 그 언어로 쓴다 — 사용자가 다른 언어를 요청했을 때만 그 언어 -->
<title>표지에 적힌 문서 제목</title>          <!-- 꼬리말에 그대로 쓰인다. 파일명이 아니라 사람이 읽는 제목: 밑줄 · 대괄호 · 버전 표기(v1.4 · Official) · 언어 태그(KOREAN) · 확장자를 빼고, 표지 제목이 없으면 파일명을 띄어 쓴 짧은 제목. 휴대폰 한 줄 안팎(40자 안팎). "Mobile Summary" 같은 말을 붙이지 않는다 -->
<meta name="theme-color" content="#0F62FE">  <!-- 대표색(원본의 강조색 하나) — 이 값 하나가 대표색의 기준이다 -->
<style>
:root{
  --fp-radius: 28px;        /* 원본 카드 · 도형의 모서리. 각진 문서는 0~4px, 둥근 문서는 16~32px */
  --fp-font: "Pretendard", sans-serif;          /* 원본 본문 글꼴(웹 글꼴이 없으면 가장 가까운 것) */
  --fp-font-display: "Pretendard", sans-serif;  /* 원본 제목 글꼴(명조 제목이면 명조) */
  --fp-text: #1D1D1F;       /* 본문 글자색(원본이 쓰는 검정 계열) */
  --fp-muted: #6E6E73;      /* 보조 글자색 */
  --fp-surface: #FFFFFF;    /* 기본 바탕 */
  --fp-surface-alt: #F5F5F7;/* 번갈아 깔리는 둘째 바탕(원본의 옅은 바탕색 계열) */
}
</style>
<!-- 원본 글꼴이 웹 글꼴이면 https 로 불러온다(예: Google Fonts) -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=...">
```

- 그 밖의 CSS 는 쓰지 않는다. **크기 · 여백 · 카드 모양은 FeatPaper 가 넣는다**(아래 클래스). 브랜드는 토큰으로만 바꾼다.
- 원본에 보조색이 있으면 차트의 `colors` 에 쓴다(4번).
- 바탕과 글자의 대비는 읽을 수 있게 유지한다(어두운 바탕 문서여도 본문 바탕은 밝게, 대신 `mood-bold` 로 첫 화면을 원본 색으로).

#### 3. 구조 (FeatPaper 규칙)

```
<body class="fpx mood-clean">        ← mood: 원본 표지를 보고 고른다. 표지 바탕이 대표색이면 bold, 옅은 색이면 soft, 흰 바탕이면 clean
  <main>
    첫 화면  section.fpx-stage         ← 원본 1쪽(표지)
    섹션들   section.fpx-sec × N        ← 원본의 흐름 순서대로, 원본 쪽 번호를 단다
  </main>
</body>
```

**만들지 않는 것** — 뷰어가 자리에 맞게 넣는다: 원문 보기 버튼(섹션마다 끝에), 꼬리말(맨 끝), 머리줄 · 하단 툴바 ·
문의 버튼, 목차. 비슷한 것을 직접 그리지 않는다.
`fp-` 로 시작하는 클래스(키트 CSS 의 `fp-open` · `fp-table` 등)와 `fpx-foot` · `data-fp-section` 은 뷰어 전용 이름이다 — 키트에서 베껴 쓰지 않는다.

##### 3-1. 첫 화면

```html
<section class="fpx-stage" data-page="1" data-fp-open="none" data-fp-nav-label="개요" data-section-title="문서 제목">
  <p class="fpx-kicker" data-reveal>회사명<i></i>문서 종류</p>
  <h1 class="fpx-hero" data-reveal>문서 제목</h1>
  <p class="fpx-lead" data-reveal>이 문서가 말하는 것을 한두 문장으로</p>
  <ul class="fpx-tags" data-reveal><li>키워드</li><li>키워드</li></ul>     <!-- 있으면 2~4개 -->
  [수치 카드 갤러리 — 원본에 핵심 숫자가 있을 때만, 2~4개]
</section>
```

- 첫 화면에는 위 네 가지만 둔다(문단 · 목록 · 단서 문장을 넣지 않는다).
- 제목은 원본 표지의 제목. 휴대폰에서 3줄을 넘으면 원본의 짧은 표현을 쓴다. 줄바꿈(`<br>`)은 넣지 않는다.

##### 3-2. 섹션

```html
<section class="fpx-sec tone-gray" data-page="3-4" data-section-title="결론 한 문장" data-fp-nav-label="짧은 목차 이름">
  <div class="fpx-sec-head"><span class="fpx-eyebrow">01<i></i>짧은 목차 이름</span></div>
  <h2 class="fpx-title" data-reveal>이 쪽들이 말하는 결론 한 문장</h2>
  [근거 블록들 — 3-3 에서 원본 내용에 맞는 것만 고른다]
</section>
```

- `data-page` (**필수**): 이 섹션이 다룬 원본 쪽. 한 쪽 `"3"`, 여러 쪽 `"3-4"`. 슬라이드면 슬라이드 번호.
  원본 순서를 지키고, 원본의 모든 쪽이 어느 섹션엔가 들어가게 한다(표지 1쪽은 첫 화면).
- 바탕은 `tone-gray` → `tone-white` → `tone-gray` … 로 **번갈아** 단다(첫 섹션이 gray).
- 섹션 수는 원본 내용 단위대로(보통 3~8개). 쪽마다 하나씩 기계적으로 나누지 않는다 — 한 이야기를 하는 쪽들은 묶는다.
- `data-fp-nav-label`: 목차에 서는 짧은 이름(12자 안팎). `fpx-eyebrow` 의 이름과 같게.
- `fpx-title`: 제목을 옮기지 말고 **그 쪽들의 결론**을 한 문장으로(예: "현황" → "검사의 62%를 아직 사람이 합니다").
  휴대폰에서 3줄 안(한국어 30자 · 영어 60자 안팎).
- **한 섹션의 근거 블록은 4개까지.** 수치 카드 갤러리는 섹션에 하나, 표 · 그래프는 합쳐 두 개까지. 더 있으면
  가장 중요한 것만 남긴다(나머지는 원문에 있고, 뷰어가 원문 버튼을 붙인다). 쪽이 많아 넘치면 섹션을 나눈다.

##### 3-3. 근거 블록 (고르는 것)

| 원본에 있는 것 | 블록 |
|---|---|
| 설명 문단 | `<p class="fpx-body" data-reveal>…<strong>강조</strong>…</p>` (짧게, 2~3문장) |
| 소제목 | `<h3 class="fpx-sub" data-reveal>…</h3>` |
| 항목 나열 | `<ul class="fpx-list" data-reveal><li><span class="fpx-mark"></span><span>항목</span></li>…</ul>` |
| 순서 · 단계 | `<ul class="fpx-list is-ordered" data-reveal><li><span class="fpx-mark">1</span><span>단계</span></li>…</ul>` |
| 핵심 숫자 2~4개 | 수치 카드 갤러리(아래) |
| 표 | `<div class="fpx-panel" data-reveal><table><thead><tr><th>…</th></tr></thead><tbody><tr><td>…</td></tr></tbody></table></div>` — 첫 열은 항목 이름, 숫자 열의 `th` · `td` 에 `class="num"` |
| 그래프 | `<div class="fpx-panel" data-reveal><figure data-fp-chart='{"type":"bar","title":"…","unit":"억 원","x":["1Q","2Q"],"series":[{"name":"…","values":[1.2,3.4]}],"colors":["#0F62FE","#FF832B"]}'></figure></div>` — `type` 은 bar · line, 값은 숫자(원본 그대로), `colors` 는 원본 계열 색(없으면 생략) |
| 한 줄 메시지 · 인용 | `<blockquote class="fpx-statement" data-reveal>…<strong>강조</strong>…</blockquote>` — 두 줄 안팎. 인용이면 말한 사람은 뒤에 `fpx-note` 로 |
| 출처 · 단서 · 가정 · 각주 | `<p class="fpx-note">…</p>` — 섹션 맨 아래에 **하나**로 모은다. 문단마다 단서를 붙이지 않는다 |
| 원본의 그림 · 도표를 그대로 보여 줄 때 | `<figure class="fpx-media" data-reveal><button type="button" class="fpx-crop" data-fp-open-page="4" data-fp-crop="0.05,0.2,0.9,0.5"><img alt=""></button><figcaption>설명</figcaption></figure>` — `img` 에 src 를 쓰지 않는다(뷰어가 그 쪽 그림을 채운다). crop 은 쪽 안의 x,y,너비,높이(0~1) |

수치 카드 갤러리:

```html
<div class="fpx-gallery" data-reveal><ul class="fpx-track">
  <li class="fpx-tile"><b class="fpx-figure">62%</b><span class="fpx-tile-label">수작업 검사 비중</span><small class="fpx-tile-note">2026년 상반기</small></li>
</ul></div>
```

#### 4. 지켜야 할 것

1. **지어내지 않는다.** 숫자 · 표 칸 · 그래프 값은 원본에 있는 것만, 원본 그대로 쓴다. 없으면 그 블록을 쓰지 않는다.
   그래프 값을 그림에서 어림했으면 쓰지 않는다(표 · 본문에 숫자로 적힌 것만).
2. 원본의 말투 · 용어 · 고유명사를 유지한다. 번역하지 않는다(원본 언어 그대로 — 사용자가 다른 언어를 요청했을 때만 번역).
3. 요약은 원본을 대신하지 않는다 — 결론과 근거를 빠르게 읽게 하고, 자세한 것은 원본으로 보낸다(버튼은 뷰어가 붙인다).
4. 위 클래스 밖의 레이아웃(직접 만든 카드 · 그리드 · 고정 위치 요소 · 큰 배경 이미지)을 쓰지 않는다.
5. 글은 휴대폰 한 화면 기준으로 짧게. 문단은 2문장 안, 목록은 5개 안. 목록 한 줄은 `<strong>머리말</strong>` + 한 문장
   (한국어 40자 · 영어 80자 안팎).

#### 5. 내기 전에 확인

- [ ] `<html lang>` · `theme-color` · `:root` 토큰이 원본에서 읽은 값이다
- [ ] `<body class="fpx mood-…">` 안에 `<main>` 하나
- [ ] 첫 화면 `section.fpx-stage data-page="1"`, 나머지 섹션은 모두 `section.fpx-sec` + `data-page` + `data-section-title` + `data-fp-nav-label`
- [ ] 섹션이 원본 순서이고, 원본의 모든 쪽이 어느 섹션엔가 들어갔다
- [ ] 바탕이 gray / white 로 번갈아
- [ ] 섹션마다 근거 블록 4개 이하, 단서 · 출처는 `fpx-note` 하나로
- [ ] `<title>` 이 표지의 문서 제목이다(파일명 · 밑줄 · 버전 표기 없음, 40자 안팎)
- [ ] 모든 숫자가 원본에 있다
- [ ] 원문 버튼 · 꼬리말 · 외부 레이아웃 · `<script>` · 이벤트 속성 · `<iframe>` 이 없다(키트도 넣지 않는다)
- [ ] 쪽 그림 `img` 에 src 를 쓰지 않았다(영상 poster 만 주소)

## A FeatPaper link, brand presets

D) When the user asks for a mobile summary of a FeatPaper link (featpaper.com/v/…, /u/…, /l/…, /n/…) instead of a file (only then: a plain request to read or summarize a link is not this skill), keep that document and its link: never register it again or upload a new version. Keep each step short: no extra status checks, no second reading of the same pages. Check ownership before anything else: take the document id from the link (a /u/ share code does not carry it: open the link once with featpaper_read_document only to learn its documentId, and use nothing else from that result until ownership is confirmed) and call get_document. If it fails or the document is not in the connected account, answer in one sentence that this document is not in the connected FeatPaper account (for example "이 문서는 연결된 피트페이퍼 계정에 없어서 요약할 수 없어요.") and stop; never guess why (deleted, private, shared by someone else or a permission problem) and never mention files or uploads: never read it any further (no more featpaper_read_document, no download, no summary of what was already returned) and never use another document with a similar name. Then call get_mobile_summary(linkKey) once (its preset, F, and its pageMedia, used below) and show the form (C1) right away, leaving out what the preset fixes, with candidate sections from what get_document and a quick featpaper_read_document give. After the form, in one pass: the summary is always built from a vision reading of the pages (the AI hub source). Check it with get_document_source: if a source is attached and it is about 400 bytes or more per page (numPages from get_document), the pages were already read with vision, so reuse it: featpaper_read_document serves that source as the document's text, so read it once in this turn with featpaper_read_document (earlier turns' tool results are gone; follow nextFrom only if it stopped early), build the summary from that text, and do not read, download or parse the pages again (get_document_source gives only the size). Otherwise do B on this document first: get the original PDF with get_document_download and render it in code; if the download does not work, look at the pages with featpaper_view_page (4 pages per call) instead. Attach the source as in B, then build the summary from it. Use the media placed on its pages from that get_mobile_summary result (do not call it again in C2): its "pageMedia" lists { page, type: video | gif, url, autoPlay, box } in page order; box is where the media sits on the page in percent (x, y, width, height), the same form as the page image address's region=x,y,w,h. Every summary section whose pages carry a video leads with the video itself instead of that page's image, so the reader sees the moving ad first and the explanation under it: <figure class="fpx-media"><video src="<url exactly as listed>" autoplay muted loop playsinline controls preload="metadata" poster="https://feat.page/u/<share code>/ai/region?page=N&region=<the video's box x,y,width,height in percent, as listed>&view=crop" style="display:block;width:100%;max-height:70vh;object-fit:contain;border-radius:var(--fp-radius);background:#000"></video><figcaption>what the video shows, in a few words</figcaption></figure>. If a page has several videos, use the largest one that autoplays (by box), at most two per section. A GIF goes in the same place as <figure class="fpx-media" data-reveal><img src="<url exactly as listed>" alt="" style="display:block;width:100%;height:auto;border-radius:var(--fp-radius)"><figcaption>…</figcaption></figure>. Never put a link to the original page instead of the media and never an iframe; these files are FeatPaper's own, so the rule against outside requests does not apply to them. Then C2–C4 for that document (attach_mobile_summary with its linkKey). A summary already attached to the document is never a reason to stop: always build a new one from the form's picks and attach it (attaching replaces it).

F) Brand preset: some FeatPaper teams fix how their summaries look. When get_mobile_summary returns "preset", it comes before the document's own look and before the form's picks: write in preset.picks.language; when picks.sections is given, write exactly those sections, one each, in that order — this order wins over the original page order, so a section may point back to an earlier page — and add no others; each section's data-page is the pages that hold its content, and its text is that content as printed there (for a contact section the actual name, email, phone or link), never a pointer such as "see the original" — if the document has nothing for a preset section, leave that section out; use picks.images (large = 이미지 크게, medium = 이미지 적당히, text = 글 위주: text leads, but every section whose pages are mainly pictures still keeps one small page image after its text) and picks.length (short = 짧게, normal = 보통, long = 자세히). The form asks only what the preset leaves open, and it is never skipped: when the preset fixes sections, images and length, the form is only the extra-requests text field and its submit button (no "추가할 섹션" field when picks.sections is given), shown before any reading, and its message still starts with the app's name, for example "피트페이퍼 모바일 요약 — 추가 요청: 없음". FeatPaper adds the preset's brand (colors, corner radius, mood), fonts and required notes itself when the summary is attached: do not copy them into the file and do not mention the preset to the user. If an attach check names the preset's language, rewrite the text in that language and attach again.
