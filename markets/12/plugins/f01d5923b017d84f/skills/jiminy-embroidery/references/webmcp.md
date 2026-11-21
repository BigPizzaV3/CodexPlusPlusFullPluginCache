# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# WebMCP operating rules / WebMCPの使い方

## 1. Discover the host and page
Read the actual browser/tool documentation exposed in this conversation. A browser feature named WebMCP must be advertised by the host; do not assume an API from memory. Select/reuse the requested Jiminy tab through documented APIs. Wait for observable initialization (loaded controls and stable status), without destructive reloads.
Check site readiness and current work. “AI functions ready” is site-side readiness, not evidence that the host discovered or called tools.
Use the host's documented discovery mechanism to obtain current tool names, descriptions and input schemas. If discovery is not available, record that fact and evaluate permitted UI operation. Do not probe private page objects or evaluate arbitrary JavaScript as a substitute.

## 2. Read before writing
Call get_workspace_status, get_studio_guide and get_studio_state only if present in the current list. Read their real schemas first; do not assume they accept empty arguments.
If these names are absent, use advertised equivalent read-only functions or visible UI. Identify current image, project/dirty state, hoop, colors, regions, stitches and active Studio/PRO surface from observed results.
Build a capability map for import, placement, colors, segmentation, cleanup, region settings, Tatami/running, Satin Art Pro, cuts/splits, centerlines, Start/End, Fur, Mix, preview, ordering, project save and exports. Mark each as available, UI-only, absent or unverified. Tool descriptions—not historical names—determine coverage.

## 3. Execute grounded operations
For each action specify observed target ID, schema-valid arguments, intended state change and verification. Recheck target IDs after segmentation. Respect units, enums, required fields and selection scope.
Save existing work before replacement/import. Verify the save, not merely a click. Use documented host file transfer procedures; local paths are not automatically browser-accessible.
Apply mutations sequentially where dependent. Await actual completion/jobs as documented; then read state or inspect the screen. Separate call acceptance from completed computation and from reflected output.
Inspect PRO input after opening and Studio output after returning. A Studio tool does not imply all Satin/Fur controls are exposed. Inspect tool availability for each surface.
Use preview/playback and inspect generated geometry. Successful JSON alone cannot prove lettering readability or smooth satin boundaries.

## 4. Handle errors and fallback
Record stage, actual tool/button, exact error, last confirmed state, preservation status and next available action. Redact credentials and connection secrets from public reports.
For timeout after a mutation, read state before retrying; it may have completed. Do not blindly duplicate imports, generation or exports. Retry transient errors once only after evidence supports it; otherwise change method or report the blocker.
For invalid arguments, reread schema and correct the field. For stale IDs, refresh mapping. For missing data in PRO, verify selection/transfer before geometry repair.
For modelContext unavailable or missing host capability, describe a tab/session-specific discovery failure; do not claim all Web/Desktop environments fail. If permitted, use visible browser controls under the host's fallback policy. If no operation route exists, give concise manual steps and mark production unexecuted.
For server MCP owner/authentication errors, distinguish that route from browser WebMCP; do not alter login or publication settings to fix a production request.

## 5. Future batch commands
Use a command/batch tool only when the current list and guide advertise it. Validate documented syntax and scope, establish backup, and keep checkpoints after analysis and preview. Inspect each step's status; on partial failure preserve successful work and resume only pending steps. Use documented stop/undo only if available. Never promise rollback for an irreversible operation.
Python-like examples are design proposals until implemented. Arbitrary eval is not a command parser. Reuse supported production operations rather than creating an undocumented parallel engine.

## Evidence levels
Record separately: site readiness; host discovery; successful invocation; expected state reflected; preview inspected; actual file saved. Claim only levels demonstrated in this task. Do not add fictional tool dependencies or MCP server URLs to this skill's metadata.


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


## 輪郭毛の柔らかさ・細幅・境界検査（2.25.0）
輪郭毛だけの比較ではfurStyle=contourを使う。検証完了前にふわふわ・三角毛を削除せず、旧図案の互換性を保つ。
contourFurSettings.whorlSoftness=0〜1（0で従来）、adaptiveWidth=trueで細い部分の根元幅を縮める。外向きの毛先が収まらない場合は同じ色・保護範囲内の逆方向のみ試す。柔らかさは中心への方向集中と中心増毛の放射を緩める。くしは優先。centerBlend、naturalVariation、短い毛を合わせて全体・顔・足を拡大比較する。
Basicの保護マスクは元画像の対応範囲に保護画素が1点でもあればそのセルを保護する。輪郭毛の消しゴム変更後は線分全体を検査して分割する。最終はDetailでも確認。意図的外毛と保護穴の逸脱を区別する。
移動は既存の方向最適化・島内経路を使う。1色の縫う移動と複数色の島内JUMPを区別し、STITCH/JUMP/移動距離、unreachable/budgetLimitedを確認。ジャンプ数と未糸切りの糸露出は別。島・穴を横切らず離れた島のJUMPを0と約束しない。
AI操作は画面移動後にツール一覧とget_workspace_statusを取り直す。同名登録時・画面終了時は旧登録を解除（対応APIがある場合）。ホストの古いハンドルが直った証拠にはしない。読取→設定→生成→状態・全体/拡大→Studio取込→重複検査→出力。失敗した変更を無条件で再試行しない。
合成細幅テストで従来0点→39点、線分の収容と1画素保護穴の保存を確認。クマの美観や実縫製改善の証拠ではない。
