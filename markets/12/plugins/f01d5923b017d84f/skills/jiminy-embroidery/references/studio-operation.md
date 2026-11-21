# Studio operation reference / 本体操作の判断資料
const GUIDE = {
  proEntry: '初回は必ずStudioから開始。画像と枠・完成寸法 → 減色 → 仕上げ → 領域解析 → 輪郭抽出 → 背景除外・色・基本の縫い設定を準備する。サテンはopen_stitch_pro {kind:"satin"}、毛並みは{kind:"fur"}で図案を渡す。PROのURLを直接開いても図案は渡らない。',
  preserveWork: '別の図案を始める前に現在の編集用JSONを保存し、実ファイルの取得を確認する。新しいPCでは前の作業や接続が自動復元されると仮定しない。',
  proReturn: 'PROへの移動後は機能一覧を再取得して状態を読む。データが空ならStudioへ戻って受け渡し直す。生成したらStudioへ送信し、inspect_pro_resultで追加／入替を確認。元の畳縫いとの重なりと全体を確認して保存する。',
  workflow: '元画像を目視し、素材・毛並み・線・重要な細部を見分ける。減色、輪郭、技法、縫い順をプレビューで比較し、必要なら部分修正して再生成する。最後に枠と形式を確認して書き出す。',
  hints: [
    '減色の指定数は図案の見た目の色数と同じとは限らない。背景や影、半透明部分も確認する。',
    '島の数は色数ではない。多すぎる場合は小さな断片、背景、ノイズ、仕上げ処理を画像と合わせて確認する。',
    '広い面には畳縫い、狭い線にはサテンや走り縫いを候補にする。幅、糸密度、布と機械の条件で変わる。',
    '輪郭を最後に縫うと境界が締まる場合がある。重なりや渡り糸をプレビューで確認する。',
    '縫い順は下地・奥の面から手前の面へ検討し、色替え、渡り糸、引きつれを点検する。',
    '犬やキツネなど毛のある図案は毛並み縫いを候補にする。ただし顔の細部や広い面まで一律に変更せず、画像の毛流れと試作を比較する。',
    '初回に文字や細線を扱うときはサテンアートPROの inspect_satin_work で状態を読み、元画像とプレビューを見て島を選ぶ。自動の軌道を作ると、ほぼ直線は端点だけのライン、曲がる軌道は島内に収まる範囲で制御点を減らしたスプラインになる。制御点数だけを品質と見なさず、穴・輪郭・針目を確認する。16点を超える軌道は needsPointReduction を参考にWorkが微調整する。',
    '文字は字形の骨格と筆の流れを手掛かりに、直線・曲線・角・交差・穴に応じて必要な部分だけ分ける。分割後はset_satin_stroke_routeで中心線を指定できる。サテンの針は軌道を横切るため、軌道の向きと針目の向きは別に確認する。'
  ],
  satinReview: {
    start: '英数字・ひらがな・カタカナ・漢字のいずれも元画像の骨格を見て、自然な直線・曲線・折れ・交差・閉じた輪に分解する。島1個が筆1本とは限らない。必要な箇所だけ分割し、穴・開口・文字の読みやすさを保つ。',
    universalStrokeCriteria: {
      segmentation: '方向が急に変わる角、交差、枝分かれ、閉じた輪、幅の急変では分割を検討する。見た目上つながる字形を機械的に切らない。漢字の横画・縦画・はらい・曲がりも一画の骨格として観察する。',
      line: '一筆の中心線を端点間の線でなぞっても輪郭の中央に収まり、幅の変化・曲がり・字形の特徴を損なわないときに直線を選ぶ。縦画でも自動候補が曲がったなら画像の縦画を基準に引き直す。',
      spline: '連続した曲がりが字形に必要ならスプラインを選ぶ。角や交差を一本の滑らかな曲線で丸めず、必要なら筆を分ける。制御点は曲率が変わる場所と端点を優先し、減らした後の中心線と針目を再確認する。',
      judgment: '自動判定は候補点列の幾何だけを見るため、それが文字のどの筆かは分からない。Workが元画像の骨格、穴・開口、交差での前後関係を見て、候補を採用・修正・棄却する。'
    },
    endpoints: 'まず自動ボタンで中心線を取得し、形を画面で見る。閉じたループはそのまま使い、切らずに端も延長しない。島をカットして開いた線や枝分かれでは、始点・終点を方向と延長の判断材料にする。自動曲線を2点の直線へ置き換えない。outerの自由端だけ輪郭近くまで伸ばし、junctionは伸ばさない。枝は主線を残してappend:trueで追加し、接合部の針目を確認する。',
    sequence: ['分割位置と島の形を確認', '軌道の始点・終点と進行方向を確認', '直線かスプラインかを選ぶ', '必要な曲がりだけを残して制御点と曲線強度を調整', 'サテン生成後の針目・穴・元の畳縫いとの重なりを確認'],
    routeAcceptance: '点が少なくても、中心から外れる、折り返す、穴や島の外へ出る、急に曲がる軌道は採用しない。needsPointReductionは16点超の見直し目印であって合否判定ではない。必要な曲がりは残す。',
    stitching: 'サテンの針は中心線を横切る向きになる。針目の向きと幅、角の詰まり、文字の可読性を元画像と比較する。悪化したら変更前の図案からやり直し、分割・軌道・密度を順に再検討する。',
    output: 'Studioへ送る前に元の畳縫いを置き換えるか判断し、送った後は重なりと縫い順を確認する。JEF/PESの保存だけで品質が保証されるわけではない。',
    examplesOnly: 'Dの縦棒と曲線、Gの開口部、漢字の横画と縦画は確認用の例であり、線種や分割の固定ルールではない。'
  },
  caution: 'このガイドは候補であり、自動決定や刺繍機での品質保証ではない。画面を見て判断する。'
};
Read workflow first; this reference supplies additional Studio/Satin inspection criteria.

出力後は get_generated_files または get_studio_state で実際に生成された形式・名前・容量を確認する。downloadRequested はブラウザへの保存要求であり端末への保存完了ではない。保存が始まらない場合は画面の生成ファイル名を押す。


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


## 全体・部分の再編集（2.16.0）
PRO詳細設定「全体・部分の調整」の「背景以外の全体を対象にする」で、画像端の最頻色と同じ色で端につながる背景を除外する。従来・ふわふわ・増毛で共通。背景が多色・端に人物が接する場合は誤判定があり得るので、Studioで島選択または消しゴムも使い、背景の縫い残りを確認する。
「部分を追加」で足・腕などの名前を付け、「範囲を囲む」で画像上をドラッグして四角の範囲を登録。「調整対象」を選択し、くしはその範囲のみに反映。全体を選ぶと全体のくし調整に戻る。部分の長さ・細さ・根元間隔・はみ出し指定は増毛・三角毛の生成時に適用。後に追加した部分が重なりで優先され、グリッド境界でも根元が密集しないよう検査する。全体ウィザードは個別設定を維持するため、個別領域の針数は別途確認する。
増毛の「輪郭内に収める」が初期設定。「外側へのはみ出しを許可」は画像端につながる背景のみに毛先を延ばす。はみ出し上限は処理画像の点数（mmではなく、BasicとDetailで実サイズが変わる）。根元は対象内、画像外・閉じた穴・他色・色別消しゴムは保護。背景を経由して別領域へ入ることはしない。外に出る毛は長い渡りを作らないため隣の毛と無理につなげず、ジャンプ増加を確認する。従来方式のはみ出し指定は本機能の対象外。
Studioへ「送信」すると、くしの場・色別マスク・部分名/範囲/数値・輪郭設定・背景以外の全体指定をfurSettingsとしてブラウザ内に保存し、PROを開き直す際に復元する。毛並み生成はファー構成リスト、畳縫い等の下地は通常の構成リスト。追加と入れ替えを区別し、再編集は既存毛並みを二重に追加しない。異なる画像を読む時は部分設定をリセットする。画像等はMCPサーバーへ送らない。
ブラウザWebMCP set_fur_settingsはwholeForeground, furBoundary, furOverhangを扱う。set_fur_partは名前と画像に対する0〜1の四角rect{x,y,w,h}、任意のstrokeLength/zigzagWidth/zigzagSpacing/furBoundaryを登録し、返ったidで同じ部分を更新できる。設定変更後は画面「調整を反映して生成」で再生成し、最終総針数と輪郭を確認。試し縫いを必ず行う。


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

## 外毛クマの比較実例（2.19.1）
この図案の頭・腕の選択領域50で、contour、basic、outside、edgeBridge=12、幅0.25、50段、ずらし0.5、中心方向ブレンド0.7を使う。額(0.5,0.3)、左右腕(0.36,0.62)/(0.66,0.62)を中心点とし、外から #9e6a3e → #bf8550 → #d6ad7f の3色にする。
|案|長さ|はみ出し上限|根元間隔|段間隔|PRO点数|JUMP|移動距離概算mm|
|---|---:|---:|---:|---:|---:|---:|---:|
|A 控えめ|18|4|8|4|9993|1894|3854.66|
|B 基準|22|8|7|4|11292|2129|4214.51|
|C 強め|28|12|6|3|24852|3140|5476.52|
長さ・上限・間隔・edgeBridgeは処理画像の座標値でありmmではない。PRO点数にはJUMPも含み、最終ミシン針数とは別。Bはこのクマで外毛量と点数のバランスがよい基準候補。Cは毛量が増えるが放射状の硬い毛や時間増加を確認する。すべての図案でBを固定使用しない。
edgeBridge=6の初回案では毛先が背景へ出なかった。密度だけ増やして成功としない。太い外周線を越える幅を12に調整後、保存データと元画像を照合し、Bの毛の点475点が端につながる白背景に出たことを確認した。475は背景側の毛の点数で、475本の毛ではない。全体の点数は17349。目鼻口・花・穴は拡大して確認し、外縁近くの模様への干渉も確認する。
左右足は同じ2色、腹は部位ごとの1色を保ち、通常の粗い下地を残す。頭・腕の旧毛を停止して二重縫いを避ける。保存名BEAR_FLUFFY_OUTSIDE_B_FINAL.jiminyを対照・再編集の実例とする。画面と保存データで確認済みだが実機縫製は未確認。必ず試し縫いする。
English: Use the bear A/B/C trial as a measured example, not a universal preset. Processing-pixel settings are not mm; PRO point counts include jumps. Verify actual exterior geometry, preserve part palettes and separate underlay, disable old fur for the same part, inspect protected details, and trial sew.

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

2.23.3 毛並みPROのサテン・輪郭毛でもrepairLongJump=trueを新規設定で初期ONにする。set_fur_settingsで明示OFF可。furStyle=contour またはroutingMode=hair_satinに限り、通常のtravelModeより優先。生成後の本体と縫い順を保ち、同色・同じ連結島の最長JUMP（処理座標100px以上）一箇所だけ局所針方向へ振る島内移動ステッチに変更。travelPitchはPRO処理座標、表示座標へscaleを一度だけ掛ける。外毛本体を許可していても移動は元の色領域の内側のみ。穴・色別消しゴム・選択除外・外背景を越えず、接続できなければJUMP保持。毛並みPROは経路の先頭をJUMPとして扱うため修正した二経路だけ同じ順序で結合してStudioへ戻す。最適化ボタンでもこの方式がONなら全体を並べ替えずJUMP限定調整。その他の旧毛並みは従来通り。花の計算比較JUMP38→37、2101→2147経路点（46点追加）。実画面操作と機械書出し・試し縫いは未実施。

2.23.4 毛並みPROのrepairLongJump=trueは最長一箇所ではなく、同色・同じ連結島で安全につなげられるJUMPを複数調整する。サテンPRO側は承認済みの最長一箇所方式を保持。毛並み本体・針順・色は不変。各経路は追加済みのつなぎではなく不変の元データから計画し、周囲の針方向へ振る。島外・穴・マスク・別島・色替え・経路なしはJUMP保持。最大200箇所、追加2万経路点の上限。探索対象3000点超の色グループは保持。花計算比較JUMP38→3（入口と2色替え）、35箇所接続、695点追加、2101→2796経路点。追加箇所の厚み・中心重なりは試し縫いで確認。経路点と最終機械針数を区別。

2.23.5 所長の見た目評価により毛並みPROはv182の広いサテン移動へ戻す。専用保持モジュールで幅168・前進28・針間隔20を比較。サテンPROの承認済み一筆サテンとJUMP限定調整は保持。毛並みPROのrepairLongJump=trueという互換設定名は広い移動のONを表す。前の広い移動プリセットボタンで168/28/20を再適用でき、保存済み数値は保持。毛並み本体の形を保ちながら縫い順と移動を計画するため、縫い順を固定する方式ではない。同じ色領域の連結島内だけを移動し、穴・色替え・マスク・外背景は縫って越えない。狭い場所は幅を縮める。比較は当時の保存済み毛並み本体を使用し877→26JUMP、総31463経路点を完全再現。現在の毛並み密度設定を当時に戻す操作ではない。追加点が多くなるので針数・厚み・重なり・縫製時間と試し縫いを確認。機械針数ではない。


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
