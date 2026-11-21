# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# English operating guide and bilingual terms
> Historical supporting reference: past reports and proposed techniques are not current verification. Follow the v2.0 workflow and discover current capabilities for every production task. 過去の報告・候補手順を含む資料です。現在の機能と制作結果は毎回確認してください。

Use the same skill for English and Japanese users. Respond in their language. Preserve exact UI labels so users can find the controls. Do not require familiarity with technical stitch names.

## Production workflow

1. Open the requested Jiminy site using the authorized browser tools. Inspect current initialized state and preserve existing projects. Choose “保存して次へ / Save and continue” before importing a new image; verify the backup before discarding existing data.
2. Identify actual capabilities rather than inferring them from desktop, GPT Web or browser-extension branding. Desktop and Web Work may expose browser control; ordinary chat may not. An extension must actually expose the target browser/tab. Discover WebMCP only when the API is advertised, call only listed tools, and verify results. Separate page-side readiness, discovery, successful invocation and actual state changes. “modelContext unavailable” is a failure on that tab, not proof of platform-wide incompatibility. Use permitted UI control when available. Do not require legacy connection codes, extra login or a dedicated plugin.
3. Generate or import an embroidery-friendly design when authorized. Inspect the exact lettering, shapes and holes. Fit the design into the hoop. Default candidate: 110×110 mm. Verify actual exported dimensions separately.
4. Choose colors from the image. Typical multicolor candidate: start with 8 and simplify to 4–5. Honor specified counts. For black lettering, analyze black and white, then exclude background and holes without removing intended white design details.
5. Quantize, clean, label and extract contours. A 10 px small-island threshold is a starting candidate, not a reason to remove meaningful dots or fine strokes. If island count explodes, inspect fragmented input rather than treating island count as color count.
6. Prefer Satin Art Pro for lettering. Never finish a lettering request merely by auto-filling everything with tatami. Separate vertical stems, crossbars, curves, hooks, sweeps and branches. Cut/split difficult islands into natural strokes if the current UI supports it. Y may need three branches; D/G may need stem and curve separation; 風 needs outer strokes, inner strokes and crossings examined separately.
7. Inspect centerlines and splines for abrupt curvature or kinks. Adjust control points, tangents and subdivision as supported. Set start/end and extension direction using actual controls. Do not invent internal APIs. Use “connect a stroke” and crossing-priority tools only if currently present; verify that connections do not cross holes or escape the outline.
8. Treat approximately 0.4 mm satin spacing as a starting candidate. Confirm whether a control means stitch spacing, pitch or path sampling. Do not conflate these. Choose safe satin spans for wide strokes; split or explain a local tatami fallback when needed. Set crossing order so the intended top stroke sews later.
9. Generate in PRO and return to Studio. Verify the returned layer and preview. Disable redundant ordinary tatami under imported satin; distinguish necessary underlay from redundant fill.
10. Use tatami for large surfaces, running stitch for fine lines, Fur PRO for hair direction, and two-color Mix for decorative effects. For Mix, inspect both colors, cross/parallel pattern, spacing, angle and offset. Verify feature availability for L&S, outline satin, underlay and advanced PRO edits.
11. Regenerate after edits. Inspect holes, background, outline, stroke joins, kinks, long stitches, density, crossing order, travel threads and color changes. Automatic sorting must preserve artistic layer order. Preview thread thickness/shadow does not change stitch density.
12. Export actual JEF/PES files; confirm nonempty files and preview. A download-listener timeout alone is not failure: check generated file links and synchronized downloads. Report actual dimensions, colors, techniques and limitations. Never claim satin completion without generation, return and preview verification. Machine test stitching remains distinct from screen validation.

## Bilingual vocabulary

| 日本語 | English |
| --- | --- |
| サテン縫い | Satin stitch |
| 畳縫い | Tatami fill |
| 走り縫い | Running stitch |
| 下縫い | Underlay |
| 輪郭サテン | Outline satin |
| 長短ステッチ / L&S | Long and short stitch / L&S |
| 島・領域 | Island / Region |
| 島をカット・分割 | Cut / Split an island |
| 一画 | Character stroke |
| 中心線 | Centerline |
| 軌道 | Stitch path |
| スプライン | Spline |
| 制御点 | Control point |
| 始点・終点 | Start / End |
| 延長方向 | Extension direction |
| 交差の優先 | Crossing priority |
| 一画をつなぐ | Connect a stroke |
| 毛並みPRO | Fur PRO |
| 2色Mix | Two-color Mix |
| クロス・平行 | Crosshatch / Parallel |
| 密度・間隔 | Density / Spacing |
| ピッチ | Pitch |
| 減色 | Quantization / Color reduction |
| 背景を除外 | Exclude background |
| 渡り糸 | Travel thread / Jump stitch |
| 自動整列 | Automatic sorting |
| 刺繍枠 | Embroidery hoop |
| 保存して次へ | Save and continue |

## Evidence limits

Previous work includes successful basic Studio processing and JEF/PES output, and reported PRO return/Mix operations. Island cutting, start/end, stroke joining, crossing priority and detailed fur edits include requests or implementation reports, not universal visual proof. Confirm current controls and quality for each design. The skill itself does not unlock unavailable browser capabilities or add application features.
