# Diễn giải tài liệu gốc và quy tắc ưu tiên định dạng

Giữ nguyên byte của `HLP_Medical_Visual_Assistant_Knowledge_Pack.docx`. Tài liệu gốc có một số đoạn hướng dẫn **raw cards format** (“chỉ xuất format, không giải thích, không code fence”) và ví dụ YAML/JavaScript. Chúng là **mẫu cho đầu ra chuyên biệt**, không phải mệnh lệnh bắt buộc cho mọi tương tác.

Quy tắc:
1. User yêu cầu format raw từ Knowledge Pack → tuân theo tuyệt đối format đó (ví dụ Markdown cards `Title: ...`), không thêm code fence.
2. User yêu cầu Mermaid/YAML/JSON/JS → dùng tiêu chuẩn riêng tại `04`, `06`, `07` thay vì áp các giới hạn cards.
3. User cần PNG/hình minh họa/video → tạo media thật khi được hỗ trợ; đừng ép kết quả thành cards.
4. User muốn giải thích/luyện học → có thể giải thích, nguồn, cảnh báo và hỏi học viên; không bị khóa bởi lệnh “không giải thích” trong template import.
5. Khi hai tài liệu mâu thuẫn, ưu tiên yêu cầu hiện tại và tiêu chuẩn kỹ thuật + tính chính xác từ SKILL.md; không áp dụng cấu trúc giả định cho mọi loại hình.
