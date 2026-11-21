# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# Creative stitch design / 縫い方をデザイン道具にする

Use creative treatment when requested or offer a concise optional direction. Preserve logos, exact text and required colors. Do not silently redesign faithful-conversion requests.

| Tool | Creative use | Verify |
| --- | --- | --- |
| Fur PRO | Grass, feathers, flames, waves, light trails, flowing abstract marks | supported direction controls, silhouette, crowded roots and boundary leakage |
| Satin | Shiny ribbons, raised-looking graphic strokes, ornamental outlines, abstract bands | actual stitch width, smooth curves and corner congestion |
| Tatami | Directional shading, contrasting facets, rhythmic area patterns | per-region angles and excessive layered density |
| 2-color Mix | Crossed textures, parallel color rhythm, optical blending | supported combinations, actual thread colors, spacing and readability |
| Running | Sketch-like lines, contour accents, geometric rhythm | continuity and visibility at final size |

Prefer one or two deliberate treatments rather than stacking all effects. Plan a small representative area first; inspect before applying broadly. A rendered gloss/relief is not proof of physical stitch relief. Spacing-based optical blending is a candidate, not a guaranteed smooth gradient.
For combined satin/Mix treatments verify the current app supports the combination. Do not duplicate two complete fills just to simulate it. Record creative choices per region so a repair does not overwrite the entire design.
