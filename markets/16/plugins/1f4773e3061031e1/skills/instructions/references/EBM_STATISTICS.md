# EBM quantitative reasoning — safety checks

## Binary outcomes (có cùng thời điểm theo dõi)
- CER = events_control / n_control; EER = events_treatment / n_treatment.
- RR = EER / CER (chỉ khi CER > 0); RRR = 1 − RR cho kết cục bất lợi, nếu có ý nghĩa.
- ARR = CER − EER (lợi ích cho kết cục bất lợi); nếu ARR > 0, NNT = 1/ARR, báo số nguyên làm tròn **lên** và **thời gian theo dõi**. Nếu ARR < 0, báo ARI = EER − CER và NNH = 1/ARI (bối cảnh cùng outcome bất lợi). NNT/NNH phải dựa trên nguy cơ tuyệt đối, không lấy 1/RRR.
- Nếu 0 events hoặc follow-up không đồng đều, không dùng phép chia đơn giản thiếu điều kiện; cân nhắc rate/time-to-event.
- 95% CI của ARR khi cắt qua 0 tạo NNT hai phía không liên tục; không báo CI của NNT bằng cách đảo hai đầu một cách thiếu điều kiện.

## Diagnostic reasoning
- Sensitivity = TP/(TP+FN); specificity = TN/(TN+FP).
- LR+ = sensitivity/(1−specificity); LR−=(1−sensitivity)/specificity nếu mẫu số khác 0.
- pre-test odds = p/(1−p); post-test odds = pre-test odds × LR; post-test p = odds/(1+odds).
- PPV/NPV thay đổi theo prevalence/baseline risk; không diễn giải như tính chất bất biến của test.

## Association and uncertainty
- OR khác RR; với biến cố thường gặp, OR có thể xa 1 hơn RR. HR là hazard ratio theo time-to-event và giả định mô hình, không suy trực tiếp là risk ratio tại một thời điểm.
- p-value **không** là xác suất giả thuyết null đúng hay xác suất kết quả ngẫu nhiên. Không lấy p<0.05 thay thế giá trị lâm sàng.
- 95% CI phản ánh quy trình ước lượng và assumptions; không đồng nghĩa có 95% xác suất tham số cố định nằm trong một CI đã quan sát theo frequentist.
- Missing data, multiplicity, post-hoc subgroup và phân tích không prespecified phải được xem xét.

## Ví dụ hoàn toàn giả định
Trong 100 đối chứng có 20 biến cố, 100 can thiệp có 10 biến cố sau **30 ngày**: CER=0.20, EER=0.10, ARR=0.10, RR=0.50, RRR=0.50, NNT=10/30 ngày. Không đủ dữ liệu để suy CI chính xác nếu không tính bằng phương pháp tương ứng. Không đại diện cho bất kỳ thuốc thực tế nào.

## Khi trả kết quả tính toán
Ghi dữ liệu nguồn; phép tính; đơn vị/phần trăm; kiểm tra lại; assumptions; khoảng thời gian; giới hạn ngoại suy. Không làm tròn dữ liệu trung gian quá sớm.
