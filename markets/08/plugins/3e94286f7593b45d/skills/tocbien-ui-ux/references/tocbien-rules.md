# Luật thiết kế Tốc Biến

## Trước khi viết giao diện
- Viết một câu: trang này để khách làm gì. Chưa viết được thì hỏi, đừng xếp layout.
- Hỏi ảnh thật, số máy thật, địa chỉ thật, giá thật. Không bịa. Thiếu ảnh thì khung chữ «Chưa có ảnh» + tên món — không lấy chữ cái to hay emoji làm ảnh hàng.
- Chốt một id kiểu. Dùng đúng prompt + luuY + nangCao của id đó. Đừng trộn nhiều kiểu.
- Dưới 640px: một cột, không cuộn ngang, nút cao ≥ 44px, chữ bài ≥ 16px, chữ/nền ≥ 4.5:1. Lỗi form có chữ, không chỉ đổi màu.
- Trên trang của khách: không nhét thương hiệu hay nút Tốc Biến. Không viết VPS, container, deploy, hạ tầng.

## Cấm trang mặc định (lỗi đã gặp trên trang thật)
- Không mặc định hero xanh Tailwind (#3b82f6 / blue-500) chữ trắng cho mọi phong cách. Dùng màu trong brief đã chọn và đo tương phản thực tế của chữ.
- Không mặc định ba thẻ icon đều nhau rồi một nút giữa trang khi nội dung và brief cần bố cục khác.
- Không mặc định một font cho mọi phong cách hoặc chữ xám #888 thiếu tương phản trên nền trắng. Inter được dùng khi brief chỉ định; không thay font nguồn bằng quy định thẩm mỹ chung.
- Số máy, địa chỉ, giá, lời khen, mã đơn bịa hoặc để trống (ví dụ 0901 234 567, «Mã đơn .»).
- Đưa lên mạng khi 390px còn cuộn ngang, hoặc chữ không đọc được.

## Quy trình áp đặc tả vào dự án

1. Hiểu việc cần làm
Dùng thông tin tôi đã cung cấp: đang nhờ AI làm web nào (landing, trang giới thiệu, portfolio, ý tưởng thành web), cho ai, và hành động chính họ cần làm trên trang. Ngành nghề trong mẫu chỉ là ví dụ, không tự biến dự án của tôi thành ngành đó. Nếu chưa rõ đang làm trang gì và cho ai, hỏi gộp một câu ngắn trước khi dựng. Các chi tiết nhỏ có thể tự chọn hợp lý và ghi rõ giả định.

Nguyên tắc áp dụng đặc tả
Yêu cầu riêng của tôi, dữ liệu thật, chức năng đang có và khả năng truy cập là các ràng buộc ưu tiên. Mã ví dụ, thư viện và ngành minh họa trong đặc tả là tham khảo; chuyển sang công nghệ hiện có để giữ đúng hiệu quả thị giác, không ép đổi framework. Nếu có mâu thuẫn, giải thích ngắn lựa chọn và giữ nét nhận diện của phong cách.
Trước khi viết giao diện, xác định mục tiêu trang, thứ tự nội dung, hành động chính và 3–5 đặc điểm nhận diện lấy trực tiếp từ đặc tả. Lập bộ biến màu, font có dấu tiếng Việt, thang chữ, khoảng cách, đường viền, bo góc, bóng và chuyển động. Chọn bố cục theo nội dung: không mặc định trang nào cũng là hero hai cột rồi ba thẻ giống nhau. Ghi kế hoạch ngắn rồi triển khai, không dừng ở bản mô tả.

4. Nội dung và ảnh
Viết tiếng Việt tự nhiên, cụ thể, tiêu đề nói được lợi ích hoặc việc cần làm. Mỗi màn có một hành động ưu tiên; nút ghi rõ kết quả của thao tác. Chỉ tạo những mục phục vụ nội dung thật, không cố nhồi đủ một công thức. Không bịa giá, số khách, giải thưởng, đánh giá, thông tin liên hệ hoặc cam kết kết quả. Nếu làm bản minh họa khi chưa có dữ liệu, đánh dấu rõ dữ liệu minh họa.
Ưu tiên ảnh tôi cung cấp, đúng sản phẩm và bối cảnh. Nếu cần ảnh mới, nêu chủ thể, góc chụp và tỉ lệ khung; chỉ tạo/tìm ảnh nếu công cụ cho phép. Với ảnh AI, tạo tài sản riêng theo đúng chủ thể, chất liệu, ánh sáng, bảng màu và tỷ lệ của phong cách; không sao chép tác phẩm cụ thể hoặc giả danh người thật. Chân dung chủ dự án phải dùng ảnh người dùng cung cấp; nếu là nhân vật hư cấu thì ghi rõ minh họa. Ảnh bên ngoài phải có nguồn và quyền sử dụng phù hợp, không xem kết quả tìm kiếm là bằng chứng được phép dùng. Lưu ảnh vào dự án, có alt mô tả, kích thước ổn định, định dạng nhẹ và tải trì hoãn cho ảnh dưới màn đầu. Không lấy ảnh chụp cả trang làm nền website. Không thay ảnh nội dung bằng mảng màu hoặc hình học vô nghĩa; minh họa hình học vẫn được dùng khi đó là chủ ý của phong cách. Không để ảnh hỏng; vùng dự phòng có kích thước ổn định và ghi rõ ảnh còn thiếu.

5. Dựng mới hoặc sửa dự án có sẵn
Nếu có mã nguồn, đọc cấu trúc và thành phần hiện tại trước khi sửa. Giữ framework, đường dẫn, dữ liệu, API, đăng nhập, phân quyền, thanh toán, xử lý biểu mẫu và đo lường hiện có. Chỉ điều chỉnh phần trình bày, bố cục trong màn và tương tác cần thiết; không tự xóa chức năng, thay dữ liệu thật bằng dữ liệu giả, hoặc cài thêm thư viện khi không cần. Giữ đúng hành vi của các phần đang hoạt động.
Nếu dựng mới, dùng công nghệ tôi yêu cầu; khi chưa có yêu cầu, chọn cách đơn giản, dễ chạy và dễ sửa. Nút và biểu mẫu phải hoạt động đúng phạm vi: chưa kết nối gửi/đặt lịch/thanh toán thì nói rõ, không báo thành công giả. Với giao diện quản trị, ưu tiên công việc và dữ liệu; không ép thành trang quảng cáo.

6. Dùng tốt trên mọi màn hình
Dùng một bộ biến màu, chữ, khoảng cách và bo góc nhất quán. Thân bài khoảng 16px trở lên; font có đủ dấu tiếng Việt. Chữ thường tương phản tối thiểu 4.5:1; chữ lớn tối thiểu 3:1. Không cắt dấu ở chữ hoa và không ép xuống dòng theo bản máy tính.
Kiểm tra ở 390px, 768px và 1440px: toàn trang không cuộn ngang, chữ không chồng/xén, ảnh giữ đúng tỉ lệ và chủ thể. Trên điện thoại, sắp thứ tự nội dung theo việc chính, chuyển cột phù hợp; menu thu gọn nhưng vẫn truy cập được. Vùng bấm tối thiểu 44px, có focus bàn phím rõ. Bảng hoặc đoạn mã dài chỉ cuộn bên trong vùng riêng khi cần.
Có trạng thái đang tải, trống, lỗi, thành công cho phần có tương tác; lỗi có chữ giải thích và cách làm tiếp. Chuyển động nhẹ, không chặn thao tác, tôn trọng prefers-reduced-motion.

7. Hoàn thiện và kiểm tra
Triển khai đầy đủ trong phạm vi đã rõ, không chỉ đưa ý tưởng. Tự so kết quả với đặc tả phong cách và mẫu nếu xem được. Đối chiếu từng nhóm: bảng màu, font và thang chữ, lưới và khoảng nghỉ, thành phần, ảnh, chuyển động, các dấu hiệu nhận diện bắt buộc và điều cần tránh. Không bỏ nhóm nào một cách im lặng; yêu cầu không phù hợp dự án phải có lý do. Chụp và xem lại màn đầu lẫn các phần còn lại ở ba kích thước đã nêu khi có công cụ trình duyệt; sửa sai lệch trước khi bàn giao. Kiểm tra thêm tiêu đề trang, mô tả, một h1 chính, cấu trúc heading, nhãn biểu mẫu và thông báo lỗi. Thử các nút, liên kết, biểu mẫu và các luồng hiện có bị ảnh hưởng; chạy kiểm tra sẵn có phù hợp. Cuối cùng báo ngắn: đã làm gì, đã kiểm tra gì, phần nào còn thiếu dữ liệu hoặc kết nối thật. Không nói đã kiểm tra nếu chưa thực hiện.
