# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。


# Jiminy Embroidery Guide v2.1

[Open Jiminy Stitch Studio Agent / 制作サイトを開く](https://jiminy-stitch-studio-agent.nihonno.chatgpt.site/)

## Mission / 目的

Turn a simple “embroider this image / この画像を刺繍にして” request into analysis, planning, verified operation, inspection, repair and actual JEF/PES delivery. Skill supplies judgment; WebMCP supplies an operation route; Jiminy supplies production. Do not require the user to know feature names.
Reply in the user's language; keep exact labels, text and file formats. Explain visible outcomes in plain language. Use one bilingual skill, not competing language versions.

## Proposal-led collaboration / AIの提案で仕上がりをすり合わせる

After source generation or inspection, analyze the image and recommend specific treatments with a plain-language reason. Do not lead with a generic “変えたいところはありますか？”. Offer 2–3 relevant alternatives plus “すべてお任せ”; ask a small number of questions at a time and build on the user’s choice. For flowers discuss direction/vein treatment, for lettering readability/stroke weight, for animals fur/solid areas as appropriate. Do not expose irrelevant feature lists or ask every possible question.
At any stage, “すべてお任せします / handle everything” switches to autonomous mode immediately: retain every agreed preference, choose the remaining design and stitch details, and continue through enlarged inspection, repair and delivery without routine design questions. This authorizes reasonable source redesign within the stated motif when useful; preserve exact text and essential identity. Mandatory host approvals and genuinely blocking missing inputs still apply. A later user correction updates the current plan without discarding earlier preferences.
Show meaningful proposals and enlarged inspection results, not only successful command output. Ensure the live operations stay inside the user’s authorized production scope.

## Five roles / 5つの役割

1. **DESIGN ANALYZER**: Read analysis and stitch rules (get_jiminy_guide topic: design-rules). Inspect the source and identify background, meaningful regions, colors, text, fine lines, broad faces, outlines, fur, holes, islands and sharp curvature. Record region identity and intended physical size.
2. **STITCH PLANNER**: Choose the general recipes (get_jiminy_guide topic: general-recipes) and, when creative treatment is requested, creative techniques (get_jiminy_guide topic: creative). Assign method, direction, color, layering and checks per region. Use Satin Art Pro for suitable lettering, rather than accepting automatic fill as final.
3. **JIMINY OPERATOR**: Read environment routing (get_jiminy_guide topic: environment) and WebMCP procedure (get_jiminy_guide topic: webmcp) before operation. Discover actual tools and schemas; operate only available features. Preserve existing work.
4. **QUALITY INSPECTOR**: Read quality and delivery gates (get_jiminy_guide topic: quality). Inspect generated stitches, not only source artwork or a successful button press. Fix defects and repeat affected checks.
5. **RECOVERY ENGINE**: Read recovery rules (get_jiminy_guide topic: recovery) after a failure. Diagnose geometry, input, transfer or connection problems; repair the cause; verify the result. Use cut/split as a geometric repair when appropriate.

These are responsibilities inside one skill, not a requirement to launch five agents.

## Production loop / 制作ループ

1. Inspect supplied artwork. If asked to generate a source, use image-generation capability and verify it. Clarify only consequential unknowns; do not impose embroidery terminology on beginners. Treat 110×110mm as a proposed starting hoop, never proof of machine compatibility.
2. Discover current operation capability and read current project state before mutations. Before replacement, ask once: save and continue / continue without saving / cancel. Respect an existing user decision. Saving generates a JSON backup and retains the old work until chat attachment is confirmed by the host or the user confirms the saved file. Without saving, proceed directly without another confirmation.
3. For flowers/leaves, read vein direction and split artwork (get_jiminy_guide topic: flower-veins). Confirm the desired flow and any source redesign before implementing them; reuse preferences already stated. Analyze and select a general recipe. Preserve exact lettering and essential landmarks. Simplify insignificant details relative to final millimeter size.
4. Prepare colors and regions. Roughly 8 colors then 4–5 is a candidate for simple artwork; preserve requested colors. Exclude background selectively. Treat less than 10px as a cleanup candidate only after confirming what the UI measures; protect dots and small intentional marks.
5. Produce region-specific stitches. Read satin geometry (get_jiminy_guide topic: satin) for letters/curves and feature catalog (get_jiminy_guide topic: features) for detailed settings. Inspect transfer into PRO and return to Studio. Remove redundant main Tatami underneath replacement satin/fur; retain intentional underlay.
6. Inspect preview at whole-design scale and high zoom; use playback for direction, layering and travel. Apply targeted repairs and regenerate. Never declare a defective or uninspected preview complete.
7. Ask once which output formats are wanted, allowing multiple checked choices: editable JSON, JEF, PES, PEC, DST. Reuse formats already requested and let the user change the selection. PES/PEC/DST are experimental. Generate selected formats only. Verify actual nonempty files, dimensions and format independently. Save editable project and completed preview when possible. Explain unavailable outputs and unresolved checks.
8. Report actual methods, size, colors, preview and output files; distinguish screen verification from machine sew-out.

## Additional references / 必要時に読む資料

- English terminology and operating guide (get_jiminy_guide topic: english): English requests and translation of technical terms; this main workflow takes precedence over older summaries.
- Historical cases (get_jiminy_guide topic: recipes): Y/D/G failures, dog, 3BIKI and mountain lettering; use as supporting examples, not fixed recipes for every user.
- Public bilingual description (get_jiminy_guide topic: public-description): copy for the skill/plugin listing and beginner prompt examples.

## Boundaries / 制作範囲

Do not modify Jiminy code, authentication or publication settings as part of embroidery production. Do not require old connection codes or a dedicated server plugin as the default route. Distinguish browser WebMCP from server MCP/API. A site link opens a destination; it does not install tools or guarantee automation.
Do not fabricate tool names, call internal functions, run arbitrary page JavaScript or introduce browser flags to bypass unavailable capabilities. Follow the current host's browser, upload/download and fallback rules.
Support future command execution only when actually advertised and documented. Do not present illustrative Python-like syntax as implemented. Bundled scripts require a supported runtime; the skill itself provides no runtime or UI.

## Manual commands and mixed operation / 手動コマンドと併用
At task start read the packaged skill and retrieve the latest public catalog and relevant guides using a supported Web reader, or the selected browser page WebMCP get_jiminy_guide_catalog/get_jiminy_guide if available. Read transport-policy, command-catalog and environment. Remote MCP is optional and not included in the skills-only plugin. Compare public version with the selected page commandVersion. MCP distributes guides and command specifications only; never send execution requests, Studio IDs or artwork to the server.
開始時にプラグインからガイド一覧・通信方針・最新コマンド仕様・環境ガイドを取得する。サーバーの公開一覧は実行能力の証明ではない。対象画面のコマンド一覧と仕様バージョンを照合する。
When WebMCP listing fails, or the user chooses manual/PC operation, use the bottom コマンド・ステータス panel. Select a listed command or enter {"command":"get_studio_state","args":{}}. Execute only the target page's registered allowlist, never arbitrary JavaScript. State reads run directly; mutations show the target and require the panel confirmation. Existing import/save prompts remain mandatory.
WebMCPが利用できない場合、手動を希望する場合、PCから操作する場合は下端の「コマンド・ステータス」を使う。本体・サテン・毛並みの各画面で一覧が異なる。読み取り、設定、生成、転送、保存を区別する。変更前に図案を保全し、結果とプレビューを確認する。
Use WebMCP, local manual commands and visible clicks case by case. Successful local commands do not prove WebMCP communication. History records 手動 or WebMCP, area, timestamps and result status without arguments or result payloads. Manual calls must not turn the WebMCP lamp green.
両方の経路と通常の画面操作をケースバイケースで併用してよい。画面移動後は対象番号と状態・一覧を取り直す。手動成功をWebMCP成功と報告しない。履歴は各画面で閲覧でき、結果は画面内だけに保持する。
Read results on screen (expand if needed), copy to chat, or save JSON and attach for analysis. Preview images are shown when available. Only claim visibility of a screen actually accessible through the current host. The user's separate right panel is not automatically visible. Do not automatically upload results or save to the MCP server. JSON result exports may include artwork/state/preview; the user decides whether to share. Commands downloading files still need actual file confirmation.
結果は拡大・コピー・JSON保存できる。AIにその画面が見えない場合はコピーを貼るかファイルを添付する。結果JSONは取得内容に応じて図案を含むため、共有はユーザーが選ぶ。命令の履歴と結果JSONは別。最新コマンド一覧を取得するだけではソフト更新や新プラグイン取得は行わない。


## File delivery and replacement / ファイル受け渡しと入れ替え（2.6.0）
- 新しい画像を選ぶ前に、既存データを「保存して進む／保存せず進む／キャンセル」の一度だけ確認する。既に回答済みなら繰り返さない。ドラッグやWebMCP取込では画像の選択後に同じ確認を行う。
- 保存する場合は既存プロジェクトをJSONで生成し、そのfileIdをinspect_import_promptで読む。ダウンロード要求だけで初期化しない。チャット添付の成功、またはユーザーの保存先確認まで元データを保持。保存しない場合はそのまま入れ替え。
- 完成後は必要な形式を複数チェック：編集用JSON / JEF / PES / PEC / DST。指定済み形式を再質問しない。select_delivery_formatsは選択のみ、generate_selected_filesは生成。PES/PEC/DSTは試験的。分割出力とDST色順の補助ファイルも一覧で確認する。
- get_generated_filesでfileId・実ファイル名・形式・容量を取得。describe_generated_fileでMIME・SHA-256・maxChunkBytesを取得し、read_generated_file_chunkをoffset順に呼んでbase64を復元。最大1048576 bytes/回。大きなJSONはホストの正式なファイル処理へ逐次書込みし、全文を会話本文へ貼らない。
- 総容量とSHA-256を照合し、ホストが実際に提供する添付・ファイルリンク機能でチャットへ渡す。ホストが対応しない場合は未完了と理由を報告する。WebMCPを追加するだけで自動添付が保証されるわけではない。blob URLは現在のページだけで有効なのでチャットのダウンロードリンクとして提示しない。
- ホストの添付成功を確認した場合だけacknowledge_chat_file_delivery(fileId,sha256)。全内容の取得を検証し、保存待ちの入れ替えを進める。これはエージェントの報告でありサイトからホストの添付状態を直接検証する機能ではない。端末保存はsavedToDevice:nullのまま。
- 「生成済み」「内容取得・照合済み」「チャット添付済み」「ダウンロード要求済み」「端末保存を確認済み」を区別し、実施した段階だけ報告。ファイル名・形式・bytesは実結果を使う。
- サーバーMCPは従来どおり2つのガイド読取のみ。制作データをサーバーへ送らず、制作中にプラグインの登録・設定を勝手に変更しない。

大きなJSONはdescribe_generated_fileとread_generated_file_chunkにcompression:"gzip"を指定すると転送量を削減できる。transferBytes・transferSha256で圧縮データを照合し、gzip解凍後に元bytes・sha256を照合。ダウンロードする実形式はJSONのままで変更されない。


## Chat output selection and machine filenames / チャットで形式と命名方法を選ぶ（2.7.0）
- Ask in the user's conversation language. Do not require users to press the software's Generate selected files button; it remains for manual use. If the desired formats and naming style were already specified, reuse them. Otherwise ask once, preferably together: formats (editable JSON, JEF, PES, PEC, DST; multiple selections) and naming (date / three digits only / custom). Allow a skip at the start and resolve unspecified output choices at completion. Do not repeat answered questions.
- 日本語では「必要な形式（複数可）と、名前の付け方（日付／数字のみ／自分で指定）を選んでください」。英語では “Which file formats would you like, and how should they be named: date, three digits only, or a custom name?”。ホストに複数チェックUIがなければ番号や自由文で受け付ける。機械名だけで制限を推測せず、分かっている指定を使う。
- inspect_export_options reads selected formats, namingMode, fileName and usedNumbers. set_export_naming accepts mode:date, mode:numbers with optional number:"007", or mode:custom with fileName:"BEAR_01". No extension in custom names; ASCII letters, digits, hyphen and underscore, 1–64 characters. Unknown machine constraints are not guaranteed by this character rule.
- 数字のみは既存ソフトと同じ001〜999の3桁。番号省略なら未使用番号を選び、指定した使用済み番号は拒否する。各形式や分割で番号が進むので、JEFとPESが同じ番号になると約束しない。履歴が一杯なら止めて別の命名方法を選ぶ。番号履歴や既存ファイルを勝手に消さない。使用履歴はこのブラウザの記録であり、USBや機械内のファイルの有無は検証できない。
- Date naming uses the browser's local clock: design_YYYYMMDD_HHMMSS. It is convenient for sorting, but longer names can be unsuitable for older machines. Three-digit naming preserves the existing old-machine option; it does not make every file format or hoop compatible. If the user knows the machine's filename length, supported formats or hoop, follow those constraints. PES/PEC/DST remain experimental.
- Order: select_delivery_formats → set_export_naming → inspect_export_options → generate_selected_files → get_generated_files → describe/read chunks → verify bytes and hashes → host file attachment. Report the actual resulting filenames (including numeric advancement and split/helper outputs), formats and sizes, not proposed names. Generation, browser download request, chat delivery and confirmed device saving remain separate.
- 生データの保存にも選択した命名方式を適用。旧データの入れ替え前バックアップは別の処理で、保存する／保存しない／キャンセルの回答を尊重する。プラグインは変更しない。サーバーMCPはガイド読取のみ、操作は対象ページのWebMCPで実行する。


## 編集保存・新規作成・再開（Jiminy format v1）
編集用の推奨保存形式は.jiminy。標準gzip/DEFLATEでUTF-8 JSONの全制作状態を可逆圧縮する。generate_editable_projectは既定でjiminy、format=jsonで従来JSONを生成。select_delivery_formatsはjiminy/json/jef/pes/pec/dstに対応。ミシン用形式と編集用形式は別。新規作成や画像の入れ替え前には既存の保存・破棄・取消の確認を使う。バックアップ生成を待ち、チャット添付またはユーザーの保存先確認が完了するまで現在の制作状態を保持する。保存要求と端末保存完了は区別する。メニューの「開く」で.jiminyと従来.jsonを読み込める。破損・未対応versionは現データを置換せずエラーになる。
圧縮アルゴリズムをJiminy独自発明と説明しない。仕様と独立した解凍手順: /jiminy-format.md。既に圧縮済みの.jiminyの転送はcompression=noneを推奨。転送gzipを使った場合、転送層だけを解凍し元.jiminyのbytes/SHA-256を照合する。圧縮率は実ファイルの測定値だけを報告する。プロジェクトをMCPサーバーへ送らない。

## Dog photo keepsake / 愛犬の写真と毛並みリズム
1. Ask for the actual dog photo first. Offer two routes: use a supported host image-generation/editing tool to simplify it into embroidery-friendly artwork while preserving identity, coat markings and facial expression; or import the original photo into Studio and adjust background, colors and regions. Do not invent a replacement dog. If image editing is unavailable, explain the limit and use the original-photo route.
2. Prepare size, background removal, palette and fur regions in Studio, then use open_stitch_pro {kind:"fur"}. Fur PRO is 毛並みリズム刺繍 PRO; opening its URL alone does not transfer the prepared image.
3. Inspect gaps at whole-design and face zoom. Owner experience: photo-derived fur may leave small gaps. Preserve intentional sparse texture; repair obvious missing patches or unwanted fabric showing through. Use necessary Studio underlay before the fur layer; a supporting underlay is not necessarily an opaque gap-filling surface. If coverage is needed, consider a light base fill separately. Avoid a full dense duplicate Tatami layer beneath fur. Do not promise zero gaps; verify density and coverage by preview and trial sewing.
4. Generate a first fur pass, then inspect_fur_work.stitchPoints. This is a path-point count, not a guaranteed final machine needle-event count. The existing 自動調整ウィザード requires a generated pass. Set a target, preserve current colors/masks where appropriate, compare plans, and inspect the regenerated result before confirming. Target counts are not guaranteed limits.
5. Use the flow button to display directional arrows and the flow brush modes なじませ / 強制 / 整える to follow the real coat direction, especially cheeks, ears and chest. Use the eraser's color filter and 消す(Mask) to remove background hairs or hair covering eyes/nose/mouth; 修復(Clear) removes the mask. Regenerate and check the result. Erasing is a mask operation, not deletion of the original dog photo. Preserve project recovery before substantial edits.
6. The current browser WebMCP tools inspect_fur_work, set_fur_settings, optimize_fur_stitches and send_fur_to_studio do not draw flow strokes or erase masks and do not run the wizard. Use available supported visual browser controls for those steps, or give precise manual instructions. Remote MCP only retrieves guides. Do not claim an unsupported command exists.
7. Before export, return to Studio and check the combined design count including underlay, fur, face, lettering and outline. Above 20,000 stitches, advise that sewing will take longer and compare wizard settings, density, small-detail removal and palette reduction while retaining the dog's likeness. 20,000 is an advisory threshold, not a machine limit. Report measured final stitches separately from fur path points and planned target.
8. Estimate pure stitch time as final stitch count / stated stitches per minute. For example, 20,000 at an assumed 600 stitches/minute is about 33.3 minutes before color changes, trims, slowdown and stops; at 500 it is 40 minutes. Ask/reuse actual machine speed when known; do not infer it. The Fur wizard displays a provisional estimate from its own path points only, excluding Studio layers and pauses. Never call this actual measured sewing time.

写真の毛並みは少しの隙間が残る場合がある。下縫い→毛並み→必要な顔・文字・輪郭という重なりを確認し、隙間を全て密度で埋めようとしない。毛の方向の矢印、消しゴム、ウィザードを活用し、表情を守る。出力前に全レイヤーの総針数と仮定した速度での参考時間を伝える。

## Provisional sewing time / 予想時間の幅（実測前の仮ルール）
Use the final combined exported stitch count, including underlay, fur, face, lettering and outline. Default to an explicitly assumed 400 stitches/minute, editable for the selected machine; this is not a measured household-machine average. Display a range: lower = (stitches / speed) × 1.3 + color changes × seconds per change / 60; upper = (stitches / speed) × 2 + the same color-change allowance. Default handling time is an editable 30 seconds/change. The 1.3–2 multiplier is provisional owner-selected guidance, not a validated confidence interval or guaranteed upper limit. It already covers slow starts, jump movement, trimming and restart overhead; do not add those separately. The earlier per-event 5-second/half-speed model is not used in this range. Count actual color-change events, not just unique colors. If unknown, disclose excluded/unknown handling rather than inventing it. For 5,000 stitches at 400 spm and 5 changes at 30 seconds each, the unrounded range is 18.75–27.5 minutes; display approximately 19–28 minutes. Fur PRO uses its own path-point proxy and excludes Studio layers, so label it provisional and recalculate using final export stitches before delivery. Estimate is not actual sewing or guaranteed completion time.
予想時間は目安です。本番と同じ生地・芯材・糸・設定で試し縫いを行い、仕上がりと実際の所要時間を確認してください。Use trial-sewing observations to calibrate the allowances; never claim the estimate or a data preview proves sewability.

## 毛並み・丸み・波の判断 / Fur, curved fill and flowing rows (2.12.0)
- ①毛並みは既存の毛並み内で従来 legacy／ふわふわ fluffy を選ぶ。旧データに表現がなければ従来。メインのふわふわは平行または放射の流れに沿う長短の毛を重ねる。PROは画像から抽出した流れに沿う毛の長さを変化させる。両者の生成方式・単位は異なり、同じ見た目になるとは約束しない。従来の数値をPROへ自動換算しない。
- メインの毛並み設定から「毛並みPROのウィザードで調整」。選択領域・表現・既存PRO設定を渡し、PROで生成後に既存ウィザードを開く。PROの密度・長さ・方向ブラシ・色別消しゴムを使い、メインへ戻す。選択領域には保護マスクを適用する。消しゴムで保護範囲を戻すと対象が広がるので確認。戻した毛並みは編集可能な別レイヤーで、元の領域設定は残る。二重縫いを避け、元の上縫いとPROレイヤーの有効状態を確認する。
- ②丸みに沿う塗り curve-fill はクマの頬・腕、花びらなど広い面の流れに使う。メインで開始／中央／終了の3点を上下に調整するか、曲線の点をドラッグ。角度、列間隔、ステッチ長を調整して再生成。画像から立体形状を自動推定する機能ではない。複雑な形は領域を分ける。
- ③波に沿う列 flow-lines は水面・波・髪・雲など連続する流れ。②の基準曲線に波の強さ／回数を加えて列を並べる。穴・領域外は縫わず、急な曲線は短いステッチで確認。列間隔は基準方向での間隔で、曲がりが強い場合は実際の密度を拡大確認する。
- メインの縫い方を切り替えても領域・色は保持。変更した縫い方の設定は領域内に記録し、戻すと復元。両毛並み表現は同じ設定項目を使う。保存・再編集には.jiminy／JSONを使い、旧JSONも読める。
- 毛並みは少量の隙間が出る。必要なら下縫いを先に作る。輪郭から毛を出す機能は今回追加しない。はみ出し防止と穴の保護を優先する。画像の厚み・手刺繍の質感・立体感を保証しない。
- 選択の目安：短時間・少ない針数は畳、面の丸みは②、波の長い流れは③、自然な毛は①。目・鼻・口・小文字はサテン／走りで読みやすさを優先。全体と顔を拡大し、最終総針数・JUMP・糸替え・時間幅を確認。2万針超は時間と密度を再検討。実際の布・糸・芯・ミシン設定で試し縫いする。
- Browser commands: set_region_stitch {id,fillType,furStyle,flowGuide:[start,middle,end],flowBend,flowCycles}. Guide values are -1..1; cycles .25..4. Use live schemas and required workspace/page IDs. PRO set_fur_settings supports furStyle legacy/fluffy. Remote MCP remains guide-only; never send image, project, region IDs or operation commands to it.
- Start with the simplest stitch that serves the design. Curve fill and flowing rows are experimental paths, not proof of successful machine sewing. Confirm preview and final exports.


## 毛並みPROの経路確認・ウィザード（2.13.0）
- 生成時に経路最適化は実行済み。ただし選択マスクや色別消しゴムで切った後はジャンプが増える。Studio送信・JSON保存の直前にも再最適化する。「実行済み」だけで改善を断言しない。
- 詳細設定の隣の「経路確認」タブで毛の流れ優先／ジャンプの移動距離優先を選ぶ。同じ色の縫いの順序と進行方向を調整する。毛の形状・くしで整えた流れの場は再生成しない。距離優先でもジャンプ数が必ず減るわけではない。距離または回数が増える候補は元の順序を保持する。
- JUMP数・移動距離mm・毛並みの縫い点を実行前後で比較する。毛並みの点数はミシン用ファイルの最終総針数ではない。色開始や別パスの移動も含む。最適化で長い縫いを分割すると点数は増える場合がある。
- ジャンプをつなぐ距離は0〜10mm。新規設定は0mm（つながない）、旧データの保存済み値は尊重。0mmなら消した隙間はジャンプで保持する。距離を上げると隙間を横断する通常ステッチが発生し得るため、黙って上げない。穴・目鼻・背景・消した部分を拡大し、不要な横糸があれば0mmに戻す。色開始は必ずジャンプ。
- ウィザードの「目標／プラン／調整・経路」を往復できる。タブ切替だけでは生成・流れの初期化をしない。未計算のプランには進めない。目標数は近似で、確定前と最適化後に実際の点数・ジャンプを再確認。ブラシ・消しゴムで手動調整し、経路確認タブで優先と距離を設定して比較する。元に戻すも使用できる。
- 通常の構成リストには従来の畳縫い・メイン毛並み、ファー構成リストにはPRO生成データ。必要なら粗い畳または疎な従来毛並みを下地として先に縫い、PROを上に重ねる。下地は任意。PRO側に通常の畳設定を移さない。
- WebMCP inspect_fur_work: routeMetrics（points/stitches/jumps/jumpDistanceMm）とoptimizationReport（before/after/goal/keptOriginal/shortJumpThreshold）。set_fur_settings: optimizationGoal:"flow"|"distance", shortJumpThreshold:0..10。optimize_fur_stitchesは非同期開始。完了を確認し、inspectと全体・顔・ジャンプ表示を比較してからsend_fur_to_studio。手動操作は同じUI。
- サーバーMCPは公開ガイドの読み取りのみ。制作データは送らない。試し縫いで確認する。

English: PRO optimizes during generation and before return/save. Masking can introduce new jumps. Use Route review to compare flow vs travel-distance priorities, jump count, travel mm and sewing points. New projects default to 0mm connecting distance; respect existing saved values. Increasing it can sew across erased gaps. Wizard tabs preserve combed flow; target points are approximate. Compare actual results, enlarged details and final machine stitches; trial sewing is required. Remote MCP remains guide-only.


## 増毛・三角毛（試験・2.15.0）
PROでfurStyle="zigzag"を選ぶ。根元中心を固定した等間隔の千鳥格子に配置する。zigzagSpacing=3〜40（PRO処理座標）、zigzagWidth=.05〜1（間隔に対する根元幅）、strokeLength=毛の長さを独立に調整。密度・旧zigzagRows／zigzagOverlapはこの方式では使わない。従来／ふわふわと通常の構成リストは変更しない。
1 毛束を配置で三角の配置ガイドを表示、2 くしで整えるで方向ブラシを使い、3 縫いを生成。根元中心はくしで移動せず、毛先の方向を変更する。細さ・長さが大きすぎれば均等配置でも重なるので確認する。画像の平坦部は同じ色・保護範囲内の方向を補間し、判定閾値だけで中心の根元を除外しない。全域に方向情報がなければ初期方向は仮なので手で整える。
輪郭／穴／選択マスクからの距離を4近傍で計算して外側から内側の帯へ縫う。同じ帯・同色の近い根元を候補にする。Aの出口根元とBの入口根元の中間点Mを作り、A毛先→M→B毛先。開始は最初の入口根元、終了は最後の出口根元。底辺は縫わない。候補の左右を比較し、近い側を入口にする。既存経路との交差、遠い相手、違う色、穴やマスクを横切る接続は除外する。繋がらない部分は別経路としてジャンプする。実際の3D形状を計算する方式ではなく、倒れた三角の毛を2D縫いで表現する。
PRO結果はファー構成リスト、任意の粗い畳／従来毛並みの下地は通常の構成リストに保持。短いジャンプの通常縫いへの接続は0固定。生成→最適化後の針数・JUMP・糸替え・時間幅を確認。送信／保存時は未生成の変更を再生成する。布での試し縫いが必要。
English: Uniform staggered fixed roots, independent spacing, width and length. Comb changes direction, not root positions. After placement, route outer distance bands first. Join tip A to midpoint(A exit root, B entry root) to tip B; leave triangle bases open. Validate colour/masks and crossings; disconnected chains remain jumps. Flat regions inherit nearby directions within the same protected colour region. This is a 2D stitch representation, not physical 3D simulation. Legacy/fluffy and optional normal-list underlay stay separate. Trial sewing is required.

増毛ウィザード（2.15.1）: 目標はPROの点数（縫い＋JUMP）で最終ミシン針数ではない。根元の間隔3〜40を実生成の計測で最大5回調整し、最も近い計測済み設定を提示。通常のプランは細さ・長さを維持、短い毛のプランは長さを0.8倍。5,000／8,000／10,000プリセット、手入力可。目標は近似で到達を保証しない。微調整も根元間隔で最大3回再計測。現設定の色・マスク・くしの方向を保持する。


## 陰影を守る近似色の統合 / Preserve shading while merging colours (2.17.0)
目標は色数の少なさと立体感の両立。元画像・全体・顔・衣服の拡大を見て、ベース、影、ハイライト、重要な輪郭を見分ける。4〜5色を固定目標にしない。減色でしわや目元が消えたら、一度8〜12色程度で陰影を確保し、その結果から近い色を明示的に統合する。
白とほぼ白、同じ役割の中間色は優先してまとめる。黒と濃いグレーでも、ポケット・ひざ・裾のしわを表すなら分ける。肌・服は必要な明暗を少なくとも2段階で残す。色距離、面積、糸番号の一致だけで自動的に潰さない。小領域は目・口・しわ等の役割を確認して除外する。
元の編集データを残して候補を比較し、形を失う一歩手前を採用。例: 青灰色肌、ピンクの服、黒のカーゴでは、12色から白1・黒/濃灰/中灰3・青灰1・ピンク明暗2の7色へ統合できた。これは今回の図案の確認済み例で、すべての図案の最適色数を意味しない。
Studioではinspect_stitch_colorsで現在縫う単色RGBグループと実際の糸番号を確認し、merge_stitch_colorsへfromColorとtoColorCodeを指定する。これは輪郭を再抽出せず色を統合し、縫わない設定・密度・角度を保持する。Mix、サテン、PRO毛並みの追加層は別に点検する。旧画面はapply_stitch_region_editsで100領域以下ずつ設定し、最後に一度生成する。糸メーカー未保存時の既定は画面と同じJanome。画像パレット番号と糸番号を混同しない。
生成後に全体と顔・しわを確認。元画像の減色パレット数、現在縫う色数、出力の色ブロック数、実糸番号の種類数は区別する。JEFの糸番号と明暗差を読み、同じ番号への丸めで影が消えていないか確認する。生成ファイルのSHA-256と容量を検証して保存し、実機試し縫いは別の確認として扱う。
Prefer fewer colours without flattening the design. Recover useful shading first, then explicitly merge colours with the same visual role. Preserve black versus dark grey when they define clothing folds, and preserve readable face highlights/shadows. Inspect effective stitch colours rather than quantization counts; keep background skips and stitch settings. Validate final export thread indices as well as whole-design and close-up previews. The tested 12-to-7 example is design-specific, not a universal optimum.


## ふわふわ表現：部分の広さと奥行きで糸色数を判断する（2.18.0）
「ふわふわにしたい」は見た目の要望であり、furStyle=fluffyと同義ではない。今回のクマで使ったのはFur PROのcontour（輪郭から重ねる毛）。従来、fluffy、zigzag、contourを混同せず実際のモードを報告する。この判断は犬や他の毛のある図案にも適用する。
広く複数の段が見える面は3色、狭い面は2色、細い縁・1～2段しか入らない部分は1色を候補にする。面積だけでなく有効な段数、穴、毛の長さと重なり、実寸、針数をプレビューで判断する。固定のmm閾値や自動3D判定はない。奥まった腕の付け根・足の内側などは共通パレットの濃い1色、明るい小部分は明るい1色も選ぶ。すべての狭い部分を濃くしない。左右対称の同じ役割には同じRGBと糸番号を使う。
contourFurSettingsでgradientEnabled=true、gradientColors=1|2|3を指定する。1色はgradientStartのみを使い、gradientReverseは効果なし。2色はgradientStart/gradientEnd、3色は中間も使う。反転は色の順のみを変える。根元間隔・段の間隔・毛の長さ・くし方向は独立に判断する。同じRGBの別部位を「シャキッと(Fur)」が別番号に割り当てない。異なるRGBを糸番号へ近似することは残るため、プレビューと出力用糸番号の両方を確認する。
粗い下地は通常の構成リスト、表の毛はFur構成リスト。クマ試作は下地の間隔3mm、ピッチ4.5mm、足は毛の長さ8・根元間隔7、お腹は長さ6というPRO処理座標の設定を使った。mmの毛長とは言わない。下地3～5mmと長めのピッチは試作候補で、必要ならクロスを比較し、布で試し縫いして決める。肉球・目鼻口・花・穴を保護する。部位別に返す際は既存結果を重複追加せず、入替と追加の範囲を確認する。生成前の点数を完成結果として送らない。
English: Judge 1/2/3 thread counts by usable row depth, width, holes and shading role. Broad volumes may use three threads; narrow areas two; tiny rims or recesses one shared dark thread. Light small details can use one light thread. Use the same RGB and actual thread assignment for matching left/right parts. This is visual judgement, not automatic 3D inference. A fluffy appearance can use contour fur and does not imply the fluffy generator. Keep coarse normal-list underlay separate; protect face, pads and flowers and trial sew.


## めちゃふわふわ：輪郭の外へ伸ばす毛（2.19.0・試験）
Fur PRO contourのfurBoundary=outside、furOverhang（0～20、処理画像の点）、毛の長さを別々に設定する。外周に濃い輪郭線があると、選んだ毛の色の境界で止まり、密度を上げても外へ広がらないことがある。その場合に限りcontourFurSettings.edgeBridge=1～16（整数、処理画像の点）を試す。初期値0は従来の保護。外周の細い輪郭線を越える幅であり、画像全体の保護を解除する設定ではない。背景は端から連続した背景色の領域のみ。根元は選択した色の内部に置き、細い外縁を通過し、毛先は自分の色または外側の背景に置く。目・口・肉球・花・内部の穴と消しゴムを保護し、入り組んだ細い形では他の模様と重ならないか拡大確認する。輪郭の内外を見た実機試験は未完了。
長さだけ増やすと放射状の硬い毛やジャンプ増加につながる。控えめ／ふわふわ／強めの3案を比較し、段の間隔を毛の長さより小さく、根元の間隔は針数を見て決める。顔・左右の足の同色糸番号は共通にする。広い面は3色、狭い面2色、細い縁や奥は濃い1色、明るい小部分は明るい1色を候補にする。くしは毛先の方向を整え、中心点は額・腕・足に分けて置く。現在のクマを一般的な唯一の設定にしない。
生成後に毛の実際のはみ出し、穴保護、点数、JUMP、ジャンプ距離、色変更を比較する。PROの点数を最終ミシン針数と呼ばない。最終合成時は同じ部位の古い毛を停止または置き換え、下地や他の部位を消さず、二重に追加しない。対照版と各試作を保存する。濃い下縫いは見えすぎないよう粗くし、試し縫いを必ず行う。
English: For contour fur only, compare three outward-overhang prototypes. edgeBridge is an optional 0–16 processing-pixel corridor through a thin outer ink line; 0 preserves prior behaviour. Keep roots inside the selected colour and tips in that colour or edge-connected exterior background. Preserve enclosed holes, erased masks and facial/pad/flower details. Inspect close-ups for near-edge motifs; this is not automatic 3D or proven machine sewing. Compare actual geometry, travel and combined output, replace rather than double-stitch an old part, and trial sew.


## 見た目から案内するウィザード（2.20.0）
ユーザーに機能名を覚えさせない。画像を見て「整った花びら」「柔らかく重なる毛・羽」「流れる翼・尾」のうち適した2〜3案と理由を提案する。任された場合は自分で選び、設定→生成→全体と拡大の比較→修正→保存まで進める。質問は対象範囲・仕上がり・色など必要な項目だけ。
Satin Art Proの花びらサテンと毛並みPROの輪郭・重ね毛は別方式。前者は選択島の輪郭／線と中心点から花びらを作る。後者は色・保護マスク内の輪郭の段をずらし、中心点とくしで重なる毛・羽を作る。通常の「サテン往復」経路とも区別する。輪郭サテンを付けただけで花びらPROを使ったとは言わない。
サテンPRO：島→見た目候補→中心点（ライン式なら線）→間隔・長さ・段→生成→検査→必要なら修正→Studioへ。毛並みPRO：対象→表現→暫定目標→プラン→くし・消しゴム・中心点→再生成→実経路の最適化前後→Studio全体を再生成して検査。目標や初期値は保証ではない。少ない目標に合わせるために隙間を放置しない。
小さなサンプルから試す。1色で形を確かめてから2色／3色、内側／外側、重なりを比較。変更前の編集データを残す。px・正規化座標・mmを混同しない。サテンはサテン構成リスト、毛並みはFur構成リスト、任意の下地は普通の構成リスト。元の畳との二重縫いを点検する。試し縫いで確認する。
English: Recommend visual outcomes before feature names. Offer a few relevant options, or choose autonomously when delegated. Petal Satin PRO, contour overlapping Fur PRO and conventional hair_satin routing are distinct methods. Use target → appearance → candidate plan → visual review → local edits → regenerate → verify combined Studio output. Preserve editable work and distinguish units, layer ownership and provisional points from machine stitches.


## 2つのPROの選び方と同一図案の比較（2.21.0）
機能名を知らない利用者には「整った花びら・葉・飾り」ならSatin Art PRO、「段をずらして重なる毛・羽・柔らかい質感」なら毛並みPROの輪郭重ね毛を提案する。従来のロング毛・ふわふわ・三角毛は別の選択肢として保持する。下縫いは通常の構成リスト、毛並みPROの出力はFur構成リスト。
まずStudioで画像→減色→仕上げ→領域→輪郭を実行し、背景を縫わない設定にしてからopen_stitch_proで渡す。PROのURLを開くだけで画像受渡し済みと判断しない。
同じ図案・寸法・中心点・間隔・段数を固定し、1色→2色→3色の比較を提案する。狭い部分は1〜2色で十分な場合がある。サテンの花びらは中心に集め、毛並みは段をずらして重ねる。生成経路点数と機械の針数を区別し、最後はStudioに戻して構成・縫い順・実糸色を確認する。比較画像は試し縫いの証明ではない。

## 輪郭内になじむつなぎ縫い（2.22.0）
目的はJUMPをゼロにすることではなく、移動の縫いも図案内になじませること。花びらサテンと毛並みPROにtravelMode=off|run|zigzagを追加。初期offで従来の経路を保つ。runは短い走り縫い、zigzagは小さなジグザグの実縫いであり、曲がったJUMPではない。対象内の近い端点へ順序を調整し、元の毛・花びらの向きは反転しない。同じ糸色・元色/島・段の範囲を保護し、輪郭外・穴・消しゴム・選択範囲外を横切る接続は拒否する。短い内側の折れ道も候補にするが、大回りはせず収まらない場合はJUMP。外毛の毛先が輪郭外ならつなぎ縫いの端点にしない。
Satinのset_petal_settings、Furのset_fur_settingsでtravelMode/travelMaxGap/travelWidth/travelPitch/travelBudgetを設定できる。数値は処理画像px。試す初期候補: 最大40px・幅2px・針間隔8px・追加点数上限0.2。解像度/図案寸法で調整し、細い部分はrunまたはoffにする。毛並みは生成で反映、または順序最適化で比較。既存ファイルを読み込むだけでは改善されない。
追加の針目と厚みを増やすため点数予算と同じセルへの集中制限を適用。行き先が近いだけで美観が保証されるわけではない。つなぎが後から覆われる保証もない。JUMP破線とつなぎ縫いを区別し、全体・拡大・再生で顔、穴、余白、重なり順を確認。試し縫い必須。
保存した花の計算比較: /samples/blended-travel/。3色サテンは同じ保存輪郭・設定から再計算してJUMP199→152、47接続、実際の経路点+186。保存した3色毛並み経路はJUMP877→412、465接続、経路点+1161。入口JUMPを含む経路数であり、機械出力の総針数/渡り数ではない。クマの改善結果や試し縫い確認として流用しない。サーバーMCPはガイド取得のみ。

## Vector-aligned large zigzag travel / 針方向に沿う大きなジグザグ移動
travelMode=zigzag は前後の実際の針の往復から向きを推定し、左右の軸を滑らかにつなぐ。移動全体の上限 travelMaxGap は1–300処理画像px、左右の幅 travelWidth は0–60px。travelPitch は1–30pxで移動の刻みと各１針の上限を兼ねる。例180/24/20は花の比較用で、機械の推奨mm値ではない。最終寸法に換算して試し縫いする。
別の島には渡らない。同色でも別島は接続しない。島IDと画像の四方向連結領域、穴、消しゴム、全ての針間の線を保護する。危険な接続はJUMPを残す。大きな移動でも追加点数・重なり上限を維持する。再生成してプレビュー再生で確認する。


## Repeated vector sweeps / 針方向を優先する往復移動
zigzag は各位置で左→右と針方向に沿って往復し、少し前進して繰り返す。１往復で接続完了という制約はない。travelAdvance（0.1–30処理画像px、初期2px）を振り幅travelWidthと１針上限travelPitchから独立して指定する。実効前進量は幅の20%以下にも制限し、戻りの線が斜めに崩れにくくする。前後の針方向は滑らかにつなぐ。多くの往復で点数が増えるためtravelBudget上限は維持する。JUMPが残る理由を点数上限・境界・重なりに分けて説明し、ゼロJUMPを優先しない。Furの数値は倍率換算される。既存ファイルは再生成して確認する。


## Continuous satin movement / 連続サテン移動（試験）
travelMode=satin をSatin set_petal_settings/Fur set_fur_settingsで選ぶ。既存off/run/zigzagは維持。経路は独自のA*による島内の回り込み、針方向と道の長さを考慮した局所順序選択、左右レール往復で構成する。研究のコードやライブラリは取り込んでいない。大域最適や完全被覆の証明はない。
同じ島・糸色・重なり順グループ内で接続。色別指定時は段だけを理由にJUMPで分断しないが、段順指定のorderGroupは維持。閉じた花びら/毛のループは近い線上へ入口を回して向きと全周を保つ。開いた毛は形を欠かさないため始点を維持する。
travelWidth は左右の振り幅、travelAdvance は前進量、travelPitch は１針上限（処理画像px）。穴、消しゴム、輪郭外、別の同色島を横切らない。狭い所は振り幅を縮め、必要なら幅0で通過する。元の輪郭外の毛先が接続端の場合はJUMPが残り得る。
このモードではtravelMaxGap、travelBudgetによる割合打切り、同じセル3回の打切りを使わず、移動も総経路点数totalPointsに含める。無制限計算ではなく、探索/点数上限に達した接続は拒否しunreachableに記録する。JUMPゼロを保証しない。元データを保持し総点数、重なり、全体/拡大/再生、試し縫いを確認。最終JEF/PES針数は書出し後に別途確認。
花の保存済み経路の計算比較：Satin JUMP199→3、総経路点13139。Fur877→25、総43690。実機未確認。比較ページの緑は診断表示で実際の糸色ではない。

2026-10-10 大きな連続サテン移動の比較：travelWidth=168（前回24の7倍）、travelAdvance=28（前回4の7倍）、travelPitch=20（1針上限は別設定）。サテンPRO・毛並みPROとも幅0〜420処理画像pxを指定可能。狭い所は幅を縮めるため実際の幅は場所ごとに異なる。これは1095pxの花での比較値で、全画像共通の推奨値ではない。経路JUMPはSatin199→3、Fur877→26、総経路点数8255/31463。書出し機械針数・実機縫いは未確認。

2026-10-11 針数を抑える比較：幅168・前進28を維持し、travelPitchを20から30処理画像pxへ広げた。移動の折返し位置・線形状・移動距離・JUMP数は同じで、直線上の分割点だけを削減。Satin総経路点8255→5964、Fur31463→23804。最終出力で機械側の最大針長による再分割があれば、この削減率は維持されない。中心の重なり量や糸の厚みそのものを減らす変更ではない。処理画像と刺繍サイズからmm換算し、試し縫いを確認。

2026-10-11 局所方向に合わせた移動：元の針線から近傍8サンプルの軸を計算し途中の方向を優先。左右端の方向が揃い、全幅を保護領域内で振れるときのみサテン往復。短い/縦方向/幅不足はライン。端点の軸の交点へ島内で回り込める場合は折れ点を追加し、穴はA*で複数区間に分ける。局所方向との一致が0.6未満の長いラインは接続を拒否しJUMPを残す。厳密な全交差禁止の証明ではない。開いた毛束は近い終点から反転して全線を保持。別島・穴を横断しない。比較はSatin1692経路点/JUMP38、輪郭毛2101経路点/JUMP38。機械針数ではない。輪郭毛の根元間隔12/段間隔10/18段は処理365pxの花の比較値で全画像推奨ではない。少し疎らにボタンは現在値から根元間隔1.2倍/段間隔1.25倍/段数0.9倍。再生成・全体拡大確認・試し縫いが必要。

2.23.0 一筆サテン（試験）：メイン畳縫いのfur-engine.js内generateRadialSatinClippingを確認し、円弧に沿って内外交互に針を置く考え方を花びら輪郭に応用。set_petal_settingsのoneStroke=true、または花びらパネルの一筆サテンを選ぶ。輪郭・内側専用。生成時に隣の針へ進む連続ジグザグを作り、従来の後付けサテン移動は行わない。同色の隣段へ短く安全に渡れる場合のみ結合。別島・穴・接続不能は経路分割。全体一本や交差ゼロを保証しない。既存の三角方式はoneStroke=falseで保持。糸色は段ごとの振分けで、三角単位ミックスとは異なり色の帯が出やすい。花の比較設定spacing16,length73,rows9,rowGap38（1095px）で786経路点・5経路。機械針数ではなく、実画面と書出し・試し縫いは未確認。


## 中心の隙間を補う短い毛・弱いつむじ（2.23.6・試験）
Fur PROのcontourのみ。中心点を単なる収束点でなく短い毛の補完範囲として扱う。通常画面の輪郭毛設定で「中心の隙間を短い毛で埋める」をONにし、中心を埋める半径4〜80、中心の毛の長さ1〜40（いずれも処理画像px）、回す強さ−1〜1を設定する。0は渦なし、負は逆方向。選択した中心ごとに全体値／短い重なり(overlap)／つむじ(whorl)を選べる。旧プロジェクトはcenterFillEnabled=falseで従来形を保持。中心が保護マスクや別色上なら追加しない。千鳥の根元から短い三角毛を出し、外側へ既存毛長に馴染ませ、中心範囲の重複を最寄り中心の担当に分ける。明示的なくしの方向も優先し、目鼻口・穴・消しゴムを保護する。これは2D表現で物理的な毛や実機の縫い上がりではない。
ブラウザWebMCP/手動コマンド set_fur_settings の contourFurSettings に centerFillEnabled/centerFillRadius/centerFillLength/centerFillTwist、furCenters の各点に centerStyle=inherit|overlap|whorl を指定できる。設定後は再生成。補完毛もFur構成リストに保持し、下縫いは通常構成リストへ別途。保存・再編集で設定を保持する。
移動欄「毛の線をたどる移動」(followHairTravel=true)をONにすると、輪郭毛の広いサテン移動より優先し、元の毛の座標・順序を保持したまま既存線と短い10px接続を候補にする。針間隔20px、同じ島・元色・糸色とマスクを保護。大回りは拒否、自然につながらない場合はJUMPを保持。初期OFFで旧設定を変えない。設定は処理画像に対して座標倍率で換算する。JUMPをゼロにする目的ではない。
クマ顔の計算比較 /samples/bear-face/#K : H(中心補完なし)5333縫い点/432JUMP、K(額つむじ・頬耳overlap、半径28/毛10/回転0.2)6333/403、L(半径38/毛12)7268/383。5つの中心点と表の輪郭毛・2色は共通、下縫いなし。生成経路の非JUMP点であり機械形式での最終針数ではない。小さいKから比較し、中心が濃くなりすぎたら半径・長さ・回転を減らす。ブラウザ実操作・実機試し縫いは未確認。公開ガイドとソース内のスナップショットを更新し、インストール済み個人プラグイン本体の更新は別途確認する。サーバーMCPはガイド読取専用。


## 輪郭毛の毛先ゆらぎ・実糸比較（2.23.7・試験）
Fur PRO contourFurSettings.naturalVariation=0〜1。旧データと初期値は0で従来の計算を保持。根元の等間隔配置は保ち、輪郭接線を前後2点の方向と補間して細かな段差をなめらかにする。毛長を最大18%×設定値、向きを最大約4.6度×設定値で決定的に変化させる。毎回ランダムに変わる処理ではない。明示的なくしの強さ1の方向は変えない。長さは境界で切られるため輪郭や段の規則性は残る。目鼻口・穴・マスクを保護する。方向と長さの変更後に必ず再生成し、全体と頬・耳の拡大で比較。
クマM/N案はゆらぎ0.65、中心に合わせる強さ0.8、段間隔10、根元18、長さ34、中心増毛38/12/0.2。左右の頬・耳の中心位置を鏡像にした比較であり、自動左右対称検出ではない。Mはジャノメ214ブラウン1色、Nは205ダークブラウン→214ブラウン→213ベージュ3色。ソフト内のJANOME_THREADS表のRGBを使用し、公式JANOME糸色表 https://www7.janome.co.jp/global/wp-content/uploads/accessoriescatalog.pdf で番号と色名を確認。RGBは実物の色を保証しない。Fur画面の糸候補ボタンで同じRGBを選べるが、実機ファイルの糸番号設定完了を意味しない。Studioで実糸メーカー・番号・左右の共通割当と書き出し番号を確認する。別メーカーはそのメーカーの表で改めて選ぶ。
毛束を1回ずつ指定した1/3色へ分配し、架空の中間色糸は増やさない。色ごとにまとめる縫い順で糸替えを抑えるが重なり順は変わる。試し縫いをする。計算比較 /samples/bear-face/#M と #N はライブ画面制作やJEF/PES出力・試し縫いを行った証明ではない。目鼻口は参考塗り表示。毛先の調整を追加したため点数・JUMPは再計測し、最終ミシン針数と区別する。


## クマ顔の合成確認（2.23.8）
採用したM/Nの輪郭毛に、通常リスト相当の粗い畳下縫い（間隔3mm・ピッチ4.5mm・45度）と顔パーツの畳（間隔0.3mm・ピッチ2.5mm・45度）を別層で合成した計算試作を /samples/bear-face-composite/ に保存。毛を作り直さず既存M/Nの経路を使う。順序は下縫い→毛→口周り・耳のベージュ213→目鼻口の濃茶205→白い目の光001。毛の色数と総実糸色数を区別し、両案とも総実糸は4種類。単色案でも顔のため糸替えがある。
顔パーツはStudio畳エンジンで生成。試作スクリプトでは丸めにより輪郭外となった端点を含む線を丸ごと捨てず、0.5px以下で有効区間を調べ、輪郭・穴内に保護された区間の始点終点を残す。これは比較試作のクリップ処理で、Studio本体エンジンの更新ではない。Satin PROを使ったとは報告しない。白・濃茶・ベージュを参考塗りでなく実縫いで表示する。画像線幅は毛1px、顔2.5pxの模式表示で実糸幅の証明ではない。
試作JEFを実際に生成し、ヘッダーの内部糸IDをJANOME_THREADSのcatalogへ逆照合、縫い命令と終端・糸替え数を読み直す。内部ID11/14/19/2は商品番号214/205/213/001と区別。試作は顔の735×470px切り出し、10px/mmで73.5×47mmの仮寸法・110mm枠指定。下端は切り出し境界で、クマ全体の完成データではない。ブラウザStudioでの合成・端末保存・試し縫いは未確認。完成全体へ組み込む前に元プロジェクト、寸法、枠、二重縫い、糸順を確認する。実機試し縫いが必要。顔の試作JEFを全身の完成ファイルとして渡さない。


## v239 縫い順の向き＋島内ジャンプ補修（試験）
毛並みリズムPROのset_fur_settings、花びらサテンPROのset_petal_settingsでoptimizeRouteDirection:true（初期ON）。既存の連続STITCHを経路として扱い、経路の境目をJUMPと誤認しない。動的計画法で前後の同一ドメイン移動距離を合わせ、短くなる場合だけ経路を逆順にする。経路順・糸色・段・針目の形は保つ。複数段をまたぐ連続経路とdirectionLockedは逆順にしない。色替え時の移動はこの距離集計の対象外。必ずしも最長JUMPが短くなる保証はない。
サテンPROのoneStroke:true、repairLongJump:trueでは最長一箇所だけでなく、同じ糸色・島内の複数JUMPを既存針目のグラフで回り込み、周囲の針方向になじませる。最大200箇所・追加2万点。毛並みPROの輪郭毛でfollowHairTravel:trueとrepairLongJump:trueなら、毛の線をたどる処理のあと同じ補修を適用（最大200箇所・追加2千点）。同RGBでも別の連結島は縫って横断せず、穴・マスク・選択外を避ける。経路がない／上限に達した所はJUMPを残す。内側のつなぎSTITCHと島間の機械JUMPを区別する。画像pxからmmへの縮尺と最終出力の針数を確認。
設定を変えたら再生成。ON/OFFで本体針目・糸色・段順、JUMP、移動距離、追加点数を比較。比較ページ /samples/route-optimization/ は保存された顔の毛データから計算した追加補修で、Studioの画面操作／実機の試し縫い／新JEF書出しは未実施。既存の顔合成JEFは前版のまま。新しい共通処理を畳や走り縫い全般に適用したとは言わない。布の試し縫いが必要。


## v240 複数色の島内JUMP経路／サテンの斜めつなぎ抑止
この項目はv239の複数色・サテンの補修方式を更新する。毛並みPRO set_fur_settings.islandTravelMode は auto / stitch / jump。初期autoは生成結果が1糸色なら従来の島内つなぎ縫い、複数糸色なら輪郭・穴・凹みを避ける針上げの島内JUMP。stitchは旧つなぎ縫い、jumpは1色でも島内JUMP。本体経路の逆順判断は継続する。各糸色の縫い順を保ち、A*の島内経路を移動間隔travelPitchごとの複数JUMPに分ける。追加点はisJump:true,islandJumpWaypoint:true。STITCHを追加せず、JUMP点数が増えても縫う針数の増加とは区別する。連結島・sourceColor・選択マスクを保護。別の島は通常のJUMPで、針上げを禁止すると機械的に移動できない。
サテンPROのrepairLongJump:trueは花びら／一筆サテンのJUMPを同じ島内で回り込ませる。斜めのつなぎSTITCHを追加せず、段の移動も複数JUMPにする。針目の形・色・段順を保つ。追加移動点最大2万、計算で通路が見つからない／上限に達した場合は報告のunreachable,budgetLimitedを見て再調整し、穴横断を解消したと断言しない。島内経路の各直線区間を厳密な輪郭交差／ラスタ境界で検査する。
JUMPは糸切りではない。糸切りなしでは渡り糸が布上に残ることがある。上の糸色で隠れるかはプレビューだけでは保証できず、最終色にも同じ注意。試し縫いで確認する。比較 /samples/route-optimization/ は保存済み毛データを用いた計算試作、画面操作と新JEF出力・実機未実施。一色の計算結果が前版と同一であること、3色の既存STITCH点数が不変で全JUMP区間が島内であること、穴・U字凹み・同RGB別島を検査。


## v241 JEFの連続JUMPと顔試作
JEF出力で複数JUMPの途中へゼロ移動STITCHを入れず、連続JUMPの最後だけ従来の補助STITCHを入れる。島内回り込みの途中では針を落とさない。既存の単独JUMPの補助STITCHは保つ。/samples/bear-face-ready/ に更新経路を下縫い・実縫いの目鼻口と合成したJEF試作を置いた。顔切り出し73.5×47mm、110mm枠の仮指定。一色の毛／三色の毛でも顔パーツ込みの実糸は4種類。端末保存、ライブStudio操作、実機の縫製は未確認。全身の完成品とは言わない。


## 採用例と運用判断（2.24.2）
採用済みの顔試作は /samples/bear-face-ready/ 。クマ全身の完成や実機確認を意味しない。
|項目|採用値・判断|
|---|---|
|顔の寸法|73.5×47mm、110mm枠指定の計算試作|
|粗い畳下地|間隔3mm、ピッチ4.5mm、45度。一般には間隔3〜5mmから布と隙間で判断。毛と別層|
|輪郭毛|根元間隔18、段間隔10、段数24、毛長34、幅0.5、千鳥0.5。PRO処理座標でありmmではない|
|方向・自然さ|中心強さ0.8、ゆらぎ0.65。中心増毛半径38、長さ12、回転0.2。額・両頬・両耳の5中心を配置、左右は鏡像|
|移動|optimizeRouteDirection:true、repairLongJump:true、followHairTravel:true、islandTravelMode:auto。短いJUMPの通常接続閾値0|
|M|毛214ブラウン1色。合成JEF 8,574 STITCH、314 JUMP/ゼロ移動、糸替え3回、18,566bytes|
|N|毛205→214→213の3色。合成JEF 8,648 STITCH、1,915 JUMP/ゼロ移動、糸替え5回、25,142bytes|
両案とも顔パーツを含め実糸4種類。JEFのSTITCH数には最後のJUMP後の互換パディングを含む。JUMP点数は針数ではない。連続JUMPの途中に針落ちを挿入しない。
1色の輪郭毛は従来のなじむつなぎ縫い、複数色は島内の針上げ経路を基本にする。花びら／一筆サテンはrepairLongJumpで島内を回り込む。別島を縫って橋渡ししない。unreachable・budgetLimitedが非ゼロなら未解決を報告し、マスクと寸法を確認する。JUMPは糸切りではなく渡り糸が残り得る。
数値を別画像へ丸写ししない。処理画像寸法と完成mmを合わせ、狭い部位は1〜2色へ減らし、左右の糸割当を揃える。くし・中心点を保持して変更後再生成、下地と毛の二重縫い、目鼻口、穴、凹部、最終針数を確認する。試し縫いで密度・引きつれ・渡り糸を確認する。
取得順：catalog→transport-policy→workflow→studio-operation→recipes→quality→command-catalog。サーバーMCPはガイド読取だけ。実操作は選択ページのWebMCPで現在のスキーマを確認し、利用できないコマンドを発明しない。設定変更、生成、保存要求、端末保存確認を区別する。


## 輪郭毛の柔らかさ・細幅・境界検査（2.25.0）
輪郭毛だけの比較ではfurStyle=contourを使う。検証完了前にふわふわ・三角毛を削除せず、旧図案の互換性を保つ。
contourFurSettings.whorlSoftness=0〜1（0で従来）、adaptiveWidth=trueで細い部分の根元幅を縮める。外向きの毛先が収まらない場合は同じ色・保護範囲内の逆方向のみ試す。柔らかさは中心への方向集中と中心増毛の放射を緩める。くしは優先。centerBlend、naturalVariation、短い毛を合わせて全体・顔・足を拡大比較する。
Basicの保護マスクは元画像の対応範囲に保護画素が1点でもあればそのセルを保護する。輪郭毛の消しゴム変更後は線分全体を検査して分割する。最終はDetailでも確認。意図的外毛と保護穴の逸脱を区別する。
移動は既存の方向最適化・島内経路を使う。1色の縫う移動と複数色の島内JUMPを区別し、STITCH/JUMP/移動距離、unreachable/budgetLimitedを確認。ジャンプ数と未糸切りの糸露出は別。島・穴を横切らず離れた島のJUMPを0と約束しない。
AI操作は画面移動後にツール一覧とget_workspace_statusを取り直す。同名登録時・画面終了時は旧登録を解除（対応APIがある場合）。ホストの古いハンドルが直った証拠にはしない。読取→設定→生成→状態・全体/拡大→Studio取込→重複検査→出力。失敗した変更を無条件で再試行しない。
合成細幅テストで従来0点→39点、線分の収容と1画素保護穴の保存を確認。クマの美観や実縫製改善の証拠ではない。

輪郭毛でfollowHairTravelを使い先頭JUMPを縫う移動へ修正した連続経路は、同じ色・sourceColor・幅・島で線分が収容される場合に一本に結合して返す。独立レイヤーの先頭がStudioで再びJUMPになるのを防ぐ。縫う順序と元の点列は維持し、最終routeMetricsとafterJumpsを一致させる。

2.25.1: 新規の選択は毛並み／輪郭毛／サテン／デッサン。旧ふわふわ・三角毛・ミックスは新規候補から外すが、旧プロジェクトの復元・再生成は保持。クマのDetail・1色輪郭毛の実生成では12,149点、STITCH12,148、JUMP1（開始位置への移動）。接続前の312JUMPから減少。元1095画素マスクで縫う12,148線分の保護範囲逸脱0を確認。混合3色とは解像度・設定が違うため同条件比較と呼ばない。実縫製は未検証。


## 輪郭毛の中央の継ぎ目・内毛/外毛（2.26.0）
毛と毛の一般的な隙間と、輪郭から内側へ重ねた段が出会う中央/斜めの継ぎ目を区別する。contourFurSettings.seamFillEnabledは2.26.0では初期OFF。2.26.1から新規は初期ON、保存済みのOFFは維持。OFFではv204の毛の生成と同一。ONでは同じ色・選択・消しゴムの保護範囲の内側だけに短い毛を追加し、既存の根元/毛先/くし/段数/糸色を変更しない。中心点から放射するcenterFillとは別。
seamFillWidth=1〜20（既定6）、seamFillLength=1〜40（既定8）、seamFillSpacing=2〜20（既定4）。単位はPRO処理座標。「中央の白線を補う（標準）」は幅10・長さ8・間隔4を設定してONにする。方向は近傍毛の軸を平均し、明示的なくしを優先。線分全体が同じ色・保護範囲内か検査し、追加毛の重複を抑える。穴・顔・肉球などの別領域は補わない。白線が必ず消える、布が必ず隠れるとは約束せず、密度/重なり/点数/JUMPを全体と拡大で比較する。
「輪郭内版」はfurBoundary=inside、furOverhang=0、edgeBridge=0。「少し外毛版」はfurBoundary=outside、furOverhang=3、edgeBridge=0。境界以外の設定と中心/くし/グラデーションは保持する。外毛は背景につながる外側だけへ許可し、内側の穴を外背景として扱わない。外周の別色の線が毛先を止める場合、edgeBridgeの幅を別に調整して、顔・穴への影響を再確認する。自動でその線を越えない。
四角の合成形状で基準510点、標準補い付き内毛594点、外毛612点を比較。これは低密度のアルゴリズム検査でありクマの最終針数ではない。OFFの完全一致、明示的なくし、再現性、外毛の上限、保護穴、3色の保持をテスト。実際のStudio→PRO受け渡しでクマも確認し、旧レイヤーを追加重複させず比較用コピーに置換する。試し縫いは別途必要。
MCPサーバーは公開ガイドの取得専用。seamFill設定を含む制作操作はページのWebMCPまたは画面操作で行い、図案・画面IDをMCPサーバーへ送らない。

2.26.1 中央のランダム補毛：新規・空の設定ではseamFillEnabled=true、seamFillJitter=.35。保存済みのseamFillEnabled=falseと、v204以前の既存輪郭設定（フラグ未保存）はOFFを維持。seamFillJitter=0〜1、0で規則的。標準ボタンは幅10・長さ8・間隔4・ランダム.35。中央の短い毛だけに、根元位置・長さ・向きの小さな固定乱数のゆらぎを加える。再生成で同じ形を再現する。強さ1のくしの方向にはランダムな回転を加えない。既存輪郭毛は変えない。保護境界内の近い補毛だけを連続経路へまとめ、穴や別色を横切る接続を作らない。補毛ON時の毛をたどる探索は、従来の迂回上限を満たせない高コスト領域だけ早めに打ち切る。受理される経路の形は保持する。生成量・JUMP・重なりは再確認。
