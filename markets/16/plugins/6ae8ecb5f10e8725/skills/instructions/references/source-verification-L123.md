# Protocol kiểm chứng nguồn và Update by Bing — L1/L2/L3

Giữ nguyên và ưu tiên áp dụng `anti_hallucination.pdf`, `luat Update by Bing.pdf` trong cùng thư mục. Phần này hướng dẫn thi hành thực tế; không thay thế 2 PDF gốc.

## Hai trục xác minh độc lập
**Độ mở link:**
- L0: URL người dùng nêu nhưng chưa được kiểm tra, hoặc chỉ suy đoán.
- L1: Tên/URL xuất hiện trong kết quả tìm kiếm hoặc metadata; CHƯA đọc nội dung nguồn.
- L2: Có snippet/abstract hoặc nội dung trích từ kết quả/nguồn thứ cấp, chưa trực tiếp mở được trang mục tiêu.
- L3: Đã mở trực tiếp trang nguồn bằng công cụ và đối chiếu phát biểu liên quan. Mở thành công không tự chứng minh nội dung có full text.

**Mức truy cập:** Full text / một phần văn bản / abstract-only / metadata-only / inaccessible. Không được nâng abstract-only thành full text. Với PDF cần kiểm tra văn bản/hình khi phù hợp.

**Quy trình:** tách claim -> tìm trang tổ chức chính thức/tài liệu gốc -> mở trang -> tìm đúng nội dung -> ghi tên + năm/phiên bản + đối tượng -> so sánh -> kết luận có mức chắc chắn và giới hạn. Không đặt PMID, DOI, năm hay tiêu đề nếu chưa thấy trên nguồn. Nếu bài đã được cập nhật, không dùng cached snippet làm dữ liệu mới.

## Khi người dùng yêu cầu Update by Bing
1. Nhận diện phạm vi là câu trả lời gần nhất, trừ khi người dùng chỉ định phần khác.
2. Dùng search hiện có, không tự nhận đang dùng engine Bing.
3. Xác minh nguồn trực tiếp; ghi nguyên nhân nếu không mở được.
4. Viết lại toàn bộ bản đã được kiểm chứng, không chỉ thêm câu 'đã cập nhật'.
5. Thêm 'Những gì đã thay đổi' và cuối cùng 'Đã kiểm tra nguồn' với URL L3 thực sự dùng.
6. Không có web -> công khai giới hạn, không ngụy tạo xác nhận.

**Mẫu dòng source audit nội bộ:** Claim | nguồn | URL | publication/version | truy cập ngày | URL L# | access full/abstract/... | thông tin đối chiếu | confidence.
