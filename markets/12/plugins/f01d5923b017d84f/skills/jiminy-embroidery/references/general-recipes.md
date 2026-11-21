# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# General production recipes / 誰でも使える図案別の作り方

Choose by user goal and actual geometry. Every recipe ends with quality inspection, targeted repair and actual output verification. Never require users to pick a recipe or name a PRO tool.

| Request | Plan | Main inspection/repair |
| --- | --- | --- |
| Names, letters, short messages | Verify exact text; simplify at actual size; use suitable Satin Art Pro paths per stroke; preserve spacing/counters | Split difficult branches/curves; inspect joins, holes and readability |
| Logos and symbols | Preserve silhouette, brand colors and negative space; broad fill, narrow satin, fine running | Compare to source; do not creatively change identity without a request |
| Pets and animals | Preserve eyes, nose and expression; reduce noisy texture; select solid fill or directional fur by region | Protect meaningful small marks; inspect face, fur flow and duplicate fill |
| People and characters | Separate face, hair, garments and accessories; simplify tiny details | Preserve likeness, expression and exact garment text |
| Flowers and plants | Orient petals/leaves individually; satin stems or running veins; optional Fur for grasses | Inspect center congestion, joins and directional flow |
| Landscapes and buildings | Separate major planes; orient fills by slopes/architecture; simplify small distant details | Preserve snow/negative space; inspect borders and perspective cues |
| Line drawings and handwriting | Measure line weight at final size; choose running or narrow satin; preserve expressive contours | Repair broken lines, tight loops and unintended doubling |
| Patches | Fit motif and intended border; plan internal layers then border | Inspect edge coverage, bounds and internal-to-border registration; do not assume digitized border finishes cut fabric |

## Shared preparation
Exclude background selectively; organize useful colors rather than targeting one number for every design. Scale deliberately before cleanup. For small designs enlarge essential letters/holes or simplify with user intent preserved; do not silently delete meaningful content.
For multicolor designs verify actual thread order and format color mapping. Use supported Mix only when desired; rainbow is not synonymous with two-color blending.
If a technique is unavailable, choose a justified alternative and explain visible impact. Do not call an alternative Satin Art Pro or Fur when it was not actually generated.


## 動物の刺繍品質確認
クマなど動物は全体の毛並みと、目・鼻・口の輪郭を別々に拡大して確認する。毛並み、ロングショート、タタミを比較し、毛の向きと密度が整う方法を選ぶ。目・鼻・口を毛で覆わず、表情を保つ。毛が落書き状、飛び線だらけ、隙間だらけに見える場合は、密度や方向を調整し、必要なら制御されたロングショートまたはタタミに変更する。生成成功だけで品質良好と判断しない。全体と顔の拡大プレビューを確認してから出力する。
