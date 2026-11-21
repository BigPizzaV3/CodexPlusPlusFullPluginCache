# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# Production recipes / 制作レシピ
> Historical supporting reference: past reports and proposed techniques are not current verification. Follow the v2.0 workflow and discover current capabilities for every production task. 過去の報告・候補手順を含む資料です。現在の機能と制作結果は毎回確認してください。

Read this for lettering, complex branch repair, animal designs, two-color decoration or troubleshooting. Preserve user choices over defaults. Values below are starting candidates, not machine-tested guarantees.

## 風 / Kaze lettering

- Plan the outer left/top enclosure, outer right hook, inner top stroke, inner enclosed shapes, central stem and lower sweep separately. Adapt this inventory to the actual typeface; do not cut based on a preconceived glyph.
- Determine which touching strokes belong to one uninterrupted satin path and which need cutting at branches or crossings. Cutting is a geometry operation, not merely skipping a color.
- Keep the character’s inner holes clear. Inspect both sides of satin strips at turns. A correct centerline alone does not prove correct needle landing.
- Preview the outer hook at high zoom for abrupt curvature, fan concentration, wide stitches and an unnatural final spike.
- Use 0.4mm spacing as a candidate only after identifying the actual spacing control. Verify start/end direction with playback. Confirm crossings remain correct after sorting.
- Return PRO stitches to Studio; turn off redundant plain fill in these exact regions. Recheck full glyph readability before exporting.
- 文字を最初から畳で仕上げない。自動サテンの難所を分割して詰める。部分畳が必要なら、その部分と理由を説明する。

## Y / D / G / geometric shapes

- Y: compare three-branch construction with a trunk-plus-branch construction. Inspect junction overlap and travel. Never force one spline through all three arms.
- D/G: separate the straight stem from the curved section when curvature bends abruptly. Adjust tangents and endpoint extension; check inner/outer strip boundaries.
- Circle: check continuity, seam and stitch fan. Square/triangle/star: inspect every corner; use subdivision where a smooth curve rounds away the intended point or concentrates stitches.
- Compare original silhouette with regenerated stitches; automatic success must not hide geometry distortion.

## Animals / 犬・毛並み

- Use a clean source with broad color areas. Start from roughly 4–5 useful colors where appropriate; preserve eye, nose and face landmarks.
- If islands number in the thousands, inspect texture noise. Simplify the image or quantization before attempting thousands of tiny stitch objects.
- Use Fur PRO where fur direction matters; keep eyes/nose distinct. Use fill for clothing or solid areas and suitable satin for outlines. Verify fur boundaries and avoid duplicating fill with fur.
- Export only after checking the complete animal looks like the original, not merely after seeing a nonzero stitch count.

## Multicolor text and 2-color Mix / 虹色文字

- For exact text such as 3BIKI, confirm all five characters in the original and final preview. Keep user-specified order and approximately 1mm character spacing when requested.
- Select the actual two thread colors for each Mix region. Use crosshatch or parallel as requested; inspect angle, offset and spacing.
- Distinguish color blending from satin geometry. Mix controls do not automatically produce good satin lettering. Confirm which methods the current UI can combine.
- For gradients, verify the actual supported technique; do not promise a gradient from an untested spacing change.
- Preserve face/garment colors from the user's design; do not substitute Janome/Brother approximations without checking the mapping and preview.

## Mountain scenes / 山

- Separate snow, slopes, distant mountains, forest and background. Use slope-oriented fill rather than one global angle everywhere.
- Keep lettering in Satin Art Pro and landscape in appropriate fills. Preserve intended layer order with any automatic travel optimization.
- Exclude empty background while retaining white snow and letter holes. White is not always background.

## Fault diagnosis / 失敗対応

| Observation / 現象 | Next action / 対応 |
| --- | --- |
| WebMCP modelContext unavailable | Report tab-specific discovery failure; use permitted UI controls. Do not fabricate browser flags or platform support |
| Site says AI functions ready | Treat as readiness only; obtain actual host tool list before claiming WebMCP discovery |
| PRO opens with no shape | Inspect transfer state and source region. Do not draw an unrelated replacement or claim transfer success |
| Spline kinks / 腰折れ | Inspect branch graph and curvature; subdivide natural strokes and smooth supported control points |
| Satin crosses a hole | Correct boundaries, path, connection or split. Do not fill the hole to mask the defect |
| Too-wide satin span | Split into safe geometry or explain local fill fallback; derive limits from machine/material settings, not an invented universal number |
| Dense intersection | Separate stroke order; reduce redundant overlap while maintaining junction coverage |
| Tatami remains beneath satin | Disable redundant region fill, retain intentionally needed underlay, regenerate |
| Thousands of islands | Simplify source, reduce texture, revisit colors and cleanup; preserve meaningful small details |
| Global settings overwrite edits | Restore from Undo or saved project; reflect settings only to intended selection |
| Side panel/menu clipped | Use available UI sizing, scroll or fit controls and inspect fresh state; do not guess hidden coordinates |
| Popup closes during selection | Reopen and inspect fresh controls; verify selected state before proceeding |
| Download listener times out | Inspect generated file links and documented shared download folder; verify actual nonempty files |
| Backup cannot be verified | Preserve current data and resolve saving before initialization |

## Final report / 完了報告

State actual stitch techniques per region, exported dimensions, hoop, thread colors, output filenames and preview. Mention unresolved operations and machine-test status. Separate screen confirmation from physical stitch quality. Never claim every Jiminy feature was tested; mark currently observed, historically reported and unverified capabilities.

## Photo fur checks
Read workflow: Dog photo keepsake / 愛犬の写真と毛並みリズム. Check intentional gaps vs missing coverage, preserve required underlay, use wizard/flow arrows/color mask eraser, and report combined stitches plus speed-based provisional sewing time.


## カラフルな鳥：全身の羽の比較例（2.20.0）
頭だけに羽を付けて完了にしない。羽がある頭・肩・胸・翼・尾を対象にし、目・白い顔・嘴・足・枝・背景は別の縫いとして保護。全身Fur PROの従来／サテン往復D、ふわふわ／毛並みロングE、Fur＋翼curve-fill＋尾flow-lines＋細い輪郭サテンFを比較した。
この図案のStudio実生成：D STITCH5524/JUMP2061、E STITCH5846/JUMP1828、F STITCH5737/JUMP1149。FはEよりJUMP約37％減。これを一般的な保証や針数目標にしない。Eは自然な柔らかさ、Fは翼の形が読みやすい候補。サテンPRO花びらと毛並みPRO輪郭・重ね毛の比較とは別の試作。
D/E普通の下地は畳間隔1.2mm・ピッチ4mm。この鳥の縮尺での値で、クマの粗い3〜5mm下地を機械的に流用しない。Fは翼の緑curve-fill間隔0.55mm、青／水色flow-lines間隔0.5mm、ピッチ3mm。上縫いを外して隙間が増えたら下地密度を検査して調整。頭と胸に残したFurとの重複は避ける。針数・JUMP・糸替え・全身と細部を比較し、試し縫いする。


## Studioから制作する花の2/3色比較（2.21.0）
単色ピンクの5枚花図案をStudioで1095×1095px・110mm枠に読み込み、2色減色（白背景＋花）→仕上げ→領域→輪郭→背景SKIPとする。Satin PROの試作設定はneat、中心547.5/547.5px、spacing34、length73、rows9、rowGap38、gather0.8、variation0.04、width0.8。2色は#f59eb8→#a92e59、3色は中間#e15c8fを追加、gradientOrder=color。2色のPRO生経路点1179、Studioでは2006表示点・Raw1377。これを機械針数と混同しない。
毛並みPROでは解像度が変わるのでStudioのpx値をそのまま流用しない。輪郭重ね毛contour、hair_satin、basic、根元間隔10、毛長36、幅0.8、20段・段間8・ずれ0.5・中心への寄せ0.8、内向き、はみ出しなし、中心0.5/0.5を試作した。2色の画面表示は8131経路点。密度を変更したら再生成を完了してから数値を読む。
同じ入力で色数のみを変えて比較する。中央の集中・境目の斑・背景の縫い込み・既存サテンと毛並みの重複を確認する。この設定は試作例で、下縫いも試し縫いも未検証。ハートの多中心サンプルには中央の空白があり、完成推奨例として扱わず修正比較用にする。

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


## 輪郭毛の中央の継ぎ目・内毛/外毛（2.26.0）
毛と毛の一般的な隙間と、輪郭から内側へ重ねた段が出会う中央/斜めの継ぎ目を区別する。contourFurSettings.seamFillEnabledは2.26.0では初期OFF。2.26.1から新規は初期ON、保存済みのOFFは維持。OFFではv204の毛の生成と同一。ONでは同じ色・選択・消しゴムの保護範囲の内側だけに短い毛を追加し、既存の根元/毛先/くし/段数/糸色を変更しない。中心点から放射するcenterFillとは別。
seamFillWidth=1〜20（既定6）、seamFillLength=1〜40（既定8）、seamFillSpacing=2〜20（既定4）。単位はPRO処理座標。「中央の白線を補う（標準）」は幅10・長さ8・間隔4を設定してONにする。方向は近傍毛の軸を平均し、明示的なくしを優先。線分全体が同じ色・保護範囲内か検査し、追加毛の重複を抑える。穴・顔・肉球などの別領域は補わない。白線が必ず消える、布が必ず隠れるとは約束せず、密度/重なり/点数/JUMPを全体と拡大で比較する。
「輪郭内版」はfurBoundary=inside、furOverhang=0、edgeBridge=0。「少し外毛版」はfurBoundary=outside、furOverhang=3、edgeBridge=0。境界以外の設定と中心/くし/グラデーションは保持する。外毛は背景につながる外側だけへ許可し、内側の穴を外背景として扱わない。外周の別色の線が毛先を止める場合、edgeBridgeの幅を別に調整して、顔・穴への影響を再確認する。自動でその線を越えない。
四角の合成形状で基準510点、標準補い付き内毛594点、外毛612点を比較。これは低密度のアルゴリズム検査でありクマの最終針数ではない。OFFの完全一致、明示的なくし、再現性、外毛の上限、保護穴、3色の保持をテスト。実際のStudio→PRO受け渡しでクマも確認し、旧レイヤーを追加重複させず比較用コピーに置換する。試し縫いは別途必要。
MCPサーバーは公開ガイドの取得専用。seamFill設定を含む制作操作はページのWebMCPまたは画面操作で行い、図案・画面IDをMCPサーバーへ送らない。

2.26.1 中央のランダム補毛：新規・空の設定ではseamFillEnabled=true、seamFillJitter=.35。保存済みのseamFillEnabled=falseと、v204以前の既存輪郭設定（フラグ未保存）はOFFを維持。seamFillJitter=0〜1、0で規則的。標準ボタンは幅10・長さ8・間隔4・ランダム.35。中央の短い毛だけに、根元位置・長さ・向きの小さな固定乱数のゆらぎを加える。再生成で同じ形を再現する。強さ1のくしの方向にはランダムな回転を加えない。既存輪郭毛は変えない。保護境界内の近い補毛だけを連続経路へまとめ、穴や別色を横切る接続を作らない。補毛ON時の毛をたどる探索は、従来の迂回上限を満たせない高コスト領域だけ早めに打ち切る。受理される経路の形は保持する。生成量・JUMP・重なりは再確認。
