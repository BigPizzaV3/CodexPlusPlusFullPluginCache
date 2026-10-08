import { mkdir, writeFile } from "node:fs/promises";
import { basename, join } from "node:path";

// Accept an existing Playwright page belonging to the real development app.
export async function startCapture(page, dir) {
  // Each attempt owns a new directory; preserve earlier evidence.
  await mkdir(dir);
  const session = await page.context().newCDPSession(page);
  const frames = [];
  const pending = [];
  let style;
  let installed = false;
  let accepting = true;
  let writeError;
  const cleanup = async () => {
    try {
      await session.send("Page.stopScreencast");
    } finally {
      accepting = false;
      await Promise.all(pending);
      const results = await Promise.allSettled([
        installed
          ? page.evaluate(() => {
              for (const type of [
                "pointermove",
                "pointerdown",
                "pointerup",
                "click",
              ]) {
                document.removeEventListener(
                  type,
                  window.__demoCapture.handler,
                  true,
                );
              }
              delete window.__demoCapture;
            })
          : Promise.resolve(),
        style ? style.evaluate((el) => el.remove()) : Promise.resolve(),
        session.detach(),
      ]);
      const failed = results.find((result) => result.status === "rejected");
      if (failed) throw failed.reason;
    }
  };
  try {
    const geometry = await page.evaluate(() => {
      if (window.__demoCapture)
        throw new Error("A capture already owns this page");
      const events = [];
      const handler = (event) => {
        if (!event.isTrusted) return;
        events.push({
          type: event.type,
          epochSeconds: (performance.timeOrigin + event.timeStamp) / 1000,
          x: event.clientX,
          y: event.clientY,
          button: event.button,
          buttons: event.buttons,
        });
      };
      window.__demoCapture = { events, handler };
      for (const type of ["pointermove", "pointerdown", "pointerup", "click"]) {
        document.addEventListener(type, handler, true);
      }
      return {
        widthCss: innerWidth,
        heightCss: innerHeight,
        dpr: devicePixelRatio,
        timeOrigin: performance.timeOrigin,
      };
    });
    installed = true;
    style = await page.addStyleTag({
      content: "* { cursor: none !important; }",
    });
    session.on("Page.screencastFrame", (frame) => {
      void session
        .send("Page.screencastFrameAck", { sessionId: frame.sessionId })
        .catch(() => {});
      if (!accepting) return;
      const file = `frame-${String(frames.length).padStart(6, "0")}.png`;
      frames.push({
        file,
        epochSeconds: frame.metadata.timestamp,
        metadata: frame.metadata,
      });
      pending.push(
        writeFile(join(dir, file), Buffer.from(frame.data, "base64")).catch(
          (error) => {
            writeError ??= error;
          },
        ),
      );
    });
    await session.send("Page.startScreencast", {
      format: "png",
      maxWidth: 3200,
      maxHeight: 2000,
      everyNthFrame: 1,
    });
    for (let n = 0; n < 100 && !frames.length; n++)
      await new Promise((resolve) => setTimeout(resolve, 50));
    if (!frames.length) throw new Error("No real renderer frames captured");
    return {
      async stop(task, outcome) {
        try {
          // Let the final action paint before stopping and draining frame delivery.
          await page.evaluate(
            () =>
              new Promise((resolve) => {
                requestAnimationFrame(() => requestAnimationFrame(resolve));
              }),
          );
          await session.send("Page.stopScreencast");
          accepting = false;
          const final = await page.evaluate(() => ({
            stopEpochSeconds:
              (performance.timeOrigin + performance.now()) / 1000,
            events: window.__demoCapture.events,
          }));
          await Promise.all(pending);
          if (writeError) throw writeError;
          const manifest = {
            task,
            outcome,
            session_id: basename(dir),
            viewport: {
              width: geometry.widthCss,
              height: geometry.heightCss,
              dpr: geometry.dpr,
            },
            source:
              "CDP Page.startScreencast from the actual app renderer; native window chrome excluded",
            clock:
              "CDP frame metadata timestamp and DOM performance.timeOrigin + event.timeStamp, Unix epoch seconds",
            geometry,
            firstFrameEpochSeconds: frames[0].epochSeconds,
            ...final,
            frames,
          };
          await writeFile(
            join(dir, "manifest.json"),
            JSON.stringify(manifest, null, 2) + "\n",
          );
          return {
            dir,
            frames: frames.length,
            events: final.events.length,
            duration: final.stopEpochSeconds - frames[0].epochSeconds,
            geometry,
          };
        } finally {
          await cleanup();
        }
      },
    };
  } catch (error) {
    await cleanup().catch(() => {});
    throw error;
  }
}
