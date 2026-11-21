# Dark tech (`dark-tech`)

Nền tối, một màu neon

- Hợp với: Hợp khi đang dùng AI để dựng website cho AI, API và tự động hóa cần cho thấy cách kiểm dữ liệu thay vì chỉ trang trí neon.
- Ngành minh hoạ: Công cụ, phần mềm
- Trang minh hoạ làm việc gì: Bàn rà hóa đơn mẫu từ tài liệu nguồn sang dữ liệu có kiểu
- Thang (1–10): biến tấu bố cục 8 · chuyển động 7 · mật độ 3
- Xem mẫu: https://tocbien.cloud/phong-cach/dark-tech/

## Đặc tả

Dark Tech: nền xanh đen #0b0e14, bề mặt #111621, mực sáng, xanh lam #4c9aff làm điểm nhấn. Sans-serif cho lời giới thiệu; monospace cho đoạn mã, ví dụ và nhãn kỹ thuật. Hero tập trung công việc và kết quả, có ví dụ đầu vào/đầu ra hoặc giao diện sản phẩm thực tế. Các mục khả năng, cách dùng và giới hạn rõ ràng; không dùng neon dày hoặc giả số liệu hoạt động. Viền nhẹ, bóng tiết chế, chuyển động ít. Điện thoại cho mã cuộn trong khung riêng, toàn trang không tràn.

**Chi tiết cần giữ:** Chuyển động phải có lý do, đừng cho mọi khối cùng hiện dần. Tôn trọng prefers-reduced-motion.

**Lưu ý khi áp dụng:** Một màu nhấn thôi. Thêm màu neon thứ hai là trang lập tức trông rẻ tiền.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: dark-tech

Biến thể: Technical Review Workspace / dữ liệu trên bề mặt tối. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #0B1018 |
| surface | #121B27 |
| surface-raised | #192534 |
| foreground | #E7EDF5 |
| muted | #9CACBF |
| accent | #65D8E8 |
| on-accent | #0B1018 |
| border | #223044 |
| focus | #93E5EF |
| warning | #F5C469 |
| error | #FF9EA8 |

## Typography

IBM Plex Sans 400/500/600 cho chữ; IBM Plex Mono 400/500 cho dữ liệu. H1 desktop 60 px/1.1 và mobile 36 px/1.2; H2 28 px; body 16 px/1.55; bảng 14–16 px theo mật độ và kiểm đọc; label 12–14 px chỉ metadata ngắn. Giá trị tiền dùng tabular-nums.

## Lưới, nhịp và responsive

Desktop 12 cột, chứng từ5 và dữ liệu 7, max-width 1360 px, gutter 32 px, gap 24 px. Từ768 px dùng tabs Tài liệu/Dữ liệu khi hai panel không đủ rộng; không scale screenshot. Log/JSON overflow riêng có nhãn và nút copy.

## Bề mặt và vật liệu

Radius 6 px, viền 1 px, shadow 0 8 px24 px rgba(0,0,0,.18) chỉ ở panel nổi; không glass. Vùng chọn border accent với opacity fill.08. Pattern lưới nền nếu có ở opacity.03, không phủ trên bảng.

## Thành phần và trạng thái

### Dòng dữ liệu

Tên trường, giá trị, trạng thái và control sửa. Label Cần kiểm/Đã xác nhận bằng chữ; không dùng chấm màu đơn lẻ. Click row và nút sửa phải có hành vi phân biệt.

### Vùng chứng từ

Có highlight theo tọa độ chuẩn hóa 0..1 của ảnh. Khi resize không dịch khỏi vùng cần chỉ; alt/description cung cấp nội dung cho người không thấy ảnh.

### Input sửa

Chỉnh inline có Lưu/Hủy; hủy trả giá trị cũ. Validation theo trường, không cho tổng tiền thành NaN.

### Bản xuất

Hiển thị JSON/CSV thật từ state hiện tại. Copy có success/failure; CSV escape dấu phẩy/dấu ngoặc kép/xuống dòng, không dùng tên Excel cho dữ liệu CSV.

## Chuyển động và phương án giảm chuyển động

Highlight vùng 180 ms và row state 200 ms; tắt motion vẫn thấy liên hệ qua mã trường. Không giả thời gian xử lý OCR, không chạy chữ code nền.

## Những điều tránh

Cấm score tin cậy bịa, dữ liệu khách thật, upload giả đã xử lý, cyberpunk glitch, coin/orbital, dashboardKPI trang trí hoặc gọi mapping tĩnh là AI suy luận trực tiếp.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH DARK-TECH
Bố cục và nhận diện: Brief Dark Tech mới: #0B1018 nền, #121B27 surface, #223044 border, #E7EDF5 chữ, #9CACBF secondary, cyan #65D8E8 accent, amber #F5C469 cảnh báo. IBM Plex Sans/Mono, H1 52–68 px, radius 6 px, grid chặt. Độ sâu bằng viền/surface, không sci-fi trang trí.

## 3. Nội dung mở đầu

**H1:** Từ chứng từ tới dữ liệu có thể kiểm tra.

**Lời dẫn:** Xem một tài liệu mẫu, rà lại các trường trích xuất và sửa phần cần xác nhận.

**Hành động chính:** Thử một chứng từ mẫu

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Đầu vào và đầu ra

**Bố cục và hành vi:** Một chứng từ hư cấu trái, bảng trường phải, đường liên hệ giữa vùng tài liệu và trường.

**Nội dung và đầu ra:** Nêu mô phỏng với dữ liệu dựng sẵn, không hứa OCR trực tiếp.

### 2. Chọn tài liệu mẫu

**Bố cục và hành vi:** Ba mẫu Hóa đơn/Phiếu giao/Biên nhận có thông tin hư cấu đồng bộ.

**Nội dung và đầu ra:** Không nhận upload tài liệu thật trong bản static.

### 3. Kiểm trường

**Bố cục và hành vi:** Các dòng ngày/số phiếu/tổng tiền có trạng thái Cần kiểm/Đã xác nhận.

**Nội dung và đầu ra:** Một dòng intentionally khác dữ liệu trên ảnh để người xem sửa có mục đích.

### 4. Rà soát

**Bố cục và hành vi:** Chọn dòng làm nổi vùng tương ứng trên chứng từ; sửa giá trị rồi đánh dấu kiểm.

**Nội dung và đầu ra:** Không score AI tự bịa như 98.6%; dùng trạng thái kiểm chứng được.

### 5. Bản xuất mẫu

**Bố cục và hành vi:** Hiện JSON/CSV tương ứng với giá trị đã sửa; nút copy và reset.

**Nội dung và đầu ra:** Không gửi sang kế toán hoặc workflow thật.

## 5. Dữ liệu và trạng thái tương tác

documentId, fields, reviewed; đổi document có dữ liệu chưa xem lưu riêng hoặc cảnh báo rõ. Copy JSON đúng kiểu, tiền không mất định dạng số trong dữ liệu. Reset cả highlight lẫn fields.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

768 px hai panel có thể tabs,390 px Tài liệu/Dữ liệu chuyển bằng nút giữ row đang chọn; code cuộn trong panel, không tràn body.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Highlight 180 ms, dòng sửa 200 ms; không typing toàn bộ JSON hoặc nền neon bay.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Chứng từ hư cấu tự dựng và dữ liệu đối chiếu; không giả cam kết OCR/chính sách bảo mật thật.

**Cover:** Một trường đang kiểm, chứng từ và dòng dữ liệu đủ lớn; điểm cyan gắn thao tác, không vòng tròn phát sáng vô chức năng.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Sửa tổng tiền cập nhật bản xuất đúng.
2. Highlight trỏ đúng vùng tài liệu.
3. Khi thao tác sao chép bị chặn phải có vùng văn bản dự phòng và không báo đã chép.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
