# Video workflow

Current generated-video entry path:

`Bảng Điều Khiển` → `+ Tạo video` → `Kế hoạch chi tiết` → `Bắt đầu tạo video` → B1–B7 → `Nhật ký` / `Tiến trình trực tiếp`.

The plan includes channel, phone, topic, video count, voice/subtitle options, B4/B7 gates, and an explicit creation date. The customer must select a date for each accepted run when the UI requires it.

Support checks:

1. Confirm the customer used `+ Tạo video` from `Bảng Điều Khiển`.
2. Ask which stage B1–B7 stopped at and read `Nhật ký` → `Tiến trình trực tiếp`.
3. Capture the exact error text and affected video/channel.
4. For voice failures, switch to the voice references instead of giving generic render advice.
5. For provider failures, identify the exact provider/model before suggesting a connection check.

Do not tell users to edit project/database rows or force a completed pipeline state.
