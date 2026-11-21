# 原本14の適用とコア画像プロンプト

このSkillの出典は original-14.txt。旧試作の「実画像を通常生成」「フルバナーの周辺背景を設計」は原本から確認できないため、既定動作から除去した。原本は英語プロンプト3本だけを返す。実画像やフルバナーを明示依頼された場合にだけ拡張する。

## 完成プロンプトの骨格

次の要素を実際の内容で埋め、A/B/Cそれぞれが単独で使える3本を作る。原本の構図・人物・文字・参考画像制約を全案に残す。

```text
Design exclusively for a 1546x423 core safe-area image.
Aspect ratio matching 1546x423. The canvas is exactly 1546 x 423 pixels.
This is only the core image, not a full-size YouTube banner.
No background extension beyond the canvas.
No extra elements outside the frame.
Create a complete, balanced composition entirely within this short rectangle.
{案ごとの構図・文字・主役・配色・照明}
Render exactly this text: “{表示する日本語等の原文}”.
Use large bold high-contrast text readable on a smartphone, with intentional line breaks.
Keep all text comfortably inside the canvas. No extra words, subtitles, or watermarks.
{人物がある場合: 本人写真と同一人物。頭全体と上部余白、手も内側。胸上等の保守的な大きさ}
Use the reference only for color palette, mood, lighting, and overall visual tone.
Do not transfer subject scale, vertical alignment, cropping logic, or banner boundaries from the reference.
Style match: {指定がある場合の率と対象}. Safe composition, scale, clarity, and spacing take priority.
No cropping, overflow, or implied space outside the canvas.
```

Aは最も整然・明快、Bは視覚的階層と対比、Cは照明や活気を変える。大きな人物で枠を埋めるなど、3案の差を安全領域の逸脱で作らない。

## 移行時の判断

- 1546×423を「確認済みの現在のYouTube仕様」として説明せず、旧GPTのコア画像設計として維持する。入稿や端末表示まで求められた時は公式ヘルプを確認する。
- 原本のSTRICT出力は最終3プロンプトに適用する。表示文字等が欠け、プロンプトを完成できないときの必要最小限の確認を妨げない。文字や肩書きを創作して厳密フォーマットだけを満たさない。
- 本人写真がない人物依頼では、外部ツールに本人写真を添付する条件を具体的に示す。未添付を添付済みとして書かない。人物なしの依頼に本人写真や手の描写を足さない。
- ユーザーが明示している枚数・言語・修正対象の変更は優先し、原本どおりの出力とは区別する。
