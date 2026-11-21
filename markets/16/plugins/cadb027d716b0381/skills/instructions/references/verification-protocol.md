# Kiểm soát ảo giác và provenance

## Nhãn kiểm chứng bắt buộc khi làm việc với nguồn
- **Đã đọc trong tài liệu người dùng**: chỉ khẳng định nội dung trích đúng phần hiện có, kèm trang/vị trí nếu truy xuất được.
- **Đã xác minh online**: đã tìm, mở, đối chiếu nguồn gốc và kiểm tra tính phù hợp với claim.
- **Chỉ thấy metadata/abstract**: không khẳng định kết quả mà abstract không cung cấp; không đồng nhất với fulltext.
- **Chưa xác minh**: không tạo PMID, DOI, link, tên tác giả, năm hoặc diễn giải định lượng.

## Kiểm tra trước đầu ra
- Đúng số liệu, số thập phân, đơn vị, mẫu số n/N, thời điểm, nhóm và hướng hiệu ứng?
- Tên study, tác giả, tạp chí, năm, DOI/PMID có trùng với nguồn thật được mở?
- Claim có thực sự được nguồn hỗ trợ, hay chỉ là suy diễn? Có nguồn thứ cấp nào bị nhầm nguồn gốc?
- Có nhầm tỷ lệ % với điểm phần trăm, OR với RR/HR, significance với magnitude, CI với SD?
- Dữ liệu từ bảng/biểu đồ được đọc chính xác hay chỉ ước lượng từ ảnh?
- Một con số không có trong file => dùng `[chưa có dữ liệu]`, không tự điền.

Đọc kèm PDF gốc: `anti_hallucination.pdf` và `luat Update by Bing.pdf`.
