> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Case lesson 03 — 見えない相談価値をイラストで可視化する

## 問題と入力

相談・教育型イベントでは、完成物の写真だけでは参加後の変化が伝わりにくい。入力は複数の悩みと相談テーマで、実写の証拠より心理的な敷居を下げることが重要だった。

## 判断

「好きな状態を見つける→優先順位を整理する→次の行動を決める」という認知の変化を、同じ画風・人物世界の連作で描いた。イラストは飾りではなく、抽象語を具体的な場面へ翻訳する図解である。この原則は資産相談、学習支援、医療説明、採用面談、SaaS導入相談にも応用できる。

## ブロック選択

- `free-design`: 連作イラストと短い動詞を一体化し、順序そのものを理解させる場合。`content.html`, `css`, `texts[]`, `images[]` を使う。
- `media`: 相談風景と一つの説明なら、`title`, `body`, `imageUrl`, `imageAlt`, `presentation: "editorial"` で十分。
- `cardgrid`: 互いに独立した3〜4テーマで、図解の連続性を必要としない場合。`cards[].title`, `cards[].text`, `columns` を使う。
- `process`: 短い実手順なら使えるが、番号badgeは自動表示されるためtitleへ`01`や`STEP 1`を書かない。PC3列・タブレット2列・モバイル1列固定なので、孤立する最終行が構図を崩す場合は無理に使わない。
- `faq`, `calendar`: 質問回答と予約はネイティブに保つ。根拠のない安心保証は書かない。

画像なしを利用者が選んだ案件では、イラストがこの教材の中心でも、画像枠や架空の図解を作らない。短い動詞、番号、罫線、色面、余白、文字サイズの差で認知の変化を表す。画像やイラストを使う方向が選ばれている場合は、3段階の順序を小さなgalleryへ押し込めず、各場面の観察可能な行為・素材・変化を本文と対応する面積で一体化する。これは固定枚数の要求ではなく、視覚方針と情報のcoverageを確認するための基準である。3段階の順序をPCとモバイルで異なる列数や重なりとして見せる必要があり、native `process` の固定列では密度や主従が成立しない場合だけ、その一連の説明を選択的に`free-design`へする。

## 実装技法（短い抜粋）

```html
<section data-lp-role="experience">
  <h2 data-lp-text="journey-heading"></h2>
  <div class="sequence">
    <figure><img data-lp-image="journey-a"><figcaption data-lp-text="journey-a-label"></figcaption></figure>
    <figure><img data-lp-image="journey-b"><figcaption data-lp-text="journey-b-label"></figcaption></figure>
    <figure><img data-lp-image="journey-c"><figcaption data-lp-text="journey-c-label"></figcaption></figure>
  </div>
</section>
```

```css
.sequence{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.75rem}
.sequence img{width:100%;aspect-ratio:1;object-fit:contain}.sequence figcaption{text-align:center}
@media(max-width:640px){.sequence{grid-template-columns:1fr;gap:1.75rem}h2{text-align:left}}
```

背景ブラシや紙面は別の `images[]` として束縛できるが、ライブ文字をラスタ画像の内部へ埋め込まない。`texts[]` の各要素は `id`, `label`, `value`, `role`、`images[]` は `id`, `url`, `alt`, `role` を持つ。

## レスポンシブ規則

- PCは3場面を横並びにして変化を一望させる。全画像の比率、人物の大きさ、余白を揃える。
- モバイルは1列にし、画像→短い説明を3回繰り返す。順番をDOMで保持する。
- native `cardgrid` は`columns=2`でモバイルも2列、`3`でモバイル1列、`4`でモバイル2列になる。説明量と希望するPC・モバイル列が両方合うときだけ使い、列数を埋めるために内容を増減しない。
- 大見出しの手動改行はデバイス別に検証する。タブレットで助詞だけが次行へ送られる場合、フォント、列幅、padding、改行位置を同時に見直す。

## 後半の作り込み

連作のあとに「次に何が決まるか」を一枚のノートや成果物で見せる。これは装飾的な締めではなく、相談の出口を具体化する章である。その後はFAQで心理的障壁を解き、明確な案内と予約へつなぐ。前半と後半で人物、線、色温度を統一し、途中で別作品のようなイラストへ切り替えない。

## 使わない条件・失敗例

- 実物の状態、性能、安全性、症例などを証明すべき場面で、イラストを証拠として使わない。
- 「相談すれば必ず成功する」「契約不要」など未確認の保証を安心コピーとして加えない。
- 子ども向けでない案件に幼すぎる絵柄を当てない。相談者の属性を資料なしで固定しない。
- 同じ人物ポーズを色だけ変え、段階の違いを表したことにしない。

## 観察された弱点

初期版には根拠のない保証、長い見出し、タブレットでの不自然な分割があった。最終版でも連作間の余白はやや広く、イラストの一貫性は生成ごとに目視確認が必要である。イラストが美しくても、各場面が異なる問いへ答えていなければ情報密度は上がらない。
