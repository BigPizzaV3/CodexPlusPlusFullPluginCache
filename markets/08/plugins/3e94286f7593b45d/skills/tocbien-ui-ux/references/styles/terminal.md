# Terminal (`terminal`)

Nền đen, chữ đơn cách xanh lá, khung dòng lệnh

- Hợp với: Hợp khi đang dùng AI để dựng website cho công cụ kỹ thuật cần cho người xem hiểu lỗi, trạng thái và đầu ra.
- Ngành minh hoạ: Công cụ kỹ thuật, quản trị, kho vận
- Trang minh hoạ làm việc gì: Trình kiểm tra luồng dữ liệu có log lỗi, sửa và chạy lại
- Thang (1–10): biến tấu bố cục 6 · chuyển động 2 · mật độ 6
- Xem mẫu: https://tocbien.cloud/phong-cach/terminal/

## Đặc tả

Terminal: nền đen xanh #0a0e0a, chữ sáng và xanh lá dịu. Dùng font đơn cách có tiếng Việt, đường kẻ mảnh và nhãn gợi cửa sổ dòng lệnh. Phần mô tả, các bước và trạng thái trình bày có nhịp như phiên làm việc, nhưng ngôn ngữ vẫn dễ hiểu. Trạng thái có cả chữ và dấu hiệu, không chỉ chấm màu. Phần ví dụ phải được ghi là minh họa nếu không chạy thật; không giả vờ đang xử lý dữ liệu của khách. Điện thoại giữ cỡ chữ đọc được; bảng chuyển cách trình bày hoặc cuộn trong vùng riêng, không thu nhỏ toàn trang.

**Chi tiết cần giữ:** Font đơn cách phải có bộ dấu tiếng Việt, nhiều font kiểu này thiếu và làm chữ vỡ. Xanh lá trên nền đen dễ chói, dùng sắc dịu và chỉ cho chữ quan trọng.

**Lưu ý khi áp dụng:** Chỉ dùng khi khách hiểu nghề. Người không rành kỹ thuật nhìn màn hình đen là đóng tab ngay.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Design Philosophy
The **Terminal CLI** aesthetic pays homage to the raw power of the command line. It strips away the "user interface" layers to reveal the "system" underneath. It is **brutally functional, high-contrast, and authentically retro**. It feels like hacking into a mainframe or configuring a server.

The vibe is **Cyber-Industrial, Hacker, and System-Level**. It is not "Matrix" rain (too cliché); it is a clean, usable ZSH/BASH shell environment.

**Key visual signatures:**
*   **Monospace Supremacy**: Every single character, from the largest headline to the smallest footer link, is monospaced.
*   **The Cursor**: The blinking block or underscore cursor `_` is the heartbeat of the interface.
*   **Shell Metaphors**: Use prompt characters (`>`, `$`, `~`), command flags (`--help`), and status codes (`[OK]`, `[ERR]`).
*   **Scanlines (Subtle)**: A very faint CRT scanline effect to give it depth without ruining readability.

# Design Token System

## Colors (Dark Mode Only)
The palette mimics a phosphor monitor. High contrast is non-negotiable.

*   **Background**: `#0a0a0a` (Deep black, but not pure OLED black to allow for scanlines)
*   **Foreground**: `#33ff00` (Classic Terminal Green) or `#ffb000` (Amber) - *Let's go with Green for this implementation as the primary, with Amber as secondary.*
    *   `primary`: `#33ff00` (Bright Neon Green)
    *   `secondary`: `#ffb000` (Amber/Orange for warnings or accents)
    *   `muted`: `#1f521f` (Dimmed green for borders/inactive text)
    *   `accent`: `#33ff00` (Same as primary, used for cursors/active states)
    *   `error`: `#ff3333` (Bright Red)
    *   `border`: `#1f521f` (Dimmed green)

## Typography
*   **Font**: `JetBrains Mono`, `Fira Code`, or `VT323`.
*   **Style**: **ALL CAPS** for headers. Lowercase for "code" or body text is acceptable, but consistency is key.
*   **Scale**: Strict modular scale. Headers shouldn't be "smooth"; they should snap to grid sizes.

## Radius & Borders
*   **Radius**: `0px`. Absolutely no rounded corners.
*   **Borders**: `1px` solid or dashed. Borders are crucial for defining "windows" or "panes".

## Shadows & Effects
*   **Shadows**: No drop shadows.
*   **Text Shadow**: A subtle "glow" for the primary text to mimic phosphor persistence.
    *   `text-shadow: 0 0 5px rgba(51, 255, 0, 0.5)`
*   **CRT Overlay**: A pointer-events-none overlay with scanlines.

# Component Stylings

## Buttons
*   **Structure**: Text enclosed in brackets `[ INITIATE ]` or a solid block of color with inverted text.
*   **Hover**: The background fills with the primary color, text becomes black (inverted video).
*   **Active**: A "pressed" state might shift the text 1px down or blink rapidly.

## Cards (Windows/Panes)
*   **Structure**: A black box with a 1px green border.
*   **Header**: A "title bar" at the top: `+--- SYSTEM STATUS ---+` or a solid inverted bar.
*   **Content**: Padded monospaced text inside.

## Inputs
*   **Style**: No box. Just a prompt `user@acme:~$` followed by the input field.
*   **Cursor**: A blinking block `█` at the caret position.
*   **Focus**: No ring, just the blinking cursor.

# Layout Strategy
The layout should feel like a grid of terminal windows (`tmux` or `vim` splits).
*   **Strict Grid**: Content is aligned to a rigid character grid.
*   **Separators**: Use ASCII characters for dividers: `----------------` or `================` or `//`.

# Non-Genericness (The Bold Factor)
*   **ASCII Art**: Use ASCII art for the logo or key graphic elements.
*   **Typewriter Effect**: Headlines should appear character-by-character.
*   **Raw Data Visualization**: Stats shouldn't be pie charts; they should be progress bars `[||||||||||.....]`.

# Effects & Animation
*   **Blink**: Utilities for `animate-blink` (standard cursor blinking).
*   **Glitch**: Occasional subtle text offsets on hover.
*   **Typing**: `typing-demo` animation for the hero text.

# Iconography
*   **Lucide Icons**: Use them, but style them to look pixelated or low-fi if possible, or strict `stroke-width-2`.
*   **Color**: Icons are always the primary terminal color.

# Responsive Strategy
*   **Mobile**: The "windows" stack vertically. The text size remains legible (monospaced fonts can be wide, so watch for overflow). Wrap long lines with a `\` indicator.

# Accessibility
*   **Contrast**: The bright green on black exceeds AA requirements.
*   **Focus**: High visibility is inherent to this style (inverted colors).

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH TERMINAL
Bố cục và nhận diện: Mono toàn bộ; nền #0a0a0a, green #33ff00, amber #ffb000, error #ff3333; radius 0, border 1 px, không drop shadow. Grid như tmux; header 40–56 px theo nhịp ký tự.

## 3. Nội dung mở đầu

**H1:** > kiểm_tra_luồng

**Lời dẫn:** Chạy thử quy trình nhận yêu cầu, kiểm dữ liệu và lập báo cáo trong một terminal minh họa.

**Hành động chính:** Chạy workflow mẫu

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Lệnh mở đầu

**Bố cục và hành vi:** Một prompt và câu giải thích, nút [ CHẠY MẪU ] rõ.

**Nội dung và đầu ra:** Không shell thật; gọi thẳng đây là mô phỏng kiểm dữ liệu workflow.

### 2. Dữ liệu đầu vào

**Bố cục và hành vi:** Pane trái có hai dataset Đủ thông tin/Thiếu email; pane phải là schema.

**Nội dung và đầu ra:** Ba bản ghi với tên giả, email example.com; không credential/token.

### 3. Log thực thi

**Bố cục và hành vi:** Ba bước Nhận dữ liệu/Kiểm trường/Tạo báo cáo, mỗi dòng có [OK] hoặc [ERR].

**Nội dung và đầu ra:** Thiếu email ở bản ghi 2 phải dừng bước tạo báo cáo và nêu đường sửa.

### 4. Sửa và chạy lại

**Bố cục và hành vi:** Ô sửa email được liên kết từ dòng lỗi; chạy lại chỉ sau validation.

**Nội dung và đầu ra:** Lệnh gợi ý là nhãn mô phỏng, không thực thi mã người dùng.

### 5. Báo cáo

**Bố cục và hành vi:** Khung kết quả số hợp lệ/số lỗi, nút sao chép báo cáo local và reset.

**Nội dung và đầu ra:** Nếu clipboard bị từ chối, hiện văn bản để chọn thủ công.

## 5. Dữ liệu và trạng thái tương tác

idle/running/error/success; trong running khóa chạy trùng, log từ dataset thật, cancel dừng timer và không cập nhật sau reset. Báo lỗi gồm bản ghi, trường thiếu, cách sửa.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

Dưới 768 px panes xếp dọc; dòng log wrap có chỉ báo tiếp dòng, không cho ASCII tràn document; nút thao tác bằng ngôn ngữ rõ bên cạnh lệnh.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Cursor 1 s steps; hiệu ứng typing chỉ phần trang trí, aria không đọc lại từng chữ. Log hiện theo bước tối đa 1.2 s để minh họa, reduced-motion hiện kết quả tức thì.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Không cần ảnh stock; dataset, log và sơ đồ phải cùng một kịch bản thực thi local.

**Cover:** Một pane log 5–7 dòng, prompt lớn, [ERR] amber/red và [OK] green; không hàng trăm dòng nhỏ.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Dataset thiếu email luôn báo đúng bản ghi 2.
2. Sửa email rồi chạy thành công với tổng đúng.
3. Cancel/reset không để log cũ tiếp tục xuất hiện.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
