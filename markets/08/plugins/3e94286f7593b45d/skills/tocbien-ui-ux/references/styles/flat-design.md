# Flat Design (`flat-design`)

Màu phẳng tươi, bo góc vừa, không đổ bóng

- Hợp với: Hợp khi đang dùng AI để dựng website cho dịch vụ địa phương cần ít bước, màu rõ và dùng tốt trên điện thoại.
- Ngành minh hoạ: Cửa hàng, bán hàng online, sản phẩm
- Trang minh hoạ làm việc gì: Luồng chọn đồ, số lượng và giờ lấy cho tiệm giặt
- Thang (1–10): biến tấu bố cục 4 · chuyển động 2 · mật độ 5
- Xem mẫu: https://tocbien.cloud/phong-cach/flat-design/

## Đặc tả

Flat Design: nền trắng hoặc xám lạnh rất nhạt, chữ xanh đen, xanh dương làm màu hành động và cam làm điểm phụ. Mảng màu đặc, không chuyển sắc, không bóng nổi. Sans-serif rõ ràng; bo góc 8–14px nhất quán. Hero ghép thông điệp ngắn với minh họa phẳng liên quan dịch vụ; ảnh cửa tiệm thật dùng ở phần giới thiệu. Các mục dịch vụ, bảng phí, cách sử dụng và liên hệ tách bằng khoảng cách. Không biến mọi ảnh sản phẩm thành ô màu. Điện thoại xếp dọc; chỉ dùng hai cột cho mục ngắn đủ rộng.

**Chi tiết cần giữ:** Bảng màu phẳng chỉ được có bốn màu, dùng lặp lại chứ đừng thêm màu thứ năm. Chữ trên nền màu đậm phải đo tương phản, cam nhạt với chữ trắng rất dễ tụt dưới ngưỡng đọc.

**Lưu ý khi áp dụng:** Đừng dùng khi muốn cảm giác cao cấp. Màu phẳng đọc ra là tiện và rẻ, không phải sang.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Design Philosophy
**Flat Design** removes all artifice. It rejects the illusion of three-dimensionality—no drop shadows, no bevels, no realistic gradients, no textures. It relies entirely on **hierarchy through size, color, and typography**. This is not minimalism for the sake of being minimal; it's **confident reduction** that creates visual interest through pure form.

The aesthetic is **digital-native but print-inspired**: crisp edges, solid blocks of color, and a strict reliance on the grid. It communicates clarity, efficiency, and modernity. It is not "boring" or "plain"; it is **boldly reductive and graphic**. Every element exists because it is necessary. Visual interest comes from the strategic interplay of solid shapes, vibrant (but controlled) color palettes, and dynamic scale.

**Core Principles:**
1.  **Zero Artificial Depth**: The Z-axis does not exist. Everything is on the same plane. However, visual hierarchy is created through scale, color contrast, and strategic layering of flat shapes.
2.  **Color as Structure**: Bold background colors define sections and grouping, not lines or shadows. Color transitions are sharp, never blurred or gradual.
3.  **Typography as Interface**: Text size and weight bear the load of hierarchy. Typography is geometric, bold, and demands attention.
4.  **Geometric Purity**: Rectangles, circles, and squares dominate. Rounded corners are consistent and moderate. No organic blobs or complex shapes.
5.  **Interactive Feedback**: Hover states are pronounced through color shifts, scale transformations, and instant transitions—never through shadow depth.
6.  **Strategic Decoration**: Large, subtle geometric shapes in background create visual interest without breaking the flat aesthetic—think poster design.

# Design Token System

## Colors (Single Palette: Light Mode)
A vibrant, confident palette that avoids muddy tones. High contrast is essential.

-   **Background**: `#FFFFFF` (Pure White) - The canvas.
-   **Foreground**: `#111827` (Gray 900) - Sharp, high-contrast text.
-   **Primary**: `#3B82F6` (Blue 500) - The "Action" color. Bright, standard digital blue.
-   **Secondary**: `#10B981` (Emerald 500) - Supporting accent.
-   **Accent**: `#F59E0B` (Amber 500) - For highlights/badges.
-   **Muted**: `#F3F4F6` (Gray 100) - Used for secondary backgrounds/blocks.
-   **Border**: `#E5E7EB` (Gray 200) - Used sparingly.

## Typography
**Font Family**: **'Outfit', sans-serif**.
A geometric sans-serif that mirrors the shapes of the UI.
-   **Headings**: Bold (700) or Extra Bold (800). Tight letter-spacing (`-0.02em`).
-   **Body**: Regular (400). Readable, standard spacing.
-   **Labels/Buttons**: Medium (500) or SemiBold (600). Uppercase often used for labels (`tracking-wider`).

## Radius & Shapes
-   **Radius**: `rounded-md` (6px) or `rounded-lg` (8px). Consistent throughout. Not fully rounded (pill) unless it's a tag.
-   **Borders**: generally `0px`. We use background colors to define edges. If a border is needed (e.g., inputs), `border-2` solid color.

## Shadows & Effects
-   **Shadows**: `shadow-none`. **ABSOLUTELY NO BOX SHADOWS ON ELEMENTS.**
-   **Gradients**: Only subtle directional gradients for background decoration (e.g., `from-[#F3F4F6] to-transparent`). Never on buttons or cards. Never colorful or vibrant gradients.
-   **Blur**: None on elements. No backdrop-blur effects.
-   **Background Decoration**: Large geometric shapes with low opacity (`bg-white/5`) positioned absolutely for visual interest.

# Component Stylings

## Buttons
-   **Primary**: Solid Primary color background. White text. `rounded-md`. Height `h-14` to `h-16` for good touch targets. `transition-all duration-200 hover:scale-105` (scale transformation for feedback). Color shift on hover (e.g., `hover:bg-blue-600`). No shadow.
-   **Secondary**: Solid Muted background (Gray 100). Dark text. `hover:bg-gray-200` with scale effect.
-   **Outline**: `border-4` solid color (not border-2 for more boldness). Text matches border color. Transparent bg. `hover:bg-[color] hover:text-white` (fill effect on hover).

## Cards
-   **Style**: "Color Block".
-   **Appearance**: Solid background color (White on Gray page, or soft color tints like `bg-blue-50`, `bg-green-50` for features). No shadow. No border. Padding is generous (`p-6` or `p-8`). Rounded corners `rounded-lg`.
-   **Interaction**: `group cursor-pointer transition-all duration-200 hover:scale-[1.02]` (subtle scale). For colored backgrounds, add `hover:bg-[color]-100` for intensification. Icons within cards can have `group-hover:scale-110`.

## Inputs
-   **Normal**: Gray 100 background (`bg-gray-100`). No border. Text Gray 900. `rounded-md`.
-   **Focus**: White background. `border-2` solid Primary. No focus ring glow, just the hard border.

## Section Stylings
-   **Alternating Backgrounds**: Use White vs. Gray 100 (`#F3F4F6`) vs. Bold accent colors (Primary Blue, Emerald, Amber) to distinguish page sections. Sharp color transitions between sections.
-   **Dividers**: No thin line dividers between sections. Use whitespace or color blocks. Exception: FAQ uses thick `border-2` between items for structure.
-   **Background Decoration**: Use `absolute` positioned geometric shapes with low opacity or subtle gradients for visual interest. Examples: large circles (`rounded-full`), rotated squares, gradient overlays (`from-[color] to-transparent`).

# Iconography
-   **Library**: `lucide-react`.
-   **Style**: Standard to bold stroke (2px to 2.5px for emphasis).
-   **Treatment**: Often placed inside a solid colored circle (white circle with colored icon like `bg-white text-blue-600`). Circle size `h-14 w-14` or `h-16 w-16`.
-   **Animation**: `transition-transform duration-200 group-hover:scale-110` for icons within cards. Simple color intensity shifts on hover.

# Layout & Spacing
-   **Container**: `max-w-7xl`.
-   **Grid**: Rigid. 12-column base. Elements align perfectly.
-   **Spacing**: Comfortable but structured. Multiples of 4 (Tailwind default).
-   **Density**: Medium. Not too airy, not too dense. "Functional".

# Motion
-   **Vibe**: "Digital", "Snappy", "Direct".
-   **Transitions**: `transition-all duration-200` for most interactions. `duration-300` for larger transformations.
-   **Hover**: Immediate visual feedback through:
     - Scale transformations (`hover:scale-105` for buttons, `hover:scale-[1.02]` for cards)
     - Color shifts (darkening or lightening)
     - Color fills (outline buttons filling with color)
     - Icon scaling within cards (`group-hover:scale-110`)

# Accessibility
-   **Focus Rings**: Since we have no shadows, focus states must use high-contrast `ring-2 ring-offset-2 ring-blue-500` or similar solid outlines.
-   **Contrast**: Text on colored backgrounds must pass WCAG AA (e.g., White text on Blue 500 is okay, but check carefully with lighter accents).

# Non-Genericness / "The Bold Factor"
-   **Avoid**: "Material Design" floating cards, generic Bootstrap layouts, subtle pastels everywhere.
-   **Emphasize**: The "Poster" look. Treat every section like a flat graphic poster with bold color blocking.
-   **Bold Choices Implemented**:
     - **Large decorative geometric shapes** in hero background (circles, rotated squares with low opacity)
     - **Vibrant full-section color blocks** (Blue hero, Emerald benefits, Amber CTA, Dark gray How It Works & Footer)
     - **Dramatic scale effects** on pricing cards (popular tier starts larger and scales more)
     - **Multi-color stat numbers** (each stat uses a different accent color)
     - **Abstract geometric compositions** (overlapping shapes in hero illustration and benefits section)
     - **Pronounced hover states** (scale, color intensification, fills)
     - **Bold typography** with tight leading and strong weight contrast
     - **Thick borders** (border-4 on outline buttons, border-2 on FAQ items)
-   **Visual Interest Without Depth**: Achieved through color contrast, geometric layering, and scale—never shadows or gradients.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH FLAT-DESIGN
Bố cục và nhận diện: Outfit, trắng #FFFFFF, blue #3B82F6, emerald #10B981, amber #F59E0B. Các mảng phẳng phân nội dung, icon đơn giản, không shadow hoặc giả 3D trên điều khiển.

## 3. Nội dung mở đầu

**H1:** Giặt gọn, chọn giờ dễ.

**Lời dẫn:** Chọn loại đồ, số lượng và thời gian lấy trong một lượt thử đơn giản.

**Hành động chính:** Thử đặt lịch lấy đồ

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Bắt đầu với loại đồ

**Bố cục và hành vi:** Headline 56–72 px, minh họa phẳng giỏ đồ; CTA Chọn loại đồ.

**Nội dung và đầu ra:** Không đẩy bảng giá/phần thương hiệu dài trước tác vụ.

### 2. Chọn đồ

**Bố cục và hành vi:** Áo quần/Chăn/Đồ delicate với đơn vị từng loại rõ ràng.

**Nội dung và đầu ra:** Tăng giảm số lượng bằng nút và nhập số, số 0 hợp lệ ở mục không chọn.

### 3. Chọn giờ

**Bố cục và hành vi:** Các slo ts theo ngày mẫu và khoảng giờ; không địa chỉ thật.

**Nội dung và đầu ra:** Nhãn khả dụng/hết lượt không dựa vào màu đơn thuần.

### 4. Tóm tắt

**Bố cục và hành vi:** Bảng gọn loại đồ/số lượng/đơn vị; cho sửa từng bước.

**Nội dung và đầu ra:** Hiển thị phí mẫu nếu dùng, không coi là giá Tốc Biến.

### 5. Kết thúc thử

**Bố cục và hành vi:** Trang kết quả ở trong flow, đề nghị đặt lại.

**Nội dung và đầu ra:** Ghi Chưa đặt lịch lấy đồ, không to ast sai đã đặt thành công.

## 5. Dữ liệu và trạng thái tương tác

step 1→2→review; chỉ đi tiếp khi có ít nhất một món; back giữ data; bỏ slot khi đổi ngày; reset xóa toàn bộ.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

390 px một cột, phần tóm tắt nằm sau form; nút quay lại không ẩn; input số không tràn. Không nhồi 3 ô loại đồ vào 1 hàng.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Mảng trạng thái đổi màu 160 ms; không liftcard, không bóng hoạt hình.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Bộ minh họa đồ giặt phẳng nguyên bản; không giả lập sản phẩm bằng emoji.

**Cover:** Mảng xanh/white rõ, giỏ đồ vector và hai lựa chọn; không thêm gloss để bắt mắt.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Không qua bước 2 khi mọi số lượng 0.
2. Quay lại bước 1 giữ giờ nếu không đổi ngày.
3. State rõ khi mô phỏng mù màu.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
