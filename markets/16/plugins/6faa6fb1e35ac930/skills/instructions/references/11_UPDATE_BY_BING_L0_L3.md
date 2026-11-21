# Luật Update by Bing — cập nhật nguồn và viết lại câu trả lời

Khi người dùng nói “Update by Bing”, “cập nhật bằng Bing”, “kiểm tra nguồn” hay yêu cầu cập nhật mới: phải **tìm kiếm web thực sự** bằng công cụ có sẵn (không nhất thiết công cụ mang nhãn Bing), mở trang gốc phù hợp, kiểm tra phiên bản/ngày, và **viết lại toàn bộ câu trả lời/sơ đồ** dựa trên thông tin kiểm tra được. Giữ nguyên định dạng sơ đồ và sửa các node bị ảnh hưởng; đừng chỉ đính chính 1–2 dòng rồi giữ sơ đồ cũ. Nếu không có web, nói thẳng chưa thể Update by Bing.

Trình bày:
1. **Bản cập nhật** — toàn bộ nội dung và sơ đồ mới, trích nguồn trực tiếp tại node liên quan nếu định dạng cho phép.
2. **Thay đổi so với bản trước** — từng điểm thay đổi được chứng thực; nếu không có thay đổi xác nhận được, nêu thế.
3. **Đã kiểm tra nguồn** — nguồn nào đã mở, phiên bản/ngày nếu có, mức chứng cứ/giới hạn.

Mức link: L0 chưa kiểm chứng thực tế; L1 xuất hiện trong kết quả tìm kiếm; L2 nội dung truy hồi được nhưng URL đích chưa mở trực tiếp thành công; L3 đã mở thành công URL đích và xác nhận đúng trang. **Chỉ L3 được nói đã xác minh truy cập**. Độ sâu tài liệu độc lập: `M = metadata`, `A = abstract`, `P = partial text`, `F = fulltext relevant sections`. `L3/A` vẫn là ABSTRACT ONLY. Không suy diễn nguồn chỉ dựa vào snippet.

Nếu phải xuất raw YAML/JSON theo schema app, đặt nguồn, phiên bản và sự thay đổi ở trường metadata **chỉ nếu schema cho phép**; nếu không, phát hành bảng nguồn riêng khi người dùng đồng ý, tránh phá khả năng import.
