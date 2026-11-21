# Vaporwave (`vaporwave`)

Hoàng hôn neon, lưới phối cảnh và chữ điện tử

- Hợp với: Hợp khi đang dùng AI để dựng website cho landing âm nhạc, sự kiện và văn hóa cần không khí mạnh nhưng lịch vẫn dễ đọc.
- Ngành minh hoạ: Âm nhạc, sự kiện, văn hoá
- Trang minh hoạ làm việc gì: Đêm nghe nhạc điện tử với ba tiết mục và lựa chọn chỗ mẫu
- Thang (1–10): biến tấu bố cục 9 · chuyển động 7 · mật độ 5
- Xem mẫu: https://tocbien.cloud/phong-cach/vaporwave/

## Đặc tả

Nền #090014, magenta/cyan/cam; Orbitron, JetBrains Mono và Share Tech Mono. Hoàng hôn sọc, sàn lưới phối cảnh, chữ chrome chuyển sắc, cửa sổ lịch nghe, nút xiên, timeline và trò chuyện kiểu IRC.

**Chi tiết cần giữ:** Trên điện thoại xếp nội dung theo thứ tự đọc; hỗ trợ bàn phím, focus rõ và prefers-reduced-motion. Mọi số liệu trong bản minh hoạ phải được ghi rõ.

**Lưu ý khi áp dụng:** Giữ chữ tiếng Việt rõ, nút dễ bấm và hiệu ứng không che nội dung.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Vaporwave / Outrun Design System

## 1. Design Philosophy

**"Digital Nostalgia meets Neon Future — A synthetic reality drenched in retro-futuristic excess."**

This is a bold celebration of 1980s retro-futurism, vaporwave aesthetics, and early computer graphics. The design transports users to a synthetic digital dimension where neon lights pierce through infinite grids, CRT scanlines distort reality, and every interaction feels like commanding a vintage terminal from the year 2088.

### Core Aesthetic DNA

**Visual Language**: High-contrast maximalism with unapologetic neon saturation. Nothing is subtle. Every element glows, transforms, or pulses with digital energy. The design rejects minimalism in favor of dense, layered visual effects that create depth through overlapping gradients, glows, scanlines, and perspective distortions.

**Emotional Tone**: Nostalgic yet futuristic. Simultaneously retro (80s arcade cabinets, VHS tapes, early Windows UIs) and forward-looking (cyberpunk cityscapes, holographic interfaces, digital utopias). The mood is dreamy, synthetic, slightly surreal — like navigating a computer from a past vision of the future.

**Design Pillars**:
1. **The Infinite Grid**: Perspective-transformed wireframe grids that recede toward the horizon, creating spatial depth and that iconic outrun highway feeling
2. **Neon Glow Supremacy**: Hot magenta (#FF00FF), electric cyan (#00FFFF), and sunset orange (#FF9900) with aggressive drop shadows and box shadows that make elements appear to emit light
3. **CRT Scanlines & Distortion**: Global overlay of horizontal scanlines and subtle RGB chromatic aberration mimicking old CRT monitors
4. **Terminal/Command-Line Interfaces**: Text prefixed with ">" symbols, monospace fonts, window chrome with colored dots, status bars — everything references DOS prompts and early GUIs
5. **Geometric Transformation**: Skewed containers, rotated icons, perspective grids — elements are rarely perfectly aligned; they feel kinetic and dimensional
6. **Gradient Mania**: Multi-stop gradients everywhere — text fills, backgrounds, borders, glows. Especially the iconic sunset gradient (yellow → orange → pink → purple)

### Interaction Philosophy

**Hover States Are Theatrical**: Buttons don't just change color — they un-skew, explode with glow, scale up, and invert colors. Icons rotate. Cards lift off the page. Every interaction is a micro-event.

**Sound Design (Visual)**: If this design had sound, it would be the hum of neon tubes, the buzz of CRT static, retro synthesizers, and lo-fi beats. The visual design echoes this through pulsing animations, glitch effects, and rhythmic repetition (scanlines, grid patterns).

### The "Anti-Patterns" (What This Is NOT)
- **Not Flat**: Aggressive use of shadows, glows, gradients, and depth
- **Not Minimalist**: Dense with effects, borders, patterns, and overlays
- **Not Corporate**: Playful, artistic, experimental — this is a portfolio piece, not a bank
- **Not Muted**: Colors are 100% saturated; contrasts are extreme

## 2. Design Token System (The DNA)

### Colors (Dark Mode Only)

**Philosophy**: Maximum saturation, high contrast, pure digital primaries. These aren't subtle brand colors — they're neon tubes glowing in a dark void.

*   **Background (The Void)**: `#090014` — Near-black with a subtle purple tint. This is the infinite digital space where everything floats.
*   **Foreground (Chrome Text)**: `#E0E0E0` — Light silver-gray for body text. Readable yet retro.
*   **Card Background (Glass Panels)**: `rgba(26, 16, 60, 0.8)` or `#1a103c` — Semi-transparent deep purple. Enables glass-morphism with backdrop blur.
*   **Primary Accent (Hot Magenta)**: `#FF00FF` — Pure magenta. Used for primary CTAs, highlights, avatars, feature icons, accent borders. This is THE hero color.
*   **Secondary Accent (Electric Cyan)**: `#00FFFF` — Pure cyan. Used for links, focus rings, secondary borders, hover states, card title glows. Complements magenta perfectly.
*   **Tertiary Accent (Sunset Orange)**: `#FF9900` — Vibrant orange. Used sparingly for special highlights, "sun" gradients, and attention-grabbing elements.
*   **Border (Default)**: `#2D1B4E` — Muted dark purple. Non-interactive borders and dividers.
*   **Border (Active)**: `#00FFFF` or `#FF00FF` — Neon borders for interactive/hovered elements.

**Gradient Combinations**:
- **Sunset Gradient**: `linear-gradient(to right, #FF9900, #FF00FF, #00FFFF)` — The signature vaporwave gradient used for text fills
- **Glow Gradient**: `linear-gradient(to bottom, #FF9900, #FF00FF)` — Used for the floating "sun" background element
- **Accent Bar**: `linear-gradient(to right, #FF00FF, #00FFFF)` — Sharp gradient for top borders and accent lines

### Typography

**Font Philosophy**: Fonts must evoke both retro computing terminals and futuristic sci-fi interfaces. Geometric sans-serifs for impact, monospace for authenticity.

*   **Headings**: `"Orbitron", sans-serif` (weights: 400, 500, 700, 900)
    - Geometric, wide, futuristic letterforms
    - Used for: Page titles, section headings, card titles, pricing
    - Characteristics: All-caps preferred, extreme weights (black/900), tight tracking on large sizes
*   **Body/UI/Code**: `"Share Tech Mono", monospace` (weight: 400)
    - Technical, terminal-like, fixed-width
    - Used for: Body text, buttons, labels, input fields, status text
    - Characteristics: Uppercase for UI elements, normal case for body copy, wide letter-spacing (tracking)

**Type Scale & Hierarchy**:
- **Hero Headlines**: `text-5xl` to `text-9xl` (80px-128px) with responsive scaling. Split across multiple lines for drama.
- **Section Headings**: `text-3xl` to `text-6xl` (30px-60px). Always bold/black weight.
- **Card/Component Titles**: `text-2xl` (24px). Cyan color with text glow.
- **Body Text**: `text-lg` to `text-xl` (18px-20px). Generous line-height for readability.
- **UI Labels/Buttons**: `text-sm` to `text-lg`, all-caps, wide tracking (`tracking-wider`, `tracking-widest`).

**Text Effects**:
- **Glow on Headings**: `drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]` for white text, `drop-shadow-[0_0_30px_rgba(255,0,255,0.6)]` for gradient text
- **Card Title Glow**: `drop-shadow-[0_0_5px_rgba(0,255,255,0.8)]` on cyan titles
- **Gradient Text Fill**: Use `bg-gradient-to-r from-[#FF9900] via-[#FF00FF] to-[#00FFFF] bg-clip-text text-transparent` for hero statements

### Radius & Borders

**Border Philosophy**: Sharp, geometric, high-contrast. Borders are neon light tubes, not subtle dividers.

*   **Border Radius**: `rounded-none` (0px) is primary. Vaporwave is aggressively geometric and angular. Occasional `rounded-full` for dots/circles only.
*   **Border Width**: `border-2` (2px) is standard. Heavier borders (`border-4`) for emphasis or outer containers.
*   **Border Colors**:
    - Default/Inactive: `#2D1B4E` (dark purple, subtle)
    - Interactive/Hover: `#00FFFF` (cyan) or `#FF00FF` (magenta)
    - Top Accent Bars: Gradient or solid cyan (`border-t-2 border-t-[#00FFFF]`)
*   **Multi-Border Patterns**: Cards often have a colored top border (`border-t-2`) plus subtle side borders in different colors for layered effect

### Shadows & Effects (The Glow)

**Effect Philosophy**: Everything emits light. Shadows are colored glows, not dark drops.

*   **Box Shadows (Neon Glow)**:
    - **Magenta Glow**: `shadow-[0_0_10px_#FF00FF]` or `shadow-[0_0_20px_#FF00FF]` for intense glow
    - **Cyan Glow**: `shadow-[0_0_20px_rgba(0,255,255,0.2)]` for containers, `shadow-[0_0_15px_#00FFFF]` for inputs
    - **Large Area Glow**: `shadow-[0_0_50px_rgba(0,255,255,0.2)]` for major containers like final CTA
*   **Text Shadows (See Typography section)**
*   **Hover State Glows**: Buttons and interactive elements dramatically increase glow intensity on hover (2x-3x the base glow)

### Textures & Background Patterns

**Pattern Philosophy**: The void is never empty. Layers of grids, scanlines, dots, and gradients create dimensional depth.

*   **Perspective Grid Floor**:
    ```css
    background-image: linear-gradient(transparent 95%, #FF00FF 95%), linear-gradient(90deg, transparent 95%, #FF00FF 95%);
    background-size: 40px 40px;
    transform: perspective(500px) rotateX(60deg) translateY(-100px) scale(2);
    mask-image: linear-gradient(to bottom, transparent, black);
    ```
    Creates the iconic receding grid effect
*   **Floating Sun**: Massive blurred gradient orb (`h-[600px] w-[600px] blur-[100px] bg-gradient-to-b from-[#FF9900] to-[#FF00FF] opacity-20`)
*   **Global Scanlines Overlay**:
    ```css
    background: linear-gradient(rgba(18,16,20,0) 50%, rgba(0,0,0,0.25) 50%);
    background-size: 100% 4px;
    ```
    Applied as fixed overlay to entire page for CRT effect
*   **RGB Chromatic Aberration** (subtle): `linear-gradient(90deg, rgba(255,0,0,0.06), rgba(0,255,0,0.02), rgba(0,0,255,0.06))`
*   **Dot Patterns**: `radial-gradient(#FF00FF 1px, transparent 1px)` with `background-size: 20px 20px` for section backgrounds
*   **Gradient Overlays on Images**: Duotone effect via `bg-gradient-to-br from-[#FF00FF] to-[#00FFFF] opacity-20 mix-blend-overlay`

## 3. Component Stylings

### Buttons

**Primary Button** (`variant="primary"`):
```tsx
// Skewed container that un-skews on hover
-skew-x-12 transform
border-2 border-[#00FFFF]
bg-transparent
text-[#00FFFF]
rounded-none
uppercase tracking-wider font-mono

// Hover state
hover:skew-x-0
hover:bg-[#00FFFF]
hover:text-black
hover:shadow-[0_0_20px_#00FFFF]

// Inner content is counter-skewed
<span className="inline-block skew-x-12 transform">{children}</span>
```

**Secondary Button** (`variant="secondary"`):
```tsx
-skew-x-12 transform
border-2 border-[#FF00FF]
bg-[#FF00FF]
text-white
rounded-none

hover:skew-x-0
hover:scale-105
hover:opacity-80
```

**Outline Button** (`variant="outline"`):
```tsx
border-2 border-[#FF00FF]
bg-transparent
text-[#FF00FF]
rounded-none

hover:bg-[#FF00FF]
hover:text-white
```

**Ghost Button** (`variant="ghost"`):
```tsx
text-[#E0E0E0]
rounded-none

hover:bg-[rgba(0,255,255,0.1)]
hover:text-[#00FFFF]
```

**Sizes**: `sm` (h-9), `default` (h-12), `lg` (h-14), `icon` (h-10 w-10)

### Cards / Containers

**Standard Card**:
```tsx
border border-[#FF00FF]/30
border-t-2 border-t-[#00FFFF]  // Laser accent on top
bg-[#1a103c]/80
backdrop-blur-md
p-6

// Card Title (cyan with glow)
font-heading font-semibold text-2xl
text-[#00FFFF]
drop-shadow-[0_0_5px_rgba(0,255,255,0.8)]

// Card Description
font-mono text-[#E0E0E0]/70 text-sm
```

**Terminal Window Container** (Product Detail style):
```tsx
// Outer border with glow
border-2 border-[#00FFFF]
bg-black/80
shadow-[0_0_20px_rgba(0,255,255,0.2)]

// Title bar
bg-[#00FFFF]/10
border-b border-[#00FFFF]
px-4 py-2

// Window control dots
<div className="flex gap-2">
  <div className="h-3 w-3 rounded-full bg-[#FF00FF]" />
  <div className="h-3 w-3 rounded-full bg-[#00FFFF]" />
  <div className="h-3 w-3 rounded-full bg-[#FF9900]" />
</div>
```

**File Explorer Window** (Benefits section):
```tsx
// Container
border-2 border-[#E0E0E0]/20
bg-[#1a103c]/90
backdrop-blur

// Title bar
bg-[#E0E0E0]/10
border-b-2 border-[#E0E0E0]/20

// Status bar
border-t-2 border-[#E0E0E0]/20
bg-[#090014]
text-[#E0E0E0]/50 text-xs
```

### Inputs

**Terminal-Style Input**:
```tsx
border-b-2 border-[#FF00FF]  // Underline only
bg-black
text-[#00FFFF] font-mono text-lg
px-3 py-2

placeholder:text-[#FF00FF]/50

focus-visible:border-[#00FFFF]
focus-visible:shadow-[0_0_15px_#00FFFF]
focus-visible:outline-none
```

## 4. Non-Generic "Bold" Choices (The "Wow" Factor)

These are mandatory unique design signatures that prevent the Vaporwave style from looking generic:

1.  **Aggressive Skewing**: Buttons and badges use `-skew-x-12` transform, creating dynamic diagonal shapes that un-skew on hover for a kinetic morphing effect
2.  **Global CRT Scanlines**: Fixed overlay across entire viewport with horizontal line pattern and RGB chromatic aberration
3.  **Perspective Grid Backgrounds**: Multiple sections use CSS perspective transforms to create the iconic receding grid floor effect
4.  **Gradient Text Fills**: Hero headlines use multi-stop gradient backgrounds clipped to text (`bg-clip-text text-transparent`)
5.  **Rotating Icon Containers**: Feature icons sit inside `rotate-45` diamond containers that spin to `rotate-90` on hover
6.  **Dual-Border Patterns**: Cards combine a bright cyan top border with subtle pink side borders for layered neon tube aesthetic
7.  **Terminal/Window Chrome**: Multiple UI patterns mimic vintage OS interfaces (window title bars with colored dots, file explorer layouts, command prompts)
8.  **Massive Blurred Sun**: Giant gradient orb in background (`600px` diameter with `blur-[100px]`) creates atmospheric depth
9.  **IRC-Style Elements**: Testimonials use chat message formatting with `<username>` angle bracket syntax
10. **Alternating Timeline Layout**: How It Works section uses alternating left-right layout with central checkpoint line
11. **Glowing Hover Amplification**: Interactive elements don't just highlight — they explode with 2-3x glow intensity and trigger color inversions

## 5. Animation & Motion

**Philosophy**: Snappy, mechanical, retro-digital. Like a CRT monitor warming up or old computer software responding to input.

*   **Transition Speed**: `duration-200 ease-linear` — Fast, unnatural, digital. No organic easing curves.
*   **Hover Transformations**:
    - Buttons: Un-skew, fill with color, invert text, explode glow
    - Cards: Translate upward (`-translate-y-2`), increase shadow
    - Icons: Rotate 45° or scale
    - Links: Add underline, change color, add glow
*   **Continuous Animations**:
    - Trust indicator: `animate-pulse` for attention
    - Terminal cursor: Could add blinking effect
    - Icons: `animate-pulse` on placeholders
*   **Transform Origins**: Use `transform-origin` carefully on perspective grids (`top center`, `bottom center`)
*   **Transition Classes**: `transition-all`, `transition-colors`, `transition-transform` depending on what's changing

## 6. Layout Strategy & Spacing

**Container Width**: `max-w-7xl` for main content, `max-w-6xl` for pricing, `max-w-4xl` for FAQ/Final CTA, `max-w-5xl` for hero

**Spacing System**:
*   **Section Padding**: `py-20 sm:py-32` (80px-128px vertical rhythm)
*   **Component Gaps**: `gap-8` (32px) for grids, `gap-12` (48px) for larger spacing
*   **Inner Padding**: Cards use `p-6` or `p-8`, containers use `px-4` on mobile
*   **Margins**: Generous — headings have `mb-8` to `mb-20` depending on size

**Grid Usage**:
*   Features: `grid-cols-1 md:grid-cols-3`
*   Stats: `grid-cols-1 md:grid-cols-2 lg:grid-cols-4`
*   Blog: `grid-cols-1 md:grid-cols-3`
*   Benefits: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
*   Pricing: `grid-cols-1 md:grid-cols-3`

**Z-Index Layering** (back to front):
1. Background grid (fixed, `z-0`)
2. Floating sun gradient (fixed)
3. Section backgrounds
4. Content (`z-10` for nav/sections)
5. Scanline overlay (fixed, `z-50`)

## 7. Responsive Strategy

**Breakpoints**: Mobile-first approach using `sm:`, `md:`, `lg:` prefixes

**Mobile Adaptations** (< 640px):
*   **Typography**: Scale down headings by 1-2 sizes (e.g., `text-5xl` instead of `text-8xl`)
*   **Spacing**: Reduce section padding from `py-32` to `py-20`, margins from `mb-20` to `mb-12`
*   **Grids**: Stack to single column (`grid-cols-1`)
*   **Buttons**: Full-width CTA buttons in hero, stacked vertically
*   **Timeline**: Left-aligned with offset instead of alternating layout
*   **Borders**: Maintain neon borders (essential to vibe)
*   **Glow Effects**: Slightly reduce intensity to prevent overwhelming small screens
*   **Grid Backgrounds**: Keep perspective grids but simplify (they add essential atmosphere)
*   **Touch Targets**: Buttons maintain minimum 44px height via `h-12` and `h-14` sizes

**Tablet** (640px - 1024px):
*   **Grids**: Often 2 columns before jumping to 3/4
*   **Typography**: Mid-range sizes
*   **Navigation**: Show full menu on tablets

**Key**: The vaporwave aesthetic MUST survive on mobile. Neon glows, borders, and grid backgrounds are non-negotiable even on small screens.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH VAPORWAVE
Bố cục và nhận diện: Poster chiếm trọng tâm, không theo split SaaS. Hero rộng 1280 px, tiêu đề Orbitron 80–110 px và dòng mono 16 px; sàn lưới ở lớp nền dưới, mặt trời sọc sau tiêu đề. Giữ magenta/cyan/cam và nền tím #090014 của brief Vaporwave / Outrun.

## 3. Nội dung mở đầu

**H1:** NEON 88 · bước vào một tối khác.

**Lời dẫn:** Một buổi nghe nhạc điện tử trong thế giới hoài niệm số. Toàn bộ lịch và nhân vật trên trang là minh họa.

**Hành động chính:** Xem chương trình / Chọn suất minh họa

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Poster sự kiện

**Bố cục và hành vi:** Tựa ở trung tâm, artwork sân khấu chạy ngang phía dưới; thời gian và địa điểm mẫu ở hai góc cùng trục.

**Nội dung và đầu ra:** Dùng thời gian minh họa Thứ Bảy · 19:00–22:00, không đồng hồ đếm ngược đến ngày giả. CTA Xem chương trình.

### 2. Chương trình

**Bố cục và hành vi:** Timeline ba mốc như cửa sổ máy tính cũ; giờ mono trái, tên tiết mục và ảnh nhỏ bên phải.

**Nội dung và đầu ra:** 19:00 Warm-up; 20:00 Neon Fields; 21:00 Afterimage. Chọn một mốc đổi artwork và mô tả tiết mục.

### 3. Không gian

**Bố cục và hành vi:** Ba ảnh cùng một sân khấu: toàn cảnh, bàn nghe và ánh sáng chi tiết; có caption ngắn.

**Nội dung và đầu ra:** Không dùng ảnh lễ hội hàng nghìn người để quảng bá buổi nghe nhỏ. Đồ họa chrome và scanline không phủ mặt nhân vật.

### 4. Chọn suất mẫu

**Bố cục và hành vi:** Cửa sổ viền cyan, hai lựa chọn chỗ đứng/chỗ ngồi có nhãn.

**Nội dung và đầu ra:** Chọn suất cập nhật tóm tắt; không yêu cầu thẻ ngân hàng. Hiện rõ Chưa tạo vé hoặc giữ chỗ.

### 5. Thông tin trước buổi nghe

**Bố cục và hành vi:** FAQ ngắn thực sự liên quan: giờ vào, nội dung buổi nghe, cách xem lịch mẫu.

**Nội dung và đầu ra:** Điều khiển tắt hiệu ứng ở vị trí nhìn thấy; không tự phát nhạc.

## 5. Dữ liệu và trạng thái tương tác

selectedSlot=null ban đầu; chọn suất bật nút Xem lựa chọn. Đổi tiết mục không xóa suất. Reset trả về không chọn; tuyệt đối không giả tồn kho vé.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

Dưới 768 px dùng poster dọc; dưới 390 px H1 40–52 px, timeline xếp dọc. Giữ transform ở khung trang trí; chữ và hitbox không nghiêng, không tạo tràn ngang.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Lưới trôi chậm 24 s linear; glow chu kỳ 6 s, không nhấp nháy nhanh. Hover unskew/glow 250 ms; nút Tắt hiệu ứng dừng mọi vòng nền và lưu lựa chọn trong phiên.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Một artwork AI sân khấu neon và hai ảnh không gian nhất quán, không ghép ảnh stock không liên quan.

**Cover:** Chụp frame mặt trời, phối cảnh và headline cùng hiện; cover dọc giữ một cửa sổ timeline. Không dùng chỉ một ảnh neon không có chữ và UI.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Pause dừng cả grid và glow; reduced-motion không có chuyển động nền.
2. Chọn từng tiết mục đổi đúng artwork/tên giờ.
3. Thu cover về 320 px vẫn nhận ra hoài niệm số và phối cảnh, chữ chính không bị cắt.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
