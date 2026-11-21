# Cyberpunk (`cyberpunk`)

Đen tuyền, neon lơ và hồng, lưới phát sáng

- Hợp với: Hợp khi đang dùng AI để dựng website cho game, cộng đồng công nghệ và sự kiện đêm cần không khí mạnh cùng tác vụ rõ.
- Ngành minh hoạ: Phòng máy, quán game, công nghệ
- Trang minh hoạ làm việc gì: Game jam với đề bài ánh sáng, đội mẫu và bộ lọc vai trò
- Thang (1–10): biến tấu bố cục 8 · chuyển động 4 · mật độ 5
- Xem mẫu: https://tocbien.cloud/phong-cach/cyberpunk/

## Đặc tả

Cyberpunk: nền đen tím #07060f, mực sáng, neon lơ #22d3ee và hồng #f43f8e làm điểm nhấn. Lưới và vân màn hình rất mờ ở nền, tiêu đề sans-serif hẹp đậm, quầng sáng chỉ ở điểm nhấn. Dùng ảnh phòng máy hoặc sản phẩm thật phù hợp ở hero hay phần không gian; không thay ảnh bằng các thanh gradient vô nghĩa. Dịch vụ, cấu hình hoặc bảng giá có hàng rõ và số dễ đọc. Không nhấp nháy hoặc hiệu ứng lỗi liên tục. Điện thoại giảm glow, bỏ lớp không cần, nội dung xếp dọc.

**Chi tiết cần giữ:** Quầng sáng chỉ đắp cho tên thương hiệu và một cụm nhấn, đừng đắp cho chữ thân bài. Chữ phụ màu xám xanh phải đo lại tương phản trên nền đen, rất dễ tụt dưới ngưỡng đọc.

**Lưu ý khi áp dụng:** Neon trên nền đen đọc lâu rất mỏi mắt. Dùng cho trang ngắn, đừng dùng cho trang phải đọc nhiều.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Cyberpunk / Glitch Design System

## 1. Design Philosophy

**Core Principles**: "High-Tech, Low-Life." The aesthetic is a digital dystopia colliding with a high-tech noir reality. It captures the tension between advanced technology and societal decay—a world of underground hackers, neon-drenched megacities, and corrupted data streams. This isn't a clean, utopian future; it's gritty, imperfect, and palpably dangerous. Every pixel should feel like it's being rendered on a malfunctioning CRT monitor in a rain-soaked Tokyo alley or a rogue terminal in a subterranean bunker.

**The Vibe**: Dangerous, electric, rebellious, and aggressively futuristic-retro. It draws heavily from the visual language of 80s sci-fi (Blade Runner, Akira) and hacker culture (The Matrix, Ghost in the Shell). The interface should feel *alive* and volatile—buzzing with digital energy, glitching with data corruption, and pulsing with raw power. It’s not just a website; it’s a hacked feed, a forbidden interface, a window into the sprawl.

**The Tactile Experience**:
- **Imperfect Technology**: Embrace the artifacts of analog-to-digital conversion. Scanlines, chromatic aberration (RGB splitting), and signal noise are not bugs; they are features. The UI should feel like it's struggling to contain the data it displays.
- **The Void vs. The Light**: The background isn't just dark; it's a void. Against this absolute blackness, neon light (cyan, magenta, acid green) doesn't just color elements—it *illuminates* them. Light sources should feel physical, casting glows and shadows that define the hierarchy.
- **Industrial Brutalism**: Shapes are hard, angular, and utilitarian. Chamfered corners (45-degree cuts) replace friendly rounded rectangles. Borders are technical and precise, resembling blueprints or HUD (Heads-Up Display) schematics rather than decorative frames.

**Visual Signatures That Make This Unforgettable**:
- **Chromatic Aberration**: RGB color splitting on text and elements (red/cyan offset shadows) to simulate lens distortion or signal interference.
- **Scanlines**: Subtle horizontal line overlays mimicking the refresh rate of old CRT monitors, adding texture and unifying the composition.
- **Glitch Effects**: Intentional "corruption" via clip-path animations, skewed transforms, and flickering text that suggests a unstable connection or a hacked system.
- **Neon Glow**: Text and borders that literally glow with intense, multi-layered box-shadow/text-shadow stacking, creating a "light saber" or "neon sign" effect against the dark background.
- **Corner Cuts**: Chamfered/clipped corners on cards and buttons creating a militaristic, tech-panel aesthetic.
- **Circuit Patterns**: Decorative SVG backgrounds resembling PCB traces or data highways, suggesting the underlying hardware.

---

## 2. Design Token System (The DNA)

### Colors (Dark Mode - Mandatory)

```
background:          #0a0a0f      // Deep void black with slight blue undertone
foreground:          #e0e0e0      // Primary text, not pure white (less harsh)
card:                #12121a      // Card background, deep purple-black
muted:               #1c1c2e      // UI chrome/elevated backgrounds
mutedForeground:     #6b7280      // Secondary text, reduced contrast
accent:              #00ff88      // PRIMARY NEON - Electric green (Matrix-inspired)
accentSecondary:     #ff00ff      // SECONDARY NEON - Hot magenta/pink
accentTertiary:      #00d4ff      // TERTIARY NEON - Cyan/electric blue
border:              #2a2a3a      // Subtle borders
input:               #12121a      // Deep input background
ring:                #00ff88      // Focus ring matches accent
destructive:         #ff3366      // Error/danger red-pink
```

### Typography

**Font Stack**:
- **Headings**: `"Orbitron", "Share Tech Mono", monospace` — Geometric, futuristic, robotic
- **Body**: `"JetBrains Mono", "Fira Code", "Consolas", monospace` — Clean monospace for that terminal feel
- **Accent/Labels**: `"Share Tech Mono", monospace` — For UI labels, timestamps, badges

**Scale & Styling**:
- H1: `text-6xl` to `text-8xl`, `font-black`, `uppercase`, `tracking-widest`
- H2: `text-4xl` to `text-5xl`, `font-bold`, `uppercase`, `tracking-wide`
- H3: `text-xl` to `text-2xl`, `font-semibold`, `uppercase`
- Body: `text-base`, `font-normal`, `tracking-wide`, `leading-relaxed`
- Code/Labels: `text-sm`, `font-mono`, `uppercase`, `tracking-[0.2em]`

### Radius & Border

```
radius.none:     0px        // Sharp cuts are the default
radius.sm:       2px        // Minimal softening
radius.base:     4px        // Rare, only for inputs
radius.chamfer:  Use clip-path for corner cuts instead of border-radius
```

**Border Width**: `1px` default, `2px` for emphasis, borders often use gradient or glow effects

**Chamfered Corner Pattern** (apply via clip-path):
```css
clip-path: polygon(
  0 10px, 10px 0,           /* top-left cut */
  calc(100% - 10px) 0, 100% 10px,  /* top-right cut */
  100% calc(100% - 10px), calc(100% - 10px) 100%,  /* bottom-right cut */
  10px 100%, 0 calc(100% - 10px)   /* bottom-left cut */
);
```

### Shadows & Effects

**Neon Glow (CSS Variable Tokens)**:
```css
/* Main neon glow - used on hover states, focus rings, highlighted elements */
--box-shadow-neon: 0 0 5px #00ff88, 0 0 10px #00ff8840;

/* Small neon glow - subtle accents */
--box-shadow-neon-sm: 0 0 3px #00ff88, 0 0 6px #00ff8830;

/* Large neon glow - emphasized states, hero elements */
--box-shadow-neon-lg: 0 0 10px #00ff88, 0 0 20px #00ff8860, 0 0 40px #00ff8830;

/* Secondary neon (magenta) */
--box-shadow-neon-secondary: 0 0 5px #ff00ff, 0 0 20px #ff00ff60;

/* Tertiary neon (cyan) */
--box-shadow-neon-tertiary: 0 0 5px #00d4ff, 0 0 20px #00d4ff60;
```

**Text Shadows for Depth**:
```css
/* Glitch effect text shadow (used on hero headline) */
drop-shadow: 0 0 10px rgba(0, 255, 136, 0.5);

/* Gradient text glow */
drop-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
```

**Chromatic Aberration (via CSS animation on .cyber-glitch)**:
Implemented via ::before and ::after pseudo-elements with:
- text-shadow: -1px 0 #ff00ff (magenta left)
- text-shadow: -1px 0 #00d4ff (cyan right)
- clip-path animations for glitch effect

### Textures & Patterns (CRITICAL FOR DEPTH)

1. **Scanlines Overlay** (CSS pseudo-element):
```css
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 2px,
  rgba(0, 0, 0, 0.3) 2px,
  rgba(0, 0, 0, 0.3) 4px
);
pointer-events: none;
```

2. **Grid/Circuit Pattern** (subtle background):
```css
background-image:
  linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
background-size: 50px 50px;
```

3. **Noise Texture**: Apply subtle CSS noise filter or SVG noise overlay at 5-10% opacity

4. **Gradient Mesh**: Radial gradients of accent colors at very low opacity in corners

---

## 3. Component Stylings

### Buttons

All buttons use:
- Font: monospace
- Text transform: uppercase
- Letter spacing: wider
- Transition: all for smooth effects
- Focus ring: 2px accent color

**Default Variant**:
```
- Background: transparent
- Border: 2px solid accent (#00ff88)
- Text: accent color
- Clip-path: .cyber-chamfer-sm (smaller chamfer)
- Hover: background fills with accent, text becomes background color, neon glow shadow
```

**Secondary Variant**:
```
- Border: 2px solid accentSecondary (#ff00ff)
- Text: accentSecondary
- Hover: fills with magenta, neon-secondary glow
```

**Outline Variant**:
```
- Border: 1px solid border (#2a2a3a)
- Background: transparent
- Hover: border becomes accent, text becomes accent, neon glow appears
```

**Ghost Variant**:
```
- No border
- Hover: background accent/10 opacity, text becomes accent
```

**Glitch Variant** (CTAs):
```
- Background: solid accent (#00ff88)
- Text: background color (high contrast)
- Uses .cyber-glitch class for chromatic aberration effect
- Hover: brightness increases (filter: brightness(1.1))
```

### Cards/Containers

**Default Card Variant**:
```
- Background: card (#12121a)
- Border: 1px solid border (#2a2a3a)
- Clip-path: chamfered corners via .cyber-chamfer class
- Transition: all 300ms for smooth interactions
- Hover: translateY(-1px), border becomes accent, neon glow appears (if hoverEffect prop)
```

**Terminal Variant** (variant="terminal"):
```
- Background: background (#0a0a0f) instead of card
- Border: 1px solid border
- Automatic decorative header bar with traffic light dots (red/yellow/green)
- Content padding-top to accommodate header
- Clip-path: chamfered corners
- Used for: Blog cards, FAQ items, some pricing tiers
```

**Holographic Variant** (variant="holographic"):
```
- Background: muted (#1c1c2e) at 30% opacity
- Border: 1px solid accent at 30% opacity
- Box-shadow: neon glow
- Backdrop-filter: blur for glassmorphic effect
- Corner accents: 4 small border corners at card edges using absolute positioning
- Used for: Product details card, hero HUD panels
```

### Inputs

```
- Wrapper: relative positioning for prefix icon
- Prefix: ">" symbol in accent color, absolute positioned left
- Background: input (#12121a)
- Border: 1px solid border (#2a2a3a)
- Clip-path: .cyber-chamfer-sm
- Text: monospace, accent color
- Padding-left: 8 (to accommodate prefix)
- Placeholder: mutedForeground, styled as terminal prompt
- Focus: border becomes accent, neon glow shadow, outline removed
- Transition: all 200ms
```

---

## 4. Layout Strategy

**Max-Width**: `max-w-7xl` for main content, full-bleed sections with contained inner content

**Grid Patterns**:
- Features: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` with `-skew-y-1` on container
- Pricing: `grid-cols-1 md:grid-cols-3` with middle card scaled up
- Stats: Horizontal flex with `divide-x divide-border`

**Spacing**: 8px base grid. Generous padding (`py-24` to `py-32` for sections). Dense internal component spacing.

**Asymmetry Requirements**:
- Hero: 60/40 split minimum
- At least one section with overlapping elements (negative margins)
- Use `rotate-1` or `skew-y-1` transforms on section containers
- Stagger card heights in grid where content allows

---

## 5. Non-Genericness (THE BOLD FACTOR)

**MANDATORY BOLD CHOICES**:

1. **Glitched Headlines**: Hero h1 MUST have chromatic aberration text-shadow AND a CSS animation that occasionally "glitches" (random skew/translate flicker)

2. **Scanline Overlay**: The entire page has a subtle scanline overlay (via ::after on body or main)

3. **Terminal Aesthetic**: At least one section must feel like a terminal (monospace, > prefixes, blinking cursor animations)

4. **Neon Borders That Actually Glow**: Not just colored borders - stacked box-shadows creating real glow effect

5. **Corner Cuts**: Cards use clip-path for chamfered/cut corners, not rounded corners

6. **Animated Elements**:
   - Blinking cursors (animation: blink 1s step-end infinite)
   - Subtle hover glitch effects
   - Gradient border animations (hue rotation)

7. **Circuit/Grid Background**: Visible tech-pattern in at least one section background

8. **Typing/Typewriter Effect**: Consider on subtitle or at least style as if mid-type (trailing cursor)

---

## 6. Effects & Animation

**Motion Feel**: Sharp, digital, slightly mechanical. Quick snaps rather than smooth eases.

**Transitions**:
```css
transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
/* Or for more digital feel: */
transition: all 100ms steps(4);
```

**Keyframe Animations**:

```css
/* Blink cursor */
@keyframes blink {
  50% { opacity: 0; }
}

/* Glitch effect */
@keyframes glitch {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(2px, -2px); }
  60% { transform: translate(-1px, -1px); }
  80% { transform: translate(1px, 1px); }
}

/* Scanline scroll */
@keyframes scanline {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100vh); }
}

/* RGB shift/chromatic pulse */
@keyframes rgbShift {
  0%, 100% { text-shadow: -2px 0 #ff00ff, 2px 0 #00d4ff; }
  50% { text-shadow: 2px 0 #ff00ff, -2px 0 #00d4ff; }
}
```

---

## 7. Iconography

**Lucide Icons Configuration**:
- Stroke width: `1.5px` (thin, technical feel)
- Size: Generally `h-5 w-5` or `h-6 w-6`
- Color: Inherit from text (usually accent or foreground)
- Style: Add subtle glow on hover via filter: `drop-shadow(0 0 4px currentColor)`

**Icon Containers**: Place icons inside bordered squares/hexagons with glow effect

---

## 8. Responsive Strategy

**Mobile Adaptations** (Mobile-first approach):

**Typography Scaling**:
- Hero h1: text-5xl (mobile) → text-7xl (md) → text-8xl (lg)
- Subheadline: text-base → text-lg → text-xl
- Section headings: text-4xl → text-5xl
- Maintain uppercase and tracking at all sizes

**Layout Changes**:
- Navigation: Hide nav links on < lg, show abbreviated CTA text on < sm
- Stats: 2x2 grid with borders only on top 2 items (mobile) → 4-column with vertical borders (desktop)
- All feature/blog/testimonial grids: Single column → 2-column (md) → 3-column (lg)
- Pricing: Stack vertically → 3-column grid, highlighted card scale only on md+
- Hero HUD: Hidden on mobile (lg:block)
- Footer: Stack to single column → 4-column grid

**Maintained Elements**:
- Scanline overlay (full page)
- Chamfered corners on all cards
- Neon glow effects (may reduce intensity on mobile for performance)
- Grid/circuit backgrounds
- Monospace typography
- Terminal aesthetic (>, $, prefixes)
- Dark color scheme

**Touch Targets**:
- Minimum 44px height for all interactive elements
- Adequate spacing between tappable items
- FAQ accordions with full-width click area

---

## 9. Accessibility

**Contrast**: All text meets WCAG AA (accent green on dark bg = 7.5:1 ratio - excellent)

**Focus States**:
```css
focus-visible:outline-none
focus-visible:ring-2
focus-visible:ring-accent
focus-visible:ring-offset-2
focus-visible:ring-offset-background
```
Plus add glow effect matching the neon aesthetic.

**Reduced Motion**: Respect `prefers-reduced-motion` - disable glitch animations, keep static chromatic aberration

---

## 10. Implementation Notes

- Use Tailwind arbitrary values `[...]` extensively for custom shadows and clip-paths
- CSS variables for colors enable easy theming
- Scanlines implemented via CSS, not images
- Glitch animations should be subtle and infrequent (not distracting)
- Test glow effects on different screens (can look washed out on low contrast displays)
- Consider GPU performance with multiple box-shadows - use `will-change: transform` sparingly

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH CYBERPUNK
Bố cục và nhận diện: Nền #0a0a0f, green #00ff88 chủ đạo, magenta #ff00ff và cyan #00d4ff phụ; Orbitron/Share Tech Mono theo nguồn. Clip góc, scanline, HUD và glitch có vai trò riêng; khác Outrun ở mật độ kỹ thuật và cấu trúc đô thị.

## 3. Nội dung mở đầu

**H1:** NIGHT SHIFT · dựng thứ bạn muốn chơi.

**Lời dẫn:** Một game jam cuối tuần dành cho người làm hình, âm thanh và lập trình. Thông tin cộng đồng trên trang là minh họa.

**Hành động chính:** Tìm đội minh họa

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Lời mời tham gia

**Bố cục và hành vi:** Headline và poster game nguyên bản, ba nhãn vai trò bên dưới; CTA Tìm đội mẫu.

**Nội dung và đầu ra:** Không dùng số người online giả hoặc countdown giả khan hiếm.

### 2. Đề bài và giới hạn

**Bố cục và hành vi:** Khối nhiệm vụ có mục tiêu, giới hạn thời gian minh họa, tài sản được dùng và đầu ra.

**Nội dung và đầu ra:** Ví dụ làm một game ngắn xoay quanh ánh sáng; không lời hứa giải thưởng hoặc nhà tài trợ bịa.

### 3. Tìm đội

**Bố cục và hành vi:** Sáu đội mẫu có vai trò đang tìm và ý tưởng; filter Lập trình/Hình/Âm thanh.

**Nội dung và đầu ra:** Chọn đội mở hồ sơ và lịch dự kiến; không gửi tin nhắn thật.

### 4. Bảng tiến độ

**Bố cục và hành vi:** Ba giai đoạn Ý tưởng/Bản chơi thử/Trình diễn, gắn một đội mẫu xuyên suốt.

**Nội dung và đầu ra:** Dữ liệu minh họa có nhãn, không realtime hoặc cập nhật ngẫu nhiên.

### 5. Hồ sơ tham gia mẫu

**Bố cục và hành vi:** Chọn vai trò và viết điều muốn làm, hiển thị hồ sơ ghép đội thử.

**Nội dung và đầu ra:** Không thu tài khoản mạng xã hội hay giả tham gia đã được duyệt.

## 5. Dữ liệu và trạng thái tương tác

roleFilter lọc đúng team needs; selectedTeam giữ khi quay lại. Form cần vai trò và ý tưởng; empty filter có reset. Không nút gửi tin thật.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

390 px HUD chuyển thành ba khối đọc dọc, đoạn dài không mono quá nhỏ; clip-path không cắt hitbox hoặc focus. H1 42–56 px, body 16–18 px.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Glitch ngắn 120 ms khi chủ động hover, không lặp chớp toàn màn; scanline tĩnh. Pause mọi loop nền và reduced-motion không glitch.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Artwork AI thế giới game nguyên bản và hình dự án hư cấu; tránh hình thương hiệu game có sẵn.

**Cover:** Poster game, tiêu đề và một nhãn tìm đội, neon xanh chủ đạo; không sunset/lưới đường chân trời của Vaporwave.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Lọc vai trò thay đúng danh sách đội.
2. Focus không bị clip-path cắt.
3. Bản giảm chuyển động còn đủ ngôn ngữ HUD và tương phản neon.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
