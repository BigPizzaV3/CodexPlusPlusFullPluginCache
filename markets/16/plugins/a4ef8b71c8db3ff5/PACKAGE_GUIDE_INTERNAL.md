# Học Luật v1.0.0 — thông tin dành cho chủ sở hữu

Gói này chứa **đúng ba Skills** và không có MCP:

- `legal-english`: Anh văn pháp lý, biên dịch Anh–Việt/Việt–Anh, thuật ngữ và luyện tập.
- `legal-reading`: đọc giáo trình, sách luật, văn bản pháp luật, bài báo và bản án.
- `law-tutor`: Socratic, cổ điển, IRAC/CREAC, vấn đáp, phản hồi và đánh giá.

Các câu hỏi mẫu trong plugin.json có thể được dùng thử trong Plugin Preview. Các hướng dẫn an toàn và chống ảo là cấu hình nội bộ, **không được đưa vào phần giới thiệu công khai**.

## Quy định về nguồn

Không xem bất kỳ URL nào là bằng chứng điều luật hiện hành nếu chưa đọc trực tiếp điều khoản và kiểm tra sửa đổi, hiệu lực. Ưu tiên VBPL, Pháp điển, Công báo, nguồn gốc thực tế phù hợp với jurisdiction.

## Cấu trúc

`plugin.json` ở root, `skills/<skill-name>/SKILL.md` ở ba thư mục con ngay dưới skills/, `assets/gpt-icon.png` là icon ứng dụng. `agents/openai.yaml` dưới mỗi skill tùy chọn.
