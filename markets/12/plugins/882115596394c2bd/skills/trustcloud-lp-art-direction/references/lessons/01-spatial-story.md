> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Case lesson 01 — 空間を「歩く順序」で語る

## 問題と入力

静かな写真を主役にした見学型イベント。入力には全景、素材の接写、着座時の眺めがあるが、性能値や比較表は少ない。課題は、写真集にせず「訪れると何が分かるか」を後半まで持続させることだった。

## 判断

ページを物件紹介ではなく、視線と身体の移動として組み立てた。全景で約束を示し、動線、素材、座ったときの感覚へ寄る。各写真は、見えている事実、来場者が自分の目的・利用場面（住宅なら暮らし）と比べる観点、現地で確かめる問いへつなげ、大きな写真の間に同じ意味の画像や説明を繰り返さない。入力にない性能や保証を、質問形式に変えて補わない。これは店舗、宿泊施設、展示、工場見学にも使える。重要なのは空間の種類ではなく、来場者が「どこで・何を・どう確かめるか」の順序である。

## ブロック選択

- `media`: 1枚の証拠写真と説明で成立する導入。実例では `content.title`, `body`, `imageUrl`, `imageAlt`, `presentation: "editorial"`, `reverse`, `borderRadius`, `titleAlign`, `bodyAlign`, `eyebrow` を使用した。
- `gallery`: 複数画像が同じ問いを別角度から補強するとき。`images[]`, `columns`, `presentation: "editorial"` を使う。
- `free-design`: 写真、観察項目、素材の接写を一つの編集面として関係づける場合。`content.title`, `html`, `css`, `texts[]`, `images[]` を持ち、各 text は `id`, `label`, `value`, `role`、image は `id`, `url`, `alt`, `role` で束縛する。
- `section` / `faq` / `calendar`: 見出し、質問、予約操作はネイティブ機能に残す。`calendar.content.presentation: "stacked"` とし、IDは予約導線のアンカーにする。

## 実装技法（短い抜粋）

完成例の構成・コードも、案件に合わせて自由に利用できる。

```html
<section data-lp-role="experience">
  <div class="feature">
    <img data-lp-image="primary-scene">
    <div><h2 data-lp-text="experience-heading"></h2><p data-lp-text="experience-lede"></p></div>
  </div>
  <div class="observations">
    <article><h3 data-lp-text="observation-a"></h3><p data-lp-text="observation-a-body"></p></article>
    <article><h3 data-lp-text="observation-b"></h3><p data-lp-text="observation-b-body"></p></article>
  </div>
</section>
```

```css
.feature{position:relative;min-height:34rem}.feature img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.observations{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:600px){.feature{display:flex;flex-direction:column;min-height:0}.feature img{position:relative;height:17rem}.observations{grid-template-columns:1fr}}
```

## レスポンシブ規則

- PCでは写真とコピーを同時に見せるが、文字を写真の重要部分へ重ねない。最大幅や `object-position` は画像の焦点から決める。
- モバイルでは絶対配置を解除し、画像→見出し→説明の読順にする。2〜3列の観察項目は1列にし、境界線を横線へ変える。
- 意図的改行は語句単位。`white-space: pre-line` を狭幅だけに使い、320pxでも語中を割らない。

## 後半の作り込み

後半は、素材の接写や空間の関係を観察可能な事実として示し、来場者が自分の目的・利用場面（住宅なら暮らし）と比べる観点、現地で確かめる問いへ具体度を上げる。例えば見えている中庭と居室のつながりから、普段の過ごし方との相性を現地で確かめる問いへ進める。提供された時系列や参加手順がないなら、見どころをprocessの番号へ再掲せず、新しい判断材料がない短い案内は既存の安心・予約案内へ統合する。最後の自由デザイン内のCTAには `data-lp-action="booking"` を付け、操作先はネイティブ `calendar` に任せる。写真を足すたびに、その画像だけが答える問いを一つ書けないなら削る。

## 使わない条件・失敗例

- 比較条件や数値が意思決定の中心なら、雰囲気の連続写真だけでは弱い。`specs`, `metrics`, `comparison` を優先する。
- 関係のない素材接写、同じ全景の再利用、長文を画像へ焼き込むことは避ける。
- 画像上の長文を縮小してモバイル対応としない。写真の端をぼかすだけで文字領域を作ったつもりにしない。

## 観察された弱点

初期案では写真の重複、説明の抽象度、白背景と写真の硬い境界が残った。最終版でも画像生成した素材が同一空間に見えるかは個別確認が必要である。この手法は実在性を保証しないため、現物写真が証拠になる案件では生成画像へ置換しない。
