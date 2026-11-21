import { clamp, json, standaloneSvg } from "./contract.mjs";
import { recordVideo } from "./video.mjs";

export function mountCutaway({ frame: modelFrame, render }) {
  const container = document.querySelector(".cutaway-root");
  const get = selector => container.querySelector(selector);
  const config = JSON.parse(get("#cutaway-data").textContent);
  const root = get("main");
  const diagram = get("#drawing svg");
  const slider = get("#progress");
  const play = get("#play");
  const shell = get("#shell");
  const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let progress = clamp(config.state.progress);
  let selected = config.state.part;
  let running = false;
  let visible = true;
  let request = 0;
  let last = null;
  let videoJob = null;
  let videoUrl = null;

  function selectPart(id) {
    if (videoJob) return;
    const part = config.parts.find(item => item.id === id);
    if (!part) return;
    selected = id;
    get("#part-title").textContent = part.title;
    get("#part-description").textContent = part.description;
    const sources = get("#part-sources");
    sources.replaceChildren(...part.sources.map(sourceId => {
      const source = config.research.sources[sourceId];
      const link = document.createElement("a");
      link.href = source.url;
      link.textContent = source.label;
      link.target = "_blank";
      link.rel = "noreferrer";
      return link;
    }));
    diagram.querySelectorAll("[data-part]").forEach(node => node.classList.toggle("selected", node.dataset.part === id));
    root.querySelectorAll("[data-select]").forEach(node => node.setAttribute("aria-pressed", String(node.dataset.select === id)));
  }

  function draw() {
    const state = modelFrame(progress);
    slider.value = String(progress * 100);
    slider.setAttribute("aria-valuetext", `${state.title}, ${Math.round(progress * 100)} percent through the illustration`);
    get("#stage").textContent = state.title;
    get("#stage-description").textContent = state.description;
    play.textContent = motion.matches ? "Next stage" : running ? "Pause" : progress >= 1 ? "Replay" : "Play cycle";
    play.setAttribute("aria-pressed", String(running));
    render({ root, diagram, state, view: config.view });
    return state;
  }

  function suspend() {
    cancelAnimationFrame(request);
    request = 0;
    last = null;
  }
  function stop() {
    running = false;
    suspend();
    draw();
  }
  function tick(time) {
    request = 0;
    if (!running || !visible || document.hidden || motion.matches) return;
    if (last !== null) progress = clamp(progress + Math.min((time - last) / 1000, .06) / config.cycleSeconds);
    last = time;
    if (progress >= 1) running = false;
    draw();
    if (running) request = requestAnimationFrame(tick);
  }
  function resume() {
    last = null;
    if (running && visible && !document.hidden && !request && !motion.matches) request = requestAnimationFrame(tick);
  }
  function exterior() {
    const node = diagram.querySelector("#exterior");
    if (node) node.setAttribute("opacity", shell.checked ? "1" : "0");
  }
  function download(text, type, name) {
    const url = URL.createObjectURL(new Blob([text], { type }));
    const link = document.createElement("a");
    link.href = url;
    link.download = name;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function exportView(format) {
    if (videoJob) return;
    if (format === "mp4") return exportVideo();
    const state = { progress, part: selected, exterior: shell.checked };
    try {
      if (format === "svg") {
        download(standaloneSvg(new XMLSerializer().serializeToString(diagram), { ...config, state }), "image/svg+xml", "cutaway.svg");
      } else {
        const page = document.implementation.createHTMLDocument(`${config.title} · Cutaway`);
        page.documentElement.lang = "en";
        const charset = page.createElement("meta");
        charset.setAttribute("charset", "utf-8");
        const viewport = page.createElement("meta");
        viewport.name = "viewport";
        viewport.content = "width=device-width,initial-scale=1";
        page.head.prepend(charset, viewport);
        page.body.style.margin = "0";
        page.body.append(container.cloneNode(true));
        page.querySelector("#cutaway-data").textContent = json({ ...config, state });
        page.querySelector("#export-status").textContent = "";
        page.querySelector("#save-video").removeAttribute("href");
        page.querySelector("#save-video").hidden = true;
        const doctype = new XMLSerializer().serializeToString(page.doctype);
        download(`${doctype}\n${page.documentElement.outerHTML}`, "text/html", "cutaway.html");
      }
      get("#export-status").textContent = "Download prepared.";
    } catch {
      get("#export-status").textContent = "Downloads are unavailable in this preview. Use the attached file.";
    }
  }

  function clearVideo() {
    if (videoUrl) URL.revokeObjectURL(videoUrl);
    videoUrl = null;
    get("#save-video").removeAttribute("href");
    get("#save-video").hidden = true;
  }

  async function exportVideo() {
    const saved = { progress, running };
    stop();
    clearVideo();
    videoJob = new AbortController();
    const controls = [...root.querySelectorAll("button, input")].filter(node => node.id !== "cancel-video");
    const disabled = controls.map(node => node.disabled);
    controls.forEach(node => { node.disabled = true; });
    const button = get('[data-export="mp4"]');
    button.setAttribute("aria-busy", "true");
    get("#cancel-video").hidden = false;
    get("#export-status").textContent = "Preparing video. Keep this tab open.";
    let percentage = -1;
    try {
      const blob = await recordVideo({
        diagram, config, signal: videoJob.signal,
        drawFrame(value) { progress = value; return draw(); },
        onProgress(value) {
          const next = Math.floor(value / 5) * 5;
          if (next === percentage) return;
          percentage = next;
          get("#export-status").textContent = `Preparing video: ${next}%. Keep this tab open.`;
        },
      });
      videoUrl = URL.createObjectURL(blob);
      const link = get("#save-video");
      link.href = videoUrl;
      link.hidden = false;
      get("#export-status").textContent = "Video ready.";
      link.click();
    } catch (error) {
      get("#export-status").textContent = error.name === "AbortError" ? "Video export cancelled." : error.message || "Video export failed. Download the HTML and try it in a browser.";
    } finally {
      videoJob = null;
      controls.forEach((node, index) => { node.disabled = disabled[index]; });
      button.removeAttribute("aria-busy");
      get("#cancel-video").hidden = true;
      progress = saved.progress;
      running = saved.running && !motion.matches;
      draw();
      resume();
    }
  }

  play.addEventListener("click", () => {
    if (motion.matches) {
      progress = config.steps.find(value => value > progress + .00001) ?? 0;
      draw();
      return;
    }
    if (running) return stop();
    if (progress >= 1) progress = 0;
    running = true;
    draw();
    resume();
  });
  slider.addEventListener("input", () => {
    const value = Number(slider.value);
    progress = clamp(value / 100);
    stop();
  });
  get("#reset").addEventListener("click", () => { progress = 0; stop(); });
  root.querySelectorAll("[data-select]").forEach(node => node.addEventListener("click", () => selectPart(node.dataset.select)));
  diagram.querySelectorAll("[data-part]").forEach(node => node.addEventListener("click", () => selectPart(node.dataset.part)));
  shell.addEventListener("change", exterior);
  root.querySelectorAll("[data-export]").forEach(node => node.addEventListener("click", () => exportView(node.dataset.export)));
  get("#cancel-video").addEventListener("click", () => videoJob?.abort(new DOMException("Cancelled", "AbortError")));
  window.addEventListener("pagehide", () => { videoJob?.abort(new DOMException("Page closed", "AbortError")); clearVideo(); });
  document.addEventListener("visibilitychange", () => document.hidden ? suspend() : resume());
  motion.addEventListener("change", stop);
  if (typeof IntersectionObserver !== "undefined") new IntersectionObserver(entries => {
    visible = entries.at(-1).isIntersecting;
    if (visible) resume(); else suspend();
  }).observe(get("#drawing"));
  shell.closest("label").hidden = !diagram.querySelector("#exterior");
  shell.checked = config.state.exterior;
  exterior();
  selectPart(selected);
  draw();
}
