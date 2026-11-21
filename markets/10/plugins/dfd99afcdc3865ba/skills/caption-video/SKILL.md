---
name: caption-video
description: 動画をカットし、音声から時間付き字幕を作成・修正してMP4で保存する。動画の仕上げ・字幕編集に使う。
---

Open open_video_editor. The user imports the actual video or adds an existing generated output through its widget. Never invent local clip IDs, durations or captions for unheard speech.

1. Read unsketchEditProject from widget context. Apply requested trims and reorder with edit_video_project using exact IDs and validated source times. Captions use source-relative seconds, so trimming does not shift their meaning.
2. For speech transcription, direct the user to the explicit 音声を送って自動字幕 button. It sends only the selected audio range to transcription, at most 60 seconds per clip and six new clips per account per day. Existing jobs are recovered, never resubmitted. This allowance does not spend generation credits. Do not call the app-only transcription tools yourself or claim recognition from silent frames.
3. Alternatively, the user imports SRT/VTT or supplies a timed transcript. Use clip.captions=[{start,end,text}] for timed cues and clip.caption only for a fixed overlay. Keep all cues within source duration. Preserve the user's wording unless correction or translation was requested.
4. Let the user review transcript text and timing; correct recognized names without inventing speech. Apply edits through edit_video_project. The widget offers MP4 by default and WebM when selected; export depends on browser codec support.
5. Preview and save after export. Do not call subtitles complete merely because text was inserted. If source audio is absent or unsupported, report the limitation and use the supplied transcript/SRT/VTT without guessing.

No new media generation is required for cuts or captions. Do not offer purchases or publish media.
