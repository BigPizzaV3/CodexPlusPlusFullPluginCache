# Mô hình, bản vẽ và bàn giao đồng bộ

## Trước khi dựng/sửa

Xác minh đúng host/session/document/revision và quyền qua runtime. Lấy một spec chung có IDs cho phòng/tường/cửa/cột/dầm/sàn/mái/thiết bị; giữ unit, datum/cao độ và quan hệ hosted. Đối chiếu geometry đọc lại với spec, không chỉ tin tham số đã gửi.

| Host | Những điểm phải đọc/kiểm theo capability thực có |
| --- | --- |
| Revit | Document/family/type/instance, unit trong API, phase/design option/level, hosted openings, transaction và save riêng; worksharing/linked model không mặc nhiên được phép sửa |
| AutoCAD | Drawing/units/UCS/layer/block/xref, modelspace–paperspace, block transform; không explode/chuyển toàn bộ layer để dễ thao tác |
| SketchUp | Model units, instance transform và component definition dùng chung; sửa definition có thể tác động nhiều instance, phải preview ảnh hưởng |
| Rhino/Grasshopper | Document units/tolerance, BRep/mesh/curve validity, GH parameters/bake target; preview GH không là object đã bake/lưu |
| Blender | Scene/collection/view layer/units, world transform/evaluated mesh sau modifier, dependency/material/resource; source mesh hoặc bbox chưa là hình cuối |

Đây là checklist, không tự thêm API hoặc tool chưa có. Recipe hoàn thành chỉ chứng minh phần job trả về; native readback/save/export cần evidence riêng.

## Kiểm trước ảnh đẹp

Kiểm shell/cao độ → openings/mối nối → nội thất/vùng dùng → mái/thoát nước → trần/MEP → bản vẽ. Dùng clay/orthographic/section/cutaway chỉ đúng vùng lỗi trước render vật liệu. Mặt cắt kiểm mái chồng, sàn bậc, đầu cột/dầm, cửa–trần. Contact hình học không chứng minh chịu lực/chống thấm.

Khách cần EEVEE thì probe runtime/GPU/context/version thật. Không render Cycles rồi nói EEVEE đã đạt; không đổi engine nguồn proven tại chỗ. Không giảm chi tiết/texture/sample âm thầm. Dùng instance/shared mesh, quản lý bộ nhớ và thứ tự stage trước khi đề nghị giảm chất lượng.

## Bàn giao

Lấy đúng candidate cuối: model, spec, mặt bằng/mặt đứng/mặt cắt, schedules, ảnh/sections, resources/licenses và report cùng revision. Với mỗi artifact giữ path/hash và kết quả mở lại khi runtime hỗ trợ. Mở lại bằng process mới để kiểm font/texture/link/camera/engine; report của revision trước không là kết quả hiện tại.

Không nói đã lưu/export chỉ vì transaction commit hoặc có screenshot. Không tự save các chỉnh sửa thủ công ngoài phạm vi. Hủy job không là undo. Nếu cần file dẫn xuất render/in3D, giữ master và nêu khác biệt; bản in cần scale/độ kín/độ dày/slicer riêng.

Render đẹp không là bản vẽ thi công đúng. Hồ sơ thi công còn khảo sát, quy chuẩn áp dụng, tính toán và người có thẩm quyền chịu trách nhiệm; nói giới hạn theo phần thiếu, không phủ nhận các kết quả đã đo trong scope.
