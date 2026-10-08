import { explicitTier } from "./phrases.mjs";
import {
  BUNDLED_MODEL_CATALOG,
  validateModelProfile,
} from "./model-catalog.mjs";

export const MODEL_PIN_ROUTE_BY_MODEL = Object.freeze({
  "gpt-5.6-luna": "economy",
  "gpt-5.6-terra": "standard",
  "gpt-5.6-sol": "deep",
});

const modelSlugByName = Object.freeze({
  luna: "gpt-5.6-luna",
  terra: "gpt-5.6-terra",
  sol: "gpt-5.6-sol",
});
const directClause = String.raw`(?:^|[.!?;]\s*|\b(?:and|then)\s+)`;
const stickyAlwaysPattern = new RegExp(
  `${directClause}(?<control>(?:please\\s+)?(?:pin\\b|` +
    `do\\s+not\\s+(?:switch|change)(?:\\s+the)?\\s+current\\s+model\\b))`,
  "i",
);
const stickyNamedPrefixPattern = new RegExp(
  `${directClause}(?<control>(?:please\\s+)?(?:keep\\s+using|` +
    `stick\\s+(?:to|with)|use\\s+only)\\b)`,
  "i",
);
const clearPatterns = [
  new RegExp(
    `${directClause}(?:please\\s+)?(?:clear|remove)(?:\\s+the)?` +
      `\\s+model\\s+pin\\b`,
    "i",
  ),
  new RegExp(
    `${directClause}(?:please\\s+)?unpin(?:\\s+the)?\\s+model\\b`,
    "i",
  ),
  new RegExp(
    `${directClause}(?:please\\s+)?resume\\s+automatic\\s+routing\\b`,
    "i",
  ),
];
const effortToken = String.raw`low|medium|high|xhigh|max|ultra`;
const exactEffortContinuation =
  String.raw`(?=$|\s*$|[,;.!?\n]|\s+(?:reasoning|effort)\b|` +
  String.raw`\s+for\s+(?:this|the)\s+(?:thread|session)\b|` +
  String.raw`\s+(?:or|and)\s+(?=(?:gpt-5\.6-)?(?:luna|terra|sol)\b)|` +
  String.raw`\s+and\s+do\s+not\s+(?:switch|change)\b)`;
const modelEffortSource =
  String.raw`\b(?:gpt-5\.6-)?(luna|terra|sol)\b` +
  String.raw`(?:\s+model)?(?:\s*\/\s*|\s+(?:with|at|using|on)\s+|\s+)` +
  `(${effortToken})\\b${exactEffortContinuation}`;
const stickySubjectPattern =
  /\b(?:gpt-5\.6-)?(?:luna|terra|sol)\b|\b(?:current|same)\s+model\b|\b(?:low|medium|high|xhigh|max|ultra)\s+(?:reasoning|effort)\b/i;
const taskClauseBoundaryPattern =
  /(?:,\s*)?\b(?:and\s+then|and|then)\s+(?=(?:please\s+)?(?:add|analy[sz]e|audit|build|change|check|compare|debug|diagnose|document|edit|explain|fix|implement|inspect|investigate|list|locate|modify|read|refactor|remove|rename|review|run|test|update|verify|write)\b)/i;

function requireExactKeys(value, expected, label) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new TypeError(`${label} must be an object`);
  }
  const actual = Object.keys(value).sort();
  const wanted = [...expected].sort();
  const unknown = actual.find((key) => !wanted.includes(key));
  if (unknown) {
    throw new RangeError(`${label} has unknown key: ${unknown}`);
  }
  const missing = wanted.find((key) => !actual.includes(key));
  if (missing) {
    throw new RangeError(`${label} is missing key: ${missing}`);
  }
}

export function validateModelPinProfile(
  value,
  catalog = BUNDLED_MODEL_CATALOG,
) {
  requireExactKeys(
    value,
    ["route", "model", "reasoningEffort"],
    "model pin profile",
  );
  const validated = validateModelProfile(value, catalog);
  const route = MODEL_PIN_ROUTE_BY_MODEL[validated.model];
  if (value.route !== route) {
    throw new RangeError("model pin route must match its model");
  }
  return { route, ...validated };
}

function profileFromMatch(match) {
  const model = modelSlugByName[match[1].toLowerCase()];
  return validateModelPinProfile({
    route: MODEL_PIN_ROUTE_BY_MODEL[model],
    model,
    reasoningEffort: match[2].toLowerCase(),
  });
}

function allMatches(pattern, prompt) {
  return [...prompt.matchAll(new RegExp(pattern.source, `${pattern.flags}g`))];
}

function controlStart(match) {
  return match.index + match[0].lastIndexOf(match.groups.control);
}

function boundedControlClause(prompt, start) {
  const tail = prompt.slice(start, start + 160);
  const punctuation = /(?:[;!?\n]|(?<!\d)\.(?=\s|$))/.exec(tail);
  const taskBoundary = taskClauseBoundaryPattern.exec(tail);
  const boundaryIndex = [punctuation?.index, taskBoundary?.index]
    .filter((index) => index !== undefined)
    .sort((left, right) => left - right)[0];
  return boundaryIndex === undefined ? tail : tail.slice(0, boundaryIndex);
}

function stickyControlMatch(prompt) {
  const candidates = allMatches(stickyAlwaysPattern, prompt)
    .map((match) => ({ index: controlStart(match) }));
  for (const match of allMatches(stickyNamedPrefixPattern, prompt)) {
    const index = controlStart(match);
    if (stickySubjectPattern.test(boundedControlClause(prompt, index))) {
      candidates.push({ index });
    }
  }
  return candidates.sort((left, right) => left.index - right.index)[0] ?? null;
}

export function parseModelPinControl(prompt) {
  if (typeof prompt !== "string") {
    throw new TypeError("prompt must be a string");
  }
  const clear = clearPatterns.some((pattern) => pattern.test(prompt));
  const stickyMatch = stickyControlMatch(prompt);
  if (!clear && stickyMatch === null) {
    return { kind: "none" };
  }
  if (clear && stickyMatch !== null) {
    return {
      kind: "invalid",
      reasonCode: "session_model_pin_conflicting_controls",
    };
  }
  if (clear) {
    return { kind: "clear" };
  }

  const clause = boundedControlClause(prompt, stickyMatch.index);
  const profiles = [...clause.matchAll(new RegExp(modelEffortSource, "gi"))]
    .map(profileFromMatch);
  const unique = new Map(
    profiles.map((profile) => [
      `${profile.model}/${profile.reasoningEffort}`,
      profile,
    ]),
  );
  if (unique.size === 0) {
    return { kind: "invalid", reasonCode: "session_model_pin_incomplete" };
  }
  if (unique.size > 1) {
    return { kind: "invalid", reasonCode: "session_model_pin_ambiguous" };
  }
  return { kind: "set", profile: [...unique.values()][0] };
}

export function oneTurnProfileConflicts(prompt, config, pinnedProfile) {
  const pinned = validateModelPinProfile(pinnedProfile);
  const requested = explicitTier(prompt, config);
  if (requested === null) {
    return false;
  }
  const route = requested.route;
  const profile = {
    route,
    model: requested.modelOverride ?? config.routes[route].model,
    reasoningEffort:
      requested.reasoningEffortOverride ?? config.routes[route].reasoningEffort,
  };
  return profile.model !== pinned.model ||
    profile.reasoningEffort !== pinned.reasoningEffort;
}
