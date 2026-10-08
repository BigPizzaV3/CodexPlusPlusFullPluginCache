# ผลทดสอบ Reel2SRT 0.1.0

วันที่ 23 กันยายน 2026 — local macOS, Python 3.12.14, faster-whisper 1.2.1, PyAV 18.1.0, numpy 2.5.2; ใช้โมเดล large-v3-turbo ที่ cache อยู่แล้ว ไม่มีการเรียก paid transcription API

| การตรวจ | ผล |
|---|---|
| Plugin compatibility manifest validator | ผ่าน |
| Skill frontmatter/naming validator | ผ่าน |
| Automated tests | 20 tests ผ่าน ไม่มี skip ใน runtime ที่ใช้ |
| Duration/language matrix | 30/60/180/300 วินาที × ไทย/อังกฤษ/ผสม ผ่านด้วยเวลา word จำลอง |
| Media decoding matrix | MOV จำลอง 30/60/180/300 วินาที: รักษา offset เสียง 1 วินาทีและ trailing silence ผ่าน |
| Negative media | ไม่มี audio และ 301 วินาที ถูกปฏิเสธตามคาด |
| คลิปจริง 1 คลิป | ถอดเสียงใหม่จาก MOV 40.666667 วินาที ได้ 23 cues เป็น draft |
| Replay alignment เดิม 15 ชุด | 13 structural pass; 2 review_required จาก cue/token เกินเกณฑ์ ไม่มีการแก้เวลาปลอมให้ผ่าน |
| ความถูกต้องคำ/ขอบเสียงแบบมนุษย์ | ยังไม่ประเมินครบ ไม่มี CER/WER หรือ timing accuracy ที่รับรอง |
| ไทย/อังกฤษ/ไทยผสมด้วยคลิปจริง 30/60/180/300 | ยังไม่ครบ มีแผน 24 cases ใน benchmark.csv |
| ติดตั้ง/แชร์ข้ามบัญชี ChatGPT | ยังไม่ทดสอบ |
| Import เข้า CapCut | ยังไม่ทดสอบ |

## สิ่งที่พบและแก้

ตัวถอดเสียงภาษาไทยให้ชิ้นคำ/สระที่ duration เป็นศูนย์ได้ การปฏิเสธทุกชิ้นจะทำให้ baseline ใช้ไม่ได้ จึงเก็บตัวอักษรไว้ใน cue ที่มีขอบเสียงจริง และรวม combining marks ก่อนแบ่ง cue เพิ่ม regression tests ป้องกันข้อความหายหรือสระหลุดขึ้นต้น cue ไม่สร้างเวลาใหม่ให้ชิ้นคำเหล่านั้น

เสียงที่ถอดใหม่มี 18 word/subword indices ที่ probability ต่ำกว่า 0.5 (ไม่ใช่จำนวนคำผิดที่วัดแล้ว) ต้องฟังเทียบก่อนใช้เป็นไฟล์ final การผ่านโครงสร้างไม่พิสูจน์ความแม่นของ ASR หรือคุณภาพเท่ากับงานที่ผู้ขายเคยตรวจด้วยตนเอง

ไฟล์ผลลัพธ์คลิปจริงส่งให้ผู้ขายแยกจาก ZIP เพื่อไม่แจกเนื้อหาส่วนตัวให้ลูกค้า รายงาน regression ที่อยู่ใน ZIP มีเฉพาะรหัสเคส/ผล ไม่มี source video หรือ transcript ของผู้ขาย

## ทำซ้ำ

ติดตั้ง requirements ใน environment ที่ใช้ทดสอบ แล้วจาก package root รัน:

```sh
python3 -m unittest discover -s tests -v
python3 skills/reel2srt/scripts/reel2srt.py --video '/path/clip.mov' --out '/path/fresh/clip.srt' --language th
```

ถ้าไม่มี PyAV/numpy จะ skip 3 media tests ต้องไม่รายงานว่า media tests ผ่าน ในการรันครั้งนี้ติดตั้งครบและไม่มี skip

สถานะส่งมอบ: **prototype สำหรับทดลอง Early Access; ยังไม่รับรองพร้อมขายแบบเปิดลิงก์แล้วใช้ได้ทุกบัญชี**
