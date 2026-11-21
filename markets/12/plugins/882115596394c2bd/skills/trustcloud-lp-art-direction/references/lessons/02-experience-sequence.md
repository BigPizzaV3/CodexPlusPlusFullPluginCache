> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Case lesson 02 — 複数体験を一日の物語にする

## 問題と入力

見学、対話、講座、移動など複数の体験を含むイベント。写真と情報量は多いが、単純なカード列では参加価値と時間の流れが分断される。課題は、写真を証拠として保ちつつ「この順に体験すると疑問がどう解けるか」を示すことだった。

## 判断

情報を施設別ではなく意思決定の変化で並べた。最初に現物を見る、次に経験者や専門家へ聞く、最後に学びを整理する。時刻表は logistics ではなく体験の予告として写真と組ませた。この考え方はツアー、カンファレンス、学校説明会、採用イベント、体験会へ移せる。

## ブロック選択

- `media`: 一人の話や一つの現場など、単独写真が主張を担う箇所。実例のフィールドは `title`, `body`, `imageUrl`, `imageAlt`, `presentation: "editorial"`, `reverse`, `eyebrow` など。
- `process`: 画像を必要としない短い標準手順なら `steps[].title`, `steps[].text` を使う。
- `free-design`: 時刻と写真が対応する工程、紙面風の講座要点など、情報の空間関係が意味を持つ箇所。`texts[]` と `images[]` のIDをHTMLへ束縛する。
- `faq` と `calendar`: 費用、所要時間、持ち物などの障壁と予約操作はネイティブで扱う。事実がない質問を埋め草として作らない。

## 実装技法（短い抜粋）

```html
<section data-lp-role="experience">
  <div class="sequence-copy">
    <p data-lp-text="sequence-eyebrow"></p><h2 data-lp-text="sequence-heading"></h2>
    <ol>
      <li><span class="time" data-lp-text="step-a-time"></span><div><h3 data-lp-text="step-a-title"></h3><p data-lp-text="step-a-body"></p></div></li>
      <li><span class="time" data-lp-text="step-b-time"></span><div><h3 data-lp-text="step-b-title"></h3><p data-lp-text="step-b-body"></p></div></li>
    </ol>
  </div>
  <figure><img data-lp-image="sequence-proof"><figcaption data-lp-text="sequence-caption"></figcaption></figure>
</section>
```

```css
section{display:grid;grid-template-columns:.62fr 1fr;gap:2rem}.time{font-variant-numeric:tabular-nums}
li{display:grid;grid-template-columns:5rem 1fr}figure img{width:100%;height:100%;object-fit:cover}
@media(max-width:640px){section{grid-template-columns:1fr}li{grid-template-columns:4rem 1fr}figure img{height:auto;aspect-ratio:8/5}}
```

装飾写真と情報写真を区別する。キャプションは `figcaption` と `data-lp-text` で編集可能にし、画像に説明を焼き込まない。工程の視覚方針がある場合は、全素材を小さなgalleryへ均して終えず、工程の意味を担う場面・細部・手元などを本文と対応する大きさで見せる。画像数のノルマは設けず、画像なし指定では短い動詞・番号・余白の編集で成立させる。

## レスポンシブ規則

- PCは工程と写真を左右で対応させる。時刻列の幅を固定して視線を揃える。
- モバイルは工程を先に、対応写真を後に置く。横長写真の人物や対象が切れない `object-position` を画像ごとに決める。
- 紙面風の背景素材を使う場合、PC用とモバイル用を必要に応じて分ける。PC素材の文字領域を縮小して流用しない。

## 後半の作り込み

「見どころ一覧」で止めず、学びを持ち帰る章と、参加当日の流れ、最後の未使用写真まで役割を分けた。時系列説明は一箇所へ集約し、前章では体験の意味を語る。CTAは途中の節目と終盤に置けるが、すべて `data-lp-action="booking"` で同じネイティブ予約地点へ導く。

## 使わない条件・失敗例

- 単一講座や短時間相談で工程が意思決定に不要なら、無理に時系列を作らず `media` と `specs` で十分。
- 同一写真を各工程へ再掲しない。実際の順番が不明なら時刻を創作しない。
- 人物の発言を提供資料なしで testimonials 化しない。写真に写る人物の役割も推測しない。
- 同じ内容を体験紹介と時刻表で二重に説明しない。

## 観察された弱点

初期版には説明重複、キャプションの離脱、PC末尾の孤立、狭幅での語中改行があった。装飾的な手書き注記は狭幅で省略されており、情報の本体には使えない。写真が豊富なケースほど、出典と被写体の内容を変えない運用が必要である。
