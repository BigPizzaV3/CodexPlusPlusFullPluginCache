# Dạy cách sử dụng plugin

Đọc cùng `00_USER_GUIDE_VI.md`; dùng hướng dẫn đó cho thao tác công khai thay vì suy đoán tên nút hoặc vị trí giao diện. Đọc `04_OFFICIAL_SOURCES.md` khi cần đối chiếu thông tin sản phẩm.

## Xác định điều người học muốn làm

Phân biệt ba yêu cầu: học khái niệm, thao tác với một plugin cụ thể, hoặc hoàn thành công việc bằng plugin. Suy ra từ câu hỏi và ngữ cảnh; không bắt người học trả lời một bảng khảo sát dài.

Nếu hỏi “thêm hướng dẫn dùng plugin”, cung cấp cả phần dùng chính GPT Learning và bài học chọn/gọi plugin khác. Nếu đang sửa một gói plugin, thêm hướng dẫn vào tài nguyên có thể được skill đọc; không chỉ viết hướng dẫn trong câu trả lời rồi bỏ quên gói.

## Lộ trình dạy

1. Bắt đầu bằng một việc người học quan tâm: tóm tắt tài liệu được cung cấp, soạn bài giảng, luyện viết hoặc tạo sản phẩm học tập.
2. Giải thích plugin/skill/công cụ kết nối bằng một ví dụ ngắn. Không dạy thuật ngữ MCP trước khi người học cần hiểu nó.
3. Dùng hướng dẫn công khai để đi qua tìm, cài, gọi bằng @ và kết nối nếu cần. Không giả định thao tác đã xảy ra chỉ vì đã hướng dẫn.
4. Cho người học thử một đầu vào nhỏ, không nhạy cảm. Yêu cầu họ nêu sản phẩm muốn nhận và tiêu chí kiểm tra.
5. Phản hồi dựa trên kết quả thật hoặc kết quả do người học cung cấp. Nếu chỉ có mô phỏng, ghi rõ là mô phỏng.
6. Tăng khó bằng cách thêm một nguồn hoặc một yêu cầu định dạng. Chỉ phối hợp nhiều plugin khi mỗi plugin có một vai trò rõ ràng.

## Khi người học nêu tên plugin cụ thể

- Đọc mô tả và các khả năng thực sự sẵn có nếu có công cụ khám phá plugin. Không suy ra khả năng từ tên gọi.
- Tận dụng công cụ tích hợp sẵn của host khi phù hợp. Không mặc định việc tìm nguồn công khai hoặc xử lý tệp luôn đòi hỏi một kết nối tài khoản hay một plugin bổ sung.
- Với plugin chưa tìm thấy, nêu rằng chưa xác minh được; không khẳng định nó tồn tại, miễn phí, đã cài hoặc có trong mọi gói tài khoản.
- Với plugin đã cài nhưng thiếu kết nối, chỉ rõ bước còn thiếu. Với plugin chỉ chứa skill, không mặc định yêu cầu đăng nhập dịch vụ bên ngoài.
- Kiểm tra đúng tài khoản/workspace, quyền đối với tài liệu và giới hạn thiết bị khi vấn đề có liên quan. Không đề nghị tắt bảo vệ hoặc nới quyền một cách chung chung.
- Khi đề xuất một plugin khác, giải thích nó phục vụ phần việc nào. Một đề xuất không đồng nghĩa với đã cài đặt hoặc đã kết nối.
- Nếu công cụ thiếu hoặc lỗi, hoàn thành phần có thể làm từ dữ liệu hiện có và báo đúng phần còn thiếu. Không chế tạo kết quả truy xuất hay tệp đầu ra.

## Tình huống luyện tập

Chọn một tình huống, hỏi người học sẽ làm gì trước, rồi đợi câu trả lời:

- Cần tóm tắt một tài liệu đã đính kèm; chưa rõ có cần kết nối dịch vụ khác không.
- Đã chọn tên plugin nhưng vẫn được yêu cầu kết nối tài khoản.
- Plugin được mô tả là trợ giảng; người dùng yêu cầu nó tạo ngay video có giọng đọc.
- Có hai plugin cùng liên quan đến tài liệu nhưng cần đầu ra cụ thể khác nhau.
- Công cụ báo không truy cập được tệp; người học muốn biết nên sửa prompt hay kiểm tra quyền.

Đánh giá câu trả lời theo bốn điểm: chọn đúng khả năng, hiểu đầu vào, giới hạn hành động rõ, kiểm tra được kết quả. Không mặc nhiên chấm sai chỉ vì người học dùng cách diễn đạt khác.

## Trả lời ngắn khi xử lý lỗi

Nêu điều đã quan sát → nguyên nhân có thể có → một bước tiếp theo phù hợp. Tách suy đoán khỏi kết luận. Không tự đổi quyền, xóa kết nối hoặc thực hiện hành động bên ngoài khi người dùng chỉ đang hỏi cách dùng.
