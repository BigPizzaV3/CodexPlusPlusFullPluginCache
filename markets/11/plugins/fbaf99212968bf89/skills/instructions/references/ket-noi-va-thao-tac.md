# Kết nối và thao tác CAD/BIM

## Kiểm năng lực

Đọc công cụ/schema phiên hiện tại, sau đó kiểm capability có thật. Kiểm riêng kết nối MCP, xác thực CWS, bridge online, host adapter, tài liệu đang mở và quyền hành động. Bắt tay MCP hoặc xem danh mục recipe không chứng minh có thể ghi Revit/SketchUp/Blender.

Không đổi phần mềm hoặc tài liệu để làm cho lệnh thành công. Khi host mục tiêu không có, có thể đề xuất phương án phân tích ngoại tuyến; chỉ chuyển host khi người dùng yêu cầu và runtime mới được xác minh. Không dùng plugin điều khiển máy khác nếu chưa rõ nó là cùng thiết bị/dự án và có quyền phù hợp.

## Đọc và lập kế hoạch

1. Dùng snapshot đúng tài liệu/revision và truy vấn tối thiểu vùng/vật thể cần thiết. Không gửi toàn mô hình hoặc toàn lịch sử hội thoại khi một tập đối tượng nhỏ đủ dùng.
2. Giữ binding do runtime xác nhận: tenant/user, project/device, app/process/session nonce, document ID và revision theo hợp đồng thực tế. Không gửi trường tưởng tượng mà schema không hỗ trợ.
3. Khi lớp thực thi chưa hỗ trợ kiểm binding/revision hoặc kiểm trước ghi cần thiết, giữ thao tác ghi ở trạng thái chưa sẵn sàng. Nêu đúng khả năng thiếu; không dùng hướng dẫn văn bản để thay thế bảo vệ server.
4. Chuẩn bị preview/diff: đối tượng thêm/sửa/xóa, kích thước, quan hệ bị ảnh hưởng, phần phải giữ, kiểm sau sửa và khả năng khôi phục.

## Ghi và lưu

- Thực hiện trong đúng phạm vi người dùng đã yêu cầu/duyệt, tuân thủ quyền và xác nhận của nền tảng. Không lặp xin phép cho các bước đọc hoặc tác vụ thường lệ đã được cho phép. Thay đổi ngoài phạm vi cần được duyệt trước.
- Yêu cầu approval/plan ID có căn cứ từ lớp hỗ trợ khi hợp đồng có chúng. Không tự gán `approved: true`, tạo token duyệt hoặc coi biên bản họp là approval.
- Trước ghi, kiểm revision hiện tại với preview. Thay đổi đồng thời hoặc phiên/tài liệu khác thì đọc lại và cập nhật preview; không ghi đè bằng dữ liệu cũ.
- Không thử lại lệnh ghi không rõ kết quả một cách mù quáng. Tra trạng thái theo job/idempotency key có thật trước để tránh tạo đối tượng trùng.
- Dùng transaction/undo được adapter hỗ trợ; không hứa khôi phục hoàn hảo khi chưa có evidence. Hủy job không đồng nghĩa hoàn tác những gì đã ghi.
- Đọc lại đối tượng và kích thước sau thực thi. Ghi rõ phần đạt, chưa đạt hoặc cần xem lại ở revision mới.
- Transaction commit, thay đổi trong bộ nhớ ứng dụng, lưu file và xuất file là các kết quả riêng. Không nói file đã lưu nếu chỉ có native commit. Không tự lưu mọi chỉnh sửa thủ công đang có trong tài liệu.
- Xuất/lưu cần đúng phạm vi và đường dẫn được phép; xác minh artifact thực tế, loại file, phiên bản và nội dung khi có công cụ. Không ghi đè file khác hoặc gửi file qua dịch vụ ngoài phạm vi.

## Trả lỗi hữu ích

Nêu ngắn điều đang chặn, phần vẫn làm được và một bước khắc phục cụ thể. Chưa có bridge thì không yêu cầu khách tự tìm `CWS_ARCHITECTURE_BRIDGE_URL` hay nhập token vào chat. Không coi setup của nhà phát triển là việc khách phổ thông phải tự cấu hình. Chỉ đưa liên kết cài/ghép nối đã được xác minh, không bịa bộ cài “một chạm”.
