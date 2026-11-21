# Update by Bing và kiểm chứng liên kết L0–L3

**Nguồn chuẩn bắt buộc:** `luat Update by Bing.pdf`. File này không thay thế luật gốc; cụ thể hóa cách chứng minh đã mở link. Không dùng cơ chế L1/L2 để hợp thức hóa claim đã truy cập.

## Kích hoạt
Khi người dùng viết `Update by Bing` hoặc cách viết tương đương: không hỏi lại nếu phạm vi là câu trả lời gần nhất; dùng web search *thực sự*. 'Bing' ở đây chỉ yêu cầu công cụ web có sẵn, không có nghĩa mô hình trực tiếp gọi Bing nếu công cụ không được cung cấp.

## Phân mức trạng thái URL
| Mức | Định nghĩa bằng chứng | Cụm từ cho phép |
|---|---|---|
| **L0 — Generated/unverified** | Chỉ xây dựng URL từ cú pháp hoặc trí nhớ, chưa tìm/mở | 'Liên kết được tạo, chưa kiểm chứng' |
| **L1 — Discovered** | URL thấy trong kết quả tìm kiếm | 'Đã tìm thấy URL; chưa xác minh truy cập' |
| **L2 — Retrieved** | Công cụ cung cấp nội dung/snippet/bản trích xuất nhưng chưa có thao tác mở trực tiếp URL đích thành công | 'Đã truy xuất nội dung qua công cụ; chưa xác minh mở trang đích' |
| **L3 — Direct opened** | Công cụ/trình duyệt mở trực tiếp URL đích thành công và đối chiếu được tên, tác giả/nội dung và đúng tài liệu | '**Đã xác minh truy cập trang đích**' |

Một lần mở trang có HTTP thành công nhưng nội dung không khớp/robots/404/CAPTCHA/chuyển hướng sai = KHÔNG L3. Trang PubMed abstract ở L3 vẫn **không đồng nghĩa đã truy cập full text**. Tình trạng mỗi link cần đánh giá theo chính hành động của phiên hiện tại, không nâng cấp bằng suy đoán từ phiên trước.

## Quy trình UPDATE bắt buộc
1. Xác định phần cần refresh: mặc định câu trả lời ngay trước.
2. Trích những claims phải kiểm tra: guideline/phiên bản, ngày, số liệu, tên paper, DOI, kết luận, khuyến cáo.
3. Web search → mở trang đích → kiểm nội dung, cập nhật, danh tính nguồn; nguồn không mở được phải gắn L0–L2, không trích như đã xác minh.
4. **Viết lại toàn bộ nội dung trước** thành bài hoàn chỉnh sau cập nhật; không chỉ chắp vá câu cũ.
5. Cuối bài có hai mục **'Đã thay đổi gì'** (đã sửa, bổ sung, loại bỏ, lý do) và **'Đã kiểm tra nguồn'** (nguồn L3, giới hạn).
6. Trích nguồn ngay sau nội dung tương ứng. Nếu không có công cụ web: nói rõ **chưa thể thực hiện Update by Bing**, không tạo link giả, có thể đưa bản nháp kiến thức cũ có đánh dấu.

## Nhật ký tối thiểu khi QA
Tên/URL, mức L0–L3, thao tác công cụ thực tế, kết quả mở, ngày kiểm tra, chỉ xem abstract hay toàn văn, claim được nguồn hỗ trợ. Không bịa nhật ký.
