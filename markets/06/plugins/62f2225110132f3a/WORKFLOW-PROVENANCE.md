# Workflow provenance

อ่านโค้ดเดิมจากงาน Codex วันที่ 4 กันยายน 2026: `transcribe_precise.py`, `transcribe_folder_media.py`, `retranscribe_region.py` และ alignment ที่บันทึกไว้ 15 ไฟล์ บทสนทนาที่อ้างถึงให้แนวทางผลิตภัณฑ์ ส่วนโค้ดที่พบเป็นฐาน implementation จริง ไม่ได้สรุปว่าเป็น workflow ล่าสุดทุกส่วนที่ผู้ขายเคยปรับไว้

## คงไว้

- faster-whisper large-v3-turbo, CPU int8, beam size 5
- VAD, min_silence_duration_ms=200, word_timestamps=True
- condition_on_previous_text=False, temperature=0
- รวมข้อความตาม word string ของ engine, แบ่งที่ gap 0.20 วินาที/42 code points/4.5 วินาที
- ยึดเวลาเสียง ไม่ยืดซับให้เต็ม timeline

## เปลี่ยนอย่างมีเหตุผล

- รับ path เป็น argument แทน path ที่ผูกกับเครื่องผู้ขาย
- จำกัด >0 ถึง 300 วินาทีก่อน ASR และตรวจ video/audio track
- default auto พร้อม `th` เพื่อเทียบ baseline และ `en`; auto ยังไม่ผ่านการเทียบคุณภาพกับ baseline
- decode เสียงโดยรักษา frame timestamps และ offset บน timeline วิดีโอ
- เวลา cue ปัดเข้าด้านในระดับ millisecond แทน round ที่อาจเกิน duration เศษมิลลิวินาที
- ไม่ clamp เวลาผิดแบบเงียบ ๆ; block เพื่อ review
- รวมอักขระไทยที่เป็น combining mark กับชิ้นคำก่อนหน้าโดยใช้ขอบเวลาเดิม ป้องกันสระ/วรรณยุกต์ขึ้นต้น cue ใหม่
- เก็บชิ้นคำ duration ศูนย์ไว้ใน cue ที่มีช่วงเวลาเสียงจริง ไม่ลบข้อความหรือสร้างเวลาปลอม
- ไม่เขียนทับผลเดิมและระบุ draft/review state ชัดเจน

ข้อจำกัด: ค่าตั้งต้น ASR เดิมไม่ใช่หลักประกันคุณภาพเท่ากันทุกคลิป ต้องฟังเทียบและตรวจการแบ่งคำไทยโดยคน ไม่มีโมเดล forced alignment ใหม่หรือ cloud backend เพิ่มมาในรุ่นนี้
