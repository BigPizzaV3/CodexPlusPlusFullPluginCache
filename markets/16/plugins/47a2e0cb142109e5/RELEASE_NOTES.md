# Release Notes — Thực Hành Nội - Nhi - Tim mạch 0.14.1

## Thay đổi so với 0.14.0
- Chỉ thay Conversation Starter số 3 thành: “Tìm y văn Vai trò Octreotide trong xuất huyết tiêu hóa”.
- Giữ nguyên Starter số 1–2, nội dung Skill, biểu tượng, PDF references, 4 URL và package ID.
- Không xóa hoặc thay đổi chức năng phân loại tổng quan y văn và PubMed Clinical Queries.
- Đây là bản cấu hình để upload và kiểm thử, chưa tự submit.

## Lịch sử bản 0.14.0

## So với 0.13.1
- Xóa toàn bộ câu tặng/nhắc đến đơn vị nhận trong metadata public; mô tả trung lập, không hàm ý tài trợ hay liên kết tổ chức.
- Giữ nguyên package id gốc, biểu tượng và hai PDF nguồn (kiểm tra checksum SHA-256 ở báo cáo QA).
- Bổ sung 4 URL HLP Plugin Hub: Website, Support, Privacy Policy, Terms of Service.
- Nâng cấp dạy học nội khoa, nhi khoa, tim mạch, ECG/echo, suy luận, MCQ và OSCE.
- Bảo tồn phân loại review y văn và PubMed Clinical Queries 10 link (5 categories × 2 scope).
- Bổ sung 5 reference Markdown thực hành: lâm sàng/ECG, review/PubMed, đánh giá, chống ảo chuyên ngành, Update by Bing.
- Chuyển mọi cập nhật và trích dẫn động sang quy tắc có công cụ: không ngụ ý có web nếu phiên dùng không cấp.
- Siết bảo mật bệnh nhân và phân biệt giáo dục mô phỏng với xử trí bệnh nhân thật.
- Không thêm cờ Public/Free/Paid không bắt buộc; anh tự submit.

## Giới hạn kiểm thử
Kiểm tra ZIP/manifest/YAML/đường dẫn/reference/PDF ở môi trường build không chứng minh đã pass review hoặc vận hành đúng trên Portal. Bốn URL HLP được đặt theo URL đã sử dụng từ các plugin HLP trước; cần xác nhận trực tiếp bằng trình duyệt người dùng.
