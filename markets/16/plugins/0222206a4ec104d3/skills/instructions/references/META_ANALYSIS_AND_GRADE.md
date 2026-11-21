# Phân tích gộp, dị hợp và GRADE

## Cấu trúc trích dữ liệu và effect measure
- Nhị phân: RR, OR, RD; không hoán đổi OR và RR; cần baseline risk phù hợp cho lợi ích tuyệt đối/NNT.
- Liên tục: MD cùng thang đo; SMD khi các thang đo khác nhau nhưng cùng construct, cân nhắc chiều score; không trộn MD và SMD tùy tiện.
- Time-to-event: HR và survival methods; tránh thay HR bằng RR khi censoring đáng kể.
- Ghi rõ định nghĩa outcome, follow-up, effect direction, unit of analysis, adjusted vs unadjusted, cluster design, multiple arms, crossover, paired data.

## Quy trình lựa chọn tổng hợp
1. Xét tính đồng nhất về clinical, methodological và statistical trước pooling.
2. Chọn phương pháp fixed/common-effect hoặc random-effects theo mô hình khoa học; random-effects KHÔNG tự giải quyết khác biệt lâm sàng.
3. Kết quả: pooled estimate + 95% CI + số nghiên cứu/đối tượng, trọng số và sự phù hợp của mô hình.
4. Heterogeneity: tau², I², Q và CI/prediction interval nếu phù hợp. I² một mình không đánh giá tất cả heterogeneity, nhất là ít nghiên cứu.
5. Đánh giá influence/outliers, sensitivity/subgroup trước hoặc theo protocol; thận trọng multiple comparisons và subgroup không định trước.
6. Publication/missing evidence: xem trial registries, small-study effects, funnel/ Egger khi đủ dữ liệu và điều kiện; nếu k nhỏ không suy từ funnel symmetry rằng bias không tồn tại.
7. Không pooling khi không tương thích; dùng narrative/synthesis without meta-analysis phù hợp và giải thích.

## Công thức minh họa (chỉ dùng khi đủ dữ liệu)
- Event risk = events / group total; RR = risk_treat / risk_control.
- RD = risk_treat - risk_control; absolute effect depends on credible baseline risk.
- Khi ARR = risk_control - risk_treat > 0 (và cùng thời điểm): NNT = 1 / ARR, thường làm tròn lên và nêu thời gian; đừng báo NNT nếu ARR=0/âm theo nghĩa điều trị có lợi.
- Mean difference = mean_treat − mean_control; xem SD và CI trước tổng hợp.
- Bất kỳ forest plot hoặc bảng số liệu giả định phải gắn chữ 'mô phỏng', không giả là dữ liệu đã tìm.

## GRADE đúng cấp độ
GRADE đánh giá *body of evidence* cho **từng outcome**, không phải chấm 'toàn bài' bằng một con số. Xem risk of bias, inconsistency, indirectness, imprecision, missing evidence/publication bias; với bằng chứng không ngẫu nhiên cân nhắc logic tăng/giảm phù hợp phương pháp. Bốn mức: high / moderate / low / very low. Đưa Summary of Findings: số study/người, baseline risk, relative and absolute effects, 95% CI, certainty, lý do giảm/tăng. Không dùng 'RCT luôn chắc chắn cao' hoặc 'SR là mức chứng cứ cao' nếu không biết chất lượng nghiên cứu.

## Ví dụ GIẢ ĐỊNH để dạy
Giả sử trial A có events 10/100 intervention, 20/100 control, cùng follow-up 30 ngày (chỉ mô phỏng), RR=0.5, ARR=0.10, NNT=10/30 ngày, trước khi tính CI. Đây không phải bằng chứng một thuốc có hiệu quả. Cần nhấn mạnh uncertainty khi không có CI và không suy hiệu quả thực tế.
