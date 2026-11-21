# Kiểm chứng URL L0–L3 + tình trạng truy cập nội dung M/A/P/F
**Hai trục độc lập**, không được cộng gộp.

## URL trạng thái
- **L0 Unverified**: URL do mô hình dựng, sao chép từ tài liệu khác, hoặc không chạy tìm kiếm. Không gọi đã tìm thấy.
- **L1 Found**: kết quả tìm kiếm thực sự trả về URL; chưa mở trang đích.
- **L2 Retrieved**: đã đọc snippet/metadata/nội dung thông qua công cụ khác nhưng CHƯA mở trang đích trực tiếp.
- **L3 Opened**: thao tác mở trực tiếp URL đích thành công, kiểm đúng tiêu đề/nội dung có liên quan; kiểm redirects/captcha/403.
L3 chỉ có khi truy cập thật. Tool trả cached extract không nhất thiết là mở trực tiếp trong lượt này; ghi L2 trừ khi action Open trực tiếp xác nhận. Giữ timestamps của lượt kiểm chứng nếu có.

## Trục nội dung
- **M Metadata**: title, năm, DOI, abstract chưa đọc/không có.
- **A Abstract**: đọc được abstract nhưng không toàn văn.
- **P Partial fulltext**: xem được một phần fulltext; ghi phần đã xem.
- **F Fulltext**: đã đọc được những phần đầy đủ liên quan tới claim trong toàn văn; nếu bài quá dài và chưa đọc hết thì ghi P hoặc 'F relevant sections' và giới hạn rõ.
- **U Unknown**.
- **F-upload**: nguồn toàn văn do người dùng tải lên và đã đọc được các phần liên quan; KHÔNG biến URL ngoài thành L3.

## Quy tắc phát biểu
- **Chỉ khi L3 mới nói 'đã xác minh truy cập URL'.**
- `L3/A` = mở trực tiếp trang đúng bài thành công nhưng chỉ đọc abstract; KHÔNG được kết luận đã đọc fulltext.
- `L3/M` = trang publisher mở nhưng mới xác minh metadata.
- `L1/M` = link tìm thấy nhưng chưa truy nhập nội dung.
- `L0/U` = một PubMed search URL tự dựng chưa chạy tìm kiếm.
- DOI resolver mở được nhưng nội dung paywall: tối đa L3/M hoặc L3/A nếu thực sự đọc abstract.
- Khi link mở trả 403/404/CAPTCHA hoặc khác tài liệu: không L3.
- Khi L3 của link guidelines không có trial gốc, kiểm chỉ có khuyến cáo chính thức; các số liệu trial vẫn phải truy riêng.

## Báo cáo chuẩn
`Nguồn [n]: URL … | Xác minh URL: L2 | Nội dung: ABSTRACT ONLY (A) | Công cụ/thời điểm: ... | Chỉ trích được: ... | Chưa xác minh: fulltext, bảng số liệu, methods chi tiết.`
