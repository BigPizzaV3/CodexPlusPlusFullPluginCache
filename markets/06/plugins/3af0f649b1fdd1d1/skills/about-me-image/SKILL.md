---
name: about-me-image
description: Tạo ảnh chiếc hộp kim loại About Me khi người dùng gõ /aboutme hoặc muốn một diorama trực quan về bản thân.
---

# About Me – AI Life Box

Khi người dùng nhập `/aboutme`, tạo ảnh bằng công cụ tạo ảnh. Nếu thông tin về họ chưa đủ để chọn ít nhất ba vật thể có căn cứ, hỏi tối đa ba câu ngắn về công việc, sở thích và điều quan trọng với họ trước khi tạo. Ưu tiên thông tin vừa được người dùng cung cấp. Không coi các chủ đề họ từng đặt câu hỏi là sở thích, nghề nghiệp hay sự thật đời tư. Không suy đoán tuổi, nơi ở, gia đình, con cái, ngoại hình, mục tiêu hay tính cách. Không cần xác nhận prompt khi đã có đủ dữ kiện.

## Bố cục bắt buộc

Ảnh chính là **một chiếc hộp thiếc chữ nhật bo góc đang mở**, nhìn chính diện từ trên xuống ở góc 90 độ. Nắp chiếm nửa trên, bản lề ngang ở giữa, lòng hộp chiếm nửa dưới. Toàn bộ viền hộp và cả hai phần đều nằm trọn trong khung hình. Bố trí một số vật thể thu nhỏ bên trong cả nắp lẫn lòng hộp. Nền bên ngoài hộp đơn giản; ánh sáng studio chân thực, kim loại và vật thể có độ sâu. Cảm giác flat-lay/diorama photorealistic, gọn, cao cấp.

Ảnh tham khảo bố cục: `assets/about-me-template.jpeg` tại gốc plugin. Trước khi gọi công cụ tạo ảnh, xác định đường dẫn thật của plugin từ `skill_root` nếu có, mở ảnh mẫu bằng công cụ xem ảnh, rồi truyền **đường dẫn tuyệt đối** qua `referenced_image_paths`. Không truyền chuỗi tương đối `assets/...` cho công cụ. **Điều kiện bắt buộc trước khi tạo ảnh:** từ `skill_root` là thư mục `skills/about-me-image`, lấy thư mục gốc plugin bằng cách đi lên hai cấp, sau đó nối `assets/about-me-template.jpeg`. Kiểm tra tệp tồn tại và mở bằng công cụ xem ảnh; gọi `image_gen.imagegen` với `referenced_image_paths: [đường_dẫn_tuyệt_đối_đến_ảnh_mẫu]`. Nếu không thể đọc hoặc truyền ảnh mẫu, **dừng trước khi tạo ảnh**, đề nghị người dùng đính kèm ảnh chiếc hộp mẫu trong cuộc trò chuyện. Khi ảnh nằm trong hội thoại mà không có đường dẫn, dùng `num_last_images_to_include` theo hướng dẫn công cụ để gửi đúng ảnh đó. Không tạo ảnh chỉ từ mô tả bằng chữ. Ảnh mẫu quy định hình dạng hộp, góc nhìn, vị trí nắp và đáy; các vật thể bên trong được thay bằng dữ kiện của người dùng.

## Nội dung và prompt

Lập danh sách 3–7 vật thể và dữ kiện đã được xác nhận mà từng vật thể đại diện. Nếu chỉ biết người dùng làm công nghệ, có thể chọn laptop, sơ đồ cơ sở dữ liệu hoặc thiết bị máy chủ; không thêm con cái, thú cưng, du lịch, nhiếp ảnh hay tiền mã hóa nếu không có lời xác nhận. Không dùng ảnh chân dung giống người thật nếu họ chưa cung cấp ảnh. Tránh ảnh một người ngồi ở bàn làm việc, văn phòng, poster tiểu sử, bảng thông tin, infographic, ảnh ghép hoặc hộp nhỏ đặt trong một căn phòng.

Prompt phải bắt đầu bằng cấu trúc hộp và góc chụp, rồi chỉ rõ vật thể ở nắp và lòng hộp; yêu cầu **không có người, khuôn mặt, chữ dài, bảng liệt kê hay tiểu sử**. Nếu cần chữ, tối đa vài từ ngắn. Không ghi dữ kiện chưa được xác nhận vào prompt, kể cả như chi tiết trang trí.

Sau khi tạo ảnh, xem kết quả. Chỉ trả khi chiếc hộp chiếm phần lớn ảnh, nắp và lòng hộp nhìn thấy rõ, toàn bộ vật thể có căn cứ. Nếu ảnh thành chân dung/bàn làm việc hoặc có thông tin bịa đặt, gọi công cụ chỉnh sửa với ảnh đầu ra làm đích và ảnh mẫu làm tham khảo, yêu cầu đổi toàn bộ bố cục thành hộp mở nhìn từ trên xuống và bỏ các chi tiết vô căn cứ. Nếu vẫn không đạt, báo rõ là chưa tạo được ảnh đúng mẫu; không trình bày ảnh sai như kết quả hoàn chỉnh.
