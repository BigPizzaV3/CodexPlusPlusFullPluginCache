// Read-only preflight on the same print-media page that will become the PDF.
// Check actual text line rectangles, not a container's nominal scrollHeight.
(() => {
  if (!matchMedia('print').matches) throw new Error('print media is required');
  const pages = [...document.querySelectorAll('.sheet.report-page')];
  if (pages.length < 8 || pages.length > 10) throw new Error('canonical pages are required');
  const tolerance = 1; // CSS px: ignore subpixel rounding, not a line of lost text.
  const issues = new Map();
  let checked = 0;
  const add = (page, node, code, pixels) => {
    const element = node.nodeType === Node.TEXT_NODE ? node.parentElement : node;
    const block = element.closest('.bm, .card, .ax, .sr, .fig, li, tr, p') || element;
    const section = page.getAttribute('aria-label');
    const anchor = element.closest('[data-baseline], [data-research-id]');
    const contentId = anchor ? (anchor.dataset.baseline || anchor.dataset.researchId) : '';
    const component = `${block.tagName.toLowerCase()}${block.className && typeof block.className === 'string'
      ? '.' + block.className.trim().split(/\s+/).join('.') : ''}`;
    const key = `${page.dataset.page}|${contentId}|${component}|${code}`;
    const previous = issues.get(key);
    const overflow = Math.round(pixels * 25.4 / 96 * 10) / 10;
    if (!previous || previous.overflow_mm < overflow) {
      issues.set(key, {page: Number(page.dataset.page), section, content_id: contentId, component,
                       code, overflow_mm: overflow});
    }
  };
  for (const page of pages) {
    const main = page.querySelector('.page-content');
    const footer = page.querySelector('.ft');
    if (!main || !footer) throw new Error('canonical body/footer are required');
    const sheet = page.getBoundingClientRect();
    const footerTop = footer.getBoundingClientRect().top;
    const inspect = (node, rectangles) => {
      const element = node.nodeType === Node.TEXT_NODE ? node.parentElement : node;
      const style = getComputedStyle(element);
      if (style.visibility !== 'visible' || style.display === 'none') return;
      const clips = [];
      for (let ancestor = element; ancestor && ancestor !== page; ancestor = ancestor.parentElement) {
        const css = getComputedStyle(ancestor);
        // The canonical header's intentional ellipsis is outside main anyway.
        if (css.textOverflow === 'ellipsis') continue;
        const x = ['hidden', 'clip'].includes(css.overflowX);
        const y = ['hidden', 'clip'].includes(css.overflowY);
        if (x || y) clips.push({box: ancestor.getBoundingClientRect(), x, y});
      }
      for (const rect of rectangles) {
        if (rect.width <= 0 || rect.height <= 0) continue;
        checked++;
        if (rect.bottom > footerTop + tolerance && rect.top < sheet.bottom) {
          add(page, node, 'footer_overlap', rect.bottom - footerTop);
        }
        const outside = Math.max(sheet.left - rect.left, rect.right - sheet.right,
                                 sheet.top - rect.top, rect.bottom - sheet.bottom);
        if (outside > tolerance) add(page, node, 'sheet_clipping', outside);
        for (const {box, x, y} of clips) {
          const amount = Math.max(x ? box.left - rect.left : 0, x ? rect.right - box.right : 0,
                                  y ? box.top - rect.top : 0, y ? rect.bottom - box.bottom : 0);
          if (amount > tolerance) add(page, node, 'body_clipping', amount);
        }
      }
    };
    const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.textContent.trim() || node.parentElement.closest('svg')) continue;
      const range = document.createRange();
      range.selectNodeContents(node);
      inspect(node, [...range.getClientRects()]);
    }
    // Visible illustrations are body content; sprite definitions/icons are not.
    for (const element of main.querySelectorAll('img, .closing-qr svg')) {
      inspect(element, [element.getBoundingClientRect()]);
    }
  }
  if (!checked) throw new Error('body text was not measured');
  return {status: issues.size ? 'overflow' : 'ok', media: 'print', pages: pages.length,
          checked_rects: checked, tolerance_px: tolerance, issues: [...issues.values()]};
})()
