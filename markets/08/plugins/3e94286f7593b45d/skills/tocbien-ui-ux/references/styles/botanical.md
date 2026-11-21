# Botanical (`botanical`)

Xanh lá dịu, chữ có chân nghiêng, khối bo vòm

- Hợp với: Hợp khi đang dùng AI để dựng website cho spa và chăm sóc sức khỏe nhẹ nhàng, nơi đặt lịch là việc chính.
- Ngành minh hoạ: Spa, mỹ phẩm thiên nhiên, phòng trà
- Trang minh hoạ làm việc gì: Không gian thư giãn chọn dịch vụ theo nhu cầu và khung giờ
- Thang (1–10): biến tấu bố cục 5 · chuyển động 2 · mật độ 3
- Xem mẫu: https://tocbien.cloud/phong-cach/botanical/

## Đặc tả

Botanical: nền trắng ngả xanh #f3f6f0, mực xanh sẫm #1f2b22, nhấn xanh rêu #2f4a34. Tiêu đề serif có một cụm nghiêng, thân bài sans-serif. Hero cân bằng chữ với ảnh cây hoặc không gian chăm sóc thật trong khung bo vòm; các mục dịch vụ, nguyên liệu, quy trình và đặt lịch chỉ xuất hiện khi có nội dung. Thẻ trắng viền nhẹ, bo khoảng 18px; nút xanh đậm dạng viên thuốc. Không thay ảnh spa bằng gradient. Trên điện thoại ảnh xuống dưới chữ, các dịch vụ xếp dọc, menu vẫn mở được.

**Chi tiết cần giữ:** Font phải có bộ dấu tiếng Việt — nhiều font có chân đẹp lại thiếu, làm chữ ồ ề ấ vỡ thành dấu rời. Kiểm bằng cách gõ thử 'rồi, bằng, đến, ấm' trước khi chốt.

**Lưu ý khi áp dụng:** Đừng dùng cho thứ cần cảm giác dứt khoát. Kiểu này nói rằng ở đây mọi thứ diễn ra chậm.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Design Style: Botanical / Organic Serif

## 1. Design Philosophy

This style is a **digital ode to nature**—it breathes, flows, and grounds itself in organic beauty. It is **soft, sophisticated, and deeply intentional**, rejecting the rigid, hyper-digital sharpness of modern tech aesthetics in favor of **warmth, tactility, and natural imperfection**.

### Core Essence
The Botanical Organic style embodies the calming presence of a botanical garden, the earthy warmth of a ceramics studio, and the refined elegance of editorial design. It whispers rather than shouts. Every element feels **hand-touched, sun-warmed, and naturally crafted**.

### Fundamental Principles

*   **Vibe**: Peaceful, curated, artisanal, high-end wellness, sustainable luxury, botanical elegance
*   **Visual DNA**:
    *   **Organic Softness**: Hard angles are purposefully rare. Every corner is rounded, every shape flows like water-smoothed stones or unfurling leaves. The 200px arch radius on images creates iconic architectural moments.
    *   **Typographic Elegance**: Typography is the protagonist—Playfair Display's high-contrast strokes command attention while maintaining grace. Italics add a handwritten, personal touch. Headlines breathe with generous scale (text-5xl to text-8xl).
    *   **Earthbound Palette**: Every color derives from nature—forest floors, clay pottery, sage gardens, terracotta tiles. No artificial brights. Muted, sophisticated, grounded.
    *   **Tactile Texture**: The subtle paper grain overlay is non-negotiable—it transforms cold digital pixels into warm, touchable surfaces. This is the secret ingredient that prevents flatness.
    *   **Breathing Space**: Whitespace is sacred. Sections have generous vertical padding (py-32), cards float with ample gaps (gap-8, gap-16), and every element has room to exist without crowding.
    *   **Intentional Movement**: Animations are slow, graceful, and fluid—like plants swaying in breeze. Duration-500 to duration-700 with ease-out curves. Nothing snaps or jerks.
    *   **Staggered Rhythm**: Breaking the grid creates natural, organic flow. Every second feature card translates vertically. Images rotate subtly. The design breathes asymmetry within structure.

## 2. Design Token System

### Colors (Light Mode - Earthy & Muted)
*   **Background**: `#F9F8F4` (Warm Alabaster / Rice Paper) - Not stark white.
*   **Foreground**: `#2D3A31` (Deep Forest Green) - The primary text color. Softer than black.
*   **Primary/Accent**: `#8C9A84` (Sage Green) - For buttons, highlights, icons.
*   **Secondary/Muted**: `#DCCFC2` (Soft Clay / Mushroom) - For backgrounds of cards, secondary buttons.
*   **Border**: `#E6E2DA` (Stone) - Very subtle, low contrast.
*   **Interactive**: `#C27B66` (Terracotta) - Hover states or "call to action" pops.

### Typography
*   **Headings**: **"Playfair Display"** (Google Font). It is a transitional serif with high contrast strokes, feeling both classic and modern.
    *   Weight: 600/700 for headlines.
    *   Style: Italicize key words for emphasis.
*   **Body**: **"Source Sans 3"** (Google Font). A clean, legible humanist sans-serif that pairs beautifully with Playfair.
    *   Weight: 400/500.
*   **Scaling**: Large. Headlines should feel airy and grand.

### Radius & Shapes
*   **Radius**: Highly rounded.
    *   Standard Card: `rounded-3xl` (24px).
    *   Buttons: `rounded-full` (Pill shape).
    *   Images: Often `rounded-t-full` (Arch) or `rounded-[40px]`.
*   **Border**: Thin, delicate. `1px` solid.

### Shadows & Effects
*   **Elevation**: Very soft, diffused shadows. No harsh dark drops.
    *   Default: `0 4px 6px -1px rgba(45, 58, 49, 0.05)`
    *   Medium: `0 10px 15px -3px rgba(45, 58, 49, 0.05)`
    *   Large: `0 20px 40px -10px rgba(45, 58, 49, 0.05)`
    *   Extra Large: `0 25px 50px -12px rgba(45, 58, 49, 0.15)`
*   **Paper Grain Texture** (CRITICAL): A subtle SVG noise overlay is **mandatory** on the main background. This is applied as a fixed, full-screen overlay with `opacity-[0.015]` using an SVG fractal noise filter. This texture is the defining element that transforms the design from flat digital to warm, tactile, paper-like. Without it, the design loses its soul.
    ```jsx
    <div
      className="pointer-events-none fixed inset-0 z-50 opacity-[0.015]"
      style={{
        backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
        backgroundRepeat: "repeat",
      }}
    />
    ```
*   **Blur Effects**: Use backdrop-blur-sm on overlays (like the hero quote card) to create depth and layering.

## 3. Component Stylings

### Buttons
*   **Primary**: Pill-shaped (`rounded-full`). Background is **Deep Forest Green** (`#2D3A31`) with White text. On hover, it lightens slightly or shifts to Terracotta.
*   **Secondary**: Transparent background with a **Sage Green** border (`1px`). Text is Sage Green.
*   **Typography**: Uppercase, wide tracking (`tracking-widest`), small font size (text-sm).

### Cards (Features, Pricing)
*   **Background**: White (`#FFFFFF`) or Soft Clay (`#F2F0EB`).
*   **Border**: None or very subtle Stone (`#E6E2DA`).
*   **Shape**: `rounded-3xl`.
*   **Hover**: Slight lift (`-translate-y-1`) and a bloom of soft shadow.

### Inputs
*   **Style**: Underlined only (Border-bottom) or pill-shaped with a very light background (`#F2F0EB`).
*   **Focus**: No harsh blue rings. A soft Sage Green border transition.

## 4. Non-Generic "Bold" Choices
*   **Arch Imagery**: Use CSS `clip-path` or `border-radius` to turn standard rectangular images into **Arches** (classic Roman arch shape) or **Organic Blobs**.
*   **Overlapping Typography**: Allow big serif headlines to slightly overlap images or background shapes.
*   **Decorative Lines**: Use fine, 1px SVG lines that curve or meander to connect sections, mimicking vines or roots.
*   **Italic Emphasis**: Frequently use the *Italic* variant of Playfair Display for single words within a bold headline.

## 5. Layout Strategy & Spacing
*   **Container**: `max-w-7xl`. We want airiness.
*   **Whitespace**: Generous. `gap-12` or `gap-16` between grid items. `py-24` or `py-32` between sections.
*   **Grid**: Break the grid. Use `translate-y-12` on every second card in a row to create a "staggered" natural look.

## 6. Icons (Lucide React)
*   **Style**: Thin stroke (`stroke-width={1.5}`).
*   **Color**: Deep Forest Green or Sage.
*   **Integration**: Don't put them in heavy boxes. Let them float, or place them in soft, pale circles.

## 7. Animation & Micro-Interactions
*   **Feel**: Slow, graceful, fluid. Everything moves like it's suspended in honey or swaying in a gentle breeze. "Eased out" significantly.
*   **Durations**:
    *   Fast interactions: `duration-300` (button hovers, link colors)
    *   Standard: `duration-500` (card lifts, transforms)
    *   Slow, dramatic: `duration-700` to `duration-1000` (image scales, hero image hover)
*   **Hover Behaviors**:
    *   Cards: `-translate-y-1` or `-translate-y-2` with shadow intensification
    *   Images: `scale-105` with `duration-700` for smooth, luxurious feel
    *   Buttons: `bg-opacity-90` subtle darkening with `duration-300`
    *   Blog cards: Lift entire card while scaling image, arrow translates right (`translate-x-1`)
*   **Focus States**: Sage green ring (`ring-[#8C9A84]`) with 2px width and offset for accessibility
*   **Accordion**: Smooth height transitions with `max-h-0` to `max-h-48` and opacity fade
*   **Mobile Menu**: Slide in from top with backdrop
*   **Scroll**: Elements should gently fade up and float into place (`opacity-0` to `opacity-100`, `translate-y-4` to `translate-y-0`)

## 8. Responsive Strategy
*   **Mobile-First Approach**: The design gracefully adapts while maintaining its organic, sophisticated character.
*   **Navigation**: Desktop shows horizontal nav with Sign In button. Mobile displays hamburger menu that opens a full-screen overlay with vertical nav links.
*   **Hero Image**: Uses `aspect-[3/4]` on mobile, transitions to `aspect-square` with fixed height on md+ breakpoints. This prevents excessive height on small screens.
*   **Grid Breakpoints**:
    *   Features: `grid-cols-1` → `md:grid-cols-3`
    *   Stats: `grid-cols-2` → `md:grid-cols-4`
    *   Blog/Testimonials: `grid-cols-1` → `md:grid-cols-3`
    *   Pricing: `grid-cols-1` → `lg:grid-cols-3`
*   **Typography Scaling**: Headlines reduce from `text-8xl` to `text-5xl` on mobile. Body text remains `text-lg` but line-height adjusts.
*   **Spacing Adjustments**: `py-32` becomes `py-16` on mobile, `gap-16` becomes `gap-12`, padding reduces from `p-8` to `p-4` where needed.
*   **Touch Targets**: All buttons maintain minimum 44px height (`h-12`, `h-14`) for comfortable mobile tapping.
*   **Staggered Cards**: The `translate-y-12` offset on alternating cards only applies at `md:` breakpoint and above to prevent awkward stacking on mobile.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH BOTANICAL
Bố cục và nhận diện: Playfair Display cùng font body từ nguồn; nền #F9F8F4, chữ forest #2D3A31, sage #8C9A84, clay #DCCFC2. Lưới so le 5/7; ảnh vòm cao, nét lá mảnh không chạm chữ. H1 64–80 px, khoảng section 96 px.

## 3. Nội dung mở đầu

**H1:** Dành một khoảng dịu lại.

**Lời dẫn:** Chọn một buổi thư giãn theo thời gian và cảm giác bạn đang tìm kiếm.

**Hành động chính:** Chọn buổi thư giãn

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Buổi thư giãn

**Bố cục và hành vi:** Ảnh vòm phòng chăm sóc và headline; có link Chọn buổi phù hợp.

**Nội dung và đầu ra:** Bối cảnh Thảo An, nhân vật/địa điểm minh họa. Không hứa điều trị hoặc giảm bệnh.

### 2. Chọn theo nhu cầu

**Bố cục và hành vi:** Ba lựa chọn Nghỉ ngắn/Thư giãn dài/Trải nghiệm thảo mộc; mỗi lựa chọn có thời lượng và mô tả.

**Nội dung và đầu ra:** Đưa khác biệt dịch vụ ra chữ cụ thể thay ba câu cảm xúc giống nhau.

### 3. Điều diễn ra trong buổi

**Bố cục và hành vi:** Ba đoạn Đón tiếp/Trải nghiệm/Kết thúc xen ảnh chất liệu.

**Nội dung và đầu ra:** Nêu trải nghiệm, mùi hương và quyền yêu cầu điều chỉnh; không chỉ hình lá.

### 4. Lịch minh họa

**Bố cục và hành vi:** Chọn ngày mẫu và khung giờ; tóm tắt dịch vụ được giữ trên cùng panel.

**Nội dung và đầu ra:** Có slot không khả dụng để minh họa trạng thái, ghi rõ không phản ánh lịch thật.

### 5. Trước khi tới

**Bố cục và hành vi:** Checklist đồ cần chuẩn bị và form ghi chú mong muốn.

**Nội dung và đầu ra:** CTA Xem yêu cầu mẫu; không giả liên hệ đã gửi.

## 5. Dữ liệu và trạng thái tương tác

serviceId thay đổi duration và danh sách slot tương ứng; đổi dịch vụ xóa slot không còn phù hợp và báo lý do. Không cho xác nhận khi chưa có giờ; có sửa lựa chọn.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

390 px đưa lựa chọn dịch vụ trước câu chuyện thương hiệu dài; vòm ảnh 240–300 px; lịch 2 cột slot; text 16–18 px. Border focus rõ trên sage, không dựa vào màu lá nhạt.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Lá có dịch chuyển 2–4 px rất chậm nếu cần; ảnh reveal 600 ms, chọn slot 180 ms. Reduced-motion không làm mất nội dung.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Bộ ảnh AI thảo mộc và phòng cùng nhận diện; không ảnh trước/sau giả hoặc kết quả điều trị bịa.

**Cover:** Một vòm ảnh phòng, lá mảnh bên lề và serif; dọc giảm phần nav để thấy dịch vụ. Không phủ leaf texture lên mặt/người/chữ.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Đổi dịch vụ có slot cũ không hợp lệ phải yêu cầu chọn lại.
2. Nhãn lịch mẫu xuất hiện trước thao tác xác nhận.
3. Nút/label không chìm vào màu sage.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
