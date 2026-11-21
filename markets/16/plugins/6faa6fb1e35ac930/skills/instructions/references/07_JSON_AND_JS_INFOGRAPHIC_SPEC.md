# JSON cấu trúc, JS flow object — render-friendly, không chạy code tùy ý

**Ưu tiên JSON data object** (ngay cả khi user gọi “JavaScript infographic object”), trừ khi người dùng yêu cầu module/export JS. JSON hợp lệ, key đặt trong nháy kép, không comment, không trailing commas, không dùng `eval`, `Function`, script từ tài liệu nguồn, URL tùy tiện, hoặc nội dung điều khiển.

```json
{
  "title": "Sơ đồ ôn tập giả định",
  "purpose": "education",
  "nodes": [
    {"id": "Start", "type": "start", "text": "Bắt đầu"},
    {"id": "EndNode", "type": "end", "text": "Tóm tắt"}
  ],
  "edges": [{"from": "Start", "to": "EndNode", "label": "tiếp tục"}],
  "layout": {"direction": "TB"}
}
```

Khuyến nghị các loại node: `start`, `fact`, `decision`, `action_illustration`, `reassessment`, `merge`, `end`. Nếu endpoint của app có schema nghiêm ngặt, ưu tiên schema do user cung cấp hơn ví dụ này. `nodes[].id` unique; edge endpoints hợp lệ; nội dung thuần data; không hiển thị API key hoặc đường dẫn nội bộ.

Yêu cầu “chỉ JSON” → không thêm lời giải thích/chú giải/markdown code fence; đưa nguồn vào trường `sources` nếu schema cho phép. Khi không có nơi gắn nguồn, cung cấp bảng provenance riêng **chỉ khi user cho phép ngoài raw format**, còn không thì hỏi rõ nếu nguồn bắt buộc.
