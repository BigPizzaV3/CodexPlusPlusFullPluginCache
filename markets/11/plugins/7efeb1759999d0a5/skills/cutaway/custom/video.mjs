const unsupported = "MP4 export is unavailable here. Download the HTML and open it in a current Chrome or Safari browser.";

function pending(start, signal, timeout = 5000) {
  return new Promise((resolve, reject) => {
    let cleanup = () => {};
    let settled = false;
    const finish = (error, value) => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      signal.removeEventListener("abort", abort);
      cleanup();
      if (error) reject(error); else resolve(value);
    };
    const abort = () => finish(signal.reason);
    const timer = setTimeout(() => finish(new Error("Video export timed out. Please try again.")), timeout);
    signal.addEventListener("abort", abort, { once: true });
    if (signal.aborted) return abort();
    try {
      cleanup = start(value => finish(null, value), error => finish(error)) ?? cleanup;
      if (settled) cleanup();
    } catch (error) { finish(error); }
  });
}

function wait(milliseconds, signal) {
  return pending(done => {
    const timer = setTimeout(done, milliseconds);
    return () => clearTimeout(timer);
  }, signal, milliseconds + 5000);
}

function lines(context, text, x, y, width, height, limit) {
  const words = String(text).trim().split(/\s+/);
  let line = "", row = 0;
  for (const word of words) {
    const next = line ? `${line} ${word}` : word;
    if (context.measureText(next).width > width) {
      if (row === limit - 1 || !line) {
        let clipped = next;
        while (clipped && context.measureText(`${clipped}…`).width > width) clipped = clipped.slice(0, -1);
        context.fillText(`${clipped}…`, x, y + row * height);
        return;
      }
      context.fillText(line, x, y + row++ * height);
      line = word;
    } else line = next;
  }
  if (line) context.fillText(line, x, y + row * height);
}

async function paint(context, diagram, config, state, signal) {
  const copy = diagram.cloneNode(true);
  copy.querySelectorAll("metadata, script, desc, title").forEach(node => node.remove());
  const bounds = copy.getAttribute("viewBox").trim().split(/[ ,]+/).map(Number);
  const [, , width, height] = bounds;
  if (bounds.length !== 4 || !bounds.every(Number.isFinite) || width <= 0 || height <= 0) throw new Error("The drawing needs a valid viewBox to export video.");
  copy.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  copy.setAttribute("width", String(width));
  copy.setAttribute("height", String(height));
  const url = URL.createObjectURL(new Blob([new XMLSerializer().serializeToString(copy)], { type: "image/svg+xml" }));
  const picture = new Image();
  try {
    await pending((done, fail) => {
      picture.onload = done;
      picture.onerror = () => fail(new Error("This preview couldn't render the video. Download the HTML and try it in a browser."));
      picture.src = url;
      return () => { picture.onload = null; picture.onerror = null; };
    }, signal);
    context.fillStyle = "#f6f3ec";
    context.fillRect(0, 0, 1080, 1080);
    context.fillStyle = "#293a31";
    context.font = "600 38px sans-serif";
    lines(context, config.title, 48, 62, 984, 44, 2);
    context.font = "20px sans-serif";
    const status = { likely: "Likely match", confirmed: "Identified", unknown: "Unconfirmed", generic: "Illustrative model" }[config.research.identification.status];
    lines(context, `${status}: ${config.research.identification.name}`, 48, 140, 984, 24, 1);
    const scale = Math.min(984 / width, 650 / height);
    context.drawImage(picture, (1080 - width * scale) / 2, 164 + (650 - height * scale) / 2, width * scale, height * scale);
    context.font = "600 28px sans-serif";
    lines(context, state.title, 48, 855, 984, 34, 2);
    context.font = "22px sans-serif";
    lines(context, state.description, 48, 930, 984, 28, 2);
    context.fillStyle = "#647066";
    context.font = "18px sans-serif";
    lines(context, `Illustrative cutaway · ${config.note}`, 48, 1018, 984, 24, 2);
  } finally {
    picture.src = "";
    URL.revokeObjectURL(url);
  }
}

export async function recordVideo({ diagram, config, drawFrame, signal, onProgress }) {
  const mimeType = typeof MediaRecorder !== "undefined" && ["video/mp4;codecs=avc1.420028", "video/mp4;codecs=avc1"].find(type => MediaRecorder.isTypeSupported(type));
  if (!mimeType || typeof HTMLCanvasElement.prototype.captureStream !== "function") throw new Error(unsupported);
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = 1080;
  const context = canvas.getContext("2d", { alpha: false });
  if (!context) throw new Error(unsupported);
  const controller = new AbortController();
  const abort = () => controller.abort(signal.reason);
  const hidden = () => { if (document.hidden) controller.abort(new Error("Video export stopped because the tab was hidden. Keep it open and try again.")); };
  signal.addEventListener("abort", abort, { once: true });
  document.addEventListener("visibilitychange", hidden);
  if (signal.aborted) abort();
  hidden();
  const active = controller.signal;
  const chunks = [];
  let stream, recorder, finishing = false, bytes = 0;
  const deadline = setTimeout(() => controller.abort(new Error("Video export took too long. Please try again.")), 90000);
  try {
    active.throwIfAborted();
    await paint(context, diagram, config, drawFrame(0), active);
    stream = canvas.captureStream(30);
    try { recorder = new MediaRecorder(stream, { mimeType, videoBitsPerSecond: 6_000_000 }); }
    catch { throw new Error(unsupported); }
    recorder.addEventListener("dataavailable", event => {
      if (!event.data.size) return;
      bytes += event.data.size;
      if (bytes > 64 * 1024 * 1024) controller.abort(new Error("The video is too large. Please try a shorter cycle."));
      else chunks.push(event.data);
    });
    recorder.addEventListener("error", () => controller.abort(new Error("The browser couldn't encode this video. Download the HTML and try another browser.")));
    recorder.addEventListener("stop", () => {
      if (!finishing) controller.abort(new Error("Video export stopped before the cycle finished. Please try again."));
    });
    recorder.start(1000);
    const frames = Math.round(Math.min(30, Math.max(4, config.cycleSeconds)) * 30);
    const started = performance.now();
    for (let index = 0; index <= frames + 18; index++) {
      await wait(Math.max(0, started + index * 1000 / 30 - performance.now()), active);
      active.throwIfAborted();
      const progress = Math.min(1, index / frames);
      await paint(context, diagram, config, drawFrame(progress), active);
      onProgress(Math.floor(progress * 100));
    }
    await wait(50, active);
    finishing = true;
    await pending(done => {
      recorder.addEventListener("stop", done, { once: true });
      recorder.stop();
      return () => recorder.removeEventListener("stop", done);
    }, active);
    active.throwIfAborted();
    if (!bytes) throw new Error("The browser returned an empty video. Please try again.");
    return new Blob(chunks, { type: "video/mp4" });
  } finally {
    finishing = true;
    try {
      if (recorder && recorder.state !== "inactive") recorder.stop();
    } finally {
      stream?.getTracks().forEach(track => track.stop());
      clearTimeout(deadline);
      signal.removeEventListener("abort", abort);
      document.removeEventListener("visibilitychange", hidden);
      canvas.width = canvas.height = 0;
    }
  }
}
