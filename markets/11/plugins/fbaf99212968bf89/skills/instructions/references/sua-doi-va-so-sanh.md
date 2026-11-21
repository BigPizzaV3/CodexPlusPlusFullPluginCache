# Sửa đúng ý và so sánh được

## Một baseline cho mỗi lượt so sánh

Giữ nguồn và revision gốc, IDs không gian/đối tượng, mục tiêu, điều khóa, phần được sửa và tiêu chí kết quả. Dữ liệu khách đã chốt dùng tiếp, không hỏi lại. Nếu không có baseline/snapshot, nêu chưa có đối chứng; không tự suy trạng thái file cũ từ ảnh mới.

Làm 2–3 phương án chỉ khi có khác biệt đáng kể, ví dụ giữ nguyên hệ kỹ thuật, ưu tiên diện tích dùng, hoặc ưu tiên ít sửa hiện trạng. Cùng đơn vị/diện tích gốc/phạm vi đo. Bảng chỉ gồm số thực đo/tính, lợi ích, đánh đổi và phần chưa kiểm. Không tự cho điểm tổng bằng trọng số chưa được khách chấp nhận.

Chi phí dùng khối lượng/phạm vi/đơn giá có vùng và thời điểm; chưa có thì trình tác động định tính hoặc khoảng có nguồn, không bịa ngân sách để phương án được chọn. Không tối ưu diện tích bằng bỏ lối đi, tường, shaft hoặc phần bắt buộc.

## Khóa và diff

- Khóa đến từ baseline/quyết định thật. Mục bị khóa không đổi khi khách chỉ yêu cầu sửa khu khác. Phương án vi phạm được nêu riêng để khách quyết định, không ngầm mở khóa.
- Executor mặt bằng có `--baseline` kiểm fields đã khóa; kết quả là so spec 2D, không phải khóa thực thi trên CAD/server. Client gửi approved:true không chứng minh quyền.
- Diff gồm thêm/xóa/đổi và thay đổi kéo theo. Ghép A+B tạo candidate mới và kiểm lại, không lấy hai kết quả cũ làm evidence cho tổ hợp.

| Khi thay | Phần cần kiểm lại |
| --- | --- |
| Cửa/lỗ mở | Tường hosted, khuôn/lintel, vùng quét, đồ/lối đi, elevation và schedule |
| Tường/phòng | Diện tích, cửa/đồ, giao thông, ánh sáng/thông gió, MEP và bản vẽ |
| Cầu thang/cao độ | Sàn/bậc/landing/headroom, cột/trần/cửa/mái, giao thông và mặt cắt |
| Bếp/WC/thiết bị | Vùng dùng, cửa tủ, nguồn cấp/thoát/hút, bảo trì và vật liệu |
| Mái/trần | Mối nối, thoát nước/điểm xả, MEP, cao độ, render view và hồ sơ |

## Vòng sửa có evidence

Đọc hiện trạng → chỉ ra lỗi/vị trí → root cause hoặc giả thuyết → preview phạm vi sửa → áp dụng khi được phép trên đúng revision → đọc lại/đo lại → save/export theo quyền. Revision đổi giữa preview và ghi thì lấy lại snapshot/preview, không dùng approval cũ.

Ghi quyết định ngắn: chọn gì, vì sao, theo nguồn nào, thay quyết định nào. Chỉ lưu bền vững qua tính năng có thật và consent phù hợp. Không gọi việc tạo report cục bộ là đã huấn luyện model hoặc nhớ mãi cho mọi khách.
