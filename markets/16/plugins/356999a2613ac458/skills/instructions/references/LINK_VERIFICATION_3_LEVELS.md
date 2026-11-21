# Kiểm chứng URL 3 mức — chuẩn dùng cho toàn bộ plugin

- **Chưa kiểm chứng (L0)**: chỉ suy ra/soạn URL, URL có trong ghi nhớ hoặc tài liệu tải lên mà chưa chạy tìm kiếm. Không gọi L1.
- **L1 — Found**: URL xuất hiện trong kết quả truy vấn tìm kiếm có thật. Chỉ được ghi "đã tìm thấy URL"; chưa kiểm chứng nội dung hoặc truy cập.
- **L2 — Retrieved**: công cụ trả về được nội dung thực/đoạn văn của nguồn, chưa mở trực tiếp trang đích trong phiên này. Ghi "đã truy xuất nội dung", chưa xác minh truy cập trực tiếp.
- **L3 — Opened**: đã thực hiện hành động mở trực tiếp URL/trang đích bằng công cụ truy cập, trang tải thành công, tiêu đề/chủ đề đúng và nội dung cần dẫn được đối chiếu. Chỉ L3 được ghi **"đã xác minh truy cập"**.
- Việc browser chuyển hướng phải kiểm tra điểm đến đúng nguồn; trang lỗi, CAPTCHA, access denied, timeout, blank, paywall chỉ thấy abstract thì không xác nhận **truy cập toàn văn**. Một trang metadata/abstract có thể là L3 cho metadata/abstract, KHÔNG là L3 cho full text.
- Kiểm tra link L3 không chứng minh nghiên cứu có chất lượng cao/khuyến cáo đúng với cá nhân, phải bình báo riêng.

## Mẫu nhật ký
| Nguồn & URL | Thời điểm (giờ VN) | Thao tác | Mức | Nội dung xác minh | Giới hạn |
| --- | --- | --- | --- | --- | --- |
| ... | ... | search / retrieve / open | L0–L3 | title/year/claim | abstract/paywall/error |

Tuyệt đối không viện dẫn trạng thái kiểm tra ở phiên trước như chứng cứ L3 **trong phiên hiện tại** nếu người dùng yêu cầu xác minh truy cập hiện tại; có thể nêu lịch sử và thử lại.
