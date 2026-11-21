---
name: silence-map
description: "Detect actual amplitude-defined quiet runs in bounded audio and export sample-timed review cues without modifying audio."
---

# Silence Map

Require one actual mono/stereo MP3/WAV,0.1–120seconds,20MB,max96kHz. threshold_db-60 to-20(default-35),min_quiet_seconds0.1–2(default0.3). FFmpeg amplitude-threshold quiet runs are not RMS/LUFS,voice activity or speech absence. Unmarked complement is not speech;it includes quiet runs shorter than duration gate. Noise,music and soft speech depend on threshold. No transcription,editing,denoise or audio removal. Decode elapsed sample timeline resets0;integer decoded frame PTS/count establish duration,not original container time or rounded log text. More than200quiet intervals fails instead of truncation. Audit stores nothing. Create exports quiet.csv,unmarked.csv,Audacity tab-separated quiet labels,JSON,time-overview PNG/readme ZIP. Plot green marks accepted quiet,dark unmarked;not waveform/probability. Preserve ZIP/full document when optional plot/JSON saves fail. Source audio is not rehosted/included/modified;derived exports are public. Reopen exact saved PNG/JSON/ZIP without processing again. Report actual timestamp/codec boundaries rather than semantic utterances. Native Linux/runtime and intended-host checks remain separate.
