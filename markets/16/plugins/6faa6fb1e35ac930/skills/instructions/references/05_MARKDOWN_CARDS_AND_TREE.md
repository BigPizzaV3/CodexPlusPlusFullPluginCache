# Markdown Cards & Arrows — tương thích Knowledge Pack gốc

Đây là format đặc thù để nhập ứng dụng (không đồng nhất với Mermaid):

```text
Title: Cấu trúc học thuật giả định

# Tập hợp thông tin [#f4c85b] | Start
- Nêu chủ đề
- Kiểm tra tài liệu

# Nhánh lựa chọn [#62b15c] | Choice
- Câu hỏi rõ ràng

# Kết luận học tập [#4aa3df] | Summary
- Điểm cốt lõi

-> Start -> Choice : đánh giá
-> Choice -> Summary : đủ thông tin
```

Bắt đầu chính xác `Title: ...`. Card theo `# Card Title [#RRGGBB] | Key`; `Key` chỉ ASCII không khoảng trắng (ví dụ `Initial`, `RedFlags`, `Reassess`). Dùng `-> Key1 -> Key2 : label`. Màu sắc không phải ý nghĩa duy nhất: mọi nhánh dùng nhãn. Không tự chèn JSON/YAML/JS vào đầu ra nếu người dùng yêu cầu strict cards format.

Nếu user chọn Markdown tree: `# / ## / ###`, nhánh có indentation rõ và `Merge: ...` ở chỗ hợp; không trộn cards format trừ khi cần chuyển đổi.

**Phân biệt:** Markdown cards, Mermaid, YAML, JSON là các ngôn ngữ **khác nhau**. Không bao giờ gắn code fence `mermaid` cho cards-and-arrows, vì renderer Mermaid sẽ không hiểu.
