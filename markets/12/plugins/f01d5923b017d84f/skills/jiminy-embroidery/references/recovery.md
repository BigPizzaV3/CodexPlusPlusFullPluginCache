# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# Recovery engine / 失敗と修正

Preserve current work and identify the failing stage. Connection errors, missing selections and invalid parameters are not repaired by cutting geometry. Use geometric repair only after confirming valid input and transfer.

| Symptom | Inspect | Targeted repair |
| --- | --- | --- |
| Automatic path/generation error | selected region, holes, branch graph, valid parameters, tool error | if shape complexity is causal, cut into natural strokes and regenerate individually |
| Spline kink/腰折れ | anchor spacing, tangents, curvature, branch junction and both satin boundaries | remove unnecessary points through supported controls; adjust tangent/end extension; split abrupt curve |
| Y or branch | three arms and junction density | compare three branches or trunk-plus-branch; check central gaps/overlap |
| D/G bend | stem-to-curve transition and inner boundary | separate straight stem and arc where appropriate; smooth the curve |
| Hole closed | original hole, boundary, long cross-hole span and density | correct shape/path, split, widen necessary negative space consistent with source; adjust supported spacing |
| Tatami under satin/fur | region object list and intentional underlay | disable only redundant main fill; regenerate and inspect coverage |
| Thousands of islands | source texture, color fragmentation and cleanup units | simplify/reduce colors; remove insignificant small islands while protecting eyes/dots |
| Dense crossing | duplicate fills and stroke order | reduce unnecessary overlap and restore intended crossing order |
| Broken contour | source/stitched overlay, split endpoints | adjust joins/registration and inspect whole silhouette |
| Excessive travel/JUMP | playback, region sequence and required layering | reorder compatible regions; preserve crossings and outlines; recheck |
| Wrong PRO input | selected region and transfer state | fix transfer; do not invent substitute geometry |
| Clipped controls or closing popup | current visible UI | use documented scroll/fit/resize; reopen and verify selection |
| Settings erased local edits | global versus selected application | Undo or restore saved project; apply to intended scope |
| Export timeout | output links and documented download location | verify file before re-export; report missing format separately |

## Cut/split procedure
1. Compare source, region boundary and automatic path. Identify a branch, crossing, abrupt turn or stem/curve transition.
2. Confirm cut/split exists in current tool/UI. Save/establish an undo point if supported.
3. Cut into units that can be sewn with a coherent path. Avoid cutting across holes or losing source silhouette.
4. Select each new region; refresh IDs; acquire centerline, generate spline and assign Start/End through available controls.
5. Inspect both sides of satin and needle landings; adjust joins and layer order. Return to Studio and remove redundant main fill.
6. Regenerate, inspect the junction at zoom and whole-design scale, and replay travel.

Do not assume cutting fixes every automatic error. After two materially different unsuccessful geometry repairs, preserve progress, explain the remaining defect and choose a supported alternative only if acceptable to the design. Do not loop identical retries or label partial production complete.
