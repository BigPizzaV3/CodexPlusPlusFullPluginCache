import { readFileSync } from 'node:fs';
import { DocumentError } from './errors.mjs';
import { exampleDocument } from './recipes.mjs';

function freeze(value) { if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); } return value; }
export const catalog = freeze(JSON.parse(readFileSync(new URL('../data/catalog.json', import.meta.url), 'utf8')));
export const categories = Object.freeze(Object.keys(catalog.resources));
export const resourceMaps = Object.fromEntries(categories.map(category => [category, new Map(catalog.resources[category].map(entry => [entry.id, entry]))]));
const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replaceAll('ё', 'е').trim();
const aliases = new Map(categories.flatMap(category => catalog.categories[category].aliases.map(alias => [normalize(alias), category])));

export function searchCatalog({ query = '', category, offset = 0, limit = 12 } = {}) {
  if (category && !categories.includes(category)) throw new DocumentError(`Unknown resource category: ${category}`);
  if (!Number.isInteger(offset) || offset < 0 || !Number.isInteger(limit) || limit < 1 || limit > 50) throw new DocumentError('Catalog offset must be nonnegative; limit must be 1…50');
  const q = normalize(query);
  const inferred = aliases.get(q);
  const selected = category ? [category] : inferred ? [inferred] : categories;
  const categoryQuery = inferred && selected.includes(inferred);
  const matches = selected.flatMap(kind => catalog.resources[kind].map(entry => {
    const id = normalize(entry.id);
    const words = q.split(/\s+/).filter(Boolean);
    const description = normalize(`${entry.description} ${entry.label ?? ''} ${entry.tags?.join(' ') ?? ''}`);
    const score = !q || categoryQuery ? 1 : id === q ? 100 : id.startsWith(q) ? 80 : id.includes(q) ? 60 : words.every(word => description.includes(word) || id.includes(word)) ? 20 : 0;
    return { category: kind, entry, score };
  })).filter(item => item.score > 0).sort((a, b) => b.score - a.score);
  const page = matches.slice(offset, offset + limit);
  return {
    revision: catalog.revision, source_revision: catalog.sourceRevision, query, category: category ?? inferred ?? null,
    total: matches.length, offset, limit, next_offset: offset + page.length < matches.length ? offset + page.length : null,
    categories: [...new Set(page.map(item => item.category))].map(kind => ({ id: kind, ...catalog.categories[kind] })),
    entries: page.map(({ category: kind, entry }) => ({ category: kind, ...structuredClone(entry), example: exampleDocument(kind, entry), preview: { available: false, reason: 'Native ACE renderer and resources are required; this response contains a layout example, not a visual preview.' } })),
  };
}

export function renderCatalogPage(page) {
  const lines = [`Catalog ${page.revision}; ${page.total} matches; offset ${page.offset}; next_offset: ${page.next_offset ?? 'none'}.`];
  if (!page.entries.length) lines.push('No matching catalog entries. Try a category or another keyword; do not invent identifiers.');
  for (const category of page.categories) lines.push(`\n## ${category.title}\n${category.notes}`);
  for (const entry of page.entries) {
    lines.push(`\n### ${entry.category}: ${entry.id}\n${entry.description}`);
    if (entry.category === 'frames') lines.push(`Windows: ${entry.windows}; aspect: ${entry.pixels[0] / entry.pixels[1]}; recolorable ink: ${entry.ink}.`);
    if (entry.category === 'fonts') lines.push(`Separate italic faces: ${entry.italicFaces}. Verify glyph coverage for the requested language with actual font files.`);
    if (entry.example) lines.push(`Complete native document (empty photo slots where applicable):\n\`\`\`json\n${JSON.stringify(entry.example, null, 2)}\n\`\`\``);
    else lines.push('Requires the original template document and assets. Its name is not a native YAML field or a recipe.');
  }
  return lines.join('\n');
}

/** Generated MD is documentation only. Runtime validation reads the JSON above. */
export function renderCatalogMarkdown() {
  const lines = ['## 23. Каталоги встроенных ресурсов', '', `<!-- Generated from data/catalog.json; revision ${catalog.revision}. Run npm run catalog:sync after editing that file. -->`, '', `Срез исходного каталога: ${catalog.sourceRevision}, commit ${catalog.sourceCommit}. Ревизия структурированных данных: ${catalog.revision}. Идентификаторы чувствительны к регистру и пробелам.`, ''];
  for (const kind of categories) {
    lines.push(`### ${catalog.categories[kind].title}`, '', catalog.categories[kind].notes, '');
    const definitions = {
      grids: [['ID рецепта', 'Раскладка', 'rects (готовые координаты)', 'swap'], e => [e.id, e.description, JSON.stringify(e.rects), e.swap ? JSON.stringify(e.swap) : '—']],
      frames: [['preset', 'PNG, px', 'Аспект W/H', 'Окон', 'ink', 'Вид'], e => [e.id, e.pixels.join(' × '), e.aspect, e.windows, e.ink ? 'да' : 'нет', e.description]],
      fonts: [['font.family', 'Выбор веса', 'Отдельные курсивные faces'], e => [JSON.stringify(e.id), e.description, e.italicFaces ? 'есть' : 'нет']],
      shapes: [['kind', 'Название', 'Форма'], e => [e.id, e.label, e.description]],
      templates: [['Имя шаблона', 'Пропорция', 'Слайдов'], e => [e.id, e.ratio, e.slides]],
      stickers: [['source', 'Пак', 'Что изображено'], e => [JSON.stringify(e.id), e.pack, e.description]],
    };
    const [headings, row] = definitions[kind];
    lines.push(`| ${headings.join(' | ')} |`, `| ${headings.map(() => '---').join(' | ')} |`);
    for (const entry of catalog.resources[kind]) lines.push(`| ${row(entry).map((value, i) => i === 0 ? `\`${value}\`` : String(value).replaceAll('|', '\\|')).join(' | ')} |`);
    lines.push('');
  }
  return lines.join('\n').trimEnd() + '\n';
}
