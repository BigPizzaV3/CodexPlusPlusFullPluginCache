# 案件データと納品物

この形式は担当AIが作成する。利用者へJSONの編集やコマンド実行を求めない。生成した実素材と元台本を一つの案件ディレクトリへ置き、case.jsonからの相対パスで参照する。絶対パス、外部URL、上位ディレクトリ、シンボリックリンクは素材参照に使わない。素材は権限のある原本からコピーする。

```json
{
  "case_id": "video-001",
  "title": "動画の題名",
  "doctor_id": "doctor-demo",
  "source": {"path": "source.md", "sha256": "元原稿のSHA-256", "version": "v1"},
  "profile": {"id": "doctor-demo", "version": "v1", "design_version": "v1"},
  "design": {"background": "#f6f8fb", "ink": "#172b4d", "accent": "#176b87"},
  "scenes": [
    {
      "id": "scene-01",
      "purpose": "二つの状態の違いを同じ尺度で比較する",
      "quote": "原稿内で一意に見つかる発話",
      "end_cue": "次の話題へ移る直前",
      "duration": "発話に合わせ約5秒。編集時に調整",
      "placement": "正方形でインサート。未撮影なので左右は撮影後に確認",
      "selected": "diagram",
      "options": [
        {"id": "diagram", "title": "要点の図解", "type": "図解", "kind": "diagram", "mode": "square", "status": "pending", "reason": "関係を一目で示せる", "description": "本人の配色に合わせた比較図。生成・目視後にreadyへ更新する", "files": []},
        {"id": "animation", "title": "動く比較図", "type": "図解動画", "kind": "video", "mode": "motion", "status": "proposal", "reason": "変化の順序を見せられる", "description": "選択後に制作する16:9の動画", "files": []}
      ]
    }
  ],
  "digest": [{"quote": "ダイジェストで抜く原稿内の一意な発話", "display": "画面用の表示文。必要なら??で伏せる", "status": "proposed"}],
  "notes": ["今回の編集で必要な補足だけ"]
}
```

サンプルの文言やダミーSHAをそのまま実行しない。quoteは元台本そのものと照合する。

## 項目

- `case_id`：案件の固定ID。選択変更時にも保持。`doctor_id`と`profile.id`を一致させ、本人設定・デザインの版を固定する。
- `source.sha256`：保存した元原稿のバイト列から算出。本文改訂時は再計算し、全quoteを照合し直す。読み上げ本文は素材指示を差し込むために勝手に改稿しない。
- `design`：納品HTMLの配色。生成素材の画風やフォントは本人設定を制作時に別途適用する。これだけで既成画像の色は変わらない。
- `scenes[].quote`：元原稿内で一意な引用。引用が複数になる時は前後を含めて一意にする。素材の開始位置として使用し、終了合図・秒数目安・配置は編集者に読める自然文で記す。
- `selected`：採用option ID。未選択はnullで未完成。明示的な素材なしは`selected: null, omit: true`に、`omission_reason`と`omission_basis: "user"`または`"not_applicable"`を付ける。本人の指示またはその台本に不要な具体的理由を記録し、未取得素材を省略に変えて隠さない。
- `purpose`：各場面が視聴者へ伝える目的。空欄不可。単なる素材の種類名ではなく、何を理解・実感してもらうかを書く。
- `kind`：各optionの表現種類。`illustration`, `photo`, `diagram`, `chart`, `text_card`, `video`, `brand_asset`のいずれか。日本語の`type`は表示用名称として保持。`video`は`mode: "motion"`と実動画を要する。
- `mode`：`square`＝1:1インサート、`full`＝16:9全画面静止画、`motion`＝16:9全画面動画、`overlay`＝本人提供画像などの元比率を保つインサート。
- `status`：`ready`は実ファイルを目視確認し、下記productionの制作根拠・ファイルハッシュ付きレビューを記録済み、`proposal`は未制作の別案、`pending`は採用済みだが作成中/不足あり。状態を装うためダミー画像や開始フレームを動画として置かない。
- `files`：必要な実素材を表示順に並べる。複数の静止画像はすべてHTML・素材一覧・全文プレビューに表示される。各画像のファイル名と対応発話・切替順はdescriptionへ記し、同じ場面の複数画像を一枚として納品点数に数えない。`poster`は動画用の任意の静止プレビュー。未制作案は画像を持たなくてもよい。選択肢に原本と別サイズ等を含める際は用途をdescriptionへ記載。
- `digest`：指定があればapproved、自動提案ならproposed。quoteとdisplayは区別し、本文はquoteの原文を太赤字にする。空配列ならダイジェストを追加しない。
- `recording`：任意。`file`へ撮影原本の相対パス。実測できた場合だけ`duration_seconds`, `width`, `height`, `fps`, `has_audio`を記録。未撮影をエラーにしない。
- `prompter_path`：依頼・提供済みのプロンプター稿の任意相対パス。氏名・プロフィール全文などをnotesへ無目的に入れない。

## ビルドと確認

```bash
python3 scripts/build_handoff.py case.json --output delivery --zip editor-handoff.zip --require-complete
```

出力先は案件用の新しいフォルダとZIPを指定する。既存の納品物を無断で上書きせず、改訂時は版別の出力先を使う。ファイルが作れない環境ではHTML/ZIP完成と報告しない。

スクリプトは実素材の生成、参考動画の分析、台本の医学的検証を行わない。機械検査通過はこれらの目視・内容検査の代替にならない。`quality-report.json`の`passed`／`needs_review`と実物レビューを読み、未解決を修正する。完成納品の検査では必ず`--require-complete`を付ける。部分完成では下書きを保存して終了コード3を返すため、ファイルが出力されたことだけで完成としない。途中確認用の下書きだけはこのフラグを省ける。確認後に納品ファイルへの実リンクを示す。

このビルドは閲覧用の`preview.html`と`preview-report.json`も作る。[確認ページと修正](review-page.md) に従ってSitesの本人向け限定ページへ配信し、実際に返ったURLを確認リンクとして渡す。自己完結HTMLの容量を超える場合は`script.html`と参照素材をまとめて配信し、本文や全素材へのアクセスを保つ。Sitesの保存・配信はビルダーとは別の工程であり、生成しただけでは配信済みではない。最終確認のために利用者へ解凍やHTML編集を要求しない。

会話内表示を利用者が明示した場合だけ、caseへ`"preview": {"inline_requested": true}`を指定する。既定はfalseで、`preview-parts/part-NNN.html`の小さな分割表示を標準で生成・提示しない。明示依頼で分割する場合も全文・文献・全素材を保ち、その表示環境の容量制限に合わせる。原寸ZIPと閲覧用コピーは分けて保持する。

## 完成判定用の記録

以下は担当AIが実行結果から記録する。利用者へ記入を求めず、サンプルの「確認済み」を実績としてコピーしない。原稿・素材を変更したらハッシュを更新し、影響するレビューをやり直す。

各採用ready optionの`production`。医学説明の比較セットでは未採用候補も全点に必要：

```json
{
  "method": "image_generation",
  "tool": "実際に実行した画像生成機能名",
  "evidence": "実行結果と取得した素材を識別できる記録。認証情報や期限付きURLは入れない",
  "review": {
    "status": "passed",
    "evidence": "実物を開き、依頼した場面・文字・比率・身体表現を確認した内容",
    "files_sha256": {"assets/illustration.png": "確認した実ファイルのSHA-256"}
  }
}
```

`method`は`image_generation`, `video_generation`, `layout`, `user_provided`, `motion_graphics`。イラスト・写真を`layout`だけで作成済みとはしない。図形レイアウトは比較図等へ使う。動画は実際に変化する映像ファイルであることを確認する。`review.status`は`passed`または`needs_revision`。files_sha256にはそのoptionの全filesを入力相対パスで記録する。

caseの`quality`：

```json
{
  "version": 1,
  "source_sha256": "実際に確認したsource.sha256と同じ値",
  "capabilities": {
    "image_generation": {"status": "not_tested", "tool": "", "evidence": "必要な最初の素材で確認する"},
    "video_generation": {"status": "not_tested", "tool": "", "evidence": "必要な最初の素材で確認する"},
    "file_output": {"status": "not_tested", "tool": "", "evidence": "実ファイル作成と読み戻しで確認する"}
  },
  "profile_assets": [
    {"role": "intro", "status": "missing", "scene_ids": [], "evidence": "本人設定と実原本の参照を確認する"},
    {"role": "ending", "status": "missing", "scene_ids": [], "evidence": "本人設定と実原本の参照を確認する"},
    {"role": "gift", "status": "missing", "scene_ids": [], "evidence": "今回のCTAとの対応と実原本を確認する"}
  ],
  "requirements": {"required_kinds": ["illustration", "diagram", "video"], "required_modes": ["square", "motion"], "required_profile_roles": []},
  "reviews": {
    "material_mix": {"status": "needs_revision", "evidence": "制作前の初期状態。場面の目的と採用素材を別の視点でレビューする"},
    "visual": {"status": "needs_revision", "evidence": "全採用素材を実物で確認する"},
    "editor_ready": {"status": "needs_revision", "evidence": "全文・挿入位置・編集指示・実ファイルを確認する"}
  },
  "host_checks": {
    "hosted": {"status": "not_run", "evidence": "限定アクセスと配信成功は未確認"},
    "browser": {"status": "not_run", "evidence": "未実施"},
    "chat_preview": {"status": "not_applicable", "evidence": "限定確認ページを使い、会話内表示は依頼されていない"}
  }
}
```

- capabilitiesは`verified`, `unavailable`, `not_needed`, `not_tested`。verifiedには実行したツールと出力の根拠、unavailableには確認できた制約、not_neededには今回不要な理由が必要。未確認をunavailableへ書き換えない。
- profile_assetsは必ずintro/ending/giftの3役を記録し、`verified`, `not_applicable`, `waived`, `missing`を使う。verifiedは実原本と対応scene_ids、waivedは本人が省略・代替を指定した発言、not_applicableは台本に該当役割がない等の具体的根拠を残す。必要な役割をrequired_profile_rolesへ入れた場合はverifiedまたは本人のwaiverが必要。短い技術試験等で3役とも原稿にない場合に限り、各役割の理由を付けて全てnot_applicableにできる。
- requirementsはこの台本に適した採用計画と本人指定から決める。サンプルの種類を全案件へ強制せず、不足が出た後で要件を消して完成にしない。静止人物イラストで伝わる姿勢にvideo/motionを、正方形の情報素材にfullを機械的に要求しない。利用者が動画から静止画等への変更を明示した場合は、発言と変更理由を記録してrequirementsも更新する。採用済みreadyの実物で満たす。
- reviewsは`passed`または`needs_revision`。material_mixには各場面の目的、偏り、動画を使う／使わない理由を具体的に記録する。採用素材が5点以上で図解・グラフ・文字カードが80%以上の時は偏り確認が働く。妥当なら`diagram_heavy_reason`へ台本上の理由と再点検結果を書く。これは他種の枚数を無理に埋めるノルマではない。
- host_checksのhostedとbrowserは`passed`, `not_run`, `failed`。hostedは実際の限定アクセス確認と配信成功をevidenceへ記録し、passed時には実URLをurl、限定配信の確認結果をvisibility: privateとして残す。browserはページ表示・再生・選択・書き出しの実操作を記録する。配信成功や静的検査だけでbrowserをpassedにしない。Siteのproject_id・保存版ID・配信ID・配信元SHAは制作メモにも保持し、URLを作り直さない。
- chat_previewは上記状態に加えて`not_applicable`を使える。標準の限定確認ページでは会話内表示は対象外とし、不要な分割確認を完了条件にしない。会話内表示を明示依頼された場合はnot_applicableにせず、対象環境で確認する。旧案件の検査記録を新しい限定配信のpassedへ流用しない。

初回は実物レビューまで記録して下書きをビルドし、表示・操作を確認した結果をqualityへ追記して改訂出力を作る。原稿や実素材が変わっていなければ素材自体の生成を繰り返す必要はない。機械検査が通っても対象ホストがnot_runなら、その未検証範囲を完成報告に残す。

ビルダーのcompleteは素材と台本パッケージの判定であり、Sitesへの配信完了ではない。hostedがnot_runでも配信用ファイルは作れるが、最終確認リンクを納品済みと報告する前には実際の限定アクセス確認と配信成功を記録する。公開結果を得た後の管理記録更新だけを目的に、同じ内容を再配信し続けない。

## 選択変更の戻し方

HTMLで別案・素材なし・修正メモを選び、依頼文またはJSONを保存して元のチャットへ戻す。HTML内で選択しても実素材や納品ZIPは変わらず、変更待ちとして表示する。

受領した選択データのcase_id・sourceのSHA・scene ID・option IDを現行案件と照合。不明なIDや古い原稿は適用せず、原稿の再照合へ戻る。相対ファイル参照を書き換える入力として使わない。採用を変更した場面だけ更新する。生成済みの候補なら既存ファイルと有効なレビューを再利用し、新しいHTMLとZIPおよび同じ確認URLへ反映する。内容の修正や未制作候補の選択がある場合だけ、該当素材を実制作・再確認する。個人に恒常的な好みとして反映する指示ならdoctor-profileも更新し、今回だけの修正を全員共通スキルへ混ぜない。利用者が汎用ルール化や見本としての掲載を明示した場合は、再利用する制作原則とその案件だけの個人情報・配色を分けて反映する。


## 医学説明の3〜5候補（任意の場面拡張）

[医学説明の3〜5案](../../asset-planning/references/medical-variants.md)に該当するsceneへ、次のmedical_variantsを付ける。対象外の既存場面には不要。

```json
{
  "medical_variants": {
    "target_count": 3,
    "option_ids": ["anatomical", "cute", "schematic"],
    "reason": "同じ部位の説明を、解剖関係・親しみやすさ・情報量の違いから比較する"
  }
}
```

- target_countは3〜5の整数。option_idsはその数と一致する重複のない実option ID。scene.optionsへ同じIDの候補を作る。初期selectedはセット内の推奨IDとする。完成済みの動画など、同じsceneにあるセット外の候補への選択変更も可能。その場合も比較セット全案の完成条件は維持し、未制作の動画案で静止画セットの候補数を埋めない。
- 候補数と理由は制作前に記録する。生成に失敗した後でtarget_countやoption_idsを縮めて完成にしない。有効な明示的場面省略は既存のomit形式に従い、失敗を隠す省略はしない。
- 全候補のfilesにそれぞれ独立した実画像を入れ、全案をreadyにして完成とする。確認対象は本編の採用だけではない。同じ画像の別名コピーは別案と認めない。複数画像を順に見せる一案は複数filesのまま一案として数える。
- anatomicalとcuteの2スタイルを必須とし、通常の3案目はschematic。4〜5案目は説明目的に合うcontextやmetaphor等。各案は静止画像の候補であり、3〜5本の動画生成を意味しない。

各対象optionには、通常のkind・mode・status・files・productionに加え、次のmedical_visualを付ける。以下は未確認の記入例であり、サンプルをpassedの実績としてコピーしない。

```json
{
  "medical_visual": {
    "style": "anatomical",
    "explanation": "描く部位と関係、説明のため省いた細部を具体的に記す",
    "review": {
      "status": "needs_revision",
      "evidence": "実画像と参照を確認してから結果を記録する",
      "references": []
    }
  }
}
```

styleはanatomical、cute、schematic、context、metaphor。explanationは空欄にせず、候補の見せ方と適用範囲を書く。medical_visual.reviewは実物を確認してからstatus: passedと具体的なevidenceを記録し、解剖案のreferencesには実際に確認した資料の題名・所在・照合した関係を1件以上入れる。他の案でも参照した資料は記録する。かわいい案で意味の誤りを許容しない。

全候補に通常のproductionと、全filesのSHA-256に対応したproduction.reviewも必要。medical_visualへ重複したハッシュ欄を作らず、画像変更時は両方の内容確認をやり直す。statusだけ、汎用的な「確認済み」だけで実際の確認を代替しない。

ビルダーは医学説明の比較欄を開いた状態で表示し、各案の実画像・表現ラベル・説明範囲・確認記録と、候補の準備数を示す。採用素材と比較用の別案のファイル数を分け、ZIPには全候補を保持する。品質検査は未採用候補の画像、記録、ファイル同一性も検査するが、解剖の正しさや参照資料の内容を自動認定するものではない。本人向け限定確認ページでも同じ全候補が見えることを確認する。
