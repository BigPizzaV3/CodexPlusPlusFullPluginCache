/**
 * Extract path-like tokens from a user prompt for routing heuristics.
 *
 * Bare English slash pairs (put/call, and/or, buy/sell) are not paths. Real
 * workspace references usually have a file extension, a known root segment,
 * a relative/absolute prefix, three or more segments, or an npm scope.
 */

const pathCandidatePattern =
  /(?:^|[\s("'`])(?!(?:luna|terra|sol)\/(?:low|medium|high|xhigh|ultra)\b)(?:\.{0,2}\/)?[\w@.-]+(?:\/[\w.@-]+)+|[\w@.-]+\.(?:c|cc|cpp|css|go|html|java|js|json|md|mjs|py|rb|rs|sh|ts|tsx|yaml|yml)\b/gi;

const knownFileExtensionPattern =
  /\.(?:c|cc|cpp|css|go|html|java|js|json|md|mjs|py|rb|rs|sh|ts|tsx|yaml|yml)$/i;

/**
 * First path segment that strongly suggests a real repo path.
 * Omits words that also form common English slash pairs (client/server,
 * high/low) so bare domain jargon is not treated as a workspace path.
 */
const knownPathRootPattern =
  /^(?:src|lib|libs|docs?|tests?|spec|specs|app|apps|packages?|plugins?|scripts?|bin|config|configs?|internal|cmd|pkg|api|components?|services?|modules?|fixtures?|examples?|tools?|node_modules|vendor|dist|build|public|assets?|hooks?|skills?|workflows?|pages?|routes?|middleware|utils?|helpers?|types?|styles?|migrations?|\.github|include|src-tauri|__tests__|__mocks__)$/i;

/**
 * @param {string} rawMatch
 * @returns {boolean}
 */
export function isLikelyPathToken(rawMatch) {
  const token = rawMatch.trim();
  if (token.length === 0) {
    return false;
  }
  if (knownFileExtensionPattern.test(token)) {
    return true;
  }
  if (token.startsWith("@") && token.includes("/")) {
    return true;
  }

  const relativeOrAbsolute = /^(?:\.{1,2}\/|\/)/.test(token);
  const body = token.replace(/^(?:\.{1,2})?\//, "");
  const segments = body.split("/").filter(Boolean);
  if (segments.length === 0) {
    return false;
  }
  if (segments.length >= 3) {
    return true;
  }
  if (relativeOrAbsolute) {
    return true;
  }
  if (segments.length === 2 && knownPathRootPattern.test(segments[0])) {
    return true;
  }
  return false;
}

/**
 * @param {string} prompt
 * @returns {string[]}
 */
export function matchPathTokens(prompt) {
  const candidates = prompt.match(pathCandidatePattern) ?? [];
  return candidates.filter(isLikelyPathToken);
}
