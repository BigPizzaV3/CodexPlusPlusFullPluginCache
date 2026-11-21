# Sticky-stack (`sticky-stack`)

Từng bước xếp chồng khi cuộn

- Hợp với: Hợp khi đang dùng AI để dựng website cho dịch vụ có quy trình dài cần người xem nhớ đúng thứ tự và đầu ra.
- Ngành minh hoạ: Gara, dịch vụ theo quy trình
- Trang minh hoạ làm việc gì: Quy trình cải tạo bốn bước từ khảo sát tới bàn giao
- Thang (1–10): biến tấu bố cục 7 · chuyển động 7 · mật độ 4
- Xem mẫu: https://tocbien.cloud/phong-cach/sticky-stack/

## Đặc tả

Sticky-stack: nền ngà #faf8f4, các bước trên bề mặt sáng, mực đậm, nhấn cam đất #c2521b. Mỗi bước có số, tiêu đề, kết quả và mô tả vừa đủ. Số bước theo quy trình thật, không ép thành ba bước. Trên máy tính dùng position:sticky cho khối trước giữ lại khi khối sau đi lên; không khóa cuộn và không che nội dung dài. Thứ tự trong mã phải đúng thứ tự đọc. Trên điện thoại và khi prefers-reduced-motion, bỏ ghim và xếp dọc bình thường, chiều cao theo nội dung.

**Chi tiết cần giữ:** Ghim và xếp chồng phải phục vụ thứ tự nội dung. Sắp theo chú ý → quan tâm → muốn → hành động, đừng ghim những khối không liên quan.

**Lưu ý khi áp dụng:** Chỉ dùng khi nội dung THẬT SỰ có thứ tự. Ghim những khối không liên quan lại với nhau chỉ làm khách khó chịu.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: sticky-stack

Biến thể: Sticky Stack / trình tự bốn bước chồng có điều khiển. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #F3F0E8 |
| surface | #FFFFFF |
| surface-alt | #E6E9DF |
| foreground | #252924 |
| muted | #596255 |
| accent | #416658 |
| on-accent | #FFFFFF |
| border | #D6D8CD |
| focus | #275F85 |
| error | #A23E35 |

## Typography

Inter 400/500/600/700. H1 desktop 72 px/1.1, tablet 52 px, mobile 38 px; số bước 64 pxdesktop/40 pxmobile; paneltitle 36 px/1.2; body 18 px/1.6. Số bước không to đến mức đẩy đầu ra của bước khỏi màn.

## Lưới, nhịp và responsive

Max-width 1200 px, panel desktop ảnh 6 cột/nội dung 6 cột, gap 32 px; vùng header ngoài stack. Panel không cao hơn viewport trừ navigation và24 pxmargin. Khi nội dung vượt hoặc viewport thấp dưới 700 px, chuyển flow thường.

## Bề mặt và vật liệu

Radius 12 px, border 1 px, shadow 0 12 px32 px rgba(30,40,28,.10). Stackoffset 24 px, scale từ.96 đến 1; depth được tạo bằng thẻ thật, không ảnh chụp chồng. Z-index tăng theo thứ tự bước, focus không kẹt ở panel đã bị che.

## Thành phần và trạng thái

### Bộ chọn bước

Nút 1–4có nhãn tên bước; aria-current cho bước hiện tại. Chọn nút cuộn đến section theo cách không scrollhijack.

### Panel bước

Gồm đầu vào, việc thực hiện, đầu ra và ảnh. Không để CTA quan trọng ở đáy panel bị cắt. Nội dung tồn tại ngaytrongDOM.

### Xem toàn bộ

Tắt sticky/transform nhưng giữ nội dung và thứ tự; focus được trả đến heading bước đang xem.

### Checklist bàn giao

Checkboxlabel rõ, trạng thái lưu trong phiên thử; không tự đánh hoàn thành vì cuộn qua bước. Reset không thay đổi viewportmode.

## Chuyển động và phương án giảm chuyển động

Dựa tiến độ cuộn tự nhiên, không intercept wheel. Tối đa scale 4%, không opacity 0. Reduced-motion và mobile chuyển flow tĩnh; không phải điều kiện cho đọc nội dung.

## Những điều tránh

Cấm pin mọi section, totalheight ngụy tạo khiến cuộn quá lâu, focus ở phía dưới panel che, cùng một hiệu ứng trên 37mẫu, hoặc đổi nội dung phù hợp chỉ để gắn n8n.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH STICKY-STACK
Bố cục và nhận diện: Brief bố cục Sticky Stack mới: nền #F3F0E8, chữ #252924, accent #416658; Inter, H1 64–80 px; radius của panel 12 px, viền #D6D8CD. Bốn thẻ chồng theo thứ tự, scale sâu 0.96–1 và offset 24 px. Đây là ngôn ngữ bổ trợ đề xuất, cơ chế stack mới là nhận diện.

## 3. Nội dung mở đầu

**H1:** Bốn bước, mỗi bước một điều rõ ràng.

**Lời dẫn:** Xem một quy trình sửa nhà qua đầu vào, công việc và sản phẩm bàn giao từng giai đoạn.

**Hành động chính:** Xem bốn bước / Xem checklist bàn giao

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Tổng quan bốn bước

**Bố cục và hành vi:** Headline và danh sách 1–4, CTA Theo dõi quy trình; không hero kéo dài trước hiệu ứng.

**Nội dung và đầu ra:** Không số căn đã sửa, cam kết phạt hoặc bảo hành bịa.

### 2. 01 Khảo sát

**Bố cục và hành vi:** Panel ảnh hiện trạng và checklist yêu cầu; chiều cao tối đa phù hợp màn.

**Nội dung và đầu ra:** Đầu ra: ảnh hiện trạng và phạm vi cần làm.

### 3. 02 Phần thô

**Bố cục và hành vi:** Panel tiếp theo chồng lên, giữ tab số 01 làm ngữ cảnh.

**Nội dung và đầu ra:** Đầu ra: ảnh đường điện/nước và checklist, cùng công trình mẫu.

### 4. 03 Hoàn thiện

**Bố cục và hành vi:** Chọn vật liệu và ảnh sau hoàn thiện tương ứng; không mỗi bước một căn nhà.

**Nội dung và đầu ra:** Đầu ra: danh sách vật liệu và hạng mục chờ kiểm.

### 5. 04 Bàn giao

**Bố cục và hành vi:** Checklist local, rồi nút Xem toàn quy trình mở 4 bước trong luồng đọc thông thường.

**Nội dung và đầu ra:** Không giả thanh toán hoặc nghiệm thu công trình thật.

## 5. Dữ liệu và trạng thái tương tác

activeStep đồng bộ với scroll/nút; checklist độc lập không mất khi cuộn. ViewAll tắt pin, giữ bước đang xem làm focus đích; reset chỉ checklist.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

Dưới 768 px hoặc chiều cao dưới 700 px tắt pin dài, dùng steps dọc; nút Tiếp/Trước hỗ trợ bàn phím. Không panel cao hơn viewport làm nội dung bị kẹt.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Stack desktop theo tiến độ cuộn, không ép wheel; scale rất nhỏ, không opacity 0 làm section mất. Reduced-motion dùng ViewAll mặc định.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Ảnh minh họa cùng một công trình qua bốn giai đoạn; bản vẽ và checklist rõ là dữ liệu mẫu.

**Cover:** Chụp frame bước 2 làm nội dung chính, để lộ mép bước 1 và 3 nhằm thể hiện stack; không chụp hero đầu trang khi các lớp chưa chồng. Khung dọc cho thấy 2 lớp rõ và giữ đầy đủ chữ của bước 2.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Ở 1280×720 đọc được đáy mọi panel.
2. ViewAll không làm mất checklist.
3. Reduced-motion hiện đủ 4 bước đúng thứ tự.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
