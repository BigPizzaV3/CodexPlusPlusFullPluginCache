# Hướng dẫn CSV (kế thừa mục tiêu plugin gốc)

## Xuất dữ liệu từ bảng tính
- **Excel:** Chọn sheet cần xuất, File → Save As/Save a Copy → chọn `CSV UTF-8 (Comma delimited)` nếu có. CSV chỉ chứa sheet đang xuất; biểu đồ, định dạng, công thức có thể không được giữ nguyên. Kiểm tra lại dấu thập phân, ngày và ký tự tiếng Việt.
- **Google Sheets:** Mở sheet → File → Download → `Comma-separated values (.csv)`. Tải xuống tập tin và mở bằng trình soạn thảo văn bản để xem nội dung.
- **Text editor:** Dùng 1 hàng tiêu đề, mỗi dòng 1 bản ghi, các cột phân cách dấu phẩy và chuỗi có dấu phẩy được đặt trong dấu ngoặc kép theo chuẩn CSV.

Ví dụ hoàn toàn **GIẢ ĐỊNH**:
```csv
study_id,group,age,score
S001,A,9,14
S002,B,10,18
S003,A,11,16
```
Ví dụ chỉ minh họa cú pháp, không phải dữ liệu người bệnh thực hoặc kết quả nghiên cứu.

## Dán dữ liệu vào ChatGPT
1. Gỡ bỏ cột nhận dạng và các ghi chú tự do chứa thông tin cá nhân.
2. Nếu được hỗ trợ, tải tệp CSV vào chat; nếu không, mở CSV bằng trình soạn thảo rồi sao chép vài dòng đã ẩn danh vào hộp chat.
3. Cho biết mỗi dòng đại diện cho người, lần khám hay lần đo; mô tả đơn vị và cách mã hóa nhóm (A/B, 0/1).
4. Kiểm tra rằng số dòng đã dán chỉ là một phần mẫu nếu không phải toàn bộ bảng; không cho phép suy số liệu toàn nghiên cứu từ ví dụ.

## Vấn đề thường gặp
- CSV với dấu chấm phẩy `;` do cài đặt vùng; dấu phẩy trong số thập phân khiến parser hiểu nhầm cột.
- Chữ Việt bị lỗi encoding; thử UTF-8 và xác minh lại trên bản gốc.
- Dữ liệu quá dài bị cắt khi sao chép; xác định n dòng thực sự đã nhìn thấy.
- ID chứa số 0 đầu cần là chuỗi (`0012`, không phải `12`).
