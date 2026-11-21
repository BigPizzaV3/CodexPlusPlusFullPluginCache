# Kiểm tra logic đồ thị / graph integrity

## Mỗi biểu đồ nhánh phải đáp ứng
- `id` node là duy nhất, ASCII an toàn (`^[A-Za-z][A-Za-z0-9_]*$`) trong YAML/JSON; Markdown-card `Key` không có khoảng trắng.
- Bất cứ cạnh `from/to` nào đều trỏ đến node đã tồn tại; không có mồ côi trừ nhánh được ghi chú intentionally optional.
- Nếu có nút bắt đầu (`start`) thì duy nhất, có đường đi đến các nhánh hoặc nút kết thúc; không dùng start làm điểm merge.
- Decision hai nhánh phải có nhãn phân biệt như Có/Không hoặc Dương tính/Âm tính, điều kiện đủ; không đảo logic phủ định.
- Branch và merge được thể hiện tường minh; không phát sinh đường điều trị sai do nhập nhằng cấu trúc.
- Loop chỉ xuất hiện nếu có điều kiện dừng và điểm tái đánh giá.
- Giữ đồng nhất cặp ngưỡng/đơn vị, mức độ tuổi, dương/âm, trước/sau, mg/mL/mg/kg.
- Các node không nằm trong đường đi phải được liệt kê là “bước tùy chọn”, không đánh lừa là thực hành thường quy.
- Nếu phương pháp thay đổi theo guideline/năm/địa phương, ghi rõ thời điểm/đối tượng và tiêu chuẩn đang được dùng.

## Audit cấp độ khuyến cáo
Mỗi nút có vai trò `fact`, `question`, `decision`, `action_illustration`, `reassessment`, `source_note`, `end`. Bản flow giáo dục cần bộc lộ giả định và điểm chưa chắc chắn; không tự tạo lưu đồ chỉ định lâm sàng từ một infographic thứ cấp.
