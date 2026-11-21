# Install or update / 安裝或更新

EW Manim Draw 0.5.0

## Existing owner copy / 更新既有外掛

Attach the complete ZIP to a conversation with Plugin Creator and request an update of your existing EW Manim Draw. Preserve its plugin identity, sharing and icons. Use this request:

> 請以這個完整 ZIP 更新我擁有的 EW Manim Draw 為 0.5.0。保留原外掛 ID、圖示與分享範圍，完整保留 skills 下的程式與參考文件。這是 Skills-only 外掛，不新增 MCP、不公開發布。先確認既有外掛及我的更新權限；完成後提供真實保存狀態與外掛連結。

Only an actual successful plugin update makes the installed plugin 0.5.0. Attaching a ZIP to ordinary chat is not installation. Account/workspace permissions may limit the import workflow; do not infer success from having downloaded the ZIP.

## Friend's independent copy / 朋友安裝

Friends who have Plugin Creator creation permission may attach this ZIP and request creation of their own private plugin. Their copy is independent; later upgrades require sending the new complete ZIP and updating that copy. Do not delete/recreate an existing copy merely to upgrade it.

> 請使用這個 ZIP 建立我自己的私人 EW Manim Draw 0.5.0 外掛，保留全部程式、技能、圖示及範例，不公開發布。請核對建立權限並提供實際保存狀態。

## First use / 第一次使用

Select the installed EW Manim Draw, attach a document and say:

> 把這份文件畫成動態架構圖。

Check: full architecture visible at frame one; current step only is emphasized; captions/progress change together; labels readable; arrows/source facts preserved; actual GIF downloaded.

## Local execution / 本地程式

Requires Python and Pillow from requirements.txt. Use a licensed language font:

```bash
python skills/ew-manim-draw/scripts/diagram.py skills/ew-manim-draw/examples/guided_architecture.json --font /absolute/font.ttf --out output
```

For Traditional/Simplified Chinese, use an appropriate Noto Sans CJK font. The package does not include fonts. Use `--embed-font` only when the supplied font license permits embedding; otherwise the exact font must be installed on the HTML viewer's computer. Optional Playwright/Chromium are only needed for browser verification, not GIF/PNG output.

The build tested renderer outputs and one-sentence source interpretation; it did not test import into a friend's account or HTML browser playback. Users without a suitable execution host can obtain validated JSON, but installing a skills-only plugin does not create Python/browser permissions.
