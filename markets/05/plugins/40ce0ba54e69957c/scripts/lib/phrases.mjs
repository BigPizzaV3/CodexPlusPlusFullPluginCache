import { matchPathTokens } from "./path-tokens.mjs";

const controlPrefix = String.raw`\b(?:use|choose|select|route(?: this)? to|go with|switch to|keep (?:it|this)|make (?:it|this)|stick (?:to|with)|prefer|run (?:this )?(?:on|with)|(?:i(?:'d| would) like|i want|let'?s use|give me)(?: the)?)\b`;
// Reject "do not use sol", "stop use sol/xhigh", "never use the deep tier".
const controlNegationBefore =
  /(?:^|[\s,;:]\s*)(?:do not|don['’]?t|never|stop(?:\s+to)?)\s+$/i;
const modelNames = Object.freeze({
  luna: "economy",
  terra: "standard",
  sol: "deep",
});
const routeRank = Object.freeze({
  economy: 1,
  standard: 2,
  deep: 3,
});
// Cost and capability wording that selects a tier without naming a model.
// "max"/"maximum" is deliberately absent: it belongs to effort requests such as
// "use maximum reasoning", which must not read as a deep-tier control.
const tierSynonyms = Object.freeze({
  economy: String.raw`econom(?:y|ical)|cheap(?:est)?|budget|low[- ]cost|light(?:weight)?|minimal`,
  standard: String.raw`standard|normal|default|balanced|middle`,
  deep: String.raw`deep(?:est)?|strongest|most capable|heaviest|heavy`,
});
const tierControlSuffix =
  String.raw`(?=\s*(?:$|[,.!?;]|(?:tier|route|profile|model|option)\b|(?:for|on)\b|(?:please|here|instead|now)\b|(?:and|then)\b))`;
const effortToken = String.raw`low|medium|high|xhigh|max|ultra`;
const effortPattern = String.raw`(${effortToken})`;
// Model must sit on the agent noun: "spawn sol agent with high effort".
// Avoids "spawn agent dynamically" / "spawn a terra gent" false controls.
const spawnModelPattern = new RegExp(
  String.raw`\b(?:spawn|launch)\s+(?:(?:a|an|one)\s+)?(?:(?:` +
    effortToken +
    String.raw`)(?:-|\s+)effort\s+)?(luna|terra|sol)\s+agents?\b` +
    String.raw`(?:\s+with\s+(` +
    effortToken +
    String.raw`)(?:\s+effort)?\b)?`,
  "gi",
);
// Models named only as the thing to avoid ("instead of sol") are not requests.
const excludedModelPattern =
  /\b(?:instead of|rather than|not|without)\s+(luna|terra|sol)\b/gi;

const negation = String.raw`(?:do not|don['’]?t|never|stop(?:\s+to)?)`;
const delegationVerb = String.raw`(?:use|spawn|call|launch|invoke|start|create)`;
const agentNoun = String.raw`(?:sub[- ]?)?agents?`;
const handOffVerb = String.raw`(?:farm|hand|fan|split)`;
// Optional count / effort / model tokens between verb and agent so
// "do not spawn sol agent" and "never use 2 high-effort agents" still deny.
const agentRequestModifiers = String.raw`(?:(?:one|two|three|four|\d+|an?|any|more|other)\s+)*(?:(?:low|medium|high|xhigh|ultra)(?:-|\s+)effort\s+)?(?:(?:luna|terra|sol)\s+)?`;
// False positives here are safe -- the parent simply does the work itself --
// while a false negative delegates against an explicit instruction. Matching is
// therefore deliberately broad.
const noDelegationPatterns = [
  new RegExp(
    `\\b${negation}\\s+(?:\\w+\\s+){0,2}${delegationVerb}\\s+${agentRequestModifiers}${agentNoun}\\b`,
    "i",
  ),
  new RegExp(
    `\\b(?:avoid|without)\\s+(?:(?:using|spawning|calling|launching|creating)\\s+)?${agentNoun}\\b`,
    "i",
  ),
  new RegExp(`\\bcontinue without using ${agentNoun}\\b`, "i"),
  new RegExp(`\\bno (?:more\\s+)?${agentNoun}\\b`, "i"),
  /\b(?:avoid|without) delegat(?:e|ing|ion)\b/i,
  /\bno delegation\b/i,
  /\b(?:do not|don['’]?t|never) delegate\b/i,
  new RegExp(
    `\\b${negation}\\s+(?:\\w+\\s+){0,2}${handOffVerb}\\s+(?:this\\s+|it\\s+|that\\s+)?(?:out|off)\\b`,
    "i",
  ),
  /\bstay in (?:the )?parent\b/i,
  /\bkeep (?:this|it) in the (?:main|current|parent|same) session\b/i,
  /\b(?:you\s+)?(?:do|handle|answer|fix|write)\s+(?:this|it|that)\s*,?\s+not\s+(?:with\s+|using\s+)?an?\s+(?:sub[- ]?)?agent\b/i,
  /\bhandle this (?:yourself|in the parent)\b/i,
  /\b(?:just )?(?:do|handle|answer|fix|write) (?:this|it|that) yourself\b/i,
];

// Conversational atoms. A prompt is passthrough only when it consists entirely
// of these, which is why both patterns below are anchored to the whole prompt.
// Anchoring is the only thing keeping "thanks, now fix the bug" out of
// passthrough and must never be relaxed to a substring match.
// Sorted longest-first so "thank you" wins over "thanks" and "good morning"
// wins over "good"; regex alternation is first-match, not longest-match.
const conversationalAtoms = [
  "hi", "hello", "hey", "yo",
  "good morning", "good afternoon", "good evening",
  "thanks", "thank you", "thanks so much", "thx", "ty", "cheers",
  "ok", "okay", "k", "kk", "got it", "understood", "makes sense",
  "sounds good", "sounds great", "that works",
  "perfect", "great", "nice", "awesome", "cool", "lgtm", "looks good",
  "sure", "yes", "yep", "yeah", "no", "nope",
  "continue", "proceed", "go ahead", "carry on", "keep going", "next",
  // Continuation of prior work must stay conversational so a short follow-up
  // does not force a fresh economy re-route mid-task.
  "continue with the task", "continue with task", "continue with the work",
  "continue with work", "continue with it", "continue with this",
  "keep going with the task", "keep going with the work",
  "proceed with the task", "proceed with the work",
  "please", "there", "my friend", "so much",
]
  .slice()
  .sort((left, right) => right.length - left.length)
  .map((atom) => atom.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
  .join("|");
// Questions directed at the assistant rather than at the work.
const smallTalkTails = [
  String.raw`how are you(?: doing)?(?: today)?`,
  String.raw`how(?:'s| is) it going`,
  String.raw`what(?:'s| is) up`,
  String.raw`sup`,
].join("|");
const smallTalkPatterns = [
  new RegExp(
    `^(?:(?:${conversationalAtoms})[\\s,.!?]*)*(?:${smallTalkTails})[\\s,.!?]*$`,
    "i",
  ),
  new RegExp(`^(?:good (?:morning|afternoon|evening)[\\s,.!?]*)+$`, "i"),
];
const acknowledgementPatterns = [
  new RegExp(`^(?:(?:${conversationalAtoms})[\\s,.!?]*)+$`, "i"),
];
const passthroughPatterns = [...smallTalkPatterns, ...acknowledgementPatterns];
const recurringFailurePatterns = [
  /\b(?:i(?:'m| am)\s+)?still\s+(?:get(?:ting)?|see(?:ing)?|hit(?:ting)?|encounter(?:ing)?|receiv(?:e|ing))\s+(?:(?:this|that|the(?:\s+same)?|same)\s+)?(?:error|failure|exception|crash|issue|problem)\b/i,
  /\b(?:this|that|the(?:\s+same)?|same)\s+(?:error|failure|exception|crash|issue|problem)\s+(?:still\s+)?(?:keeps?\s+happening|persists?|recurs?)\b/i,
  /\b(?:this|that|the)\s+[\w-]+\s+(?:is\s+still\s+failing|keeps?\s+failing|continues?\s+to\s+fail)\b/i,
  /\b(?:the|this|that)?\s*fix\s+(?:did not|didn't|does not|doesn't|has not|hasn't)\s+work\b/i,
  /\b(?:the\s+)?same\s+(?:bug|error|failure|issue|problem)\s+again\b/i,
  /\bstill\s+(?:broken|failing|not working)\b(?:[^.!?\n]{0,80}\b(?:previous|prior|earlier)\s+fix\b)?/i,
  /\b(?:we|i)\s+(?:already|previously)\s+tried\b[^.!?\n]{0,120}\b(?:failed|did not work|didn't work)\b/i,
];

// A text defect is trivial regardless of surrounding subject matter: fixing a
// typo in a security section is still a typo fix.
const textDefectPattern =
  /\b(?:add|adjust|change|correct|debug|fix|mention|rename|replace|update)\b[^.!?\n]{0,100}\b(?:comment|spelling|typo|wording)\b/i;
// Editing documentation is trivial only when no security subject is present.
// Otherwise "update the auth docs to remove the leaked credential" would excuse
// substantive security work from its floor.
// One vocabulary, three derived patterns. These were previously three separate
// literal lists that drifted apart within a single commit: "migrate" reached the
// clause set but not the floor set, so "migrate the credentials table" scored as
// routine work. Where a pattern needs a verb the others must not have, it is
// added at the point of use so the difference is visible rather than accidental.
// re-* forms are listed explicitly because \bdesign\b does not match inside
// "redesign".
const verbs = Object.freeze({
  edit: Object.freeze([
    "add", "adjust", "change", "correct", "fix", "mention", "rename",
    "replace", "update",
  ]),
  substantive: Object.freeze([
    "analy[sz]e", "audit", "debug", "design", "redesign", "re-?architect",
    "rewrite", "diagnose", "harden", "implement(?:s|ed|ing)?", "integrate",
    "investigate", "migrate", "purge", "refactor", "remove", "review",
    "revoke", "rotate", "secure", "validate", "verify",
  ]),
});
const anyOf = (...groups) => `(?:${groups.flat().join("|")})`;
const documentationNoun =
  String.raw`(?:docs?|documentation|readme(?:\.md)?|changelog(?:\.md)?)`;

const documentationEditPattern = new RegExp(
  `\\b${anyOf(verbs.edit)}\\b[^.!?\\n]{0,100}\\b${documentationNoun}\\b`,
  "i",
);
const documentationPattern =
  /\b(?:README(?:\.md)?|CHANGELOG(?:\.md)?|documentation|docs?\/|docs?\b|\.md\b)\b/i;
const boundedEditVerbPattern = new RegExp(`\\b${anyOf(verbs.edit)}\\b`, "i");
// Deliberately excludes "fix": it is too common an edit verb to treat a sibling
// clause containing it as substantive work.
const substantiveClauseActionPattern = new RegExp(
  `\\b${anyOf(verbs.substantive)}\\b`,
  "i",
);
const workClauseBoundaryPattern =
  /(?:\b(?:also|and|plus|then|while)\b|[,;.!?\n]+)/i;

// "test" counts as a sensitive action only as a verb. As a noun it describes the
// artifact rather than the work, so "add a unit test for the payment helper" is
// routine while "test that credentials cannot leak" is not.
// The substantive vocabulary plus "fix", which must fire a floor ("fix the auth
// bypass") even though it is too common to mark a sibling clause as substantive.
const sensitiveActionPattern = new RegExp(
  `\\b${anyOf(verbs.substantive, ["fix"])}\\b` +
    String.raw`|(?<!\b(?:a|an|the|another|integration|new|regression|smoke|unit)\s)\btests?\b`,
  "i",
);
const databaseObject = String.raw`(?:table|column|database|db)`;
const destructiveMigrationPatterns = [
  /\b(?:destructive migration|irreversible migration|delete production data)\b/i,
  new RegExp(
    `\\bdrop(?:s|ping)?\\s+(?:the\\s+)?(?:[\\w.-]+\\s+){0,3}` +
      `${databaseObject}\\b(?!\\s+(?:border|renderer)\\b)`,
    "i",
  ),
  new RegExp(
    `\\btruncate\\s+(?:(?:the|a)\\s+)?` +
      `(?:(?:production|prod)\\s+)?${databaseObject}\\b`,
    "i",
  ),
  /\bwipe\s+(?:the\s+)?production data\b/i,
  new RegExp(
    `\\bwipe\\s+(?:(?:the|a)\\s+)?(?:[\\w.-]+\\s+)?` +
      `${databaseObject}\\b`,
    "i",
  ),
];
// Named vulnerability classes belong here alongside the generic nouns. Without
// them "fix the sql injection in the search endpoint" scores as routine work and
// routes to the cheapest profile.
const securityNounPattern =
  /\b(?:auth(?:entication|orization)?|oauth|credentials?|password (?:hash(?:ing)?|rounds?|reset|policy)|jwt|json web tokens?|cryptograph\w*|encrypt\w*|leak\w*|permission boundary|access control|admin roles?|rbac|secrets?|secur(?:e|ity)|vulnerabilit\w*|csrf|xsrf|xss|sql injection|command injection|privilege escalation|session (?:cookie|fixation|token|id)|(?:httpOnly|samesite|secure) cookies?|cookies? (?:flags?|settings?|attributes?)|cors|hmac|certificate pinning|pii|personal data|rate limiting|rate limits? (?:for|on|to)|(?:path|directory) traversal|file upload path|sanitiz\w*|token validation|tls|ssl)\b/i;
const paymentNounPattern =
  /\b(?:billing|payments?|payouts?|financial transactions?)\b/i;
const diagnosticActionPattern =
  /\b(?:debug|diagnose|investigate|root cause)\b/i;
const diagnosticQuestionPattern = /\bwhy (?:is|are|does|do|did)\b/i;
const figureOutWhyPattern = /\bfigure out why\b/i;
const diagnosticFailurePattern =
  /\b(?:bug|broken|crash(?:es|ed|ing)?|error|exception|fail(?:s|ed|ing|ure)?|hang(?:s|ing)?|incorrect|intermittent|issue|not working|problem|regression|timeout|unexpected|wrong|500s?)\b|\bexit(?:s|ed|ing)? with code\b/i;
const brokenUserFlowPattern =
  /\b(?:login|sign[- ]?in|checkout)\b[^.!?\n]{0,100}\b(?:broken|crash(?:es|ing)?|fail(?:s|ed|ing)?|intermittent|not working|500s?)\b|\b(?:broken|crash(?:es|ing)?|fail(?:s|ed|ing)?|intermittent|not working|500s?)\b[^.!?\n]{0,100}\b(?:login|sign[- ]?in|checkout)\b/i;
const domainImplementationPattern =
  /\b(?:add|build|change|create|fix|implement|update|write)\b[^.!?\n]{0,120}\b(?:coverage|flows?|helpers?|integration|specs?|tests?)\b|\b(?:coverage|specs?|tests?)\b[^.!?\n]{0,120}\b(?:flows?|helpers?|integration)\b/i;
const unitTestPattern = /\bunit tests?\b/i;
const architecturePlanningPattern =
  /\b(?:architect(?:ure|ing)?|design(?:s|ed|ing)?|plan(?:s|ned|ning)?)\b/i;
const implementationPattern =
  /\bimplement(?:s|ed|ing|ations?)?\b/i;
const agentSubjectPattern = /\b(?:sub[- ]?)?agents?\b/i;
const agentOrchestrationPattern =
  /\b(?:dynamic(?:ally)?|orchestrat\w*|model selection|model routing|routing models?|route models?|spawn(?:s|ed|ing)?|delegat\w*)\b/i;
const strongAgentOrchestrationPattern =
  /\b(?:dynamic(?:ally)?|orchestrat\w*|model selection|model routing|routing models?|route models?)\b/i;
const multiModelSpawnPattern =
  /\b(?:multi[- ]model|different models?)\b[^.!?\n]{0,120}\b(?:spawn|agent|delegate|dispatch)\b/i;
const dynamicModelRoutingPattern =
  /\b(?:dynamic(?:ally)?\s+(?:model|agent)|model\s+(?:selection|routing))\b/i;
// Phrases where a tier word is ordinary technical vocabulary rather than a
// routing control. These are removed before tier matching, which is more
// reliable than inspecting whatever follows the tier word: a user may write
// "use economy please" or "go with economy, it is fine", and no allowlist of
// trailing keywords covers that without dropping real requests.
// "deep dive" belongs here because classify.mjs handles depth requests on a
// separate path.
const tierCollocationPattern =
  /\b(?:deep learning|deep dive|standard library|standard deviation|standard input|standard output|standard error|default branch|default export|light mode|dark mode|normal distribution|heavy lifting|econom(?:y|ies) of scale)\b/gi;

function hasSubstantiveSiblingWork(prompt) {
  return prompt.split(workClauseBoundaryPattern).some((clause) => {
    if (!substantiveClauseActionPattern.test(clause)) {
      return false;
    }
    return !(
      textDefectPattern.test(clause) ||
      (documentationPattern.test(clause) &&
        boundedEditVerbPattern.test(clause))
    );
  });
}

export function matchesNoDelegation(prompt) {
  return noDelegationPatterns.some((pattern) => pattern.test(prompt));
}

export function matchesSmallTalk(prompt) {
  return smallTalkPatterns.some((pattern) => pattern.test(prompt));
}

export function matchesPassthrough(prompt) {
  return passthroughPatterns.some((pattern) => pattern.test(prompt));
}

/**
 * True when the prompt only rejects a model/tier (`stop use sol`,
 * `do not use the deep tier`) without requesting another profile. Those turns
 * must not fall through to a fresh economy/luna structural route.
 */
export function matchesModelControlRejection(prompt) {
  if (typeof prompt !== "string") {
    return false;
  }
  const modelOrTier =
    String.raw`luna|terra|sol|econom(?:y|ical)|cheap(?:est)?|budget|standard|normal|default|balanced|deep(?:est)?|strongest|heaviest|heavy`;
  const rejectionPattern = new RegExp(
    String.raw`(?:do not|don['’]?t|never|stop(?:\s+to)?)\s+` +
      String.raw`(?:use|choose|select|route(?: this)? to|go with|switch to|prefer)\b` +
      String.raw`[^.!?\n]{0,80}\b(?:` +
      modelOrTier +
      String.raw`)\b`,
    "i",
  );
  if (!rejectionPattern.test(prompt)) {
    return false;
  }
  // A positive request for a different model/tier is not rejection-only.
  // Use a lightweight positive probe that ignores config defaults.
  const positiveModel = new RegExp(
    `${controlPrefix}[^.!?\\n]{0,40}?\\b(luna|terra|sol)\\b`,
    "gi",
  );
  for (const match of prompt.matchAll(positiveModel)) {
    if (!controlMatchIsNegated(prompt, match.index)) {
      const name = match[1].toLowerCase();
      if (!excludedModelNames(prompt).has(name)) {
        return false;
      }
    }
  }
  return true;
}

export function matchesRecurringFailure(prompt) {
  return recurringFailurePatterns.some((pattern) => pattern.test(prompt));
}

export function matchesTrivialEdit(prompt) {
  const paths = new Set(matchPathTokens(prompt));
  if (paths.size > 2) {
    return false;
  }
  if (hasSubstantiveSiblingWork(prompt)) {
    return false;
  }
  if (textDefectPattern.test(prompt)) {
    return true;
  }
  if (securityNounPattern.test(prompt)) {
    return false;
  }
  return (
    documentationEditPattern.test(prompt) ||
    (documentationPattern.test(prompt) && boundedEditVerbPattern.test(prompt))
  );
}

export function matchesParallelWork(prompt) {
  const splittingSignal = [
    /\b(?:in parallel|independent(?:ly)?|parallelize|separate workstreams?)\b/i,
    /\bat the same time\b/i,
    /\bdivide the work\b/i,
    /\bsplit (?:this|the work|the task)\b/i,
    /\brun one each\b/i,
  ].some((pattern) => pattern.test(prompt));
  const paths = new Set(matchPathTokens(prompt));
  const namedRoles = /\b(?:repo reader|reviewer|test runner|file editor|implementer|agents?)\b/gi;
  const units = /\b(?:two|three|four|\d+)\s+(?:files?|tasks?|workstreams?|checks?|updates?|reviews?)\b/i;
  return splittingSignal && (paths.size >= 2 || (prompt.match(namedRoles) ?? []).length >= 2 || units.test(prompt));
}

export function safetyFloorReasons(prompt) {
  const reasons = [];
  const trivial = matchesTrivialEdit(prompt);

  if (
    !trivial &&
    agentSubjectPattern.test(prompt) &&
    ((architecturePlanningPattern.test(prompt) &&
      agentOrchestrationPattern.test(prompt)) ||
      (implementationPattern.test(prompt) &&
        strongAgentOrchestrationPattern.test(prompt)))
  ) {
    reasons.push("agent_orchestration_architecture");
  }
  if (
    !trivial &&
    securityNounPattern.test(prompt) &&
    sensitiveActionPattern.test(prompt)
  ) {
    reasons.push("security_sensitive");
  }
  if (
    !trivial &&
    paymentNounPattern.test(prompt) &&
    sensitiveActionPattern.test(prompt)
  ) {
    reasons.push("payment_sensitive");
  }
  if (destructiveMigrationPatterns.some((pattern) => pattern.test(prompt))) {
    reasons.push("destructive_migration");
  }
  if (
    /\b(?:race (?:condition|bug|failure|issue|in|within)|deadlock|lock ordering|thread safety|distributed lock|concurrency[- ]safe|concurrency (?:bug|correctness|failure|issue|problem))\b/i.test(
      prompt,
    )
  ) {
    reasons.push("concurrency_correctness");
  }
  if (
    /\b(?:cross-service|across (?:three|four|five|\d+) services|distributed architecture|system-wide architecture|broad architecture)\b/i.test(
      prompt,
    )
  ) {
    reasons.push("cross_service_architecture");
  }
  if (
    /\b(?:ambiguous production (?:incident|outage)|production .*root cause|diagnose .*production (?:incident|outage)|multiple plausible causes)\b/i.test(
      prompt,
    )
  ) {
    reasons.push("ambiguous_incident");
  }
  return reasons;
}

export function standardFloorReasons(prompt) {
  if (matchesTrivialEdit(prompt)) {
    return [];
  }
  if (
    diagnosticActionPattern.test(prompt) ||
    ((diagnosticQuestionPattern.test(prompt) ||
      figureOutWhyPattern.test(prompt)) &&
      diagnosticFailurePattern.test(prompt)) ||
    brokenUserFlowPattern.test(prompt)
  ) {
    return ["diagnostic_work"];
  }
  if (
    paymentNounPattern.test(prompt) &&
    unitTestPattern.test(prompt) &&
    domainImplementationPattern.test(prompt)
  ) {
    return ["payment_test_work"];
  }
  return [];
}

export function isSensitiveSubordinateTask(value) {
  return (
    typeof value === "string" &&
    (securityNounPattern.test(value) ||
      paymentNounPattern.test(value) ||
      destructiveMigrationPatterns.some((pattern) => pattern.test(value)) ||
      /\b(?:race condition|deadlock|lock ordering|thread safety|distributed lock|concurrency)\b/i.test(
        value,
      ))
  );
}

export function hasDynamicDelegationLanguage(prompt) {
  return (
    typeof prompt === "string" &&
    (multiModelSpawnPattern.test(prompt) ||
      dynamicModelRoutingPattern.test(prompt))
  );
}

function controlMatchIsNegated(text, matchIndex) {
  return controlNegationBefore.test(text.slice(0, matchIndex));
}

function excludedModelNames(prompt) {
  return new Set(
    [...prompt.matchAll(excludedModelPattern)].map((match) =>
      match[1].toLowerCase(),
    ),
  );
}

export function explicitTier(prompt, config) {
  const matches = [];
  const excludedModels = excludedModelNames(prompt);
  // Prefer the first model after the control verb (non-greedy gap). A greedy
  // gap latched onto "sol" in "use luna instead of sol" and inverted the request.
  // Effort attaches via slash or a short connector so "use sol to fix the high
  // priority bug" does not pick up "high".
  const modelPattern = new RegExp(
    `${controlPrefix}[^.!?\\n]{0,40}?\\b(luna|terra|sol)\\b` +
      `(?:(?:\\/|[\\s,]*(?:with|at|using|on)?[\\s,]*)(${effortToken})\\b)?`,
    "gi",
  );
  for (const match of prompt.matchAll(modelPattern)) {
    if (controlMatchIsNegated(prompt, match.index)) {
      continue;
    }
    const modelName = match[1].toLowerCase();
    if (excludedModels.has(modelName)) {
      continue;
    }
    matches.push({
      route: modelNames[modelName],
      modelOverride: `gpt-5.6-${modelName}`,
      reasoningEffortOverride:
        match[2]?.toLowerCase() ??
        config.routes[modelNames[modelName]].reasoningEffort,
    });
  }
  for (const match of prompt.matchAll(spawnModelPattern)) {
    if (controlMatchIsNegated(prompt, match.index)) {
      continue;
    }
    const modelName = match[1].toLowerCase();
    if (excludedModels.has(modelName)) {
      continue;
    }
    matches.push({
      route: modelNames[modelName],
      modelOverride: `gpt-5.6-${modelName}`,
      reasoningEffortOverride:
        match[2]?.toLowerCase() ??
        config.routes[modelNames[modelName]].reasoningEffort,
    });
  }

  const scrubbed = prompt.replace(tierCollocationPattern, " ");
  for (const [route, synonyms] of Object.entries(tierSynonyms)) {
    const tierPattern = new RegExp(
      `${controlPrefix}[^.!?\\n]{0,100}?\\b(?:${synonyms})\\b` +
        `(?!\\s+(?:reasoning|effort))${tierControlSuffix}`,
      "gi",
    );
    for (const match of scrubbed.matchAll(tierPattern)) {
      if (controlMatchIsNegated(scrubbed, match.index)) {
        continue;
      }
      matches.push({
        route,
        modelOverride: null,
        reasoningEffortOverride: null,
      });
      break;
    }
  }
  if (matches.length === 0) {
    return null;
  }

  const routes = new Set(matches.map(({ route }) => route));
  const route = [...routes].sort((left, right) => routeRank[right] - routeRank[left])[0];
  const selected = matches.find(
    (match) => match.route === route && match.modelOverride !== null,
  );
  return {
    route,
    modelOverride: selected?.modelOverride ?? null,
    reasoningEffortOverride:
      selected?.reasoningEffortOverride ?? null,
    conflictResolved: routes.size > 1,
  };
}
