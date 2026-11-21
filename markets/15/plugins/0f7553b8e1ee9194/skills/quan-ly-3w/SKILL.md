---
name: quan-ly-3w
description: Vận hành nhà trọ 3W từ dữ liệu MCP được cấp quyền, gồm tòa, phòng, khách thuê, hợp đồng, công tơ, hóa đơn, công nợ, đối soát, ZNS và thay đổi có xem trước. Dùng khi người dùng hỏi hoặc yêu cầu thao tác với tài khoản Quản lý 3W; không dùng cho hệ thống nhà trọ khác hay tư vấn chung không cần dữ liệu 3W.
---

# Quản lý 3W

Làm việc qua MCP `https://quanly.3w.com.vn/mcp/marketplace`. Dữ liệu trực tiếp và kiểm tra an toàn của máy chủ là nguồn có thẩm quyền; không đoán ID, tenant, tòa, phòng, hợp đồng, hóa đơn, số tiền hoặc người nhận.

## Thiết lập sau khi cài

Chỉ khi đang thiết lập plugin hoặc người dùng yêu cầu kết nối: dùng luồng đăng nhập của ứng dụng để nối tài khoản 3W và chọn tòa. Nếu kết nối đã hoạt động, giữ nguyên và dùng lại. Sau đăng nhập, gọi `3w_building_list`, báo tên các tòa thực tế được phép xem rồi kết thúc lượt thiết lập. Lượt này chỉ đọc; không tạo dữ liệu hoặc yêu cầu gửi mật khẩu vào chat.

## Thực hiện

- Với yêu cầu chỉ đọc, chọn báo cáo chuyên biệt và đường gọi ngắn nhất. Dùng `billing_readiness` cho trạng thái hóa đơn/chỉ số, `electricity_financials` cho các số tiền điện và `latest_per_room` cho chỉ số gần nhất hoặc bước đầu của nhập/sửa công tơ.
- Xác định duy nhất đối tượng bằng tool `list/get` trong grant. Không dùng tên gần giống hoặc dữ liệu ngoài grant để lấp chỗ trống.
- Với thay đổi, đọc trạng thái hiện tại, dùng `prepare`, đối chiếu bản xem trước rồi `commit` và đọc lại kết quả. Chế độ xác nhận do máy chủ trả về quyết định việc dùng quyền đã cấp hay xác nhận riêng. Không dựng token, giả lập xác nhận hoặc tái dùng approval cũ.
- `confirmation_mode="owner_routine_management"` cho biết thao tác thông thường cụ thể đủ điều kiện dùng quyền chủ tài khoản đã cấp một lần. Commit vẫn kiểm tra quyền tài khoản, tòa và trạng thái dữ liệu. Quyền này không áp dụng cho tài chính, hợp đồng, phân quyền, thông báo hoặc thiết bị.
- Khi máy chủ trả `confirmation_mode="owner_meter_entry"`, chủ tài khoản đã cấp quyền tự lưu chỉ số mới cho kết nối. Sau prepare, thực hiện commit theo đúng yêu cầu nhập chỉ số của người dùng và đọc lại; không yêu cầu bấm widget. Không suy diễn quyền này cho sửa chỉ số, tạo hóa đơn hoặc gửi ZNS.
- Khi máy chủ trả `confirmation_mode="owner_invoice_workflow"`, chủ đã cấp quyền riêng cho lập bill thường kỳ và gửi ZNS lần đầu. Thực hiện commit theo đúng lệnh của người dùng, đọc lại bill và theo dõi operation gửi tới kết quả cuối. Không yêu cầu duyệt lại; không áp dụng cho sửa bill, bill cuối, gửi lại hoặc thu tiền.
- `confirmation_mode="owner_device_relay"` chỉ áp dụng cho quyền điều khiển công tơ đã được chủ cấp riêng; theo dõi tới kết quả và trạng thái thiết bị thực tế. Không mở rộng sang quyền khác.
- Chính sách xin quyền của ứng dụng AI vẫn áp dụng. Skill không tự đổi cài đặt quyền của ứng dụng.
- Kết nối marketplace không thu thập hoặc xử lý số/ảnh giấy tờ định danh hay thông tin đăng nhập của khách thuê. Không yêu cầu người dùng gửi các dữ liệu này vào chat; phần này được thực hiện trực tiếp trên 3W. Dùng các trường liên hệ thông thường mà công cụ thực tế cho phép.
- Với nhập chỉ số công tơ mới, nếu prepare trả `confirmation_mode="user_click_in_widget"`, để người dùng bấm Xác nhận trong widget ChatGPT; widget lưu và trả kết quả. Không yêu cầu duyệt lại trên website và không gọi commit lần nữa. Không gọi tool chỉ dành cho giao diện hay lấy mã xác nhận. Chỉ dùng `confirmation_url` dự phòng khi client không hiển thị widget.
- Nếu commit trả `operation_id`, theo dõi `3w_action_status` tới trạng thái cuối. Không gọi `queued` là hoàn tất. Khi retry, giữ nguyên idempotency key của thao tác để tránh ghi trùng.
- Trạng thái gửi phải phân biệt `processing`, `provider_accepted`, `recipient_confirmed`, `failed`, `not_sent`; kiểm tra trạng thái không được gửi lại.
- Trả lời ngắn bằng tiếng Việt, tên tòa/phòng và kết quả khách cần biết. Dùng múi giờ `Asia/Ho_Chi_Minh`, ngày `dd/MM/yyyy`, giờ 24h và tiền `1,000,000đ`. Không yêu cầu khách hiểu mã công cụ, intent hay JSON. Đặt tên liên kết audit là “Lịch sử thao tác”.

Đọc [references/workflows.md](references/workflows.md) khi yêu cầu liên quan hóa đơn, công tơ, hợp đồng, ảnh bill, ZNS, đối soát hoặc bất kỳ thao tác ghi nào.
