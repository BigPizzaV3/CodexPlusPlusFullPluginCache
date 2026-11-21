# Kiểm chứng liên kết L0–L3 và độ sâu tài liệu (hai trục độc lập)

L0 — URL được tạo/copy/nhớ, chưa tìm kiếm và chưa mở: “Liên kết đề xuất, chưa kiểm chứng”.
L1 — URL được thấy trong kết quả tìm kiếm: “Đã tìm thấy URL trong kết quả tìm kiếm; chưa xác minh truy cập”.
L2 — Công cụ truy xuất được một phần nội dung/cache/snippet, nhưng không hoàn thành thao tác mở trực tiếp trang đích: “Đã truy xuất nội dung, chưa xác minh mở trang đích”.
L3 — Đã dùng công cụ mở URL trực tiếp, trang đích trả nội dung liên quan và xác định đúng nguồn: **“Đã xác minh truy cập”**. Không tính trang 403, 404, CAPTCHA, redirect sai, login chặn nội dung, lỗi công cụ. Phải kiểm tra URL cuối nếu redirect.

Trục nội dung:
- METADATA ONLY: tiêu đề, tác giả, năm, DOI, không có kết quả.
- ABSTRACT ONLY: có abstract, không có bài đầy đủ.
- PARTIAL: chỉ có phần nội dung toàn văn rõ ràng.
- FULLTEXT: truy xuất được toàn bộ bài hoặc phần đầy đủ cần đánh giá và có thể kiểm tra methods/tables; tránh tuyên bố fulltext nếu bản PDF thiếu phụ lục cần thiết.

Ví dụ: `L3 / ABSTRACT ONLY` hoàn toàn hợp lệ, nhưng **không được** nói “fulltext đã xác minh”. Link PubMed Clinical Queries được tạo từ mã hóa URL và chưa mở = **L0**. Link tới trang CLSI sản phẩm L3 có thể chỉ đủ xác nhận ấn bản, không đủ để trích breakpoint thuộc nội dung paywall.

Biểu mẫu audit: Ngày | URL cuối | Điều đã mở | L-level | Access level | Claim được hỗ trợ | Giới hạn | Điểm cần cập nhật.
