# Capability & distribution — ตรวจ 23 กันยายน 2026

| ประเด็น | ผลตรวจ | ผลต่อ Reel2SRT |
|---|---|---|
| Plugin แบบ skills-only | เอกสารรองรับ | ไม่ต้องมี MCP/server สำหรับแพ็ก workflow |
| Python/ASR/video decoding | Plugin ไม่ได้จัดหา runtime เหล่านี้เอง | ตรวจใน environment ผู้ใช้ทุกครั้ง |
| Manifest | portable `plugin.json` และ legacy `.codex-plugin/plugin.json` รองรับ | แพ็กนี้มีทั้งสองแบบ |
| Local testing | เอกสารรองรับ personal/local marketplace บน surface ที่รองรับ | ยังไม่ได้เพิ่ม marketplace หรือติดตั้งให้บัญชีนี้ |
| Workspace publishing | ต้องมีสิทธิ์ admin และอยู่ในขอบเขต workspace | ห้ามส่งลิงก์ workspace แล้วอ้างว่าลูกค้าภายนอกเข้าได้ |
| Public listing | skills-only ยื่น review ได้ แล้วผู้พัฒนาเลือก publish หลังอนุมัติ | ยังไม่ submit/publish ไม่มี public install URL |
| จ่าย 199 แล้วได้ private install link ทุก plan | หลักฐานที่อ่านไม่ยืนยัน | ต้องทดลองผู้รับจริงก่อนให้คำมั่น |
| จำกัดเฉพาะผู้โอน | ไม่ได้สร้าง auth/entitlement backend | manual delivery คุมการส่งครั้งแรก แต่กันคัดลอกไม่ได้ |
| ค่าใช้จ่าย | prototype รัน ASR ในเครื่อง ไม่มี paid API | ไม่ได้แปลว่าฟรีหรือใช้ได้ไม่จำกัดในทุกบัญชี |

อ้างอิงทางการที่เปิดอ่าน:

- [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) — package skills/resources; capabilities vary by surface.
- [Package your plugin](https://developers.openai.com/plugins/build/plugins) — portable manifest, compatibility fallback, local marketplaces, workspace boundaries.
- [Build skills](https://developers.openai.com/plugins/build/skills) — instructions and supporting scripts; skill without MCP.
- [Submit plugins](https://developers.openai.com/plugins/deploy/submission) — skills-only submission, permission/identity requirements, review then publish.
- [faster-whisper upstream](https://github.com/SYSTRAN/faster-whisper) — word timestamps and VAD configuration.

ข้อสรุป: สร้างและทดสอบแพ็กเกจได้ตอนนี้ ส่วน “โอนแล้วคลิกลิงก์ใช้ใน ChatGPT ทุกบัญชี” ยังเป็นสมมติฐานการแจกจ่ายที่ไม่ได้พิสูจน์ ไม่ใช้ข้อความในบทสนทนาเก่าเป็นหลักฐานความสามารถปัจจุบัน
