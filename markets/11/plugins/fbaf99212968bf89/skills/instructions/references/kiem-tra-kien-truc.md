# Kiểm thiết kế theo hệ công trình

Kiểm để giúp kiến trúc sư quyết định và sửa; đây không phải bộ tiêu chuẩn cấp phép. Bắt đầu bằng nhu cầu, đất, hiện trạng và điều phải giữ. Khi chỉ có concept, phân biệt rõ phạm vi concept với hồ sơ thi công; không bắt khách hoàn thành mọi thông tin để xem một phương án.

## Thứ tự ưu tiên

An toàn/phạm vi → công năng và logic → số đo/nhất quán → hình học → hình ảnh → tốc độ. Mỗi issue: vị trí/ID, triệu chứng, phép đo hoặc bằng chứng, nguyên nhân đã xác minh hay giả thuyết, đề xuất và hạng mục cần kiểm lại. Ưu tiên ba điểm có tác động lớn trước.

| Hạng mục | Kiểm thực dụng |
| --- | --- |
| Brief/khu đất | Đủ phòng/người dùng, ranh/tiếp cận/cao độ; số đo nguồn nào, ràng buộc nào đã khóa |
| Diện tích | Trục/phủ bì/thông thủy; tường/void/shaft và phòng lồng; không cộng rectangle trùng |
| Giao thông | Liên thông, đoạn hẹp, vật cản, ngưỡng và thay cao độ; graph đơn thuần không là kiểm bề rộng |
| Cửa | Lọt lòng, khuôn/lá/tay nắm, phía mở, vùng quét toàn hành trình, cửa–cửa và cửa–đồ; cửa ngoài cũng phải kiểm |
| Cửa sổ | Lỗ thật, sill/lintel, vùng mở, tủ/hood che; diện tích kính không đồng nghĩa thông gió |
| Nội thất | Vùng đứng/ngồi/kéo ghế/mở tủ/đi quanh giường và lối bảo trì theo đồ thật |
| Bếp/WC | Hướng dùng thiết bị, khô–ướt, cửa, thao tác, hút/thoát; không đặt thiết bị chồng đường đi |
| Cầu thang | Số bậc/cao-rộng bậc/landing/headroom/lan can, đầu–cuối đúng sàn; yêu cầu theo công trình cụ thể |
| Mối nối | Tường–sàn/cột–dầm/dầm–mái/bậc–landing: kiểm mặt cắt/solid sau modifier; gần nhau không là liên kết chịu lực |
| Mái/thoát nước | Pitch/valley/gutter/downpipe/điểm xả, mối nối/mặt dưới; giao hình không chứng minh kín nước |
| Trần/MEP | Headroom, dầm/ống/đèn, khoảng bảo trì, phối hợp không gian; không dựng ống giả cho đẹp |
| Kết cấu | Đường truyền tải/nhịp/móng/tính toán chuyên môn; thiếu dữ liệu giữ UNKNOWN |
| Ánh sáng/thông gió | Hướng nguồn có thật, che chắn và lối khí; mô tả ý đồ riêng với kết quả mô phỏng |
| Quy chuẩn/tiêu chuẩn | Nguồn chính thức, hiệu lực, địa điểm, loại công trình và phạm vi; không tự dùng ngưỡng ví dụ như luật |
| Bản vẽ/schedules | Cùng IDs/units/revision: mặt bằng, mặt đứng, mặt cắt, diện tích và cửa thống nhất |
| Render/bàn giao | Clay/ortho/section trước ảnh đẹp; engine/preset thật, mở lại file/texture/font/link |

## Phạm vi và số đo

Chỉ đánh PASS cho phép kiểm thực đã chạy trong coverage. Tách threshold yêu cầu khách/dự án, ngưỡng tiêu chuẩn đã xác minh và dung sai số học. Số đo bbox là broad phase; object không nhãn/không được kiểm phải hiện trong coverage, không biến mất khỏi báo cáo.

Nếu không có công cụ đọc native/evaluated mesh, tiếp tục đánh giá brief, ảnh hoặc spec trong phạm vi đó. Không nói đã kiểm va chạm toàn mô hình, kết cấu, PCCC hoặc xin phép. Thông tin thiếu ở một hệ không chặn các phần độc lập.

Phong thủy/Lỗ Ban theo reference riêng, mặc định tắt và không ghi đè các mục an toàn/công năng. Không yêu cầu người dùng phổ thông tự chọn trường phái/bảng/chu kỳ. Không thêm lời hứa tài lộc hay bảng cung chưa thẩm định.
