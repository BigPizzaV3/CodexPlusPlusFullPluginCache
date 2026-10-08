# Plugin report component library

この文書は、固定[`scripts/render_report.py`](../scripts/render_report.py)が生成するvisual componentと検査項目の参照です。HTMLを手動生成・再実装するための仕様ではありません。固定renderer runtimeを展開・検証できない場合は、ここにある断片から似たHTMLを作らず、`SKILL.md`のdelivery mode選択に従います。text diagnosis modeでは、このcomponentを再現しません。

## 1. Template placeholders

`assets/report-template.html`で置換できるplaceholderは3つだけです。

| placeholder | 内容 |
|---|---|
| `{{DOCUMENT_TITLE}}` | escape済みのdocument title |
| `{{SVG_SPRITE}}` | `assets/report-icons.svg`のinline SVG sprite |
| `{{REPORT_PAGES}}` | `.sheet.report-page`要素の並び（8〜10ページ） |

未解決placeholder、HTML comment、remote assetを完成品へ残しません。

## 2. Page shell

```html
<section class="sheet report-page" data-page="1" aria-label="01 判定">
  <div class="tk tk-tl"></div><div class="tk tk-tr"></div>
  <div class="tk tk-bl"></div><div class="tk tk-br"></div>
  <header class="hd">
    <span class="hd-l">
      <span class="header-wordmark" aria-label="ROGNALIA"><!-- traced SVG --></span>
      <span class="hd-sep">|</span><span>立地診断 mini</span>
    </span>
    <span class="hd-r">住所｜調査日 YYYY.MM.DD <b>01 判定</b></span>
  </header>
  <p class="kick">01｜VERDICT</p>
  <h1 class="pt">初期スクリーニング判定</h1>
  <p class="lead">このページで答える問いを一文で示す。</p>
  <main class="page-content"><!-- page body --></main>
  <footer class="ft">
    <p class="disc">固定免責</p>
    <div class="meta">
      <span class="fl"><span class="footer-wordmark" aria-label="ROGNALIA"><!-- traced SVG --></span><span>立地診断 mini</span></span>
      <span class="pg"><b>1</b> / 8</span>
    </div>
  </footer>
</section>
```

Rules:

- `.sheet`はA4 1枚。`overflow:hidden`を前提に、本文を縮小せずcopyを契約内へ収める。
- `.tk-*`は四隅のtrim mark。削除しない。
- `.hd`と`.ft`は全ページ共通。正式wordmarkを小さくinline挿入する。
- `.disc`は固定免責を完全一致で全ページに1件置く。
- `.pg`は実page数と一致する連番にする。
- header、footer以外へwordmarkを追加しない。大きなlogo、`Powered by`、copyrightを置かない。

## 3. Fixed page story

| 順番 | section | 主要component |
|---:|---|---|
| 1 | 判定 | `.idg`, `.vgrid`, `.scale-wrap`, `.conf`, `.concl`, `.assump`, `.legend`, `.toc` |
| 2 | 論拠 | `.ev`, `.st`, `.src`, `.plan`, `.chips`, `.note-line` |
| 3 | 基礎数値 | `.dstrip`, `.acq`, `.mrow`, `.metric`, `.bar-chart`, `.stacked-bar`, `.nochart` |
| 4 | 調査軸 | `.rt`と`data-research-id="R1"`〜`R8` |
| 5 | 業態適合 | `.lens`, `.fig-h`, `.demand-diagram`, `.dnode`, `.obs` |
| 6 | 競合・相乗 | `.ct`, `.kind`, `.obs`, `.missing-state` |
| 7 | 反証監査（条件付き） | `.cov`, `.risk-list`, `.risk-item`, `.risk-level` |
| 7または8 | 検証計画 | `.cond`, `.fc`, `.at` |
| 最終1〜2枚 | 出典・監査 | `.cov`, `.sreg`, `.sr`, `.method-note`, `.handoff`, `.closing-qr` |

risk合計が3件以上なら反証監査pageを追加します。sourceは16件まで1ページ、17〜32件は2ページへ均等分割します。最終pageだけに`.handoff`を置きます。

## 4. Shared headings and evidence

```html
<div class="blk-h">
  <span class="no">支持</span>
  <span class="t">判定を押し上げる3要因</span>
  <span class="note">状態記号と出典は01の凡例に対応</span>
</div>
```

```html
<div class="ev">
  <p class="et">短い論点名</p>
  <p class="ed">確認した事実と判断への意味を混ぜず、110字以内で説明する。</p>
  <div class="em">
    <span class="st is-confirmed">確認済み</span>
    <span class="src">S1・S3</span>
  </div>
</div>
```

Status class:

| status | class | label |
|---|---|---|
| `confirmed` | `.is-confirmed` | 確認済み |
| `estimated` | `.is-estimated` | 推定 |
| `reference` | `.is-reference` | 参考情報 |
| `not_found` | `.is-notfound` | 公開情報では確認できず |
| `field_check` | `.is-fieldcheck` | 現地・資料確認 |

色だけで状態を表さず、必ずlabelを併記します。confirmed / estimatedの主張には実在するS番号を付けます。

## 5. Verdict

- `.scale`は1件だけ置き、`.cell`を1〜5の5区分にする。
- 選択中の区分だけ`.cell.sel`と`aria-current="true"`を持つ。
- labelは1=`見送り推奨`、2=`見送り寄り`、3=`条件次第`、4=`前向きに検討`、5=`積極検討`で固定する。
- `.conf`はratingとは別の根拠確度。低・中・高のうち1件だけ`.on`にする。
- `.concl`の左罫線はviolet。結論を装飾cardへ埋めず、短い宣言として見せる。
- `.toc`は実際のsection番号へ合わせ、risk pageがない時に空の07を残さない。

## 6. Baselines and charts

各D1〜D4は`<section class="dstrip" data-baseline="D1">`として1件ずつ置きます。

- `.metric`はname、display value、時点、範囲、S番号を同じblockへ置く。
- `bar_pair`は同一定義・同一境界の2時点値だけを`.bar-chart`で表示する。barは原点0。
- `stacked_share`は同一出典・同一年次・同一範囲で合計100の時だけ`.stacked-bar`を表示する。
- 比較できない時は`.nochart`へ取得状態と理由を置き、0値のchartを作らない。
- 上位地域代替、地点照合が必要、初期診断では未取得を`.acq`の文字で明示する。

## 7. Research table

`.rt`は列を`軸 / 確認した事実 / 判断への含意`の3つに固定します。各rowへ`data-research-id="R1"`〜`R8`を1件ずつ付けます。

- findingは140字以内、meaningは100字以内。
- 未確認を不存在や自動減点へ変えない。
- `.hl`は未取得または現地確認が必要なrowに使う。警告色で煽らない。

## 8. Demand connection diagram

`.demand-diagram`は次を線で接続します。

```text
アクセス ─┐                  ┌→ 来店目的
          ├→ 想定業態 ──────┤
相乗施設 ─┘                  └→ 需要時間帯
```

node textはR2、相乗施設、business、customer purpose、demand periodsから作ります。decorativeな数値や根拠のない顧客像を追加しません。SVG pathはconnectorとしてのみ使い、意味のあるnode textはHTMLに残します。

## 9. Risk and verification

- riskは`重大阻害 / 不一致 / 要確認`へ分け、`.risk-level`の文字を必ず表示する。
- riskが3件以上なら専用pageへ置く。0〜2件なら検証計画pageの先頭へ置く。
- `.cond`は判定反転条件と対応する現地確認・追加dataを結ぶ。
- `.fc`は必ず5件。紙面上でcheckできる空欄を残す。
- `.at`は`取得するもの / 方法 / 意思決定への使い方`の3列にする。

## 10. Sources and handoff

```html
<li class="sr">
  <span class="sid2">S1</span>
  <div>
    <a class="t2" href="完全URL">出典title</a>
    <p class="u2">短縮表示URL</p>
    <p class="m2">発行主体 | 情報時点 | 支持 <b>R1・R3</b></p>
  </div>
</li>
```

- sourceは1〜32件。実際に開いて本文を確認したURLだけを載せる。
- 最終source pageのleadは`主要な判断根拠は、N件の公開出典から確認できる。`とする。
- `.handoff`は最終pageだけに置き、page contentの15%以内にする。固定免責の上へ最低3mmの安全余白を残し、source件数が上限でも重ねない。
- CTAは固定URLと静的QRを使う。価格、申込、`有料版なら取得可能`、成果保証を置かない。

## 11. Print action

画面上に次のbuttonを1件だけ置きます。

```html
<button class="print-action" type="button" onclick="window.print()">
  <span class="print-action-label">PDFとして保存</span>
</button>
```

`script`要素、追加event handler、PDF変換library、canvas、blob生成は使いません。`@media print`でbuttonを完全に消します。

## 12. Completion checklist

1. `.report-page`が8〜10件で、page numberが1から連番、分母が実page数と一致する。
2. 全pageにheader wordmark、固定免責、footer wordmark、`立地診断 mini`が各1件ある。
3. 一次判定scaleが5区分、選択中が1件、根拠確度が独立して表示される。
4. R1〜R8とD1〜D4が各1件ある。
5. source IDが欠番なく、全参照S番号が存在する。
6. 現地確認が5件あり、flip conditionと追加dataが接続されている。
7. placeholder、絵文字、remote asset、`Powered by`、copyright、radar chartが0件。
8. `onclick="window.print()"`が1件、`script`要素が0件。
9. A4 print previewでHTML page数とPDF page数が一致し、白紙、clipping、重なりがない。
10. 文字を縮めて収めず、risk pageまたはsource continuationの条件で8〜10ページに収めている。
