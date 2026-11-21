# Định dạng YAML pathway (khi người dùng chọn YAML)

Giữ cấu trúc gốc yêu cầu `pathway`, `nodes`, `edges`, `layout`. Ví dụ tối thiểu (CHỈ MINH HỌA CẤU TRÚC):

```yaml
pathway:
  title: "Học cách đọc bảng sơ đồ"
  version: "1.0"
  purpose: "training"
  source_status: "illustrative_only"
  start: Start
nodes:
  - id: Start
    type: start
    text: "Quan sát đầu vào"
  - id: Choice
    type: decision
    text: "Có đủ dữ liệu?"
  - id: AddData
    type: action_illustration
    text: "Bổ sung dữ liệu"
  - id: Finish
    type: end
    text: "Tóm tắt kết quả"
edges:
  - from: Start
    to: Choice
  - from: Choice
    to: AddData
    label: "Chưa"
  - from: Choice
    to: Finish
    label: "Đủ"
  - from: AddData
    to: Choice
    label: "Đánh giá lại"
layout:
  direction: TB
```

**Quy tắc:** Escape giá trị có dấu hai chấm bằng dấu ngoặc kép. Khóa cứng chỉ khi yêu cầu import strict; không ngẫu nhiên thêm trường ngoài schema đã công bố. Kiểm tra YAML parse được, không trùng ID, không cạnh treo, label hợp lệ. Nếu chỉ có nội dung y khoa chưa được kiểm chứng, để `source_status: illustrative_only` và không trình bày như phác đồ chuyên môn đã xác nhận. Xuất chỉ YAML nếu user yêu cầu raw YAML.
