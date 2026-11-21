/** Register bundled bytes without a font URL or a wider resource allowlist. */
export function loadItalicFonts(faces, {FontFaceType = FontFace, fontSet = document.fonts} = {}) {
  return Promise.all(faces.map(({family, source, ...descriptors}) => {
    const bytes = Uint8Array.from(atob(source), character => character.charCodeAt(0));
    const face = new FontFaceType(family, bytes, descriptors);
    fontSet.add(face);
    return face.load();
  }));
}
