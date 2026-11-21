---
name: email-html-rules
description: Write or change the HTML of an Apsis Vega email so it renders as intended in every inbox, Outlook included. Use when the user wants to draft, create, design, lay out or edit an email or its content, or when the email-campaign skill reaches the step of writing the content. Covers the layout shell, inline styles, the mobile classes, buttons, images, fonts and a known-good skeleton.
---

Apsis Vega works on the user's Apsis account. The company is Apsis, with a capital A and the rest in lower case, never in all capitals, and the product is Apsis Vega. Once the user has picked an account and a section, pass the same `account` and `section` to every later call. When a tool result asks for the user's go-ahead, say what the next call would do and wait for their answer in a new message. The user's explicit instructions take priority over this skill, and a tool's own refusals and notes always apply.

# Apsis email HTML — authoring rules

Read this before writing HTML for `plan_email_activity`, `create_email_activity` or `edit_email_activity`.

Authored HTML is rewritten before delivery. The rewrite is silent — no error, no warning — and the
preview shows its result, so check the preview. Follow this document and the first draft will be sound.

**The preview is a browser render.** It shows what the rewrite did, not what Outlook for Windows
does with it. Failures specific to Outlook classic (section 6) appear only in a test send to an
Outlook classic inbox, and the preview and Outlook can disagree in either direction. Anything built
outside the patterns in section 3 needs that test send before it goes out.

---

## 1. The shape of what you write

**Write a fragment, not a document.** Your HTML is inserted into a cell of the platform's
own 600px table shell. The shell already has its `<html>`, `<head>` and `<body>`. Document-level tags
you supply are not rejected — they are relocated into the body as stray elements inside a cell, which
some clients render as visible text at the top of the email. So: no `<html>`, `<head>`, `<body>`,
`<meta>` or `<title>`.

**Your whole toolkit is inline `style` attributes plus the built-in classes in section 3.**
Every `<style>` block is stripped, all of them, with no diagnostic. Everything that can
only live in a stylesheet goes with it: media queries, `@import` and web fonts, `:hover`, and
`prefers-color-scheme`. There is no way to change the 600px mobile breakpoint and no way to ship a
dark-mode variant.

Two more that don't follow from either rule above and so have to be stated:

- **Inline `!important` is stripped.** Yours, not the platform's — the injected stylesheet
uses `!important` freely and you cannot outrank it.
- **Conditional comments are removed from authored HTML.** See section 5.

**Top-level table at `width="100%"`.** The platform supplies the 600px container; a nested
600px table plus side padding overflows it. The outer page background and the white container belong
to the shell and can't be changed from here.

**Defaults are injected into anything that omits them.** `text-align:left` into every
`<td>`/`<th>` with no `text-align`, `font-weight:400` into every cell with no `font-weight`, and
`border-spacing:0` into every table. Hence rules 2.1 and 2.2.

**When building from a reference design, its layout is the spec.** Buttons on a shared baseline,
equal card heights and centred logos are part of what was asked for, not polish to drop. If a detail
can't be built with the rules and patterns here, tell the user which one before submitting. Never
drop it silently, and never improvise a construct the skill doesn't cover without saying so.

---

## 2. Rules that cost a send

Apply these by construction. Each fails silently.

**2.1 — Declare `text-align` inline on every cell, including left-aligned ones.**
`align="center"` as an attribute is not enough; the injected `text-align:left` wins wherever CSS
beats presentational attributes, which is most places.

**2.2 — Declare `color:` inline on every anchor.** `a { color:#000; text-decoration:none }`
is always in force, so a bare anchor renders as black body text nobody reads as a link. Add `<u>` or
`text-decoration:underline` if it should look like one.

**2.3 — Put `m-full-width` on every fixed-width table, and on every image meant to fill its
column, by hand.** Elements built in the Apsis editor get a generated wrapper that handles this;
authored HTML has none. Omitting it side-scrolls on every phone. Images narrower than a phone —
logos, icons, headshots, badges — get no width class and keep their pixel width. On those,
`m-full-width` stretches them to the full width of the phone.

**2.4 — Give every image its own cell, with `class="imgfix"` on the cell and `display:block` on
the image.** Otherwise a line-height gap opens beneath it. `class="imgfix"` sets `font-size:0` and
`line-height:0` on the cell, so text sharing the cell collapses with it. An image that sits next to
text, such as a headshot beside a name, goes in a cell of its own: a separate row or a nested table.

**2.5 — Every image with `m-full-width` also gets `height:auto` inline.** Keep both the `width`
and `height` attributes. Outlook classic sizes images from the attributes, and the mobile classes
never fire there. Every other client takes `height:auto` and scales the height with the width.
Without it the `height` attribute holds while `m-full-width` widens the image, and it distorts on
mobile.

---

## 3. The class vocabulary

All `m-` classes fire only at `max-width:600px`. `class="imgfix"` applies at every width. Verified present in
the delivered stylesheet and observed firing in Outlook classic, Outlook web, Outlook
mobile and a narrow browser.

### Width
| Class | Effect |
|---|---|
| `m-full-width` | `width:100%` — required by hand per rule 2.3 |
| `m-half-width` | `width:50%` |
| `m-width-10` … `m-width-100` | `width:N%`, every integer 10–100 |
| `img.m-full-width`, `img.m-true-size` | image-specific width overrides |
| `img.d-full-width`, `img.d-true-size` | desktop equivalents, not media-scoped |

### Display
| Class | Effect |
|---|---|
| `m-block` | `display:block` — the stacking primitive |
| `m-show` | `display:block` (pair with an inline `display:none`) |
| `m-hide` | `display:none` |
| `m-inline-block` | `display:inline-block` |
| `m-inline` | `display:inline` |
| `m-table` | `display:table` |
| `m-top-column` | `display:table-header-group` — reverses source order on mobile |
| `m-table-unstacked` | `table-layout:fixed` |

### Spacing and alignment
| Class | Effect |
|---|---|
| `m-p-t-N`, `m-p-r-N`, `m-p-b-N`, `m-p-l-N` | mobile padding per side, **N ∈ 0–15 only** |
| `m-vertical-spacing` | `padding-bottom:10px` |
| `m-align-center` | `text-align:center !important` |

### Always available
| Class | Effect |
|---|---|
| `class="imgfix"` | `line-height:0; font-size:0` on the cell — closes the gap under images. Also forces `margin:0 !important` on every image inside it, so any margin you put on the image, including `margin:0 auto`, is cancelled |

### Patterns that work

**Stack two columns on mobile** — `class="m-block m-full-width m-p-l-0 m-p-r-0"` on
each `<td>`. `m-full-width` alone is not enough: two 100% cells in one row is 200% wide. The
`m-p-l-0 m-p-r-0` clears the inline gutter that separated the columns; it does not touch outer padding
held on a wrapper cell, so the outer inset survives.

**Reorder on mobile** — add `m-top-column` to the cell that should come first.

**Different copy per device** — `<span class="m-hide">…</span>` and
`<span class="m-show" style="display:none">…</span>`.

**Mobile padding caps at 15px.** `m-p-{t,r,b,l}-N` accepts 0–15 only. Desktop gutters of
40px are fine; the mobile override cannot exceed 15.

**Every `<tr>` becomes `width:100%; display:table` on mobile** regardless of class. This is
what makes stacking work, and it also widens narrow centred spacer rows.

**Centre an image narrower than its container** — wrap it in a nested table with `align="center"`
as an attribute, and put `class="imgfix"` on the cell inside that table. Never centre an image with margin:
`class="imgfix"` cancels the margin in browser clients, while Outlook classic centres the image from the
cell's `text-align` anyway. The same markup then centres in Outlook and sits left everywhere else.

```html
<td align="center" style="text-align:center;padding:24px 0 8px;">
  <table role="presentation" align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
    <tr>
      <td align="center" class="imgfix" style="text-align:center;padding:0;line-height:0;font-size:0;">
        <img src="https://images.example.com/logo.png" alt="Company name" width="180" height="50" border="0" style="display:block;width:180px;">
      </td>
    </tr>
  </table>
</td>
```

**Two buttons side by side** — one centred table, one wrapper cell per button, and the gap made
from padding on the wrapper cells. Never with a spacer cell (section 6). Give each wrapper cell the
background colour of the block it sits in. Align the first button right and the second left: on
mobile the row widens to full width, and this keeps the two buttons together near the centre instead
of drifting apart.

```html
<table role="presentation" align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
  <tr>
    <td align="right" bgcolor="#1a2b5c" style="text-align:right;background-color:#1a2b5c;padding:0 6px 0 0;">
      <table role="presentation" align="right" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td align="center" bgcolor="#e85d04" style="text-align:center;background-color:#e85d04;padding:11px 22px;font:bold 13px/16px Verdana,Geneva,sans-serif;">
            <a href="https://example.com/first" style="text-decoration:none;color:#ffffff;">First action</a>
          </td>
        </tr>
      </table>
    </td>
    <td align="left" bgcolor="#1a2b5c" style="text-align:left;background-color:#1a2b5c;padding:0 0 0 6px;">
      <table role="presentation" align="left" border="0" cellpadding="0" cellspacing="0">
        <tr>
          <td align="center" bgcolor="#e85d04" style="text-align:center;background-color:#e85d04;padding:11px 22px;font:bold 13px/16px Verdana,Geneva,sans-serif;">
            <a href="https://example.com/second" style="text-decoration:none;color:#ffffff;">Second action</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

**No fixed `height` on a cell that holds text, unless the cell also has `class="row"`.** Cards
stack and widen on mobile, so their content gets shorter, and nothing else in the vocabulary
releases a fixed height. The result is an empty band under the content on every phone. `row` is the
one class that does: `height:auto !important` on mobile.

**Equal-height cards with buttons on a shared baseline** — each card is a nested table with two
rows: content, then button. The content cell carries `height="N"`, `class="row"` and `valign="top"`;
the button row has no height. On desktop both content cells are N tall, so the buttons line up. On
mobile `row` releases the height and each card shrinks to its content, with its button directly
underneath. Outlook classic ignores the mobile class and keeps the desktop layout.

The card backgrounds sit on the nested tables, not on the column cells. The column cells hold the
gutter as padding, so the gap between the cards stays the page colour.

Size N to the taller card's content at desktop width, then check the preview. A fixed height on a
cell is a minimum, so N too small makes that card grow and the buttons drift apart again. N too
large shows as an empty band above both buttons.

```html
<table role="presentation" class="m-full-width" width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td class="m-block m-full-width m-p-l-0 m-p-r-0 m-p-b-10" width="50%" valign="top" style="text-align:left;padding:0 6px 0 0;">
      <table role="presentation" class="m-full-width" width="100%" border="0" cellpadding="0" cellspacing="0" style="background-color:#f2f4f9;">
        <tr>
          <td class="row" height="260" valign="top" bgcolor="#f2f4f9" style="text-align:left;background-color:#f2f4f9;padding:16px 16px 0;font:14px/22px Verdana,Geneva,sans-serif;font-weight:400;color:#333333;">
            Card content
          </td>
        </tr>
        <tr>
          <td bgcolor="#f2f4f9" style="text-align:left;background-color:#f2f4f9;padding:16px;">
            <!-- button table, as in section 8 -->
          </td>
        </tr>
      </table>
    </td>
    <td class="m-block m-full-width m-p-l-0 m-p-r-0" width="50%" valign="top" style="text-align:left;padding:0 0 0 6px;">
      <!-- second card: same structure, same N -->
    </td>
  </tr>
</table>
```

---

## 4. Classes that look useful and are not

**Dead — scoped under a wrapper authored HTML never has.** Accepted, no effect, shipped as
dead weight. Everything under `.m-show-row`, plus `.menu .menu-spacing`, `.list .list-type`,
`.list .list-item`, `.list .m-list-item`, `.icon-menu-item.icon-text span`.

**`.column` does nothing.** It exists only as `.m-show-row.regular .column`. Copying
`class="column m-full-width"` out of an exported Apsis template is the most tempting error here: it
works in the export because of the wrapper and does nothing here. Use `m-block`.

**Live but with side effects.** These fire, rarely as the name suggests. Don't use them as
decoration.

| Class | What it does on mobile |
|---|---|
| `button-link` | forces the inner `a` to `display:block`, `border-radius:5px`, `padding:10px 20px` — overrides your button styling |
| `list` | forces the table and its inner table to `width:100%` |
| `.menu` | forces `table.menu td` and `table.menu th` to `width:100%` |
| `body-padding` | `padding:0` |
| `body-text` | `max-height:unset` |
| `row` | `height:auto` — one sanctioned use: on a cell with a fixed `height`, it makes that height desktop-only. See the equal-height cards pattern in section 3 |
| `image` | inner `img` gets `max-width:100%` |

---

## 5. Conditional comments and Outlook targeting

**Comments are removed from authored HTML — all of them.**

- `<!--[if mso]>` — branch deleted entirely.
- `<!--[if gte mso 9]>` — branch deleted entirely. Both forms treated identically; the sanitiser is
  not matching on condition text.
- `<!--[if !mso]><!-->` (downlevel-revealed) — the comment wrappers are removed and the content kept,
  so it becomes unconditional markup.
- A plain `<!-- comment -->` — removed cleanly, content and all, with no leak.

Two consequences. **VML is unavailable**, so the usual rounded-button fallback can't be built. And you
lose targeting *in both directions*: the MSO branch vanishes and the non-MSO branch becomes visible
everywhere, including in Outlook.

Note for anyone reading the delivered source: the platform's own `<head>` still carries live
`[if gte mso 9]` blocks (OfficeDocumentSettings, and the MSO font-substitution stylesheet). Those are
assembled after the sanitiser runs. Their presence is not evidence that you can author one.

---

## 6. Outlook

Outlook for Windows renders with Word, which behaves differently from every other client here.

- **`border-radius` does not render.** A rounded button arrives square. This is
acceptable — a square button with solid fill and real padding reads as a deliberate button. Design
for it rather than trying to defeat it; with VML gone there is no alternative anyway.
- **Padding must be on the `<td>`, not on the `<a>` or a `<div>`.** Anchor padding is
ignored and the button collapses to a bare text label. This is the single most damaging Outlook
mistake, and it looks fine in every other client.
- **`padding:` on a `<th>` works.** `<th>` is usable; inline padding is not overridden by
the platform's `table th{padding:0}`.
- **Outlook mobile insets the whole message.** The app adds its own margin around
the body, so no background can reach the screen edge there however the HTML is written. A design
that depends on edge-to-edge colour will look inset in Outlook mobile and flush elsewhere.
- **Empty spacer cells show.** A cell holding only `&nbsp;` or a space with inline `font-size:0;
line-height:0` renders in Outlook classic as a white bar at text height, even inside a coloured
block. Make every gap from padding on a cell that holds content. A cell with no content shouldn't
exist.
- **Images follow the cell's `text-align`, even with `display:block`.** In browser clients a
block image ignores `text-align`. The same image can centre in Outlook and sit left everywhere else.
Centre images with the nested-table pattern in section 3.

**Not established, so don't lean on them.** `background-image` on cells, `box-shadow`, CSS gradients,
`max-width`, transform, SVG images, `letter-spacing` and negative margins are all unreliable here.
Use tables for layout rather than flex or grid, set `line-height` in pixels, and put a solid
`background-color` behind any text that has to be legible.

**Lead with a font that is actually installed.** Word does not reliably fall through a font stack when
the first name is missing, so an uninstallable brand font in first position risks a serif on the client
you care most about. Web fonts are stripped anyway, so put the system font first:
`Verdana, Geneva, sans-serif` or `Arial, Helvetica, sans-serif`, and check the metrics still fit.

On top of that, the platform's own MSO stylesheet remaps some families outright, matching on the
`style` attribute: Lato, Merriweather Sans, Open Sans, Roboto, Source Sans Pro and DM Sans
become Verdana; Arvo, Lora, Merriweather, Noticia Text and Playfair Display become Times New
Roman.

---

## 7. Personalisation, links and images

- **Data tags** use `##<discriminator>##`. Call `list_email_data_tags` first — unknown discriminators
  are rejected at create time.
- **Links are rewritten** to tracked Apsis URLs when link tracking is on. `data-apsis-track="false"`
  on an anchor exempts it.
- **After `duplicate_email_activity`**, copies made before 2026-10-02 have dead links; duplicate the
  original again.
- **Images need a public `https` URL.** Never a local path, `file://` or `data:` URI — it renders
  broken for every recipient. Use the image upload tools for anything the user supplies.

---

## 8. Known-good skeleton

Satisfies every rule in sections 1 and 2, with button padding on the cell per section 6.

```html
<table role="presentation" class="m-full-width" width="100%" border="0" cellpadding="0" cellspacing="0" style="background-color:#ffffff;">

 <!-- Logo: narrower than the column, so no width class; centred with a nested table -->
 <tr>
 <td align="center" style="text-align:center;padding:24px 0 16px;">
 <table role="presentation" align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
 <tr>
 <td align="center" class="imgfix" style="text-align:center;padding:0;line-height:0;font-size:0;">
 <a href="https://example.com" style="display:block;text-decoration:none;color:#000000;"><img border="0" src="https://images.example.com/logo.png" alt="Company name" width="180" height="50" style="display:block;width:180px;"></a>
 </td>
 </tr>
 </table>
 </td>
 </tr>

 <!-- Banner: fills the column, so m-full-width plus height:auto -->
 <tr>
 <td align="center" class="imgfix" style="text-align:center;padding:0;line-height:0;font-size:0;">
 <img class="m-full-width" border="0" src="https://images.example.com/banner.jpg" alt="Describe the image" width="600" height="300" style="display:block;width:600px;height:auto;">
 </td>
 </tr>

 <!-- Heading -->
 <tr>
 <td align="center" class="m-p-l-15 m-p-r-15" style="text-align:center;padding:24px 45px 4px;font:bold 26px/32px Verdana,Geneva,sans-serif;color:#1a1a1a;">
Heading goes here
 </td>
 </tr>

 <!-- Body copy -->
 <tr>
 <td align="center" class="m-p-l-15 m-p-r-15" style="text-align:center;padding:16px 45px;font:14px/24px Verdana,Geneva,sans-serif;font-weight:400;color:#333333;">
Body copy with a <a href="https://example.com" style="text-decoration:none;color:#0066cc;"><u>link</u></a>.
 </td>
 </tr>

 <!-- Button: padding on the cell, square in Outlook by design -->
 <tr>
 <td align="center" style="text-align:center;padding:16px 45px 32px;">
 <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
 <tr>
 <td align="center" bgcolor="#0066cc" style="text-align:center;background-color:#0066cc;border-radius:4px;padding:13px 34px;font:bold 14px/18px Verdana,Geneva,sans-serif;">
 <a href="https://example.com" style="text-decoration:none;color:#ffffff;">Call to action</a>
 </td>
 </tr>
 </table>
 </td>
 </tr>

 <!-- Two columns that stack on mobile -->
 <tr>
 <td class="m-p-l-15 m-p-r-15" style="text-align:left;padding:0 45px 32px;">
 <table role="presentation" class="m-full-width" width="100%" border="0" cellpadding="0" cellspacing="0">
 <tr>
 <td class="m-block m-full-width m-p-l-0 m-p-r-0" width="50%" valign="top" style="text-align:left;padding-right:12px;font:14px/24px Verdana,Geneva,sans-serif;font-weight:400;color:#333333;">
Left column
 </td>
 <td class="m-block m-full-width m-p-l-0 m-p-r-0" width="50%" valign="top" style="text-align:left;padding-left:12px;font:14px/24px Verdana,Geneva,sans-serif;font-weight:400;color:#333333;">
Right column
 </td>
 </tr>
 </table>
 </td>
 </tr>

</table>
```

---

## 9. Confirm before you submit

Check each one is present. Everything here fails silently if it isn't.

- [ ] Fragment only — the outermost element is a `<table>`
- [ ] Top-level table at `width="100%"`
- [ ] Every `<td>` and `<th>` has an inline `text-align`
- [ ] Every `<a>` has an inline `color:`
- [ ] Every fixed-width table, and every image meant to fill its column, has `m-full-width`. Logos, icons and headshots don't
- [ ] Every image with `m-full-width` has `height:auto` inline, as well as `width` and `height` attributes
- [ ] Every image sits in its own cell, with `class="imgfix"` on the cell and `display:block` on the image
- [ ] No image is centred with `margin:` — narrower images are centred with a nested `<table align="center">`
- [ ] No empty spacer cells — every gap is padding on a cell that holds content
- [ ] No fixed `height` on a cell holding text unless that cell also has `class="row"`
- [ ] Every `m-p-*-N` value is 0–15
- [ ] Button padding is on the `<td>`, and the button still reads well square
- [ ] Widths are explicit pixel attributes as well as styles
- [ ] Every image URL is a public `https` address
- [ ] Data tags verified with `list_email_data_tags`
- [ ] Styling lives in inline `style` attributes and the section 3 classes, and nowhere else
- [ ] The reference design's alignments are matched, or the user has been told which can't be
- [ ] Anything built outside the section 3 patterns is flagged to the user for an Outlook classic test send

If you can't tell whether something survives, assume it doesn't and use an inline style.

---

## 10. Doing something else on purpose

These rules describe what renders reliably through Apsis's pipeline and the major clients. If the user
wants something that requires breaking one and understands the trade-off, say plainly which rule and
what will happen, then proceed. Never break one silently, and never on your own initiative.
