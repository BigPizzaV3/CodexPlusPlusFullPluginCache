# LEARN EBM — Ba mức kiểm chứng liên kết (L1–L3) | v0.10.2

## A. Nguyên tắc bắt buộc
**Chỉ ghi “đã xác minh truy cập” / “direct access verified” khi đạt L3.** Không dùng nhãn này cho kết quả tìm kiếm, đường dẫn được tạo theo cú pháp, snippet, kết quả đọc gián tiếp hoặc trang người dùng khẳng định đã mở mà công cụ chưa tự xác nhận.

| Mức | Tiêu chuẩn tối thiểu | Nhãn được phép | Không được khẳng định |
|---|---|---|---|
| L1 — Found in search | URL xuất hiện trong kết quả tìm kiếm thực tế, có nguồn hoặc kết quả truy xuất nêu URL; chưa mở trực tiếp | `L1 — URL tìm thấy trong kết quả tìm kiếm; chưa xác minh truy cập` | Đã truy cập trang, đã đọc tài liệu hoặc đã xác minh URL mở được |
| L2 — Content retrieved | Công cụ trả về nội dung liên quan (ví dụ trang trích xuất/lưu đệm, bản ghi cơ sở dữ liệu, phần tài liệu có văn bản) và có thể đối chiếu nội dung với URL, nhưng **chưa thử mở trực tiếp URL đích thành công** | `L2 — Đã truy xuất nội dung; chưa xác minh truy cập trực tiếp URL` | Đã xác minh trang mở trực tiếp, đã đọc full text khi chỉ có abstract |
| L3 — Direct open succeeded | Đã thao tác mở trực tiếp URL đích trong phiên kiểm tra, trang đích tải thành công; xác nhận trang đúng nguồn/tài liệu và không phải trang lỗi, CAPTCHA, thông báo chặn, paywall thay cho nội dung được khẳng định | `L3 — Đã xác minh truy cập URL trực tiếp` | Đã xác minh toàn văn, bảng/hình/khuyến cáo hay độ tin cậy nội dung nếu chưa thực sự đọc/đối chiếu |

**Ngoài L1–L3: `L0 — Chưa kiểm chứng`** chỉ dùng cho URL tự tạo theo cấu trúc, do người dùng cung cấp mà chưa được tìm thấy bằng tìm kiếm thực tế, hoặc nguồn chưa được kiểm tra. L0 **không phải mức xác minh thứ tư**.

## B. Quy trình bắt buộc cho từng URL
1. Xác định **URL cụ thể**, đối tượng cần xác minh (bài báo/guideline/website/search results), công cụ có thể dùng và thời điểm kiểm tra.
2. Nếu chỉ xây dựng link theo cú pháp (ví dụ URL tìm kiếm PubMed), gán L0. Nếu link xuất hiện trong *kết quả tìm kiếm thực* nhưng chưa truy xuất nội dung, gán L1.
3. Nếu đọc được nội dung từ công cụ lấy dữ liệu, bộ nhớ đệm, bản trích xuất, API hoặc bản ghi, đối chiếu tựa đề/tác giả/PMID/DOI khi có và ghi L2. **Snippet hoặc tiêu đề search result đơn thuần không đủ thành L2.**
4. Nếu có thể, dùng chức năng **open/click/direct navigation** đối với chính URL đích hoặc URL chuẩn (canonical); theo dõi redirect, xác nhận địa chỉ cuối, trang đúng nguồn và nội dung phù hợp. Khi thành công mới gán L3. Chỉ nhận L3 từ **thao tác truy cập thực**, không suy luận từ HTTP link format hay indexed search.
5. Trường hợp HTTP 200 nhưng chỉ trả về CAPTCHA, trang lỗi, yêu cầu đăng nhập, placeholder, hoặc chuyển sang trang không liên quan: **không nâng lên L3** cho tài liệu đích. Nếu trang landing/abstract mở được nhưng toàn văn bị khóa, L3 chỉ áp dụng cho **landing/abstract**, không phải full text.
6. Nếu lần mở trực tiếp lỗi/timeout/403/404, vẫn giữ mức cao nhất có bằng chứng hợp lệ (L1/L2) kèm tình trạng `direct open failed` và thời điểm; không diễn đạt như đã mở thành công. Nếu công cụ hiện không có khả năng mở trực tiếp, không được tự nâng hạng.
7. Nếu người dùng tự báo “tôi mở được”, ghi `người dùng báo truy cập được — chưa được hệ thống xác minh` trừ khi công cụ cũng mở thành công.
8. Mức là trạng thái **của một URL và lần kiểm tra cụ thể**, không tự lan sang các URL khác, toàn bộ trang web, nghiên cứu cùng tên hay toàn văn. Kiểm tra cũ phải ghi thời gian; các link có thể đổi trạng thái về sau.

## C. Kiểm chứng liên kết khác với kiểm chứng nội dung
- **L1/L2/L3 nói về đường dẫn/khả năng truy cập**, KHÔNG phải mức chất lượng bằng chứng EBM hay mức độ tin cậy của một kết luận khoa học.
- Ghi thêm riêng `Độ sâu nội dung`: `metadata / abstract / full text / bảng-hình liên quan / guideline version`, chỉ khi thật sự đọc được.
- Xác minh PMID/DOI/tiêu đề của bản ghi **không tự chứng minh URL publisher mở trực tiếp**.
- Một URL PubMed search tự dựng có thể L0; nếu mở trang kết quả và xác nhận truy vấn hiển thị chính xác có thể L3 **cho trang tìm kiếm**, nhưng không xác minh nội dung của mọi bài xuất hiện.
- Một file PDF do người dùng tải lên và đã đọc được là **nội dung tệp đã truy xuất**; không từ đó khẳng định liên kết bên ngoài tới nhà xuất bản đạt L3.

## D. Mẫu báo cáo kiểm chứng
| URL / Tài liệu | Mức truy cập | Cách kiểm tra | Độ sâu đọc | Thời điểm | Giới hạn |
|---|---|---|---|---|---|
| https://example.org/... | L1/L2/L3 hoặc L0 | search / retrieved extract / direct open | metadata / abstract / full text | YYYY-MM-DD (múi giờ nếu cần) | lỗi, redirect, paywall, chưa mở... |

**Cách phát biểu chuẩn:**
- L0: `Tôi đã tạo URL tra cứu nhưng chưa kiểm tra đường dẫn.`
- L1: `Tôi tìm thấy URL trong kết quả tìm kiếm; chưa mở trang.`
- L2: `Tôi đã truy xuất nội dung qua công cụ, nhưng chưa xác minh trang đích mở trực tiếp.`
- L3: `Tôi đã mở trực tiếp URL và xác nhận trang đúng tài liệu [nêu phạm vi: landing/abstract/toàn văn].`

## E. Kiểm thử âm tính
1. Search snippet có link nhưng chưa mở → L1, không L3.
2. Công cụ trả abstract thông qua chỉ mục, không mở URL → L2, không L3.
3. URL hợp lệ về cú pháp nhưng chưa thực thi → L0.
4. Direct open chuyển sang CAPTCHA/403/404 hoặc trang khác → không L3.
5. Direct open trang PubMed abstract thành công → L3 **trang abstract**, không khẳng định đọc full text.
6. Landing page của nhà xuất bản mở được, toàn văn bị paywall → L3 **landing page**, không full text.
7. Search result của một PDF không chứng minh đã xem các hình/bảng trong PDF.
8. URL trước đây được mở thành công nhưng lần này không thử lại → ghi `L3 đã kiểm chứng vào ngày...` chỉ khi có log thật, không nói xác minh truy cập hiện tại.

Phải áp dụng nhất quán khi `Update by Bing`, tra PubMed, Clinical Queries, đưa liên kết hướng dẫn, trích dẫn bài nghiên cứu và tự đánh giá các URL HLP.
