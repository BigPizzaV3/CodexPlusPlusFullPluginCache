# Kiểm chứng và chống ảo — vận hành

## Nhãn mức độ chắc chắn
- **Đã xác minh**: nêu nguồn gốc rõ, nguồn hỗ trợ đúng claim, còn hiệu lực đối với ngữ cảnh.
- **Suy luận/ước tính**: mô tả giả định, khoảng và yếu tố làm thay đổi kết quả.
- **Chưa xác minh**: thiếu dữ liệu, nguồn hoặc tra cứu. Không biến thành kết luận.
Không gắn phần trăm tự tạo cho sự tự tin của mô hình; ưu tiên mô tả loại bằng chứng và giới hạn.

## Kiểm tra dữ kiện dinh dưỡng
1. Phân biệt food composition database, nhãn bao bì, kết quả phân tích trực tiếp, dữ liệu do người dùng nhập.
2. Mỗi phép tính có nguồn và trọng lượng khả thực (edible portion, grams, raw/cooked). Soát kcal↔kJ (1 kcal ≈4.184 kJ), nhưng không tự đảo đơn vị khác khi thiếu cơ sở.
3. Không khẳng định thiếu vi chất hay năng lượng từ một ngày ăn; chỉ nói khả năng cần đánh giá thêm.
4. Tuổi, giới, tình trạng tăng trưởng, bệnh lý, hoạt động, hấp thu, thuốc, và giai đoạn bệnh khiến nhu cầu thay đổi; không gán giá trị mặc định như đơn cá thể.
5. Đối với bài báo, kiểm tra thứ tự: tên/DOI/PMID → thiết kế → dân số → outcome → effect size & CI → bias → applicability. Không suy từ abstract sang nội dung full-text không thấy.
6. Có kiểm tra lỗi số như ngược liều, đổi 5/50, kJ/kcal, mg/µg, phần trăm/nồng độ, nhóm can thiệp/chứng, tử số/mẫu số.
7. Nếu nguồn mâu thuẫn, nêu khác biệt về dân số, thời điểm, mục tiêu, định nghĩa, phương pháp; kết luận thận trọng.

## Mẫu báo cáo ngắn
- Dữ kiện xác minh: ... (nguồn/phiên bản)
- Ước lượng và giả định: ...
- Dữ kiện còn thiếu: ...
- Mức độ áp dụng: chung / học thuật / ca giả định; cần đánh giá trực tiếp khi lâm sàng.

## Về hai PDF di sản
`anti_hallucination.pdf` là nguyên tắc nền; không dùng ngưỡng '80%' như một phép đo xác suất tin cậy thực nghiệm. Nếu không chắc, giải thích nguồn bất định thay vì trình bày độ chính xác giả.
