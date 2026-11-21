# Quy tắc UX — 119 quy tắc

Chuyển từ UI UX Pro Max (MIT, © 2024 Next Level Builder) — xem THIRD-PARTY-NOTICES.md. Mức: High = phải sửa trước khi giao.

## Navigation

- **Smooth Scroll** (High, Web) — Anchor links should scroll smoothly to target section. Nên: Use scroll-behavior: smooth on html element. Tránh: Jump directly without transition. Đúng: `html { scroll-behavior: smooth; }` Sai: `<a href='#section'> without CSS`
- **Sticky Navigation** (Medium, Web) — Fixed nav should not obscure content. Nên: Add padding-top to body equal to nav height. Tránh: Let nav overlap first section content. Đúng: `pt-20 (if nav is h-20)` Sai: `No padding compensation`
- **Active State** (Medium, All) — Current page/section should be visually indicated. Nên: Highlight active nav item with color/underline. Tránh: No visual feedback on current location. Đúng: `text-primary border-b-2` Sai: `All links same style`
- **Back Button** (High, Mobile) — Users expect back to work predictably. Nên: Preserve navigation history properly. Tránh: Break browser/app back button behavior. Đúng: `history.pushState()` Sai: `location.replace()`
- **Deep Linking** (Medium, All) — URLs should reflect current state for sharing. Nên: Update URL on state/view changes. Tránh: Static URLs for dynamic content. Đúng: `Use query params or hash` Sai: `Single URL for all states`
- **Breadcrumbs** (Low, Web) — Show user location in site hierarchy. Nên: Use for sites with 3+ levels of depth. Tránh: Use for flat single-level sites. Đúng: `Home > Category > Product` Sai: `Only on deep nested pages`

## Animation

- **Excessive Motion** (High, All) — Too many animations cause distraction and motion sickness. Nên: Animate 1-2 key elements per view maximum. Tránh: Animate everything that moves. Đúng: `Single hero animation` Sai: `animate-bounce on 5+ elements`
- **Duration Timing** (Medium, All) — Motion duration depends on distance complexity platform and user context. Nên: Use shared motion tokens and test that feedback stays responsive. Tránh: Present 150-300ms or any cutoff as a universal requirement. Đúng: `transition-colors duration-200` Sai: `One duration copied to every transition`
- **Reduced Motion** (High, All) — Respect user's motion preferences. Nên: Check prefers-reduced-motion media query. Tránh: Ignore accessibility motion settings. Đúng: `@media (prefers-reduced-motion: reduce)` Sai: `No motion query check`
- **Loading States** (High, All) — Show feedback during async operations. Nên: Use skeleton screens or spinners. Tránh: Leave UI frozen with no feedback. Đúng: `animate-pulse skeleton` Sai: `Blank screen while loading`
- **Hover vs Tap** (High, All) — Hover effects don't work on touch devices. Nên: Use click/tap for primary interactions. Tránh: Rely only on hover for important actions. Đúng: `onClick handler` Sai: `onMouseEnter only`
- **Continuous Animation** (Medium, All) — Infinite animations are distracting. Nên: Use for loading indicators only. Tránh: Use for decorative elements. Đúng: `animate-spin on loader` Sai: `animate-bounce on icons`
- **Transform Performance** (Medium, Web) — Some CSS properties trigger expensive repaints. Nên: Use transform and opacity for animations. Tránh: Animate width/height/top/left properties. Đúng: `transform: translateY()` Sai: `top: 10px animation`
- **Easing Functions** (Low, All) — Easing should match how an element changes speed and purpose. Nên: Use deceleration when arriving acceleration when leaving and linear for constant-rate progress. Tránh: Reject linear easing even for steady rotation or progress. Đúng: `ease-out for entry; linear for spinner` Sai: `ease-in-out for every motion`
- **Auto-Rotating Content Controls** (High, All) — Auto-rotating content needs user control. Nên: Provide previous next and play/pause; stop on focus or hover and when reduced motion is requested. Tránh: Auto-advance slides without a stop control. Đúng: `button aria-label="Pause carousel"` Sai: `timer-only carousel`
- **Cancellable State Transitions** (High, Web) — Rapid compact-control changes can interrupt an in-flight transition. Nên: Cancel or replace prior motion; set the final semantic state directly and handle cancellation cleanup. Tránh: Depend on animationend or transitionend for required state correctness. Đúng: `previous?.cancel(); setSelected(next)` Sai: `Enable the chip only inside transitionend`

## Layout

- **Z-Index Management** (High, Web) — Stacking context conflicts cause hidden elements. Nên: Define z-index scale system (10 20 30 50). Tránh: Use arbitrary large z-index values. Đúng: `z-10 z-20 z-50` Sai: `z-[9999]`
- **Overflow Hidden** (Medium, Web) — Hidden overflow can clip important content. Nên: Test all content fits within containers. Tránh: Blindly apply overflow-hidden. Đúng: `overflow-auto with scroll` Sai: `overflow-hidden truncating content`
- **Fixed Positioning** (Medium, Web) — Fixed elements can overlap or be inaccessible. Nên: Account for safe areas and other fixed elements. Tránh: Stack multiple fixed elements carelessly. Đúng: `Fixed nav + fixed bottom with gap` Sai: `Multiple overlapping fixed elements`
- **Stacking Context** (Medium, Web) — New stacking contexts reset z-index. Nên: Understand what creates new stacking context. Tránh: Expect z-index to work across contexts. Đúng: `Parent with z-index isolates children` Sai: `z-index: 9999 not working`
- **Content Jumping** (High, Web) — Images badges validation text and skeleton replacements can shift nearby content when they update. Nên: Reserve appropriate space or keep async states in a stable content-driven container. Tránh: Insert compact text or media without a layout strategy. Đúng: `aspect-ratio for media; stable count slot for badges` Sai: `Badge insertion pushes toolbar actions`
- **Viewport Units** (Medium, Web) — 100vh can be problematic on mobile browsers. Nên: Use dvh or account for mobile browser chrome. Tránh: Use 100vh for full-screen mobile layouts. Đúng: `min-h-dvh or min-h-screen` Sai: `h-screen on mobile`
- **Container Width** (Medium, Web) — Content too wide is hard to read. Nên: Limit max-width for text content (65-75ch). Tránh: Let text span full viewport width. Đúng: `max-w-prose or max-w-3xl` Sai: `Full width paragraphs`
- **Long Token Wrapping** (High, Web) — URLs identifiers and user content must not force horizontal overflow. Nên: Use overflow-wrap anywhere and let flex or grid text children shrink. Tránh: Apply word-break break-all to all prose. Đúng: `.token { min-inline-size: 0; overflow-wrap: anywhere; }` Sai: `.token { white-space: nowrap; }`
- **Chip Collection Reflow** (High, All) — Filter chips and editable value collections must preserve labels when space or text size changes. Nên: Wrap the collection or use an operable +n disclosure for hidden overflow values. Tránh: Force all chips into one clipped row or hide overflow values. Đúng: `<div class='chip-list'>{chips}</div> with flex-wrap` Sai: `<div class='chip-list' style='height:32px;overflow:hidden'>`

## Touch

- **Touch Target Size** (High, Mobile) — Touch target guidance depends on platform and web context. Nên: Use 44pt on iOS and 48dp on Android; for web use the separate WCAG Target Size rule. Tránh: Treat one unit or minimum as universal across platforms. Đúng: `iOS 44pt; Android 48dp; Web 24 CSS px plus WCAG exceptions` Sai: `w-6 h-6 buttons`
- **Touch Spacing** (Medium, Mobile) — Adjacent touch targets need adequate spacing. Nên: Minimum 8px gap between touch targets. Tránh: Tightly packed clickable elements. Đúng: `gap-2 between buttons` Sai: `gap-0 or gap-1`
- **Gesture Conflicts** (Medium, Mobile) — Custom gestures can conflict with system. Nên: Avoid horizontal swipe on main content. Tránh: Override system gestures. Đúng: `Vertical scroll primary` Sai: `Horizontal swipe carousel only`
- **Tap Delay** (Medium, Mobile) — 300ms tap delay feels laggy. Nên: Use touch-action CSS or fastclick. Tránh: Default mobile tap handling. Đúng: `touch-action: manipulation` Sai: `No touch optimization`
- **Pull to Refresh** (Low, Mobile) — Accidental refresh is frustrating. Nên: Disable where not needed. Tránh: Enable by default everywhere. Đúng: `overscroll-behavior: contain` Sai: `Default overscroll`
- **Haptic Feedback** (Low, Mobile) — Tactile feedback improves interaction feel. Nên: Use for confirmations and important actions. Tránh: Overuse vibration feedback. Đúng: `navigator.vibrate(10)` Sai: `Vibrate on every tap`

## Interaction

- **Focus States** (High, All) — Keyboard focus, including controls inside a modal, needs a visible indicator. Nên: Use a visible focus ring on every interactive control, including modal controls. Tránh: Remove focus outline without replacement. Đúng: `focus:ring-2 focus:ring-blue-500` Sai: `outline-none without alternative`
- **Hover States** (Medium, Web) — Visual feedback on interactive elements. Nên: Change cursor and add subtle visual change. Tránh: No hover feedback on clickable elements. Đúng: `hover:bg-gray-100 cursor-pointer` Sai: `No hover style`
- **Active States** (Medium, All) — Show immediate feedback on press/click. Nên: Add pressed/active state visual change. Tránh: No feedback during interaction. Đúng: `active:scale-95` Sai: `No active state`
- **Disabled States** (Medium, All) — Clearly indicate non-interactive elements. Nên: Reduce opacity and change cursor. Tránh: Confuse disabled with normal state. Đúng: `opacity-50 cursor-not-allowed` Sai: `Same style as enabled`
- **Loading Buttons** (High, All) — Prevent double submission during async actions. Nên: Disable button and show loading state. Tránh: Allow multiple clicks during processing. Đúng: `disabled={loading} spinner` Sai: `Button clickable while loading`
- **Error Feedback** (High, All) — Users need to know when something fails. Nên: Show clear error messages near problem. Tránh: Silent failures with no feedback. Đúng: `Red border + error message` Sai: `No indication of error`
- **Success Feedback** (Medium, All) — Confirm successful actions to users. Nên: Show success message or visual change. Tránh: No confirmation of completed action. Đúng: `Toast notification or checkmark` Sai: `Action completes silently`
- **Confirmation Dialogs** (High, All) — Prevent accidental destructive actions. Nên: Confirm before delete/irreversible actions. Tránh: Delete without confirmation. Đúng: `Are you sure modal` Sai: `Direct delete on click`

## Accessibility

- **Color Contrast** (High, All) — Text must be readable against background. Nên: Minimum 4.5:1 ratio for normal text. Tránh: Low contrast text. Đúng: `#333 on white (7:1)` Sai: `#999 on white (2.8:1)`
- **Color Only** (High, All) — Don't convey information by color alone. Nên: Use icons/text in addition to color. Tránh: Red/green only for error/success. Đúng: `Red text + error icon` Sai: `Red border only for error`
- **Alt Text** (High, All) — Images need text alternatives. Nên: Descriptive alt text for meaningful images. Tránh: Empty or missing alt attributes. Đúng: `alt='Dog playing in park'` Sai: `alt='' for content images`
- **Heading Hierarchy** (Medium, Web) — Screen readers use headings for navigation. Nên: Use sequential heading levels h1-h6. Tránh: Skip heading levels or misuse for styling. Đúng: `h1 then h2 then h3` Sai: `h1 then h4`
- **ARIA Labels** (High, All) — Interactive elements need accessible names. Nên: Add aria-label for icon-only buttons. Tránh: Icon buttons without labels. Đúng: `aria-label='Close menu'` Sai: `<button><Icon/></button>`
- **Keyboard Navigation** (High, Web) — Web users need complete keyboard navigation with visible focus on every operable control. Nên: Keep tab order aligned with visual order and test every action without a pointer. Tránh: Keyboard traps or illogical tab order. Đúng: `tabIndex for custom order` Sai: `Unreachable elements`
- **Screen Reader** (Medium, All) — Content should make sense when read aloud. Nên: Use semantic HTML and ARIA properly. Tránh: Div soup with no semantics. Đúng: `<nav> <main> <article>` Sai: `<div> for everything`
- **Form Labels** (High, All) — Inputs must have associated labels. Nên: Use label with for attribute or wrap input. Tránh: Placeholder-only inputs. Đúng: `<label for='email'>` Sai: `placeholder='Email' only`
- **Error Messages** (High, All) — Error messages must be announced. Nên: Use aria-live or role=alert for errors. Tránh: Visual-only error indication. Đúng: `role='alert'` Sai: `Red border only`
- **Skip Links** (Medium, Web) — Allow keyboard users to skip navigation. Nên: Provide skip to main content link. Tránh: No skip link on nav-heavy pages. Đúng: `Skip to main content link` Sai: `100 tabs to reach content`
- **Motion Sensitivity** (High, All) — Parallax/Scroll-jacking causes nausea. Nên: Honor prefers-reduced-motion and present the final readable state without parallax or scroll-jacking. Tránh: Force scroll effects. Đúng: `@media (prefers-reduced-motion)` Sai: `ScrollTrigger.create()`
- **Focus Not Obscured (Minimum)** (High, Web) — WCAG 2.2 AA requires keyboard focus to remain at least partially visible. Nên: Offset sticky UI with scroll-padding and dismiss or move persistent overlays. Tránh: Let headers footers banners or chat widgets fully cover focus. Đúng: `scroll-padding-top: var(--header-height)` Sai: `fixed overlay covers :focus`
- **Focus Not Obscured (Enhanced)** (Medium, Web) — WCAG 2.2 AAA requires keyboard focus to remain fully visible. Nên: Keep the entire focused component unobscured by author-created content. Tránh: Present this enhanced AAA criterion as an AA requirement or allow persistent UI to hide any part of focus. Đúng: `close persistent overlay before focus moves behind it` Sai: `sticky footer covers half the focused button`
- **Focus Appearance** (Medium, Web) — WCAG 2.2 AAA defines minimum area and contrast for focus indicators. Nên: Use an indicator at least as large as a 2 CSS px perimeter with 3:1 state contrast. Tránh: Present this enhanced AAA criterion as an AA requirement or use a thin low-contrast outline. Đúng: `outline: 2px solid currentColor; outline-offset: 2px` Sai: `box-shadow: 0 0 1px low-contrast`
- **Dragging Movements** (High, All) — WCAG 2.2 AA requires a single-pointer alternative for author-controlled drag operations. Nên: Add buttons menus or tap-to-move controls and retain keyboard operation. Tránh: Make dragging the only way to reorder resize or select. Đúng: `Move up and Move down buttons beside drag handle` Sai: `drag handle only`
- **Target Size (Minimum)** (High, Web) — WCAG 2.2 AA requires 24 CSS px pointer targets or an applicable exception. Nên: Use at least 24 by 24 CSS px or verify spacing equivalent inline user-agent or essential exceptions. Tránh: Assume native 44pt or 48dp guidance defines web conformance. Đúng: `min-width: 24px; min-height: 24px` Sai: `tiny adjacent icon buttons`
- **Consistent Help** (Medium, All) — WCAG 2.2 A requires repeated help mechanisms to stay in the same relative order. Nên: Keep contact self-help and automated help in consistent locations. Tránh: Move help controls to different locations on each page. Đúng: `shared header help menu` Sai: `page-specific help placement`
- **Text Reflow and Spacing** (Critical, Web) — Text must remain available at narrow widths zoom and user spacing overrides. Nên: Use fluid sizes content-driven height and unitless line height. Tránh: Clip text in fixed-width or fixed-height boxes. Đúng: `.copy { inline-size: min(100%, 65ch); height: auto; line-height: 1.5; }` Sai: `.copy { width: 900px; height: 40px; overflow: hidden; }`
- **Compact Control Semantics** (Critical, Web) — Interactive chips need a native role accessible name state keyboard operation and visible focus. Nên: Prefer a button and expose pressed or selected state that matches the visible label. Tránh: Use a clickable div or reveal the only action on hover. Đúng: `<button aria-pressed='true'>Open now</button>` Sai: `<div class='selected' onclick='toggle()'>Open now</div>`
- **Contextual Live Badge Updates** (High, Web) — Async badge and count changes should announce a meaningful contextual status without moving focus. Nên: Use one appropriate atomic status message such as 3 items in cart. Tránh: Announce a bare number or make every badge a competing live region. Đúng: `<span role='status' aria-atomic='true'>3 items in cart</span>` Sai: `<span aria-live='polite'>3</span>`

## Performance

- **Image Optimization** (High, All) — Large images slow page load. Nên: Use appropriate size and format (WebP). Tránh: Unoptimized full-size images. Đúng: `srcset with multiple sizes` Sai: `4000px image for 400px display`
- **Lazy Loading** (Medium, All) — Load content as needed. Nên: Lazy load below-fold images and content. Tránh: Load everything upfront. Đúng: `loading='lazy'` Sai: `All images eager load`
- **Code Splitting** (Medium, Web) — Large bundles slow initial load. Nên: Split code by route/feature. Tránh: Single large bundle. Đúng: `dynamic import()` Sai: `All code in main bundle`
- **Caching** (Medium, Web) — Repeat visits should be fast. Nên: Set appropriate cache headers. Tránh: No caching strategy. Đúng: `Cache-Control headers` Sai: `Every request hits server`
- **Font Loading** (Medium, Web) — Web fonts can block rendering. Nên: Use font-display swap or optional. Tránh: Invisible text during font load. Đúng: `font-display: swap` Sai: `FOIT (Flash of Invisible Text)`
- **Third Party Scripts** (Medium, Web) — External scripts can block rendering. Nên: Load non-critical scripts async/defer. Tránh: Synchronous third-party scripts. Đúng: `async or defer attribute` Sai: `<script src='...'> in head`
- **Bundle Size** (Medium, Web) — Large JavaScript slows interaction. Nên: Monitor and minimize bundle size. Tránh: Ignore bundle size growth. Đúng: `Bundle analyzer` Sai: `No size monitoring`
- **Render Blocking** (Medium, Web) — CSS/JS can block first paint. Nên: Inline critical CSS defer non-critical. Tránh: Large blocking CSS files. Đúng: `Critical CSS inline` Sai: `All CSS in head`

## Forms

- **Input Labels** (High, All) — Every input needs a visible label. Nên: Always show label above or beside input. Tránh: Placeholder as only label. Đúng: `<label>Email</label><input>` Sai: `placeholder='Email' only`
- **Error Placement** (High, All) — Each invalid field needs an inline error connected to that field. Nên: Show a specific error below the input and reference it with aria-describedby. Tránh: Show only a top-level error without identifying each invalid field. Đúng: `<input aria-describedby="email-error"><p id="email-error">Enter an email address</p>` Sai: `Red border or summary only`
- **Inline Validation** (Medium, All) — Validate as user types or on blur. Nên: Validate on blur for most fields. Tránh: Validate only on submit. Đúng: `onBlur validation` Sai: `Submit-only validation`
- **Input Types** (Medium, All) — Use appropriate input types. Nên: Use email tel number url etc. Tránh: Text input for everything. Đúng: `type='email'` Sai: `type='text' for email`
- **Autofill Support** (Medium, Web) — Help browsers autofill correctly. Nên: Use autocomplete attribute properly. Tránh: Block or ignore autofill. Đúng: `autocomplete='email'` Sai: `autocomplete='off' everywhere`
- **Required Indicators** (Medium, All) — Mark required fields clearly. Nên: Use asterisk or (required) text. Tránh: No indication of required fields. Đúng: `* required indicator` Sai: `Guess which are required`
- **Password Visibility** (Medium, All) — Let users see password while typing. Nên: Toggle to show/hide password. Tránh: No visibility toggle. Đúng: `Show/hide password button` Sai: `Password always hidden`
- **Submit Feedback** (High, All) — Confirm form submission status. Nên: Show loading then success/error state. Tránh: No feedback after submit. Đúng: `Loading -> Success message` Sai: `Button click with no response`
- **Input Affordance** (Medium, All) — Inputs should look interactive. Nên: Use distinct input styling. Tránh: Inputs that look like plain text. Đúng: `Border/background on inputs` Sai: `Borderless inputs`
- **Mobile Keyboards** (Medium, Mobile) — Show appropriate keyboard for input type. Nên: Use inputmode attribute. Tránh: Default keyboard for all inputs. Đúng: `inputmode='numeric'` Sai: `Text keyboard for numbers`
- **Redundant Entry** (Medium, All) — WCAG 2.2 A avoids requiring the same information twice in one process. Nên: Auto-populate prior values or let users select previously entered information. Tránh: Ask users to retype the same address or account data without necessity. Đúng: `reuse confirmed shipping address` Sai: `repeat full address form`

## Responsive

- **Mobile First** (Medium, Web) — Design for mobile then enhance for larger. Nên: Start with mobile styles then add breakpoints. Tránh: Desktop-first causing mobile issues. Đúng: `Default mobile + md: lg: xl:` Sai: `Desktop default + max-width queries`
- **Breakpoint Testing** (Medium, Web) — Test at all common screen sizes. Nên: Test at 320 375 414 768 1024 1440. Tránh: Only test on your device. Đúng: `Multiple device testing` Sai: `Single device development`
- **Touch Friendly** (High, Web) — Mobile layouts need touch-sized targets. Nên: Increase touch targets on mobile. Tránh: Same tiny buttons on mobile. Đúng: `Larger buttons on mobile` Sai: `Desktop-sized targets on mobile`
- **Readable Font Size** (High, All) — Text must be readable on all devices. Nên: Minimum 16px body text on mobile. Tránh: Tiny text on mobile. Đúng: `text-base or larger` Sai: `text-xs for body text`
- **Viewport Meta** (High, Web) — Set viewport for mobile devices. Nên: Use width=device-width initial-scale=1. Tránh: Missing or incorrect viewport. Đúng: `<meta name='viewport'...>` Sai: `No viewport meta tag`
- **Horizontal Scroll** (High, Web) — Avoid horizontal scrolling. Nên: Ensure content fits viewport width. Tránh: Content wider than viewport. Đúng: `max-w-full overflow-x-hidden` Sai: `Horizontal scrollbar on mobile`
- **Image Scaling** (Medium, Web) — Images should scale with container. Nên: Use max-width: 100% on images. Tránh: Fixed width images overflow. Đúng: `max-w-full h-auto` Sai: `width='800' fixed`
- **Table Handling** (Medium, Web) — Tables can overflow on mobile. Nên: Use horizontal scroll or card layout. Tránh: Wide tables breaking layout. Đúng: `overflow-x-auto wrapper` Sai: `Table overflows viewport`

## Typography

- **Line Height** (Medium, All) — Adequate line height improves readability. Nên: Use 1.5-1.75 for body text. Tránh: Cramped or excessive line height. Đúng: `leading-relaxed (1.625)` Sai: `leading-none (1)`
- **Line Length** (Medium, Web) — Long lines are hard to read. Nên: Limit to 65-75 characters per line. Tránh: Full-width text on large screens. Đúng: `max-w-prose` Sai: `Full viewport width text`
- **Font Size Scale** (Medium, All) — Consistent type hierarchy aids scanning. Nên: Use consistent modular scale. Tránh: Random font sizes. Đúng: `Type scale (12 14 16 18 24 32)` Sai: `Arbitrary sizes`
- **Font Loading** (Medium, Web) — Fonts should load without layout shift. Nên: Reserve space with fallback font. Tránh: Layout shift when fonts load. Đúng: `font-display: swap + similar fallback` Sai: `No fallback font`
- **Contrast Readability** (High, All) — Body text needs good contrast. Nên: Use darker text on light backgrounds. Tránh: Gray text on gray background. Đúng: `text-gray-900 on white` Sai: `text-gray-400 on gray-100`
- **Heading Clarity** (Medium, All) — Headings should stand out from body. Nên: Clear size/weight difference. Tránh: Headings similar to body text. Đúng: `Bold + larger size` Sai: `Same size as body`
- **Heading Line Balance** (Medium, Web) — Short multi-line headings may use balanced wrapping as a progressive visual heuristic. Nên: Bound the measure and test natural-wrap fallback across widths fonts and locales. Tránh: Promise an exact final line or insert blanket nonbreaking spaces or hardcoded br tags. Đúng: `.hero-title { max-inline-size: 20ch; text-wrap: balance; }` Sai: `Heading copy rewritten with forced last-line breaks`

## Feedback

- **Loading Indicators** (High, All) — Loading feedback should match the expected wait and avoid flashing for near-instant work. Nên: Follow platform and component guidance; preserve layout focus and accessible busy status. Tránh: Apply one timing threshold to every operation or leave long waits unexplained. Đúng: `Stable skeleton or progress with aria-busy` Sai: `Flickering spinner or frozen UI`
- **Empty States** (Medium, All) — Guide users when no content exists. Nên: Show helpful message and action. Tránh: Blank empty screens. Đúng: `No items yet. Create one!` Sai: `Empty white space`
- **Error Recovery** (Medium, All) — Help users recover from errors. Nên: Provide clear next steps. Tránh: Error without recovery path. Đúng: `Try again button + help link` Sai: `Error message only`
- **Progress Indicators** (Medium, All) — Show progress for multi-step processes. Nên: Step indicators or progress bar. Tránh: No indication of progress. Đúng: `Step 2 of 4 indicator` Sai: `No step information`
- **Toast Notifications** (Medium, All) — Transient messages for non-critical info. Nên: Auto-dismiss after 3-5 seconds. Tránh: Toasts that never disappear. Đúng: `Auto-dismiss toast` Sai: `Persistent toast`
- **Confirmation Messages** (Medium, All) — Confirm successful actions. Nên: Brief success message. Tránh: Silent success. Đúng: `Saved successfully toast` Sai: `No confirmation`

## Content

- **Truncation** (Medium, All) — Handle long content gracefully. Nên: Truncate with ellipsis and expand option. Tránh: Overflow or broken layout. Đúng: `line-clamp-2 with expand` Sai: `Overflow or cut off`
- **Date Formatting** (Low, All) — Use locale-appropriate date formats. Nên: Use relative or locale-aware dates. Tránh: Ambiguous date formats. Đúng: `2 hours ago or locale format` Sai: `01/02/03`
- **Number Formatting** (Low, All) — Format large numbers for readability. Nên: Use thousand separators or abbreviations. Tránh: Long unformatted numbers. Đúng: `1.2K or 1,234` Sai: `1234567`
- **Placeholder Content** (Low, All) — Show realistic placeholders during dev. Nên: Use realistic sample data. Tránh: Lorem ipsum everywhere. Đúng: `Real sample content` Sai: `Lorem ipsum`
- **Essential Text Truncation** (Critical, All) — Headings actions errors safety text and distinguishing names need complete access. Nên: Wrap stack resize or provide a visible full-detail path. Tránh: Clamp essential meaning only to make cards uniform. Đúng: `Action label wraps or opens full details` Sai: `Primary action shown only as an unexplained ellipsis`
- **Compact Label Semantics** (High, All) — Badges communicate state while chips or tags represent values or actions. Nên: Choose static or interactive markup from the label's meaning and ownership. Tránh: Make every pill clickable or encode status with color alone. Đúng: `<span class='status'>Pending</span>` Sai: `<div class='pill' onclick='toggle()'>Pending</div>`
- **Compact Label Overflow** (High, All) — A badge chip or pill label should stay whole on one line when practical and disclose unavoidable truncation. Nên: Bound only unpredictable values; use nowrap with a shrinkable label; expose full text to keyboard pointer and touch users. Tránh: Let one compact label wrap to a second line or use a hover-only tooltip. Đúng: `Flexible label with min-width 0 and an operable full-value disclosure` Sai: `Fixed-width badge wraps to second line or clips with title-only recovery`

## Onboarding

- **User Freedom** (Medium, All) — Users should be able to skip tutorials. Nên: Provide Skip and Back buttons. Tránh: Force linear unskippable tour. Đúng: `Skip Tutorial button` Sai: `Locked overlay until finished`

## Search

- **Autocomplete** (Medium, Web) — Help users find results faster. Nên: Show predictions as user types. Tránh: Require full type and enter. Đúng: `Debounced fetch + dropdown` Sai: `No suggestions`
- **No Results** (Medium, Web) — Dead ends frustrate users. Nên: Show 'No results' with suggestions. Tránh: Blank screen or '0 results'. Đúng: `Try searching for X instead` Sai: `No results found.`

## Data Entry

- **Bulk Actions** (Low, Web) — Editing one by one is tedious. Nên: Allow multi-select and bulk edit. Tránh: Single row actions only. Đúng: `Checkbox column + Action bar` Sai: `Repeated actions per row`

## AI Interaction

- **Disclaimer** (High, All) — Users need to know they talk to AI. Nên: Clearly label AI generated content. Tránh: Present AI as human. Đúng: `AI Assistant label` Sai: `Fake human name without label`
- **Streaming** (Medium, All) — Waiting for full text is slow. Nên: Stream text response token by token. Tránh: Show loading spinner for 10s+. Đúng: `Typewriter effect` Sai: `Spinner until 100% complete`
- **Feedback Loop** (Low, All) — AI needs user feedback to improve. Nên: Thumps up/down or 'Regenerate'. Tránh: Static output only. Đúng: `Feedback component` Sai: `Read-only text`

## Spatial UI

- **Gaze Hover** (High, VisionOS) — Elements should respond to eye tracking before pinch. Nên: Scale/highlight element on look. Tránh: Static element until pinch. Đúng: `hoverEffect()` Sai: `onTap only`
- **Depth Layering** (Medium, VisionOS) — UI needs Z-depth to separate content from environment. Nên: Use glass material and z-offset. Tránh: Flat opaque panels blocking view. Đúng: `.glassBackgroundEffect()` Sai: `bg-white`

## Sustainability

- **Auto-Play Video** (Medium, Web) — Autoplaying media consumes data and creates motion barriers. Nên: Prefer click-to-play; provide pause and captions; stop off-screen and honor reduced motion. Tránh: Auto-play high-resolution loops without pause or captions. Đúng: `<video controls preload="none"><track kind="captions" /></video>` Sai: `autoplay loop`
- **Asset Weight** (Medium, Web) — Heavy 3D/Image assets increase carbon footprint. Nên: Compress and lazy load 3D models. Tránh: Load 50MB textures. Đúng: `Draco compression` Sai: `Raw .obj files`

## Security / Accessibility

- **Accessible Authentication (Minimum)** (Critical, All) — WCAG 2.2 AA says authentication must not depend only on a cognitive function test unless an exception applies. Nên: Allow password managers and paste; offer passkeys OAuth or another non-cognitive method. Tránh: Block paste or require manual OTP transcription with no alternative. Đúng: `autocomplete="current-password" and paste allowed` Sai: `onpaste preventDefault`

## Forms / Accessibility

- **Focusable Error Summary** (High, Web) — An error summary for failed validation complements inline field errors and must be easy to find by keyboard and screen reader users. Nên: Place it at the top of the form; move focus to its heading or container after failed submit; link each item to its invalid field; retain inline errors. Tránh: Replace inline errors with a visual-only summary or move focus on every blur. Đúng: `<div role="alert" tabindex="-1" aria-labelledby="error-title"><h2 id="error-title">There is a problem</h2><a href="#email">Enter an email address</a></div>` Sai: `Toast only with no field links or focus target`
