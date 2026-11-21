# Quy trình Quản lý 3W v1.0.3

## Đọc dữ liệu

- Hóa đơn/chỉ số theo tháng: `3w_invoice_list` với `report="billing_readiness"`, `building_query` và kỳ người dùng yêu cầu. Báo trả phòng chỉ đúng khi `checkout_notice=true` hoặc có trong `checkout_notice_rooms`; `end_date` không phải báo trả.
- Tiền điện: `3w_invoice_list` với `report="electricity_financials"`; báo riêng chi phí điện, tiền điện đã lập hóa đơn và tiền điện đã thu.
- Chỉ số gần nhất hoặc chuẩn bị nhập/sửa: `3w_meter_reading_list` với `report="latest_per_room"`; dùng ID thật tool trả về.
- Hóa đơn chi tiết: `report="records"`; kiểm tra kỳ được bao phủ, trạng thái hủy và bản ghi trùng trước khi cộng tổng.
- Ảnh hóa đơn: xác định duy nhất invoice, gọi `3w_invoice_image_export`, hiển thị ảnh thay vì chỉ in URL.
- ZNS: đọc `3w_invoice_get`; không dùng kênh gửi khác để kiểm tra và không gửi thử.
- Đối soát: dùng `bank_reconcile.list/get`; giữ riêng tiền ngân hàng, tiền áp dụng, còn thiếu và tiền thừa. Nội dung chuyển khoản không tự chứng minh hóa đơn đã thanh toán.
- Hồ sơ khách hàng: dùng `customer_profile`, `customer_invoice`, `customer_job`; không gộp người chỉ vì tên hay phòng giống nhau.

## Ghi dữ liệu

1. Đọc trạng thái hiện tại, schema tool và quyền; xác định duy nhất đối tượng, kỳ, số tiền và side effect.
2. Gọi đúng `.prepare`. Preview có thể tạo intent nhưng chưa áp dụng thay đổi nghiệp vụ.
3. Đối chiếu cũ/mới, phép tính, cảnh báo và tác động với yêu cầu. Nếu thao tác chưa được ủy quyền tự động, trình bày bản xem trước và cơ chế xác nhận mà máy chủ trả về.
4. `owner_routine_management` cho phép dùng quyền quản lý thông thường đã được chủ cấp cho thao tác đủ điều kiện. `owner_meter_entry` áp dụng cho chỉ số mới; `owner_invoice_workflow` cho bill thường kỳ và ZNS lần đầu; `owner_device_relay` cho điều khiển công tơ. Chỉ dùng chế độ thực tế trong kết quả prepare, không suy đoán từ lời nhắn; các quyền không thay thế nhau. Với `user_click_in_widget`, người dùng bấm Xác nhận trong widget, sau đó đọc lại; không gọi commit thêm lần nữa. Không tự gọi công cụ xác nhận của giao diện hoặc dùng trình duyệt để duyệt. Nếu không có widget, dùng URL dự phòng. Các thao tác khác giữ cơ chế approval máy chủ. Chính sách xin quyền của ứng dụng AI vẫn áp dụng.
5. Gọi đúng công cụ commit với `intent_id` và `idempotency_key` của thao tác khi quyền tự động phù hợp hoặc xác nhận riêng đã hợp lệ. Khi retry, dùng lại cùng key và kiểm tra trạng thái; không tạo lệnh mới chỉ vì phản hồi chậm.
6. Đọc lại bản ghi; theo dõi `3w_action_status` đến trạng thái cuối nếu có tác vụ nền.

Các thao tác sửa hóa đơn, thu tiền, đối soát, gửi ZNS, kết thúc hợp đồng và điều khiển thiết bị có phạm vi phê duyệt riêng. Không mở rộng một xác nhận hoặc một chế độ ủy quyền sang thao tác khác.

## Trường hợp quan trọng

- Nhập hợp đồng từ ảnh: rà đủ trường bắt buộc; tra phòng, khách và dịch vụ. Phòng tồn tại không có nghĩa đang có người thuê. Không tạo phòng trùng và không coi cọc giữ phòng là tiền hợp đồng đã thu.
- Chỉ số hàng loạt: lấy `latest_per_room`; khi cần, kiểm tra phòng báo trả bằng `billing_readiness`; sau đó tạo một preview gộp. Lịch sử/đơn giá riêng của phòng ưu tiên hơn mặc định tòa.
- Hóa đơn giữa chu kỳ: luôn để `invoice_batch.prepare` kiểm tra. Hóa đơn tiền nhà nhiều tháng không tự chặn dịch vụ tháng mới.
- Sửa và gửi lại bill: sửa và đọc lại trước; gửi ZNS bằng một preview/approval riêng; theo dõi tới trạng thái cuối.
- Dồn công nợ không phải thu tiền. Không biến bút toán nội bộ thành giao dịch tiền.

## Trả lời

Nêu theo thứ tự: kết luận, bằng chứng/số liệu, trạng thái thực hiện, cảnh báo hoặc xác nhận còn thiếu. Không nói “đã xong” khi mới prepare, queued hoặc provider accepted.
