---
name: tra-cuu-phap-luat
description: Tra cứu và kiểm chứng văn bản pháp luật Việt Nam bằng Lawgical trước khi trích dẫn. Dùng cho MỌI câu hỏi về pháp luật Việt Nam - tra cứu luật, tìm một Điều/Khoản cụ thể, hỏi một văn bản còn hiệu lực hay không, so sánh hai văn bản, tra nghĩa vụ / thời hạn / mức phạt, hoặc kiểm tra Lawgical có văn bản X hay không. Dùng cả khi câu hỏi viết bằng tiếng Anh (Vietnamese law, decree, circular). Skill này bắt buộc một quy trình xác minh bốn bước - đúng văn bản, đủ nội dung, còn hiệu lực, đúng nguồn - vì kho dữ liệu có thể trả về kết quả nghe rất thuyết phục nhưng sai. KHÔNG dùng cho pháp luật nước ngoài, và không thay thế ý kiến của luật sư có chứng chỉ.
license: Proprietary
compatibility: Cần plugin (connector) Lawgical tại https://legal.lawgical.vn/mcp đã kết nối và được gắn vào đoạn chat đang dùng.
metadata:
  author: Lawgical
  version: "1.1"
  homepage: https://lawgical.vn
---

# Tra cứu & kiểm chứng văn bản pháp luật Việt Nam

Lawgical lập chỉ mục hơn 150.000 văn bản pháp luật Việt Nam từ nguồn chính thức của nhà
nước. Skill này không dạy cách gọi công cụ — nó dạy cách **không trả lời sai**.

Lý do cần nó: kho dữ liệu tra cứu theo cơ chế khớp mờ. Khi không tìm thấy thứ bạn hỏi, nó
thường **không báo lỗi** mà trả về một văn bản gần giống. Kết quả trông hoàn chỉnh, có số
ký hiệu, có điều khoản — và là văn bản khác. Quy trình kiểm chứng ở dưới là thứ chặn điều đó.

## Ba quy tắc không được phá

1. **Không trả lời pháp luật Việt Nam bằng trí nhớ.** Luôn tra cứu. Luật Việt Nam sửa đổi
   liên tục và số hiệu Điều rất dễ nhớ nhầm.
2. **Không trích dẫn khi chưa chạy đủ 4 bước kiểm chứng.** Không có ngoại lệ cho văn bản
   "trông đúng rồi".
3. **Thiếu dữ liệu thì nói thiếu.** Một câu trả lời pháp lý sai gây thiệt hại lớn hơn nhiều
   so với việc nói rõ phần nào chưa kiểm chứng được.

## Công cụ

Các công cụ Lawgical xuất hiện sẵn khi plugin đã được **gắn vào đoạn chat đang dùng**. Nếu
không thấy công cụ nào, xem phần [Xử lý sự cố](#xử-lý-sự-cố) — gần như luôn là do chưa gắn
plugin vào chat, không phải mất kết nối.

Mỗi lần gọi trả về nội dung tính **1 lượt** vào hạn mức ngày của tài khoản; hạn mức đặt lại
lúc **00:00 giờ Việt Nam (ICT)**. `get_account_status()` cho biết hạn mức và số lượt còn lại.

| Công cụ | Tính lượt? | Dùng để |
|---|---|---|
| `get_account_status()` | **Không tính lượt** | Xem hạn mức và số lượt đã dùng / còn lại hôm nay |
| `search_legal_docs(keywords)` | 1 lượt | **Bước đầu tiên.** Tìm theo từ khóa trên toàn kho |
| `get_summary(query)` | 1 lượt | Mục lục Chương / Mục / Điều. **Dùng trước `get_document` với luật dài** để định vị đúng Điều mà không phải tải 60.000 ký tự |
| `get_document(query)` | 1 lượt | Toàn văn theo tên, doc id, hoặc số ký hiệu (ví dụ `"20/2023/QH15"`). Văn bản thiếu nội dung: xem phần cuối |
| `get_laws(tinh_trang, keyword, limit, offset)` | 1 lượt | Duyệt riêng **Luật** do Quốc hội ban hành, không gồm Nghị định / Thông tư hướng dẫn và **không gồm văn bản hợp nhất**. Mặc định chỉ hiện Luật còn hiệu lực; `tinh_trang="tất cả"` hiện cả Luật đã hết hiệu lực |
| `check_compliance(question)` | 1 lượt | Cùng cơ chế tìm nhưng nhận đầu vào dạng câu hỏi. Trả về trích đoạn thô để **bạn** phân tích — công cụ không tự kết luận |

**Tra không ra thì không mất lượt.** Chỉ những lần thực sự trả về nội dung mới bị tính; lần
gọi lỗi cũng không tính. Vì vậy **cứ tra khi chưa chắc chắn** — thứ nên tránh là tiêu lượt để
tải lại văn bản đã có sẵn trong đoạn chat.

Vài thói quen tiết kiệm lượt:

- Gọi `get_account_status()` trước khi làm việc nhiều bước nếu tài khoản có hạn mức ngày —
  không tốn lượt mà biết còn bao nhiêu.
- Dùng `get_summary` để tìm đúng Điều, thay vì `get_document` cả một bộ luật.
- Đã tải văn bản rồi thì đọc lại trong ngữ cảnh, đừng gọi lại công cụ.

## Quy trình

1. **`search_legal_docs`** với từ khóa tiếng Việt bao quát khái niệm, không phải một từ trơ.
   Nên kèm cách diễn đạt của Điều / Chương, ví dụ `"quyền hạn chế xử lý dữ liệu cá nhân Điều 10"`.
   Từ khóa tiếng Anh vẫn chạy nhưng khớp kém hơn nhiều — hãy dịch câu hỏi sang thuật ngữ
   pháp lý tiếng Việt trước khi tìm.
2. **Đọc tiêu đề từng kết quả trước khi chọn.** Kết quả khớp số ký hiệu thường **không phải**
   văn bản đó mà là văn bản *dẫn chiếu* tới nó (xem kiểm chứng 4).
3. **`get_summary`** nếu là văn bản dài, để định vị đúng Điều cần đọc.
4. **`get_document`** lấy toàn văn phần cần dùng.
5. **Chạy 4 bước kiểm chứng bên dưới** — trước khi đọc nội dung, không phải sau.
6. Đọc đúng Điều / Khoản và trả lời từ chính văn bản.
7. **Trích dẫn chính xác**: Điều / Khoản / Điểm, kèm số ký hiệu và tình trạng hiệu lực.

**Tra cứu mỗi lần một định danh.** Thử số ký hiệu trước (`"91/2025/QH15"`); nếu sai thì thử
riêng tên văn bản (`"Luật Bảo vệ dữ liệu cá nhân"`). **Đừng bao giờ ghép hai thứ** — chuỗi
`"91/2025/QH15 Bảo vệ dữ liệu cá nhân"` không khớp chính xác với chỉ mục nào nên rơi xuống
xếp hạng mờ và trả về một văn bản không liên quan mà không hề báo.

Lưu ý số ký hiệu **không duy nhất**: 34 tỉnh thành đều có thể có `01/2024/QĐ-UBND` của
riêng mình. Luôn kiểm tra **Cơ quan ban hành**, không chỉ Số ký hiệu.

## Bốn bước kiểm chứng — bắt buộc trước khi trích dẫn

Kho dữ liệu này sai theo bốn kiểu khác nhau, và mỗi bước dưới đây chỉ mất vài giây, không
tốn thêm lượt nào (chỉ đọc lại thứ đã có trong ngữ cảnh).

> **Checklist:** ① Đúng văn bản? ② Đủ nội dung? ③ Còn hiệu lực? ④ Đúng nguồn?
> **Làm cả bốn.** Đừng bỏ bước nào vì văn bản "trông đúng rồi" — trông đúng chính là kiểu
> lỗi ở đây.

### ① Đúng văn bản — có phải văn bản tôi yêu cầu không?

`get_document` đôi khi trả về một văn bản **không liên quan** thay vì báo không tìm thấy.
Đọc dòng `Số ký hiệu` trong bảng thông tin và xác nhận nó khớp đúng thứ đã yêu cầu.

Chỉ riêng bước này là khác biệt giữa một câu trả lời đúng và một câu trả lời sai nhưng được
trích dẫn đầy tự tin. Đây là kiểu lỗi phổ biến nhất của hệ thống.

### ② Đủ nội dung — đã có toàn văn chưa?

Hai kiểu thiếu:

- **Chỉ có metadata**: đúng bảng thông tin, vài trăm ký tự, không có điều nào.
- **Bị cắt giữa chừng**: có nội dung thật nhưng dừng đột ngột.

Kiểm tra hai dấu hiệu: số hiệu Điều có **liên tục** không, và văn bản có **kết thúc đúng chỗ**
không — với một Luật là phần ký của Quốc hội (`Luật này được Quốc hội … thông qua ngày …`
rồi tới dòng CHỦ TỊCH QUỐC HỘI). Nếu dãy Điều nhảy số, hoặc kết thúc giữa câu, **đừng trích dẫn**.

Nếu có công cụ chạy code, kiểm tra bằng máy thay vì bằng mắt — dán toàn văn vào biến `d`:

```python
import re
arts = sorted({int(m) for m in re.findall(r'Điều (\d+)\.', d)})
print('số Điều:', len(arts), '| từ', arts[0], 'đến', arts[-1])
print('thiếu:', [n for n in range(arts[0], arts[-1] + 1) if n not in arts] or 'không')
print('kết thúc:', repr(d[-160:]))
```

Danh sách `thiếu` phải rỗng và phần `kết thúc` phải là khối ký. Không chạy được code thì
kiểm tra bằng mắt: đọc số hiệu Điều cuối cùng rồi cuộn xuống cuối văn bản.

**Nếu văn bản thiếu nội dung** (chỉ có bảng thông tin, hoặc thiếu điều ở giữa): đừng trích
phần không có. Nói rõ phần nào của văn bản chưa kiểm chứng được, chỉ trích phần đã kiểm
chứng, không suy diễn phần thiếu, và chỉ người dùng tới bản chính thức do cơ quan ban hành
công bố.

### ③ Còn hiệu lực — đây có còn là luật hiện hành không?

Đọc `Tình trạng hiệu lực` trên chính văn bản, rồi kiểm tra xem đã có **bản hợp nhất** mới hơn chưa.

**Văn bản hợp nhất (số ký hiệu dạng `…/VBHN-VPQH`) đã gộp mọi sửa đổi, bổ sung sau này và là
bản thể hiện luật hiện hành.** `get_laws` chỉ liệt kê **Luật**, nên **không bao giờ** trả về
văn bản hợp nhất. Tìm nó bằng `search_legal_docs`, và nhớ rằng một luật có thể có **nhiều**
bản hợp nhất qua các năm (ví dụ tại thời điểm tháng 10/2026):

```
search_legal_docs("văn bản hợp nhất Luật Giao dịch điện tử")
  → 154/2026/VBHN-LQ-VPQH   (xác thực 28/09/2026)   ← bản mới nhất
  → 42/VBHN-VPQH            (xác thực 27/02/2025)
  → 20/2023/QH15            (luật gốc)
```

Trích dẫn luật gốc 2023, hay một bản hợp nhất cũ, khi đã có bản hợp nhất mới hơn là **sai
về luật hiện hành**. Ưu tiên bản hợp nhất có **ngày xác thực mới nhất**, và nói rõ đang dùng
bản nào.

> **Suy ra:** đừng kết luận Lawgical không có một văn bản chỉ vì `get_laws` không trả về gì.
> `get_laws` chỉ có Luật, và mặc định chỉ hiện Luật còn hiệu lực. Chạy lại với
> `tinh_trang="tất cả"`, rồi tìm bằng `search_legal_docs` hoặc `get_document` theo số ký hiệu.

### ④ Đúng nguồn — đây là văn bản đó, hay văn bản trích nó?

Tìm theo số ký hiệu phần lớn trả về những văn bản **dẫn chiếu** nó ở phần `Căn cứ`.

Ví dụ thật: tìm `20/2023/QH15` trả về 8 kết quả và **không kết quả nào là Luật Giao dịch
điện tử** — toàn bộ là Quyết định của các tỉnh và quy chuẩn kỹ thuật QCVN có trích dẫn luật
này. Nếu tiêu đề là văn bản địa phương hoặc quy chuẩn kỹ thuật trong khi bạn đang hỏi về
một Luật, thì bạn đang đọc phần dẫn chiếu, không phải luật.

### Dấu hiệu phải dừng lại và kiểm chứng lại

| Ý nghĩ | Thực tế |
|---|---|
| "Tìm thấy rồi — nó trả về một văn bản rất dài" | Độ dài không chứng minh gì. Kiểm tra `Số ký hiệu`. |
| "8 kết quả, kho dữ liệu tốt đấy" | Có thể **tất cả** chỉ là văn bản dẫn chiếu, không cái nào là văn bản cần tìm. |
| "`get_laws` không trả về gì, vậy là không có" | `get_laws` chỉ có Luật, mặc định chỉ Luật còn hiệu lực. Chạy lại với `tinh_trang="tất cả"` và tìm bằng `search_legal_docs`. |
| "Tình trạng ghi Còn hiệu lực, vậy đây là bản hiện hành" | Có thể đã có bản hợp nhất thay thế. Tìm `VBHN`. |
| "Nội dung trông đủ mà, dài thế còn gì" | Kiểm tra tính liên tục của Điều và phần ký cuối văn bản. |
| "Tôi tóm tắt nghĩa vụ này theo hiểu biết chung" | Phải trích nguyên văn Điều. Kho dữ liệu là nguồn đúng, không phải trí nhớ. |

## Ví dụ một lượt tra cứu đầy đủ

**Người dùng hỏi:** "Luật Giao dịch điện tử quy định thế nào về chữ ký điện tử?"

1. `search_legal_docs("chữ ký điện tử giao dịch điện tử")` → nhiều kết quả, đọc tiêu đề từng cái.
   Phần lớn là Quyết định cấp tỉnh trích dẫn luật → **kiểm chứng ④ loại chúng ra**.
2. `search_legal_docs("văn bản hợp nhất Luật Giao dịch điện tử")` → thấy luật gốc
   `20/2023/QH15` và **hai** bản hợp nhất: `42/VBHN-VPQH` (xác thực 27/02/2025) và
   `154/2026/VBHN-LQ-VPQH` (xác thực 28/09/2026) → **kiểm chứng ③: dùng bản mới nhất**.
3. `get_summary("154/2026/VBHN-LQ-VPQH")` → mục lục cho thấy chữ ký điện tử nằm ở Chương III
   (Điều 22).
4. `get_document("154/2026/VBHN-LQ-VPQH")` → kiểm tra `Số ký hiệu` và `Cơ quan ban hành`
   khớp (**①**), dãy Điều liên tục và có phần cuối văn bản (**②**).
5. Đọc đúng Điều trong Chương III, trích nguyên văn.

**Trả lời:** nêu nội dung theo đúng Điều / Khoản, ghi rõ nguồn là *Văn bản hợp nhất
154/2026/VBHN-LQ-VPQH, xác thực ngày 28/09/2026* (hợp nhất Luật Giao dịch điện tử
20/2023/QH15), và nói rõ đây là bản hợp nhất mới nhất chứ không phải luật gốc 2023.

## Khi văn bản thiếu hoặc chỉ có metadata

**Dấu hiệu:** `get_document` chỉ trả về bảng thông tin (Số ký hiệu / Loại văn bản / Ngày ban
hành …) mà không có điều nào, hoặc không tìm thấy gì.

1. **Gọi lại `get_document` với đúng số ký hiệu**, hoặc riêng tên đầy đủ của văn bản (ví dụ
   `"Luật Bảo vệ dữ liệu cá nhân"`). Hai dạng này đều khớp chính xác; một chuỗi ghép cả hai
   hay từ khóa chung chung mới rơi vào xếp hạng mờ.
2. **Kiểm tra lại chính định danh.** Số ký hiệu có nhiều biến thể — thực tế có cả
   `40 /2026/TT-BCT` với một dấu cách lạc trước dấu gạch chéo. Sai một ký tự là không khớp
   được ở bước 1.
3. **Nếu là Luật, chạy lại `get_laws` với `tinh_trang="tất cả"`** để loại khả năng bị bộ lọc
   mặc định (chỉ Luật còn hiệu lực) che.
4. **Chạy lại `search_legal_docs`** với một cụm từ đặc trưng trong nội dung của văn bản,
   rồi kiểm chứng lại từ đầu.
5. **Vẫn không có thì nói rõ là chưa kiểm chứng được văn bản đó**, và chỉ người dùng tới
   bản chính thức do cơ quan ban hành công bố.

## Cách trả lời

- **Không đưa ra ý kiến pháp lý như thể của chính mình.** Thuật lại văn bản nói gì, trích
  điều luật, và nêu rõ khi nào cần luật sư có chứng chỉ.
- **Trích nguyên văn với nghĩa vụ / thời hạn / mức phạt — không diễn giải.** Cách soạn luật
  Việt Nam rất chặt về số ngày, mức phạt và ngưỡng áp dụng; một câu diễn giải làm rơi chữ
  "làm việc" khỏi "15 ngày làm việc" là đã đổi mất câu trả lời.
- **Nêu ngày có hiệu lực.** Một luật có hiệu lực từ 01/07/2024 trả lời khác cho câu hỏi về
  tình huống năm 2023.
- **Luôn dẫn tên văn bản kèm số ký hiệu**, và ghi rõ đang dùng bản gốc hay bản hợp nhất.
- **Trả lời bằng ngôn ngữ của người dùng** (mặc định tiếng Việt), nhưng giữ nguyên thuật ngữ
  pháp lý tiếng Việt kể cả khi trả lời bằng tiếng Anh.
- Nếu kho dữ liệu và giả định của người dùng khác nhau, hãy cho họ xem chính văn bản.

## Xử lý sự cố

**Không thấy công cụ Lawgical nào, hoặc ChatGPT nói đại ý "tôi thấy có connector Lawgical
nhưng không gọi được".**
Đây là tình huống hay gặp nhất và **không phải lỗi kết nối**: ChatGPT không tự bật plugin cho
mọi đoạn chat. Bấm biểu tượng plugin ở ô nhập tin nhắn và gắn Lawgical vào đoạn chat này.

**"Authorization with Lawgical failed", hoặc kết nối xong nhưng không có công cụ nào.**
Nếu plugin được tạo bằng một URL Lawgical cũ, hoặc lần đăng nhập trước bị gián đoạn, hãy
**xóa hẳn plugin và thêm lại** rồi đăng nhập lại; kết nối lại cái cũ sẽ không chạy, vì client
giữ token gắn với URL và cấu hình ban đầu.

**"Your session has expired. You can reconnect to re-authorize."**
Kết nối lại plugin Lawgical. Nếu lặp lại, hãy báo cho Lawgical qua https://lawgical.vn/support.

**"Không thể tra cứu: đã dùng hết … lượt tra cứu hôm nay."**
Tài khoản đã dùng hết hạn mức ngày; hạn mức đặt lại lúc 00:00 giờ Việt Nam.
`get_account_status()` không tính lượt và cho biết con số chính xác. Các lần tra không ra kết
quả **không** bị tính, nên con số này chỉ gồm những lần thành công.

**Chưa cài Lawgical.**
Cài Lawgical từ mục **Plugins** của ChatGPT hoặc Codex, rồi đăng nhập tài khoản Lawgical khi
được hỏi. Hướng dẫn kèm ảnh: https://lawgical.vn/cai-dat
