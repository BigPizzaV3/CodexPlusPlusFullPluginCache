# Video Recording

Record only a public demo, local fixture, or disposable synthetic browser session for local debugging and verification. Browser video can expose visible names, messages, notifications, account details, filenames, faces, and other people even when the intended interaction is harmless.

## Privacy gate

- Never record a sign-in, password, payment, health or education record, private message, admin page, personal account, or third-party private content. Reproduce the behavior with synthetic data instead.
- Never record a user's everyday browser profile or signed-in tabs. Use a new isolated synthetic session.
- Before recording, close unrelated tabs and notifications and verify the exact origin, viewport, and synthetic data.
- Stop immediately if an unexpected identifier, notification, private tab, or real account appears.
- Save the video only in a task-specific temporary directory outside the plugin, repository, and public outputs.
- Do not upload, publish, attach, share, or place the recording in a public output, even after editing. Keep it as a temporary local diagnostic and report only the verified result.
- Remove the temporary recording after local review. Redaction after capture is not a substitute for preventing sensitive capture.

## Basic Recording

```bash
# Open a public demo in a new isolated session
playwright-cli -s=synthetic-video open https://demo.playwright.dev/todomvc

# Start recording
playwright-cli -s=synthetic-video video-start TEST_OUTPUT_DIR/TEST_TODO_DEMO.webm

# Add a chapter marker for section transitions
playwright-cli -s=synthetic-video video-chapter "Getting Started" --description="Opening the public demo" --duration=2000

# Navigate and perform actions
playwright-cli -s=synthetic-video snapshot

# Add another chapter
playwright-cli -s=synthetic-video video-chapter "Synthetic Input" --description="Entering test data" --duration=2000
playwright-cli -s=synthetic-video fill "getByPlaceholder('What needs to be done?')" "TEST_ITEM"

# Stop and save
playwright-cli -s=synthetic-video video-stop
playwright-cli -s=synthetic-video close
```

## Best Practices

### 1. Use Descriptive Filenames

```bash
# Include context in filename
playwright-cli video-start TEST_OUTPUT_DIR/TEST_TODO_FLOW.webm
playwright-cli video-start TEST_OUTPUT_DIR/TEST_LAYOUT_RUN_42.webm
```

### 2. Record entire hero scripts.

For an authorized synthetic demo, a reviewed code snippet can add pauses and annotations. Keep the recording local by default; the existence of a recording does not authorize sharing it.

1) Perform scenario using CLI and take note of all locators and actions. You'll need those locators to request their bounding boxes for highlight.
2) Create a file with the intended script for video (below). Use pressSequentially w/ delay for nice typing, make reasonable pauses.
3) Use playwright-cli run-code --filename your-script.js

**Important**: Overlays are `pointer-events: none` — they do not interfere with page interactions. You can safely keep sticky overlays visible while clicking, filling, or performing any actions on the page.

```js
async page => {
  await page.screencast.start({ path: 'video.webm', size: { width: 1280, height: 800 } });
  await page.goto('https://demo.playwright.dev/todomvc');

  // Show a chapter card — blurs the page and shows a dialog.
  // Blocks until duration expires, then auto-removes.
  // Use this for simple use cases, but always feel free to hand-craft your own beautiful
  // overlay via await page.screencast.showOverlay().
  await page.screencast.showChapter('Adding Todo Items', {
    description: 'We will add several items to the todo list.',
    duration: 2000,
  });

  // Perform action
  await page.getByRole('textbox', { name: 'What needs to be done?' }).pressSequentially('Walk the dog', { delay: 60 });
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.waitForTimeout(1000);

  // Show next chapter
  await page.screencast.showChapter('Verifying Results', {
    description: 'Checking the item appeared in the list.',
    duration: 2000,
  });

  // Add a sticky annotation that stays while you perform actions.
  // Overlays are pointer-events: none, so they won't block clicks.
  const annotation = await page.screencast.showOverlay(`
    <div style="position: absolute; top: 8px; right: 8px;
      padding: 6px 12px; background: rgba(0,0,0,0.7);
      border-radius: 8px; font-size: 13px; color: white;">
      ✓ Item added successfully
    </div>
  `);

  // Perform more actions while the annotation is visible
  await page.getByRole('textbox', { name: 'What needs to be done?' }).pressSequentially('Buy groceries', { delay: 60 });
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.waitForTimeout(1500);

  // Remove the annotation when done
  await annotation.dispose();

  // You can also highlight relevant locators and provide contextual annotations.
  const bounds = await page.getByText('Walk the dog').boundingBox();
  await page.screencast.showOverlay(`
    <div style="position: absolute;
      top: ${bounds.y}px;
      left: ${bounds.x}px;
      width: ${bounds.width}px;
      height: ${bounds.height}px;
      border: 1px solid red;">
    </div>
    <div style="position: absolute;
      top: ${bounds.y + bounds.height + 5}px;
      left: ${bounds.x + bounds.width / 2}px;
      transform: translateX(-50%);
      padding: 6px;
      background: #808080;
      border-radius: 10px;
      font-size: 14px;
      color: white;">Check it out, it is right above this text
    </div>
  `, { duration: 2000 });

  await page.screencast.stop();
}
```

Use overlays only to clarify the authorized synthetic test. Never place private values in overlay text.

### Overlay API Summary

| Method | Use Case |
|--------|----------|
| `page.screencast.showChapter(title, { description?, duration?, styleSheet? })` | Full-screen chapter card with blurred backdrop — ideal for section transitions |
| `page.screencast.showOverlay(html, { duration? })` | Custom HTML overlay — use for callouts, labels, highlights |
| `disposable.dispose()` | Remove a sticky overlay added without duration |
| `page.screencast.hideOverlays()` / `page.screencast.showOverlays()` | Temporarily hide/show all overlays |

## Tracing vs Video

| Feature | Video | Tracing |
|---------|-------|---------|
| Output | WebM file | Trace file (viewable in Trace Viewer) |
| Shows | Visual recording | DOM snapshots, network, console, actions |
| Use case | Demos, documentation | Debugging, analysis |
| Size | Larger | Smaller |

## Limitations

- Recording adds slight overhead to automation
- Large recordings can consume significant disk space
- Recordings can retain sensitive pixels even when the final frame looks safe
