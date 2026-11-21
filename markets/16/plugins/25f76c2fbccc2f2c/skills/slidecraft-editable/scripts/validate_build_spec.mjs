// Reject incomplete native-content audit coverage before rendering a deck.
const normalize = text => text.replace(/\s+/gu, ' ').trim();
export function validateBuildSpec(spec, expectations) {
  if (!Array.isArray(spec.slides) || !spec.slides.length) throw new Error('At least one authored slide is required');
  if (!Number.isInteger(expectations.slideCount) || expectations.slideCount < 1 || !Array.isArray(expectations.slides)) throw new Error('Expectations require slideCount and slides');
  const rules = new Map();
  for (const rule of expectations.slides) {
    if (!Number.isInteger(rule.slide) || rule.slide < 1 || rule.slide > expectations.slideCount || rules.has(rule.slide)) throw new Error('Audit slide numbers must be unique and within slideCount');
    if (!Array.isArray(rule.requiredTexts) || rule.requiredTexts.some(t => typeof t !== 'string')) throw new Error('Audit requiredTexts must be an array of strings');
    rules.set(rule.slide, rule);
  }
  for (const slide of spec.slides) if (slide.targetIndex === null) delete slide.targetIndex;
  const appended = spec.slides.filter(s => s.targetIndex === undefined).length;
  const retained = spec.baseDeck ? expectations.slideCount - appended : 0;
  if (retained < 0 || (!spec.baseDeck && expectations.slideCount !== appended)) throw new Error('Expected slideCount is inconsistent with authored slides');
  const targets = new Set();
  let next = retained;
  for (const slide of spec.slides) {
    if (slide.targetIndex !== undefined) {
      if (!spec.baseDeck || !Number.isInteger(slide.targetIndex) || slide.targetIndex < 0 || slide.targetIndex >= retained || targets.has(slide.targetIndex)) throw new Error('Existing-slide targets must be unique valid indices in the base deck');
      if (slide.replaceContents !== true) throw new Error('Existing-slide reconstruction requires replaceContents:true; use the native API for focused edits');
      targets.add(slide.targetIndex);
    } else if (slide.replaceContents) throw new Error('replaceContents requires an existing slide');
    const number = slide.targetIndex === undefined ? ++next : slide.targetIndex + 1;
    const elements = slide.elements;
    if (!Array.isArray(elements) || !elements.length) throw new Error(`Slide ${number}: authored elements are required`);
    const rule = rules.get(number);
    if (!rule || rule.nativeText !== true || rule.noAutofit !== true) throw new Error(`Slide ${number}: audit must require native text and no autofit`);
    const text = elements.filter(e => e.kind === 'text');
    if (text.filter(e => e.role === 'title').length !== 1) throw new Error(`Slide ${number}: exactly one native title is required`);
    const checked = rule.requiredTexts.map(normalize).join(' ');
    for (const element of text) {
      if (typeof element.text !== 'string' || !normalize(element.text) || !Number.isFinite(element.size) || element.size <= 0) throw new Error(`Slide ${number}: text requires nonempty content and a positive font size`);
      if (!checked.includes(normalize(element.text))) throw new Error(`Slide ${number}: add every authored text block to requiredTexts`);
    }
    for (const [kind, field] of [['table','nativeTables'],['chart','nativeCharts']]) {
      const count = elements.filter(e => e.kind === kind).length;
      if (count && (!Number.isInteger(rule[field]) || rule[field] < count)) throw new Error(`Slide ${number}: audit must cover all native ${kind} objects`);
    }
  }
  return spec;
}
