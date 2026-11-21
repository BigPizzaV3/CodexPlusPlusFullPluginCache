# Bento (`bento`)

Lưới ô lớn nhỏ xen kẽ

- Hợp với: Hợp khi đang dùng AI để dựng website cho người làm nhiều loại việc muốn giới thiệu 5–7 điểm mà không kéo trang quá dài.
- Ngành minh hoạ: Cửa hàng, xưởng dịch vụ
- Trang minh hoạ làm việc gì: Portfolio sản phẩm trong lưới bảy ô có case và công cụ nhỏ
- Thang (1–10): biến tấu bố cục 7 · chuyển động 5 · mật độ 5
- Xem mẫu: https://tocbien.cloud/phong-cach/bento/

## Đặc tả

Bento: nền sáng #f4f5f7, ô trắng, mực gần đen, nhấn xanh dương. Lưới ô lớn nhỏ xen kẽ bằng CSS Grid; ô quan trọng nhất rộng hơn và đứng đầu thứ tự đọc. Mỗi ô phục vụ một nội dung rõ, dùng ảnh thật, biểu tượng hoặc số liệu đúng chỗ. Bo vừa, viền mảnh, khoảng cách đều. Lấp lưới bằng cách đổi kích thước ô theo nội dung, không bịa thêm mục hoặc thẻ rỗng. Không lồng thẻ nhiều tầng. Trên điện thoại một cột theo ưu tiên, bỏ các vị trí hàng/cột cố định để không tạo khoảng trống.

**Chi tiết cần giữ:** Lưới không được hở một ô nào. Sắp nội dung theo thứ tự chú ý → quan tâm → muốn → hành động, đừng rải đều tầm quan trọng cho mọi ô.

**Lưu ý khi áp dụng:** Lưới phải kín. Thừa một ô trống là hỏng cả bố cục, nên số ô phải chia vừa với số việc bạn có.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: bento

Biến thể: Bento Portfolio / mô-đun có thứ bậc. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #F4F4F0 |
| surface | #FFFFFF |
| foreground | #202322 |
| muted | #59635C |
| accent | #356B4F |
| on-accent | #FFFFFF |
| border | #DCDDD5 |
| focus | #174E8A |
| error | #A73232 |

## Typography

Inter 400/500/600/700. Display desktop 64 px/1.05, tablet 48 px/1.1, mobile 36 px/1.15; H2 32/28/26 px; Tiêu đề ô24 px/1.2; body 16 px/1.6; metadata 14 px/1.4. Dùng độ lớn ô và thứ bậc chữ để tạo nhịp, không dùng bảy font cho bảy ô.

## Lưới, nhịp và responsive

Grid desktop 12 cột, gap 16 px, max-width 1280 px, padding 32 px. Tablet 6 cột gap 16 px; mobile 2 cột gap 12 px và gutter 20 px. Ô có nội dung dài được tăng hàng, không fixed height cắt text. Tối đa hai ô liên tiếp cùng kích thước nếu cần tạo nhịp; một ô chính luôn có ưu thế diện tích.

## Bề mặt và vật liệu

Radius 20 px cho ô lớn,12 px cho control nội bộ, không thêm nhiều lớp card trong card. Viền 1 px #DCDDD5; bóng 0 4 px 16 px rgba(0,0,0,.04) chỉ ở ô có tương tác. Có thể dùng tối đa ba dạng bề mặt: ảnh, màu đặc và nền trắng; tất cả cùng bộ type.

## Thành phần và trạng thái

### Ô dự án

Toàn ô là một link nếu chỉ có một hành động. Tên dự án và vai trò luôn hiện, không chỉ xuất hiện khi hover. Focus outline 2 px nằm ngoài ô, không bị overflow của ảnh cắt. Không lồng button trong link.

### Ô công cụ

Nếu có điều khiển bên trong, ô không là link. Nút cao 44 px, hitbox riêng và label rõ; chạy công cụ không tự mở case study.

### Ô tác giả

Chân dung không chiếm nhiều diện tích hơn tác phẩm chính. Caption gắn với vai trò tác giả, không quote tự khen hoặc logo khách giả.

### Case mở rộng

Nằm sau grid, span toàn hàng. Close có label, quay lại trả focus đúng ô; nội dung max-width 72 ch, gallery có kích thước ổn định.

## Chuyển động và phương án giảm chuyển động

Hover ô dịch 2 px trong 180 ms ease-out. Không animate toàn grid đổi thứ tự khi pointer đi qua. Mở case 240 ms; chỉ một case được mở. Reduced-motion không chuyển vị trí, vẫn đổi border.

## Những điều tránh

Cấm grid mọi ô bằng nhau, ô rỗng lấp chỗ, chữ nhỏ để nhét đúng hàng, đặt layout order khác DOM order, gradient khác họ trên từng ô, hoặc dùng Bento như lý do gom mọi thứ vào card.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH BENTO
Bố cục và nhận diện: Brief mới đề xuất cho bố cục Bento: nền #F4F4F0, chữ #202322, surface #FFFFFF, accent #356B4F; Inter cho UI và heading, H1 56–72 px. Grid 12 cột/gap 16 px, radius 20 px, border #DCDDD5, shadow tối đa 0 4 px 16 px rgba(0,0,0,.04). Đây là lựa chọn riêng cho mẫu này, không chuẩn bắt buộc của mọi Bento.

## 3. Nội dung mở đầu

**H1:** Một người, nhiều cách tạo ra sản phẩm.

**Lời dẫn:** Một hồ sơ dự án nhỏ, từ công cụ tiện ích đến nhận diện và thử nghiệm tương tác.

**Hành động chính:** Khám phá dự án

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Bảng tác phẩm

**Bố cục và hành vi:** Bảy ô có vai trò xác định: intro 4×2, dự án chính 8×2, hai dự án 4×2, ghi chú 4×1, chân dung 4×1, liên hệ 4×1.

**Nội dung và đầu ra:** Không ô rỗng để lấp lưới; chiều cao là đề xuất theo hàng cơ sở 120 px, nội dung dài được tăng tự nhiên.

### 2. Dự án chính

**Bố cục và hành vi:** Ô lớn chứa ảnh sản phẩm và tên công dụng; click mở case ngay dưới grid.

**Nội dung và đầu ra:** Ví dụ công cụ lập lịch cá nhân có input và output rõ, không KPI trang trí.

### 3. Hai thử nghiệm

**Bố cục và hành vi:** Một ô ảnh, một ô tương tác code-native, khác texture nhưng cùng hệ type.

**Nội dung và đầu ra:** Mỗi ô có label mở dự án và caption vai trò.

### 4. Case đang xem

**Bố cục và hành vi:** Vùng mở rộng span 12 theo cùng lưới, gồm vấn đề/giải pháp/tài sản/đường quay lại.

**Nội dung và đầu ra:** Không modal có chiều cao vượt màn khiến mất grid.

### 5. Trao đổi

**Bố cục và hành vi:** Ô liên hệ dẫn tới form dưới grid, không cả ô lẫn nút nested thành hai link.

**Nội dung và đầu ra:** Dùng nhãn Xem brief mẫu, không gán khách hàng thật.

## 5. Dữ liệu và trạng thái tương tác

activeProject một lúc một; mở case cập nhật aria-expanded, đóng trả focus ô nguồn. Ô tương tác phụ không kích link dự án khi bấm nút bên trong.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

768 px grid 6 cột; 390 px: 2 cột nhưng intro/dự án chính span 2, ô nhỏ chỉ 1 cột khi vẫn đọc được. Thứ tự DOM intro→dự án→tác giả→liên hệ, không visual reorder làm sai tab.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Hover nâng 2 px trong 180 ms, mở case 240 ms; không mọi ô đều lắc hoặc phát video. Reduced-motion đổi trạng thái ngay.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Bìa AI cho từng dự án và ảnh chân dung minh họa; không ô rỗng để đủ lưới.

**Cover:** Cover thể hiện 5–7 ô và một ô lớn rõ, không screenshot rất nhiều tile. Dọc dùng bố cục grid mobile thật, không crop nửa grid desktop.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Bảy ô đều có chức năng/nội dung, không ô rỗng.
2. Tab order khớp thứ tự đọc.
3. Cover desktop và mobile thể hiện cùng các dự án.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
