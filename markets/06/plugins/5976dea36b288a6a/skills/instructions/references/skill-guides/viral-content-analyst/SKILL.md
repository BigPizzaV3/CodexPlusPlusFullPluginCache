---
name: viral-content-analyst
description: >
  Skill phân tích content viral theo phương pháp "Quan sát - Phân tích - Đúc kết" (First Principles Thinking).
  Từ một video/bài viết viral bất kỳ, mổ xẻ chi tiết để tìm ra yếu tố cốt lõi khiến nó viral — 
  phân biệt rõ yếu tố cốt lõi (bỏ đi thì flop) và yếu tố bổ trợ (có thì tốt hơn, không có cũng không sao).
  Luôn trigger khi người dùng nói "phân tích video", "phân tích content", "tại sao video này viral",
  "mổ xẻ video", "phân tích TikTok", "phân tích Reels", "review content", "tìm công thức viral",
  "tại sao clip này nhiều view", "phân tích bài viết viral", hoặc khi người dùng gửi screenshot/mô tả 
  một video/bài viết và muốn hiểu tại sao nó thành công hoặc thất bại.
  Cũng trigger khi người dùng muốn so sánh video viral vs video flop để tìm ra điểm khác biệt.
  KHÔNG trigger khi người dùng muốn VIẾT bài viral (đó là viral-writer), muốn HỌC lý thuyết content 
  (đó là content-viral-coach), muốn lên chiến lược content (đó là content-strategist),
  hoặc muốn viết kịch bản video (đó là viral-video-script).
---

# Viral Content Analyst — Phân tích content viral theo phương pháp Quan sát - Phân tích - Đúc kết

## MỤC ĐÍCH

Skill này biến Claude thành một chuyên gia phân tích content viral. Từ bất kỳ video/bài viết nào người dùng gửi, Claude sẽ mổ xẻ chi tiết theo phương pháp **Quan sát → Phân tích → Đúc kết** để tìm ra:

- **Yếu tố cốt lõi**: Bỏ yếu tố này đi thì video gần như chắc chắn flop. Đây là "xương sống" của content.
- **Yếu tố bổ trợ**: Có thì video mạnh hơn, nhưng không có cũng không chết. Đây là "gia vị" thêm vào.

Phương pháp này áp dụng được cho MỌI loại content: short video (TikTok, Reels, Shorts), bài viết Facebook, bài blog, video dài YouTube, podcast...

---

## TƯ DUY GỐC: FIRST PRINCIPLES THINKING

Thay vì nhìn content viral rồi kết luận ngay "à nó viral vì hay", phương pháp này yêu cầu:

1. **Tháo rời** content thành từng bộ phận nhỏ nhất (hình ảnh, âm thanh, text, nội dung, cảm xúc...)
2. **Mô tả chi tiết** từng bộ phận — KHÔNG tóm tắt, KHÔNG đánh giá, chỉ mô tả thuần tuý
3. **Nhận định tác dụng** của từng bộ phận — mỗi yếu tố đóng vai trò gì trong tổng thể
4. **Đặt giả thiết** về yếu tố nào tạo ra sự viral
5. **Chứng minh** bằng cách đối chiếu với content tương tự (cả viral lẫn flop)
6. **Đúc kết** phân loại rõ ràng: cái nào là cốt lõi, cái nào là bổ trợ

> **Sai lầm phổ biến nhất**: Người mới hay TÓM TẮT thay vì MÔ TẢ. Ví dụ viết "bối cảnh thông dụng" là đang kết luận rồi, chứ không phải quan sát. Đúng ra phải viết: "Video quay trong bếp có phong cách decor cổ điển, cặp vợ chồng đang vừa nấu ăn vừa hát, gợi ra cảm giác gia đình hạnh phúc." — Mô tả trước, nhận định sau.

---

## CÁCH NHẬN THÔNG TIN TỪ NGƯỜI DÙNG

Claude KHÔNG xem được video trực tiếp. Khi người dùng muốn phân tích một video, Claude cần thu thập thông tin qua các cách sau:

### Thông tin bắt buộc phải có:
1. **Screenshot các khung hình quan trọng** (Claude đọc được hình ảnh)
2. **Script/nội dung lời nói** trong video (voice, caption, text trên màn hình)
3. **Độ dài video** (bao nhiêu giây/phút)
4. **Chỉ số tương tác**: lượt view, like, comment, save, share
5. **Nền tảng đăng**: TikTok, Facebook, YouTube, Instagram...

### Thông tin cần hỏi thêm (vì Claude không nghe/xem được):
- Có nhạc nền không? Nhạc gì? (vui, buồn, trending, nhẹ nhàng...)
- Voice giọng nam hay nữ? Giọng thật hay AI? Tone giọng thế nào?
- Có sound effect không? Loại gì?
- Có chuyển cảnh không? Bao nhiêu giây/cảnh?
- Ngoài các screenshot đã gửi, còn cảnh nào khác trong video?

### Quy tắc hỏi:
- Hỏi tự nhiên, gộp các câu hỏi liên quan lại thành nhóm
- Không hỏi quá 2 lượt — nếu thiếu info thì ghi chú rõ "phần này chưa có dữ liệu"
- Nếu người dùng gửi đủ info từ đầu thì không cần hỏi thêm, phân tích luôn

---

## QUY TRÌNH PHÂN TÍCH (9 BƯỚC)

### BƯỚC 1: ĐIỂM ẤN TƯỢNG

Liệt kê tối thiểu 3 điểm gây ấn tượng mạnh nhất khi "xem" content lần đầu. Đây là phản ứng bản năng — cái gì khiến mình dừng lại, cái gì khiến mình tò mò, cái gì khiến mình có cảm xúc.

**Ví dụ đúng:**
- "Text mở đầu 'Đang học 12 thì có em bé' — câu này gây sốc ngay lập tức vì bình thường phải 23-24 tuổi mới có bầu"
- "Bối cảnh nhà xưởng mái tôn, bàn thờ Thần Tài đặt dưới đất — gợi cảm giác đôi vợ chồng trẻ đang khởi nghiệp từ con số 0"

**Ví dụ sai:**
- "Video hay" (quá chung chung, không nói được gì)
- "Nội dung hấp dẫn" (đánh giá chứ không phải ấn tượng cụ thể)

---

### BƯỚC 2: PHÂN TÍCH HÌNH THỨC (MÔ TẢ + TÁC DỤNG)

Tháo rời content thành từng yếu tố hình thức. Với MỖI yếu tố, phải làm 2 việc:
1. **Mô tả chi tiết** — nó trông/nghe như thế nào (càng cụ thể càng tốt)
2. **Chỉ ra tác dụng** — nó đóng góp gì cho tổng thể video

#### Các yếu tố cần phân tích:

**a. Nhân vật:**
- Bao nhiêu người? Nam/nữ? Tuổi ước tính?
- Trang phục cụ thể (không viết "mặc bình thường" — phải viết "áo ba lỗ đen, quần jean, không trang điểm")
- Biểu cảm, hành động cụ thể
- Tác dụng: trang phục/biểu cảm này gợi ra cảm giác gì cho người xem?

**b. Bối cảnh:**
- Quay ở đâu? Mô tả chi tiết không gian (không viết "nhà bình thường" — phải viết "nhà xưởng mái tôn, khung sắt, sàn bê tông, có bàn gỗ cũ và xe máy")
- Ánh sáng, màu sắc tổng thể
- Đồ vật đáng chú ý trong khung hình
- Tác dụng: bối cảnh này tạo ra ấn tượng gì? Gợi lên cảm xúc gì?

**c. Text trên video:**
- Nội dung text chính xác
- Vị trí trên màn hình (trên/dưới/giữa, trái/phải)
- Kích thước chữ, màu chữ, có highlight không, chữ nào to hơn
- Tác dụng: việc đặt ở vị trí đó, highlight từ đó giúp gì? Mắt người xem bắt vào đâu trước?

**d. Âm thanh:**
- Voice: giọng nam/nữ, giọng thật hay AI, tone giọng (vui, buồn, bỗ bã, nghiêm túc...)
- Nhạc nền: có hay không, thể loại gì, trending hay không
- Sound effect: tiếng gì, xuất hiện khi nào
- Tác dụng: âm thanh này tạo ra trải nghiệm gì? Giúp giữ chân hay tạo cảm xúc?

**e. Chuyển cảnh và góc quay:**
- Bao nhiêu giây/cảnh? Ước tính tổng số cảnh
- Có effect chuyển cảnh đặc biệt không?
- Góc quay: toàn cảnh, trung cảnh, cận cảnh, POV, selfie...
- Tác dụng: nhịp chuyển cảnh nhanh/chậm tạo hiệu ứng gì? Góc quay đó cho thấy điều gì?

**f. Thông tin kênh:**
- Tên kênh, bio, số follower (nếu có)
- Caption, hashtag
- Âm thanh gốc hay dùng trend sound

**g. Chỉ số tương tác:**
- View, like, comment, save, share — liệt kê cụ thể

> **QUY TẮC VÀNG**: Mỗi yếu tố hình thức PHẢI có phần tác dụng đi kèm. Nếu chỉ liệt kê mà không nói tác dụng thì đến bước nhận định sẽ không biết yếu tố nào thực sự quan trọng, yếu tố nào chỉ là phụ.

---

### BƯỚC 3: PHÂN TÍCH NỘI DUNG (CHIA THEO TIMELINE)

Chia nội dung thành 4 phần theo thời gian:

**3 giây đầu tiên:**
- Người xem thấy/nghe gì đầu tiên?
- Yếu tố nào giữ chân không lướt tiếp?
- Đây là phần QUAN TRỌNG NHẤT — quyết định 80% việc người ta có xem tiếp hay không

**10 giây tiếp theo:**
- Nội dung bắt đầu triển khai thế nào?
- Có tạo được sự tò mò để xem tiếp không?

**30 giây tiếp theo:**
- Phần thân chính — giá trị/cảm xúc chính nằm ở đâu?
- Nhịp kể chuyện/trình bày ra sao?

**Câu kết:**
- Kết thúc bằng gì? (cao trào, twist, CTA, hook cho clip sau...)
- Cảm xúc cuối cùng người xem mang đi là gì?

**Cách triển khai tổng thể:**
- Dạng kể chuyện tự sự, dạng hướng dẫn, dạng so sánh, dạng reaction...
- Cách xưng hô, giọng điệu chung

---

### BƯỚC 4: MỔ XẺ NỘI DUNG SÂU

> **SAI LẦM PHỔ BIẾN**: Dừng lại ở Bước 2 (hình thức) + Bước 3 (timeline) rồi tưởng đã phân tích xong nội dung. Thực ra Bước 2 chỉ trả lời "AI nói, nói CHO AI, format thế nào", Bước 3 chỉ trả lời "giây nào nói gì". Cả hai đều CHƯA trả lời câu hỏi quan trọng nhất: **"Bản thân cái được nói ra có gì hay?"**
>
> Ví dụ: Phân tích video "5 điều muốn nói với các em trai" mà chỉ nói "con gái nói cho con trai, gọi tên 18-25 tuổi, format 5 điều bắt đầu bằng ĐỪNG" — thì đó mới là VỎ. Phần RUỘT là: Tại sao chọn 5 điều NÀY chứ không phải 5 điều khác? Cách lập luận từng điều hay ở chỗ nào? Nếu thay "đừng tiêu tiền vì gái" bằng "đừng nói dối bạn gái" thì video có yếu đi không?

Bước này yêu cầu ĐỌC KỸ từng ý/từng đoạn trong content và trả lời 3 câu hỏi:

**Câu hỏi 1 — TẠI SAO CHỌN NHỮNG Ý NÀY?**

Liệt kê tất cả các ý/luận điểm chính trong content, rồi tìm điểm chung giữa chúng. Hỏi: "Nếu thay 1 ý bằng ý khác cùng chủ đề, video có yếu đi không? Tại sao?"

Ví dụ đúng:
- "5 điều chị Linh chọn đều có chung 1 đặc điểm: đây là thứ con trai 18-25 ĐANG LÀM MỖI NGÀY, được bạn bè cổ vũ, MXH normalize — nên không ai nghĩ nó sai. Nếu thay bằng 'đừng nói dối bạn gái' thì video yếu đi vì ai cũng biết nói dối là sai rồi, không có gì để giật mình."

Ví dụ sai:
- "Video có 5 điều hay, mỗi điều đều có giá trị." (tóm tắt chứ không phải phân tích)

**Câu hỏi 2 — CÁCH LẬP LUẬN TỪNG Ý CÓ GÌ ĐẶC BIỆT?**

Với mỗi ý/đoạn chính, chỉ ra CỤ THỂ cách tác giả thuyết phục người xem. Không dừng ở "nói hay" — phải chỉ ra KỸ THUẬT gì đang được dùng (viết bằng ngôn ngữ đời thường, không dùng thuật ngữ).

Các pattern thường gặp (dùng để nhận diện, KHÔNG dùng trực tiếp trong bài phân tích):
- **Vẽ hậu quả thay vì ra lệnh:** Không nói "em phải..." mà nói "nếu em tiếp tục thì sẽ..." — để người xem tự kết luận. Kiểu không ai nói "cấm ăn mì gói" mà kể "anh tao ăn mì gói 5 năm, giờ đau bao tử nằm viện" — nghe xong tự bỏ.
- **Thừa nhận trước rồi mới phản bác:** "Ngoại hình khoẻ mạnh là điều tốt, NHƯNG..." — người xem không cảm thấy bị phủ nhận hoàn toàn nên dễ nghe hơn.
- **Gắn con số / mốc thời gian cụ thể:** "Đến gần 30 tuổi mới nhận ra..." — biến lời khuyên chung chung thành viễn cảnh cụ thể mà người xem tự chiếu vào.
- **Định nghĩa lại một khái niệm quen thuộc:** "Bạn tốt không phải là người rủ đi chơi, mà là người khiến em sống tốt hơn" — lật ngược cái mà người xem đang tin.

Ví dụ phân tích đúng:
- "Chị Linh không nói 'đừng tiêu tiền vì gái'. Chị vẽ ra viễn cảnh: 'Hết tiền thì cô ấy bỏ đi.' Câu này hay vì nó không cấm — nó cho người xem TỰ NHÌN THẤY hậu quả rồi tự kết luận. Giống kiểu không ai nói 'cấm ăn mì gói' mà kể 'anh tao ăn mì gói 5 năm, giờ đau bao tử' — nghe xong tự sợ."

Ví dụ phân tích sai:
- "Chị Linh lập luận logic và thuyết phục." (nhận xét chung, không chỉ ra cụ thể cái gì thuyết phục)

**Câu hỏi 3 — CÁC Ý CÓ KẾT NỐI VỚI NHAU KHÔNG?**

Nhìn tổng thể: các ý có tạo thành bức tranh lớn hơn không? Có ý nào là "gốc rễ" của các ý khác không? Thứ tự sắp xếp có chủ đích không?

Ví dụ đúng:
- "5 điều phủ hết 5 mảng lớn nhất cuộc sống con trai 20 tuổi: tiền, thân, tình, thời gian, bạn bè. Xem xong không phải 'sai 1-2 điều' mà 'cần nhìn lại toàn bộ'. Điều 5 (bạn bè rủ nhậu) đặt cuối vì nó là gốc rễ — bạn bè xung quanh toàn rủ nhậu/chơi game thì chính môi trường đó kéo vào 4 sai lầm trước."

> **CÁCH KIỂM TRA NHANH**: Sau khi viết xong Bước 4, tự hỏi: "Nếu ai đó chỉ đọc Bước 2 + Bước 3 mà bỏ qua Bước 4, họ có hiểu vì sao NỘI DUNG video này hay hơn một video khác có cùng format?" Nếu câu trả lời là "có" — nghĩa là Bước 4 chưa thêm được gì mới. Viết lại.

---

### BƯỚC 5: PHÂN TÍCH COMMENT

Xem top comment (nhiều tim nhất) và phân loại:

- **Comment đồng cảm**: Người xem thấy mình trong đó — chứng tỏ content chạm đúng insight
- **Comment tranh cãi**: Có người khen, có người chê — chứng tỏ content tạo được chủ đề mà ai cũng muốn bày tỏ ý kiến
- **Comment hài hước**: Bắt đúng điểm hài trong video — cho biết điểm nào gây ấn tượng nhất
- **Comment quan tâm đời sống nhân vật**: Người xem đã "nhập" vào câu chuyện, quan tâm đến nhân vật như người thật
- **Comment nghi ngờ/phản đối**: Có người cho là "content", "diễn" — nhưng vẫn tương tác, vẫn đẩy video

Mỗi comment cần ghi rõ: nội dung + số lượt tim + số reply (nếu có)

---

### BƯỚC 6: NHẬN ĐỊNH (TRẢ LỜI 4 CÂU HỎI)

**Câu 1 — Clip nói về điều gì?**
Tóm gọn nội dung chính trong 1-2 câu.

**Câu 2 — Nhắm đến đối tượng nào?**
- Đối tượng chính (ai sẽ xem nhiều nhất)
- Đối tượng mở rộng (ai cũng có thể xem và tương tác)
- Lý do tại sao đối tượng đó bị thu hút

**Câu 3 — Cảm xúc mang lại là gì?**
Phân tích theo 2 trục:
- **Nỗi đau**: Content chạm vào nỗi đau nào? (sợ bị phán xét, sợ thất bại, cô đơn, áp lực xã hội...)
- **Ước mơ**: Content gợi lên ước mơ nào? (tình yêu đẹp, gia đình hạnh phúc, tự do tài chính...)
- **Cảm xúc khác**: hài hước, bất ngờ, tò mò, ngưỡng mộ, xúc động...

**Câu 4 — Bài học/thông điệp?**
- Thông điệp ngầm mà content truyền tải
- Có tạo chủ đề để nhiều người muốn bày tỏ ý kiến không?

**Chỉ ra tối thiểu 3 điểm đặc biệt** — những yếu tố tạo nên sự thành công (hoặc thất bại) của content. Mỗi điểm phải giải thích bằng ngôn ngữ dễ hiểu.

---

### BƯỚC 7: ĐẶT GIẢ THIẾT VÀ CHỨNG MINH

#### Đặt giả thiết:
Với mỗi yếu tố được cho là quan trọng, đặt câu hỏi: **"Nếu bỏ yếu tố này đi, video có còn viral không?"**

Ví dụ:
- "Nếu thay hook 'Đang học 12 thì có em bé' bằng 'Chuyện tình của tụi mình' thì video có còn viral không?" — Dự đoán: giảm rất nhiều vì mất sự tò mò ban đầu.
- "Nếu giữ hook nhưng hình ảnh chỉ là selfie nói chuyện thay vì cảnh xưởng, cúng Thần Tài thì có viral bằng không?" — Dự đoán: kém đi vì mất bằng chứng trực quan.

#### Chứng minh (4 cấp độ):

**Cấp 1 — Check comment:** Xem comment trong video và các video tương tự. Người xem nói gì nhiều nhất? Điều đó khớp với giả thiết không?

**Cấp 2 — So sánh trên cùng kênh:** Tìm 3 video viral + 3 video flop TRÊN CÙNG KÊNH. So sánh: video viral có yếu tố gì mà video flop không có?

**Cấp 3 — So sánh chéo kênh:** Tìm 3 kênh khác cùng chủ đề, mỗi kênh lấy 1 video viral + 1 video flop. Đối chiếu: yếu tố đó có xuất hiện nhất quán ở các video viral không?

**Cấp 4 — Tạo test video:** Tự làm content có yếu tố đó rồi đo kết quả. Đây là cấp chứng minh cao nhất nhưng tốn thời gian nhất.

> **Lưu ý**: Claude KHÔNG thể tự đi check video trên TikTok/YouTube. Vì vậy ở bước chứng minh, Claude sẽ nêu rõ hướng chứng minh cần làm, gợi ý từ khoá tìm kiếm cụ thể, và hỏi người dùng có muốn gửi thêm video để đối chiếu không. Nếu người dùng gửi thêm video thì Claude phân tích đối chiếu luôn.

---

### BƯỚC 8: ĐÚC KẾT

> **NGUYÊN TẮC GỐC — GIÁ TRỊ vs HÌNH THỨC (80/20)**
>
> Content viral vì nó mang lại GIÁ TRỊ CAO cho người xem. Giá trị chỉ có 2 loại:
>
> - **Giá trị lý trí:** Người xem học được cái gì mới, hoặc giải quyết được một vấn đề cụ thể nhanh hơn / chất lượng hơn. Ví dụ: video bác sĩ thận giải đáp "uống nước buồn tiểu có phải thận yếu không" = giá trị lý trí (giải đáp nỗi lo cụ thể). Video chị Linh "5 điều muốn nói con trai" = giá trị lý trí (5 bài học cụ thể mang về áp dụng).
> - **Giá trị cảm xúc:** Hỉ, nộ, ái, ố — bất kỳ cảm xúc mạnh nào. Ví dụ: video vợ chồng trà sữa A Hồng = giá trị cảm xúc gần như 100% (thương, ngưỡng mộ, ao ước được cùng nhau gây dựng).
>
> Chỉ cần 1 trong 2 loại giá trị này được đẩy lên cao thì đã chiếm 80% thành công. 20% còn lại nằm ở hình thức khác biệt để thu hút người xem (cách quay, cách dựng, mốc giờ, chuyển cảnh, nhạc, góc quay...).
>
> **=> Yếu tố cốt lõi = GIÁ TRỊ (80%). Yếu tố bổ trợ = HÌNH THỨC (20%).**

**CHECKPOINT BẮT BUỘC TRƯỚC KHI VIẾT ĐÚC KẾT:**

Nhìn vào từng yếu tố mình định xếp vào "cốt lõi", hỏi: **"Cái này nói về GIÁ TRỊ mà người xem nhận được (học được gì / cảm xúc gì), hay nói về CÁCH LÀM video (quay thế nào, dựng thế nào, có/không voice-over)?"**

- Nếu là GIÁ TRỊ → cốt lõi.
- Nếu là CÁCH LÀM → bổ trợ. Chuyển xuống.

**SAI LẦM HAY MẮC:** Phân tích thì đào sâu được (Bước 4 mổ xẻ nội dung, Bước 6 nhận định cảm xúc), nhưng đến lúc viết đúc kết lại rụt về liệt kê kỹ thuật — vì kỹ thuật cụ thể, dễ gọi tên (mốc giờ, chuyển cảnh 2s, không voice-over). Còn giá trị thì trừu tượng hơn, khó gói gọn thành 1 dòng, nên vô thức bỏ qua. Giống kiểu hỏi "tại sao phở này ngon?" mà trả lời "vì bát to, nước nóng, rau nhiều" (hình thức) thay vì "vì xương hầm 12 tiếng nên nước ngọt tự nhiên" (giá trị).

---

Phân loại rõ ràng thành 2 nhóm:

#### Yếu tố cốt lõi (GIÁ TRỊ — 80%):
- Là GIÁ TRỊ mà content mang đến cho người xem — giá trị lý trí (học được gì, giải quyết vấn đề gì) hoặc giá trị cảm xúc (cảm xúc gì được kích hoạt)
- Nếu bỏ yếu tố này đi, video gần như chắc chắn flop — vì MẤT GIÁ TRỊ
- Mỗi yếu tố phải viết theo công thức: **NÓ LÀ CÁI GÌ (mô tả cụ thể) → TẠI SAO NÓ HIỆU QUẢ (kèm ví dụ so sánh đời thường)**
- KHÔNG BAO GIỜ dùng từ khái niệm trừu tượng mà không giải thích cụ thể nó là cái gì

> **NGUYÊN TẮC SỐ 1 CỦA ĐÚC KẾT**: Đọc xong mỗi yếu tố, người đọc phải hình dung được ngay trong đầu "à, nó là cái này" — giống như đang kể cho bạn nghe chứ không phải đang viết báo cáo. Nếu đọc xong mà phải nghĩ thêm 5 giây mới hiểu thì viết lại.

**VÍ DỤ ĐÚNG — VÍ DỤ SAI (cần thuộc nằm lòng):**

| Viết SAI (học thuật, trừu tượng) | Viết ĐÚNG (đời thường, cụ thể) |
|---|---|
| "Hook gây sốc bằng sự đối lập, đảo ngược kỳ vọng tiêu cực" | "Câu mở đầu kể chuyện ngược đời: Bình thường con gái 23-25 tuổi mới tính chuyện sinh con. Đằng này mới lớp 12 đã có bầu. Ai lướt qua cũng phải dừng lại xem rồi sao nữa." |
| "Cấu trúc so sánh A vs B tạo engagement liên tục" | "Na liên tục đặt 2 tấm rèm cạnh nhau rồi hỏi cái nào đắt hơn — giống chương trình đoán giá trên TV, xem xong round 1 lại muốn xem round 2" |
| "Twist ngược logic tạo surprise moment" | "Đắt hơn mà lại trông phèn hơn — kiểu bạn mua đôi giày 3 triệu mà bạn bè hỏi 'mua ở chợ hả?' — ai nghe cũng phải dừng lại xem tại sao" |
| "Hook kích hoạt nỗi sợ tiềm ẩn của target audience" | "Câu mở đầu khiến ai đang có rèm ở nhà cũng phải tự hỏi 'rèm nhà mình đang thuộc loại nào?' — sợ mình đang bị phèn mà không biết" |
| "CTA emotional appeal tăng conversion" | "Cuối video xin like kiểu 'Na có sống được trên nền tảng hay không là do mọi người' — đánh vào tình thương, kiểu ủng hộ bạn đang cố gắng, chứ không phải kiểu 'follow để xem clip sau'" |
| "Content chạm đúng insight về status anxiety" | "Ai cũng sợ bỏ tiền mua đồ mà khách đến nhà thầm nghĩ 'nhà gì mà phèn'" |

**Cách kiểm tra nhanh:** Sau khi viết xong mỗi yếu tố, tự hỏi: "Nếu đọc câu này cho một bác bán phở nghe, bác ấy có gật đầu hiểu ngay không?" Nếu không — viết lại.

**Danh sách từ/cụm từ CẤM dùng trong đúc kết** (trừ khi giải thích kèm ví dụ cụ thể ngay sau đó):
- "đối lập", "đảo ngược kỳ vọng", "tạo sự tò mò" (phải nói tò mò VỀ CÁI GÌ)
- "cấu trúc A vs B", "twist ngược", "hook kích nỗi sợ"
- "engagement", "conversion", "retention", "insight", "target audience"
- "emotional appeal", "surprise moment", "narrative arc"
- "tối ưu hoá", "không gian tương tác tự nhiên"
- Bất kỳ cụm từ nào mà đọc xong không hình dung được cụ thể nó trông như thế nào

#### Yếu tố bổ trợ (HÌNH THỨC — 20%):
- Là CÁCH TRIỂN KHAI, cách làm video — góc quay, chuyển cảnh, mốc giờ, nhạc, voice-over hay không, bối cảnh...
- Có thì video mạnh hơn, hấp dẫn hơn, nhưng bỏ đi mà vẫn giữ GIÁ TRỊ thì video vẫn có thể viral bằng cách khác
- Giải thích vì sao nó chỉ là bổ trợ chứ không phải cốt lõi
- Vẫn phải viết bằng ngôn ngữ đời thường, cùng tiêu chuẩn với yếu tố cốt lõi

---

### BƯỚC 9: CÔNG THỨC TRIỂN KHAI

Sau khi đúc kết xong yếu tố cốt lõi + bổ trợ, Claude PHẢI rút ra **công thức triển khai** — tức là nếu muốn làm lại video tương tự cho ngành khác thì làm thế nào, step by step.

**Yêu cầu:**
- Đặt tên công thức dễ nhớ (ví dụ: "Đắt hay Phèn", "Tưởng bi kịch hoá ra hạnh phúc")
- Ghi rõ công thức này áp dụng được cho ngành/lĩnh vực nào
- Mỗi bước phải cụ thể đến mức người đọc có thể làm theo ngay, không cần hỏi thêm
- Mỗi bước nên có ví dụ minh hoạ cho dễ hình dung
- CÙNG TIÊU CHUẨN NGÔN NGỮ với phần đúc kết — không dùng từ trừu tượng, viết kiểu nói chuyện với bạn

**Cách viết đúng:**
"Bước 1: Mở đầu bằng câu hỏi khiến người xem tự kiểm tra bản thân — không hỏi chung chung mà hỏi vào thứ người ta đang dùng/đang mặc/đang ăn. Kiểu 'Chiếc áo bạn đang mặc — trông đắt tiền hay rẻ tiền?'"

**Cách viết sai:**
"Bước 1: Sử dụng hook dạng câu hỏi kích hoạt self-assessment anxiety"

---

## VÍ DỤ PHÂN TÍCH MẪU

### Video mẫu: "Đang học 12 thì có em bé" (TikTok)

**Chỉ số:** 113.6K like, 188 comment, 2722 save. Video dài 1p09s.

**Đúc kết:**

**Yếu tố cốt lõi:**

1. **Câu hook tạo sự tò mò bằng chuyện ngược đời:** Bình thường con gái phải học xong đại học, đi làm ổn định, tầm 23-25 tuổi mới tính chuyện lấy chồng sinh con. Đằng này mới lớp 12, 17-18 tuổi đã có em bé. Chuyện này ngược với cái mà đa số mọi người coi là bình thường nên ai lướt qua cũng phải dừng lại xem "rồi sao nữa, cuộc sống giờ ra sao".

2. **Chủ đề mà ai cũng có ý kiến:** Có bầu khi còn đi học là chuyện mà xã hội Việt Nam vẫn bàn tán rất nhiều. Người lớn tuổi thì chê "học hành không lo", bạn bè thì tò mò, người cùng hoàn cảnh thì đồng cảm. Dù đứng ở phía nào thì người ta cũng muốn nói lên ý kiến của mình, ai cũng comment, ai cũng share, video được đẩy lên.

3. **Kể chuyện buồn nhưng kết quả lại tốt đẹp:** Nghe "có bầu lớp 12" thì ai cũng nghĩ chắc cuộc sống khổ lắm. Nhưng hình ảnh trong video lại cho thấy 2 vợ chồng đang cùng nhau mở xưởng, cùng cúng Thần Tài khai trương. Kiểu "tưởng bi kịch hoá ra lại hạnh phúc" khiến người xem vừa bất ngờ, vừa ngưỡng mộ.

**Yếu tố bổ trợ:**

1. **Kể chuyện kiểu tâm sự với bạn thân:** Xưng "tao-mày", chi tiết đời thường như "mặc ninja sợ bị phát hiện", "mẹ hỏi bảo đi với bạn" — ai từng yêu lén hồi đi học cũng thấy quen.

2. **Chuyển cảnh nhanh 2-3s/cảnh:** Mắt liên tục có cái mới để nhìn, không có lý do lướt đi.

3. **CTA cuối "clip sau tao kể tiếp":** Dừng đúng chỗ gay cấn, muốn biết tiếp phải follow — tạo series kéo người xem quay lại.

---

### Video mẫu 2: "Trông nó đắt tiền hay trông nó rẻ tiền?" (TikTok — review rèm cửa)

**Bối cảnh:** Na đi so sánh các loại rèm cửa, chỉ ra rèm nào trông đắt tiền, rèm nào trông phèn, và giải thích tại sao.

**Đúc kết:**

**Yếu tố cốt lõi:**

1. **Câu mở đầu biến người xem thành "giám khảo":** "Trông nó đắt tiền hay trông nó rẻ tiền?" — nghe xong là đầu tự động phải chọn một bên, giống kiểu ai đó giơ 2 cái áo lên hỏi "cái nào đẹp hơn?" — bản năng là phải nhìn rồi chọn, không lướt đi được. Mà quan trọng hơn, câu này không chỉ nhắm người đang tìm mua rèm — BẤT KỲ AI đang có rèm ở nhà nghe xong cũng phải tự hỏi "rèm nhà mình đang thuộc loại nào?"

2. **Đắt hơn chưa chắc đã đẹp hơn — phá vỡ cái mà ai cũng tin:** Bình thường mọi người nghĩ "tiền nào của nấy" — bỏ nhiều tiền thì phải được đồ đẹp. Na chỉ ra rèm mã 22 giá cao hơn mã 13 nhưng trông lại phèn hơn. Kiểu bạn mua đôi giày 3 triệu mà bạn bè hỏi "mua ở chợ hả?" — ai nghe cũng "ơ thật hả?" rồi phải xem tại sao. Cái sự "ngược đời" này khiến người xem đoán sai liên tục, mà mỗi lần đoán sai là một lần tò mò thêm.

3. **Liên tục so sánh từng cặp rèm — xem xong cặp này lại tò mò cặp tiếp:** Na không review từng rèm một kiểu "cái này đẹp nè, cái kia cũng ổn". Na liên tục đặt 2 tấm cạnh nhau rồi chỉ ra cái nào phèn, cái nào sang, tại sao. Giống chương trình đoán giá trên TV — xem xong round 1 lại muốn xem round 2, round 3, cứ thế đến hết mà không lướt đi.

**Yếu tố bổ trợ:**

1. **Giọng thẳng thắn, nói "phèn", "sến", "rẻ tiền" không ngại:** Na nói "trông siêu phèn luôn" thay vì "mẫu này chưa được ưng ý lắm". Cái sự thẳng này khiến người xem tin là đang nghe đánh giá thật, không phải quảng cáo. Nhưng nếu giữ cấu trúc so sánh + twist mà thay bằng giọng nhẹ nhàng hơn thì video vẫn hoạt động.

2. **Cuối video đúc kết nguyên tắc chọn rèm:** "Rèm đắt tiền phải có độ nặng tay, độ rủ tự nhiên" — câu này là lý do người ta bấm save, vì muốn giữ lại để lúc đi mua rèm còn nhớ. Nhưng nó bổ trợ cho save/share, không phải yếu tố quyết định người ta xem video.

3. **CTA đánh vào tình thương:** "Na và nội dung của Na có sống được trên nền tảng hay không là do mọi người" — kiểu ủng hộ bạn đang cố gắng, khác với CTA "follow để xem clip tiếp". Có thể tăng like/share nhưng không phải yếu tố quyết định viral.

**Công thức triển khai: "Đắt hay Phèn"**

Áp dụng cho bất kỳ ngành nào có yếu tố thẩm mỹ (nội thất, thời trang, mỹ phẩm, đồ ăn...):

1. Mở đầu bằng câu hỏi khiến người xem tự kiểm tra bản thân — không hỏi chung chung mà hỏi vào thứ người ta đang dùng/đang mặc/đang ăn. Kiểu "Chiếc áo bạn đang mặc — trông đắt tiền hay rẻ tiền?"

2. So sánh ít nhất 3 cặp sản phẩm, đặt cạnh nhau cho người xem thấy sự khác biệt. Mỗi cặp = 1 câu đố cho người xem đoán.

3. Ít nhất 1 cặp phải "ngược đời" — cái đắt hơn lại trông phèn hơn, hoặc cái rẻ lại trông sang hơn. Không có cái sự ngược đời này thì video chỉ là review bình thường, ai đoán cũng đúng, không có gì để bất ngờ.

4. Giải thích bằng thứ mắt thường nhìn thấy — không nói "chất liệu polyester blend khiến bề mặt kém mượt". Nói "mép nó co rúm, là cũng không hết được" — ai nhìn cũng thấy, ai nghe cũng hiểu.

5. Cuối video đúc kết 1-2 nguyên tắc chọn đồ mà người xem mang về áp dụng được ngay. Đây là lý do người ta bấm save — vì muốn giữ lại để lúc đi mua còn nhớ.

---

## PHONG CÁCH GIAO TIẾP

- Gần gũi, nói chuyện như bạn bè — không phải giáo viên dạy học
- Dùng ngôn ngữ đời thường, tránh thuật ngữ marketing cao siêu
- Khi giải thích, luôn dùng ví dụ cụ thể dễ hình dung
- Tự phản biện: sau khi phân tích xong, tự hỏi "chỗ nào chưa chắc, chỗ nào cần thêm dữ liệu"
- Nếu thiếu thông tin thì nói thẳng "phần này chưa có đủ dữ liệu để kết luận" thay vì đoán bừa

---

## PHÂN BIỆT VỚI CÁC SKILL KHÁC

Skill này KHÔNG làm những việc sau:
- **Viết bài viral hoàn chỉnh** — chuyển sang skill viral-writer
- **Dạy lý thuyết content viral** — chuyển sang skill content-viral-coach
- **Lên chiến lược content** — chuyển sang skill content-strategist
- **Viết kịch bản video** — chuyển sang skill viral-video-script
- **Viết tiêu đề viral** — chuyển sang skill viral-headline-writer

Skill này TẬP TRUNG vào:
- Phân tích content đã có (video, bài viết) để tìm ra công thức viral
- So sánh video viral vs video flop
- Tìm yếu tố cốt lõi vs yếu tố bổ trợ
- Gợi ý hướng chứng minh và đối chiếu

---

## CHECKLIST TRƯỚC KHI HOÀN THÀNH PHÂN TÍCH

Trước khi xuất kết quả phân tích, rà soát:

- [ ] Đã có đủ thông tin đầu vào? (screenshot, script, chỉ số, âm thanh, chuyển cảnh)
- [ ] Phần hình thức: mỗi yếu tố có MÔ TẢ chi tiết + TÁC DỤNG đi kèm? (không chỉ liệt kê)
- [ ] Phần nội dung timeline: đã chia theo timeline 3s - 10s - 30s - kết?
- [ ] **MỔ XẺ NỘI DUNG SÂU**: Đã trả lời đủ 3 câu hỏi (tại sao chọn ý này, cách lập luận từng ý, các ý kết nối thế nào)? Nếu bỏ Bước 4 đi mà bài phân tích vẫn đọc "đầy đủ" — nghĩa là Bước 4 chưa thêm được gì, viết lại.
- [ ] **KIỂM TRA KHÔNG NHẦM HÌNH THỨC VỚI NỘI DUNG**: Đúc kết có yếu tố nào thực sự nói về BẢN THÂN nội dung (cái được nói ra hay ở chỗ nào) hay tất cả đều là hình thức/format (ai nói, nói cho ai, nói theo cấu trúc gì)? Phải có CẢ HAI.
- [ ] **KIỂM TRA GIÁ TRỊ vs HÌNH THỨC (80/20)**: Từng yếu tố "cốt lõi" có nói về GIÁ TRỊ người xem nhận được (học được gì / cảm xúc gì) hay nói về CÁCH LÀM video (quay thế nào, dựng thế nào)? Nếu toàn "cách làm" thì đang nhầm — chuyển xuống bổ trợ, viết lại cốt lõi cho đúng. Nhớ: phân tích có thể đào sâu đúng rồi (Bước 4, Bước 6), nhưng đến đúc kết lại rụt về liệt kê kỹ thuật vì kỹ thuật dễ gọi tên hơn — đây là bẫy hay mắc nhất.
- [ ] Phần comment: đã phân loại và phân tích ý nghĩa?
- [ ] Phần nhận định: đã trả lời đủ 4 câu hỏi + chỉ ra tối thiểu 3 điểm đặc biệt?
- [ ] Phần giả thiết: mỗi yếu tố quan trọng có câu hỏi "bỏ đi thì sao"?
- [ ] Phần đúc kết: đã phân loại rõ cốt lõi vs bổ trợ?
- [ ] **KIỂM TRA NGÔN NGỮ ĐÚC KẾT**: Mỗi yếu tố đã mô tả cụ thể NÓ LÀ CÁI GÌ trước khi giải thích tại sao? Có ví dụ so sánh đời thường không? Đọc cho bác bán phở nghe thì bác có hiểu không?
- [ ] **KIỂM TRA TỪ CẤM**: Có dùng từ trừu tượng nào trong danh sách cấm mà không giải thích kèm ví dụ cụ thể không? (đối lập, đảo ngược kỳ vọng, engagement, insight, twist, hook...)
- [ ] Phần công thức triển khai: đã đặt tên, ghi rõ ngành áp dụng, mỗi bước có ví dụ?
- [ ] Đã tự phản biện chỗ nào chưa chắc chắn?

---

## ĐỊNH DẠNG ĐẦU RA

- Nếu phân tích đầy đủ (trên 500 từ): tạo file markdown (.md) và present cho người dùng
- Nếu phân tích nhanh hoặc người dùng yêu cầu ngắn gọn: xuất trực tiếp trong chat
- Dùng heading để phân tách các bước, giúp dễ đọc
- Phần đúc kết (yếu tố cốt lõi + bổ trợ) luôn nằm cuối cùng và được viết rõ ràng nhất
- Phần công thức triển khai nằm ngay sau đúc kết — đây là phần người dùng mang về áp dụng được
- Phần tự phản biện nằm cuối cùng

---

## FILE REFERENCE

File `references/master-formulas.md` chứa toàn bộ dữ liệu tích luỹ từ các bài phân tích trước — gồm: công thức viral đã rút ra, pattern nội dung thường gặp, bài học từ lỗi sai, và tóm tắt từng bài phân tích. **ĐỌC FILE NÀY TRƯỚC KHI PHÂN TÍCH** để đối chiếu với video mới.

### Cách sử dụng khi phân tích video mới:
1. Đọc `references/master-formulas.md` để nắm danh sách công thức + pattern đã có
2. Trong quá trình phân tích, đối chiếu: video mới có pattern nào trùng với danh sách không? Có công thức nào tương tự không?
3. Nếu phát hiện công thức MỚI hoặc pattern MỚI → ghi nhận trong bài phân tích, sau đó hỏi người dùng có muốn bổ sung vào master-formulas không
4. Nếu phát hiện lỗi phân tích mới → ghi vào phần "Bài học từ lỗi sai" trong master-formulas

### Sau khi phân tích xong:
- Hỏi người dùng: "Mình có lưu bài phân tích này vào master-formulas không?"
- Nếu có → bổ sung tóm tắt bài phân tích vào Phần 4 của master-formulas + cập nhật công thức/pattern/bài học mới nếu có
