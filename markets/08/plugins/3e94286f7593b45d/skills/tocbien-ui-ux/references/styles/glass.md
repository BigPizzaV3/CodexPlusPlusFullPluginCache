# Kính mờ (`glass`)

Thẻ kính mờ chồng lớp

- Hợp với: Hợp khi đang dùng AI để dựng website cho công cụ lịch và năng suất cần nhiều lớp không gian nhưng chữ vẫn rõ.
- Ngành minh hoạ: Sản phẩm công nghệ
- Trang minh hoạ làm việc gì: Lịch một ngày với thêm, sửa, xóa và hoàn tác sự kiện mẫu
- Thang (1–10): biến tấu bố cục 7 · chuyển động 6 · mật độ 3
- Xem mẫu: https://tocbien.cloud/phong-cach/glass/

## Đặc tả

Glass: nền xanh đêm #0b1024, quầng xanh dương/ngọc dịu, chữ sáng. Bề mặt kính bán trong suốt có viền sáng mảnh, blur vừa phải và bóng mềm thể hiện chiều sâu. Hero có ảnh sản phẩm thật rõ nét cạnh thông điệp; kính dùng để chứa thông tin ngắn, không phủ mờ chính sản phẩm. Các mục đặc điểm, cách dùng và lựa chọn theo dữ liệu dự án. Nút chính đặc màu để dễ tìm. Giữ nền dự phòng đủ đậm khi không hỗ trợ blur; không blur toàn trang. Điện thoại giảm hiệu ứng và xếp dọc.

**Chi tiết cần giữ:** Dùng bóng chồng nhiều lớp mềm, đừng dùng một lớp bóng phẳng — đó là chỗ khiến kính mờ trông rẻ tiền.

**Lưu ý khi áp dụng:** Bắt buộc có nền đặc dự phòng. Máy nào bật chế độ giảm trong suốt mà không có nền dự phòng là chữ biến mất.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: glass

Biến thể: Frosted Glass / agenda trên nền có chiều sâu. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #182A33 |
| surface | rgba(255,255,255,0.82) |
| surface-solid | #F1F5F5 |
| foreground | #15232B |
| muted | #40535E |
| accent | #176B76 |
| on-accent | #FFFFFF |
| border | rgba(255,255,255,0.65) |
| focus | #075B91 |
| error | #AA2F36 |

## Typography

Inter 400/500/600. H1 desktop 60 px/1.1, tablet 46 px/1.15, mobile 36 px/1.2. H2 28 px; item title 18 px/1.35; body 16 px/1.6; metadata 14 px/1.4. Không giảm opacity chữ vì muốn vật liệu trong hơn.

## Lưới, nhịp và responsive

Desktop max-width 1200 px, lịch 8 cột và detail 4 cột; gap 24 px. 768 px chuyển agenda và detail trong cùng cột. 390 pxgutter 16–20 px, inputfull-width. Ảnh nền có vùng ít chi tiết phía sau timeline; background-position phải chốt theo crop riêng.

## Bề mặt và vật liệu

Backdrop blur 20 px và saturation 120%; panel trắng opacity.82, highlight inset 0 1 px0 rgba(255,255,255,.65), shadow 0 16 px40 px rgba(0,0,0,.12). Radius 20 px. Chỉ hai lớp kính nhìn thấy; modal/entry form dùng opacity.96 để bảo đảm đọc. Không blur trực tiếp nội dung chữ.

## Thành phần và trạng thái

### Panel lịch

Lịch trên surface kính, text trên lớp riêng, nền phía sau không click-through. Slot chỉ có một hàng nhãn, trạng thái chọn dùng cả fill và check.

### Text field

Nhãn trên ô, nền gần đặc, border 1 px, cao 48 px. Focus 2 px #075B91, lỗi có text dưới và aria-describedby. Placeholder chỉ là ví dụ, không thay label.

### Popover

Không áp backdrop blur lồng nữa. Dùng nền gần đặc và z-index riêng, đủ khoảng cách để không che control đang thao tác.

### Giảm trong suốt

Toggle có label hiển thị, aria-pressed đúng. Chuyển tất cả panel sang surface-solid, không đổi dữ liệu hoặc layout. Nếu backdrop-filter không hỗ trợ, dùng fallback này tự động.

## Chuyển động và phương án giảm chuyển động

Panel fade/translate 4 px trong 180 ms, không làm background trôi theo con trỏ. Reduced-motion bỏ translate; giảm trong suốt là tùy chọn độc lập, không đồng nhất với giảm chuyển động.

## Những điều tránh

Cấm text sáng trên vùng ảnh sáng, nhiều lớp blur chồng nặng, shadow neon, background ảnh có chi tiết đánh nhau với chữ, hoặc gọi đây là triển khai Apple Liquid Glass chính thức.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH GLASS
Bố cục và nhận diện: Brief Glass mới: nền ảnh không gian trầm #182A33; panel rgba(255,255,255,.82), chữ #15232B; accent #176B76, border trắng .65; Inter, H1 52–64 px, body 16 px. Blur 20 px/saturation 120%, radius 20 px; chỉ 2 lớp kính nhìn thấy, không kính lồng vô hạn. Không tự gọi Apple Liquid Glass chính thức.

## 3. Nội dung mở đầu

**H1:** Một ngày, nhìn rõ từng khoảng.

**Lời dẫn:** Thử sắp xếp lịch cá nhân trong giao diện kính mờ, với trạng thái và nội dung luôn đọc được.

**Hành động chính:** Thử sắp xếp một ngày

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Lịch hôm nay

**Bố cục và hành vi:** Headline ngắn phía trên panel lịch; ảnh nền chỉ tạo chiều sâu, không làm nội dung trung tâm.

**Nội dung và đầu ra:** Một ngày mẫu có 4 lịch hẹn cá nhân, không dùng dữ liệu lịch thật.

### 2. Các khoảng giờ

**Bố cục và hành vi:** Timeline từ 8–18h, từng lịch có tiêu đề, thời lượng và nhãn trạng thái.

**Nội dung và đầu ra:** Lịch trùng giờ hiển thị cạnh nhau hoặc có nhãn xung đột.

### 3. Thêm lịch mẫu

**Bố cục và hành vi:** Form trong panel đặc hơn, gồm tiêu đề/bắt đầu/kết thúc; không dropdown trong backdrop-blur chồng lớp.

**Nội dung và đầu ra:** Validate kết thúc sau bắt đầu; giữ dữ liệu nếu đóng nhầm.

### 4. Xem lịch

**Bố cục và hành vi:** Panel chi tiết với sửa/xóa có đường lui, nội dung đọc được cả trên vùng ảnh sáng.

**Nội dung và đầu ra:** Xóa có hoàn tác trong phiên, không kết nối tài khoản lịch.

### 5. Độ rõ hiển thị

**Bố cục và hành vi:** Nút Giảm trong suốt chuyển sang nền gần đặc.

**Nội dung và đầu ra:** Không giảm độ tương phản của chữ để làm panel trong hơn.

## 5. Dữ liệu và trạng thái tương tác

Events có id/start/end/title; conflict dựa interval thật. Undo khôi phục đúng event và thời gian, không duplicate. Toggle độ rõ không đổi dataset.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

390 px lịch thành agenda một cột; background crop riêng để ít chi tiết sau chữ. Khi blur không hỗ trợ, panel dùng solid #F1F5F5; không phụ thuộc hiệu ứng để phân nhóm.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Panel 180 ms opacity/translate 4 px; nền không parallax trên mobile. Reduced-motion bỏ translate, giảm trong suốt luôn có control riêng.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Một ảnh AI hậu cảnh và crop mobile; giao diện lịch dựng thật.

**Cover:** Một panel lịch với background thấy xuyên ở viền; đủ highlight để nhận chất kính nhưng text sắc. Không cover thành ảnh phong cảnh.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Test cùng panel trên ảnh nền sáng/tối đều đọc được.
2. Thêm lịch trùng giờ có báo rõ.
3. Không hỗ trợ blur vẫn dùng được và không lộ chữ nền gây nhiễu.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
