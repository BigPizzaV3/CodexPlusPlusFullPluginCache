# Transport policy / 通信の絶対条件
MCP server supplies public guides only. Never send operation commands, browser/session IDs, images, stitch data, project data, or previews to this server. No command relay, polling queue, remote browser control, uploads, or server project persistence.
MCPサーバーは公開制作ガイドの取得専用。操作は現在のホストが正式に提供するブラウザWebMCPまたは画面操作のみ。画像はブラウザのファイル選択、またはブラウザ内のimport_stitch_imageで直接読み込む。画像URLによる読込は提供しない。サーバーへ画像を送らない。ブラウザ操作がない場合はその制約を報告する。環境名だけで利用可能と判断しない。リンクは操作能力を追加しない。
Within-browser Studio/PRO transfers must remain in the same origin and use a unique per-workspace channel. Never fall back to a shared channel. Existing work must be preserved before import.
生成した画像ファイルを現在のホストが正式に提供するブラウザのファイル選択で読み込む。ファイル転送が使えない場合は制約を報告する。ファイルはブラウザ内で生成し、WebMCPの分割取得でホストへ渡せる。チャット添付と端末保存は別途確認する。

Before a modifying browser tool call, read get_workspace_status in the selected tab and include expectedWorkspaceId and expectedPageInstanceId. Re-read after navigation. Workspace identifiers stay in the browser route and never go to this MCP server.

## Visible operation checks / 画面を見ながら操作確認
制作開始時の表示希望は既存の指示を優先し、通常の制作判断を任された場合は不要な質問をせず進める。毎工程で許可を取り直さない。現在のホストが正式に提供する画面表示・スクリーンショット機能がある場合だけ使用する。表示できない場合は先に説明し、右側の画面が見えていると主張しない。操作前にユーザー指定のStudio番号と実際に取得した画面の番号を照合し、不一致なら変更操作を止める。画像読み込み後、領域・背景設定後、刺繍生成後、保存前に画面を確認し、主要な結果を提示してユーザーも確認できるようにする。画面クリックとWebMCP操作を区別して報告する。WebMCPランプの青は受付準備済み、緑は受信・実行中、赤はエラー、灰は利用不可。操作履歴は本体の「ステータス」に直近100件を表示し、ブラウザのStudio別セッション保存のみ。画像・操作引数・結果データは記録しない。
Ask once at the start whether the user wants to follow the visible operation screen. Use only the current host’s supported display/screenshot capability; never assume the user’s right-side panel is accessible. Match the requested Studio against the actual target before any mutation. Inspect and show meaningful checkpoints after image import, region/background setup and stitch generation, and before export. Distinguish UI clicks from WebMCP calls; readiness does not prove communication.


# 利用環境と接続判断

環境名と能力を分けて判断する。ChatGPTをWebで開いていることと、作業ブラウザがWebMCPを提供することは別である。固定の対応表で成功を断定しない。

| 利用環境 | 確認すること | 選択する経路 |
| --- | --- | --- |
| デスクトップ版 | 今の会話にブラウザ・コンピューター操作があるか。対象タブでWebMCPが提供されるか | 公開済みWebMCPが依頼を満たせば優先。なければ許可された画面操作 |
| GPT Web版のWork | Workの作業ブラウザが利用できるか。ページ初期化後にWebMCP一覧が取れるか | 実際の能力に従いWebMCPまたは画面操作。Web版という理由で不可と決めつけない |
| GPT Web版の通常チャット | 操作ツールがこの会話にあるか | なければ制作操作は実行できないと説明。作業用会話での実行またはユーザーの手動手順を示す |
| ブラウザ拡張経由 | 拡張のブラウザ操作が公開され、対象タブを選べるか。ログイン状態や接続範囲が何か | 公開APIの範囲で操作。拡張の存在だけでWebMCP対応とみなさない |

## 実行前の手順

1. 提供されているブラウザAPIの説明を読む。ユーザーがブラウザ・タブを指定したらその選択規則を守る。ローカルブラウザ指定や拡張指定がないのにユーザーのブラウザへ切り替えない。
2. Jiminyを開く。既存タブがあれば再利用し、進行中のデータを再読み込みで失わない。
3. ページ初期化を待ち、現在の画像・領域・縫い・保存状態を確認する。
4. WebMCP能力が実際に広告されていれば、説明に沿って操作一覧を取得する。現在の一覧にあるツールだけ呼ぶ。get_workspace_status、get_studio_guide、get_studio_stateは一覧に存在する場合だけ読む。
5. 結果から対象領域、設定、成功状態を確認する。専用PRO画面の操作がStudioのツールにあると推定しない。別画面ではその画面の能力を確認する。
6. 一覧取得が modelContext unavailable で失敗した場合は「このタブでWebMCP一覧取得に失敗」と記録する。サイト全体、GPT Web全体、デスクトップ全体が非対応だとは言わない。通常クリックが動いてもWebMCP成功とは言わない。
7. 許可された画面操作があればそれで続ける。プラグインの失敗から切り替える場合は、その環境のフォールバック規則に従う。WebMCP実行にページ外の送信・権限拡張が含まれるなら別途その認可を確認する。

## 状態表示の区別

「AI操作: 30機能を準備済み」などサイト表示はサイト側の準備を表す。Workの一覧取得・呼び出し・結果反映の証拠にはしない。has_mcpやSitesの所有者エラーはサーバーMCPの情報であり、ブラウザWebMCPと混同しない。

ファイルアップロード、ダウンロード、スクリーンショットは現在のブラウザ説明の共有フォルダと保存方法に従う。ローカルのパスをそのままブラウザ側へ渡さない。

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
