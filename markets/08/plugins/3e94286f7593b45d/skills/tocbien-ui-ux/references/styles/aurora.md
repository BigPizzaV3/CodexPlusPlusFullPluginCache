# Aurora (`aurora`)

Nền loang màu mềm

- Hợp với: Hợp khi đang dùng AI để dựng website cho sản phẩm AI nhẹ nhàng cần chỉ rõ quan hệ giữa đầu vào và kết quả.
- Ngành minh hoạ: Lớp học, sự kiện
- Trang minh hoạ làm việc gì: Công cụ sắp ghi chú thành quyết định, việc cần làm và câu hỏi
- Thang (1–10): biến tấu bố cục 7 · chuyển động 6 · mật độ 4
- Xem mẫu: https://tocbien.cloud/phong-cach/aurora/

## Đặc tả

Aurora: nền tối, các quầng sáng xanh lam và xanh ngọc mềm phía sau; nếu thương hiệu có bảng màu riêng, chuyển quầng sang màu tương ứng. Một tiêu đề rõ, câu giải thích và hành động chính nổi trên vùng nền ít nhiễu. Các mục bổ sung chỉ giải đáp điều người dùng cần trước khi hành động, không nhồi hàng thẻ tính năng. Gradient là không khí nền, không là lớp che chữ. Giữ liên kết thông tin thiết yếu và đường quay lại nếu luồng cần. Màn hẹp thu gọn quầng, nút dễ bấm; nền tĩnh vẫn đẹp khi tắt chuyển động.

**Chi tiết cần giữ:** Đây là phong cách bị dùng sáo nhất. Trước khi giao, tự soi xem trang có đang giống mọi trang AI khác không, rồi đổi cặp màu và bố cục cho khác đi.

**Lưu ý khi áp dụng:** Rất dễ sáo. Nếu gradient tím sang xanh thì trang trông y hệt hàng nghìn trang khác — đổi sang cặp màu lấy từ thương hiệu của bạn.

## Đặc tả gốc chi tiết (giữ đầy đủ)

# Brief mới: aurora

Biến thể: Aurora Light / trường ánh sáng hỗ trợ công cụ ghi chú. Đề xuất riêng cho mẫu này, không tự nhận là quy chuẩn duy nhất của phong cách.

## Bảng màu theo vai trò

| Token | Giá trị |
|---|---|
| background | #F5F4FC |
| surface | #FFFFFF |
| foreground | #202335 |
| muted | #585D75 |
| accent | #6656C7 |
| on-accent | #FFFFFF |
| border | #DAD8EB |
| focus | #4B37AE |
| lavender | #BDB2FF |
| mint | #B8E8D8 |
| peach | #F4CBBD |
| error | #A83143 |

## Typography

Manrope 600/700 cho heading, Inter 400/500 cho body. H1 desktop 72 px/1.08, tablet 52 px, mobile 38 px/1.18; H2 32 px; body 18 px/1.65; UI16 px; metadata 14 px. Chỉ một từ head line được gradient nếu vẫn đủ con tr ast; body luôn solid.

## Lưới, nhịp và responsive

Max-width 1200 px, hero trung tâm nhưng phần công cụ hai vùng 6/6 cân theo lượng nội dung; padding 32 px. Mobile một cột theo input→output, gutter 20 px; có link nhảy giữa hai vùng thay sticky tóm tắt che nội dung.

## Bề mặt và vật liệu

Ba radial gradient lớn 120–160% khung, tâm lệch khác nhau, blur nền 48–80 px nếu chi phí cho phép; ưu tiên radial CSS tĩnh hơn ảnh nặng. Panel trắng.94, radius 18 px, viền 1 px, shadow 0 12 px32 px rgba(48,41,87,.06). Không biến toàn panel thành kính.

## Thành phần và trạng thái

### Chọn bối cảnh

Segmented controls có tên đầy đủ; selectedfill accent và text trắng, focus riêng. Ba dataset có nhãn ghi chú mẫu.

### Ghi chú nguồn

Mỗi dòng có id, nội dung và lựa chọn highlight. Không cho người dùng sửa text rồi trả output cũ như đã được AI hiểu.

### Kết quả

Ba nhóm quyết định/việc làm/cần hỏi; mỗi mục có liên kết nguồn cụ thể. Nhóm trống hiện Không có trong ghi chú thay bịa.

### Copy

Copy markdown từ kết quả đang chọn; nếu API clipboard bị chặn, mở text area readonly để chép thủ công. Không to ast thành công khi Promise bị reject.

## Chuyển động và phương án giảm chuyển động

Ba vùng ánh sáng trôi rất chậm 20 s, transform biên độ12 px. Có pause, mobile dùng tĩnh nếu đo thấy jank. Kết quả fade 250 ms, không loading giả. Reduced-motion ngừng trường sáng và fade.

## Những điều tránh

Cấm chỉ có gradient mà thiếu sản phẩm, badgeAI trực tiếp cho dữ liệu mẫu, glass lồng nhiều lớp, bodygradient, lưu credential hoặc tự gửi ghi chú ra bên ngoài.

## Kiểm giá trị trước triển khai

Đo tương phản của các cặp chữ/bề mặt và trạng thái thực tế; không dựa vào màu hex đơn lẻ để tuyên bố đạt. Kiểm đủ dấu tiếng Việt và fallback font. Phần bố cục nội dung, dataset, cover và kịch bản riêng nằm ngay sau brief này trong prompt độc lập.

## Đặc tả áp dụng chi tiết

CÁCH ÁP DỤNG PHONG CÁCH AURORA
Bố cục và nhận diện: Brief Aurora mới: nền #F5F4FC, chữ #202335, surface #FFFFFF, accent #6656C7; trường sáng lavender #BDB2FF/mint #B8E8D8/peach #F4CBBD. Manrope cho heading, Inter cho body; H1 64–80 px; gradient loang ở nền, không dùng chữ body gradient, radius 18 px.

## 3. Nội dung mở đầu

**H1:** Gom ý rời thành việc rõ.

**Lời dẫn:** Chọn một bộ ghi chú mẫu để xem cách sắp lại thành quyết định, việc cần làm và điều còn thiếu.

**Hành động chính:** Xem một bản tóm tắt mẫu

## 4. Đặc tả từng vùng nội dung và tác vụ

### 1. Ý chính trong ánh sáng

**Bố cục và hành vi:** Headline trên vùng nền loang, một cặp notes→summary bên dưới.

**Nội dung và đầu ra:** Nêu kết quả dựng sẵn theo mẫu, không giả AI suy luận mọi văn bản.

### 2. Chọn bối cảnh

**Bố cục và hành vi:** Ba dataset Họp dự án/Ý tưởng bài viết/Kế hoạch tuần.

**Nội dung và đầu ra:** Mỗi dataset có input và output phù hợp, không dùng cùng summary.

### 3. Ghi chú

**Bố cục và hành vi:** Danh sách 3–6 ghi chú có thể đánh dấu nguồn; không cho chỉnh sửa rồi trả bản tóm tắt cũ như thể hệ thống đã hiểu.

**Nội dung và đầu ra:** Nếu cho chỉnh sửa, ghi rõ chế độ tự sắp xếp chưa xử lý bằng AI.

### 4. Bản đã sắp

**Bố cục và hành vi:** Ba nhóm Quyết định/Việc làm/Cần hỏi lại; chọn mục làm nổi ghi chú nguồn.

**Nội dung và đầu ra:** Không bịa người phụ trách hoặc deadline ngoài input.

### 5. Mang kết quả đi

**Bố cục và hành vi:** Copy markdown hoặc reset, có preview text trước khi copy.

**Nội dung và đầu ra:** Không tự tạo công việc ở app ngoài.

## 5. Dữ liệu và trạng thái tương tác

selectedDataset đặt lại selectedNote; generatedSummary là mapping rõ. Highlight quan hệ input/output, empty bỏ nhóm không có hoặc ghi Chưa có, không invent.

Phân biệt rõ dữ liệu dựng sẵn với hành động thực: chức năng thử trong mẫu không gửi tin, tạo đơn, đặt lịch hoặc thực thi workflow bên ngoài. Nếu phiên bản khách sau này kết nối dịch vụ thật, đó là phần tích hợp riêng cần quyền và kiểm lỗi phù hợp.

## 6. Responsive và thứ tự đọc

Ở 390 px, ghi chú nằm trên bản tóm tắt; có nút Chuyển tới kết quả và quay lại. Trường sáng cắt gọn, không dùng ảnh nền nặng. Chữ 16–18 px.

Kiểm thêm 320 px và 1280×720 để phát hiện cắt chữ/đáy panel. Thứ tự DOM phải theo việc người xem cần làm, không chỉ sắp lại bằng CSS rồi khiến Tab đi lộn. Bảng/log dài cuộn bên trong vùng có nhãn.

## 7. Chuyển động và phản hồi

Aurora drift 20 s transform chậm với pause; kết quả reveal 250 ms, không loading giả kéo 3 giây. Reduced-motion nền tĩnh.

Không để motion làm chậm thao tác hoặc che lỗi. Lưu trạng thái pause trong phiên khi có vòng lặp; reduced-motion phải giữ toàn bộ thông tin và thứ tự nội dung.

## 8. Art direction và ảnh đại diện

**Tài sản nội dung:** Nền ánh sáng code-native, không cần ảnh stock; nội dung trước/sau có ý nghĩa.

**Cover:** Hai cụm notes/summary và trường sáng có hình dạng rõ; không gradient trống không sản phẩm.

**Bộ xuất:** cover 1200×750; cover dọc 900×1200; OG 1200×630; screenshot QA riêng ở viewport thực. Chụp/compose từ đúng phiên bản đã dựng, không ảnh hero hứa một thiết kế khác trang thật.

## 9. Trường hợp nghiệm thu riêng

1. Ba dataset trả ba kết quả khác nhau.
2. Không deadline/người phụ trách bịa.
3. Pause giữ nguyên trường sáng nhưng dừng chuyển động.

Ngoài ba trường hợp này, chạy bộ kiểm chung của kế hoạch: tải ảnh/font lỗi, focus, reduced-motion, zoom200%, trạng thái trống và quay lại/reset. Không ghi đạt nếu chưa có bằng chứng.

Các tên, ngành và tác vụ ở trên là ví dụ có thể chuyển sang dự án của người dùng. Giữ ngôn ngữ thị giác gốc; không ép dự án thật thành nội dung của trang minh họa.
