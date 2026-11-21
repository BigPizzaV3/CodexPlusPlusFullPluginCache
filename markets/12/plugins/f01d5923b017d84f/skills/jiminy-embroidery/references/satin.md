# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# 文字・輪郭のサテン制作

## 文字を一画ごとに設計する

1. Satin Art Proを開き、対象の色・島・元図案が正しく渡ったか確認する。
2. 接続した文字を一つの自動軌道で済ませない。縦棒、横棒、曲線、払い、はね、枝分かれを見分ける。
3. 難しい島はカットして、一方向に自然に縫える単位へ分ける。現在のUIでカット・分割ができるか確認してから操作する。穴を横切る分割や輪郭の欠けを作らない。
4. 中心線取得→軌道/スプライン生成→Start/End指定→延長方向の調整→サテン生成を、存在する機能に合わせて進める。内部関数や操作名を想像で呼ばない。
5. 線を延長するときは図案の範囲内に収める。自動線が折れる場合は制御点・接線・曲率を確認し、不要点の整理、滑らかな曲線への調整、島の分割を選ぶ。
6. 交差点では上に見せたい画を後に縫う。「一画をつなぐ」「交差の優先/解除」が現行画面にあれば使い、再生成後の穴・外形・順番を確認する。

## 形ごとの判断

| 形 | 調整方針 |
| --- | --- |
| Y・三叉 | 3本の枝へ分ける案を検討し、分岐中央の過密と隙間を確認する |
| D・G | 縦棒と曲線を分ける。急曲率の始まりや腰折れを修正する |
| 風・漢字 | 外側の囲み、内側の画、交差、はね・払いを別に検討する。内側の穴を縫いで埋めない |
| 丸・角丸 | 軌道の連続と継ぎ目を確認し、一周の途中に急な折れを作らない |
| 星・三角・四角 | 鋭角や角の方向変化を分割候補とし、長い横断糸や集中を確認する |
| 広い筆画 | 長いサテンを無理に渡さず、分割サテンまたは部分的な畳併用を検討する |

## 設定と検証

- 密度/間隔は約0.4mmを初期候補にする。表示項目がピッチ・軌道サンプル間隔・縫い間隔のどれかを確認し、違う意味の項目に0.4を入れない。
- 角度45°の指定がある場合は実際の縫い方でその方向が適切か確認する。サテンの軌道と左右の針落ち、畳の角度を混同しない。
- Start/Endで上から下など希望方向を指定し、生成後の再生で通っていることを確かめる。
- PROで生成→Studioへ返送→Studioの構成リストとプレビューで反映を確認する。別画面の生成成功だけで返送成功と言わない。
- 元の普通の畳と重なっていればその領域を停止する。輪郭サテン、下縫い、別画を一緒に削除しない。
- 各画の接合、穴、太さ、はね、交差の上下、不要な戻り、渡り糸を拡大と全体で確認する。

島カット、始終点、交差操作は過去に要望・実装報告があるが、すべての図案で品質が実証されたわけではない。利用のたびに現行機能と完成形を検証する。


## 花びらサテン（試験）
Satin Art Proの右上「花びらサテン」を開く。毛並みロングとは別のサテン表現。方式は「ライン花びら」「輪郭花びら」。まず島を選択する。ライン方式は既存の描画ツールで線・曲線を描き、線の左／右を選ぶ。輪郭方式は外形・穴を個別に有効化し、それぞれ内側（刺繍面側）／外側（逆側）を選ぶ。外側は1段。
中心点追加・移動を押し、選択した島の内側をクリックして複数の中心を追加する。中心点はドラッグで移動、一覧で選択して削除できる。中心は所属する島を担当し、同じ島内では近い中心へ振り分ける。自由な担当範囲の手描き指定はまだない。中心操作終了後、通常の島／ライン操作へ戻る。
根元の間隔、長さ、幅、段数、段間隔、中心への寄せ具合、傾き、ばらつきを変更し「花びらを生成」。数値の単位は処理画像pxで、ミシンのmmとは別。外周から内側へ段を作る。内側の段も間隔を再調整する。穴／外形を横切る内向き接続は生成しない。複数中心や凹形状では欠けが出るためプレビューを確認する。
生成結果は通常のサテン構成としてStudioへ送る。編集を続ける場合は「花びら編集データを保存」でJiminy_Petal_Editor.jsonを保存し、同じパネルで開く。画像領域・線・中心・設定を保存する。これはミシン用ファイルではない。通常サテンと花びら方式を切り替えた後は再生成が必要。試し縫いで仕上がりを確認する。


## 2色・3色の糸色ミックス（2.16.2・試験）
サテンの輪郭花びらと毛並みPROの「輪郭から重ねる毛」で指定可能。2色は色A→色B、3色は色A→色B→色C。中間のRGB糸色を自動生成せず、既存の三角の花びら／毛を１つにつき１色へ割り振る。変わり目は50対50、手前75対25・先25対75のように割合が変化する。一定の誤差を次の毛に繰り越して均等に分散し、ランダムな塊にしない。毛束数と配置座標は維持するが、色の分割でJUMPは増える。短い形では実際に生成できた最後の段までの範囲へ色の変化を合わせる。１段だけは輪郭側の１色。
UI: 糸色ミックスON、糸の色数2/3、輪郭側・中間(3色のみ)・中心側の糸色、反転、縫い順。色別は同色をまとめて2色なら原則1回／3色なら2回の糸替え(このレイヤー内、実結果で確認)。全体の糸替えとは別。色別は外側→内側の全色共通の重なり順を変えるので試し縫い確認。段順は段の重なりを優先するが糸替えが増える。三角１つごとに糸替えしない。段数・間隔・長さ・くし・中心点・はみ出し設定は従来どおり。通常サテン／ライン花びら、従来毛並み／ふわふわ／増毛には適用しない。
保存：サテン花びら編集JSONのsettings、PROのcontourFurSettings内に全設定を保持。旧5色設定はサテン編集画面で2色へ移行する。古い生成済み結果は再生成するまで変えない。くしの方向・マスクは保持し、眼鼻口・穴・背景の保護と生成後の密度、JUMP、実点数、糸替えを比較する。ミシン針数・時間・品質はこのテストだけで保証しない。試し縫い必須。
WebMCP: Satin set_petal_thread_mix {gradientEnabled,gradientColors:2|3,gradientStart,gradientMiddle,gradientEnd,gradientReverse,gradientOrder:color|layer};輪郭花びら・中心点の準備後に生成。PRO set_fur_settings {furStyle:contour,contourFurSettings:{同じgradient設定とrows,rowGap,stagger,centerBlend,direction}}。inspect_satin_workはpetalEditor/threadMixMetrics、PROはinspect_fur_workで実生成経路の色数・糸替えと点数/JUMPを確認。操作は画面WebMCPだけ。MCPサーバーはガイド取得のみ。
English: Use exactly two or three specified threads. Distribute existing triangular tufts between adjacent colours, varying proportions with row depth (50/50 at transitions), with deterministic error diffusion. Do not add intermediate threads or duplicate tufts. Colour grouping reduces changes but alters overall overlap order; layer grouping preserves row order with more changes. Inspect actual jumps, colour changes, geometry and trial sew. Applies only to contour petal satin and contour overlapping fur PRO. Preserve editable settings and masks.


## 初心者向けの見た目候補とWebMCP（2.20.0）
花びらサテンの上部に「整った花びら」「軽い飾り縫い」「2色が混ざる花びら」の初期候補を用意。画像pxの出発点なので図案の大きさに合わせて調整。中心点やラインは候補切替で削除しない。軽い飾りの中央の空きは意図した表現で、全面を埋める候補と混同しない。
現在のページで機能一覧を取得し、select_satin_island→apply_petal_preset {preset:neat|light|blend}→set_petal_center {islandId,x,y[,centerId]}→set_petal_settings→generate_petal_satin→inspect_satin_work。中心点は画像pxで島の内側。centerId指定は移動。set_petal_settingsはmode、spacing、length、width、rows、rowGap、gather、angle、variation、lineSide、outerSide、holeSide、includeOuter、includeHolesを変更し、set_petal_thread_mixは糸色を変更する。最後に生成する。返送後に元の畳との重複、輪郭と穴を確認。リモートMCPに操作や画像は送らない。
毛並みPROの輪郭・重ね毛を比較する場合、furStyle=contour、zigzagSpacing、zigzagWidth、strokeLength、contourFurSettingsのrows/rowGap/stagger/centerBlend/directionとfurBoundary/furOverhangを使う。柔らかく重ねるには段間隔＜毛の長さ、交互段のずらしを候補にする。はみ出しは目・穴・背景を保護して検査。花びらサテンと同じ数値をそのままコピーせず処理解像度と最終サイズを確認。

比較サンプル：https://jiminy-stitch-studio-agent.nihonno.chatgpt.site/samples/pro-satin/ （花1色・葉2色・ハート3色、各Satin PRO／毛並みPRO）。下縫いなしの試作。凹形状と複数中心は欠け・継ぎ目を確認し、必要なら分割・中心位置・段数を変更。JEFの糸番号は近似色で、実糸色は設定を確認。


## 2色・3色グラデーション比較（2.21.0）
2色は指定した始点色・終点色の糸だけを使い、境目付近の出現割合を徐々に入れ替える。3色は中間色を明示する。画面上の連続RGB補間を、追加の糸色として増やさない。gradientReverseで内外の色を反転できる。
Satin PROはset_petal_thread_mix、毛並みPROはset_fur_settings.contourFurSettingsで設定する。gradientOrder=colorは糸替えを抑え、layerは段の重なり順を優先する。最終の重なり・JUMPを見て判断する。
再びSatin PROを開くと花びら設定・中心点が初期値になるケースを実際のStudio試作で確認した。戻れば設定が必ず残るとは案内しない。編集データを保存し、再編集時に中心点・間隔・段数・グラデーションの有効状態を確認して再設定する。

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

2.23.1 repairLongJump=true：一筆サテンの元の針座標・順序・色を保持し、同色・同島の最長JUMP（100px以上）だけ既存サテン線をたどる島内ステッチへ変更。travelPitchは追加針間隔上限。穴・別島・色替えは縫って横断しない。安全な経路がない場合や探索対象3000点超はJUMP保持。花比較786→800経路点、JUMP5→4。試し縫い未確認。

2.23.2 JUMP限定修正を新規設定で初期ONにする。保存済みの明示的OFFは保持。既存針位置・順序を保ち、移動が周囲の針方向を横切る区間だけ局所針方向に交互に振る。輪郭と穴の安全判定で振幅を縮める。針方向に沿っている移動には余分な横振りを足さない。追加針間隔はtravelPitch上限。花比較の追加点14→38、総経路点800→824。実機の針数ではなく、重なり・厚みは試し縫いで確認。

2.23.3 毛並みPROのサテン・輪郭毛でもrepairLongJump=trueを新規設定で初期ONにする。set_fur_settingsで明示OFF可。furStyle=contour またはroutingMode=hair_satinに限り、通常のtravelModeより優先。生成後の本体と縫い順を保ち、同色・同じ連結島の最長JUMP（処理座標100px以上）一箇所だけ局所針方向へ振る島内移動ステッチに変更。travelPitchはPRO処理座標、表示座標へscaleを一度だけ掛ける。外毛本体を許可していても移動は元の色領域の内側のみ。穴・色別消しゴム・選択除外・外背景を越えず、接続できなければJUMP保持。毛並みPROは経路の先頭をJUMPとして扱うため修正した二経路だけ同じ順序で結合してStudioへ戻す。最適化ボタンでもこの方式がONなら全体を並べ替えずJUMP限定調整。その他の旧毛並みは従来通り。花の計算比較JUMP38→37、2101→2147経路点（46点追加）。実画面操作と機械書出し・試し縫いは未実施。

2.23.4 毛並みPROのrepairLongJump=trueは最長一箇所ではなく、同色・同じ連結島で安全につなげられるJUMPを複数調整する。サテンPRO側は承認済みの最長一箇所方式を保持。毛並み本体・針順・色は不変。各経路は追加済みのつなぎではなく不変の元データから計画し、周囲の針方向へ振る。島外・穴・マスク・別島・色替え・経路なしはJUMP保持。最大200箇所、追加2万経路点の上限。探索対象3000点超の色グループは保持。花計算比較JUMP38→3（入口と2色替え）、35箇所接続、695点追加、2101→2796経路点。追加箇所の厚み・中心重なりは試し縫いで確認。経路点と最終機械針数を区別。

2.23.5 所長の見た目評価により毛並みPROはv182の広いサテン移動へ戻す。専用保持モジュールで幅168・前進28・針間隔20を比較。サテンPROの承認済み一筆サテンとJUMP限定調整は保持。毛並みPROのrepairLongJump=trueという互換設定名は広い移動のONを表す。前の広い移動プリセットボタンで168/28/20を再適用でき、保存済み数値は保持。毛並み本体の形を保ちながら縫い順と移動を計画するため、縫い順を固定する方式ではない。同じ色領域の連結島内だけを移動し、穴・色替え・マスク・外背景は縫って越えない。狭い場所は幅を縮める。比較は当時の保存済み毛並み本体を使用し877→26JUMP、総31463経路点を完全再現。現在の毛並み密度設定を当時に戻す操作ではない。追加点が多くなるので針数・厚み・重なり・縫製時間と試し縫いを確認。機械針数ではない。


## v239 縫い順の向き＋島内ジャンプ補修（試験）
毛並みリズムPROのset_fur_settings、花びらサテンPROのset_petal_settingsでoptimizeRouteDirection:true（初期ON）。既存の連続STITCHを経路として扱い、経路の境目をJUMPと誤認しない。動的計画法で前後の同一ドメイン移動距離を合わせ、短くなる場合だけ経路を逆順にする。経路順・糸色・段・針目の形は保つ。複数段をまたぐ連続経路とdirectionLockedは逆順にしない。色替え時の移動はこの距離集計の対象外。必ずしも最長JUMPが短くなる保証はない。
サテンPROのoneStroke:true、repairLongJump:trueでは最長一箇所だけでなく、同じ糸色・島内の複数JUMPを既存針目のグラフで回り込み、周囲の針方向になじませる。最大200箇所・追加2万点。毛並みPROの輪郭毛でfollowHairTravel:trueとrepairLongJump:trueなら、毛の線をたどる処理のあと同じ補修を適用（最大200箇所・追加2千点）。同RGBでも別の連結島は縫って横断せず、穴・マスク・選択外を避ける。経路がない／上限に達した所はJUMPを残す。内側のつなぎSTITCHと島間の機械JUMPを区別する。画像pxからmmへの縮尺と最終出力の針数を確認。
設定を変えたら再生成。ON/OFFで本体針目・糸色・段順、JUMP、移動距離、追加点数を比較。比較ページ /samples/route-optimization/ は保存された顔の毛データから計算した追加補修で、Studioの画面操作／実機の試し縫い／新JEF書出しは未実施。既存の顔合成JEFは前版のまま。新しい共通処理を畳や走り縫い全般に適用したとは言わない。布の試し縫いが必要。


## v240 複数色の島内JUMP経路／サテンの斜めつなぎ抑止
この項目はv239の複数色・サテンの補修方式を更新する。毛並みPRO set_fur_settings.islandTravelMode は auto / stitch / jump。初期autoは生成結果が1糸色なら従来の島内つなぎ縫い、複数糸色なら輪郭・穴・凹みを避ける針上げの島内JUMP。stitchは旧つなぎ縫い、jumpは1色でも島内JUMP。本体経路の逆順判断は継続する。各糸色の縫い順を保ち、A*の島内経路を移動間隔travelPitchごとの複数JUMPに分ける。追加点はisJump:true,islandJumpWaypoint:true。STITCHを追加せず、JUMP点数が増えても縫う針数の増加とは区別する。連結島・sourceColor・選択マスクを保護。別の島は通常のJUMPで、針上げを禁止すると機械的に移動できない。
サテンPROのrepairLongJump:trueは花びら／一筆サテンのJUMPを同じ島内で回り込ませる。斜めのつなぎSTITCHを追加せず、段の移動も複数JUMPにする。針目の形・色・段順を保つ。追加移動点最大2万、計算で通路が見つからない／上限に達した場合は報告のunreachable,budgetLimitedを見て再調整し、穴横断を解消したと断言しない。島内経路の各直線区間を厳密な輪郭交差／ラスタ境界で検査する。
JUMPは糸切りではない。糸切りなしでは渡り糸が布上に残ることがある。上の糸色で隠れるかはプレビューだけでは保証できず、最終色にも同じ注意。試し縫いで確認する。比較 /samples/route-optimization/ は保存済み毛データを用いた計算試作、画面操作と新JEF出力・実機未実施。一色の計算結果が前版と同一であること、3色の既存STITCH点数が不変で全JUMP区間が島内であること、穴・U字凹み・同RGB別島を検査。


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
