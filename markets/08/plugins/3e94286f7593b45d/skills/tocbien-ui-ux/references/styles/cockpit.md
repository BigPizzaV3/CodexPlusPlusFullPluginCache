# Bảng điều khiển (`cockpit`)

Bảng dày, xem được nhiều dòng

- Hợp với: Hợp khi đang dùng AI để dựng website cho trang quản trị nội bộ cần xem nhiều dòng, tìm lỗi và xử lý cả ngày.
- Ngành minh hoạ: Kho vận, quản trị nội bộ
- Trang minh hoạ làm việc gì: Bảng vận hành workflow với KPI, lỗi, chạy lại và xuất CSV
- Thang (1–10): biến tấu bố cục 4 · chuyển động 3 · mật độ 8
- Xem mẫu: https://tocbien.cloud/phong-cach/cockpit/

## Đặc tả

Bảng điều khiển: nền xanh đen #0d1117, bề mặt #141b24, mực sáng, viền mảnh và xanh lam cho hành động. Thanh điều hướng bên trái, vùng làm việc gồm bộ lọc, tìm kiếm và bảng có thứ bậc rõ. Mật độ gọn nhưng đọc được, cột số căn phải và dùng tabular-nums. Trạng thái dùng chữ kèm màu; thao tác từng dòng dễ tìm, có trạng thái tải/trống/lỗi. Không áp bố cục hero quảng cáo vào màn quản trị. Mobile thu điều hướng thành menu và chuyển hàng thành thẻ giữ đủ trường, hoặc cho bảng cần so sánh cuộn riêng.

**Chi tiết cần giữ:** Hiện rõ trạng thái: hover, focus nhìn thấy được, viền khác nhau theo vai trò. Kiểm tương phản ở cỡ chữ nhỏ và vùng bấm đủ lớn.

**Lưu ý khi áp dụng:** Ưu tiên thứ bậc, mật độ và tốc độ đọc. Số liệu phải dóng cột bằng chữ số đều nhau.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: cockpit

Biến thể: Operational Cockpit / điều hành lượt chạy mẫu. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #101720 |
| surface | #182330 |
| surface-raised | #203041 |
| foreground | #EDF3F7 |
| muted | #A6B7C5 |
| accent | #69D4E4 |
| on-accent | #101720 |
| border | #2B3A49 |
| focus | #A6EAF2 |
| warning | #F3C56A |
| error | #EE8A91 |
| success | #92D7B5 |

## Typography

IBM Plex Sans 400/500/600, IBM Plex Mono cho log và số. H1 32 px/1.25, H2 22 px, KPI 36 px tabular, body 16 px, table 14–16 px theo cỡ màn, metadata 14 px. Không hero 96 px làm chậm truy cập dữ liệu.

## Lưới, nhịp và responsive

Sidebar 220 px, vùng chính minmax(0,1fr), max-width không ép dashboard như landing. Header controls theo 1hàng khi đủ rộng; ưu tiên cảnh báo trước chart. Tablet sidebar thu gọn có nhãn truy cập; mobile agenda/list thay bảng bị bóp.

## Bề mặt và vật liệu

Radius 6 px, border 1 px, không shadow mọi panel. Dùng surface 2 để phân level; alert có icon/text không chỉ màu. Separator rõ nhưng không viền mọi ô.

## Thành phần và trạng thái

### KPI

Tính từ dataset hợp lệ theo khung thời gian, nhãn phạm vi dữ liệu rõ. Không sparkline nếu không có chuỗi dữ liệu đi kèm.

### Toolbar bảng

Search, lọc trạng thái, timefilter và reset; bộ lọc có label, số kết quả cập nhật. Không filter ẩn trong icon không tên.

### Run detail

Timeline bước, input mẫu, lỗi và hướng sửa. Retry chỉ mô phỏng, tạo record mới liên kết parentId; giữ record lỗi cũ.

### Xuất báo cáo

CSV theo bộ lọc đang xem, header có đơn vị, escape chuẩn; trường bắt đầu=,+,-,@cần xử lý an toàn khi bảng tính mở file. Không xuất secret.

## Chuyển động và phương án giảm chuyển động

Cập nhật trạng thái 150 ms, không count-up giả các KPI. Loading chỉ khi thực sự có asynctask, skeleton không lặp vô hạn. Reduced-motion không animate rows reorder.

## Những điều tránh

Cấm KPI ngẫu nhiên, nút retry thực thi workflow thật, 10 chart trang trí, icon-only control khó hiểu, bảng ảnh không lọc được hoặc trạng thái thành công giả.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH COCKPIT
Bố cục và nhận diện: Brief Cockpit mới: nền #101720, panel #182330, border #2B3A49, chữ #EDF3F7, secondary #A6B7C5; cyan #69D4E4, amber #F3C56A, error #EE8A91. IBM Plex Sans/Mono, H1 32 px, số KPI 32–40 px, radius 6 px. Mật độ có thứ bậc, không dùng hero marketing 80 px.

## 3. Nội dung mở đầu

**H1:** Có việc cần xử lý, bạn thấy ngay.

**Lời dẫn:** Theo dõi các lần chạy workflow mẫu và tìm lý do một bước bị dừng.

**Hành động chính:** Xem lần chạy cần xử lý

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Tổng quan

**Bố cục và hành vi:** Một tiêu đề, khung thời gian và 3 KPI tính từ dataset: tổng lượt/thành công/cần xử lý.

**Nội dung và đầu ra:** Không số live ngẫu nhiên, nhãn Dữ liệu mẫu hiện cạnh thời gian.

### 2. Cần xử lý

**Bố cục và hành vi:** Lỗi quan trọng ở trên bảng: thiếu email/đích không phản hồi/dữ liệu không hợp lệ.

**Nội dung và đầu ra:** Mỗi lỗi có hướng sửa local, không mơ hồ Thất bại.

### 3. Lịch sử chạy

**Bố cục và hành vi:** Bảng 10 record với workflow, giờ, trạng thái, thời lượng; search/filter/sort.

**Nội dung và đầu ra:** Chọn row mở run-detail, không chart trang trí không liên quan.

### 4. Chi tiết lượt chạy

**Bố cục và hành vi:** Timeline các bước, input mẫu và log; hành động Sửa dữ liệu mẫu/Chạy lại mô phỏng.

**Nội dung và đầu ra:** Không thực thi n8n thật, không retry gửi tin ra ngoài.

### 5. Báo cáo và reset

**Bố cục và hành vi:** Xuất CSV dataset đang lọc với headers rõ, hoặc reset phiên.

**Nội dung và đầu ra:** Báo cáo không gọi là Excel nếu chỉ xuất CSV; không mật khẩu/credential.

## 5. Dữ liệu và trạng thái tương tác

KPI tính từ toàn bộ dataset theo bộ lọc thời gian; phải ghi rõ nếu bộ lọc bảng dùng phạm vi khác. Chạy lại tạo lượt mới có parentId, không xóa lỗi cũ. Bộ lọc không có kết quả phải có nút xóa lọc; sắp xếp ổn định.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

768 pxsidebar thu nhỏ;390 px cần xử lý đầu trang, bảng thành list có detail, chart có text summary. Không ẩn lỗi để giữ sạch layout.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Đổi trạng thái 150 ms, cập nhật data không đếm nhảy liên tục. Reduced-motion không ảnh hưởng data.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Dataset nhất quán từ cùng ba workflow, timestamps ghi mẫu; không dựng số doanh thu không liên quan.

**Cover:** Một alert, một KPI và 4 row, đủ lớn để thấy control panel; không chụp cả 10 widget nhỏ.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Retry giữ run lỗi cũ và thêm run mới có link.
2. Tổng success+error bằng tổng record trong khung giờ.
3. CSV theo bộ lọc và escape đúng dữ liệu.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
