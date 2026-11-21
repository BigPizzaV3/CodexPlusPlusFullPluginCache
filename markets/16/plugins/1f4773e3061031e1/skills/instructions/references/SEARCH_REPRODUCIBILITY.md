# Ask → Acquire: PubMed strategy and search log

## Khung câu hỏi
Therapy: PICO; etiology: PECO; diagnosis: patient/index/reference/target condition; prognosis: cohort/time/outcome; qualitative: PEO/PICo. Không buộc tất cả outcome/comparator vào truy vấn, vì làm giảm độ nhạy; theo Cochrane, thường kết hợp bệnh/vấn đề, can thiệp, bộ lọc thiết kế (khi có mục tiêu đặc thù).

## Công thức tìm kiếm
1. Tách concept: disease/population, intervention/exposure, study type khi cần.
2. Liệt kê từ đồng nghĩa tiếng Anh + MeSH đã kiểm chứng + tự do ở `[tiab]`.
3. Trong concept dùng `OR`, giữa concept dùng `AND`, dùng dấu ngoặc; `NOT` chỉ khi đã thử nghiệm ảnh hưởng tới độ nhạy.
4. RCT/systematic review filters phải kiểm tra độ phù hợp, không mặc định loại tất cả bài chưa được đánh MeSH.
5. Giới hạn từ 3 năm hoặc ngôn ngữ khi user yêu cầu; nếu systematic review chính thức, giải thích nguy cơ bỏ sót và cân nhắc tìm nhiều CSDL (MEDLINE/PubMed, CENTRAL, Embase nếu có quyền).
6. PubMed URL tạo bằng cách URL-encode **nguyên văn** truy vấn theo RFC3986 (ví dụ Python `urllib.parse.quote(query, safe='')`); không tự sửa/loại bỏ Unicode âm thầm.
7. Link `https://pubmed.ncbi.nlm.nih.gov/?term=<ENCODED_QUERY>` là link tới công cụ tìm kiếm; KHÔNG chứng minh đã có bài phù hợp; URL mới tạo phải gán **L0 — chưa kiểm chứng**. Nếu trực tiếp mở URL PubMed thành công và đối chiếu đúng truy vấn, có thể ghi **L3 đối với trang tìm kiếm**, không phải các bài bên trong.
8. Sau khi chạy thật: kiểm tra `Search Details` trong PubMed để biết Automatic Term Mapping; ghi ngày chạy và số records. Nếu không truy cập, giữ trạng thái chưa chạy.

## Template search log
- Research question and population:
- Database/platform:
- Execution date/time zone:
- Full query copied verbatim:
- Fields/syntax and filters:
- Date range, language restrictions and justification:
- URL và trạng thái L0/L1/L2/L3 (theo `LINK_VERIFICATION_3_LEVELS.md`):
- Kiểm tra trực tiếp lúc nào / URL cuối / đúng query hay không:
- Number retrieved: **not checked** unless directly observed
- Notes: observed Search Details, translations/warnings, duplicates, follow-up sources

## Giới hạn truy cập
PubMed bao gồm bản ghi, không bảo đảm full text. `Free full text` là thuộc tính truy cập được đánh dấu, không thể suy luận rằng mọi bản ghi không thuộc filter đều có paywall. Similar Articles đòi bản ghi PMID cụ thể và thao tác vào trang PubMed, không bịa link tương tự.

## Nguồn để đối chiếu
- PubMed User Guide: https://pubmed.ncbi.nlm.nih.gov/help/
- Cochrane Handbook, ch. 4: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
- PRISMA statement/resource: https://www.prisma-statement.org/
