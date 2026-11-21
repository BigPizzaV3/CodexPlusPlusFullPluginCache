> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Case lesson 04 — 雰囲気を保ちながら操作面へ着地させる

## 問題と入力

暗所、音、香り、照明など、通常の昼間写真では価値が伝わらない体験型イベント。課題は、深い没入感を作りながら、後半のFAQと予約を暗く読みにくい画面に閉じ込めないことだった。

## 判断

前半は暗色面で「全景→光の当たり方→素材→到着時の感覚」と体験を深め、FAQの前で明色面へ一度だけ切り替えた。色の転換を章の意味に合わせ、交互の暗明装飾にはしない。コンサート、ナイトツアー、飲食、スパ、展示などにも使える。

## ブロック選択

- `free-design`: 暗色面、複数写真、短い観察ラベル、背景写真上のCTAを一体化する箇所。`title`, `html`, `css`, `texts[]`, `images[]` を使用。
- `gallery` / `media`: 標準的な画像列や一つの説明で十分ならネイティブを優先する。
- `faq`: 操作性と可読性が重要なためネイティブ `items[].q`, `items[].a` を使い、明色面に置く。
- `calendar`: `title`, `note`, `presentation: "stacked"` を使う。雰囲気用HTMLで予約UIを模造しない。

## 実装技法（短い抜粋）

```html
<section class="arrival" data-lp-role="experience">
  <img class="backdrop" data-lp-image="arrival-scene">
  <div class="copy">
    <h2 data-lp-text="arrival-heading"></h2><p data-lp-text="arrival-body"></p>
    <button data-lp-action="booking"><span data-lp-text="arrival-cta"></span><img aria-hidden="true" data-lp-image="cta-icon"></button>
  </div>
</section>
```

```css
.arrival{position:relative;display:grid;grid-template-columns:62% 38%;min-height:46vw;background:#101a22;color:#f7f2e7}
.backdrop{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.copy{position:relative;grid-column:2;align-self:center}
@media(max-width:700px){.arrival{display:flex;flex-direction:column;min-height:0}.backdrop{position:relative;aspect-ratio:4/3}.copy{padding:2rem 1.5rem}}
```

装飾アイコンは `images[]` で管理し、意味を持たない場合は `aria-hidden="true"`。背景写真にも `images[].alt` を設定するが、説明文と異なる内容を推測して書かない。

## レスポンシブ規則

- PCでは画像の暗い余白へ短いコピーを置く。コントラストを実画像で確認し、半透明の黒面に頼りすぎない。
- モバイルでは背景の絶対配置を解除し、画像と文章を分ける。CTAは十分なタップ高と横幅を確保する。
- 暗色の本文を延々続けない。操作の多いFAQ・予約は明色へ切り替え、フォーカス輪郭も見える色にする。

## 後半の作り込み

後半でも雰囲気写真を追加するだけでなく、「座った視点」「素材の反射」「到着動線」のように観察軸を変える。最後の没入章で予約動機を言語化し、FAQ→開催案内→カレンダーは明色で一続きにする。色の切り替えは一回に抑えると、情緒から行動への遷移として読める。

## 使わない条件・失敗例

- 日中開催、事務的な説明、数値比較が中心なら暗色演出を先に決めない。
- 暗い写真へ細い小文字を重ねない。色だけで章や状態を識別させない。
- ページ全体を暗くし、FAQやカレンダーまで同じ演出へ巻き込まない。
- 雰囲気のための無関係な英語ラベルは原則不要。使うなら情報を妨げない補助表現に限る。

## 観察された弱点

初期版では暗色と明色の往復、FAQの位置、見出しの四行化が問題になった。最終版のアイコンは利用可能素材の近似で、完全に固有の造形ではない。暗所写真はモニター差で黒つぶれしやすく、保存後のPC・タブレット・モバイル画像で階調を確認する必要がある。
