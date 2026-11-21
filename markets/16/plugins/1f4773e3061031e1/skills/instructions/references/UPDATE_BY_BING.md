# Update by Bing — web-backed evidence refresh

## Kích hoạt
Các câu `Update by Bing`, `update by bing`, `cập nhật bằng Bing`, yêu cầu kiểm tra nguồn mới nhất tương đương kích hoạt workflow. “Bing” ở đây là nhãn lệnh của người dùng, **không có nghĩa công cụ thực tế nhất thiết là Bing**; sử dụng công cụ web/search đang khả dụng.

## Chỉ chạy khi có công cụ truy cập
1. Xác định nội dung/câu trả lời cần refresh (mặc định câu trả lời gần nhất cùng chủ đề).
2. Tách các claim cần xác minh: tác giả, năm, version, khuyến cáo, kết quả, DOI/PMID, luật, công cụ.
3. Tìm trực tuyến bằng công cụ thật; mở nguồn chính thức, phân biệt publish date và ngày sự kiện/ngày guideline áp dụng.
4. Với mỗi URL, ghi **L0/L1/L2/L3** theo `LINK_VERIFICATION_3_LEVELS.md`; **chỉ L3 mới ghi đã xác minh truy cập**. Đừng nhầm nguồn xuất hiện trong search, nội dung trả về qua extract và URL mở trực tiếp. Đối chiếu từng claim với độ sâu nội dung thật đã đọc; kiểm tra độc lập khi có tranh luận/mâu thuẫn.
5. Viết lại đáp án, không chỉ thêm link; nêu điểm thay đổi so với câu cũ.
6. Cấu trúc: **Bản cập nhật → Những gì thay đổi → Bảng kiểm chứng nguồn**, ghi URL, L0–L3, phạm vi nội dung, thời điểm và giới hạn; trích dẫn sát claim.

Nếu **không có web** hoặc trang truy cập lỗi, nói rõ chưa thể thực hiện cập nhật trực tuyến; cung cấp chuỗi PubMed/URL nơi tự kiểm tra. Không giả vờ đã mở trang, không dùng trích dẫn dựng sẵn như vừa xác minh, không khẳng định link vẫn hoạt động khi chưa mở trực tiếp đạt L3. Nếu chỉ search được link thì L1; chỉ truy xuất gián tiếp thì L2.

## Đặc thù EBM
- Không coi PubMed search link là nguồn bài báo hoặc bằng chứng hiệu quả điều trị.
- Phân biệt abstract/full-text/guideline phiên bản cập nhật.
- Báo ngày tìm kiếm, phạm vi thời gian và lý do dùng bộ lọc.
- Nếu PubMed và nhà xuất bản khác nhau về ngày xuất bản, tách online-first và print.
- Ưu tiên hệ thống nguồn: NLM PubMed User Guide, Cochrane Handbook, GRADE, EQUATOR, bản guideline gốc.
