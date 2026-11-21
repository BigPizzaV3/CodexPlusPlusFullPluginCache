# Vận hành Update by Bing — đi kèm `luat Update by Bing.pdf` gốc

Nguồn quy tắc bắt buộc: `luat Update by Bing.pdf` (bản PDF nguyên gốc trong cùng thư mục). Đây là mô tả thực thi, không thay thế tệp gốc.

## Kích hoạt
Người dùng ghi “Update by Bing” (không phân biệt chữ hoa/thường, hoặc biến thể rõ ràng) => bắt buộc sử dụng **công cụ web search khả dụng**. Không tự xưng đã dùng Bing nếu chỉ dùng công cụ tìm kiếm khác.

**Phạm vi mặc định**: rà soát và **viết lại đầy đủ câu trả lời gần nhất** trong cùng cuộc trò chuyện. Nếu người dùng chỉ định chủ đề/tài liệu khác, cập nhật đúng phần được chỉ định. Không hỏi lại nếu phạm vi rõ.

## Chu trình
1. Tách các mệnh đề kiểm chứng (năm, phiên bản guideline, mức khuyến cáo, ngưỡng, sensitivity/specificity, bệnh cảnh Nhi/người lớn, cách đọc siêu âm/CT/MRI/GPB).
2. Tìm web nguồn chính thức hoặc nghiên cứu gốc, xác minh tài liệu phù hợp chuyên ngành. Khi có PMID/DOI, đối chiếu tiêu đề, tác giả, năm; không tự phát minh link.
3. **Mở trực tiếp link đích**, đối chiếu thực tế và ghi L0/L1/L2/L3 theo `LINK_VERIFICATION_3_LEVELS.md`. Trang lỗi/không mở được **không đạt L3**. Nếu chỉ có abstract: `L3 + ABSTRACT ONLY`; không gán nhãn full text.
4. Đối chiếu mâu thuẫn, cũ/mới, sai biệt Nhi–người lớn hoặc ACR–AIUM–CAP–WHO/IARC. Không dùng nguồn thứ cấp chống lưng cho khẳng định không hiện trong nguồn.
5. **Viết lại toàn bộ câu trả lời cập nhật**, với trích nguồn sát claim. Kết thúc bằng đúng hai mục:
   - `Những gì đã thay đổi`: sửa điểm nào, vì sao, hoặc không phát hiện thay đổi.
   - `Đã kiểm tra nguồn`: URL gốc; L-level; mức truy cập full text/abstract/landing; ngày kiểm tra.
6. Nếu không thể dùng web hoặc không có nguồn L3 phù hợp: **không tuyên bố đã Update by Bing thành công**. Nêu rõ phần chưa được kiểm chứng, có thể trình bày phần kiến thức nền đáng tin cậy đã biết nhưng gắn đúng giới hạn.

## Quy tắc chất lượng tối thiểu
- Không chỉ bổ sung danh mục link vào bản cũ, không đổi tiêu đề mà giữ nguyên phần lỗi thời; sửa toàn bộ nội dung trong phạm vi yêu cầu.
- Không chép dài văn bản sở hữu bản quyền; viết diễn giải có nguồn.
- Không nói “mới nhất” nếu chưa kiểm tra trang cơ quan ban hành và ngày, phiên bản tương ứng.
- Nguồn có L3 nhưng chỉ landing page không chứng minh nội dung trả phí, tables, appendix.
- Cập nhật về GPB phải kiểm tra đúng tập WHO Classification và đúng CAP protocol/organ/version; siêu âm phải so thông số với tài liệu AIUM có liên quan, không suy diễn ngưỡng.
