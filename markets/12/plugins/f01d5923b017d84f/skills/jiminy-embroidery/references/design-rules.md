# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# Design analysis and stitch planning / 図案分析と縫い方

## Region record
For each meaningful region record identity (current ID plus visual location), semantic role, color, holes, connections/branches, approximate width at final mm size, proposed technique, direction, layer and inspection target. Rebuild ID mapping after region regeneration; IDs may change.
Separate background from white snow, white eyes and letter counters. Distinguish original image pixels, analysis pixels, hoop dimensions and actual stitched bounds.

## Decision rules
| Shape or goal | Starting method | Inspect |
| --- | --- | --- |
| Broad solid area | Tatami | coverage, angle, layering and distortion |
| Narrow filled strip | Satin | width, both boundaries, turns and long spans |
| Letters | Satin Art Pro where geometry fits | exact text, counters, joins, start/end |
| Extremely fine line | Running stitch | visibility, continuity and repeated passes |
| Directional organic texture | Fur PRO if available | flow, boundary and overlap |
| Outline | Suitable satin or running, usually last | registration and intended stroke weight |
| Crossed or layered color texture | 2-color Mix if supported | actual colors, spacing and coverage |

Choose methods from shape and desired finish, not subject name alone. Fur can express grass or movement; satin can express abstract ribbons. Do not force long satin across broad regions; split or explain local fill use.

## Parameters and material context
Treat 4–5 colors, 10px cleanup and 0.4mm satin spacing as initial candidates, not universal constants. Verify whether 10px means area or linear size and the working resolution. Verify whether a field means stitch spacing, sampling pitch or density before applying 0.4. Do not confuse preview thread thickness with stitch density.
Adapt to physical detail size, fabric, thread and machine when known. Ask about material/machine only when it materially affects the requested output. Do not invent a universal maximum satin length or JUMP threshold.
Retain useful underlay; remove duplicate main fills. Minimize travel subject to correct overlap, contour-last ordering and text crossing order.


## 動物の刺繍品質確認
クマなど動物は全体の毛並みと、目・鼻・口の輪郭を別々に拡大して確認する。毛並み、ロングショート、タタミを比較し、毛の向きと密度が整う方法を選ぶ。目・鼻・口を毛で覆わず、表情を保つ。毛が落書き状、飛び線だらけ、隙間だらけに見える場合は、密度や方向を調整し、必要なら制御されたロングショートまたはタタミに変更する。生成成功だけで品質良好と判断しない。全体と顔の拡大プレビューを確認してから出力する。

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
