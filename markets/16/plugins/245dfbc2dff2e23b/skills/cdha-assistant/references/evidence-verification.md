# Kiểm chứng nguồn và Update by Bing (quy trình chống ảo)

**Luật ưu tiên**: phải áp dụng chính văn `anti_hallucination.pdf`, `luat Update by Bing.pdf` và chuẩn L0–L3 trong `LINK_VERIFICATION_3_LEVELS.md`, kèm các tệp triển khai tương ứng. Chỉ L3 xác nhận đã mở trực tiếp nguồn đích; một trang abstract/landing có thể đạt L3 cho chính trang đó nhưng không phải full text.

**Từ khóa kích hoạt**: Update by Bing, update, guideline mới nhất, phiên bản 2026, cơ sở y học bằng chứng, kiểm tra DOI/PMID/link, so sánh khuyến cáo, trích nguồn nguyên phát.

## Quy trình
1. Chốt câu hỏi chính xác (modality, organ, population [Nhi vs người lớn], mục đích: chỉ định/siêu âm/GPB/kinh nghiệm đọc ảnh). Truy xuất trang **cơ quan chủ quản** trước, không lấy snippet làm tài liệu nguyên bản.
2. Kiểm tra `title; authors/authority; issued/updated date; edition/release date; source link; genre; exact scope`. Tránh nhầm 2026 crawler time là publication year; tránh nhầm `2025 Revision` đăng tạp chí 2026 thành hai tài liệu khác.
3. Lập mức truy cập một nguồn: `[PRIMARY FULL DOCUMENT ACCESSED]`, `[PRIMARY LANDING PAGE ONLY]`, `[ABSTRACT ONLY]`, `[SECONDARY SUMMARY]`, `[UNAVAILABLE]`. Chỉ mô tả nội dung trong phần đã đọc. Không dùng tuyên bố đầy đủ chi tiết nếu chỉ landing page.
4. Thẩm định nghiên cứu: design, population, test/index vs reference standard, blinded interpretation, selection/spectrum bias, verification bias, missing data, 2×2 sensitivity/specificity / LR / CIs, external validation, pediatric applicability.
5. Đối chiếu nguồn thứ hai độc lập khi có khác biệt quan trọng. Phân định: khoa học vs guideline vs practice parameter vs regulatory requirements, ACR/AIUM vs CAP/IARC/WHO, không gán một tổ chức ban hành quy tắc của tổ chức khác.
6. **Luôn gắn mức L0/L1/L2/L3 cho URL kiểm chứng**; tách độc lập mức đọc `FULL TEXT`, `ABSTRACT ONLY`, `LANDING ONLY`. Kết quả mở lỗi không L3.
7. Xuất kết quả 5 phần: câu hỏi; điều đã xác minh (với URL gốc); ý nghĩa học tập; giới hạn/độ chắc chắn; **điểm cập nhật** và **ngày kiểm tra**. Nếu không có truy cập web, nói không xác minh hiện hành.
8. Nếu người dùng gửi PDF bài báo, đọc file và nêu rõ phần đã thấy; không giả vờ đọc supplementary materials hay tables không cung cấp.

## Chặn lỗi thường gặp
- Không bịa PMID, DOI, prevalence, specificity, sensitivity, kappa, tiêu chuẩn chẩn đoán, ngưỡng siêu âm, kích thước u, IHC cut-off, TNM stage, BI-RADS, hệ phân loại bệnh.
- Không gắn nhãn guideline mạnh/yếu hay GRADE nếu văn bản chưa xác nhận.
- Không tự diễn giải ảnh thiếu hoàn cảnh thành tên bệnh chắc chắn. Không dịch acronym (ACR, AIUM, CAP, IARC) thành tổ chức khác.
- Khi nguồn chỉ abstract-only hoặc trả phí, phải ghi rõ `chỉ xem được tóm tắt`, đề xuất cách xem toàn văn hợp pháp; không dựng nội dung toàn văn.
- Ưu tiên nguồn gốc đã được duyệt thay vì blog tổng hợp. Mỗi quan điểm mâu thuẫn có nguồn tách biệt và điều kiện áp dụng.

## Quy tắc ưu tiên sau lệnh cập nhật
Nếu nhận `Update by Bing`, bắt buộc cập nhật **toàn bộ** phần trả lời liên quan. Chốt bằng hai đề mục chính xác `Những gì đã thay đổi` và `Đã kiểm tra nguồn`, theo bản gốc PDF. Nếu không thực sự dùng web, không gắn nhãn đã cập nhật.
