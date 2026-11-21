# Organic (`organic`)

Kem, xanh lá, khối bo hữu cơ, chữ tròn đậm

- Hợp với: Hợp khi đang dùng AI để dựng website cho nông sản và thực phẩm tươi cần kể rõ nguồn gốc lẫn lựa chọn mua.
- Ngành minh hoạ: Cửa hàng thực phẩm, nông sản, quán ăn
- Trang minh hoạ làm việc gì: Giỏ rau theo số người, số bữa và món có thể thay
- Thang (1–10): biến tấu bố cục 5 · chuyển động 3 · mật độ 5
- Xem mẫu: https://tocbien.cloud/phong-cach/organic/

## Đặc tả

Organic: nền kem #f7f4ec, chữ xanh đất #2c3327, xanh lá #3f6b3a làm màu hành động và đất nung làm điểm phụ. Tiêu đề sans-serif tròn, đậm, thân bài mềm nhưng rõ. Hero hai cột gồm lời giới thiệu, nút chính và ảnh rau/sản phẩm thật trong khung bo hữu cơ lớn. Tiếp theo là sản phẩm, nguồn gốc, cách giao và câu hỏi thường gặp nếu có. Dùng ảnh vườn hoặc nơi làm việc để củng cố câu chuyện. Không thay rau bằng ba hình tròn hay vân tre giả. Trên điện thoại chữ rồi ảnh; thẻ chỉ giữ hai cột nếu nội dung vẫn đọc thoải mái.

**Chi tiết cần giữ:** Giá tiền phải dùng chữ số đều bề ngang, không thì cột giá nhảy loạn khi số chữ số khác nhau. Đừng để nền be và chữ nâu xuống dưới ngưỡng đọc — đo lại nếu làm nhạt thêm.

**Lưu ý khi áp dụng:** Đừng dùng cho hàng công nghệ. Bảng màu đất khiến sản phẩm trông như đồ thủ công.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Design Style: Organic / Natural

## 1. Design Philosophy
This style embraces **wabi-sabi**—the acceptance of transience and imperfection. It rejects the cold precision of digital interfaces in favor of **warmth, softness, and natural connection**. It feels **tactile, grounded, and calming**.

### Visual DNA
*   **Core Signature**: Soft, amorphous blob shapes with varied organic border radii (using complex percentages like `60% 40% 30% 70% / 60% 30% 70% 40%`)
*   **Texture is Essential**: Global grain/noise texture overlay at 3-4% opacity with multiply blend mode creates paper-like quality
*   **Color Psychology**: Earth-drawn palette evokes forest floors, clay pottery, unbleached paper, dried grass, and river stones
*   **Shadow Philosophy**: Soft, diffused shadows with natural color tints (moss green, clay orange) instead of pure black
*   **Typography Emotion**: Fraunces serif brings old-world warmth with modern softness; Nunito's rounded terminals echo organic shapes

### Design Principles
*   **Vibe**: Peaceful, sustainable, handcrafted, authentic, rooted, welcoming, human
*   **Core Tenet**: "There are no straight lines in nature." Avoid sharp 90-degree angles. Everything should feel eroded by wind or water, or shaped by hand.
*   **Rhythm**: Generous whitespace creates breathing room. Staggered grids and varied border radii prevent mechanical uniformity.
*   **Interaction**: Gentle, natural motion—elements scale and lift on hover like picking up a river stone. No harsh snaps.
*   **Asymmetry**: Intentional imperfection through rotated images, offset elements, and varied card shapes creates organic authenticity
*   **Depth**: Multiple z-layers with blurred blobs, translucent overlays, and soft shadows create atmospheric depth without harsh contrast

## 2. Design Token System (The DNA)

### Colors (Single Palette - Light Mode)
A palette drawn from the forest floor, clay, and unbleached paper.
*   `background`: `#FDFCF8` (Off-white, Rice Paper)
*   `foreground`: `#2C2C24` (Deep Loam / Charcoal)
*   `primary`: `#5D7052` (Moss Green)
*   `primary-foreground`: `#F3F4F1` (Pale Mist)
*   `secondary`: `#C18C5D` (Terracotta / Clay)
*   `secondary-foreground`: `#FFFFFF` (White)
*   `accent`: `#E6DCCD` (Sand / Beige)
*   `accent-foreground`: `#4A4A40` (Bark)
*   `muted`: `#F0EBE5` (Stone)
*   `muted-foreground`: `#78786C` (Dried Grass)
*   `border`: `#DED8CF` (Raw Timber)
*   `destructive`: `#A85448` (Burnt Sienna)

### Typography
Combining a characterful serif with a clean, rounded sans-serif.
*   **Headings**: **'Fraunces'** (Google Font). A variable font with "soft" axes. It has a distinct, old-style warmth but feels modern. Use weights 600-800.
*   **Body**: **'Nunito'** or **'Quicksand'**. Rounded terminals are essential to match the organic shapes.
*   **Scale**: Moderate, not aggressive. 1.25 scale.

### Radius & Shapes
*   **Standard Radius**: `rounded-2xl` (16px) or `rounded-3xl` (24px).
*   **Organic Shapes**: Use custom classes or inline styles for specific elements to create blob shapes.
    *   Example: `border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;`
*   **Borders**: Soft, sometimes slightly imperfect (simulated via double borders or slightly transparent thick borders).

### Shadows & Effects
*   **Shadows**: Soft, diffused, colored shadows. Never pure black.
    *   `shadow-soft`: `0 4px 20px -2px rgba(93, 112, 82, 0.15)` (Moss tinted)
    *   `shadow-float`: `0 10px 40px -10px rgba(193, 140, 93, 0.2)` (Clay tinted)
*   **Textures**: **CRITICAL**. The background should have a subtle noise or paper grain overlay.
    *   Implementation: Use a fixed pseudo-element on the body or main container with a base64 noise pattern set to `mix-blend-mode: multiply` and very low opacity (3-5%).

## 3. Component Stylings

### Buttons
*   **Shape**: Fully rounded pills (`rounded-full`) for all variants
*   **Primary**: Moss Green (#5D7052) background with Pale Mist (#F3F4F1) text. Soft colored shadow: `shadow-[0_4px_20px_-2px_rgba(93,112,82,0.15)]`
*   **Outline**: 2px Terracotta (#C18C5D) border, transparent background, Terracotta text
*   **Ghost**: Transparent with Moss Green text, hover fills with Moss/10 background
*   **Interaction**: `hover:scale-105` with deepened shadow `hover:shadow-[0_6px_24px_-4px_rgba(93,112,82,0.25)]`. Active state: `active:scale-95` for tactile feedback
*   **Sizes**: Default h-12, sm h-10, lg h-14. Generous horizontal padding (px-8 to px-10)
*   **Typography**: Bold weight, base to lg sizing

### Cards / Containers
*   **Background**: Extremely light beige (#FEFEFA) over off-white page background
*   **Border**: Soft timber border (#DED8CF) at 50% opacity: `border-[#DED8CF]/50`
*   **Shape**: `rounded-[2rem]` base with asymmetric variations using custom values like `rounded-tl-[4rem]` on specific corners
*   **Shadows**: Moss-tinted soft shadow: `shadow-[0_4px_20px_-2px_rgba(93,112,82,0.15)]`
*   **Texture**: Fixed noise overlay layer at 3% opacity with multiply blend mode
*   **Interaction**: Feature cards lift with `hover:-translate-y-1` and shadow deepens to `hover:shadow-[0_20px_40px_-10px_rgba(93,112,82,0.15)]`

### Inputs
*   **Shape**: Pill-shaped with `rounded-full`
*   **Border**: Timber border (#DED8CF)
*   **Background**: `bg-white/50` (semi-transparent) revealing page grain texture beneath
*   **Focus State**: `focus-visible:ring-2 ring-[#5D7052]/30` with `ring-offset-2` for soft, natural glow (not sharp outline)
*   **Typography**: Sans-serif body font, text-sm
*   **Height**: h-12 for comfortable touch target

### Navigation
*   **Style**: Sticky floating pill (`sticky top-4`) with glassmorphism
*   **Background**: `bg-white/70` with `backdrop-blur-md` for frosted effect
*   **Border**: Soft timber border at 50% opacity with subtle shadow
*   **Shape**: `rounded-full`
*   **Logo**: Circular moss green container with white icon
*   **Mobile**: Full menu dropdown with organic rounded borders (`rounded-[2rem]`)

## 4. Layout & Spacing
*   **Container Widths**: Vary by section for visual rhythm
    *   Primary content: `max-w-7xl` (hero, features, blog, pricing)
    *   Focused content: `max-w-6xl` (how it works, FAQ)
    *   Intimate content: `max-w-5xl` (final CTA)
    *   Text-heavy sections: `max-w-4xl` (hero inner), `max-w-2xl` (product detail text)
*   **Section Padding**: Consistent `py-32` vertical spacing with `px-4 sm:px-6 lg:px-8` horizontal
*   **Grid Patterns**:
    *   Stats: `grid-cols-2 md:grid-cols-4`
    *   Features/Blog/Testimonials: `md:grid-cols-3` (or `md:grid-cols-2 lg:grid-cols-3`)
    *   Two-column layouts: `lg:grid-cols-2`
    *   Grid gaps: Consistent `gap-8` with optional `md:gap-12` for stats
*   **Whitespace Philosophy**: Use generous gaps (gap-8, gap-12, gap-16) to let design breathe. Space is a design element, not empty canvas.

## 5. Non-Genericness (The Bold Factors)
*   **Blob Backgrounds**: Large absolute-positioned blobs with `blur-3xl` create ambient color washes. Multiple shapes (via shapeIndex prop) with varied organic border radii. Used in Hero (2 blobs), Product Detail, Features, and Final CTA sections.
*   **Rotated Image Frames**: Product detail image rotated `-2deg` with thick 4px white border creates handcrafted photo feel
*   **Organic Image Masks**: Benefits section image uses complex blob border-radius: `rounded-[30%_70%_70%_30%_/_30%_30%_70%_70%]`
*   **Asymmetric Card Radii**: Feature cards cycle through 6 different border-radius patterns, mixing large corner curves (4rem, 5rem) with standard (2rem)
*   **Curved SVG Connectors**: How It Works uses hand-drawn looking curved dashed SVG path instead of straight lines
*   **Hover Micro-rotations**: Testimonial cards subtly rotate on hover (`hover:rotate-1`) mimicking picking up a physical card
*   **Varied Section Backgrounds**: Alternating between off-white, stone tint (#F0EBE5/30), sand (#E6DCCD/30), moss green (#5D7052), and terracotta (#C18C5D)
*   **Dual Texture Layers**: Global grain texture PLUS section-specific noise overlays and blob backgrounds create rich depth

## 6. Effects & Animation
*   **Transition Philosophy**: Natural, gentle motion. Use `transition-all duration-300` or `duration-500` for smooth changes
*   **Hover Animations**:
    *   Buttons: `hover:scale-105` with shadow increase
    *   Cards: `hover:-translate-y-1` (lift) or `hover:rotate-1` (subtle tilt)
    *   Stats: `group-hover:scale-110` on numbers
    *   Images: `hover:scale-105` with 700ms duration for slow reveal
    *   Icon containers: Background color fill transition
*   **Active States**: `active:scale-95` on buttons for tactile press feedback
*   **Entrance/Exit**: Details accordion uses native `open:` state with chevron rotation
*   **Image Overlays**: Fade overlays on hover (blog cards) using `group-hover:bg-transparent`
*   **No Harsh Snaps**: All transitions eased, duration 300-700ms range for organic feel

## 7. Icons (Lucide React)
*   **Style**: Default stroke width (2px)
*   **Color**: Moss Green (#5D7052) as default, white on dark backgrounds
*   **Containers**: Icons sit in `h-14 w-14` rounded-2xl containers with `bg-[#5D7052]/10` background
*   **Hover Effect**: Container fills completely to solid moss green while icon switches to white
*   **Sizing**: 28px (size={28}) for feature icons, 24px for benefit checkmarks, responsive sizing for navigation
*   **Usage**: Social icons in footer, feature icons, benefit checkmarks, navigation menu toggle, arrows in CTAs

## 8. Accessibility
*   **Contrast Ratios**:
    *   Primary text (#2C2C24) on background (#FDFCF8): 14.5:1 (AAA)
    *   Moss (#5D7052) on background: 6.2:1 (AA)
    *   Muted text (#78786C) on background: 4.8:1 (AA)
*   **Focus States**: `focus-visible:ring-2 ring-[#5D7052] ring-offset-2` provides clear, soft focus indicator
*   **Touch Targets**: All interactive elements meet 44px minimum (buttons h-12 = 48px)
*   **Semantic HTML**: Proper heading hierarchy, nav landmarks, alt text for images, aria-labels where needed
*   **Keyboard Navigation**: All interactive elements keyboard accessible, details/summary for FAQ accordion

## 9. Responsive Strategy
*   **Mobile-First Approach**: Base styles mobile-optimized, enhanced at breakpoints
*   **Breakpoint Usage**:
    *   `sm:` (640px): Horizontal padding increases, some flex-row layouts
    *   `md:` (768px): Major grid transitions (2-3 columns), nav reveals desktop version
    *   `lg:` (1024px): 3-column grids, 2-column hero/benefits layouts
*   **Typography Scaling**: Hero headline `text-5xl md:text-7xl`, sections `text-4xl md:text-5xl`
*   **Stack Behavior**: All grids collapse to single column on mobile, flex layouts switch to `flex-col`
*   **Navigation**: Mobile uses hamburger menu with slide-out panel, desktop inline nav
*   **Blob Simplification**: Blobs remain but overflow hidden on mobile to prevent layout issues

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH ORGANIC
Bố cục và nhận diện: Fraunces từ nguồn, cream #FDFCF8, moss #5D7052, terracotta #C18C5D. Không đối xứng hoàn hảo; ảnh mask hữu cơ nhưng nội dung có grid 8 px; max-width 1200, H1 64–76 px.

## 3. Nội dung mở đầu

**H1:** Một giỏ rau, vừa bữa nhà mình.

**Lời dẫn:** Chọn số người và số bữa để xem một giỏ sản phẩm minh họa phù hợp.

**Hành động chính:** Tạo giỏ của bạn

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Giỏ tuần này

**Bố cục và hành vi:** Ảnh giỏ rau là vật thể chính, bên cạnh lời hứa phạm vi rõ.

**Nội dung và đầu ra:** Tên từng loại trong ảnh phải khớp dataset; không thêm hàng chục sản phẩm trang trí.

### 2. Cỡ giỏ

**Bố cục và hành vi:** Chọn 2/4 người và 3/5 bữa; tóm tắt số lượng đổi ngay.

**Nội dung và đầu ra:** Các giá trị là dữ liệu ví dụ, không lời khuyên dinh dưỡng.

### 3. Bên trong giỏ

**Bố cục và hành vi:** Danh sách sản phẩm với ảnh nhỏ, đơn vị và lượng; cho thay một món trong giới hạn mẫu.

**Nội dung và đầu ra:** Cải xanh, cà chua, bí, nấm; nếu đổi món phải cập nhật tổng tương ứng.

### 4. Câu chuyện nguồn gốc

**Bố cục và hành vi:** Ảnh vườn và thùng đóng gói cùng bối cảnh, đoạn mô tả ngắn.

**Nội dung và đầu ra:** Ghi thương hiệu/vườn minh họa, không tem hữu cơ hoặc chứng nhận giả.

### 5. Tóm tắt lựa chọn

**Bố cục và hành vi:** Hiện cỡ giỏ, thành phần, tổng giá mẫu và ghi chú nhận hàng.

**Nội dung và đầu ra:** Cho sửa từng phần; nút cuối Xem giỏ mẫu, không tạo đơn.

## 5. Dữ liệu và trạng thái tương tác

basketSize/meals/substitutions quyết định lineItems; totals tính từ lineItems. Reset trả giỏ mặc định; không còn món thay thì nêu lý do.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

Tablet 2 cột sản phẩm; mobile 1 cột tóm tắt và 2 cột món nhỏ; ảnh mask không cắt sản phẩm. Gutter 20 px, H1 44 px, body 18 px. Panel tóm tắt không sticky che CTA.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Thay giỏ crossfade 200 ms, không animate chiều cao liên tục. Blob trang trí tĩnh trên mobile; reduced-motion không crossfade.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Ảnh AI rau theo đúng từng giỏ; nhất quán số lượng hiển thị và dữ liệu mẫu.

**Cover:** Giỏ rõ, một nhãn số bữa và mảng moss/đất; tấm cover không thêm dấu chứng nhận để tạo niềm tin giả.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Mọi tổng giá bằng tổng các món.
2. Thay cỡ giỏ không để số lượng cũ.
3. Ảnh và tên sản phẩm khớp nhau.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
