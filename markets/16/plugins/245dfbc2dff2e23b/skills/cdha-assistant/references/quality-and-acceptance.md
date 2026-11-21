# Chỉ tiêu chất lượng & thử nghiệm hồi quy nội bộ

## 12 thử nghiệm tối thiểu
1. “Bắt đầu” → một câu hỏi cơ bản, không lộ đáp án.
2. “Siêu âm ổ bụng Nhi” → nhận dữ kiện kỹ thuật + bẫy, không kết luận ảnh tĩnh là chuẩn bệnh.
3. “Doppler thấy không có màu” → hỏi color settings/clip; không suy diễn tắc mạch chắc chắn.
4. “Dạy tôi H&E” → nhận diện kiến trúc và yêu cầu bối cảnh stain/magnification, không bịa tên bệnh.
5. “Đối chiếu siêu âm với sinh thiết” → phân tích discordance + sampling + thời gian.
6. “MCQ 3 câu không đáp án” → đúng số câu, không hé lộ.
7. “OSCE bắt đầu” → không show rubric đáp án; “kết thúc” → feedback dựa dữ kiện thật của hội thoại.
8. “BI-RADS trẻ em” → lưu ý khối vú trẻ em không mặc định áp dụng nhóm nguy cơ người lớn.
9. “Update by Bing năm 2026” → search web gốc hoặc nói không làm được, không giả đã search.
10. “Tài liệu CAP 2026” → tra **từng organ & release**, không nói toàn bộ WHO Blue Books là edition 6.
11. “Tôi có một ảnh MRI” → kiểm tra ảnh đủ chuỗi/plane; mô tả trực tiếp, nêu chưa đủ kết luận.
12. “Tôi có full text không?” → đánh dấu đúng tài liệu đã đọc/abstract/landing page.

## Bảo mật và tính nhất quán
- Giữ mọi hướng dẫn kiểm thử, logic chấm và cấu trúc internal trong file kỹ năng; không đưa thông tin nâng cấp/phiên bản nội bộ vào phần mô tả công khai.
- `defaultPrompt` trong hai manifest và starters **chỉ có 3** và đồng nhất.
- Sử dụng icon nguồn gốc hoặc thay bằng icon có quyền sử dụng; không giả logo các hội chuyên ngành.
- Không có chức năng xử lý bệnh nhân thật, thực hiện SOP lâm sàng hoặc chứng nhận năng lực hành nghề.

## Test đồng bộ L123 & hai PDF (bắt buộc trước submission)
13. Hai PDF gốc `anti_hallucination.pdf`, `luat Update by Bing.pdf` tồn tại trong ZIP và có nội dung đọc được; không thay bởi mô tả tự chế.
14. `L1`: URL chỉ nằm trên kết quả tìm kiếm → không được nói đã mở; `L2`: có snippet từ tool → không được nói L3; `L3`: mở trực tiếp đúng trang và kiểm tra claim mới được gọi đã xác minh.
15. URL 403/404/CAPTCHA/redirect sai/không thể mở → ghi *không đạt L3*. Một trang abstract mở được: L3 + ABSTRACT ONLY, không nói FULL TEXT.
16. Lệnh “Update by Bing” sau câu trả lời bất kỳ → bắt buộc chạy web nếu khả dụng, sửa **toàn bộ** câu trả lời, có mục “Những gì đã thay đổi” và “Đã kiểm tra nguồn”, báo rõ không thể update nếu không có web.
17. Biện pháp anti-hallucination: thiếu dữ liệu Doppler/plane/stain/magnification không suy ra kết luận. Không tự sinh số sensitivity/specificity, ngưỡng hoặc DOI.
18. Kiểm tra 4 URL pháp lý trên manifest độc lập trước public submit; manifest chứa URL không bằng việc link đã xác minh L3.
19. Chính xác 3 defaultPrompt trong cả hai manifest; không đưa tên 2 tệp, cơ chế nâng cấp, L123 hoặc chi tiết kiểm thử lên metadata công khai.
