> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Case lesson 05 — 選択肢を比較し、相談する理由を作る

## 問題と入力

一つの完成品を売るのではなく、配置、用途、予算など複数条件を一緒に考える相談型イベント。入力には模型や図解がある。課題は、選択肢を商品カードのように誤認させず、比較から次の相談項目へ導くことだった。

## 判断

最初に全体の考え方を示し、次に3案を同じ視点で比較し、その後に総額や準備状況へ視野を広げた。画像の差を文章で言い換えるのではなく、各案で変わる生活・運用・意思決定を説明する。この原則はプラン比較、サービス導入、旅行、教育コース、業務改善相談にも適用できる。

## ブロック選択

- `comparison`: 左右二案と行単位の差が中心なら `leftTitle`, `rightTitle`, `rows[]`, `caption` を使う。
- `specs` / `metrics`: 根拠のある条件・数値には `items[].key`, `items[].value` または `items[].label`, `items[].value` を使う。
- `free-design`: 3つの図版を同じ尺度で見せ、見出しと説明を図版ごとに結びつける場合。`html`, `css`, `texts[]`, `images[]` で構成する。
- `faq`, `calendar`: 個別相談への障壁と予約操作をネイティブに残す。地図は住所が提供された場合だけ `map` を使う。

## 実装技法（短い抜粋）

```html
<section data-lp-role="experience">
  <header><h2 data-lp-text="options-heading"></h2><p data-lp-text="options-lede"></p></header>
  <div class="options">
    <article><img data-lp-image="option-a-visual"><h3 data-lp-text="option-a-title"></h3><p data-lp-text="option-a-body"></p></article>
    <article><img data-lp-image="option-b-visual"><h3 data-lp-text="option-b-title"></h3><p data-lp-text="option-b-body"></p></article>
    <article><img data-lp-image="option-c-visual"><h3 data-lp-text="option-c-title"></h3><p data-lp-text="option-c-body"></p></article>
  </div>
</section>
```

```css
.options{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}.options article{text-align:center;padding:0 1rem}
.options article+article{border-left:1px solid currentColor}.options img{width:100%;aspect-ratio:1.15/1;object-fit:cover}
@media(max-width:700px){.options{grid-template-columns:1fr}.options article+article{border-left:0;border-top:1px solid currentColor;padding-top:1.5rem}}
```

比較のあとに、図解と実写の役割を分ける。図解は関係を示し、実写は相談行為や使用場面の具体性を示す。いずれも `images[].id`, `url`, `alt`, `role` とHTMLの `data-lp-image` を一致させる。

## レスポンシブ規則

- PCは三案を同時比較できるよう、画像比率、見出し位置、本文量を揃える。列幅を保つために本文を極端に縮小しない。
- タブレットで助詞や句読点だけが次行へ孤立したら、列内paddingと文字量を減らす。`white-space` 固定で隠さない。
- モバイルは一案ずつ縦に並べ、境界線を横へ変更する。各案が画像→名称→意味の順になるようDOMを組む。

## 後半の作り込み

比較後は「全体コスト」「手元に候補がある／ない」など別軸の判断へ進める。最後に同じ模型を再掲せず、相談で持ち帰れる判断や次の行動をタイポグラフィーで締める。CTAは `data-lp-action="booking"` を使い、ネイティブ `calendar` へ接続する。

## 使わない条件・失敗例

- 選択肢の条件が資料にない場合、架空の三案を作らない。一つの体験なら `media` が適切。
- 異なる模型や例を「同一対象の変更前後」と断定しない。
- 根拠のない価格、面積、効果を比較軸にしない。図の小さなラベルだけに重要情報を置かない。
- すべての案件を三列カードへ押し込めない。選択肢が二つなら `comparison`、連続量なら `metrics` や説明図を検討する。

## 観察された弱点

初期版では異なる模型の関係を過剰に示し、終盤で同じ模型を再利用していた。最終版でも模型の台座形状と参考ビジュアルは完全一致せず、図解の小ラベルはモバイルで補助説明が必要だった。比較の美しさより、同じ尺度で比較できる正確さを優先する。
