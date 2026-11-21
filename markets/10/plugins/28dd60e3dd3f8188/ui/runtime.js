(() => {
  const surface = document.body.dataset.surface;
  let builderOpen = surface === "builder";
  const isBuilder = () => builderOpen;
  const app = document.getElementById("app");
  const feedback = document.getElementById("feedback");
  const feedbackHome = feedback.parentElement;
  const pending = new Map();
  let bridge = "starting";
  // P5, 16 Oct: the Show 3 card in ChatGPT sent the model no context at all (P1's build card did). A card that ChatGPT loads while hidden
  // can miss the 500 ms handshake and settle on window.openai, where context only goes into widget state. When ChatGPT's MCP Apps
  // host answers that handshake late, the card remembers it (lateHost) and sends model context the standard way as well.
  let lateHost = false;
  let compatibilityReady = false;
  // The widths the card draws a page at. Our sites are designed for 1440 (John, 13 Oct: "all of our sites are optimized for 1400"), so the
  // desktop render and everything measured on it is 1440. The cached thumbnails (Projects list, earlier versions, other pages) are
  // 1280x800 images and stay so.
  const DESKTOP_W = 1440, PHONE_W = 390, THUMB_W = 1280;
  // The window height a page is drawn in, and measured in. The server shoots the page in a 1440x900 / 390x844 window
  // (PAGE_PREVIEW_*_HEIGHT in src/lib/design-thumbnail-image.ts, tied to these by a test): a section sized 100vh is that tall in the
  // picture, so the section boxes must come from a frame of the same height or a click lands on the wrong section (R3-01).
  const DESKTOP_VH = 900, PHONE_VH = 844;
  let sideFold = null, sequence = 0, output = {}, host = {}, library = null, selected = null, timer, stopped = false, loadingDesign = false, zoom = null;
  // Builder view state: device preview, the page or earlier version on screen, open menu, measured section boxes.
  let device = null, pageView = null, versionView = null, menu = null, boxes = null, hover = null, researchOpen = null, addingPage = false, addPageDraft = { designId: null, text: "" }, addPageSending = false;
  // Capabilities stay in this closure, never in model context or widgetState.
  let paidAction = null, paidRequest = null, proposedDirections = null, confirmingPaid = false, modeRenderDue = false;
  let directionQuoteGeneration = 0;
  const paidControls = [], directionQuotes = new Map(), directionQuoteTasks = new Map(), paidMounts = new WeakMap(), attemptedClicks = new Set();
  const acceptedQuotes = new Set();
  let progressContext = null;
  // What ChatGPT keeps for this card when it is shown again (widgetState): the builder's view, and (moved) the build, designs or
  // saved edit this card's own Confirm started. A reloaded card then shows that work, never its old quote with "Nothing was spent"
  // or a second Confirm (audit F3/F19). Each write merges into the last one, so the two kinds never overwrite each other.
  // ChatGPT also keeps the card's standard ui/update-model-context as its whole widgetState ({ content, structuredContent }), replacing
  // what keep() wrote (live, 16 Oct: a reopened built card found no prior work and showed "This quote has expired"). That shape is
  // this card's own last model context, so it is read as modelContent; the work it names is then read again through the owner's tools.
  const hostSaved = window.openai?.widgetState;
  let cardState = hostSaved && !hostSaved.modelContent && hostSaved.structuredContent && typeof hostSaved.structuredContent === "object"
    ? { ...hostSaved, modelContent: { ...hostSaved.structuredContent, message: (Array.isArray(hostSaved.content) ? hostSaved.content : []).map(item => item?.text || "").join("\n") } }
    : hostSaved || {};
  function keep(patch) {
    cardState = { ...cardState, ...patch, ...(patch.privateContent ? { privateContent: { ...cardState.privateContent, ...patch.privateContent } } : {}) };
    window.openai?.setWidgetState?.(cardState);
  }
  const persisted = cardState.privateContent;
  let restoreView = persisted?.version === 1 ? persisted : null;
  function saveView() {
    if (!isBuilder()) return;
    keep({ privateContent: { version: 1, designId: output.design?.designId ?? null, device, pageView, versionView, selected, sideFold, zoom, researchOpen } });
  }
  function restorePresentation() {
    if (!restoreView || !output.design) return;
    const saved = restoreView; restoreView = null;
    if (saved.designId !== output.design.designId) return;
    device = ["phone", "desktop"].includes(saved.device) ? saved.device : null;
    pageView = output.pages?.some(p => p.pageId === saved.pageView) ? saved.pageView : null;
    versionView = output.versions?.some(v => v.versionId === saved.versionView && !v.current) ? saved.versionView : null;
    selected = !versionView && output.sections?.some(s => s.sectionId === saved.selected) ? saved.selected : null;
    sideFold = typeof saved.sideFold === "boolean" ? saved.sideFold : null;
    zoom = typeof saved.zoom === "number" && Number.isFinite(saved.zoom) ? Math.max(0.1, Math.min(1.5, saved.zoom)) : null;
    researchOpen = typeof saved.researchOpen === "boolean" ? saved.researchOpen : null;
  }
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  // SIT-386: page code never enters the conversation. Reading a design sends no page (fix 4: 2+ MB made the card slow to open),
  // and a saved edit sends none either (fix 2): the card draws both from previewImageUrl. Only an edit that could not be saved
  // sends its revised page (html), in widget-only _meta, because nothing else holds that paid result; the card folds it back
  // into the result it renders. A result that carries a page (currentHtml, html) in its structured content, as an older
  // server's did, renders the same way. With no currentHtml the card has nothing to measure until the person points at the
  // preview or picks a section; then it asks once for a light copy (requestLayout) so sections can be outlined.
  const withPageCode = (value, meta) => {
    const out = { ...value };
    if (typeof meta?.currentHtml === "string" && typeof out.currentHtml !== "string") out.currentHtml = meta.currentHtml;
    if (typeof meta?.html === "string" && typeof out.html !== "string") out.html = meta.html;
    return out;
  };
  // A paid edit is delivered when its result has the revised html (a pasted page) or says it edited a saved design.
  const delivered = value => Boolean(value?.html) || value?.edited === true;
  const notify = (method, params) => {
    if (bridge === "compatibility") {
      if (method === "ui/notifications/size-changed") window.openai?.notifyIntrinsicHeight?.(params.height);
      return;
    }
    window.parent.postMessage({ jsonrpc: "2.0", method, params }, "*");
  };
  function request(method, params, limit) {
    if (stopped) return Promise.reject(new Error("This view has closed."));
    // A quote never starts paid work. It has the same deadline as a read.
    const paidCall = method === "tools/call" && params.arguments?.quoteOnly !== true
      && ["iter0_confirm_paid_action", "iter0_create_site", "iter0_edit_site", "iter0_show_three"].includes(params.name);
    const deadline = limit || (paidCall ? 900000 : 20000);
    if (bridge === "compatibility") {
      const api = window.openai;
      // Choose one bridge before interaction. Never resend a paid call through
      // another transport after a timeout or refusal.
      if (method === "tools/call" && api?.callTool) return new Promise((resolve, reject) => {
        const timeout = setTimeout(() => reject(new Error("ChatGPT did not respond. Try again.")), deadline);
        Promise.resolve().then(() => api.callTool(params.name, params.arguments)).then(resolve, error => {
          const refused = new Error(error?.message || "ChatGPT could not complete this request.");
          refused.hostRefusal = true; reject(refused);
        }).finally(() => clearTimeout(timeout));
      });
      if (method === "tools/call") {
        const unavailable = new Error("ChatGPT cannot call this tool from the card.");
        unavailable.hostRefusal = true;
        return Promise.reject(unavailable);
      }
      if (method === "ui/message" && api?.sendFollowUpMessage) return Promise.resolve().then(() => api.sendFollowUpMessage({ prompt: params.content.map(item => item.text || "").join("\n") })).then(result => result || {});
      if (method === "ui/open-link" && api?.openExternal) return Promise.resolve().then(() => api.openExternal({ href: params.url })).then(result => result || {});
      if (method === "ui/request-display-mode" && api?.requestDisplayMode) return Promise.resolve().then(() => api.requestDisplayMode({ mode: params.mode }));
      if (method === "ui/update-model-context" && (api?.setWidgetState || lateHost)) {
        if (api?.setWidgetState) keep({ modelContent: { ...params.structuredContent, message: (params.content || []).map(item => item.text || "").join("\n") } });
        // Its answer, if any, is not awaited: the widget state above is already kept.
        if (lateHost) window.parent.postMessage({ jsonrpc: "2.0", id: ++sequence, method, params }, "*");
        return Promise.resolve({});
      }
      return Promise.reject(new Error("This control is unavailable here. Continue in chat."));
    }
    return new Promise((resolve, reject) => {
      if (stopped) return reject(new Error("This view has closed."));
      const id = ++sequence;
      // Paid calls can outlive the 24-second start deadline (or return an edit).
      const timeout = setTimeout(() => { pending.delete(id); reject(new Error("ChatGPT did not respond. Try again.")); }, deadline);
      pending.set(id, { resolve, reject, timeout });
      window.parent.postMessage({ jsonrpc: "2.0", id, method, params }, "*");
    });
  }
  async function message(text) {
    const result = await request("ui/message", { role: "user", content: [{ type: "text", text }] });
    if (result.isError) throw new Error("ChatGPT could not complete this request. Try again.");
    return result;
  }
  // Signed picture links last about a day and carry their own end time (direction pictures: t={..e: ms}; previews: token={..expires: s}).
  // A card shown again after that draws no dead picture: it reads fresh links once, by itself (see resign; audit F12).
  let lapsedSeen = false;
  function lapsed(url) {
    try {
      const token = (url.searchParams.get("t") || url.searchParams.get("token") || "").split(".")[0];
      const body = JSON.parse(atob(token.replace(/-/g, "+").replace(/_/g, "/")));
      const ends = typeof body.e === "number" ? body.e : body.expires * 1000;
      return ends < Date.now() + 60000;
    } catch { return false; }
  }
  function safeUrl(value, image = false) {
    try {
      const url = new URL(value);
      if (url.origin !== "https://iter0.com" || url.username || url.password) return "";
      if (image && lapsed(url)) { lapsedSeen = true; return ""; }
      return (image ? (url.pathname === "/api/mcp/preview" || url.pathname === "/api/mcp/direction-image") : url.pathname === "/build" || url.pathname === "/delivery") ? url.href : "";
    } catch { return ""; }
  }
  const icon = (id, cls = "") => `<svg class="i ${cls}" aria-hidden="true"><use href="#${id}"/></svg>`;
  function shot(url, title) {
    const src = safeUrl(url, true);
    return src ? `<div class="thumb"><img src="${esc(src)}" alt="Preview of ${esc(title)}"></div>` : `<div class="thumb shim"></div>`;
  }
  const button = (action, text, value = "", { ghost = false, glyph = "" } = {}) => `<button class="btn${ghost ? " ghost" : ""}" data-action="${action}" data-value="${esc(value)}">${glyph ? icon(glyph) : ""}${esc(text)}</button>`;
  let toast;
  let feedbackBar = "builder-bar";
  function placeFeedback() {
    const bar = document.getElementById(feedbackBar) || document.getElementById("builder-bar");
    if (bar) bar.insertAdjacentElement?.("afterend", feedback);
    else if (!isBuilder()) feedbackHome?.appendChild?.(feedback);
    else app.appendChild?.(feedback);
    if (feedbackBar === "add-page-row" && feedback.textContent && feedback.parentElement === bar?.parentElement) {
      const sidebar = bar.parentElement, bounds = sidebar.getBoundingClientRect();
      const top = bounds.top + sidebar.clientTop, bottom = top + sidebar.clientHeight;
      const row = bar.getBoundingClientRect(), status = feedback.getBoundingClientRect();
      if (status.bottom > bottom) sidebar.scrollTop += status.bottom - bottom;
      else if (row.top < top) sidebar.scrollTop += row.top - top;
    }
  }
  function say(text, bar = "builder-bar", persistent = false) {
    feedback.textContent = text;
    clearTimeout(toast);
    feedbackBar = bar;
    placeFeedback();
    if (isBuilder() && text && !persistent) toast = setTimeout(() => { feedback.textContent = ""; }, 4000);
  }
  function fail(error) { say(error instanceof Error ? error.message : "This action is unavailable. Try again.", feedbackBar, Boolean(output.batchId)); }
  function toolErrorText(result) {
    return result.content?.find(item => item.type === "text" && typeof item.text === "string" && item.text.trim())?.text
      || "This request is unavailable. Check the response in chat or try again.";
  }
  async function toolResult(name, args) {
    const response = await request("tools/call", { name, arguments: args, _meta: { "iter0/card": true } });
    const result = response?.mcp_tool_result || response?.call_tool_result || response;
    if (!result || (name === "iter0_confirm_paid_action" && !result.isError
      && !result.structuredContent?.runId && !result.structuredContent?.batchId && !delivered(result.structuredContent))) {
      const blocked = new Error("ChatGPT has not started this action.");
      blocked.hostRefusal = true; throw blocked;
    }
    if (result.isError) {
      const failure = new Error(result.structuredContent?.code === "out_of_credits"
        ? "Not enough credits for this."
        : result.structuredContent?.code === "invalid_quote" ? "This confirmation has expired or is unavailable. Ask for this action again."
        : toolErrorText(result));
      failure.code = result.structuredContent?.code;
      // The sign-in has lapsed (the server's OAuth challenge): reading again cannot work until the person signs in.
      failure.signedOut = Boolean(result._meta?.["mcp/www_authenticate"]) || /^Sign in to your iter0 account/.test(toolErrorText(result));
      // A status the server gives with its error (a run it no longer has, or one that failed) is its last word on that run.
      const status = result.structuredContent?.status;
      if (typeof status === "string" && status !== "running") failure.final = result.structuredContent;
      throw failure;
    }
    // Some compatibility hosts return public content from callTool and keep
    // widget metadata only in their canonical globals. Match the public quote
    // before using that metadata; an older direction's quote cannot fill it.
    if (!result._meta?.paidAction && result.structuredContent?.confirmation?.quoteId) {
      const metadata = window.openai?.toolResponseMetadata;
      const candidate = metadata?.mcp_tool_result?._meta || metadata?.call_tool_result?._meta || metadata;
      if (candidate?.paidAction?.quoteId === result.structuredContent.confirmation.quoteId) {
        return { ...result, _meta: { ...result._meta, ...candidate } };
      }
    }
    return result;
  }
  async function tool(name, args) {
    const result = await toolResult(name, args);
    return withPageCode(result.structuredContent || {}, result._meta);
  }
  function theme() {
    document.documentElement.dataset.theme = host.theme === "dark" ? "dark" : "light";
    document.documentElement.dataset.mode = host.displayMode || "inline";
    if (waitCard) waitCard.feed({ ...output, theme: host.theme === "dark" ? "dark" : "light" });
    Object.entries(host.styles?.variables || {}).forEach(([key, value]) => {
      if (/^--[a-z0-9-]+$/i.test(key) && typeof value === "string") document.documentElement.style.setProperty(key, value);
    });
  }
  let progressInFlight = false;
  // R1-07: a correction that ended unfinished (polishIncomplete) is not still polishing.
  const isPolishing = value => value?.polishing === true && value.polishIncomplete !== true;
  // SIT-393: a finished build whose one correction is still running keeps checking, so the corrected page replaces
  // the first one by itself.
  // The card's health (hardening audit, 14 Oct). halted: "boot" (ChatGPT never connected), "crash" (the card's own code failed),
  // "stale" (past the age limit) or "signin" (the sign-in lapsed); each shows one message with its next step and stops reading.
  // failures: progress reads that failed in a row.
  let halted = "", failures = 0, progressError = "", followKey = "", followSince = 0;
  const following = () => !halted && (output.status === "running" || (output.status === "done" && isPolishing(output) && Boolean(output.runId) && !output.batchId));
  // A build ends within about 13 minutes. Past 30 (by the server's elapsed time, or by how long this card has watched) it is not coming
  // back on its own: the card stops reading and says so (incident 2: "in progress" 10 hours later, read every second).
  const AGE_LIMIT = 1800000;
  function halt(kind) { halted = kind; clearTimeout(timer); timer = null; render(); }
  // mode: "" a timed check; "manual" the person asked (its error shows at once); "quiet" the card's own one-off read (fresh links,
  // or the work a reloaded card remembers). The last two read even when the card is not following the run.
  async function refreshProgress(mode = "") {
    if (stopped || progressInFlight || !(mode || following())) return;
    const current = output, key = current.batchId || current.runId;
    if (key !== followKey) { followKey = key; followSince = Date.now(); }
    progressInFlight = true;
    let next, error;
    try {
      next = current.batchId ? await tool("iter0_get_design_set_status", { batchId: current.batchId })
        : await tool("iter0_get_site_status", mode === "manual" ? { runId: current.runId } : { runId: current.runId, waitCursor });
    } catch (caught) { error = caught; }
    progressInFlight = false;
    if (output === current && !stopped) {
      if (!error) {
        // A good read clears what a failed one said (incident 14 Oct: one refused read during the move to fullscreen left
        // "ChatGPT could not complete this request" on a working card for good).
        failures = 0;
        if (progressError && feedback.textContent === progressError) say("", feedbackBar);
        progressError = "";
        // "disconnected": iter0's connection in ChatGPT was removed, so the server answers the card's reads without the run.
        if (next.status === "disconnected") halt("signin"); else apply(next);
      } else if (error.signedOut) halt("signin");
      else if (error.final) apply({ ...(current.batchId ? { batchId: current.batchId } : { runId: current.runId }), ...error.final });
      // One refused or slow read is tried again quietly; the third in a row (or one the person asked for) is shown.
      else if (++failures >= 3 || mode === "manual") { progressError = error.message; fail(error); }
      if (following() && Math.max(Date.now() - followSince, (output.progress?.elapsedSeconds || 0) * 1000) > AGE_LIMIT) halt("stale");
    }
    if (!timer) poll();
  }
  function poll(immediate = false) {
    if (stopped || !following()) { clearTimeout(timer); timer = null; return; }
    // After failed reads the card waits longer (2 s, 5 s, then every 15 s), and a host nudge does not cut that short.
    if (immediate && !failures) { clearTimeout(timer); timer = null; void refreshProgress(); return; }
    // Repeated host results must not keep postponing the next progress read.
    if (timer) return;
    timer = setTimeout(() => { timer = null; void refreshProgress(); },
      Math.max(output.runId && !output.batchId && output.status === "running" ? 1000 : 5000, [0, 2000, 5000, 15000][Math.min(failures, 3)]));
  }
  const when = value => { const d = new Date(value); return Number.isNaN(d.getTime()) ? "" : d.toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" }); };
  const stamp = value => { const d = new Date(value); return Number.isNaN(d.getTime()) ? "" : d.toLocaleString(undefined, { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }); };
  const plural = (n, word) => `${n} ${word}${n === 1 ? "" : word.endsWith("h") ? "es" : "s"}`;
  const stateText = { running: "Still working. This view checks progress every few seconds.", stopped: "Check the response in chat for recovery and refund details." };

  // Research team: the same rows and wording as the builder's research card.
  function monogram(hostName) {
    const name = String(hostName).replace(/^www\./, "");
    return `<span class="mono" title="${esc(name)}">${esc((name.match(/[a-z0-9]/i) || ["?"])[0].toUpperCase())}</span>`;
  }
  const hostStack = (hosts, max, extra = true) => hosts?.length ? `<span class="hosts" aria-hidden="true">${hosts.slice(0, max).map(monogram).join("")}${extra && hosts.length > max ? `<em>+${hosts.length - max}</em>` : ""}</span>` : "";
  function researchCounts(r) {
    const parts = [];
    if (r.sources) parts.push(`read ${plural(r.sources, "source")}`);
    if (r.searches) parts.push(`ran ${plural(r.searches, "search")}`);
    return parts.join(" · ");
  }
  function renderResearch(r) {
    if (!r || !Array.isArray(r.researchers) || !r.researchers.length) return "";
    const live = r.status === "running", open = researchOpen ?? live, counts = researchCounts(r);
    const allHosts = [...new Set(r.researchers.flatMap(x => x.hosts || []))];
    // A run that stopped or failed is never worded as finished.
    const ending = r.status === "stopped" ? "Research stopped" : r.status === "failed" ? "Research couldn't finish" : "Research finished";
    const headline = live ? "Your CEO is researching" : `${ending}${counts ? ` · ${counts}` : ""}`;
    return `<section class="rt${open ? " open" : ""}" aria-label="Research team"><button class="rt-h" data-action="research" aria-expanded="${open}">${hostStack(allHosts, 3, false)}<span class="rt-t">${esc(headline)}</span>${icon(open ? "chev-d" : "chev-r")}</button>${open ? `<div class="rt-b">${live && counts ? `<div class="rt-p">${hostStack(allHosts, 4)}<span>${esc(counts[0].toUpperCase() + counts.slice(1))} so far</span></div>` : ""}<ul>${r.researchers.map(x =>
      `<li class="rt-r"><span class="av">${icon(`av-${x.id}`)}</span><span class="rt-n"><b>${esc(x.name)}</b><span>${esc(x.activity || (x.state === "working" ? "Working…" : x.state === "reported" ? "Reported" : "Waiting"))}</span></span>${hostStack(x.hosts, 3)}</li>`).join("")}</ul></div>` : ""}</section>`;
  }
  function renderThree() {
    const research = renderResearch(output.research);
    if (output.status === "done") {
      app.innerHTML = `<div class="head"><div><h1>Three directions</h1><p>Pick one to build.</p></div></div>${research}<div class="set" role="list">${(output.directions || []).map((d, i) =>
        `<article class="card" role="listitem">${shot(d.screenshotUrl || d.previewImageUrl, d.title).replace(/<\/div>$/, `<span class="tag">Design ${"ABC"[i] || i + 1}</span><button class="zoom" data-action="zoom" aria-expanded="false" aria-label="See Design ${"ABC"[i] || i + 1} larger">${icon("fit")}</button></div>`)}<div class="body"><h2 class="name">${esc(d.title)}</h2><div id="paid-build-${i}" class="paid-action">${button("build", "Build this direction", d.directionId)}</div><div id="paid-build-${i}-requote" class="requote"></div></div></article>`).join("")}</div>`;
      if (window.iter0PaidConfirm) void hydrateBuildPills(output);
    } else if (output.status === "running") {
      app.innerHTML = `<div class="head"><div><h1>Working on three designs</h1><p>${stateText.running}</p></div><span class="status warn">Working</span></div>${research}<div class="set" aria-hidden="true">${[0, 1, 2].map(() =>
        `<article class="card skel"><div class="thumb"><div class="shim"></div></div><div class="body"><div class="ln shim" style="width:60%"></div><div class="ln shim" style="height:36px;border-radius:999px"></div></div></article>`).join("")}</div><div class="foot">${button("refresh", "Check progress", "", { ghost: true, glyph: "refresh" })}</div>`;
    } else {
      app.innerHTML = `<section class="msg"><span class="ic bad">${icon("alert")}</span><div><h1>The designs stopped</h1><p>${stateText.stopped}</p></div>${button("refresh", "Check progress", "", { ghost: true })}</section>`;
    }
  }
  function renderBuild() {
    if (output.status === "running") {
      if (!waitCard || waitRun !== output.runId) {
        waitCard?.destroy(); waitRun = output.runId; waitCursor = 0;
        app.innerHTML = `<section class="build-wait-host" aria-label="Building your website"></section><div class="build-wait-footer"><p class="bw-status" id="bw-status" aria-hidden="true"></p><span class="sr-only" id="bw-phase" aria-live="polite"></span>${button("refresh", "Check progress", "", { ghost: true, glyph: "refresh" })}</div>`;
        waitCard = window.iter0MountBuildWait(app.firstElementChild, { ...output, theme: host.theme === "dark" ? "dark" : "light" });
      } else waitCard.feed({ ...output, theme: host.theme === "dark" ? "dark" : "light" });
      // SIT-486: the card's own words for what the build is doing, outside the animation's frame, so the panel always says
      // something true even before (or without) the animation drawing.
      // Screen readers hear the stage when it changes, not the clock on every progress read (PR 662 review).
      const line = document.getElementById("bw-status"), phase = document.getElementById("bw-phase"), layer = app.querySelector?.(".bw-l-stage");
      if (line) line.textContent = buildStage(output);
      if (layer) layer.textContent = buildStage(output, false);
      if (phase && phase.textContent !== buildStage(output, false)) phase.textContent = buildStage(output, false);
      if (Number.isSafeInteger(output.buildWait?.cursor)) waitCursor = Math.max(waitCursor, output.buildWait.cursor);
      return;
    }
    // Ready only when there is something to open: a finished status with no design and no link is still being delivered (V01).
    const running = output.status === "running", done = output.status === "done", ready = done && Boolean(output.designId || safeUrl(output.url));
    const label = running ? ["warn", "Building"] : ready ? ["ok", "Ready"] : done ? ["warn", "Finishing"] : ["bad", "Stopped"];
    const chip = `<span class="status ${label[0]}">${label[1]}</span>`;
    if (!running && !done) {
      const refund = { refunded: "Your credit was refunded.", pending: "Your refund is pending.", not_charged: "No credit was charged.", uncertain: "Your credit charge is still being checked." }[output.refundState] || stateText.stopped;
      app.innerHTML = `<section class="bs"><div class="top"><div><h1>Your website</h1></div>${chip}</div><div class="fail"><span class="ic">${icon("alert")}</span><div><h2>The build stopped</h2><p>${esc(refund)}</p>${button("refresh", "Check progress", "", { ghost: true })}</div></div></section>`;
      return;
    }
    // SIT-486 (John, 16 Oct, on the card after a build: "this section is also very bad"): a finished build is one compact card in the
    // chat (picture, one line, Open the builder); the builder itself only ever draws full screen.
    const image = done ? safeUrl(output.previewImageUrl, true) : "";
    const builder = done && output.designId ? button("open-builder", "Open the builder", output.designId) : "";
    const open = done && safeUrl(output.url) ? button("open", "Open in iter0", output.url, { ghost: true, glyph: "ext" }) : "";
    compactCard({ title: ready && isPolishing(output) ? "Polishing your website" : ready ? "Your site is ready" : "Your site is still being finished", chip,
      sub: ready && isPolishing(output) ? "It's ready to open. The last fixes land by themselves." : ready ? "A draft only you can see until you publish." : "It can't be opened yet. Check again in a moment.",
      image, alt: "Preview of your website", actions: `${builder}${open || button("refresh", "Check progress", "", { ghost: true })}`,
      after: output.research ? `<div class="bs-rt">${renderResearch(output.research)}</div>` : "" });
  }
  // What a running build is doing, in the card's own words (the server's stage: building, then checking and fixing, then saving).
  function buildStage(value, clock = true) {
    const elapsed = Number.isSafeInteger(value.progress?.elapsedSeconds) ? value.progress.elapsedSeconds : null;
    const stage = value.progress?.stage;
    const words = stage === "checking" ? "Your page is written. Now checking and fixing it" : stage === "saving" ? "Saving your page" : elapsed === null ? "Starting your build" : "Building your website";
    return elapsed === null || !clock ? words : `${words} · ${Math.floor(elapsed / 60)}m ${elapsed % 60}s`;
  }
  // One compact card for a finished result in the chat: a picture on the left, a title, one line and its buttons.
  function compactCard({ title, sub, chip = "", image, alt, actions, after = "" }) {
    app.innerHTML = `<section class="bs done cmp"><div class="cmp-row"><div class="shot cmp-shot">${PAGE_OUTLINE}${image ? `<img src="${esc(image)}" alt="${esc(alt)}">` : ""}</div>`
      + `<div class="cmp-tx"><div class="cmp-h"><h1>${esc(title)}</h1>${chip}</div><p>${esc(sub)}</p><div class="acts">${actions}</div></div></div>${after}</section>`;
    fadeInShot();
  }
  // The builder needs the whole screen. In the chat (inline, or a host that has not said) a design or the Projects list is a compact card.
  const fullscreen = () => host.displayMode === "fullscreen";
  function renderCompactBuilder() {
    const d = output.design;
    if (d) {
      const editing = lastEdit?.designId === d.designId ? lastEdit : null;
      const undo = editing && !editing.undone && editing.undoToken ? button("undo-edit", editing.busy ? "Undoing…" : "Undo", "", { ghost: true }) : "";
      const open = safeUrl(d.url) ? button("open", "Open in iter0", d.url, { ghost: true, glyph: "ext" }) : "";
      compactCard({ title: d.name || "Your website", image: safeUrl(editing?.image || d.previewImageUrl, true), alt: `Preview of ${d.name || "your website"}`,
        sub: editing ? (editing.undone ? "Edit undone. Your page is back to how it was." : "Edit saved to your page.") : `Saved design${when(d.updatedAt) ? ` · edited ${when(d.updatedAt)}` : ""}`,
        actions: `${button("expand", "Open the builder")}${undo}${open}` });
      return;
    }
    const designs = (Array.isArray(output.designs) ? output.designs : library?.designs || []).slice(0, 3);
    app.innerHTML = `<section class="bs done cmp"><div class="cmp-tx cmp-list"><div class="cmp-h"><h1>Your iter0 projects</h1></div>`
      + (designs.length ? `<ul>${designs.map(x => `<li><span class="cmp-mini">${safeUrl(x.previewImageUrl, true) ? `<img src="${esc(safeUrl(x.previewImageUrl, true))}" alt="">` : ""}</span><span><b>${esc(x.name)}</b><span>Edited ${esc(when(x.updatedAt))}</span></span></li>`).join("")}</ul>` : `<p>${Array.isArray(output.designs) ? "No designs yet. Describe your website in the chat to start one." : "Loading your projects…"}</p>`)
      + `<div class="acts">${button("expand", "Open your projects")}${button("open", "Open in iter0", "https://iter0.com/build?pane=projects", { ghost: true, glyph: "ext" })}</div></div></section>`;
  }
  // SIT-386: the finished picture fades in over the page outline instead of flashing white while it loads.
  function fadeInShot() {
    const shot = app.querySelector?.(".shot img");
    if (shot) { const shown = () => shot.classList.add("ld"); if (shot.complete && shot.naturalWidth) shown(); else shot.addEventListener("load", shown); }
  }
  const PAGE_OUTLINE = `<div class="wire" aria-hidden="true"><div class="nav"><i class="shim" style="width:18%;height:12px"></i><i class="shim" style="width:34%"></i></div><i class="shim" style="width:62%;height:26px"></i><i class="shim" style="width:42%;height:26px"></i><i class="shim" style="width:50%;height:10px;margin-top:6px"></i><div class="cards"><i class="shim"></i><i class="shim"></i><i class="shim"></i></div></div>`;
  // John, 12 Oct 2026 ("yes"): a paid edit of a saved design is saved as its current page, with Undo. SIT-386 fix 2:
  // iter0 keeps the page the edit replaced, so the card holds only the signed receipt (undoToken); no page travels in
  // either direction, and Undo shows whenever a saved edit comes with a receipt.
  // John, 12 Oct 2026 ("Shouldn't it open in the iter0 builder rather than having this extra UX" / "Yes"): after the
  // confirm tap the card goes fullscreen and becomes the builder, like MagicPath. A build shows the approved wait
  // animation there and opens the design when done; an edit opens the design with an "Edit saved · Undo" bar. The
  // inline result cards below remain only for hosts that refuse fullscreen.
  let lastEdit = null, openOnResult = false, buildOrigin = null;
  // SIT-486: only an edit goes full screen at its confirm tap. A build stays in the card that started it: that card holds the paid call,
  // its progress reads and what ChatGPT is told, and ChatGPT moving it full screen at the same moment left a blank panel (16 Oct dry run).
  // When the build is done its compact card offers Open the builder.
  function requestBuilderFor(quote) {
    if (isBuilder() || quote?.name !== "iter0_edit_site") return;
    // Asked inside the confirm tap, so hosts that require a user gesture for fullscreen allow it.
    void request("ui/request-display-mode", { mode: "fullscreen" }).then(mode => {
      if (mode?.mode !== "fullscreen") return;
      host.displayMode = "fullscreen"; openOnResult = true; theme(); openBuilderForResult();
    }).catch(() => {});
  }
  function openBuilderForResult() {
    // An edit that was not saved stays on its card, which shows why; the builder would show the unchanged page.
    const ready = isEditResult() ? output.saved === true : output.status === "done";
    if (!openOnResult || isBuilder() || host.displayMode !== "fullscreen" || !output.designId || !ready) return;
    openOnResult = false; builderOpen = true;
    void openDesign(output.designId).catch(error => { builderOpen = surface === "builder"; render(); fail(error); });
  }
  function editBanner(d) {
    if (lastEdit?.designId !== d.designId) return "";
    const undo = !lastEdit.undone ? `<button class="zb" data-action="undo-edit">${lastEdit.busy ? "Undoing…" : "Undo"}</button>` : "";
    return `<div class="vbar" id="edit-bar" role="status">${icon("check")}<span>${lastEdit.undone ? "Edit undone. Your page is back to how it was." : "Edit saved to your page."}</span>${undo}</div>`;
  }
  // A paid edit's result carries `saved` (true or false); a finished build's status can also carry html and a designId.
  function isEditResult() { return output.edited === true || (typeof output.html === "string" && typeof output.saved === "boolean"); }
  function renderEdited() {
    const edit = lastEdit && output.undoToken && lastEdit.undoToken === output.undoToken ? lastEdit : { busy: false, undone: false, image: "" };
    const saved = output.saved === true, undone = edit.undone;
    const chip = !saved ? `<span class="status warn">Not saved</span>` : undone ? `<span class="status warn">Undone</span>` : `<span class="status ok">Saved</span>`;
    const title = !saved ? "Edit ready" : undone ? "Edit undone" : "Edit saved";
    const sub = !saved ? output.saveNote || "The edit is ready in chat." : undone ? "Your page is back to how it was before this edit" : "Your page now has this change";
    const image = saved ? safeUrl(edit.image || output.previewImageUrl, true) : "";
    const undo = saved && !undone && output.undoToken
      ? button("undo-edit", edit.busy ? "Undoing…" : "Undo", "", { ghost: true }) : "";
    // Not saved: the paid edit is still shown, drawn from its HTML with scripts off, so the person sees what they got.
    const shot = saved ? `${PAGE_OUTLINE}${image ? `<img src="${esc(image)}" alt="Preview of your page">` : ""}`
      : `${PAGE_OUTLINE}${typeof output.html === "string" ? `<iframe class="draft" sandbox="" title="The edited page, not saved" srcdoc="${esc(output.html)}"></iframe>` : ""}`;
    app.innerHTML = `<section class="bs done"><div class="top"><div><h1>${title}</h1><p>${esc(sub)}</p></div>${chip}</div>`
      + `<div class="pv"><div class="frame"><div class="chrome"><b></b><b></b><b></b><span>${saved ? "iter0.com" : "Edited page · not saved"}</span></div><div class="shot">${shot}</div></div></div>`
      + `<div class="res"><p>${saved ? "A draft only you can see until you publish." : "Scroll the preview to see the whole edit. Your saved page is unchanged."}</p><div class="acts">${undo}${button("open-builder", saved ? "Open the builder" : "Open your saved page", output.designId)}</div></div></section>`;
    const draft = app.querySelector("iframe.draft");
    if (draft) {
      // Scaled to the card's width and as tall as the preview, so the whole edited page scrolls inside it.
      const box = draft.parentElement, scale = box.clientWidth / DESKTOP_W;
      draft.style.transform = `scale(${scale})`; draft.style.height = `${Math.ceil(box.clientHeight / scale)}px`;
    }
    fadeInShot();
  }
  async function undoEdit() {
    const edit = lastEdit;
    if (!edit || edit.busy || edit.undone) return;
    edit.busy = true; render();
    try {
      const result = await tool("iter0_undo_edit", { designId: edit.designId, undoToken: edit.undoToken });
      edit.undone = true; edit.image = result.previewImageUrl || "";
      void request("ui/update-model-context", { structuredContent: { designId: edit.designId, editUndone: true },
        content: [{ type: "text", text: "The person undid the last edit. The design is back to the page from before that edit." }] }).catch(() => {});
      // In the builder, reload the design so the preview shows the restored page.
      if (isBuilder() && output.design?.designId === edit.designId) await openDesign(edit.designId);
    } finally { edit.busy = false; render(); }
  }
  // Projects area (SIT-376). The shell paints before the host's tool result arrives; then one page of
  // cards at a time (SIT-386, John 13 Oct: "lets just use a page system"), Previous / Next below. The host's
  // result is read page 1 and 2; the page after the one on screen is read ahead with the read-only list tool
  // (cursor + page-size limit), so Next is nearly always instant. Thumbnails load lazily, so only the cards on
  // screen request an image. Searches call the same tool and update only the grid, never the typed draft.
  // mode: "" sends the founder's words as they are; "show3" or "build" is the action picked in the + menu (its chip).
  const PAGE = 6;
  const projects = { draft: "", mode: "", plus: false, search: "", loading: false, page: 0, seq: 0 };
  // The read in flight (one at a time), the cursor of the last read that failed, and the cards kept as DOM nodes (see projectCard).
  let chunk = null, failed = "", freshNode = null, noneNode = null;
  const cardNodes = new Map(), skeletonNodes = new Map();
  const projectModes = { show3: { label: "Show 3 designs", glyph: "sparkle" }, build: { label: "Build one site", glyph: "layers" } };
  const starters = ["A café or restaurant", "A trades business", "A clinic or studio", "A product launch"];
  // John, 12 Oct 2026: "Let's sharpen your website / What are we building, John?". A founder with projects is
  // sharpening a site they have; a new founder is starting one.
  function greeting() {
    const name = library?.firstName;
    if (library?.designs?.length && !projects.search) return name ? `Let's sharpen your website, ${name}` : "Let's sharpen your website";
    return name ? `What are we building, ${name}?` : "What are we building?";
  }
  // The homepage composer's typed examples (src/lib/marketing/story-copy.ts TYPED_PROMPTS / PHONE_TYPED_PROMPTS and
  // the timing in src/components/marketing/typed-placeholder.ts). They only ever change the placeholder, never the
  // draft, and stop while the field is focused or has text; reduced motion shows the first example as a still.
  const typedPrompts = ["We build an AI tool that answers support tickets. Sharpen my pitch.", "Here is my site. What would a stranger skip?", "Show me three designs for my SaaS launch.", "Add a Features page in the same style."];
  const phoneTypedPrompts = ["Sharpen my AI support tool pitch.", "What would strangers skip on my site?", "Show three designs for my SaaS.", "Add a Features page in this style."];
  const typed = { timer: 0, index: 0, length: 0, erasing: false };
  function typePlaceholder() {
    clearTimeout(typed.timer);
    const field = document.getElementById("pj-draft");
    if (!field) return;
    const prompts = window.matchMedia?.("(max-width: 639px)").matches ? phoneTypedPrompts : typedPrompts;
    const idle = () => document.activeElement !== field && !field.value;
    if (window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) { if (idle()) field.placeholder = prompts[0]; return; }
    const step = () => {
      const current = document.getElementById("pj-draft");
      if (!current) return;
      if (document.activeElement === current || current.value) { current.placeholder = "Describe your website or product"; return; }
      const prompt = prompts[typed.index % prompts.length];
      let delay;
      if (!typed.erasing) {
        typed.length = Math.min(typed.length + 1, prompt.length);
        typed.erasing = typed.length >= prompt.length;
        delay = typed.erasing ? 1700 : 45;
      } else if (typed.length > 1) { typed.length--; delay = 18; }
      else { typed.length = 0; typed.erasing = false; typed.index = (typed.index + 1) % prompts.length; delay = 350; }
      current.placeholder = prompt.slice(0, typed.length);
      typed.timer = setTimeout(step, delay);
    };
    if (idle()) typed.timer = setTimeout(step, typed.length ? 45 : 900);
  }
  const ago = value => {
    const t = new Date(value).getTime();
    if (Number.isNaN(t)) return "";
    const minutes = Math.round((Date.now() - t) / 60000), format = new Intl.RelativeTimeFormat(undefined, { numeric: "auto" });
    if (Math.abs(minutes) < 60) return format.format(-Math.max(1, minutes), "minute");
    if (Math.abs(minutes) < 1440) return format.format(-Math.round(minutes / 60), "hour");
    if (Math.abs(minutes) < 1440 * 30) return format.format(-Math.round(minutes / 1440), "day");
    return when(value);
  };
  function projectCard(d) {
    const src = safeUrl(d.previewImageUrl, true);
    return `<li class="pj-card"><button class="pj-shot" data-action="design" data-value="${esc(d.designId)}" aria-label="Open ${esc(d.name)}">${src ? `<img src="${esc(src)}" alt="" loading="lazy" decoding="async">` : ""}</button><div class="pj-meta"><div><h3 title="${esc(d.name)}">${esc(d.name)}</h3><p>Edited ${esc(ago(d.updatedAt))}</p></div><button class="ib" data-action="show3again" data-value="${esc(d.designId)}" aria-label="Show 3 new designs like ${esc(d.name)}" title="Show 3 new designs like this">${icon("sparkle")}</button></div></li>`;
  }
  // The list shows PAGE projects at a time. Cards and skeleton cards are built once and kept as DOM nodes, and showing a page moves
  // them in and out of the grid, so a message that changes nothing on screen (the host sending the list again, tool-input, a theme
  // change) touches nothing: no skeleton animation restarts and no picture is requested twice. A card is rebuilt only when its
  // design changed.
  const skeletonHtml = `<li class="pj-card pj-skel" aria-hidden="true"><div class="pj-shot"></div><div class="pj-meta"><div><h3><i style="width:62%"></i></h3><p><i style="width:38%"></i></p></div><span class="ib" aria-hidden="true"></span></div></li>`;
  const freshHtml = `<li class="pj-card pj-fresh"><button class="pj-shot pj-new" data-action="new-site" aria-label="New website">${icon("plus")}<span class="pj-new-t" aria-hidden="true">New website</span></button><div class="pj-meta"><div><h3>New website</h3><p>Describe it above</p></div></div></li>`;
  function parseNodes(html) {
    const holder = document.createElement("template");
    holder.innerHTML = html;
    return [...holder.content.children];
  }
  function freshCard() {
    if (!freshNode) freshNode = parseNodes(freshHtml)[0];
    return freshNode;
  }
  function noneCard() {
    if (noneNode?.query !== projects.search) noneNode = { query: projects.search, node: parseNodes(`<li class="pj-none" role="status"><span>No projects match “${esc(projects.search)}”.</span>${button("clear-search", "Clear search", "", { ghost: true })}</li>`)[0] };
    return noneNode.node;
  }
  function cardFor(d) {
    const src = safeUrl(d.previewImageUrl, true);
    // Name, time and whether there is a picture rebuild the card. A refreshed picture link (a new signed address for the same
    // preview) only changes the picture's address: the card and its picture element stay, and the browser keeps showing the
    // current picture until the new one has loaded.
    const sig = `${d.name}\u0001${d.updatedAt}\u0001${src ? "picture" : "none"}`;
    let kept = cardNodes.get(d.designId);
    if (kept?.sig !== sig) {
      kept = { sig, src, node: parseNodes(projectCard(d))[0] };
      cardNodes.set(d.designId, kept);
    } else if (kept.src !== src) {
      const image = kept.node.querySelector?.(".pj-shot img");
      if (image) image.src = src;
      kept.src = src;
    }
    // "Edited 5 minutes ago" moves on by itself; the card, and the picture in it, stay.
    const note = kept.node.querySelector?.(".pj-meta p"), edited = `Edited ${ago(d.updatedAt)}`;
    if (note && note.textContent !== edited) note.textContent = edited;
    return kept.node;
  }
  function keepCards() {
    const ids = new Set((library?.designs || []).map(d => d.designId));
    for (const id of [...cardNodes.keys()]) if (!ids.has(id)) cardNodes.delete(id);
  }
  function skeletons(count) {
    if (!skeletonNodes.has(count)) skeletonNodes.set(count, Array.from({ length: count }, () => parseNodes(skeletonHtml)[0]));
    return skeletonNodes.get(count);
  }
  // "New website" takes the first place on page 1 (not in a search), so page 1 shows one project fewer.
  const firstSize = () => projects.search ? PAGE : PAGE - 1;
  const pageStart = i => i === 0 ? 0 : firstSize() + (i - 1) * PAGE;
  const pageEnd = i => pageStart(i) + (i === 0 ? firstSize() : PAGE);
  const pagesFor = count => count <= firstSize() ? 1 : 1 + Math.ceil((count - firstSize()) / PAGE);
  const readDesigns = () => library?.designs || [];
  // A page can be shown once its cards are read, or when the list has no more to read.
  const pageReady = i => !library?.nextCursor || readDesigns().length >= pageEnd(i);
  function lastReadyPage() {
    let i = projects.page;
    while (i > 0 && !pageReady(i)) i--;
    return i;
  }
  function pageTotal() {
    if (!library) return null;
    if (!library.nextCursor) return pagesFor(readDesigns().length);
    return Number.isInteger(library.total) ? Math.max(pagesFor(library.total), projects.page + 2) : null;
  }
  const canPrev = () => !projects.loading && projects.page > 0;
  const canNext = () => !projects.loading && Boolean(library) && pageReady(projects.page) && (readDesigns().length > pageEnd(projects.page) || Boolean(library.nextCursor));
  function pageNodes(i) {
    const designs = readDesigns().slice(pageStart(i), pageEnd(i));
    if (!designs.length && projects.search) return [noneCard()];
    return [...(i === 0 && !projects.search ? [freshCard()] : []), ...designs.map(cardFor)];
  }
  // Skeleton cards have the size of the cards that replace them: the page's own count once the total is known.
  function waitingNodes(i) {
    const left = !projects.loading && Number.isInteger(library?.total) ? Math.max(1, library.total - pageStart(i)) : Infinity;
    return [...(i === 0 && !projects.search ? [freshCard()] : []), ...skeletons(Math.min(i === 0 ? firstSize() : PAGE, left))];
  }
  // Moves only what differs, so cards that stay are never touched.
  function syncChildren(parent, nodes) {
    nodes.forEach((node, k) => { if (parent.children[k] !== node) parent.insertBefore(node, parent.children[k] || null); });
    while (parent.children.length > nodes.length) parent.lastElementChild.remove();
  }
  function renderGrid() {
    const grid = document.getElementById("pj-grid");
    if (!grid) return;
    const waiting = !library || projects.loading || !pageReady(projects.page);
    grid.setAttribute?.("aria-busy", String(waiting));
    syncChildren(grid, waiting ? waitingNodes(projects.page) : pageNodes(projects.page));
    // A picture that came from the cache has already loaded: show it now rather than waiting for an event that will not come.
    grid.querySelectorAll?.(".pj-shot img").forEach(image => { if (image.complete && image.naturalWidth) image.classList.add("ld"); });
    renderPager();
    pump();
  }
  function renderPager() {
    const pager = document.getElementById("pj-pager");
    if (!pager) return;
    const total = pageTotal(), text = total ? `Page ${projects.page + 1} of ${total}` : `Page ${projects.page + 1}`;
    pager.hidden = !library || projects.loading || total === 1;
    const label = document.getElementById("pj-page"), prev = document.getElementById("pj-prev"), next = document.getElementById("pj-next");
    if (label && label.textContent !== text) label.textContent = text;
    if (prev) prev.disabled = !canPrev();
    if (next) next.disabled = !canNext();
  }
  function renderLibrary() {
    if (Array.isArray(output.designs) && output !== library) adoptList(output);
    // The page is already on screen: bring its few changing parts up to date and leave the rest, cards included, alone.
    if (document.getElementById("pj")) { syncShell(); renderGrid(); return; }
    const typing = document.activeElement?.id;
    const caret = typing === "pj-draft" || typing === "pj-search" ? [document.activeElement.selectionStart, document.activeElement.selectionEnd] : null;
    app.innerHTML = `<header class="bar pj-top" id="builder-bar"><div class="pj-crumb"><svg class="i pj-logo" aria-hidden="true"><use href="#mark"/></svg><span>iter0</span>${icon("chev-r")}<b>Projects</b></div><span class="spacer"></span><button class="tb" data-action="open" data-value="https://iter0.com/build?pane=projects" aria-label="Open iter0 in a new tab">${icon("ext")}<span class="hide-sm">Open iter0</span></button></header>
<div class="pj" id="pj"><div class="pj-in"><div class="pj-hello"><h1 id="pj-title">${esc(greeting())}</h1></div>
<div class="pj-ask" id="pj-ask" data-composer=""><textarea id="pj-draft" rows="1" maxlength="2000" aria-label="Describe your website" placeholder="Describe your website or product">${esc(projects.draft)}</textarea><div class="pj-tools" data-composer-toolbar=""><span class="pj-plus"><button class="pj-ib" id="pj-plus" data-action="plus" aria-label="Add and more tools" aria-haspopup="menu" aria-expanded="${projects.plus}" aria-controls="pj-menu">${icon("plus")}</button><div class="pj-menu" id="pj-menu" role="menu" aria-label="Add and more tools"${projects.plus ? "" : " hidden"}>${Object.entries(projectModes).map(([value, m]) => `<button class="pj-mi" role="menuitemradio" data-action="pick" data-value="${value}" aria-checked="${projects.mode === value}">${icon(m.glyph)}<span>${m.label}</span><svg class="i ck" aria-hidden="true"><use href="#check"/></svg></button>`).join("")}</div></span><span id="pj-chip" class="pj-chip-slot">${chipHtml()}</span><span class="spacer"></span><button class="pj-send" id="pj-send" data-action="send" aria-label="${projects.mode ? `${projectModes[projects.mode].label}: send to ChatGPT` : "Send to ChatGPT"}"${projects.draft.trim() ? "" : " disabled"}>${icon("arrow-up")}</button></div></div>
<p class="pj-free" id="pj-free"${library?.firstSiteFree ? "" : " hidden"}>Your first site is free.</p><div class="pj-starts">${starters.map(s => `<button class="pj-start" data-action="starter" data-value="${esc(s)}">${esc(s)}${icon("arrow-ur")}</button>`).join("")}</div>
<div class="pj-head" id="pj-head"><h2>Your projects</h2><span class="spacer"></span><label class="pj-find"><span class="sr-only">Search projects</span>${icon("search")}<input id="pj-search" type="search" maxlength="80" autocomplete="off" placeholder="Search projects…" value="${esc(projects.search)}"></label><button class="ib" data-action="refresh" aria-label="Refresh projects">${icon("refresh")}</button></div>
<ul class="pj-grid" id="pj-grid" aria-label="Your projects"></ul>
<nav class="pj-pager" id="pj-pager" aria-label="Projects pages" hidden><button class="btn ghost" id="pj-prev" data-action="page-prev" aria-label="Previous page" disabled>${icon("chev-l")}Previous</button><span class="pj-page" id="pj-page" role="status"></span><button class="btn ghost" id="pj-next" data-action="page-next" aria-label="Next page" disabled>Next${icon("chev-r")}</button></nav></div></div>`;
    renderGrid();
    if (caret) {
      const field = document.getElementById(typing), end = field?.value.length ?? 0;
      field?.focus(); field?.setSelectionRange?.(Math.min(caret[0] ?? end, end), Math.min(caret[1] ?? end, end));
    }
    document.getElementById("pj-draft")?.addEventListener("blur", typePlaceholder);
    typePlaceholder();
  }
  // What the person sees of the page heading changes in place; the composer, the search box and the grid are not rebuilt.
  function syncShell() {
    const title = document.getElementById("pj-title"), text = greeting();
    if (title && title.textContent !== text) title.textContent = text;
    const free = document.getElementById("pj-free");
    if (free) free.hidden = !library?.firstSiteFree;
    const field = document.getElementById("pj-search");
    if (field && document.activeElement !== field && field.value !== projects.search) field.value = projects.search;
  }
  // A list the host sent. ChatGPT sends its result again on tool-input, a theme change and so on: a copy of the list it sent last is a
  // replay and changes nothing at all, not the cards, and not a search or read in flight (review R1-01). Only the last list counts: a
  // list that matches an older one but not the last one is a new answer. A list that differs is the host's newer answer and replaces
  // what was read: rows, cursor and total (R1-02), and the person starts again at page 1. Two cases keep the person's place: a list
  // that only reaches further than the one they are reading, and fresher rows (names, times, new signed picture links) for the start
  // of a list that was read further, which are folded into the rows already read (R1-03).
  let hostList = "";
  // The two lists name the same projects in the same order as far as the shorter one goes.
  const sameStart = (a, b) => a.slice(0, b.length).every((d, k) => d.designId === b[k].designId);
  function adoptList(next) {
    const signature = JSON.stringify(next);
    if (library && signature === hostList) { output = library; return; }
    hostList = signature;
    const have = readDesigns(), got = next.designs, query = next.query || "";
    const reading = Boolean(library) && !projects.loading && query === projects.search && sameStart(have, got);
    const totalMoved = Number.isInteger(next.total) && Number.isInteger(library?.total) && next.total !== library.total;
    if (reading && got.length > 0 && got.length < have.length && next.nextCursor && !totalMoved) {
      library = { ...library, firstName: next.firstName, firstSiteFree: next.firstSiteFree, creditBalance: next.creditBalance,
        ...(Number.isInteger(next.total) ? { total: next.total } : {}), designs: have.map((d, k) => got[k] || d) };
      output = library;
      return;
    }
    const continues = reading && got.length >= have.length;
    // The read in flight stays valid only when the list still ends at the cursor it is reading from.
    const sameRead = continues && (next.nextCursor ?? null) === (library.nextCursor ?? null);
    library = next; projects.search = query; projects.loading = false;
    if (!sameRead) { projects.seq++; chunk = null; failed = ""; }
    if (!continues) projects.page = 0;
    keepCards();
  }
  // Reads happen in the background, one at a time, a page ahead of the person: the list tool with the cursor and a page-size limit.
  // A newer search or list makes every older read stale (the seq), and a stale answer changes nothing.
  function loadChunk() {
    if (chunk) return chunk.done;
    const cursor = library?.nextCursor;
    if (!cursor || projects.loading) return Promise.resolve(false);
    const seq = projects.seq, query = projects.search, job = { done: null };
    chunk = job;
    job.done = (async () => {
      try {
        const next = await tool("iter0_list_my_designs", { cursor, limit: PAGE, ...(query ? { query } : {}) });
        if (seq !== projects.seq) return false;
        if (!Array.isArray(next.designs)) throw new Error("The next page could not be loaded. Try again.");
        const known = new Set(library.designs.map(d => d.designId));
        setLibrary({ ...library, designs: [...library.designs, ...next.designs.filter(d => !known.has(d.designId))], nextCursor: next.nextCursor ?? null });
        failed = "";
        return true;
      } catch (error) {
        if (seq !== projects.seq) return false;
        failed = cursor;
        throw error;
      } finally {
        if (chunk === job) chunk = null;
      }
    })();
    return job.done;
  }
  function setLibrary(next) {
    library = next;
    if (Array.isArray(output.designs)) output = library;
  }
  // Starts the read the list needs: the page the person is waiting for, or else the page after the one they are on.
  function pump() {
    if (!library || projects.loading || chunk || !library.nextCursor || failed === library.nextCursor) return;
    if (pageReady(projects.page) && readDesigns().length >= pageEnd(projects.page + 1)) return;
    loadChunk().then(() => renderGrid(), () => {
      // A read nobody was waiting for fails quietly; a page the person asked for puts them back on the page they were on.
      if (!pageReady(projects.page) && document.getElementById("pj-grid")) {
        projects.page = lastReadyPage();
        say("The next page could not be loaded. Try again.");
      }
      renderGrid();
    });
  }
  function scrollToList() {
    const head = document.getElementById("pj-head"), box = head?.getBoundingClientRect?.();
    if (box && box.top < 0) head.scrollIntoView?.({ block: "start" });
  }
  async function showPage(i) {
    if (!library || projects.loading || i < 0 || i === projects.page || (i > projects.page && !canNext())) return;
    if (!pageReady(i)) failed = ""; // asking for the page again is a fresh try
    projects.page = i;
    renderGrid();
    scrollToList();
    if (chunk && !pageReady(i)) await chunk.done.catch(() => {});
  }
  // The button that was pressed is disabled while its action runs; keep the keyboard where it was, or on the other button at an end.
  function keepPagerFocus(control) {
    const wanted = control.disabled ? document.getElementById(control.id === "pj-next" ? "pj-prev" : "pj-next") : control;
    if (wanted && !wanted.disabled && document.activeElement !== wanted) wanted.focus?.({ preventScroll: true });
  }
  // Only the newest search may change the list or its loading state: older replies are ignored.
  async function listPage(args) {
    const seq = ++projects.seq;
    const current = () => seq === projects.seq;
    let next;
    try { next = await tool("iter0_list_my_designs", args); } catch (error) { return { current: current(), error }; }
    return { current: current(), next: Array.isArray(next.designs) ? next : null };
  }
  let searchTimer = null;
  async function search(text) {
    projects.search = text.trim().slice(0, 80);
    projects.loading = true; projects.page = 0; chunk = null; failed = "";
    renderGrid();
    const reply = await listPage({ ...(projects.search ? { query: projects.search } : {}), limit: PAGE });
    if (!reply.current) return;
    projects.loading = false;
    if (reply.error) { renderGrid(); throw reply.error; }
    if (reply.next) {
      const kept = library ? { firstName: library.firstName, creditBalance: library.creditBalance, firstSiteFree: library.firstSiteFree, pageSize: library.pageSize } : {};
      setLibrary({ ...kept, ...reply.next });
      keepCards();
    }
    renderGrid();
  }
  // The picked + action, as the site's removable chip beside the + button.
  function chipHtml() {
    const m = projectModes[projects.mode];
    return m ? `<span class="pj-chip" data-composer-inline-chip="${projects.mode}"><span>${m.label}</span><button class="pj-chip-x" data-action="clear-mode" aria-label="Remove ${m.label}">${icon("x")}</button></span>` : "";
  }
  function setPlus(open) {
    projects.plus = open;
    const menuBox = document.getElementById("pj-menu"), trigger = document.getElementById("pj-plus");
    if (menuBox) menuBox.hidden = !open;
    trigger?.setAttribute?.("aria-expanded", String(open));
  }
  function setMode(mode) {
    projects.mode = projectModes[mode] ? mode : "";
    const chip = document.getElementById("pj-chip");
    if (chip) chip.innerHTML = chipHtml();
    document.querySelectorAll?.(".pj-mi").forEach(item => item.setAttribute("aria-checked", String(item.dataset.value === projects.mode)));
    const send = document.getElementById("pj-send");
    send?.setAttribute?.("aria-label", projects.mode ? `${projectModes[projects.mode].label}: send to ChatGPT` : "Send to ChatGPT");
  }
  async function sendDraft() {
    const text = projects.draft.trim();
    if (!text) return;
    // Only words go to ChatGPT. With no + action picked, ChatGPT reads the founder's own words and decides what they want.
    const prompt = projects.mode === "build"
      ? `Build a website for this: ${text}\nQuote the credit price and check with me before starting.`
      : projects.mode === "show3"
        ? `Show me three website designs for this: ${text}\nCheck my brief with me and quote the credit price before starting.`
        : `${text}\nThis is for a website on iter0. Check my brief with me and quote any credit price before starting anything.`;
    const sent = projects.draft;
    await message(prompt);
    // Clear only what was sent: words typed while ChatGPT was acknowledging stay in the box.
    if (projects.draft === sent) {
      projects.draft = "";
      const field = document.getElementById("pj-draft");
      if (field) field.value = "";
      const send = document.getElementById("pj-send");
      if (send) send.disabled = true;
    }
    say("Sent to ChatGPT. It replies in the chat.");
  }

  // Builder data with fallbacks: one Home page and the saved version when the server sends no list.
  const pagesOf = () => output.pages?.length ? output.pages : [{ pageId: "home", title: "Home", route: "/" }];
  const versionsOf = () => output.versions?.length ? [...output.versions].sort((a, b) => b.number - a.number)
    : [{ versionId: "current", number: 1, createdAt: output.design?.updatedAt, current: true }];
  const currentVersion = () => versionsOf().find(v => v.current) || versionsOf()[0];
  const narrow = () => Boolean(window.matchMedia?.("(max-width:767px)").matches);
  // A full-page render can time out or its link can lapse. When the desktop one fails to load, the cached thumbnail takes its place once
  // per design before the card shows its placeholder (SIT-386: "Preview unavailable" on a design that was fine). The phone page is never
  // replaced by the desktop picture: it says it did not load and offers Try again.
  const previewFallbacks = new Set();
  // What has happened to each preview address: "loaded" (drawn once, so a redraw never flashes the loading state) or "failed".
  const previewDone = new Map(), previewRetries = new Map(), warmed = new Set();
  // Which page is on show instead of the design's own: an earlier version, or another page that has its own picture.
  const viewedVersion = () => versionView ? versionsOf().find(v => v.versionId === versionView) : null;
  const otherPage = () => { const p = pageView && pageView !== pagesOf()[0].pageId ? pagesOf().find(x => x.pageId === pageView) : null; return p?.previewImageUrl ? p : null; };
  // The person's choice (device) is never rewritten by a redraw. What is drawn follows it whenever a phone page exists for what is on show.
  const phoneReady = () => !viewedVersion() && !otherPage() && Boolean(safeUrl(output.design?.phonePreviewImageUrl, true));
  const deviceNow = () => device === "phone" && phoneReady() ? "phone" : "desktop";
  const previewKey = () => `${output.design?.designId}:${deviceNow()}`;
  function previewSource() {
    const d = output.design;
    const version = viewedVersion(), page = otherPage();
    const pick = (url, width, full) => {
      const base = safeUrl(url, true), tries = previewRetries.get(base);
      let src = base;
      if (base && tries) { const again = new URL(base); again.searchParams.set("retry", String(tries)); src = again.href; }
      return { src, base, width, full };
    };
    if (version && !version.current) return pick(version.previewImageUrl, THUMB_W, false);
    if (page) return pick(page.previewImageUrl, THUMB_W, false);
    if (deviceNow() === "phone") return pick(d.phonePreviewImageUrl, PHONE_W, true);
    if (previewFallbacks.has(previewKey())) return pick(d.previewImageUrl, THUMB_W, false);
    if (d.pagePreviewImageUrl) return pick(d.pagePreviewImageUrl, DESKTOP_W, true);
    return pick(d.previewImageUrl, THUMB_W, false);
  }
  // Drawn in the frame while a page is being made, and in its place if it could not be made. Calm, not blank white.
  function previewStateHtml(source) {
    const phone = source.width === PHONE_W, state = previewDone.get(source.src);
    if (state === "loaded") return "";
    if (state === "failed") return `<div class="pv-state failed" id="pv-state" role="status"><span>${phone ? "Phone preview" : "Preview"} didn't load</span>${button("retry-preview", "Try again")}</div>`;
    return `<div class="pv-state" id="pv-state" role="status" aria-live="polite"><span class="pv-dot" aria-hidden="true"></span><span>Loading ${phone ? "phone preview" : "preview"}…</span></div>`;
  }
  // The phone page is made on the server the first time it is asked for. Once the desktop page the person is looking at has drawn, ask
  // for it quietly, so the toggle finds it ready (one request per address; skipped on a data-saving connection).
  function warmPhonePreview() {
    if (!output.design || deviceNow() !== "desktop" || !phoneReady() || typeof Image !== "function") return;
    if (typeof navigator !== "undefined" && navigator.connection?.saveData) return;
    const src = safeUrl(output.design.phonePreviewImageUrl, true);
    if (!src || warmed.has(src) || previewDone.has(src)) return;
    warmed.add(src);
    new Image().src = src;
  }
  function menuHtml() {
    const d = output.design;
    if (menu === "versions") {
      const list = versionsOf(), only = list.length === 1;
      return `<div class="menu" role="menu" id="menu-versions"><div class="mh"><b>Versions</b><span>${plural(list.length, "version")}</span></div><div class="mlist">${list.map(v => {
        const viewing = versionView ? versionView === v.versionId : Boolean(v.current);
        return `<button class="mrow${viewing ? " on" : ""}" role="menuitemradio" aria-checked="${viewing}" data-action="version" data-value="${esc(v.versionId)}"><span class="vn">v${esc(v.number)}</span><span class="mt"><b>${esc(v.note || (v.current ? "Saved design" : `Version ${v.number}`))}</b><span>${esc(stamp(v.createdAt))}${v.current ? " · Current" : ""}</span></span>${viewing ? icon("check") : ""}</button>`;
      }).join("")}</div>${only ? `<p class="mnote">Earlier versions appear here after each change you make in ChatGPT.</p>` : `<p class="mnote">Pick a version to review it. Restoring always checks with you first.</p>`}</div>`;
    }
    if (menu === "publish") {
      // Each choice names its task in the link (iter0 does not read task= yet; it opens the design as before, V06).
      const base = String(d.url ?? ""), url = task => esc(`${base}${base.includes("?") ? "&" : "?"}task=${task}`);
      return `<div class="menu wide" role="menu" id="menu-publish"><div class="mh"><b>Publish</b><span>Finishes in iter0</span></div>
<button class="mrow" role="menuitem" data-action="open" data-value="${url("share")}">${icon("link")}<span class="mt"><b>Share a preview link</b><span>Anyone with the link can view this design</span></span>${icon("ext", "mx")}</button>
<button class="mrow" role="menuitem" data-action="open" data-value="${url("domain")}">${icon("globe")}<span class="mt"><b>Put it on your domain</b><span>Connect a domain and go live</span></span>${icon("ext", "mx")}</button>
<button class="mrow" role="menuitem" data-action="open" data-value="https://iter0.com/delivery">${icon("branch")}<span class="mt"><b>Send to GitHub</b><span>Connect a repository for a PR preview</span></span>${icon("ext", "mx")}</button>
<div class="msep"></div>
<button class="mrow" role="menuitem" data-action="open" data-value="${url("download")}">${icon("download")}<span class="mt"><b>Download HTML</b><span>Export the page from iter0</span></span>${icon("ext", "mx")}</button></div>`;
    }
    return "";
  }
  // The unsent Add-page description belongs to one design; another design starts empty.
  function draftText() { return addPageDraft.designId === output.design?.designId ? addPageDraft.text : ""; }
  function closeAddPage() {
    addingPage = false; addPageDraft = { designId: null, text: "" }; render();
    document.getElementById("add-page-row")?.focus();
  }
  function renderDesign() {
    const d = output.design, sections = output.sections || [], list = library?.designs || [];
    if (sideFold === null) sideFold = narrow();
    const version = viewedVersion();
    // First draw only: pick a starting device. After that `device` is the person's choice and nothing here rewrites it; a page with no
    // phone picture (an earlier version, another page, a read without a phone link) simply draws desktop and keeps the choice.
    const phoneOk = phoneReady();
    if (device === null && phoneOk) device = narrow() ? "phone" : "desktop";
    const showing = deviceNow();
    const pages = pagesOf(), activePage = pageView || pages[0].pageId;
    const chosen = !version && sections.find(s => s.sectionId === selected);
    const cur = currentVersion();
    const source = previewSource();
    const thumb = x => safeUrl(x.previewImageUrl, true) ? `<img src="${esc(safeUrl(x.previewImageUrl, true))}" alt="">` : "";
    const seg = `<div class="seg" role="radiogroup" aria-label="Preview size"><button id="dev-desktop" class="sg" role="radio" aria-checked="${showing === "desktop"}" data-action="device" data-value="desktop" aria-label="Desktop preview" title="Desktop">${icon("monitor")}</button><button id="dev-phone" class="sg" role="radio" aria-checked="${showing === "phone"}" data-action="device" data-value="phone" aria-label="Phone preview" title="${phoneOk ? "Phone" : "Phone preview is not ready for this design"}"${phoneOk ? "" : " disabled"}>${icon("phone")}</button></div>`;
    const versionBanner = version && !version.current ? `<div class="vbar" id="version-bar" role="status">${icon("clock")}<span>${source.src ? "Viewing" : "Selected"} version ${esc(version.number)}${version.createdAt ? ` · ${esc(stamp(version.createdAt))}` : ""}</span><button class="zb" data-action="version" data-value="${esc(cur.versionId)}">Back to current</button><button class="tb dark sm" data-action="restore" data-value="${esc(version.versionId)}">Restore this version</button></div>` : "";
    const typingPage = document.activeElement?.id === "add-page-input";
    const caret = typingPage ? [document.activeElement.selectionStart, document.activeElement.selectionEnd] : null;
    app.innerHTML = `<header class="bar" id="builder-bar"><button class="tb fill" data-action="library" aria-label="Projects">${icon("chev-l")}<span class="hide-sm">Projects</span></button><span class="sep hide-sm"></span><div class="name"><b>${esc(d.name)}</b><span class="st hide-sm">Saved</span></div><span class="spacer"></span>${seg}<span class="mwrap"><button id="opener-versions" class="tb${menu === "versions" ? " on" : ""}" data-action="menu" data-value="versions" aria-haspopup="menu" aria-expanded="${menu === "versions"}" aria-label="Versions">${icon("clock")}<span class="hide-sm">Version ${esc((version || cur).number)}</span>${icon("chev-d", "hide-sm")}</button>${menu === "versions" ? menuHtml() : ""}</span><button class="ib hide-sm" data-action="refresh" aria-label="Refresh preview">${icon("refresh")}</button><button class="ib hide-sm" data-action="open" data-value="${esc(d.url)}" aria-label="Open in iter0">${icon("ext")}</button><span class="mwrap"><button id="opener-publish" class="tb dark" data-action="menu" data-value="publish" aria-haspopup="menu" aria-expanded="${menu === "publish"}" aria-label="Publish">${icon("upload")}<span class="hide-sm">Publish</span></button>${menu === "publish" ? menuHtml() : ""}</span></header>
<div class="main"><aside class="side${sideFold ? " fold" : ""}" id="side" aria-label="Pages and sections"><div class="sb-head" id="pages-bar"><h2>Pages</h2><button class="ib" data-action="side" aria-label="Show or hide the sidebar" aria-expanded="${!sideFold}">${icon("chev-l", "fold-ic")}</button></div><div class="sb-body">${output.research ? `<div class="sb-rt">${renderResearch(output.research)}</div>` : ""}${pages.map((p, i) =>
      `<button class="row" data-action="page" data-value="${esc(p.pageId)}"${p.pageId === activePage ? ' aria-current="true"' : ""}>${icon(i === 0 ? "home" : "file")}<span class="t">${esc(p.title)}</span><span class="p">${esc(p.route)}</span></button>`).join("")}
${addingPage ? `<div class="addpg" id="add-page-row" data-form="add-page"><label for="add-page-input">What is the new page for?</label><input id="add-page-input" name="purpose" maxlength="240" autocomplete="off" placeholder="e.g. Pricing, with 3 plans and FAQs" value="${esc(draftText())}"><div class="addpg-acts"><button type="button" class="tb" data-action="add-page-cancel">Cancel</button><button type="button" class="tb dark" id="add-page-submit" data-action="add-page-send"${draftText().trim() && !addPageSending ? "" : " disabled"}>${addPageSending ? "Sending…" : "Add page"}</button></div></div>` : `<button class="row add" id="add-page-row" data-action="add-page" title="Describe a new page and ChatGPT adds it">${icon("plus")}<span class="t">Add a page</span></button>`}
<div class="lbl"><span>Sections</span><span>${sections.length}</span></div>${sections.length ? sections.map(s => `<button class="row" aria-pressed="${!version && selected === s.sectionId}" data-action="section" data-value="${esc(s.sectionId)}"${version ? " disabled" : selected === s.sectionId ? ' aria-current="true"' : ""}>${icon("select")}<span class="t">${esc(s.label || "Section")}</span></button>`).join("") : `<p class="lbl">No sections found</p>`}
${list.length ? `<div class="lbl"><span>Projects</span><span>${list.length}</span></div>${list.map(x => `<button class="dir" data-action="design" data-value="${esc(x.designId)}"${x.designId === d.designId ? ' aria-current="true"' : ""}><span class="im">${thumb(x)}</span><span class="tx"><b>${esc(x.name)}</b><span>${x.designId === d.designId ? "Open now" : `Updated ${esc(when(x.updatedAt))}`}</span></span></button>`).join("")}` : ""}</div>
<div class="side-foot"><button class="tb fill" data-action="show3" data-value="">${icon("sparkle")}<span>Show me 3 new designs</span></button></div></aside>
<section class="canvas${version && !version.current ? " viewing" : ""}" id="canvas" aria-label="Design preview">${versionBanner || (version ? "" : editBanner(d))}<div class="scroller" id="scroller"><div class="board" id="board"><div class="fr${source.width === PHONE_W ? " phone" : ""}" id="preview-frame"><div class="fl"><span class="pl">${icon(source.width === PHONE_W ? "phone" : "monitor")}</span><span class="fn">${esc(pages.find(p => p.pageId === activePage)?.title || d.name)}</span><span class="sub">${version && !version.current ? `Version ${esc(version.number)}` : source.width === PHONE_W ? "Phone 390" : `Desktop ${source.width}`}</span></div><div class="fb" id="preview-box"><div class="in" id="preview-image">${source.src ? `${previewDone.get(source.src) === "failed" ? "" : `<img id="preview-img" src="${esc(source.src)}" alt="Preview of ${esc(d.name)}">`}${previewStateHtml(source)}` : `<p class="preview-unavailable" role="status">${version ? `Preview unavailable for version ${esc(version.number)}` : "Preview unavailable"}</p>`}<div class="hl hover" id="hl-hover" hidden></div><div class="hl" id="hl-sel" hidden><span class="hl-tag" id="hl-tag"></span></div></div></div></div></div></div>
${version ? "" : chosen ? `<div class="chipdock"><span class="c">${icon("select")}<span>${esc(chosen.label || "Section")}</span></span><button class="tb ask-change" data-action="ask-change" aria-label="Ask ChatGPT to change this">Ask ChatGPT<span class="hide-sm"> to change this</span></button><button class="zb x" data-action="unselect" aria-label="Clear the selected section">${icon("x")}</button></div>` : `<div class="chipdock idle">${icon("select")}<span class="h" id="idle-hint">${idleHint()}</span></div>`}
<div class="zoombar"><div class="pill zoom" aria-label="Zoom"><button class="zb" data-action="zoom-out" aria-label="Zoom out">${icon("minus")}</button><span id="zoom-value"></span><button class="zb" data-action="zoom-in" aria-label="Zoom in">${icon("plus")}</button></div><div class="pill fit"><button class="zb" data-action="fit" title="Fit the page to the screen">${icon("fit")}<span>Fit</span></button></div></div></section></div>`;
    if (typingPage) {
      const field = document.getElementById("add-page-input"), end = field?.value.length ?? 0;
      field?.focus(); field?.setSelectionRange?.(Math.min(caret[0] ?? end, end), Math.min(caret[1] ?? end, end));
    }
    const img = document.getElementById("preview-img");
    img?.addEventListener("load", () => { fitPreview(); paintHighlight(); });
    fitPreview();
    void measureSections().then(() => paintHighlight());
    // A section already chosen (picked from the list, or restored with the card) is outlined, so it needs the page's layout too.
    if (selected !== null && !version) void requestLayout();
  }

  // Section geometry: lay the saved page out once per width in a script-free sandboxed frame (no scripts run,
  // nothing is shown) and read the same top-level header/section/footer boxes the server turns into section IDs.
  // The cache key is the design, the width and a hash of the exact page (two different edits can have the same length).
  const measured = new Map(), measuring = new Map();
  let hashed = { html: null, hash: "" };
  function contentHash(html) {
    if (hashed.html === html) return hashed.hash;
    let h1 = 0xdeadbeef, h2 = 0x41c6ce57;
    for (let i = 0; i < html.length; i++) { const c = html.charCodeAt(i); h1 = Math.imul(h1 ^ c, 2654435761); h2 = Math.imul(h2 ^ c, 1597334677); }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    hashed = { html, hash: (h2 >>> 0).toString(16).padStart(8, "0") + (h1 >>> 0).toString(16).padStart(8, "0") };
    return hashed.hash;
  }
  const measureWidth = () => deviceNow() === "phone" ? PHONE_W : DESKTOP_W;
  const geometryKey = () => { const html = pageHtml(); return `${output.design?.designId}:${measureWidth()}:${html.length}:${contentHash(html)}`; };
  function measureSections() {
    const key = geometryKey(), width = measureWidth(), html = pageHtml();
    if (measured.has(key)) { boxes = measured.get(key); return Promise.resolve(); }
    // Never paint the previous page's rectangles over this one while it is still being measured.
    boxes = null;
    if (!html || typeof document.createElement !== "function") return Promise.resolve();
    if (measuring.has(key)) return measuring.get(key);
    let settled = false;
    const task = new Promise(resolve => {
      const frame = document.createElement("iframe");
      frame.setAttribute("sandbox", "allow-same-origin");
      frame.setAttribute("aria-hidden", "true"); frame.tabIndex = -1;
      frame.style.cssText = `position:fixed;left:-20000px;top:0;width:${width}px;height:${width === PHONE_W ? PHONE_VH : DESKTOP_VH}px;border:0;visibility:hidden;pointer-events:none`;
      // A measurement is kept for the page it measured. It is shown only if that page is still the one on screen:
      // a late result for an earlier page or width must not assign boxes to the current output.
      const done = value => {
        settled = true; measuring.delete(key);
        if (value) { measured.set(key, value); if (measured.size > 24) measured.delete(measured.keys().next().value); }
        if (key === geometryKey()) boxes = value;
        frame.remove(); resolve();
      };
      const timeout = setTimeout(() => done(null), 4000);
      frame.addEventListener("load", () => {
        clearTimeout(timeout);
        try {
          const doc = frame.contentDocument, height = doc.documentElement.scrollHeight;
          const all = Array.from(doc.querySelectorAll("header,section,footer")).filter(el => !el.parentElement?.closest("header,section,footer")).slice(0, 50);
          const list = all.length ? all : [doc.body];
          done({ height, rects: list.map(el => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top + frame.contentWindow.scrollY, w: r.width, h: r.height }; }) });
        } catch { done(null); }
      });
      frame.srcdoc = html.replace(/<script\b[\s\S]*?<\/script>/gi, "");
      document.body.appendChild(frame);
    });
    if (!settled) measuring.set(key, task);
    return task;
  }
  // Lazy section outlines (SIT-386, John 13 Oct: "that should only happen when you click the page or click edit"). Opening a design
  // sends no page, so it opens fast. The first time the person points at the preview or picks a section, the card asks once for a
  // light copy of the page (iter0_design_layout: images and scripts removed, natural sizes kept, in widget-only metadata) and measures
  // it as above. A copy is kept per design and save, so another design, or the same one after an edit, asks again. A failure or a page
  // that is too large draws no outlines, says nothing, and leaves the section list as the way in; opening the design again retries.
  const layouts = new Map();
  let pointer = null;
  const layoutKey = () => `${output.design?.designId}:${output.design?.updatedAt}`;
  const pageHtml = () => typeof output.currentHtml === "string" ? output.currentHtml : layouts.get(layoutKey())?.html || "";
  const layoutWanted = () => isBuilder() && Boolean(output.design) && !versionView && typeof output.currentHtml !== "string" && Boolean(output.sections?.length);
  function idleHint() {
    const known = typeof output.currentHtml === "string" ? null : layouts.get(layoutKey());
    return known && (known.state === "none" || known.state === "failed")
      ? "Pick a section in the list, then describe the change in ChatGPT."
      : "Click a section on the page, then describe the change in ChatGPT.";
  }
  function requestLayout() {
    if (!layoutWanted()) return Promise.resolve();
    const key = layoutKey(), known = layouts.get(key);
    if (known) return known.task || Promise.resolve();
    const designId = output.design.designId, entry = { state: "loading" };
    layouts.set(key, entry);
    if (layouts.size > 8) layouts.delete(layouts.keys().next().value);
    document.getElementById("preview-image")?.setAttribute?.("aria-busy", "true");
    entry.task = (async () => {
      try {
        const result = await toolResult("iter0_design_layout", { designId });
        const html = result._meta?.layoutHtml;
        if (result.structuredContent?.layout === "ready" && typeof html === "string" && html) Object.assign(entry, { state: "ready", html });
        else entry.state = "none";
      } catch { entry.state = "failed"; }
      // The person may have moved to another design while this was on its way; the copy is kept for when they come back.
      if (key !== layoutKey()) return;
      if (entry.state === "ready") await measureSections();
      if (key !== layoutKey()) return;
      document.getElementById("preview-image")?.removeAttribute?.("aria-busy");
      const hint = document.getElementById("idle-hint");
      if (hint) hint.textContent = idleHint();
      if (entry.state !== "ready") return;
      // Wherever the pointer already is gets its outline as soon as the page is measured.
      if (pointer && !versionView) { const index = sectionAt(pointer); hover = index >= 0 ? index : null; }
      paintHighlight();
    })();
    return entry.task;
  }
  function boxFor(index, pageHeight) {
    // The fallback thumbnail shows only the top of the page, so section boxes measured on the whole page would land on the
    // wrong section. Pick sections from the side list while it shows.
    if (previewFallbacks.has(previewKey()) && previewSource().src === safeUrl(output.design?.previewImageUrl, true)) return null;
    const rect = boxes?.rects?.[index];
    if (!rect) return null;
    const k = boxes.height ? pageHeight / boxes.height : 1;
    return { x: rect.x, y: rect.y * k, w: rect.w, h: rect.h * k };
  }
  function placeBox(el, box) {
    if (!el) return;
    if (!box) { el.hidden = true; return; }
    Object.assign(el.style, { left: `${box.x}px`, top: `${box.y}px`, width: `${box.w}px`, height: `${box.h}px` });
    el.hidden = false;
  }
  function paintHighlight(scroll = false) {
    if (!output.design || !document.getElementById("hl-sel")) return;
    const sections = output.sections || [], page = pageSize();
    const index = sections.findIndex(s => s.sectionId === selected);
    const box = index >= 0 && !versionView ? boxFor(index, page.height) : null;
    placeBox(document.getElementById("hl-sel"), box && box.y < page.height ? box : null);
    document.getElementById("hl-tag").textContent = index >= 0 ? sections[index].label || "Section" : "";
    const hoverBox = !versionView && hover !== null && hover !== index ? boxFor(hover, page.height) : null;
    placeBox(document.getElementById("hl-hover"), hoverBox && hoverBox.y < page.height ? hoverBox : null);
    if (scroll && box) {
      const scroller = document.getElementById("scroller"), scale = fitPreview();
      scroller?.scrollTo?.({ top: Math.max(0, box.y * scale - 40), behavior: "smooth" });
    }
  }
  function sectionAt(event) {
    const inner = document.getElementById("preview-image");
    if (!inner || !boxes) return -1;
    const page = pageSize(), rect = inner.getBoundingClientRect(), scale = rect.width / page.width;
    const x = (event.clientX - rect.left) / scale, y = (event.clientY - rect.top) / scale;
    let best = -1, area = Infinity;
    (output.sections || []).forEach((_, i) => {
      const b = boxFor(i, page.height);
      if (b && x >= b.x && x <= b.x + b.w && y >= b.y && y <= b.y + b.h && b.w * b.h < area) { best = i; area = b.w * b.h; }
    });
    return best;
  }
  function pageSize() {
    const img = document.getElementById("preview-img"), source = output.design ? previewSource() : { width: DESKTOP_W, full: false };
    const width = source.width;
    if (source.full && img?.naturalWidth) return { width, height: Math.round(img.naturalHeight * width / img.naturalWidth) };
    return { width, height: width === PHONE_W ? PHONE_VH : 800 };
  }
  // What each paid action does, in the founder's words. The brief under it comes from the quote.
  const PAID_COPY = {
    iter0_create_site: ["Build your website", "A finished page you can edit and publish."],
    iter0_edit_site: ["Edit your page", "Only this change. Everything else stays as it is."],
    iter0_show_three: ["Three design directions", "Three different looks to compare before you build."],
  };  let waitCard = null, waitRun = null, waitCursor = 0, cancelled = false;
  // One message in place of the card, in the card's own message style, with its one next step.
  const NOTICES = {
    boot: ["alert", "This card didn't load", "ChatGPT didn't connect to iter0. Reload the card, or carry on in chat.", "reload", "Reload card"],
    crash: ["alert", "Something went wrong in this card", "Reload the card, or carry on in chat.", "reload", "Reload card"],
    stale: ["clock", "{whose} taking longer than usual", "The card has stopped checking. Check again, or ask ChatGPT how it's going.", "refresh", "Check progress"],
    signin: ["info", "Sign in to iter0 again", "Your iter0 sign-in has expired. Ask ChatGPT to check {what}, and it will ask you to sign in.", "refresh", "Check progress"],
    error: ["alert", "This request didn't finish", "Check the response in chat.", "", ""],
  };
  function notice(kind, said = "") {
    const words = { whose: output.batchId ? "Your designs are" : "Your website is", what: output.batchId ? "these designs" : "this build" };
    const [glyph, title, text, action, label] = NOTICES[kind].map(part => part.replace(/\{(whose|what)\}/, (_, key) => words[key]));
    document.documentElement.dataset.view = "show-three"; document.documentElement.dataset.builder = "false"; app.className = "wrap";
    app.innerHTML = `<section class="msg" role="alert"><span class="ic${glyph === "alert" ? " bad" : ""}">${icon(glyph)}</span><div><h1>${title}</h1><p>${esc(said) || text}</p></div>${action ? button(action, label, "", { ghost: true }) : ""}</section>`;
    feedback.textContent = "";
  }
  // The host's first result was an error: said in the card, not as one line under an empty card (audit F2).
  let hostFailure = "";
  function hostError(result) {
    hostFailure = toolErrorText(result);
    if (!Object.keys(output).length && !isBuilder()) render(); else fail(new Error(hostFailure));
  }
  // A display-mode change while a paid action is in flight waits for its result: redrawing then would remount the price button as a
  // live-looking "Confirm" during the paid call (PR 662 review, S-P2). The result, or the failure, draws the new mode.
  function renderForMode() { if (confirmingPaid) modeRenderDue = true; else render(); }
  function render() {
    modeRenderDue = false;
    if (waitCard && (halted || output.status !== "running" || !output.runId || output.batchId || output.approvalRequired)) {
      waitCard.destroy(); waitCard = null; waitRun = null; waitCursor = 0;
    }
    paidControls.splice(0).forEach(cleanup => cleanup());
    if (halted === "boot" || halted === "crash" || (halted && output.status === "running")) return notice(halted);
    if (hostFailure && !isBuilder() && !cancelled && !Object.keys(output).length) return notice("error", hostFailure);
    const proposals = output.approvalRequired && paidAction?.name === "iter0_show_three" ? proposedDirections || paidAction.arguments?.directions : null;
    const builderView = !(proposals || cancelled || output.approvalRequired || (output.html && !output.designId && !output.runId) || delivered(output) || output.batchId || output.runId) && isBuilder();
    const compact = builderView && !fullscreen() && !output.code;
    const view = proposals || cancelled ? "show-three" : output.approvalRequired || (output.html && !output.designId && !output.runId) ? "quote" : delivered(output) ? "build-status" : output.batchId ? "show-three" : output.runId ? "build-status" : compact ? "build-status" : isBuilder() ? "builder" : "quote";
    document.documentElement.dataset.view = view;
    document.documentElement.dataset.builder = String(view === "builder");
    restorePresentation();
    app.className = view === "builder" ? output.design ? "app" : "lib" : view === "show-three" ? "wrap" : "";
    if (output.approvalRequired) {
      // SIT-386 (John, 12 Oct: "what iter0 card??" / "the UX is hard to see"): one clear card that says what
      // will happen, what it costs and that nothing is spent before the second tap. Consent mechanics are unchanged.
      const brief = (paidAction?.summary?.split("\n")[0] || "").replace(/^(Build|Edit|Show three):\s*/i, "");
      const [heading, lede] = PAID_COPY[paidAction?.name] || ["Confirm this action", ""];
      const spend = `${paidAction?.credits} credit${paidAction?.credits === 1 ? "" : "s"}`;
      const list = Array.isArray(proposals) ? `<div class="set proposed" role="list">${proposals.map(d =>
        `<article class="card" role="listitem"><div class="body"><h2 class="name">${esc(d.title)}</h2><p>${esc(d.direction)}</p></div></article>`).join("")}</div>` : "";
      app.innerHTML = `<section class="pay"><div class="pay-h"><div class="pay-t"><h1>${esc(heading)}</h1>${lede ? `<p class="pay-lede">${esc(lede)}</p>` : ""}</div></div>`
        + (brief && !list ? `<p class="pay-brief"><span>${esc(brief)}</span></p>` : "") + list
        + `<div class="pay-f"><p class="pay-note"><span class="n0">Nothing is spent until you confirm.</span><span class="n1">Tap again to spend ${esc(spend)}.</span><span class="n2">Starting…</span></p><div id="paid-confirm" class="paid-action"></div><div id="paid-confirm-requote" class="requote"></div></div></section>`;
      if (paidAction) mountPaidPill(document.getElementById("paid-confirm"), paidAction);
      else if (paidRequest) {
        const current = output, quote = paidRequest;
        void toolResult(quote.name, quote.arguments).then(result => { if (output === current) applyResult(result); }).catch(fail);
      } else say("Ask ChatGPT for this action again.");
    } else if (output.code === "out_of_credits") {
      app.innerHTML = "<p>Not enough credits for this.</p>";
    } else if (isEditResult() && output.designId) renderEdited();
    else if (output.html && !output.runId) app.innerHTML = "<p>The edit is ready in chat.</p>";
    else if (output.batchId) renderThree();
    else if (output.runId) renderBuild();
    else if (compact) renderCompactBuilder();
    else if (isBuilder() && output.design) renderDesign();
    else if (isBuilder() && (Array.isArray(output.designs) || !Object.keys(output).length)) renderLibrary();
    // A cancelled request is the end of that request: one message and one next step, never also "waiting" (V02).
    else app.innerHTML = cancelled ? `<section class="msg"><span class="ic bad">${icon("alert")}</span><div><h1>This request was cancelled</h1><p>Ask ChatGPT to try again.</p></div></section>` : "<p>Waiting for the result from ChatGPT.</p>";
    app.scrollTop = 0;
    placeFeedback();
    saveView();
    if (lapsedSeen) { lapsedSeen = false; resign(); }
  }
  // One quiet read for fresh picture links, at most every 10 minutes.
  let resignedAt = 0;
  function resign() {
    if (halted || stopped || Date.now() - resignedAt < 600000) return;
    resignedAt = Date.now();
    if (output.batchId || output.runId) void refreshProgress("quiet");
    else if (output.design) {
      // The same design with fresh links: the page, section and device on screen stay as they are.
      const id = output.design.designId;
      void tool("iter0_get_design", { designId: id }).then(next => { if (next.design && output.design?.designId === id) { output = next; hover = null; render(); } }).catch(() => {});
    } else if (isBuilder() && Array.isArray(output.designs)) void search(projects.search).catch(() => {});
  }
  function fitPreview() {
    const canvas = document.getElementById("canvas");
    if (!canvas || !document.getElementById("preview-frame")) return 1;
    const page = pageSize(), phone = page.width === PHONE_W;
    const fit = phone ? Math.min(1, (canvas.clientWidth - 32) / PHONE_W) : Math.max(0.1, Math.min(0.72, (canvas.clientWidth - 64) / page.width));
    const scale = zoom ?? fit;
    const width = Math.round(page.width * scale), height = Math.round(page.height * scale);
    document.getElementById("preview-frame").style.width = `${width}px`;
    Object.assign(document.getElementById("preview-box").style, { width: `${width}px`, height: `${height}px` });
    const inner = document.getElementById("preview-image");
    Object.assign(inner.style, { width: `${page.width}px`, height: `${page.height}px`, transform: `scale(${scale})` });
    inner.style.setProperty("--s", String(scale));
    document.getElementById("board").style.marginLeft = `${Math.max(16, (canvas.clientWidth - width) / 2)}px`;
    document.getElementById("zoom-value").textContent = `${Math.round(scale * 100)}%`;
    return scale;
  }
  function apply(value, meta = {}) {
    const quoteId = meta.paidAction?.quoteId || value.confirmation?.quoteId;
    if (Object.keys(value).length) { cancelled = false; if (halted === "boot") halted = ""; }
    if (value.approvalRequired && acceptedQuotes.has(quoteId)) return;
    if (!value.approvalRequired && (value.batchId || value.runId || delivered(value)) && paidAction?.quoteId) acceptedQuotes.add(paidAction.quoteId);
    // An identical set result changes nothing on screen, so it is not repainted. A completed set keeps its direction buttons'
    // quote mounts (including an in-flight hydration); a running set keeps its waiting cards, so a progress read neither
    // restarts their shimmer nor drops the hover under the pointer (John, 14 Oct: "the waiting black animation still flickers").
    const sameSet = output.batchId && value.batchId === output.batchId && JSON.stringify(value) === JSON.stringify(output)
      && JSON.stringify(meta.paidAction || null) === JSON.stringify(paidAction);
    if (sameSet) return;
    // SIT-393: an unchanged result while the page is polished keeps the painted preview (no flicker every poll).
    // Each read signs a fresh preview link; only its page version (v=) says whether the picture changed.
    const polishKey = v => JSON.stringify({ ...v, previewImageUrl: String(v.previewImageUrl || "").replace(/token=[^&]*/, "") });
    if (output.runId && output.status === "done" && isPolishing(output) && polishKey(value) === polishKey(output)) return;
    // Changed direction contents must obtain fresh quotes, even for the same ID.
    if (output.batchId || value.batchId) { directionQuoteGeneration++; directionQuotes.clear(); directionQuoteTasks.clear(); }
    // Hosts can resend the same result with new globals. Remounting its pill
    // would erase the already-painted Confirm before the second click.
    if (output.approvalRequired && value.approvalRequired && paidAction?.quoteId
      && meta.paidAction?.quoteId === paidAction.quoteId && JSON.stringify(meta.paidAction) === JSON.stringify(paidAction)) {
      output = value; paidRequest = meta.paidRequest || paidRequest; return;
    }
    if ((paidAction || confirmingPaid) && (value.runId || value.batchId || delivered(value) || value.code === "out_of_credits"
      || (value.approvalRequired && meta.paidAction?.quoteId !== paidAction?.quoteId))) say("");
    paidAction = meta.paidAction || null; paidRequest = meta.paidRequest || null;
    proposedDirections = meta.proposedDirections || null;
    // A saved edit gives the design a new updatedAt; the Projects list shows it as "Edited ..." without being read again.
    if (value.edited === true && value.saved === true && value.designId) freshenLibrary(value.designId, value.updatedAt);
    if (value.undoToken && value.designId && lastEdit?.undoToken !== value.undoToken) {
      lastEdit = { designId: value.designId, undoToken: value.undoToken, busy: false, undone: false, image: "" };
    } else if (!value.undoToken && value.edited === true && value.saved === true && lastEdit?.designId === value.designId) {
      // A newer saved edit of this design came back without a receipt (its earlier page could not be kept), and it replaced the
      // page the earlier receipt names, so that earlier Undo no longer applies. Do not keep offering it (review R1-03).
      lastEdit = null;
    }
    output = value; render(); poll();
    openBuilderForResult();
    if (value.batchId || value.runId) {
      const context = { ...(value.batchId ? { batchId: value.batchId } : { runId: value.runId }), status: value.status,
        ...(value.designId ? { designId: value.designId } : {}),
        ...(value.runId && value.status === "done" && safeUrl(value.url) ? { url: value.url } : {}),
        ...(Array.isArray(value.directions) ? { directions: value.directions.map(d => ({ directionId: d.directionId, title: d.title, direction: d.direction })) } : {}) };
      const identity = JSON.stringify(context);
      if (identity !== progressContext) {
        progressContext = identity;
        // SIT-486: after "Build this direction" ChatGPT still said the three designs were generating. The card now says in words what
        // the person started and where it stands, so ChatGPT's next reply knows.
        const started = value.runId && buildOrigin?.runId === value.runId ? ` from the direction "${buildOrigin.title}"` : "";
        const words = value.runId ? (value.status === "running" ? `The person confirmed a website build in the iter0 card${started}. It is running now (runId ${value.runId}); the card shows its progress and offers Open the builder when it is done. Do not start another build, and do not say earlier designs are still generating.`
            // Live re-test, 16 Oct: given only the designId, ChatGPT linked a generic iter0.com/builder and printed "Design ID: …". The
            // done context now carries the design's own link (the card's Open in iter0) and says never to show the designId.
            : value.status === "done" ? `The website build${started} is done.${safeUrl(value.url) ? ` Its link is ${value.url}. Give the person exactly this link when they ask for the site or its link; never make up another iter0 link.` : " The card shows it with Open the builder."} The designId is for iter0 tools only: never show it to the person. For a later status question, call iter0_get_design for the current link.` : `The website build${started} stopped. The card shows the refund state.`)
          : value.status === "running" ? "The three design directions are being prepared in the iter0 card." : value.status === "done" ? "The three design directions are ready in the iter0 card. The person can pick one there to build." : "";
        void request("ui/update-model-context", { structuredContent: context, ...(words ? { content: [{ type: "text", text: words }] } : {}) }).catch(() => {});
        remember(value);
      }
    } else if (value.edited === true && value.saved === true && value.designId) remember(value);
    const restoreId = restoreView?.designId;
    if (isBuilder() && Array.isArray(value.designs)) {
      if (!host["openai/deepLink"]?.url && restoreId) void openDesign(restoreId).catch(() => { restoreView = null; void deepLink().catch(fail); });
      else void deepLink().catch(fail);
    } else if (!isBuilder() && restoreId && host.displayMode === "fullscreen" && value.status === "done" && value.designId === restoreId) {
      builderOpen = true; void openDesign(restoreId).catch(fail);
    }
  }
  function applyResult(result) {
    const value = withPageCode(result.structuredContent || {}, result._meta), meta = result._meta || {};
    const quote = meta.paidAction, directionId = quote?.arguments?.directionId;
    // A host may notify the same quote separately from callTool's response.
    // Its price belongs in that direction's pill, not in a replacement card.
    if (!confirmingPaid && output.batchId && output.status === "done" && quote?.name === "iter0_create_site"
      && output.directions?.some(direction => direction.directionId === directionId)
      && (directionQuoteTasks.has(directionId) || JSON.stringify(directionQuotes.get(directionId)) === JSON.stringify(quote))
      && (value.approvalRequired || JSON.stringify(value) === JSON.stringify(output))) return;
    apply(value, meta);
  }
  // The host's own result for this card (hostResult) and what it names (hostKey): its quote, or its set or run.
  let hostResult = null, hostKey = "";
  // Work this card started from that result is kept in widgetState (see keep), so a reloaded card can show it.
  function remember(value) {
    const id = value.batchId || value.runId || "";
    if (!hostKey || hostKey === id) return;
    keep({ privateContent: { moved: { from: hostKey, ...(value.batchId ? { batchId: id } : value.runId ? { runId: id } : { edited: true }),
      ...(value.status ? { status: value.status } : {}), ...(value.designId ? { designId: value.designId } : {}) } } });
  }
  function fromHost(result) {
    const value = result.structuredContent || {}, meta = result._meta || {};
    // A replay is the same result, metadata included: an older server sends the page itself in widget-only metadata.
    const replay = JSON.stringify(value) === JSON.stringify(hostResult?.structuredContent || null) && JSON.stringify(meta) === JSON.stringify(hostResult?._meta || {});
    // A new result from ChatGPT gets a fresh try at drawing after a crash; a copy of the one that crashed does not.
    if (halted === "crash" && !replay) halted = "";
    // A quote is named by its quote id, anything else by its own set or run (window.openai can keep a quote's metadata beside a
    // newer toolOutput).
    hostResult = result; hostFailure = "";
    hostKey = value.approvalRequired ? meta.paidAction?.quoteId || value.confirmation?.quoteId || "" : value.batchId || value.runId || "";
    // A card confirmed before this was kept still has the run it showed in its model context (window.openai only); for a quote card that
    // can only be work its own Confirm started.
    const model = value.approvalRequired && cardState.modelContent;
    const moved = cardState.privateContent?.moved || (model?.runId || model?.batchId ? { from: hostKey, ...(model.batchId ? { batchId: model.batchId } : { runId: model.runId }),
      status: model.status, designId: model.designId } : null);
    if (moved && hostKey && moved.from === hostKey) {
      // This card already started that work: show it (and read where it is), never the quote again.
      if (output.runId || output.batchId || delivered(output)) return;
      acceptedQuotes.add(hostKey);
      if (moved.edited) {
        apply({ edited: true, saved: true, designId: moved.designId });
        void tool("iter0_get_design", { designId: moved.designId }).then(next => {
          if (output.edited && output.designId === moved.designId && !output.previewImageUrl && next.design?.previewImageUrl) { output = { ...output, previewImageUrl: next.design.previewImageUrl }; render(); }
        }).catch(() => {});
      } else {
        apply({ ...(moved.batchId ? { batchId: moved.batchId } : { runId: moved.runId }), status: moved.status || "running", ...(moved.designId ? { designId: moved.designId } : {}) });
        void refreshProgress("quiet");
      }
      return;
    }
    // ChatGPT sends its original result again on a theme change and other events. A copy of it changes nothing the card has moved on
    // to: a design open in the builder stays open (audit F10), and a set or build the card has read since keeps its newer state and links.
    const same = output.batchId ? value.batchId === output.batchId : Boolean(output.runId) && !value.batchId && value.runId === output.runId;
    if (replay && ((isBuilder() && output.design) || same)) return;
    applyResult(result);
  }
  function applyCompatibilityGlobals(globals) {
    const mode = host.displayMode;
    host = { ...host, theme: globals.theme ?? window.openai?.theme, displayMode: globals.displayMode ?? window.openai?.displayMode };
    theme();
    if (host.displayMode !== mode && isBuilder() && !("toolOutput" in globals)) renderForMode();
    if ("toolOutput" in globals || "toolResponseMetadata" in globals) {
      const metadata = globals.toolResponseMetadata ?? window.openai?.toolResponseMetadata ?? {};
      const envelope = metadata.mcp_tool_result || metadata.call_tool_result;
      if (envelope?.isError) { hostError(envelope); return; }
      fromHost({ structuredContent: globals.toolOutput ?? window.openai?.toolOutput ?? envelope?.structuredContent ?? {}, _meta: envelope?._meta || metadata });
    } else poll(true);
  }
  async function confirmPaid(quote, bar) {
    if (confirmingPaid) return;
    confirmingPaid = true;
    const direction = quote.name === "iter0_create_site" && output.directions?.find(d => d.directionId === quote.arguments?.directionId);
    // The confirm card shows its own starting line in place (SIT-386); other surfaces keep the status message.
    const card = document.getElementById(bar)?.closest?.(".pay");
    requestBuilderFor(quote);
    if (card) card.classList.add("busy");
    else say("Waiting for ChatGPT.", bar, true);
    try {
      // A lost response must retry the same approved row / builder claim, not
      // create another quote or replay the one-use click tool. An unredeemed
      // code's row remains unapproved and this ordinary receipt retry refuses it.
      const retry = attemptedClicks.has(quote.quoteId) && quote.approvalId;
      attemptedClicks.add(quote.quoteId);
      const result = retry
        ? await toolResult(quote.name, { ...quote.arguments, approvalId: quote.approvalId })
        : await toolResult("iter0_confirm_paid_action", { quoteId: quote.quoteId, name: quote.name, arguments: quote.arguments, credits: quote.credits });
      if (!result.structuredContent?.approvalRequired && (result.structuredContent?.batchId || result.structuredContent?.runId || delivered(result.structuredContent))) acceptedQuotes.add(quote.quoteId);
      if (direction && result.structuredContent?.runId) buildOrigin = { runId: result.structuredContent.runId, title: direction.title };
      say("");
      applyResult(result);
    } catch (error) {
      // The card was not redrawn for a mode change while this ran; draw it now, before the reason goes beside the fresh price button.
      if (modeRenderDue) { confirmingPaid = false; render(); }
      if (error.message === "Not enough credits for this.") say(error.message, bar, true);
      else if (error.hostRefusal) {
        say("ChatGPT did not start this. Reply yes in chat to start it.", bar, true);
        // A direction's quote may only have been read by this card. Make its
        // public confirmation available for a later yes without a model turn.
        void request("ui/update-model-context", { structuredContent: { confirmation: {
          quoteId: quote.quoteId, name: quote.name, arguments: quote.arguments, credits: quote.credits,
        } } }).catch(() => {});
        return "approval";
      } else if (error.code === "invalid_quote") offerRequote(bar, "This quote is no longer available.");
      else say(`${error.message || "ChatGPT could not complete this action."} Check its status before retrying, or reply yes in chat.`, bar, true);
    } finally { confirmingPaid = false; card?.classList.remove("busy"); if (modeRenderDue) render(); }
  }
  function mountPaidPill(element, quote) {
    if (!element || !window.iter0PaidConfirm) throw new Error("The price could not be loaded. Try again, or ask in chat.");
    if (paidMounts.get(element) === quote) return;
    element.innerHTML = "";
    paidMounts.set(element, quote);
    // "Nothing was spent" only when this card watched the quote run out untouched. A quote already past its time when the card was
    // drawn may have been confirmed before (a reloaded card), and one this card tried to confirm may have started.
    const late = !(quote.expiresAt > Date.now());
    paidControls.push(window.iter0PaidConfirm.mount(element, quote, () => confirmPaid(quote, element.id),
      () => offerRequote(element.id, late || attemptedClicks.has(quote.quoteId) ? "This quote has expired." : "This quote expired. Nothing was spent.")));
  }
  // A price lasts 15 minutes. That is not lengthened here: a quote is single-use and tied to the exact page it priced, and the server
  // checks both again when it is confirmed. A stale price now has a one-tap way forward instead of a dead end (SIT-386, John 13 Oct).
  function offerRequote(pillId, text) {
    say(text, pillId, true);
    const slot = document.getElementById(`${pillId}-requote`);
    if (slot) slot.innerHTML = button("requote", "Get a new quote", pillId);
  }
  // Asks again with the quote's own request. Nothing is confirmed or spent: the server prices it again on the same page (an edit carries
  // a digest of that page) and refuses with its reason if the page has changed since.
  async function requote(pillId) {
    const current = output, direction = /^paid-build-(\d+)$/.exec(pillId);
    say("Getting a new quote…", pillId, true);
    try {
      if (direction) {
        const id = current.directions?.[Number(direction[1])]?.directionId;
        if (id) {
          directionQuotes.delete(id);
          const quote = await buildQuote(id, current);
          if (output === current) {
            mountPaidPill(document.getElementById(pillId), quote);
            const slot = document.getElementById(`${pillId}-requote`);
            if (slot) slot.innerHTML = "";
          }
        }
      } else if (paidAction) {
        const result = await toolResult(paidAction.name, paidAction.arguments);
        if (output === current) applyResult(result);
      }
      say("");
    } catch (error) {
      if (output === current) say(error.message || "A new quote could not be made. Try again, or ask in chat.", pillId, true);
    }
  }
  async function buildQuote(directionId, current) {
    const cached = directionQuotes.get(directionId);
    if (cached && cached.expiresAt > Date.now()) return cached;
    if (directionQuoteTasks.has(directionId)) return directionQuoteTasks.get(directionId);
    const generation = directionQuoteGeneration;
    const task = (async () => {
      const result = await toolResult("iter0_create_site", { directionId, quoteOnly: true });
      const quote = result._meta?.paidAction;
      if (!quote || !/^quote-[a-f0-9]{24}$/.test(quote.quoteId) || quote.name !== "iter0_create_site"
        || quote.arguments?.directionId !== directionId || !Number.isFinite(quote.credits) || quote.credits < 0
        || !Number.isFinite(quote.expiresAt) || quote.expiresAt <= Date.now()) {
        throw new Error("The price could not be loaded. Try again, or ask in chat.");
      }
      if (generation === directionQuoteGeneration && output === current) directionQuotes.set(directionId, quote);
      return quote;
    })();
    directionQuoteTasks.set(directionId, task);
    try { return await task; }
    finally { if (directionQuoteTasks.get(directionId) === task) directionQuoteTasks.delete(directionId); }
  }
  async function hydrateBuildPills(current) {
    const generation = directionQuoteGeneration;
    for (const [index, direction] of (current.directions || []).entries()) {
      try {
        const quote = await buildQuote(direction.directionId, current);
        if (generation !== directionQuoteGeneration || output !== current) return;
        mountPaidPill(document.getElementById(`paid-build-${index}`), quote);
      } catch (error) { if (output === current) say(error.message || "The price could not be loaded. Try again, or ask in chat.", `paid-build-${index}`, true); }
    }
  }
  // The Projects list is read once and kept, so a design edited since still said "Edited 6 hours ago". A save in this card, or a
  // fresh read of the design, makes that design's row current: newer time, and first in the list, as the server orders it.
  function freshenLibrary(designId, updatedAt) {
    const known = library?.designs?.find(x => x.designId === designId), time = Date.parse(updatedAt);
    if (!known || Number.isNaN(time) || time <= Date.parse(known.updatedAt)) return;
    const designs = library.designs.map(x => x.designId === designId ? { ...x, updatedAt } : x)
      .sort((a, b) => (Date.parse(b.updatedAt) || 0) - (Date.parse(a.updatedAt) || 0));
    const showing = output === library;
    library = { ...library, designs };
    if (showing) output = library;
  }
  // SIT-393 R1-03: the builder opened from a build that still polishes the page follows that build and shows the corrected
  // page once saved, never over the founder's own work (an unsent request, an older version, a menu, an edit in flight).
  // Status is read while the build can run (15 min; its ceiling is 13), every 5 s for a minute, then every 20 s. A swap
  // still waiting after that costs no reads and happens at the first tick after their work ends.
  const POLISH_STATUS_MS = 900000;
  let polishFollow = null, polishTimer;
  const localWork = () => versionView || menu || addingPage || addPageSending || draftText() || lastEdit?.busy;
  function followPolish() {
    clearTimeout(polishTimer);
    const f = polishFollow;
    if (stopped || !f || f.designId !== output.design?.designId) return void (polishFollow = null);
    const delay = f.waited < 60000 ? 5000 : 20000;
    f.waited += delay;
    polishTimer = setTimeout(checkPolish, delay);
  }
  async function checkPolish() {
    const f = polishFollow;
    if (!f) return;
    try {
      f.landed ||= f.waited > POLISH_STATUS_MS || (r => !(r.status === "done" && isPolishing(r)))(await tool("iter0_get_site_status", { runId: f.runId }));
      if (f.landed && !localWork()) {
        const next = await tool("iter0_get_design", { designId: f.designId });
        if (polishFollow === f && f.designId === output.design?.designId && !localWork()) {
          // The same design, saved again: the founder keeps their place (selected section, zoom, page) where it still exists.
          polishFollow = null;
          if (next.design && next.design.updatedAt !== output.design.updatedAt) { if (!next.sections?.some(s => s.sectionId === selected)) selected = null; output = next; hover = null; render(); }
          return;
        }
      }
    } catch { if (++f.errors > 20) return void (polishFollow = null); /* A failed read is tried again on the next tick. */ }
    followPolish();
  }
  async function openDesign(id) {
    // A design opened from its build's card while that build still polishes the page (review R1-03).
    const run = isPolishing(output) && output.status === "done" && output.designId === id && !output.batchId && output.runId;
    const next = await tool("iter0_get_design", { designId: id });
    if (next.design) {
      freshenLibrary(next.design.designId, next.design.updatedAt);
      // Opening the design again is the way to retry a layout read that failed (a page that is too large stays so).
      const key = `${next.design.designId}:${next.design.updatedAt}`;
      if (layouts.get(key)?.state === "failed") layouts.delete(key);
    }
    output = next; selected = null; zoom = null; pageView = null; versionView = null; menu = null; hover = null; render();
    if (run) polishFollow = { runId: run, designId: id, waited: 0, errors: 0 };
    followPolish();
  }
  async function deepLink() {
    const raw = host["openai/deepLink"]?.url;
    if (!raw || loadingDesign || !raw.startsWith("/") || raw.startsWith("//")) return;
    const url = new URL(raw, "https://iter0.com");
    const id = url.pathname === "/design" ? url.searchParams.get("id") : null;
    if (id) { loadingDesign = true; try { await openDesign(id); } finally { loadingDesign = false; } }
  }
  async function selectSection(value, scroll) {
    const section = output.sections?.find(s => s.sectionId === value);
    if (!section || !output.design || versionView) return;
    await request("ui/update-model-context", { structuredContent: { designId: output.design.designId, sectionId: value }, content: [{ type: "text", text: `Selected section: ${section.label}. Pass designId ${output.design.designId} and sectionId ${value}, with the change as prompt, to iter0_edit_site; iter0 loads the page itself, so send no page code. Quote and confirm any edit in chat. A confirmed edit is saved to the design, and the card offers Undo.` }] });
    selected = value; hover = null; render(); paintHighlight(scroll); say("Section selected. Describe your change in ChatGPT.");
    // Outline it once the page is measured, scrolling to it if the person picked it from the list.
    if (!boxes) void requestLayout().then(() => { if (selected === value) paintHighlight(scroll); });
  }
  async function act(action, value) {
    say("", action === "add-page" ? "add-page-row" : action === "restore" || action === "version" ? "version-bar" : "builder-bar");
    if (action !== "menu" && menu && isBuilder() && output.design) { menu = null; if (action !== "version" && action !== "open") render(); }
    if (action === "expand") {
      const mode = await request("ui/request-display-mode", { mode: "fullscreen" });
      if (mode?.mode !== "fullscreen") throw new Error("Full screen is unavailable here. Open the design in iter0.");
      host.displayMode = "fullscreen"; theme(); render();
    } else if (action === "open-builder") {
      const mode = await request("ui/request-display-mode", { mode: "fullscreen" });
      if (mode.mode !== "fullscreen") throw new Error("Fullscreen is unavailable in this host. Open the design in iter0.");
      host.displayMode = mode.mode; builderOpen = true;
      try { await openDesign(value); } catch (error) { builderOpen = surface === "builder"; render(); throw error; }
    } else if (action === "build") {
      const current = output, index = current.directions?.findIndex(direction => direction.directionId === value) ?? -1;
      say("Loading price…", index >= 0 ? `paid-build-${index}` : "builder-bar", true);
      const quote = await buildQuote(value, current);
      if (output !== current) return;
      if (index >= 0) {
        const mount = document.getElementById(`paid-build-${index}`);
        mountPaidPill(mount, quote);
        say("");
        mount.querySelector("button").click();
      } else {
        apply({ approvalRequired: true }, { paidAction: quote });
      }
    } else if (action === "requote") await requote(value);
    else if (action === "open") {
      const url = safeUrl(value);
      if (url) { const tagged = new URL(url); tagged.searchParams.set("src", "chatgpt"); await request("ui/open-link", { url: tagged.href }); }
      if (output.design) render();
    } else if (action === "undo-edit") await undoEdit();
    else if (action === "design") await openDesign(value);
    else if (action === "research") { researchOpen = !(researchOpen ?? output.research?.status === "running"); render(); }
    else if (action === "menu") { menu = menu === value ? null : value; render(); }
    else if (action === "device") { if (device !== value) { device = value; zoom = null; render(); } }
    else if (action === "retry-preview") {
      // First retry asks for the same page again at a fresh address. If that fails too, the signed link itself may have lapsed, so the
      // second retry reads the design again for new links. The device the person chose is untouched either way.
      previewFallbacks.delete(previewKey());
      const target = previewSource();
      if (!target.base) return;
      if ((previewRetries.get(target.base) || 0) >= 1 && output.design) {
        previewDone.clear(); previewRetries.clear();
        await openDesign(output.design.designId);
        return;
      }
      previewDone.delete(target.src);
      previewRetries.set(target.base, (previewRetries.get(target.base) || 0) + 1);
      render();
    }
    else if (action === "page") {
      const page = pagesOf().find(p => p.pageId === value);
      if (!page) return;
      if (page.pageId === pagesOf()[0].pageId || page.previewImageUrl) { pageView = page.pageId; selected = null; render(); }
      else await message(`Show me the ${page.title} page (${page.route}) of my design ${output.design.name}.`);
    } else if (action === "add-page") {
      addingPage = true; render();
      document.getElementById("add-page-input")?.focus();
    } else if (action === "add-page-cancel") {
      closeAddPage();
    } else if (action === "add-page-send") {
      // The typed purpose is the request; nothing is sent until the founder writes one.
      const purpose = draftText().trim();
      if (!purpose || !output.design || addPageSending) return;
      addPageSending = true; render();
      try { await message(`Add a page to my site ${output.design.name}: ${purpose}`); }
      catch (error) { addPageSending = false; render(); throw error; }
      addPageSending = false;
      closeAddPage();
      say("Sent to ChatGPT. It will reply in the chat.", "add-page-row");
    } else if (action === "version") {
      const version = versionsOf().find(v => v.versionId === value);
      versionView = !version || version.current ? null : value; render();
    } else if (action === "restore") {
      const version = versionsOf().find(v => v.versionId === value);
      if (!version) return;
      await request("ui/update-model-context", { structuredContent: { designId: output.design.designId, versionId: version.versionId }, content: [{ type: "text", text: `The user selected version ${version.number} of design ${output.design.designId}. The saved design remains unchanged until they confirm in chat.` }] });
      await message(`Restore version ${version.number} of my design ${output.design.name} (designId ${output.design.designId}, versionId ${version.versionId}) with iter0_restore_version. Check with me before you confirm it.`);
      say("ChatGPT will check with you before it restores this version.", "version-bar");
    } else if (action === "ask-change") {
      const section = !versionView && output.sections?.find(s => s.sectionId === selected);
      if (!section || !output.design) return;
      if (!boxes) void requestLayout();
      await message(`I want to change the ${section.label} section of my site (designId ${output.design.designId}, sectionId ${section.sectionId}). Ask me what I want changed before quoting or starting an edit.`);
    } else if (action === "unselect") { selected = null; render(); }
    else if (action === "side") {
      const side = document.getElementById("side");
      side.classList.toggle("fold"); sideFold = side.classList.contains("fold");
      document.querySelector("[data-action=side]").setAttribute("aria-expanded", String(!sideFold));
      setTimeout(() => { fitPreview(); paintHighlight(); }, 220);
    }
    else if (action === "fit") { zoom = null; fitPreview(); }
    else if (action === "zoom-in" || action === "zoom-out") { zoom = Math.max(0.1, Math.min(1.5, fitPreview() + (action === "zoom-in" ? 0.1 : -0.1))); fitPreview(); }
    else if (action === "library") { host["openai/deepLink"] = null; device = null; apply(library || await tool("iter0_list_my_designs", {})); }
    else if (action === "show3" || action === "show3again") {
      if (action === "show3again") await request("ui/update-model-context", { structuredContent: { designId: value }, content: [{ type: "text", text: `Use owned design ${value} as context. Read it before proposing new directions.` }] });
      await message("Show me three website designs. Check my brief with me and quote the credit price before starting.");
    } else if (action === "section") await selectSection(value, true);
    else if (action === "refresh-preview") {
      const current = output, index = current.directions?.findIndex(direction => direction.directionId === value) ?? -1;
      if (index < 0) return;
      say("Refreshing preview…", "builder-bar", true);
      const next = await tool("iter0_get_design_set_status", { batchId: current.batchId });
      if (output !== current) return;
      const direction = next.directions?.find(direction => direction.directionId === value);
      const src = safeUrl(direction?.screenshotUrl || direction?.previewImageUrl, true);
      if (!src) throw new Error("The preview is still unavailable. Try again shortly.");
      const image = document.querySelectorAll(".set .card")[index]?.querySelector(".thumb img");
      if (image) {
        image.dataset.retries = "1";
        const url = new URL(src); url.searchParams.set("retry", String(Date.now()));
        image.src = url.href;
      }
      say("");
    }
    else if (action === "reload") reload();
    else if (action === "refresh") {
      previewFallbacks.clear(); previewDone.clear(); previewRetries.clear();
      if (output.batchId || output.runId) {
        // Asked for by the person: it reads even after the card stopped checking, and starts the checks again.
        if (halted) { halted = ""; render(); }
        failures = 0; followKey = "";
        await refreshProgress("manual");
      }
      else if (output.design) await openDesign(output.design.designId);
      else if (isBuilder() && document.getElementById("pj-grid")) await search(projects.search);
      else apply(await tool("iter0_list_my_designs", {}));
    }
    // Projects area. None of these spends: Send posts the founder's words to ChatGPT, which quotes first.
    else if (action === "plus") setPlus(!projects.plus);
    else if (action === "pick") { setMode(value); setPlus(false); document.getElementById("pj-draft")?.focus(); }
    else if (action === "clear-mode") { setMode(""); document.getElementById("pj-draft")?.focus(); }
    else if (action === "send") await sendDraft();
    else if (action === "starter" || action === "new-site") {
      const field = document.getElementById("pj-draft");
      if (!field) return;
      if (action === "starter" && !field.value.trim()) { projects.draft = `${value}: `; field.value = projects.draft; }
      field.focus(); field.setSelectionRange?.(field.value.length, field.value.length);
      field.scrollIntoView?.({ block: "center", behavior: "smooth" });
      const send = document.getElementById("pj-send"); if (send) send.disabled = !field.value.trim();
    }
    else if (action === "page-next") await showPage(projects.page + 1);
    else if (action === "page-prev") await showPage(projects.page - 1);
    else if (action === "clear-search") {
      const field = document.getElementById("pj-search"); if (field) field.value = "";
      await search("");
      document.getElementById("pj-search")?.focus();
    }
  }
  document.addEventListener("click", async event => {
    const control = event.target.closest("[data-action]");
    if (projects.plus && !(control && ["plus", "pick"].includes(control.dataset.action))) setPlus(false);
    if (!control) {
      if (menu && !event.target.closest?.(".menu")) { menu = null; render(); return; }
      // Point at the page: a click on the preview selects the section under the pointer.
      if (isBuilder() && output.design && !versionView && event.target.closest?.("#preview-image")) {
        // The first click on a design asks for its layout and waits for it (see requestLayout); later clicks already have it.
        const current = output;
        if (!boxes) await requestLayout();
        if (output !== current || versionView) return;
        const index = sectionAt(event);
        if (index >= 0) try { await selectSection(output.sections[index].sectionId, false); } catch (error) { fail(error); }
      }
      return;
    }
    if (control.disabled) return;
    // A narrow card shows each direction as a small row; its picture opens that one design full width, and closes it again. It
    // calls nothing, so it skips the in-flight disabling below: disabling the focused button blurred it, and Space then did nothing
    // (PR 670 review R670-01).
    if (control.dataset.action === "zoom") {
      const card = control.closest(".card");
      if (card) control.setAttribute("aria-expanded", String(card.classList.toggle("big")));
      return;
    }
    control.disabled = true;
    try { await act(control.dataset.action, control.dataset.value); } catch (error) { fail(error); }
    finally {
      // A page button is enabled again only if there is a page that way; the keyboard stays where it was (or moves to the other button).
      control.disabled = control.id === "pj-send" ? !projects.draft.trim() : control.id === "pj-prev" ? !canPrev() : control.id === "pj-next" ? !canNext() : false;
      if (control.id === "pj-prev" || control.id === "pj-next") keepPagerFocus(control);
      saveView();
    }
  });
  document.addEventListener("mousemove", event => {
    if (!isBuilder() || !output.design || versionView || !event.target.closest?.("#preview-image")) { pointer = null; if (hover !== null) { hover = null; paintHighlight(); } return; }
    pointer = { clientX: event.clientX, clientY: event.clientY };
    if (!boxes) void requestLayout();
    const index = sectionAt(event);
    if ((index >= 0 ? index : null) !== hover) { hover = index >= 0 ? index : null; paintHighlight(); }
  });
  document.addEventListener("input", event => {
    if (event.target.id === "pj-draft") {
      projects.draft = event.target.value;
      event.target.style.height = "auto"; event.target.style.height = `${Math.min(208, event.target.scrollHeight)}px`;
      const send = document.getElementById("pj-send"); if (send) send.disabled = !projects.draft.trim();
      return;
    }
    if (event.target.id === "pj-search") {
      clearTimeout(searchTimer);
      const text = event.target.value;
      searchTimer = setTimeout(() => { if (text.trim() !== projects.search) void search(text).catch(fail); }, 300);
      return;
    }
    if (event.target.id !== "add-page-input") return;
    addPageDraft = { designId: output.design?.designId ?? null, text: event.target.value };
    const submit = document.getElementById("add-page-submit");
    if (submit) submit.disabled = !event.target.value.trim();
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Enter" && !event.shiftKey && event.target.id === "pj-draft") {
      if (event.isComposing || event.keyCode === 229) return;
      event.preventDefault();
      const send = document.getElementById("pj-send");
      if (send && !send.disabled) send.click();
      return;
    }
    if (event.key === "Enter" && event.target.id === "add-page-input") {
      // Enter that confirms an IME candidate (Chinese, Japanese, Korean) is not a send.
      if (event.isComposing || event.keyCode === 229) return;
      event.preventDefault();
      const submit = document.getElementById("add-page-submit");
      if (submit && !submit.disabled && !addPageSending) submit.click();
      return;
    }
    // Arrow keys (V05): in the Desktop / Phone switch the arrow chooses the other one and keeps the keyboard on it; in a menu it moves between
    // the choices and Enter chooses. Disabled choices are skipped; the keys are left alone when there is nowhere to go.
    const step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[event.key], group = step && event.target.closest?.("[role=radiogroup],[role=menu]");
    if (group) {
      const choices = [...group.querySelectorAll("[role=radio],[role^=menuitem]")].filter(item => !item.disabled), at = choices.indexOf(event.target);
      if (at < 0 || choices.length < 2) return;
      const next = choices[(at + step + choices.length) % choices.length];
      event.preventDefault();
      next.focus?.();
      if (group.getAttribute("role") === "radiogroup") { next.click(); document.getElementById(next.id)?.focus(); }
      return;
    }
    if (event.key !== "Escape") return;
    if (projects.plus) { setPlus(false); document.getElementById("pj-plus")?.focus(); }
    else if (menu) { const opener = menu; menu = null; render(); document.getElementById(`opener-${opener}`)?.focus(); }
    else if (addingPage && event.target.closest?.('[data-form="add-page"]')) closeAddPage();
  });
  window.addEventListener("resize", () => { fitPreview(); paintHighlight(); });
  // Host activity and returning to the card catch up without waiting for a
  // background timer. Hidden cards still read progress when their timer fires.
  document.addEventListener("visibilitychange", () => poll(true));
  window.addEventListener("focus", () => poll(true));
  window.addEventListener("pageshow", () => poll(true));
  document.addEventListener("error", event => {
    const image = event.target;
    if (image.tagName !== "IMG") return;
    image.hidden = true;
    const parent = image.parentElement;
    if (!parent) return;
    if (image.id === "preview-img" && isBuilder() && output.design) {
      const source = previewSource();
      // The phone page that did not load is never replaced by the desktop picture: the frame says so and offers Try again.
      if (source.full && source.width === PHONE_W && image.src === source.src) {
        previewDone.set(source.src, "failed"); render(); return;
      }
      // A desktop page that did not load falls back once to the cached thumbnail (a stale error from an earlier page is ignored).
      if (!versionView && image.src === source.src && source.base && source.base === safeUrl(output.design.pagePreviewImageUrl, true)
        && safeUrl(output.design.previewImageUrl, true) && !previewFallbacks.has(previewKey())) {
        previewFallbacks.add(previewKey()); render(); return;
      }
      // Nothing left to show: the loading state steps aside for the placeholder below.
      const loading = document.getElementById("pv-state");
      if (loading) loading.hidden = true;
    }
    if (output.batchId && parent.classList.contains("thumb") && !image.dataset.retries) {
      image.dataset.retries = "1";
      const failedUrl = image.src;
      setTimeout(() => {
        if (!image.isConnected || stopped || image.src !== failedUrl) return;
        const url = new URL(image.src); url.searchParams.set("retry", "1"); image.src = url.href;
      }, 1000);
    }
    if (parent.querySelector(".preview-fallback")) return;
    const placeholder = document.createElement("div");
    placeholder.className = "preview-fallback";
    const index = [...document.querySelectorAll(".set .card")].indexOf(image.closest(".card"));
    const direction = output.batchId && output.directions?.[index];
    placeholder.setAttribute("role", direction ? "group" : "img");
    placeholder.setAttribute("aria-label", `${image.alt || "Design preview"}. Preview unavailable.`);
    placeholder.innerHTML = `<p>Preview unavailable</p>${direction ? button("refresh-preview", "Refresh preview", direction.directionId, { ghost: true }) : "<span>Refresh to try again</span>"}`;
    parent.appendChild(placeholder);
  }, true);
  document.addEventListener("load", event => {
    const image = event.target;
    if (image.tagName !== "IMG" || !image.naturalWidth) return;
    image.classList?.add("ld"); // a project's picture fades in once it has loaded instead of popping in
    image.hidden = false;
    image.parentElement?.querySelector(".preview-fallback")?.remove();
    // The page the person is looking at has drawn: remember it (a redraw will not flash the loading state), size the frame to the real
    // image, and quietly ask for the other device's page.
    if (image.id === "preview-img" && isBuilder() && output.design) {
      if (image.src === previewSource().src) {
        previewDone.set(image.src, "loaded");
        const loading = document.getElementById("pv-state");
        if (loading) loading.hidden = true;
        fitPreview(); paintHighlight();
      }
      warmPhonePreview();
    }
  }, true);
  // Crash net (audit R4): an error the card's own code did not handle replaces the card with one message and Reload card, instead of a
  // card frozen on its last screen. Host messages and globals run inside guard; anything else reaches the window handlers.
  function crash(error) {
    if (stopped || halted === "crash") return;
    globalThis.console?.error?.("iter0 card:", error);
    halted = "crash"; clearTimeout(timer); timer = null;
    try { render(); } catch { notice("crash"); }
  }
  const guard = handler => event => { try { handler(event); } catch (error) { crash(error); } };
  window.addEventListener("error", event => { if (event.error) crash(event.error); });
  window.addEventListener("unhandledrejection", event => { if (event.reason) crash(event.reason); });
  // Reload card: starts the handshake again if ChatGPT never answered it, otherwise draws the card again from what it has (or, if that
  // fails too, from the host's own result) and reads its progress at once.
  function reload() {
    halted = ""; failures = 0; followKey = "";
    if (bridge === "starting") { render(); boot(); return; }
    try { render(); } catch (error) {
      output = {}; paidAction = null;
      try { if (hostResult) fromHost(hostResult); else render(); } catch { crash(error); return; }
    }
    poll(true);
  }
  window.addEventListener("message", guard(event => {
    if (event.source !== window.parent || !event.data || event.data.jsonrpc !== "2.0") return;
    const rpc = event.data;
    if (bridge === "compatibility" && !lateHost && rpc.id === initializationId && rpc.result && !pending.has(rpc.id)) {
      lateHost = true; document.documentElement.dataset.lateHost = "true";
      window.parent.postMessage({ jsonrpc: "2.0", method: "ui/notifications/initialized", params: {} }, "*");
      // What the card has already told the model goes again, now that ChatGPT can hear it.
      if (cardState.modelContent) { const { message: words, ...context } = cardState.modelContent; void request("ui/update-model-context", { structuredContent: context, ...(words ? { content: [{ type: "text", text: words }] } : {}) }).catch(() => {}); }
      return;
    }
    if (pending.has(rpc.id)) {
      const task = pending.get(rpc.id); clearTimeout(task.timeout); pending.delete(rpc.id);
      if (rpc.error) {
        const error = new Error("ChatGPT could not complete this request. Try again.");
        error.hostRefusal = true; task.reject(error);
      } else task.resolve(rpc.result);
    } else if (rpc.method === "ui/notifications/tool-result") {
      if (rpc.params.isError && rpc.params.structuredContent?.code !== "out_of_credits") hostError(rpc.params); else fromHost(rpc.params);
    } else if (rpc.method === "ui/notifications/host-context-changed") {
      const mode = host.displayMode;
      host = { ...host, ...rpc.params }; theme(); poll(true); void deepLink().catch(fail);
      // Leaving full screen puts a design back in the chat as its compact card (and entering it draws the builder).
      if (host.displayMode !== mode && isBuilder()) renderForMode();
    }
    else if (rpc.method === "ui/notifications/tool-input") {
      if (!confirmingPaid && !output.batchId && !output.runId) { cancelled = false; directionQuotes.clear(); apply({}); }
    }
    else if (rpc.method === "ui/notifications/tool-cancelled") {
      directionQuotes.clear(); apply({}); clearTimeout(timer);
      // The Projects page stays usable, so it keeps its list and says so in the status line; any other card is over, and says so once.
      if (isBuilder()) say("This request was cancelled."); else { cancelled = true; render(); }
    }
    else if (rpc.method === "ui/resource-teardown") {
      stopped = true; clearTimeout(timer); paidControls.splice(0).forEach(cleanup => cleanup()); pending.forEach(task => { clearTimeout(task.timeout); task.reject(new Error("This view has closed.")); }); pending.clear();
      window.parent.postMessage({ jsonrpc: "2.0", id: rpc.id, result: {} }, "*");
    }
  }));
  window.addEventListener("openai:set_globals", guard(event => {
    if (bridge === "starting") activateCompatibilityBridge(event.detail?.globals);
    if (!stopped && bridge === "compatibility") applyCompatibilityGlobals(event.detail?.globals || {});
  }));
  if (typeof ResizeObserver === "function") {
    let reportedHeight = null, layout = "";
    const observer = new ResizeObserver(() => {
      // Leaving the builder or full screen reports the card's height again, even if it matches the last one sent (PR 662 review).
      const now = `${document.documentElement.dataset.builder}|${document.documentElement.dataset.mode}`;
      if (now !== layout) { layout = now; reportedHeight = null; }
      if (document.documentElement.dataset.builder === "true") return;
      // The full-screen builder stops reporting once it draws, so a height reported for its loading skeleton would be kept by a host that
      // sizes the frame from reports. It reports none until it has drawn something that does.
      if (surface === "builder" && app.querySelector(".boot")) return;
      const height = Math.ceil(document.body.getBoundingClientRect().height);
      if (height !== reportedHeight) { reportedHeight = height; notify("ui/notifications/size-changed", { height }); }
    });
    observer.observe(document.body);
  }
  // Never blank (audit R1, incident 1: a blank panel until it was closed and reopened). The handshake gets 8 s and is asked again after
  // 1 s and 3 s; after the first miss the card draws its waiting state, and after the third, with nothing to show, it says so with
  // Reload card. A host that answers the compatibility way (window.openai) ends the retries.
  let initializationId = 0;
  // Until ChatGPT answers, the card takes ChatGPT's theme from window.openai, or the system's. It is set before the first paint of the
  // loading skeleton, so a dark chat never shows a light card.
  function provisionalTheme() {
    if (host.theme) return;
    host = { ...host, theme: window.openai?.theme || (window.matchMedia?.("(prefers-color-scheme: dark)").matches ? "dark" : "light"), displayMode: host.displayMode || window.openai?.displayMode };
    theme();
  }
  function boot(attempt = 0) {
    if (stopped || bridge !== "starting") return;
    const initialization = request("ui/initialize", { protocolVersion: "2026-01-26", appInfo: { name: "iter0", version: "0.5.0" }, appCapabilities: { availableDisplayModes: surface === "builder" ? ["fullscreen"] : ["inline", "fullscreen"] } }, 8000);
    initializationId = sequence;
    // guard: a drawing error is caught when it happens, so a result ChatGPT sends straight after is still drawn over it.
    initialization.then(guard(result => {
      if (bridge !== "starting") return;
      bridge = "standard"; document.documentElement.dataset.bridge = bridge; host = result.hostContext || {}; if (halted === "boot") halted = ""; theme(); notify("ui/notifications/initialized", {}); render();
    }), guard(() => {
      if (stopped || bridge !== "starting") return;
      provisionalTheme();
      if (attempt < 2) { if (!attempt) render(); setTimeout(() => boot(attempt + 1), attempt ? 3000 : 1000); }
      else if (!Object.keys(output).length) halt("boot");
    }));
  }
  provisionalTheme();
  boot();
  function activateCompatibilityBridge(globals) {
    if (stopped || !compatibilityReady || bridge !== "starting"
      || (typeof window.openai?.callTool !== "function" && typeof window.openai?.sendFollowUpMessage !== "function")) return;
    bridge = "compatibility"; document.documentElement.dataset.bridge = bridge;
    const task = pending.get(initializationId);
    if (task) { clearTimeout(task.timeout); pending.delete(initializationId); task.resolve({}); }
    say(""); applyCompatibilityGlobals({ ...window.openai, ...globals });
  }
  setTimeout(() => { compatibilityReady = true; activateCompatibilityBridge(); }, 500);
})();
