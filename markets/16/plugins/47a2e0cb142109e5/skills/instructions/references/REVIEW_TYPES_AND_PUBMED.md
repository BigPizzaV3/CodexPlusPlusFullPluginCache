# Dạng tổng quan y văn và PubMed Clinical Queries

## Chọn loại review theo mục tiêu
| Loại | Khi phù hợp | Cảnh báo |
|---|---|---|
| Narrative | Giới thiệu/bàn luận rộng, cơ chế và bối cảnh | Không mặc định tìm kiếm hệ thống |
| Systematic | Câu hỏi tập trung, quy trình tìm/chọn/lọc minh bạch | Yêu cầu protocol và đánh giá bias thích hợp |
| Meta-analysis | Có nghiên cứu đủ tương đồng để tổng hợp định lượng | Có thể là thành phần của SR, không đồng nghĩa SR |
| Scoping | Lập bản đồ phạm vi/chủ đề, khái niệm và khoảng trống | Không mặc định trả lời hiệu quả điều trị |
| Rapid | Cần chứng cứ nhanh với bước đơn giản hóa công khai | Minh bạch đánh đổi độ đầy đủ |
| Umbrella/Overview of reviews | Tổng hợp nhiều SR về chủ đề | Chú ý trùng lặp nghiên cứu gốc giữa SR |
| Living SR | Câu hỏi cần cập nhật liên tục | Cần nguồn lực và protocol cập nhật |
| Realist | Cơ chế can thiệp phức tạp: điều gì hiệu quả, cho ai, trong bối cảnh nào | Không thể giản lược thành pooled effect |
| Integrative | Kết hợp bằng chứng và phương pháp đa dạng | Cần khung tổng hợp rõ |
| Qualitative evidence synthesis | Trải nghiệm, ý nghĩa, khả năng chấp nhận | Chọn phương pháp tổng hợp định tính phù hợp |
| Mixed-methods | Kết hợp định tính/định lượng | Minh bạch chiến lược tích hợp |
| Critical / Expert | Bình luận, luận giải theo chuyên gia | Không mặc định có độ tin cậy như SR |
| State-of-the-Art | Tổng quan phát triển và hướng mới của lĩnh vực | Không tự nhận đánh giá hệ thống |

Không coi các tên là phân loại tuyệt đối hoặc loại trừ nhau. Hỏi mục tiêu, câu hỏi, khung thời gian, tính cấp bách, tài nguyên và tính tái lập trước khi khuyến nghị.

## Checklist đánh giá bài báo
1. PICO/PECO, outcome chính/phụ, thời điểm đo.
2. Thiết kế, cách chọn mẫu, tính phù hợp và thiên lệch chọn mẫu.
3. Risk of Bias theo loại nghiên cứu (RoB 2 cho RCT, ROBINS-I cho nhiều NRSI, QUADAS thích hợp cho chẩn đoán; xác minh phiên bản đang dùng).
4. Hiệu quả: tuyệt đối và tương đối, 95% CI, độ chính xác, NNT/NNH nếu có đủ căn cứ, phân tích dưới nhóm và multiplicity.
5. Độ chắc chắn tổng bằng chứng nếu thực hiện GRADE, không tự gán mức chỉ vì P < 0,05.
6. Khả năng áp dụng và khác biệt theo tuổi; bất định và giới hạn.
7. Phân biệt đã đọc full text, abstract, bảng, supplementary hay chỉ citation.

## Tạo 10 PubMed Clinical Queries
Người dùng cung cấp từ khóa; nếu yêu cầu 10 link rõ thì tạo ngay, không hỏi thêm. Bảng gồm 5 category × 2 scope:
- `therapy`, `diagnosis`, `etiology`, `prognosis`, `clinical_prediction_guides`.
- `broad` và `narrow`.

Hình thức gợi ý:
`https://pubmed.ncbi.nlm.nih.gov/clinical/?term=<URL_ENCODED_KEYWORDS>&clinical_study_category=<category>&clinical_study_scope=<broad_or_narrow>`

Đây là **mẫu liên kết**, phải kiểm thử URL thực khi có web; không xác nhận các parameter được PubMed chấp nhận vĩnh viễn. Dùng URL encoding UTF-8 phù hợp thay vì xóa dấu tiếng Việt hàng loạt. Nếu website đổi cấu trúc tham số, dùng đúng công cụ Clinical Queries tại https://pubmed.ncbi.nlm.nih.gov/clinical/ và thông báo giới hạn thay vì bịa link.

PubMed Help xác nhận 5 nhóm category và 2 scope: https://pubmed.ncbi.nlm.nih.gov/help/ . NLM tutorial: https://www.nlm.nih.gov/oet/ed/pubmed/pubmed_in_ebp/03-400.html .

Khi được yêu cầu chiến lược tái lập: ghi PICO, MeSH/field tags, Boolean, giới hạn tuổi/ngôn ngữ/năm, ngày tìm kiếm và truy vấn nguyên văn. Clinical Queries chỉ là lối tắt sàng lọc, không thay thế chiến lược SR toàn diện.

**Similar articles:** nếu đã xác nhận có PMID, dẫn đến trang PubMed của PMID đó hoặc mục Similar articles thực tế. Không bịa DOI/PMID hoặc endpoint API chỉ dựa vào tiêu đề. Nếu không có PMID, hướng dẫn tìm bản ghi trước.
