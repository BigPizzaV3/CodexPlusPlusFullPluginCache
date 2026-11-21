# MENDAN v2 — reviewer walkthrough（連続録画）

video_status: SCREEN_RECORDING

完成ファイルは [mendan-v2-demo-walkthrough.mp4](mendan-v2-demo-walkthrough.mp4)。H.264・1920×1080・30fps・4:17・音声なし。sha256 `e08268dc26c926f5c779325b764ba8b8b162126e9ad6456c6bc93a642ca12d24`。

2026-11-01 19:08〜19:18 JST に、ChatGPT デスクトップアプリ（チャットモード、プラグイン「MENDAN v2 審査用」、review テナントの合成データ）で台本 8 件を 1 本の連続テイクとして操作し、画面を ffmpeg（gdigrab、デスクトップの領域指定）で録画しました。編集で短縮したのは画面が静止している待ち時間だけで、短縮した箇所には右上に「>> N s of waiting shortened」を表示しています（25 か所、計 350 秒。一覧は ../../recording/edit_plan.json）。並べ替え・別テイクの混在・回答の切り取りはしていません。先頭 6 秒のタイトルカードと末尾 7 秒の結果カード以外の字幕は、左の英語パネル（ケース名・目的・実際に呼ばれたツール）と下の英語 1 行です。

| 開始 | ケース | 撮影中に実際に呼ばれたツール（監査表 mcp_tool_calls_v1） |
|---|---|---|
| 0:06 | intro | attach the MENDAN v2 app to a new chat (no tool call) |
| 0:17 | P1 | describe_schema (1st call TOOL_EXECUTION_FAILED, retried OK), search_candidates, get_candidate |
| 0:55 | P2 | get_candidate, list_missing_info, get_meeting_transcript |
| 1:34 | P3 | no new tool call; quotes taken from the transcript fetched in P2 |
| 1:55 | P4 | search_jobs, get_job, run_matching (NO_NEW_INFORMATION), get_matching_run, get_job |
| 2:32 | P5 | run_matching (NO_NEW_INFORMATION), list_actions, get_matching_run, create_draft (OK, 25.6 s), list_actions |
| 3:21 | N1 | get_candidate -> CANDIDATE_NOT_FOUND |
| 3:39 | N2 | no tool call (no send tool exists) |
| 3:52 | N3 | get_meeting_transcript -> MEETING_NOT_INGESTED |

撮影の経緯: 1 本目（take1）では、P5 の短い台本文に対して ChatGPT が P4 の「求人→求職者」の実行結果を create_draft に渡し NOT_FOUND になりました。審査担当が同じ文で再現しても起こり得るため、P5 の台本文を「求職者→求人のマッチングを実行してから下書き」と明示した文に改め、2 本目（take2）で全 8 件を通しで撮り直しました。完成動画は take2 だけを使っています。take1 の生ファイルは使っていません。

旧 180 秒スライドショーは履歴として残し、current-v2-artifact-manifest.json の historicalEvidence に移しました。
