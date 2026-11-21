# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# 機能一覧と制作判断
> Historical supporting reference: past reports and proposed techniques are not current verification. Follow the v2.0 workflow and discover current capabilities for every production task. 過去の報告・候補手順を含む資料です。現在の機能と制作結果は毎回確認してください。

これは過去の制作記録と現行Studioで確認した機能を集めた制作用カタログである。アプリの全機能を網羅していると断定せず、現行ガイド・一覧・画面で更新する。

| 工程/機能 | 判断・操作 |
| --- | --- |
| 図案生成 | 刺繍向けに単純な色面、読みやすい文字、十分な穴を作る。生成画像を原図として目視確認する |
| 読込・枠・配置 | 画像変更、保存して次へ、枠、拡大率、回転、中央フィットを使う。110mm標準、小枠50mm、大枠140×200等は現行選択肢を確認 |
| 色・加工 | フラット、白黒、明るさ、くっきり、反転、アニメ、スポイト、全抽出、自由色、重要色、固定色モード、K色減色を必要に応じ使う |
| 色数 | 通常図案は8色から4〜5色へ整理する案。山など指定6色は尊重。白黒文字は背景を含め2色で解析し背景を縫わない |
| 仕上げ | 色マージ、ノイズ、結合、色別設定、最終ノイズ/結合、スキャンライン除去、プレビュー更新を必要時に使う。文字の穴をつぶさない |
| 領域解析 | 色数と島数を分けて扱う。犬図案で11,482島となった例のように極端な断片化では原図や減色を見直す |
| 輪郭 | 高精度抽出、最小エリア10px候補、平滑化の反復・許容誤差。輪郭数だけで品質判定しない |
| 背景除外 | 白を一律に削除せず、背景と必要な白い図柄を区別する。色全体SKIPか個別領域除外かを選ぶ |
| 領域別設定 | 色、方式、密度、ピッチ、角度、極小ステッチ除外を設定。全体への反映は個別調整を上書きするので意図して選ぶ |
| 畳縫い | 広い面を埋める。山は斜面方向、衣服は形に合う角度。文字全体の自動畳を最終版にしない |
| 走り縫い | 極細線・補助線に検討する。サテンにできないという理由だけで文字を線へ置換しない |
| L&S | 長短ステッチの機能があるか現行UIで確認し、自然な面や毛表現に検討する。毛並みPROと同一と仮定しない |
| Satin Art Pro | 島選択、軌道生成、中心線、スプライン、ピッチ/密度、サテン生成、Studioへ返送。文字は優先使用 |
| 島カット・分割 | 難しい文字や枝・急な曲線を一画へ分ける。実操作の有無は現行画面で検証 |
| 接合・交差 | 一画をつなぐ、交差の優先/解除は過去に追加報告あり。穴・外形を横切らないか確認 |
| 輪郭サテン | 外周を仕上げる。下に同じ普通の畳が重なる場合は除外。必要な下縫いを区別する |
| 下縫い | 形を支える必要な下縫いを確認し、主縫いとの密度過剰を避ける。実項目と用途を確認 |
| 毛並みPRO | 犬などの毛の流れに使う。方向・長短・密度・元領域との境界を調整しStudioで重複を確認 |
| 2色Mix | 2色選択、クロス/平行、間隔・密度、角度、ずれを設定して再生成。グラデーションは現行機能と間隔調整で確認 |
| Mix方式 | Tatami、Brick、Spiral、Fur等が現行選択肢にある場合、図案に合う方式を選ぶ |
| 虹色文字 | 3BIKI等は全5文字の可読性、文字間約1mm、各色、クロスハッチを確認。単なる色数増加で済ませない |
| 構成と順序 | 色別SKIP、Mix、島別構成、上下順、自動整列、サテン最後を使う。糸移動最短と画の重なりを両立させる |
| プレビュー | 元画像比較、表示切替、拡大縮小、画面フィット、再生、シーク、速度、ID、渡り糸、針落ち点、リアル描画を用途に応じる |
| 糸色・見え方 | Janome/Brother/RGB、糸太さ、影を確認。プレビュー太さを実データの密度変更と混同しない |
| 履歴 | Undo/Redo、プロジェクト保存/読込を使う。変更前後のデータを保全 |
| 出力 | JEF標準、PES/PEC/DSTは画面上試験的表記に注意。ファイル名、枠、詳細設定、分割は現行UIで確認。形式ごとに実ファイルを保存 |

## 記録の信頼度

- Studioの画像読込→2色減色→仕上げ→領域→輪郭→白SKIP→畳→JEF/PESは今回の「風」で操作確認済み。
- Satin Art Proの島選択→軌道→生成→Studio返送、2色Mixは過去の操作確認報告あり。現在も同じとは断定しない。
- 中心線・Start/End・島カット・一画接合・交差改善・毛並み細部は要望や実装報告を含む。現行UIと実図案の品質をその都度確認する。
- WebMCP一覧取得は今回のタブでmodelContext unavailable。サイトの「30機能準備済み」表示とブラウザ側検出を分ける。

## 制作例

- 「風をいい感じに」: 筆文字生成→文字の穴保持→サテンの一画設計→必要な島カット→返送→元畳停止→完成確認→JEF/PES。
- 「犬を刺繍に」: 単純な図案→4〜5色候補→背景除外→顔/衣服は畳等、毛は毛並み、輪郭はサテン→重複除外→出力。
- 「3BIKIを虹色で」: 全5文字を確認→文字間約1mm候補→領域別サテンと2色Mixの可否を確認→クロスハッチ→文字の読みやすさを優先。


刺繍プレビュー背景は白・薄いグレー・濃いグレーから選べる。表示だけの変更で、画像・ステッチ・出力ファイルには影響しない。生成ファイル一覧には形式、名前、容量と保存要求の状態を表示する。端末への保存完了は確認できないため、ユーザーがダウンロード一覧・保存先を確認する。


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
PROでfurStyle="zigzag"を選ぶ。根元中心を固定した等間隔の千鳥格子に配置する。zigzagSpacing=6〜40（PRO処理座標）、zigzagWidth=.05〜1（間隔に対する根元幅）、strokeLength=毛の長さを独立に調整。密度・旧zigzagRows／zigzagOverlapはこの方式では使わない。従来／ふわふわと通常の構成リストは変更しない。
1 毛束を配置で三角の配置ガイドを表示、2 くしで整えるで方向ブラシを使い、3 縫いを生成。根元中心はくしで移動せず、毛先の方向を変更する。細さ・長さが大きすぎれば均等配置でも重なるので確認する。画像の平坦部は同じ色・保護範囲内の方向を補間し、判定閾値だけで中心の根元を除外しない。全域に方向情報がなければ初期方向は仮なので手で整える。
輪郭／穴／選択マスクからの距離を4近傍で計算して外側から内側の帯へ縫う。同じ帯・同色の近い根元を候補にする。Aの出口根元とBの入口根元の中間点Mを作り、A毛先→M→B毛先。開始は最初の入口根元、終了は最後の出口根元。底辺は縫わない。候補の左右を比較し、近い側を入口にする。既存経路との交差、遠い相手、違う色、穴やマスクを横切る接続は除外する。繋がらない部分は別経路としてジャンプする。実際の3D形状を計算する方式ではなく、倒れた三角の毛を2D縫いで表現する。
PRO結果はファー構成リスト、任意の粗い畳／従来毛並みの下地は通常の構成リストに保持。短いジャンプの通常縫いへの接続は0固定。生成→最適化後の針数・JUMP・糸替え・時間幅を確認。送信／保存時は未生成の変更を再生成する。布での試し縫いが必要。
English: Uniform staggered fixed roots, independent spacing, width and length. Comb changes direction, not root positions. After placement, route outer distance bands first. Join tip A to midpoint(A exit root, B entry root) to tip B; leave triangle bases open. Validate colour/masks and crossings; disconnected chains remain jumps. Flat regions inherit nearby directions within the same protected colour region. This is a 2D stitch representation, not physical 3D simulation. Legacy/fluffy and optional normal-list underlay stay separate. Trial sewing is required.


## 全体・部分の再編集（2.16.0）
PRO詳細設定「全体・部分の調整」の「背景以外の全体を対象にする」で、画像端の最頻色と同じ色で端につながる背景を除外する。従来・ふわふわ・増毛で共通。背景が多色・端に人物が接する場合は誤判定があり得るので、Studioで島選択または消しゴムも使い、背景の縫い残りを確認する。
「部分を追加」で足・腕などの名前を付け、「範囲を囲む」で画像上をドラッグして四角の範囲を登録。「調整対象」を選択し、くしはその範囲のみに反映。全体を選ぶと全体のくし調整に戻る。部分の長さ・細さ・根元間隔・はみ出し指定は増毛・三角毛の生成時に適用。後に追加した部分が重なりで優先され、グリッド境界でも根元が密集しないよう検査する。全体ウィザードは個別設定を維持するため、個別領域の針数は別途確認する。
増毛の「輪郭内に収める」が初期設定。「外側へのはみ出しを許可」は画像端につながる背景のみに毛先を延ばす。はみ出し上限は処理画像の点数（mmではなく、BasicとDetailで実サイズが変わる）。根元は対象内、画像外・閉じた穴・他色・色別消しゴムは保護。背景を経由して別領域へ入ることはしない。外に出る毛は長い渡りを作らないため隣の毛と無理につなげず、ジャンプ増加を確認する。従来方式のはみ出し指定は本機能の対象外。
Studioへ「送信」すると、くしの場・色別マスク・部分名/範囲/数値・輪郭設定・背景以外の全体指定をfurSettingsとしてブラウザ内に保存し、PROを開き直す際に復元する。毛並み生成はファー構成リスト、畳縫い等の下地は通常の構成リスト。追加と入れ替えを区別し、再編集は既存毛並みを二重に追加しない。異なる画像を読む時は部分設定をリセットする。画像等はMCPサーバーへ送らない。
ブラウザWebMCP set_fur_settingsはwholeForeground, furBoundary, furOverhangを扱う。set_fur_partは名前と画像に対する0〜1の四角rect{x,y,w,h}、任意のstrokeLength/zigzagWidth/zigzagSpacing/furBoundaryを登録し、返ったidで同じ部分を更新できる。設定変更後は画面「調整を反映して生成」で再生成し、最終総針数と輪郭を確認。試し縫いを必ず行う。


輪郭から重ねる毛（試験）: 毛並みPROの「毛並みの表現」で選択。外側から内側へ輪郭の段を作り、交互の段をずらして三角毛を重ねる。毛の長さより段の間隔を小さくすると重なる。根元の間隔で本数、毛の細さで幅、段数・段の間隔で厚み、ずらす量で交互の配置を調整。複数の中心点を追加・移動・削除でき、毛の向きは中心から輪郭／輪郭から中心。輪郭内／外側はみ出し許可と上限は別設定。穴・他色・消しゴム範囲は保護、中心点は対象色の中に置く。くしの編集後は再生成。中心・段設定も保存とStudio往復に含む。下縫いは通常の構成リスト、毛はファー構成リスト。従来・ふわふわ・増毛三角毛は維持。点数とジャンプ、Studioで最終総針数を確認。試し縫い必須。WebMCP set_fur_settings: furStyle=contour、furCenters（画像正規化0〜1）、contourFurSettings。

## 2色・3色の糸色ミックス（2.16.2・試験）
サテンの輪郭花びらと毛並みPROの「輪郭から重ねる毛」で指定可能。2色は色A→色B、3色は色A→色B→色C。中間のRGB糸色を自動生成せず、既存の三角の花びら／毛を１つにつき１色へ割り振る。変わり目は50対50、手前75対25・先25対75のように割合が変化する。一定の誤差を次の毛に繰り越して均等に分散し、ランダムな塊にしない。毛束数と配置座標は維持するが、色の分割でJUMPは増える。短い形では実際に生成できた最後の段までの範囲へ色の変化を合わせる。１段だけは輪郭側の１色。
UI: 糸色ミックスON、糸の色数2/3、輪郭側・中間(3色のみ)・中心側の糸色、反転、縫い順。色別は同色をまとめて2色なら原則1回／3色なら2回の糸替え(このレイヤー内、実結果で確認)。全体の糸替えとは別。色別は外側→内側の全色共通の重なり順を変えるので試し縫い確認。段順は段の重なりを優先するが糸替えが増える。三角１つごとに糸替えしない。段数・間隔・長さ・くし・中心点・はみ出し設定は従来どおり。通常サテン／ライン花びら、従来毛並み／ふわふわ／増毛には適用しない。
保存：サテン花びら編集JSONのsettings、PROのcontourFurSettings内に全設定を保持。旧5色設定はサテン編集画面で2色へ移行する。古い生成済み結果は再生成するまで変えない。くしの方向・マスクは保持し、眼鼻口・穴・背景の保護と生成後の密度、JUMP、実点数、糸替えを比較する。ミシン針数・時間・品質はこのテストだけで保証しない。試し縫い必須。
WebMCP: Satin set_petal_thread_mix {gradientEnabled,gradientColors:2|3,gradientStart,gradientMiddle,gradientEnd,gradientReverse,gradientOrder:color|layer};輪郭花びら・中心点の準備後に生成。PRO set_fur_settings {furStyle:contour,contourFurSettings:{同じgradient設定とrows,rowGap,stagger,centerBlend,direction}}。inspect_satin_workはpetalEditor/threadMixMetrics、PROはinspect_fur_workで実生成経路の色数・糸替えと点数/JUMPを確認。操作は画面WebMCPだけ。MCPサーバーはガイド取得のみ。
English: Use exactly two or three specified threads. Distribute existing triangular tufts between adjacent colours, varying proportions with row depth (50/50 at transitions), with deterministic error diffusion. Do not add intermediate threads or duplicate tufts. Colour grouping reduces changes but alters overall overlap order; layer grouping preserves row order with more changes. Inspect actual jumps, colour changes, geometry and trial sew. Applies only to contour petal satin and contour overlapping fur PRO. Preserve editable settings and masks.


2.17.0: inspect_stitch_colors returns active solid colour groups and available thread codes. merge_stitch_colors explicitly assigns RGB groups to thread colours without changing contours, background skips or stitch settings. Default unsaved thread mode matches the UI (Janome). It does not automatically infer which shadows can be removed.


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

## 内外・方向・中心点・スタイルの設定選択（2.19.2）
制作前に、毛先の境界制限と毛の向きを別々に選ぶ。furBoundary=insideは選択領域内への制限、outsideは外背景への延長許可。contourFurSettings.direction=outsideは中心から輪郭方向、insideは輪郭から中心方向であり、境界制限とは独立。毛の方向は三角の根元から毛先の方向で、ミシンの縫い順とは別。
|用途|furBoundary|furOverhang|edgeBridge|方向|
|はみ出しなしの候補|inside|0|0|outsideまたはinsideを図案で判断|
|はみ出しありのクマB実測例|outside|8|12|outside|
はみ出しなしの候補は同じクマBの長さ22・根元間隔7・段間隔4・幅0.25・50段・ずらし0.5・中心ブレンド0.7を出発点にできるが、この境界変更後の実測点数・試し縫いは未確認。生成して輪郭、穴、端の欠け、点数を確認する。実測Bの11292点や全体17349点を候補版の結果として流用しない。
はみ出しありは、背景側への許容量furOverhangと外周線を通過する幅edgeBridgeを分ける。edgeBridgeはcontour専用の任意設定0～16整数、初期値0。大きくするほど外縁の模様への干渉も点検する。はみ出しなしではedgeBridgeを0にし、既存の外毛も停止して確認する。外へ毛先が出るだけで、背景に根元を生成する設定ではない。
スタイルはlegacy=従来、fluffy=従来とは別のふわふわ生成、zigzag=均一な根元に三角毛を置く増毛、contour=輪郭に沿って段を重ねる毛。見た目がふわふわでもcontourを使う場合がある。「ふわふわ」という希望だけでfluffyに固定せず、輪郭の重なり・根元の配置・点数を見て選ぶ。contour専用の段数・段間隔・中心ブレンド・edgeBridgeを他の方式にそのまま適用しない。
中心ポイントfurCentersは画像全体に対する0～1座標で、額・左右腕・左右足を分けて必要な場所に置く。クマB実例は額(0.5,0.3)、左右腕(0.36,0.62)/(0.66,0.62)。図案が変われば位置を見直す。ポイントは毛の向きを導き、根元の均等配置そのものを置き換えない。くしで方向を調整したら再生成し、放射状に硬くなりすぎないか確認する。
長さ、根元間隔zigzagSpacing、段間隔rowGap、はみ出し上限、edgeBridgeはPRO処理画像の座標値。処理解像度basic/detailや画像サイズが違えば見た目も変わり、mm値として説明しない。中心は正規化座標、stagger/centerBlendは0～1、rowsは段数、gradientColorsは1/2/3色。針方向という曖昧な語は、毛先方向・畳縫い角度（度）・点を縫う順番のどれか確認する。
MCPのget_jiminy_guideで判断材料を読む。実操作はブラウザWebMCPのset_fur_settings（設定）、set_fur_part（部分範囲）、inspect_fur_work（needsGeneration・busy・くし変更数・点数・JUMP・移動距離）、send_fur_to_studio（生成済み結果の受渡）と画面の変換を使う。optimize_fur_stitchesは入口要求で、ウィザードが開く場合がある。呼出だけで生成・最適化完了と報告しない。生成・確認後に送る。同じ部位の旧毛を停止し、通常構成リストの下地とFur構成リストの表毛を分ける。左右の共通色、目鼻口・花・穴・肉球を確認し、試し縫いする。
English: Separate boundary permission from hair-tip direction and machine sewing order. Record inside/outside examples with units, centers, style-specific controls and validation status. The inside-clipped counterpart of bear B is a proposed starting point, not a measured result. Read public guidance through MCP; operate locally through WebMCP and visible generation controls. Verify completion and preserve underlay and protected details.


## 中心の隙間を補う短い毛・弱いつむじ（2.23.6・試験）
Fur PROのcontourのみ。中心点を単なる収束点でなく短い毛の補完範囲として扱う。通常画面の輪郭毛設定で「中心の隙間を短い毛で埋める」をONにし、中心を埋める半径4〜80、中心の毛の長さ1〜40（いずれも処理画像px）、回す強さ−1〜1を設定する。0は渦なし、負は逆方向。選択した中心ごとに全体値／短い重なり(overlap)／つむじ(whorl)を選べる。旧プロジェクトはcenterFillEnabled=falseで従来形を保持。中心が保護マスクや別色上なら追加しない。千鳥の根元から短い三角毛を出し、外側へ既存毛長に馴染ませ、中心範囲の重複を最寄り中心の担当に分ける。明示的なくしの方向も優先し、目鼻口・穴・消しゴムを保護する。これは2D表現で物理的な毛や実機の縫い上がりではない。
ブラウザWebMCP/手動コマンド set_fur_settings の contourFurSettings に centerFillEnabled/centerFillRadius/centerFillLength/centerFillTwist、furCenters の各点に centerStyle=inherit|overlap|whorl を指定できる。設定後は再生成。補完毛もFur構成リストに保持し、下縫いは通常構成リストへ別途。保存・再編集で設定を保持する。
移動欄「毛の線をたどる移動」(followHairTravel=true)をONにすると、輪郭毛の広いサテン移動より優先し、元の毛の座標・順序を保持したまま既存線と短い10px接続を候補にする。針間隔20px、同じ島・元色・糸色とマスクを保護。大回りは拒否、自然につながらない場合はJUMPを保持。初期OFFで旧設定を変えない。設定は処理画像に対して座標倍率で換算する。JUMPをゼロにする目的ではない。
クマ顔の計算比較 /samples/bear-face/#K : H(中心補完なし)5333縫い点/432JUMP、K(額つむじ・頬耳overlap、半径28/毛10/回転0.2)6333/403、L(半径38/毛12)7268/383。5つの中心点と表の輪郭毛・2色は共通、下縫いなし。生成経路の非JUMP点であり機械形式での最終針数ではない。小さいKから比較し、中心が濃くなりすぎたら半径・長さ・回転を減らす。ブラウザ実操作・実機試し縫いは未確認。公開ガイドとソース内のスナップショットを更新し、インストール済み個人プラグイン本体の更新は別途確認する。サーバーMCPはガイド読取専用。


## 輪郭毛の毛先ゆらぎ・実糸比較（2.23.7・試験）
Fur PRO contourFurSettings.naturalVariation=0〜1。旧データと初期値は0で従来の計算を保持。根元の等間隔配置は保ち、輪郭接線を前後2点の方向と補間して細かな段差をなめらかにする。毛長を最大18%×設定値、向きを最大約4.6度×設定値で決定的に変化させる。毎回ランダムに変わる処理ではない。明示的なくしの強さ1の方向は変えない。長さは境界で切られるため輪郭や段の規則性は残る。目鼻口・穴・マスクを保護する。方向と長さの変更後に必ず再生成し、全体と頬・耳の拡大で比較。
クマM/N案はゆらぎ0.65、中心に合わせる強さ0.8、段間隔10、根元18、長さ34、中心増毛38/12/0.2。左右の頬・耳の中心位置を鏡像にした比較であり、自動左右対称検出ではない。Mはジャノメ214ブラウン1色、Nは205ダークブラウン→214ブラウン→213ベージュ3色。ソフト内のJANOME_THREADS表のRGBを使用し、公式JANOME糸色表 https://www7.janome.co.jp/global/wp-content/uploads/accessoriescatalog.pdf で番号と色名を確認。RGBは実物の色を保証しない。Fur画面の糸候補ボタンで同じRGBを選べるが、実機ファイルの糸番号設定完了を意味しない。Studioで実糸メーカー・番号・左右の共通割当と書き出し番号を確認する。別メーカーはそのメーカーの表で改めて選ぶ。
毛束を1回ずつ指定した1/3色へ分配し、架空の中間色糸は増やさない。色ごとにまとめる縫い順で糸替えを抑えるが重なり順は変わる。試し縫いをする。計算比較 /samples/bear-face/#M と #N はライブ画面制作やJEF/PES出力・試し縫いを行った証明ではない。目鼻口は参考塗り表示。毛先の調整を追加したため点数・JUMPは再計測し、最終ミシン針数と区別する。


## v239 縫い順の向き＋島内ジャンプ補修（試験）
毛並みリズムPROのset_fur_settings、花びらサテンPROのset_petal_settingsでoptimizeRouteDirection:true（初期ON）。既存の連続STITCHを経路として扱い、経路の境目をJUMPと誤認しない。動的計画法で前後の同一ドメイン移動距離を合わせ、短くなる場合だけ経路を逆順にする。経路順・糸色・段・針目の形は保つ。複数段をまたぐ連続経路とdirectionLockedは逆順にしない。色替え時の移動はこの距離集計の対象外。必ずしも最長JUMPが短くなる保証はない。
サテンPROのoneStroke:true、repairLongJump:trueでは最長一箇所だけでなく、同じ糸色・島内の複数JUMPを既存針目のグラフで回り込み、周囲の針方向になじませる。最大200箇所・追加2万点。毛並みPROの輪郭毛でfollowHairTravel:trueとrepairLongJump:trueなら、毛の線をたどる処理のあと同じ補修を適用（最大200箇所・追加2千点）。同RGBでも別の連結島は縫って横断せず、穴・マスク・選択外を避ける。経路がない／上限に達した所はJUMPを残す。内側のつなぎSTITCHと島間の機械JUMPを区別する。画像pxからmmへの縮尺と最終出力の針数を確認。
設定を変えたら再生成。ON/OFFで本体針目・糸色・段順、JUMP、移動距離、追加点数を比較。比較ページ /samples/route-optimization/ は保存された顔の毛データから計算した追加補修で、Studioの画面操作／実機の試し縫い／新JEF書出しは未実施。既存の顔合成JEFは前版のまま。新しい共通処理を畳や走り縫い全般に適用したとは言わない。布の試し縫いが必要。


## v240 複数色の島内JUMP経路／サテンの斜めつなぎ抑止
この項目はv239の複数色・サテンの補修方式を更新する。毛並みPRO set_fur_settings.islandTravelMode は auto / stitch / jump。初期autoは生成結果が1糸色なら従来の島内つなぎ縫い、複数糸色なら輪郭・穴・凹みを避ける針上げの島内JUMP。stitchは旧つなぎ縫い、jumpは1色でも島内JUMP。本体経路の逆順判断は継続する。各糸色の縫い順を保ち、A*の島内経路を移動間隔travelPitchごとの複数JUMPに分ける。追加点はisJump:true,islandJumpWaypoint:true。STITCHを追加せず、JUMP点数が増えても縫う針数の増加とは区別する。連結島・sourceColor・選択マスクを保護。別の島は通常のJUMPで、針上げを禁止すると機械的に移動できない。
サテンPROのrepairLongJump:trueは花びら／一筆サテンのJUMPを同じ島内で回り込ませる。斜めのつなぎSTITCHを追加せず、段の移動も複数JUMPにする。針目の形・色・段順を保つ。追加移動点最大2万、計算で通路が見つからない／上限に達した場合は報告のunreachable,budgetLimitedを見て再調整し、穴横断を解消したと断言しない。島内経路の各直線区間を厳密な輪郭交差／ラスタ境界で検査する。
JUMPは糸切りではない。糸切りなしでは渡り糸が布上に残ることがある。上の糸色で隠れるかはプレビューだけでは保証できず、最終色にも同じ注意。試し縫いで確認する。比較 /samples/route-optimization/ は保存済み毛データを用いた計算試作、画面操作と新JEF出力・実機未実施。一色の計算結果が前版と同一であること、3色の既存STITCH点数が不変で全JUMP区間が島内であること、穴・U字凹み・同RGB別島を検査。


## 輪郭毛の柔らかさ・細幅・境界検査（2.25.0）
輪郭毛だけの比較ではfurStyle=contourを使う。検証完了前にふわふわ・三角毛を削除せず、旧図案の互換性を保つ。
contourFurSettings.whorlSoftness=0〜1（0で従来）、adaptiveWidth=trueで細い部分の根元幅を縮める。外向きの毛先が収まらない場合は同じ色・保護範囲内の逆方向のみ試す。柔らかさは中心への方向集中と中心増毛の放射を緩める。くしは優先。centerBlend、naturalVariation、短い毛を合わせて全体・顔・足を拡大比較する。
Basicの保護マスクは元画像の対応範囲に保護画素が1点でもあればそのセルを保護する。輪郭毛の消しゴム変更後は線分全体を検査して分割する。最終はDetailでも確認。意図的外毛と保護穴の逸脱を区別する。
移動は既存の方向最適化・島内経路を使う。1色の縫う移動と複数色の島内JUMPを区別し、STITCH/JUMP/移動距離、unreachable/budgetLimitedを確認。ジャンプ数と未糸切りの糸露出は別。島・穴を横切らず離れた島のJUMPを0と約束しない。
AI操作は画面移動後にツール一覧とget_workspace_statusを取り直す。同名登録時・画面終了時は旧登録を解除（対応APIがある場合）。ホストの古いハンドルが直った証拠にはしない。読取→設定→生成→状態・全体/拡大→Studio取込→重複検査→出力。失敗した変更を無条件で再試行しない。
合成細幅テストで従来0点→39点、線分の収容と1画素保護穴の保存を確認。クマの美観や実縫製改善の証拠ではない。

2.25.1: 新規の選択は毛並み／輪郭毛／サテン／デッサン。旧ふわふわ・三角毛・ミックスは新規候補から外すが、旧プロジェクトの復元・再生成は保持。クマのDetail・1色輪郭毛の実生成では12,149点、STITCH12,148、JUMP1（開始位置への移動）。接続前の312JUMPから減少。元1095画素マスクで縫う12,148線分の保護範囲逸脱0を確認。混合3色とは解像度・設定が違うため同条件比較と呼ばない。実縫製は未検証。


## 輪郭毛の中央の継ぎ目・内毛/外毛（2.26.0）
毛と毛の一般的な隙間と、輪郭から内側へ重ねた段が出会う中央/斜めの継ぎ目を区別する。contourFurSettings.seamFillEnabledは2.26.0では初期OFF。2.26.1から新規は初期ON、保存済みのOFFは維持。OFFではv204の毛の生成と同一。ONでは同じ色・選択・消しゴムの保護範囲の内側だけに短い毛を追加し、既存の根元/毛先/くし/段数/糸色を変更しない。中心点から放射するcenterFillとは別。
seamFillWidth=1〜20（既定6）、seamFillLength=1〜40（既定8）、seamFillSpacing=2〜20（既定4）。単位はPRO処理座標。「中央の白線を補う（標準）」は幅10・長さ8・間隔4を設定してONにする。方向は近傍毛の軸を平均し、明示的なくしを優先。線分全体が同じ色・保護範囲内か検査し、追加毛の重複を抑える。穴・顔・肉球などの別領域は補わない。白線が必ず消える、布が必ず隠れるとは約束せず、密度/重なり/点数/JUMPを全体と拡大で比較する。
「輪郭内版」はfurBoundary=inside、furOverhang=0、edgeBridge=0。「少し外毛版」はfurBoundary=outside、furOverhang=3、edgeBridge=0。境界以外の設定と中心/くし/グラデーションは保持する。外毛は背景につながる外側だけへ許可し、内側の穴を外背景として扱わない。外周の別色の線が毛先を止める場合、edgeBridgeの幅を別に調整して、顔・穴への影響を再確認する。自動でその線を越えない。
四角の合成形状で基準510点、標準補い付き内毛594点、外毛612点を比較。これは低密度のアルゴリズム検査でありクマの最終針数ではない。OFFの完全一致、明示的なくし、再現性、外毛の上限、保護穴、3色の保持をテスト。実際のStudio→PRO受け渡しでクマも確認し、旧レイヤーを追加重複させず比較用コピーに置換する。試し縫いは別途必要。
MCPサーバーは公開ガイドの取得専用。seamFill設定を含む制作操作はページのWebMCPまたは画面操作で行い、図案・画面IDをMCPサーバーへ送らない。

2.26.1 中央のランダム補毛：新規・空の設定ではseamFillEnabled=true、seamFillJitter=.35。保存済みのseamFillEnabled=falseと、v204以前の既存輪郭設定（フラグ未保存）はOFFを維持。seamFillJitter=0〜1、0で規則的。標準ボタンは幅10・長さ8・間隔4・ランダム.35。中央の短い毛だけに、根元位置・長さ・向きの小さな固定乱数のゆらぎを加える。再生成で同じ形を再現する。強さ1のくしの方向にはランダムな回転を加えない。既存輪郭毛は変えない。保護境界内の近い補毛だけを連続経路へまとめ、穴や別色を横切る接続を作らない。補毛ON時の毛をたどる探索は、従来の迂回上限を満たせない高コスト領域だけ早めに打ち切る。受理される経路の形は保持する。生成量・JUMP・重なりは再確認。
