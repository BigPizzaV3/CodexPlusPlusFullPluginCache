# Chuẩn kiểm chứng URL L0–L3 (L123)

## Các mức liên kết — PHẢI phân biệt
| Mức | Định nghĩa | Được phép nói | Không được nói |
|---|---|---|---|
| L0 | Chưa tìm kiếm hoặc chưa có URL xác định. | Chưa xác minh. | Có nguồn, đã truy cập. |
| L1 | Tìm thấy URL trên trang kết quả tìm kiếm, chỉ mục hoặc do người dùng/manifest cung cấp; **chưa truy cập đích**. | Đã xác định URL ứng viên. | Đã mở nguồn; link đang sống. |
| L2 | Công cụ truy xuất được một phần nội dung/snippet/extract, nhưng **chưa xác nhận bằng việc mở trực tiếp đích**. | Đã đọc nội dung qua công cụ trung gian, phạm vi nội dung là ... | Đã xác minh truy cập URL đích (L3). |
| L3 | Đã mở **trực tiếp** URL đích trong phiên kiểm tra, nguồn đúng chủ thể/tài liệu, nội dung hỗ trợ đúng claim. | Đã xác minh nguồn đích và nội dung **trong phần thực sự đọc**. | Đã đọc full text nếu chỉ có abstract/landing page. |

**L3 không đồng nghĩa FULL TEXT.** Ghi đồng thời 2 chiều độc lập: mức liên kết (`L0–L3`) và mức đọc tài liệu (`FULL TEXT ĐÃ ĐỌC`, `ABSTRACT ONLY`, `LANDING PAGE ONLY`, `SECONDARY`, `UNAVAILABLE`).

## Quy trình bắt buộc
1. Tìm nguồn chuyên môn phù hợp (ưu tiên cơ quan ban hành / nghiên cứu gốc); ghi URL nguồn gốc, đơn vị, tiêu đề, năm, phiên bản và phạm vi dân số/cơ quan/thủ thuật.
2. Mở đích, so tên/đường dẫn/phiên bản và nội dung hỗ trợ claim. Phân biệt kết quả tìm kiếm với nội dung tài liệu. Nếu 403/404/CAPTCHA/đích chuyển sai/không mở được => **không cấp L3**.
3. Lập kiểm toán URL: `Tên nguồn | URL | Nội dung thực sự đã xem | L0/L1/L2/L3 | Full text/Abstract/Landing | Ngày kiểm tra | Vướng mắc`.
4. Nếu nguồn đã ở L1/L2, chỉ nêu như nguồn tiềm năng/chưa xác minh, **không** dùng để chống lưng cho khẳng định rằng đã kiểm chứng hay khẳng định chi tiết không được đọc.
5. Không chế URL/DOI/PMID và không đổi nhãn L cấp cho thuận tiện trình bày. Nếu trang mở nhưng chỉ có tóm tắt thì ghi `L3 + ABSTRACT ONLY`.
6. 4 URL pháp lý/ hỗ trợ plugin (website, support, privacy, terms) cũng kiểm tra riêng theo chuẩn này trước khi xin public review. URL có trong manifest không tự đạt L3.

## Ca kiểm thử bắt buộc
- Snippet có title bài báo và DOI: tối đa L2 nếu chưa mở DOI/website gốc.
- Link trang CAP mở được nhưng PDF protocol sau paywall: `L3 + LANDING PAGE ONLY` cho trang CAP, **không** khẳng định đã đọc protocol.
- URL trả 404, 403 hoặc lỗi công cụ: không cấp L3; ghi lỗi thật.
- WHO trang chính thức mở được và đọc nội dung liên quan: L3 cho trang, không mặc định cho mọi link PDF gắn trên trang.
- 4 URL Netlify điền sẵn nhưng truy cập thất bại: giữ URL cấu hình, đánh dấu chưa xác minh; **không** viết 'L3 verified'.
