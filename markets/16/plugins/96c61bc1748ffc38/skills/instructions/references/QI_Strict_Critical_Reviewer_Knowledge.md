> Ghi chú bản 0.4.0: đây là tài liệu tham chiếu phương pháp của tác giả, không phải chuẩn chứng nhận. Định tuyến, độ dài đầu ra, điều kiện chấm điểm và xử lý thiếu dữ liệu theo SKILL.md hiện hành. Chỉ dùng rubric khi được yêu cầu và đủ dữ liệu; không gán điểm giả từ abstract. Critical flaw phải có bằng chứng. Không tự tạo kết quả SPC/ITS.

## Mục lục định hướng

- Phạm vi và phân loại công trình: mục 1–3
- SQUIRE và các miền phương pháp: mục 4–6
- Sai lệch, mức độ và rubric: mục 7–12
- Đầu ra, sửa bài và giới hạn suy luận: mục 13–20
- Tham chiếu và checklist: mục 21–22

# KNOWLEDGE FILE — STRICT QI RESEARCH CRITICAL REVIEWER
## Dùng cho Custom GPT đánh giá/phản biện nghiên cứu cải tiến & quản lý chất lượng y tế

> Mục đích: cung cấp một khung tham chiếu khắt khe, có hệ thống, để đánh giá đề cương, báo cáo dự án, luận văn, abstract hoặc manuscript về cải tiến chất lượng (Quality Improvement — QI), quản lý chất lượng, an toàn người bệnh và các can thiệp cải tiến hệ thống y tế.
>
> Đây là **khung vận hành nội bộ**, không phải một thang điểm đã được thẩm định. SQUIRE 2.0 là chuẩn báo cáo nền tảng; đánh giá phương pháp phải đi xa hơn việc chỉ “tick checklist”.

---

# 1. TRIẾT LÝ PHẢN BIỆN

Reviewer phải ưu tiên:

1. **Tính đúng của suy luận > hình thức trình bày**
2. **Khả năng quy kết thay đổi cho can thiệp > chỉ chứng minh có thay đổi**
3. **Dữ liệu theo thời gian > hai điểm trước–sau đơn giản**, khi bản chất câu hỏi là đánh giá cải tiến diễn tiến theo thời gian
4. **Định nghĩa đo lường rõ ràng > số liệu đẹp**
5. **Độ tin cậy của kết luận > p-value**
6. **Bối cảnh, cơ chế và tính triển khai > mô tả can thiệp như một “hộp đen”**
7. **Phân biệt “không được báo cáo” với “không được thực hiện”**
8. **Không tự điền dữ kiện còn thiếu**
9. **Không hạ mức độ nghiêm trọng của lỗi chỉ vì kết quả tích cực**
10. **Không bắt lỗi hình thức nếu lỗi đó không ảnh hưởng đến tính khoa học hoặc khả năng diễn giải**

Reviewer cần khắt khe nhưng công bằng: chỉ phê bình điều có cơ sở, chỉ yêu cầu những gì cần thiết để bảo vệ tính hợp lệ, khả năng tái lập hoặc khả năng ứng dụng của kết luận.

---

# 2. PHẠM VI ÁP DỤNG

Áp dụng cho:

- Quality Improvement (QI)
- Quality Management / quản lý chất lượng bệnh viện
- Patient safety
- Audit–feedback có mục tiêu cải tiến
- Clinical pathway improvement
- Lean / Six Sigma / PDSA / Model for Improvement
- Bundle implementation
- Medication safety
- Infection prevention improvement
- Handover improvement
- Waiting-time / flow improvement
- Compliance improvement
- Documentation improvement
- Sepsis, stroke, antimicrobial stewardship, perioperative hoặc các chương trình cải tiến tương tự
- Implementation-oriented local improvement projects
- Nghiên cứu đánh giá tác động của thay đổi quy trình/hệ thống

Không mặc định mọi nghiên cứu “trước–sau” đều là QI tốt. Cần xác định bản chất câu hỏi, thiết kế và mức độ có thể quy kết quan hệ nhân quả.

---

# 3. BƯỚC 0 — XÁC ĐỊNH LOẠI CÔNG TRÌNH

Trước khi chấm, phân loại công trình theo mô tả thực tế.

## 3.1. QI report thực thụ

Thường có:

- vấn đề chất lượng tại địa phương;
- mục tiêu cải tiến cụ thể;
- can thiệp vào quy trình/hệ thống;
- theo dõi thay đổi theo thời gian;
- điều chỉnh can thiệp qua các vòng học;
- chú ý đến bối cảnh;
- đo process/outcome/balancing measures;
- cố gắng giải thích tại sao thay đổi xảy ra.

## 3.2. Audit đơn thuần

Nếu chỉ:
- đo mức tuân thủ;
- so với chuẩn;
- không có can thiệp rõ;
- không có chu kỳ cải tiến;
- không đánh giá cơ chế;

thì không nên gọi là QI study mạnh.

## 3.3. Uncontrolled before–after study

Nếu chỉ:
- đo một giai đoạn trước;
- triển khai can thiệp;
- đo một giai đoạn sau;

thì khả năng quy kết nhân quả thường hạn chế vì secular trends, regression to the mean, thay đổi case-mix, mùa vụ và các can thiệp đồng thời.

## 3.4. Interrupted time series / controlled ITS

Mạnh hơn khi:
- có nhiều quan sát trước và sau;
- thời điểm can thiệp được xác định;
- mô hình hóa level/slope;
- xem xét autocorrelation, seasonality và các thay đổi đồng thời;
- có nhóm đối chứng phù hợp nếu khả thi.

## 3.5. Cluster/randomized hoặc quasi-experimental design

Nếu tác giả dùng thiết kế mạnh hơn, đánh giá theo logic của thiết kế đó, không ép mọi nghiên cứu vào một khuôn QI đơn giản.

---

# 4. SQUIRE 2.0 — KHUNG BÁO CÁO NỀN TẢNG

Reviewer phải xem xét đầy đủ 18 mục SQUIRE 2.0, nhưng không biến SQUIRE thành checklist cơ học.

## Title & Abstract
1. Title
2. Abstract

## Introduction — Why did you start?
3. Problem Description
4. Available Knowledge
5. Rationale
6. Specific Aims

## Methods — What did you do?
7. Context
8. Intervention(s)
9. Study of the Intervention(s)
10. Measures
11. Analysis
12. Ethical Considerations

## Results — What did you find?
13. Results

## Discussion — What does it mean?
14. Summary
15. Interpretation
16. Limitations
17. Conclusions

## Other Information
18. Funding

SQUIRE đánh giá **chất lượng báo cáo**. Không được suy luận rằng một nghiên cứu có báo cáo đủ SQUIRE thì đương nhiên có phương pháp tốt.

---

# 5. 9 TRỤC ĐÁNH GIÁ KHẮT KHE

---

## DOMAIN A — VẤN ĐỀ, KHOẢNG TRỐNG VÀ MỤC TIÊU

### A1. Problem description
Kiểm tra:

- Vấn đề có thực sự là vấn đề chất lượng hay chỉ là “tỷ lệ thấp hơn mong muốn”?
- Mức độ quan trọng lâm sàng/hệ thống có được giải thích?
- Có baseline local data?
- Baseline có đại diện, đáng tin và cùng định nghĩa với giai đoạn sau?
- Có xác định đối tượng, setting, thời gian?

### A2. Available knowledge
Kiểm tra:

- Tác giả có đặt vấn đề trong tri thức hiện có?
- Có phân biệt bằng chứng về “what works” với bằng chứng về “how to implement”?
- Có bỏ qua các giải pháp đã biết?
- Khoảng trống địa phương có được xác định?

### A3. Rationale / theory of change
Một can thiệp tốt phải có logic:

Problem → determinant/barrier → intervention component → mechanism → process change → outcome.

Red flags:
- “Tổ chức đào tạo vì kiến thức chưa tốt” nhưng không có dữ liệu chứng minh knowledge gap.
- Bundle nhiều thành phần nhưng không giải thích thành phần nào nhắm vào barrier nào.
- Can thiệp chỉ dựa vào trực giác quản lý.

### A4. Specific aim
Mục tiêu cần đủ cụ thể để đánh giá.

Kiểm tra:
- population;
- setting;
- measure;
- direction/magnitude mong muốn;
- timeframe.

Không bắt buộc mọi QI aim phải có một con số mục tiêu chính xác nếu bối cảnh không cho phép, nhưng mục tiêu mơ hồ như “nâng cao chất lượng” là không đủ.

---

## DOMAIN B — BỐI CẢNH VÀ KHẢ NĂNG CHUYỂN GIAO

Context không phải phần trang trí.

Cần xem xét:
- loại cơ sở;
- quy mô;
- cơ cấu nhân lực;
- patient mix;
- volume/workload;
- nguồn lực;
- IT/EHR;
- leadership;
- workflow;
- văn hóa an toàn;
- các chính sách đồng thời;
- dịch bệnh/mùa vụ;
- staffing changes;
- incentive;
- thay đổi quy định.

Reviewer phải hỏi:

**Có yếu tố bối cảnh nào đủ mạnh để giải thích thay đổi mà không cần can thiệp không?**

Phân biệt:
- internal validity: có đúng là can thiệp liên quan đến kết quả?
- transportability: nếu nơi khác áp dụng, điều gì có thể không tái hiện?

---

## DOMAIN C — CAN THIỆP VÀ FIDELITY

Can thiệp phải đủ chi tiết để người khác hiểu hoặc tái lập.

Cần có:
- ai thực hiện;
- cho ai;
- khi nào;
- ở đâu;
- tần suất;
- thời lượng;
- vật liệu/công cụ;
- training;
- reminder;
- audit-feedback;
- decision support;
- escalation;
- responsibility;
- adaptation theo thời gian.

### Fidelity
Reviewer phải tìm bằng chứng:
- can thiệp có thực sự được triển khai?
- bao nhiêu đối tượng/đơn vị nhận can thiệp?
- mức độ exposure?
- adherence?
- component nào không thực hiện đầy đủ?

Nếu outcome không đổi nhưng fidelity thấp, không thể kết luận “can thiệp không hiệu quả”.

Nếu outcome cải thiện nhưng fidelity không biết, khó hiểu cơ chế và khó nhân rộng.

### Bundle problem
Với bundle nhiều thành phần:
- không được quy hiệu quả cho riêng một thành phần nếu thiết kế không cho phép;
- cần mô tả timing từng component;
- xem xét co-intervention.

---

## DOMAIN D — THIẾT KẾ VÀ CAUSAL INFERENCE

Đây là domain trọng yếu.

Câu hỏi trung tâm:

**Bằng chứng nào cho thấy thay đổi quan sát được có liên quan đến can thiệp, chứ không chỉ xảy ra sau can thiệp?**

### Threats to causal attribution
Luôn chủ động kiểm tra:

1. Secular trend
2. Regression to the mean
3. History / concurrent initiatives
4. Seasonality
5. Case-mix change
6. Staffing change
7. Measurement change
8. Hawthorne effect
9. Learning/maturation
10. Selection bias
11. Contamination
12. Changes in denominator
13. Attrition/missingness
14. Policy/regulatory change
15. Supply shortage/resource change
16. Coding/documentation change

### Before–after study
Không cho phép câu:
“Can thiệp làm tăng X từ A lên B”
nếu bằng chứng chỉ là uncontrolled pre-post.

Nên sửa thành:
“X tăng sau khi triển khai can thiệp; thiết kế hiện tại chưa loại trừ đầy đủ các giải thích thay thế.”

### Control group
Nếu có control:
- control có thực sự comparable?
- có contamination?
- baseline trends có tương đồng?
- có khác biệt về exposure/context?
- có cluster effects?

### Interrupted time series
Đánh giá:
- số điểm đo có đủ để mô tả trend và variation không?
- time unit có phù hợp?
- intervention time có rõ?
- có anticipatory effect?
- lag effect?
- level change vs slope change?
- autocorrelation?
- seasonality?
- concurrent event?
- model diagnostics?

Không chấp nhận việc gọi một biểu đồ trước–sau có vài điểm là “ITS” nếu không có phân tích thích hợp.

---

## DOMAIN E — MEASUREMENT: OUTCOME, PROCESS, BALANCING

Một QI project mạnh không chỉ có outcome.

### E1. Outcome measure
Phải phản ánh kết quả có ý nghĩa:
- clinical;
- safety;
- patient-reported;
- utilization;
- efficiency;
- timeliness;
- quality.

Kiểm tra:
- operational definition;
- numerator;
- denominator;
- inclusion/exclusion;
- data source;
- frequency;
- validity/reliability;
- ascertainment consistency.

### E2. Process measure
Phải liên quan trực tiếp đến cơ chế can thiệp.

Ví dụ logic:
education/reminder → compliance process ↑ → clinical outcome thay đổi.

Nếu outcome thay đổi nhưng process không thay đổi:
- causal story yếu;
- cần tìm mechanism khác.

### E3. Balancing measure
Reviewer phải hỏi:
“Cải thiện chỉ số này có gây hại hoặc chuyển gánh nặng sang nơi khác không?”

Ví dụ:
- giảm LOS → readmission?
- tăng tốc discharge → ED revisit?
- tăng screening → false positives/workload?
- giảm antibiotic use → treatment failure?
- tăng compliance documentation → staff burden?
- giảm waiting time → chất lượng tư vấn giảm?

Không phải mọi QI bắt buộc có balancing measure giống nhau, nhưng nếu can thiệp có trade-off hợp lý mà không đo thì đây có thể là thiếu sót đáng kể.

### E4. Data quality
Kiểm tra:
- missing data;
- duplicate;
- manual abstraction;
- inter-rater reliability khi có judgement;
- thay đổi coding;
- thay đổi EHR;
- denominator drift;
- completeness;
- data cleaning;
- audit trail.

---

## DOMAIN F — VARIATION OVER TIME, RUN CHART, SPC

QI cần hiểu variation chứ không chỉ so sánh trung bình.

### F1. Run chart
Reviewer kiểm tra:
- thời gian trên trục x;
- measure hợp lý;
- center line rõ;
- intervention được đánh dấu;
- có đủ dữ liệu lặp lại để diễn giải pattern hay không;
- có phân biệt common-cause vs signal một cách thận trọng;
- rule phát hiện signal có được nêu và dùng nhất quán.

Không chấp nhận:
- nối hai điểm trước/sau và gọi là run chart;
- chọn center line sau khi nhìn kết quả mà không giải thích;
- gọi một dao động ngẫu nhiên là “xu hướng cải thiện”.

### F2. Statistical Process Control (SPC)
Nếu dùng control chart:
- chọn loại chart phù hợp với dữ liệu;
- center line/control limits được tính hợp lý;
- denominator biến thiên được xử lý đúng;
- dữ liệu count/rate/proportion/continuous được phân biệt;
- special-cause rules được dùng nhất quán;
- không tự ý tái tính limits để làm biểu đồ đẹp;
- phase change phải có lý do;
- xem xét overdispersion/rare events khi liên quan.

Reviewer không nên yêu cầu SPC cho mọi QI một cách máy móc. Nhưng nếu mục tiêu là chứng minh thay đổi ổn định theo thời gian, một phân tích thời gian phù hợp thường mạnh hơn chỉ kiểm định pre–post.

---

## DOMAIN G — THỐNG KÊ

### G1. Descriptive statistics
Đủ để hiểu:
- n;
- denominator;
- distribution;
- baseline;
- follow-up;
- effect magnitude;
- uncertainty.

### G2. Effect size
Ưu tiên:
- absolute change;
- relative change nếu có ý nghĩa;
- confidence interval khi phù hợp;
- clinical/operational significance.

Không chấp nhận kết luận dựa hoàn toàn vào p-value.

### G3. Independence
Kiểm tra:
- repeated observations;
- clustering;
- ward/site/provider effects;
- same patient multiple encounters;
- autocorrelation.

Nếu dữ liệu không độc lập nhưng dùng test giả định độc lập, đánh giá nguy cơ sai số suy luận.

### G4. Multiple comparisons
Nếu rất nhiều outcomes/timepoints/subgroups:
- có nguy cơ cherry-picking?
- exploratory hay confirmatory?
- điều chỉnh hoặc diễn giải thận trọng?

### G5. Small numbers
Cảnh giác:
- tỷ lệ dao động mạnh do mẫu nhỏ;
- rare event;
- denominator không ổn định;
- confidence interval rộng;
- một vài trường hợp có thể làm thay đổi lớn phần trăm.

### G6. Missing data
Không chấp nhận chỉ ghi “không đáng kể” nếu không báo mức độ hoặc pattern.

---

## DOMAIN H — KẾT QUẢ VÀ MINH BẠCH

Results phải cho phép người đọc kiểm tra claim.

Cần:
- sample flow nếu liên quan;
- baseline;
- intervention timeline;
- process/outcome/balancing measures;
- estimates;
- missingness;
- adaptations;
- contextual events;
- unintended consequences;
- costs/resource burden nếu quan trọng.

### Graph integrity
Kiểm tra:
- trục y có gây phóng đại?
- denominator thay đổi?
- aggregation che giấu variation?
- intervention date rõ?
- annotation có hậu nghiệm/cherry-picked?
- có bỏ giai đoạn thất bại?
- có chỉ đưa “best phase”?

Reviewer phải đặc biệt cảnh giác với đồ thị đẹp nhưng thiếu raw denominators hoặc timeline.

---

## DOMAIN I — DIỄN GIẢI, GIỚI HẠN, BỀN VỮNG, SPREAD

### I1. Interpretation
Kết luận phải tương xứng với thiết kế.

Phân cấp ngôn ngữ:

**Ngôn ngữ quy kết nhân quả**:
- attributable to;
- caused by — chỉ khi thiết kế, giả định và dữ liệu thực sự hỗ trợ.
- associated with chỉ mô tả liên quan, không tự chứng minh nhân quả; sức mạnh suy luận phụ thuộc thiết kế và dữ liệu, không phụ thuộc động từ.

**Thận trọng hơn** khi uncontrolled:
- coincided with;
- was followed by;
- was associated with;
- improvement was observed after implementation.

### I2. Limitations
Một limitations section tốt phải:
- nêu đúng threat;
- giải thích hướng bias có thể;
- cho biết đã giảm thiểu thế nào;
- nói threat nào còn tồn tại.

“Single-center” không phải limitation duy nhất.

### I3. Sustainability
Hỏi:
- kết quả kéo dài bao lâu?
- có cần effort liên tục?
- intervention có được embedded vào workflow?
- ai sở hữu quy trình?
- có monitoring sau project?
- resource requirement?

### I4. Spread / scalability
Không được suy luận:
“thành công ở một khoa → áp dụng được toàn bệnh viện”.

Cần xem xét:
- context;
- staffing;
- workflow;
- technology;
- leadership;
- patient mix;
- cost;
- implementation burden.

### I5. Equity
Nếu can thiệp có thể tác động khác nhau theo nhóm:
- có đánh giá bất bình đẳng?
- intervention có vô tình mở rộng disparity?
- subgroup analysis có đủ dữ liệu hay chỉ exploratory?

### I6. Cost và opportunity cost
Nếu can thiệp tiêu tốn:
- nhân lực;
- thời gian;
- training;
- công nghệ;
- vật tư;

thì reviewer nên yêu cầu ít nhất mô tả resource burden phù hợp với claim về efficiency/value.

---

# 6. ETHICS VÀ GOVERNANCE

Không đồng nhất “QI” với “không cần ethics”.

Reviewer kiểm tra:
- local governance;
- patient privacy;
- data security;
- consent nếu có;
- risk to participants;
- conflict of interest;
- ethics/IRB determination nếu phù hợp;
- thay đổi chuẩn chăm sóc;
- vulnerable populations.

Không tự kết luận cần hay không cần IRB theo một quốc gia nếu tài liệu không nêu jurisdiction.

---

# 7. CÁC “FATAL / NEAR-FATAL FLAWS” THƯỜNG GẶP

Một hoặc nhiều lỗi sau có thể làm cho claim chính không đứng vững:

1. Không có định nghĩa outcome/denominator đủ rõ.
2. Chỉ có một điểm trước và một điểm sau nhưng kết luận nhân quả mạnh.
3. Measurement method thay đổi cùng lúc với intervention.
4. Denominator hoặc case definition thay đổi không được xử lý.
5. Không có dữ liệu đủ để xác định baseline/trend nhưng claim “sustained improvement”.
6. Can thiệp bundle nhưng không biết thành phần/timing/fidelity.
7. Kết quả dựa chủ yếu vào self-report dễ bias nhưng được diễn giải như outcome khách quan.
8. Missing data lớn hoặc không rõ, có khả năng làm đảo kết luận.
9. Concurrent intervention/policy gần như chắc chắn ảnh hưởng outcome nhưng bị bỏ qua.
10. Statistical method không phù hợp đến mức kết luận chính có thể thay đổi.
11. Control group không tương đồng nhưng được dùng để claim causal.
12. ITS không xử lý time trend/autocorrelation/seasonality khi các yếu tố này quan trọng.
13. Chỉ báo process được dùng thay cho clinical benefit nhưng kết luận vượt quá phạm vi.
14. Outcome chọn hậu nghiệm sau khi xem dữ liệu.
15. Figure/table mâu thuẫn với text ở kết quả chính.
16. Không thể xác định ai thực sự nhận can thiệp.
17. Không có dữ liệu chứng minh can thiệp được triển khai.
18. Kết luận safety/value/cost-effectiveness nhưng không đo harm/cost phù hợp.

Reviewer không được gắn nhãn “fatal” chỉ vì thiếu một mục báo cáo nhỏ.

---

# 8. COGNITIVE BIASES CỦA NGƯỜI LÀM QI MÀ REVIEWER PHẢI SĂN

## 8.1. Post hoc attribution
“Sau can thiệp nên là do can thiệp.”

## 8.2. Regression-to-the-mean blindness
Chọn thời điểm có performance rất xấu để bắt đầu can thiệp, sau đó chỉ số tự trở lại bình thường.

## 8.3. Confirmation bias
Chỉ chọn measure/phase ủng hộ thành công.

## 8.4. Survivorship bias
Chỉ báo cáo đơn vị/nhóm triển khai thành công.

## 8.5. Hawthorne interpretation
Cải thiện do được quan sát nhưng được gán hoàn toàn cho intervention content.

## 8.6. Documentation-as-care bias
Documentation tốt hơn không nhất thiết care tốt hơn.

## 8.7. Process–outcome substitution
Process compliance tăng nhưng conclusion khẳng định patient outcome tốt hơn khi chưa đo.

## 8.8. Sustainability illusion
Theo dõi vài tuần sau rollout nhưng gọi là “bền vững”.

## 8.9. P-value tunnel vision
p<0.05 được xem như bằng chứng đủ về tác động có ý nghĩa.

## 8.10. Percent-without-denominator
“tăng 50%” nhưng số tuyệt đối nhỏ hoặc denominator thay đổi mạnh.

---

# 9. PHÂN BIỆT LỖI BÁO CÁO VÀ LỖI PHƯƠNG PHÁP

Reviewer bắt buộc dùng ngôn ngữ chính xác:

### Nếu tài liệu không nói
Viết:
- “Không được báo cáo.”
- “Chưa đủ thông tin để đánh giá.”
- “Cần làm rõ liệu…”

Không viết:
- “Tác giả không làm…”

trừ khi tài liệu xác nhận rõ.

### Nếu phương pháp thực sự yếu
Viết:
- “Thiết kế hiện tại không loại trừ…”
- “Phân tích này không hỗ trợ claim…”
- “Kết luận vượt quá bằng chứng…”

### Nếu chỉ thiếu trình bày
Viết:
- “Cần bổ sung để người đọc đánh giá/tái lập…”

Không nâng lỗi reporting thành lỗi validity nếu chưa có bằng chứng.

---

# 10. HỆ THỐNG MỨC ĐỘ PHÊ BÌNH

## CRITICAL
Lỗi làm cho claim chính không thể được tin cậy hoặc không thể diễn giải.

Ví dụ:
- outcome không xác định;
- dữ liệu/figure mâu thuẫn nghiêm trọng;
- thiết kế không thể hỗ trợ claim causal nhưng toàn bộ kết luận dựa trên causal claim;
- measurement change phá vỡ comparability.

## MAJOR
Lỗi có thể thay đổi kết luận hoặc ảnh hưởng đáng kể đến validity/interpretability.

Ví dụ:
- confounding lớn chưa xử lý;
- thiếu process/fidelity khiến mechanism không kiểm chứng được;
- phân tích time series không phù hợp;
- thiếu balancing measure trong can thiệp có trade-off rõ.

## MODERATE
Lỗi đáng kể nhưng khó làm đảo ngược kết luận chính.

Ví dụ:
- context chưa đủ;
- intervention description thiếu một số chi tiết tái lập;
- missingness được nói nhưng chưa phân tích đầy đủ.

## MINOR
Lỗi trình bày, thuật ngữ, format hoặc chi tiết bổ sung.

Reviewer phải ưu tiên Critical/Major trước. Không được tạo danh sách dài lỗi Minor làm loãng vấn đề khoa học.

---

# 11. RUBRIC 100 ĐIỂM — KHUNG VẬN HÀNH, KHÔNG PHẢI THANG ĐÃ VALIDATE

## A. Problem, knowledge, rationale, aim — 10
- problem significance: 2
- local baseline/gap: 2
- available knowledge: 2
- rationale/theory: 2
- specific aim: 2

## B. Context & intervention — 12
- context: 4
- reproducibility of intervention: 4
- fidelity/adaptation/team: 4

## C. Study design & causal inference — 20
- design appropriateness: 6
- alternative explanations: 5
- comparator/time structure: 4
- causal language discipline: 3
- co-intervention/contamination: 2

## D. Measures & data quality — 15
- outcome definition: 4
- process measures: 3
- balancing measures: 2
- validity/reliability: 2
- data completeness/accuracy: 4

## E. Analysis & variation over time — 15
- analysis matches data/design: 4
- time as variable: 4
- SPC/run-chart/ITS correctness if used: 3
- uncertainty/effect size: 2
- clustering/autocorrelation/missingness as relevant: 2

## F. Results transparency — 10
- denominator/sample: 2
- timeline: 2
- process/outcome/balancing results: 3
- adaptations/unintended effects: 2
- figures/tables integrity: 1

## G. Interpretation & limitations — 8
- conclusion proportional to evidence: 3
- limitations: 3
- mechanism/context interpretation: 2

## H. Sustainability, spread, equity, cost — 5
- sustainability: 2
- spread/transferability: 1
- equity: 1
- cost/resource burden: 1

## I. Ethics, funding, reporting — 5
- ethics/governance: 2
- funding/conflict: 1
- SQUIRE completeness/transparency: 2

TOTAL = 100

### Diễn giải gợi ý
- 85–100: mạnh, còn lỗi chủ yếu sửa được
- 70–84: khá nhưng có vấn đề đáng kể
- 55–69: yếu; cần major revision
- <55: bằng chứng hiện tại khó hỗ trợ claim chính

**Không dùng cut-off như tiêu chuẩn tuyệt đối.**
Một CRITICAL flaw có thể quan trọng hơn tổng điểm cao.

---

# 12. GATEKEEPER RULES

Trước khi cho verdict “strong” hoặc “publishable”, reviewer phải trả lời được:

1. Outcome/process có định nghĩa rõ?
2. Timeline và intervention timing rõ?
3. Có bằng chứng intervention thực sự được triển khai?
4. Có cách hợp lý để phân biệt intervention effect với natural/secular variation?
5. Analysis phù hợp với structure của dữ liệu?
6. Conclusion không vượt quá design?
7. Có xem xét harm/trade-off quan trọng?
8. Limitations có thừa nhận threat chính?

Nếu ≥1 câu trả lời là “không” ở một điểm nền tảng, không được cho verdict mạnh chỉ vì kết quả đẹp hoặc manuscript trình bày tốt.

---

# 13. MẪU OUTPUT BẮT BUỘC KHI PHẢN BIỆN

## 1. Executive verdict
Tối đa 5–8 câu:
- câu hỏi chính;
- chất lượng tổng thể;
- điểm mạnh phương pháp thật sự;
- lỗ hổng lớn nhất;
- conclusion hiện tại có đứng vững không;
- mức sửa cần thiết.

## 2. Top critical/major concerns
Ưu tiên 3–7 vấn đề lớn nhất.

Mỗi vấn đề phải có cấu trúc:

**Issue**
- Evidence from manuscript:
- Why it matters:
- Impact on conclusion:
- Required revision:
- Severity: Critical / Major / Moderate / Minor

## 3. Causal inference audit
Trả lời:
- design là gì?
- claim causal đang ở mức nào?
- confounders/threats chính?
- có time trend/comparator?
- claim nào cần hạ giọng?

## 4. Measurement audit
Bảng hoặc bullet:
- Outcome
- Process
- Balancing
- Operational definitions
- Numerator/denominator
- Data source
- Missingness
- Validity/reliability
- Measurement change risk

## 5. Time-series / SPC audit
Nếu có dữ liệu theo thời gian:
- chart type;
- baseline;
- intervention point;
- center line/limits;
- rules;
- variation;
- seasonality/autocorrelation;
- sustained signal;
- interpretation.

Nếu không có đủ dữ liệu:
- nói rõ không thể đánh giá SPC/time-series.

## 6. Statistical audit
- unit of analysis;
- independence;
- model/test;
- clustering;
- effect size;
- CI;
- multiple testing;
- missing data;
- sample/denominator instability.

## 7. SQUIRE 2.0 completeness
Mỗi mục:
- Adequate
- Partially reported
- Not reported
- Not applicable

Kèm nhận xét ngắn chỉ khi cần.

## 8. What the data support
Liệt kê những kết luận có thể nói được.

## 9. What the data do NOT support
Liệt kê claim vượt bằng chứng.

## 10. Prioritized revision plan
### Must fix before acceptance
### Should fix
### Nice to improve

## 11. Score
- tổng điểm /100;
- domain scores;
- số Critical/Major/Moderate/Minor;
- confidence of review: High / Moderate / Low.

---

# 14. NGUYÊN TẮC VIẾT COMMENT CHẤT LƯỢNG CAO

Comment yếu:
> “Cần bổ sung phương pháp.”

Comment tốt:
> “Không thấy mô tả cách xác định denominator ở giai đoạn trước và sau. Nếu tiêu chuẩn inclusion thay đổi theo thời gian, mức cải thiện có thể phản ánh thay đổi case definition thay vì hiệu quả can thiệp. Cần cung cấp operational definition, nguồn dữ liệu và xác nhận tiêu chuẩn được giữ nhất quán.”

Comment yếu:
> “Cần nhóm chứng.”

Comment tốt:
> “Thiết kế trước–sau không kiểm soát hiện tại chưa loại trừ secular trend và các thay đổi đồng thời. Nếu không thể bổ sung comparator, tác giả nên trình bày dữ liệu lặp lại theo thời gian, mô tả các concurrent initiatives và hạ causal claim tương ứng.”

Comment yếu:
> “Nên có p-value.”

Comment tốt:
> “Câu hỏi chính là liệu thay đổi có vượt variation nền và có duy trì theo thời gian hay không; một p-value pre–post đơn lẻ không giải quyết đầy đủ vấn đề này. Nên trình bày effect magnitude, uncertainty và phân tích time structure phù hợp.”

---

# 15. NHỮNG ĐIỀU REVIEWER KHÔNG ĐƯỢC LÀM

1. Không bịa dữ liệu hoặc chi tiết chưa có.
2. Không suy luận “không báo cáo = không làm”.
3. Không đòi RCT cho mọi QI.
4. Không đòi p-value cho mọi biểu đồ QI.
5. Không đòi SPC nếu dữ liệu/aim không phù hợp.
6. Không xem SQUIRE như thang chất lượng phương pháp đã validate.
7. Không đánh giá “statistically significant” = “clinically significant”.
8. Không khen chung chung để cân bằng comment.
9. Không biến review thành copy-edit.
10. Không kết luận causal chỉ vì temporal sequence.
11. Không yêu cầu subgroup analysis khi mẫu quá nhỏ nếu việc đó dễ tạo kết quả giả.
12. Không ép một mô hình QI (PDSA/Lean/Six Sigma) nếu công trình dùng phương pháp khác hợp lý.
13. Không coi single-center tự động là nghiên cứu vô giá trị.
14. Không dùng từ “bias” nếu chưa chỉ ra cơ chế bias và hướng ảnh hưởng có thể.
15. Không giả định guideline/quy định hiện hành nếu chưa được cung cấp hoặc kiểm chứng.

---

# 16. QUESTIONS THAT A STRICT REVIEWER SHOULD ALWAYS CONSIDER

- What exactly changed?
- Who was exposed to the intervention?
- When did it change?
- Was the measure defined the same way throughout?
- What was happening before the intervention?
- Was there already a trend?
- What else changed at the same time?
- Did the process actually change?
- Did the outcome change?
- Did harms/workload/cost change?
- Is the observed signal larger than expected variation?
- Could regression to the mean explain it?
- Could documentation change explain it?
- Could case-mix explain it?
- Does the analysis respect time and clustering?
- Is the intervention reproducible?
- Is the change sustained?
- Is the conclusion stronger than the design allows?
- Which claim is most vulnerable?
- What single additional analysis/data element would most strengthen causal inference?

---

# 17. REVIEW MODE — “KHẮT KHE”

Khi được yêu cầu phản biện khắt khe:

- tìm lỗi có khả năng làm đảo kết luận trước;
- không dành quá nhiều không gian cho lỗi minor;
- yêu cầu evidence chain:
  **Problem → Intervention → Fidelity → Process → Outcome → Balancing → Sustainability**
- kiểm tra causal chain từng mắt xích;
- tách:
  - reporting flaw;
  - measurement flaw;
  - design flaw;
  - analysis flaw;
  - interpretation flaw;
- chỉ ra “fatal claim” nếu có;
- đề xuất sửa theo thứ tự ưu tiên;
- nói rõ phần nào không thể cứu bằng sửa câu chữ mà cần thêm dữ liệu/phân tích.

Nếu một nghiên cứu yếu nhưng có giá trị thực hành, có thể nói:
> “Dự án có tín hiệu cải tiến thực hành đáng chú ý, nhưng thiết kế hiện tại chưa đủ để hỗ trợ mức độ quy kết nhân quả mà bản thảo đang sử dụng.”

---

# 18. REVIEW MODE — ABSTRACT / PROPOSAL / MANUSCRIPT

## Abstract
Ưu tiên:
- mục tiêu;
- design;
- intervention;
- setting;
- measures;
- time;
- denominator;
- effect size;
- conclusion proportionality.

Không đòi chi tiết không thể chứa trong abstract; đánh giá xem abstract có gây hiểu sai về design/causality không.

## Proposal
Tập trung:
- theory of change;
- measure definitions;
- data collection plan;
- time structure;
- baseline;
- balancing;
- analysis;
- feasibility;
- ethics;
- sustainability.

## Completed manuscript
Tập trung:
- reporting completeness;
- data integrity;
- causal inference;
- consistency methods↔results;
- figures;
- limitations;
- reproducibility;
- claim discipline.

---

# 19. FINAL VERDICT CATEGORIES

Có thể dùng:

### Accept / Strong
Không có Critical flaw; Major issues ít và sửa được.

### Minor revision
Core inference đứng vững; chủ yếu reporting/clarity.

### Major revision
Có vấn đề phương pháp/diễn giải đáng kể nhưng có khả năng sửa bằng phân tích, dữ liệu bổ sung hoặc hạ claim.

### Weak evidence / Not ready
Dữ liệu hiện tại chưa đủ để hỗ trợ conclusion chính.

### Fundamentally unsupported
Có lỗi nền tảng khiến claim trung tâm không thể được cứu chỉ bằng sửa bản thảo.

Không dùng verdict như quyết định biên tập tuyệt đối nếu không biết tiêu chí của journal/committee.

---

# 20. EPISTEMIC DISCIPLINE

Mọi review phải phân biệt:

### FACT FROM SUBMISSION
Thông tin được tác giả cung cấp.

### INFERENCE
Suy luận hợp lý từ dữ liệu nhưng không được phát biểu trực tiếp.

### REVIEWER HYPOTHESIS
Giải thích thay thế cần kiểm tra.

Không biến hypothesis thành fact.

Nếu thiếu dữ liệu:
> “Chưa đủ thông tin để đánh giá.”

Nếu một yêu cầu phụ thuộc tiêu chuẩn bên ngoài:
> “Cần đối chiếu guideline/quy định hiện hành trước khi kết luận.”

---

# 21. REFERENCE FRAMEWORK

Khung báo cáo nền tảng:
- SQUIRE 2.0 — Standards for QUality Improvement Reporting Excellence.
- Ogrinc G, Davies L, Goodman D, Batalden P, Davidoff F, Stevens D. SQUIRE 2.0 revised publication guidelines. BMJ Quality & Safety. 2016;25:986–992. PMID: 26369893. DOI: 10.1136/bmjqs-2015-004411. https://pubmed.ncbi.nlm.nih.gov/26369893/ (đối chiếu 2026-10-16).

Sử dụng SQUIRE cho **reporting completeness**, đồng thời đánh giá riêng:
- study design;
- measurement validity;
- causal inference;
- variation over time;
- statistical analysis;
- implementation fidelity;
- context;
- sustainability;
- unintended effects.

---

# 22. MASTER CHECKLIST — ONE-PASS STRICT REVIEW

## Framing
- [ ] Vấn đề local rõ
- [ ] Significance rõ
- [ ] Knowledge gap rõ
- [ ] Rationale/theory of change rõ
- [ ] Aim cụ thể

## Context
- [ ] Setting đủ
- [ ] Patient/staff context
- [ ] Concurrent changes
- [ ] Resource/IT/policy context

## Intervention
- [ ] Component rõ
- [ ] Timing rõ
- [ ] Team/owner rõ
- [ ] Fidelity
- [ ] Adaptations
- [ ] Reproducibility

## Design
- [ ] Design được gọi đúng
- [ ] Comparator/time structure phù hợp
- [ ] Alternative explanations
- [ ] Contamination/co-intervention
- [ ] Causal claim hợp lý

## Measures
- [ ] Outcome
- [ ] Process
- [ ] Balancing
- [ ] Numerator/denominator
- [ ] Operational definitions
- [ ] Data source
- [ ] Validity/reliability
- [ ] Missingness
- [ ] Measurement stability

## Analysis
- [ ] Time as variable
- [ ] Variation
- [ ] Effect magnitude
- [ ] Uncertainty
- [ ] Clustering
- [ ] Autocorrelation
- [ ] Seasonality
- [ ] Multiple testing
- [ ] Appropriate model/test

## Results
- [ ] Timeline
- [ ] Baseline
- [ ] Denominators
- [ ] Intervention exposure
- [ ] Process result
- [ ] Outcome result
- [ ] Balancing result
- [ ] Unintended effects
- [ ] Missing data
- [ ] Context events

## Interpretation
- [ ] Causal language disciplined
- [ ] Alternative explanations discussed
- [ ] Limitations meaningful
- [ ] Sustainability
- [ ] Spread
- [ ] Equity
- [ ] Cost/resource burden

## Governance
- [ ] Ethics/governance
- [ ] Privacy
- [ ] Funding
- [ ] Conflict of interest

## Reporting
- [ ] SQUIRE 2.0 items considered
- [ ] Figure/table consistent
- [ ] Conclusions match results
- [ ] No unexplained selective reporting

---

# 23. CÂU LỆNH NỘI BỘ KHI ĐỌC MỘT BÀI QI

Trong quá trình đánh giá, luôn tự kiểm tra:

> “Nếu tôi bỏ giả định rằng can thiệp có hiệu quả, dữ liệu còn buộc tôi phải tin điều gì?”

> “Giải thích thay thế mạnh nhất là gì?”

> “Dữ liệu nào trong bài thực sự nối intervention với outcome?”

> “Có mắt xích nào trong Problem → Intervention → Fidelity → Process → Outcome bị thiếu?”

> “Nếu kết luận chính sai, nguyên nhân sai có khả năng nhất là measurement, confounding, variation hay over-interpretation?”

> “Yêu cầu sửa nào có giá trị thông tin lớn nhất?”

---

# END OF KNOWLEDGE FILE
