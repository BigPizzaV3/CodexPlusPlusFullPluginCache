#!/usr/bin/env node
/** Read-only Playwright probe for an assembled direct-image LP route. */

import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";

function fail(message) {
  throw new Error(message);
}

function parseArgs(argv) {
  const values = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    const key = argv[index];
    const value = argv[index + 1];
    if (!key?.startsWith("--") || value === undefined) {
      fail(`invalid argument near ${key ?? "end of arguments"}`);
    }
    values.set(key, value);
  }
  for (const key of ["--base-origin", "--route", "--manifest"]) {
    if (!values.get(key)) fail(`missing ${key}`);
  }
  return {
    baseOrigin: values.get("--base-origin"),
    route: values.get("--route"),
    manifestPath: path.resolve(values.get("--manifest")),
  };
}

function validateOriginAndRoute(baseOrigin, route) {
  const match = /^http:\/\/(localhost|127\.0\.0\.1):(\d+)$/u.exec(baseOrigin);
  const port = match ? Number(match[2]) : 0;
  if (!match || !Number.isInteger(port) || port < 1 || port > 65535) {
    fail("--base-origin must be normalized loopback http with an explicit valid port");
  }
  const approved = new URL(baseOrigin);
  if (
    approved.username || approved.password || approved.pathname !== "/" ||
    approved.search || approved.hash
  ) {
    fail("--base-origin must not contain credentials, path, query, or fragment");
  }
  if (!route.startsWith("/") || route.startsWith("//") || route.includes("\\")) {
    fail("--route must be a single-slash absolute path without backslashes");
  }
  const target = new URL(route, `${baseOrigin}/`);
  if (target.origin !== approved.origin) {
    fail("resolved route origin drifted from approved origin");
  }
  return target.toString();
}

function sha256(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

function normalizeText(value) {
  return value.replace(/\s+/gu, " ").trim();
}

async function inspectVisibleBox(locator, label, approvedOverlayKeys = null) {
  await locator.scrollIntoViewIfNeeded();
  const result = await locator.evaluate((element) => {
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    let effectiveOpacity = 1;
    let hiddenAncestor = false;
    let clipped = false;
    let paintSuppressed = false;
    let ancestor = element;
    while (ancestor instanceof Element) {
      const ancestorStyle = getComputedStyle(ancestor);
      effectiveOpacity *= Number(ancestorStyle.opacity);
      hiddenAncestor ||= ancestorStyle.display === "none" || ["hidden", "collapse"].includes(ancestorStyle.visibility);
      clipped ||= ancestorStyle.clip !== "auto" || ancestorStyle.clipPath !== "none";
      paintSuppressed ||= ancestorStyle.contentVisibility === "hidden" || ancestorStyle.filter !== "none" ||
        (ancestorStyle.maskImage !== undefined && ancestorStyle.maskImage !== "none") ||
        (ancestorStyle.webkitMaskImage !== undefined && ancestorStyle.webkitMaskImage !== "none");
      if (ancestor !== element && ["hidden", "clip", "scroll", "auto"].includes(ancestorStyle.overflow)) {
        const ancestorRect = ancestor.getBoundingClientRect();
        clipped ||= rect.left < ancestorRect.left - 1 || rect.right > ancestorRect.right + 1 ||
          rect.top < ancestorRect.top - 1 || rect.bottom > ancestorRect.bottom + 1;
      }
      ancestor = ancestor.parentElement;
    }
    return {
      x: rect.x,
      y: rect.y,
      width: rect.width,
      height: rect.height,
      documentTop: rect.top + scrollY,
      documentBottom: rect.bottom + scrollY,
      display: style.display,
      visibility: style.visibility,
      effectiveOpacity,
      hiddenAncestor,
      clipped,
      paintSuppressed,
      intersectsViewport: rect.bottom > 0 && rect.top < innerHeight && rect.right > 0 && rect.left < innerWidth,
      viewportWidth: innerWidth,
    };
  });
  if (
    result.width <= 0 || result.height <= 0 || result.display === "none" ||
    ["hidden", "collapse"].includes(result.visibility) || result.hiddenAncestor || result.effectiveOpacity <= 0.01 ||
    result.clipped || result.paintSuppressed || !result.intersectsViewport
  ) {
    fail(`${label} is hidden, clipped, transparent, offscreen, or has no positive geometry`);
  }
  if (result.x < -1 || result.x + result.width > result.viewportWidth + 1) {
    fail(`${label} extends outside the horizontal viewport`);
  }
  if (approvedOverlayKeys !== null) {
    const paint = await locator.evaluate((element, allowedKeys) => {
      const allowed = new Set(allowedKeys);
      const rect = element.getBoundingClientRect();
      const left = Math.max(0, rect.left);
      const right = Math.min(innerWidth, rect.right);
      const top = Math.max(0, rect.top);
      const bottom = Math.min(innerHeight, rect.bottom);
      const points = [];
      for (const xRatio of [0.2, 0.5, 0.8]) {
        for (const yRatio of [0.2, 0.5, 0.8]) {
          points.push({
            x: left + (right - left) * xRatio,
            y: top + (bottom - top) * yRatio,
          });
        }
      }
      let painted = 0;
      for (const point of points) {
        const topmost = document.elementsFromPoint(point.x, point.y)[0];
        const overlay = topmost?.closest?.(
          "[data-lp-overlay-section-id][data-lp-overlay-index][data-lp-overlay-kind]",
        );
        const overlayKey = overlay ? [
          overlay.getAttribute("data-lp-overlay-section-id"),
          overlay.getAttribute("data-lp-overlay-index"),
          overlay.getAttribute("data-lp-overlay-kind"),
        ].join(":") : null;
        if (topmost === element || (overlayKey !== null && allowed.has(overlayKey))) painted += 1;
      }
      return { painted, total: points.length };
    }, approvedOverlayKeys);
    if (paint.total === 0 || paint.painted / paint.total < 0.6) {
      fail(`${label} is substantially covered by an unapproved sibling or fixed element`);
    }
  }
  return result;
}

async function inspectViewport(page, imageResponses, manifest, width) {

  const sectionLocators = page.locator("img[data-lp-section-id][data-lp-section-order]");
  const sectionCount = await sectionLocators.count();
  if (sectionCount !== manifest.sections.length) {
    fail(`viewport ${width}: expected ${manifest.sections.length} marked section images, found ${sectionCount}`);
  }

  const servedHashes = [];
  const boxes = [];
  for (let index = 0; index < manifest.sections.length; index += 1) {
    const section = manifest.sections[index];
    const locator = sectionLocators.nth(index);
    await locator.scrollIntoViewIfNeeded();
    await locator.evaluate(async (image) => {
      if (!image.complete) {
        await new Promise((resolve, reject) => {
          image.addEventListener("load", resolve, { once: true });
          image.addEventListener("error", () => reject(new Error("section image failed to load")), { once: true });
        });
      }
      await image.decode();
    });
    const attributes = await locator.evaluate((image) => ({
      sectionId: image.getAttribute("data-lp-section-id"),
      sectionOrder: image.getAttribute("data-lp-section-order"),
      alt: image.getAttribute("alt"),
      describedBy: image.getAttribute("aria-describedby"),
      currentSrc: image.currentSrc,
      naturalWidth: image.naturalWidth,
      naturalHeight: image.naturalHeight,
      loading: image.loading,
      complete: image.complete,
    }));
    if (attributes.sectionId !== section.id || attributes.sectionOrder !== String(section.order)) {
      fail(`viewport ${width}: section marker order drift at position ${index + 1}`);
    }
    if (!attributes.complete || attributes.naturalWidth !== 390 || attributes.naturalHeight !== section.image.height) {
      fail(`viewport ${width}: section ${section.id} intrinsic dimensions/load state drift`);
    }
    if (attributes.alt !== section.alt) {
      fail(`viewport ${width}: section ${section.id} alt drift`);
    }
    if (attributes.loading !== section.loading) {
      fail(`viewport ${width}: section ${section.id} loading policy drift`);
    }
    if (!attributes.describedBy) {
      fail(`viewport ${width}: section ${section.id} lacks aria-describedby`);
    }
    const summary = await page.evaluate((ids) => {
      const nodes = ids.split(/\s+/u).map((id) => document.getElementById(id));
      return {
        allPresent: nodes.every((node) => node !== null),
        text: nodes.map((node) => node?.textContent ?? "").join(" "),
      };
    }, attributes.describedBy);
    if (!summary.allPresent || normalizeText(summary.text) !== normalizeText(section.accessible_summary)) {
      fail(`viewport ${width}: section ${section.id} accessible summary drift`);
    }
    if (!attributes.currentSrc) {
      fail(`viewport ${width}: section ${section.id} has no currentSrc`);
    }
    const matchingResponses = imageResponses.filter((response) => response.url() === attributes.currentSrc);
    if (matchingResponses.length !== 1) {
      fail(`viewport ${width}: section ${section.id} image response is missing or ambiguous`);
    }
    const response = matchingResponses[0];
    if (!response.ok()) fail(`viewport ${width}: section ${section.id} image response returned ${response.status()}`);
    await response.finished();
    const bytes = await response.body();
    const digest = sha256(bytes);
    if (digest !== section.image.sha256) {
      fail(`viewport ${width}: section ${section.id} served image hash drift`);
    }
    servedHashes.push(digest);

    const approvedOverlayKeys = section.overlays.map((overlay, overlayIndex) =>
      `${section.id}:${overlayIndex + 1}:${overlay.kind}`,
    );
    const box = await inspectVisibleBox(
      locator,
      `viewport ${width} section ${section.id}`,
      approvedOverlayKeys,
    );
    const alpha = await locator.evaluate((image) => {
      try {
        const canvas = document.createElement("canvas");
        canvas.width = image.naturalWidth;
        canvas.height = image.naturalHeight;
        const context = canvas.getContext("2d", { willReadFrequently: true });
        if (!context) return { error: "2d canvas unavailable", maximum: 0 };
        context.drawImage(image, 0, 0);
        const pixels = context.getImageData(0, 0, canvas.width, canvas.height).data;
        let maximum = 0;
        for (let offset = 3; offset < pixels.length; offset += 4) maximum = Math.max(maximum, pixels[offset]);
        return { error: null, maximum };
      } catch (error) {
        return { error: String(error), maximum: 0 };
      }
    });
    if (alpha.error || alpha.maximum <= 2) {
      fail(`viewport ${width}: section ${section.id} has unavailable or fully transparent paint`);
    }
    const expectedWidth = Math.min(width, 390);
    const expectedX = (width - expectedWidth) / 2;
    if (Math.abs(box.width - expectedWidth) > 1 || Math.abs(box.x - expectedX) > 1) {
      fail(`viewport ${width}: section ${section.id} width or centering drift`);
    }
    const expectedRatio = section.image.width / section.image.height;
    const renderedRatio = box.width / box.height;
    if (Math.abs(renderedRatio - expectedRatio) > 0.01) {
      fail(`viewport ${width}: section ${section.id} is cropped or nonuniformly scaled`);
    }
    boxes.push(box);
  }

  for (let index = 1; index < boxes.length; index += 1) {
    if (Math.abs(boxes[index].documentTop - boxes[index - 1].documentBottom) > 1) {
      fail(`viewport ${width}: section seam ${index} has a gap or overlap`);
    }
  }
  const noOverflow = await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1);
  if (!noOverflow) fail(`viewport ${width}: page has horizontal overflow`);

  const expectedOverlays = manifest.sections.flatMap((section) =>
    section.overlays.map((overlay, index) => ({ section, overlay, index: index + 1 })),
  );
  const overlayLocators = page.locator("[data-lp-overlay-section-id][data-lp-overlay-index][data-lp-overlay-kind]");
  if (await overlayLocators.count() !== expectedOverlays.length) {
    fail(`viewport ${width}: overlay marker count drift`);
  }
  for (let index = 0; index < expectedOverlays.length; index += 1) {
    const expected = expectedOverlays[index];
    const locator = overlayLocators.nth(index);
    const attributes = await locator.evaluate((element) => ({
      sectionId: element.getAttribute("data-lp-overlay-section-id"),
      overlayIndex: element.getAttribute("data-lp-overlay-index"),
      kind: element.getAttribute("data-lp-overlay-kind"),
      ariaLabel: element.getAttribute("aria-label"),
      tagName: element.tagName,
      href: element.getAttribute("href"),
      callTracking: element.getAttribute("data-lp-call-tracking"),
      callAvailability: element.getAttribute("data-lp-call-availability"),
      pointerEvents: getComputedStyle(element).pointerEvents,
      tabIndex: element.tabIndex,
      ariaDisabled: element.getAttribute("aria-disabled"),
    }));
    if (
      attributes.sectionId !== expected.section.id ||
      attributes.overlayIndex !== String(expected.index) ||
      attributes.kind !== expected.overlay.kind ||
      attributes.ariaLabel !== expected.overlay.accessible_label
    ) {
      fail(`viewport ${width}: overlay ${index + 1} marker or label drift`);
    }
    const overlayBox = await inspectVisibleBox(locator, `viewport ${width} overlay ${index + 1}`);
    const imageIndex = manifest.sections.findIndex((section) => section.id === expected.section.id);
    const imageBox = boxes[imageIndex];
    const scale = imageBox.width / 390;
    const region = expected.overlay.reserved_region;
    const expectedBox = {
      x: imageBox.x + region.x * scale,
      documentTop: imageBox.documentTop + region.y * scale,
      width: region.width * scale,
      height: region.height * scale,
    };
    if (
      Math.abs(overlayBox.x - expectedBox.x) > 2 ||
      Math.abs(overlayBox.documentTop - expectedBox.documentTop) > 2 ||
      Math.abs(overlayBox.width - expectedBox.width) > 2 ||
      Math.abs(overlayBox.height - expectedBox.height) > 2 ||
      overlayBox.x < imageBox.x - 1 ||
      overlayBox.x + overlayBox.width > imageBox.x + imageBox.width + 1 ||
      overlayBox.documentTop < imageBox.documentTop - 1 ||
      overlayBox.documentBottom > imageBox.documentBottom + 1
    ) {
      fail(`viewport ${width}: overlay ${index + 1} bounds drift from reserved region`);
    }
    if (expected.overlay.kind === "cta") {
      if (expected.overlay.action_role === "secondary-direct-call") {
        if (
          attributes.tagName !== "A" || attributes.href !== expected.overlay.href ||
          !attributes.href?.startsWith("tel:") ||
          attributes.callTracking !== expected.overlay.tracking_marker ||
          attributes.callAvailability !== expected.overlay.availability_copy ||
          attributes.pointerEvents === "none" || attributes.tabIndex < 0 ||
          attributes.ariaDisabled === "true"
        ) {
          fail(`viewport ${width}: direct-call overlay ${index + 1} is inert or its tel target/audit markers drift`);
        }
        if (overlayBox.width < 44 || overlayBox.height < 44) {
          fail(`viewport ${width}: direct-call overlay ${index + 1} is smaller than 44x44 CSS pixels`);
        }
      }
      const visual = await locator.evaluate((element) => {
        const isTransparent = (value) => {
          if (!value || value === "transparent") return true;
          const match = value.match(/^rgba?\(([^)]+)\)$/);
          if (!match) return false;
          const parts = match[1].split(",").map((part) => part.trim());
          return parts.length === 4 && Number(parts[3]) === 0;
        };
        const rendered = (node) => {
          const style = getComputedStyle(node);
          const rect = node.getBoundingClientRect();
          return style.display !== "none" && style.visibility !== "hidden" && Number(style.opacity) > 0 && rect.width > 0 && rect.height > 0;
        };
        const style = getComputedStyle(element);
        const pseudoStyles = [getComputedStyle(element, "::before"), getComputedStyle(element, "::after")];
        const pseudoExists = (pseudo) => pseudo.content && pseudo.content !== "none" && pseudo.content !== "normal";
        const hasOpaqueBorder = (paintStyle) => ["Top", "Right", "Bottom", "Left"].some((side) =>
          parseFloat(paintStyle[`border${side}Width`]) > 0 && paintStyle[`border${side}Style`] !== "none" && !isTransparent(paintStyle[`border${side}Color`]),
        );
        const hasForbiddenPaint = (paintStyle) =>
          !isTransparent(paintStyle.backgroundColor) ||
          paintStyle.backgroundImage !== "none" ||
          hasOpaqueBorder(paintStyle) ||
          paintStyle.borderImageSource !== "none" ||
          paintStyle.boxShadow !== "none" ||
          (parseFloat(paintStyle.outlineWidth) > 0 && paintStyle.outlineStyle !== "none" && !isTransparent(paintStyle.outlineColor)) ||
          paintStyle.filter !== "none" ||
          (paintStyle.maskImage || "none") !== "none" ||
          (paintStyle.webkitMaskImage || "none") !== "none";
        const hasPseudoText = pseudoStyles.some((pseudo) => pseudoExists(pseudo) && pseudo.content !== '""');
        const hasPseudoGeometry = (pseudo) =>
          [pseudo.width, pseudo.height, pseudo.minWidth, pseudo.minHeight].some((value) => parseFloat(value) > 0) ||
          ["absolute", "fixed"].includes(pseudo.position);
        const hasPseudoPaint = pseudoStyles.some((pseudo) =>
          pseudoExists(pseudo) && pseudo.display !== "none" && pseudo.visibility !== "hidden" &&
          Number(pseudo.opacity) > 0 && hasPseudoGeometry(pseudo) && hasForbiddenPaint(pseudo),
        );
        const visibleDescendants = [...element.querySelectorAll("*")].filter(rendered).length;
        return {
          hasRenderedText: element.textContent.trim().length > 0 ||
            (element.tagName === "INPUT" && (element.getAttribute("value") || "").trim().length > 0) ||
            hasPseudoText,
          visibleDescendants,
          transparentPaint: !hasForbiddenPaint(style) && !hasPseudoPaint,
        };
      });
      if (visual.hasRenderedText || visual.visibleDescendants > 0) {
        fail(`viewport ${width}: CTA overlay ${index + 1} has duplicate rendered text or visible descendants`);
      }
      if (!visual.transparentPaint) {
        fail(`viewport ${width}: CTA overlay ${index + 1} must be visually transparent, including pseudo-element paint`);
      }
    }
  }

  return {
    width,
    result: "pass",
    dom_image_order: manifest.sections.map((section) => section.image.path),
    served_image_sha256s: servedHashes,
    no_gaps: true,
    no_overflow: true,
    overlays: "pass",
    accessibility: "pass",
    direct_call: expectedOverlays.some(({ overlay }) => overlay.action_role === "secondary-direct-call")
      ? "pass" : "not-applicable",
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const target = validateOriginAndRoute(args.baseOrigin, args.route);
  const manifestBytes = await readFile(args.manifestPath);
  const manifest = JSON.parse(manifestBytes.toString("utf8"));
  const requireFromCaller = createRequire(path.join(process.cwd(), "package.json"));
  let playwright;
  try {
    playwright = requireFromCaller("playwright");
  } catch (error) {
    fail(`Playwright is unavailable from caller project: ${error.message}`);
  }
  const browser = await playwright.chromium.launch({ headless: true });
  try {
    const viewports = [];
    for (const width of [320, 390, 430]) {
      const context = await browser.newContext({ viewport: { width, height: 900 } });
      try {
        const page = await context.newPage();
        const imageResponses = [];
        page.on("response", (response) => {
          if (response.request().resourceType() === "image") imageResponses.push(response);
        });
        const navigation = await page.goto(target, { waitUntil: "networkidle" });
        if (!navigation || new URL(navigation.url()).origin !== new URL(args.baseOrigin).origin) {
          fail(`viewport ${width}: navigation response origin drifted from approved origin`);
        }
        if (navigation.request().redirectedFrom() !== null) {
          fail(`viewport ${width}: navigation redirects are forbidden`);
        }
        if (new URL(page.url()).toString() !== target) {
          fail(`viewport ${width}: final route drifted from approved target`);
        }
        viewports.push(await inspectViewport(page, imageResponses, manifest, width));
      } finally {
        await context.close();
      }
    }
    process.stdout.write(JSON.stringify({
      kind: "lp-runtime-browser-qa",
      schema_version: "1.2",
      manifest_sha256: sha256(manifestBytes),
      base_origin: args.baseOrigin,
      route: args.route,
      viewports,
      validator_scope: "bound-evidence-not-live-browser-truth",
    }));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  process.stderr.write(`ERROR: ${error.message}\n`);
  process.exitCode = 1;
});
