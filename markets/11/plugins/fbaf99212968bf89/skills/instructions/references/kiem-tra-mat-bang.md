# Kiểm mặt bằng có phép đo

## Khi dùng

Dùng khi đã có số đo hoặc tọa độ đủ để kiểm phòng, diện tích, đồ đạc, cửa và ràng buộc sửa. Với ý tưởng ngắn chưa cần đo, trả gợi ý trước; không biến mọi câu hỏi thành yêu cầu dựng mô hình. Với 20 phòng hoặc nhiều phương án, ưu tiên executor thay tính nhẩm rời rạc.

Gói có Python standard library `scripts/kiem_tra_mat_bang.py`, không mạng, không dependency ngoài, không ghi CAD. Chỉ chạy nếu runtime cho đọc script và chạy Python. Nếu không có runtime, không báo phép đo đã chạy. Không cần gọi MCP/đòi bridge cho việc phân tích file dữ liệu cục bộ được cung cấp.

## Dữ liệu do trợ lý chuẩn bị

Từ bản vẽ/spec/lời khách tạo JSON, giữ nguồn cho từng đối tượng. Khách chỉ cần cung cấp điều họ biết; không yêu cầu khách điền schema. `source=measured` khi có phép đo/bản vẽ xác minh, `client` khi khách khai, `assumed` khi giả định. Không đổi source chỉ để đạt. Rectangle là vùng thông thủy/không gian sử dụng do đầu vào mô tả; executor không tự trừ tường, cột hoặc shaft chưa cung cấp.

Schema v1: `revision`, `units` (`m` hoặc `mm`), `floors`, `rooms`, `doors`, `furniture`. Mỗi đối tượng có `id` duy nhất; mọi tầng/phòng có `rect=[x,y,width,height]`. `floor` trỏ ID tầng. Tọa độ dùng cùng một hệ trục; không tự suy scale từ pixel/phối cảnh.

- Phòng lồng: `parent_id` trỏ phòng bao; executor trừ hợp các phòng con khỏi diện tích phòng cha. Tổng dùng hợp hình theo từng tầng, không cộng trùng. Diện tích này chưa tự là diện tích pháp lý của công trình.
- Đồ: `room_id`, `rect` và `clearance_rect` tùy chọn. Vùng dùng lấy từ kích thước thiết bị/người sử dụng/yêu cầu dự án có nguồn. Cần tính cửa tủ, kéo ghế, đứng dùng; thiếu vùng dùng giữ phần đó chưa kiểm.
- Cửa: `start=[x,y]`, `end=[x,y]` trên biên, `connects=[roomA,roomB]`, hoặc một phía `outside`. `measurement=clear` chỉ khi đoạn là số đo khoảng mở lọt lòng thực, không phải chiều rộng cánh/family. `use_zone` tùy chọn là chữ nhật cần giữ trống, không phải phép quét cánh liên tục.
- `requirements` tùy chọn có `source`, `min_room_areas_m2` và `min_clear_door_width_m` (maps từ ID sang số). Ngưỡng có đơn vị trong tên trường nên luôn m²/m dù geometry dùng mm. Ngưỡng khai báo không tự thành tiêu chuẩn đã kiểm chứng.
- Baseline có `locks=[{"id":"stair-zone","fields":["rect","floor"]}]`; candidate được kiểm theo khóa baseline, không được tự bỏ khóa để được chấp nhận. Dữ liệu nào chưa có thì không tự tạo thành baseline thật.

Ví dụ cấu trúc tối thiểu (fixture minh họa, không phải thiết kế đạt):

```json
{"schema_version":1,"revision":"candidate-01","units":"m","floors":[{"id":"f1","rect":[0,0,8,6],"source":"client"}],"rooms":[{"id":"living","floor":"f1","rect":[0,0,4,6],"source":"client"},{"id":"kitchen","floor":"f1","rect":[4,0,4,6],"source":"assumed"}],"doors":[{"id":"entry","floor":"f1","start":[0,1],"end":[0,2],"connects":["outside","living"],"measurement":"clear","source":"client"},{"id":"d1","floor":"f1","start":[4,1],"end":[4,2],"connects":["living","kitchen"],"measurement":"clear","source":"assumed"}],"furniture":[]}
```

## Chạy và đọc kết quả

Từ thư mục skill, với các đường dẫn runtime thật đã được xác minh:

```sh
python3 scripts/kiem_tra_mat_bang.py spec.json --baseline baseline.json --report ket-qua-moi.json --svg so-do-moi.svg
```

Bỏ `--baseline` khi chưa có baseline, không tạo file giả cho đủ tham số. Output mới không ghi đè file đã có. Hash gắn đúng bytes nội dung JSON canonical và revision; thay spec phải chạy lại. Xem `issues`, `coverage`, `metrics`, `diff`, không chỉ exit code.

| Kết quả | Ý nghĩa |
| --- | --- |
| INVALID_INPUT | Đầu vào không đủ/hợp lệ; chưa có phép đo đáng tin cậy |
| ISSUES_FOUND | Có đối tượng lỗi trong phạm vi kiểm; nêu ID/vị trí/cách sửa |
| PROVISIONAL_REVIEW | Có giả định, phần không hỗ trợ hoặc thiếu baseline/threshold; tiếp tục phần độc lập |
| SCOPED_REVIEW_NOT_CERTIFIED | Các phép kiểm được khai báo hoàn tất, không chứng nhận công trình hay CAD |

Graph nối đủ phòng chỉ là quan hệ qua các đoạn mở hợp lệ. **Không suy graph PASS thành đường đi đủ rộng, tiếp cận hay thoát nạn đạt**; engine luôn giữ usable_egress và continuous_door_sweep UNKNOWN. Không hỗ trợ hình xoay/cong/polygon tổng quát, walls/roof/MEP native; giữ coverage và unsupported IDs. Không ép bbox thành hình thật.

Các metrics chỉ tính phần đối tượng được hỗ trợ (`metrics_scope=SUPPORTED_OBJECTS_ONLY`). Nếu toàn bộ phòng chưa đo được thì tổng là null; không diễn giải thành diện tích bằng 0. Nếu chỉ đo được một phần, nêu diện tích phần đã đo và coverage, không gọi là tổng diện tích toàn công trình.

Trả khách: 1–3 lỗi tác động lớn, vị trí/ID và số đo, phương án sửa giữ điều đã khóa, sơ đồ khi hữu ích; phần chưa kiểm nói ngắn. Không đưa JSON/report dài vào luồng phổ thông trừ khi khách cần xuất dữ liệu.

Đối tượng có thuộc tính/geometry ngoài schema (kể cả holes/voids lồng trong room) được đánh unsupported. Không xóa trường đó để lấy kết quả đạt; cần nguồn hình học được hỗ trợ hoặc giữ phần đó chờ kiểm.
