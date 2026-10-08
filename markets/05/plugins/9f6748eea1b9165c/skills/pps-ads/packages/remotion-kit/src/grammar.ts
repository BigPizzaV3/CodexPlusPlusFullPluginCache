// packages/remotion-kit/src/grammar.ts
// The PPS ad grammar, distilled from six reference ads (docs/superpowers/specs/2026-10-02-pps-ads-skill-design.md,
// section 2). ONE source for three readers: the connector recipe quotes it to the model, the spec
// validator refuses a plan that breaks it, and the Remotion kit imports its numbers. No imports here:
// the kit cannot reach app code and the app must not pull React in through this file.

export const AD_LENGTHS = [15, 30, 60] as const
export type AdLength = (typeof AD_LENGTHS)[number]

/** An ad's clips render at its project's shape, and a project is 16:9, 9:16 or 21:9, so there is no square ad. */
export const ASPECT_RATIOS = ['9:16', '16:9'] as const
export type AdAspectRatio = (typeof ASPECT_RATIOS)[number]

/** The kind of ad. Inferred by the agent from "what is the ad about"; never a sixth question. */
export const AD_FORMATS = ['demo', 'promo', 'spokesperson'] as const
export type AdFormat = (typeof AD_FORMATS)[number]
export const DEFAULT_FORMAT: AdFormat = 'promo'

/**
 * `lockup` and `demo` are the pre-PR-3 names, kept so a stored spec or a host's cached schema still
 * works: `lockup` renders as `title`, `demo` as `agent` (its `lines` are the steps).
 */
export const BEAT_TYPES = [
  'open', 'title', 'lockup', 'kinetic', 'live', 'prompt', 'agent', 'demo', 'results', 'device', 'approve', 'proof',
  'end',
] as const
export type BeatType = (typeof BEAT_TYPES)[number]

export function canonicalBeatType(type: BeatType): BeatType {
  if (type === 'lockup') return 'title'
  if (type === 'demo') return 'agent'
  return type
}

/** Seconds a beat may run. */
export const BEAT_RANGES: Record<BeatType, { min: number; max: number }> = {
  open: { min: 2, max: 3 },
  title: { min: 2, max: 3 },
  lockup: { min: 2, max: 3 },
  kinetic: { min: 1.5, max: 2.5 },
  live: { min: 3, max: 5 },
  prompt: { min: 2.5, max: 3 },
  agent: { min: 2, max: 3 },
  demo: { min: 2, max: 3 },
  results: { min: 3, max: 4.5 },
  device: { min: 3, max: 4.5 },
  approve: { min: 2, max: 2.5 },
  proof: { min: 2.5, max: 3.5 },
  end: { min: 3, max: 8 },
}

/** The canvas world (the interface and the type), as opposed to a generated clip. */
export const CANVAS_BEATS: ReadonlySet<BeatType> = new Set<BeatType>([
  'title', 'lockup', 'kinetic', 'prompt', 'agent', 'demo', 'results', 'device', 'approve', 'proof',
])
/** The live-action world: a generated clip under the graphics. */
export const FOOTAGE_BEATS: ReadonlySet<BeatType> = new Set<BeatType>(['open', 'live', 'end'])
/** The interface beats: software being used. A promo (a series, an event, a film) never shows one. */
export const DEMO_BEATS: ReadonlySet<BeatType> = new Set<BeatType>(['prompt', 'agent', 'demo', 'device', 'approve'])

export function beatAllowedIn(type: BeatType, format: AdFormat): boolean {
  if (format === 'promo') return !DEMO_BEATS.has(type)
  return true
}

/** How a canvas beat is laid out; the kit's camera parallax and the agent's variety rule read it. */
export type CanvasFamily = 'card' | 'type' | 'device'
export const CANVAS_FAMILY: Record<BeatType, CanvasFamily | 'footage'> = {
  open: 'footage',
  live: 'footage',
  end: 'footage',
  title: 'type',
  lockup: 'type',
  kinetic: 'type',
  proof: 'type',
  prompt: 'card',
  agent: 'card',
  demo: 'card',
  results: 'card',
  approve: 'card',
  device: 'device',
}

export interface TemplateBeat {
  type: BeatType
  seconds: number
  /** The one allowed swap: a product that is not software shows results instead of an agent beat. */
  alt?: BeatType
  /** Word-timed captions from the voiceover on this footage beat. */
  captions?: boolean
}

const b = (type: BeatType, seconds: number, extra: Partial<TemplateBeat> = {}): TemplateBeat => ({
  type,
  seconds,
  ...extra,
})

export const TEMPLATES: Record<AdFormat, Record<AdLength, readonly TemplateBeat[]>> = {
  demo: {
    15: [
      b('open', 2, { captions: true }), b('title', 2), b('prompt', 2.5), b('agent', 2), b('results', 3), b('end', 3.5),
    ],
    30: [
      b('open', 2.5, { captions: true }), b('title', 2.5), b('prompt', 3), b('agent', 2.5), b('results', 3.5),
      b('live', 3, { captions: true }), b('device', 3), b('approve', 2), b('kinetic', 2), b('proof', 2.5),
      b('end', 3.5),
    ],
    60: [
      b('open', 3, { captions: true }), b('title', 3), b('prompt', 3), b('agent', 3), b('results', 4.5),
      b('live', 4.5, { captions: true }), b('device', 4.5), b('approve', 2), b('results', 4.5),
      b('live', 4.5, { captions: true }), b('kinetic', 2), b('proof', 3), b('live', 4.5, { captions: true }),
      b('device', 4.5), b('kinetic', 2), b('end', 7.5),
    ],
  },
  promo: {
    15: [b('open', 2), b('title', 2), b('live', 3), b('kinetic', 1.5), b('live', 3), b('end', 3.5)],
    30: [
      b('open', 2.5), b('title', 2.5), b('live', 3.5), b('kinetic', 2), b('live', 3.5), b('results', 3.5),
      b('live', 3), b('proof', 2.5), b('live', 3), b('end', 4),
    ],
    60: [
      b('open', 3), b('title', 3), b('live', 4.5), b('kinetic', 2), b('live', 4.5), b('results', 4), b('live', 4.5),
      b('kinetic', 2), b('live', 4.5), b('proof', 3), b('live', 4.5), b('results', 4), b('live', 4.5), b('kinetic', 2),
      b('live', 4.5), b('end', 5.5),
    ],
  },
  spokesperson: {
    15: [
      b('open', 3, { captions: true }), b('title', 2), b('live', 3.5, { captions: true }), b('results', 3),
      b('end', 3.5),
    ],
    30: [
      b('open', 3, { captions: true }), b('title', 2.5), b('live', 4, { captions: true }), b('prompt', 2.5),
      b('agent', 2.5), b('live', 4, { captions: true }), b('results', 3.5), b('kinetic', 2),
      b('live', 3, { captions: true }), b('end', 3),
    ],
    60: [
      b('open', 3, { captions: true }), b('title', 3), b('live', 4.5, { captions: true }), b('prompt', 3),
      b('agent', 3),
      b('live', 4.5, { captions: true }), b('results', 4), b('device', 4), b('live', 4.5, { captions: true }),
      b('approve', 2), b('kinetic', 2), b('live', 4.5, { captions: true }), b('proof', 3),
      b('live', 4.5, { captions: true }), b('results', 4), b('end', 6.5),
    ],
  },
}

export function templateFor(length: AdLength, format: AdFormat = DEFAULT_FORMAT): readonly TemplateBeat[] {
  return TEMPLATES[format][length]
}

/** Music tempo words the music quote carries, as a grid the canvas entrances land on. */
export const MUSIC_TEMPOS = ['slow', 'mid', 'fast'] as const
export type MusicTempo = (typeof MUSIC_TEMPOS)[number]
export const MUSIC_BPM: Record<MusicTempo, number> = { slow: 80, mid: 100, fast: 120 }

/**
 * The graphics layer. Loosened after the first dogfood ad (spec section 5): scale-ins, mask reveals, a
 * push-in on every canvas beat, parallax, cursor travel and count-ups are in; spins, flips and bounces
 * past a 3% overshoot stay out.
 */
export const MOTION = {
  easeMinMs: 200,
  easeMaxMs: 400,
  slidePxMin: 20,
  slidePxMax: 40,
  scaleInFrom: 0.92,
  captionScaleFrom: 0.96,
  pushInMax: 0.06,
  parallax: { card: 1, type: 1.04, device: 1.08 },
  overshootMax: 1.03,
  tileStaggerMsMin: 80,
  tileStaggerMsMax: 120,
  tileStaggerMs: 100,
  clickDipMs: 120,
  countUpMs: 900,
  textHoldMinS: 1.5,
  textHoldMaxS: 2.5,
  typewriterCharsPerSecond: 18,
  cutCadenceMinS: 2.5,
  cutCadenceMaxS: 3.5,
  kineticWordsMin: 3,
  kineticWordsMax: 7,
  promptWordsMin: 6,
  promptWordsMax: 24,
  agentStepsMin: 2,
  agentStepsMax: 5,
  agentStepWordsMax: 6,
  resultsMin: 3,
  resultsMax: 6,
  captionWordsMin: 2,
  captionWordsMax: 4,
  captionAccentMax: 3,
  grainOpacity: 0.06,
  vignette: 0.02,
} as const

export const SOUND = {
  musicDuckDb: 9,
  /** Music under a footage beat, so a clip's own sound (ambience, effects, a line) reads. */
  musicUnderClipDb: 6,
  /** A footage clip's own audio plays; a clip is never generated silent unless the person asked. */
  clipVolume: 1,
  targetLufs: -16,
  voiceoverMaxShare: 0.6,
  finalFadeMs: 300,
} as const

/** A clip is generated at the beat plus a handle, never under the engine-friendly minimum. */
export const CLIP = { handleSeconds: 1, minSeconds: 4 } as const

export function clipSecondsFor(beatSeconds: number): number {
  return Math.max(CLIP.minSeconds, Math.ceil(beatSeconds + CLIP.handleSeconds))
}

/** Dynamic moves only. A slow move or a locked-off frame is allowed solely on a beat marked punchline. */
export const CAMERA_MOVES = [
  'quick push-in',
  'snap zoom',
  'crash zoom',
  'orbit',
  'drone fly-by',
  'drone fly-over',
  'whip pan',
  'low-angle rise',
  'tracking shot',
  'top-down crane',
  'selfie-cam',
  'dolly-through',
] as const
type CameraMove = (typeof CAMERA_MOVES)[number]

/** "no static", "without any slow camera", "don't use a tripod": a negated veto word is not a request for one. */
const NEGATED_VETO = new RegExp(
  '\\b(no|not|never|without|avoid|don\'?t|nothing)\\s+(\\w+\\s+){0,2}?(static|slow|locked[- ]off|tripod)\\b',
  'gi',
)
/** "static" alone can be electricity; it vetoes only with camera words around it. */
const STATIC_CAMERA = new RegExp(
  '\\b((static|tripod)\\s+(shot|camera|frame|framing|wide|angle|setup)|locked[- ]off|lock(ed)?[- ]off)\\b',
  'i',
)
const SLOW_CAMERA = new RegExp(
  '\\b(slow(ly)?|gentle|gently|subtle|steady|lazy|creeping)\\s+' +
    '(push[- ]?in|pull[- ]?(out|back)|zoom|pan|tilt|dolly|track(ing)?|orbit|crane|drift|move|camera)\\b',
  'i',
)
const SPEED_WORD_SOURCE = [
  'quick', 'quickly', 'fast', 'rapid(ly)?', 'swift(ly)?', 'snap', 'hard', 'sharp', 'brisk', 'racing', 'rushing',
  'whipping', 'energetic', 'dynamic', 'aggressive', 'punchy',
].join('|')
// Regex sources are built by string concatenation, never by a template literal: Next's build folds a
// template literal that embeds a constant into one string and mis-escapes `\\b` into a backspace
// character, so the compiled regex can never match (2026-10-02: every action verb counted zero in
// production while the source and vitest were fine). Concatenated literals compile correctly.
const SPEED_WORD = new RegExp('\\b(' + SPEED_WORD_SOURCE + ')\\b', 'i')
const SPEED_WORD_ALL = new RegExp('\\b(' + SPEED_WORD_SOURCE + ')\\b', 'gi')

interface MoveMatcher {
  move: CameraMove
  /** Every pattern must match for the move to count. */
  test: readonly RegExp[]
  /** The same patterns with the g flag, for stripping the phrase before verbs are counted. */
  strip: readonly RegExp[]
  /** A move that can be done slowly needs a speed word somewhere in the prompt. */
  needsSpeed: boolean
}

function matcher(move: CameraMove, sources: readonly string[], needsSpeed: boolean): MoveMatcher {
  const wrapped = sources.map((source) => `\\b(${source})\\b`)
  return {
    move,
    test: wrapped.map((source) => new RegExp(source, 'i')),
    strip: wrapped.map((source) => new RegExp(source, 'gi')),
    needsSpeed,
  }
}

/** The drone and its pass are tied together within three words, so a drone on a table never reads as a move. */
const DRONE_LEAD = 'drone\\s+(\\w+\\s+){0,3}?'
const FLY_BY = `${DRONE_LEAD}(fly[- ]?(by|past)|flyby|flies\\s+(by|past)|sweeps?\\s+past)`
const FLY_OVER = `${DRONE_LEAD}(fly[- ]?over|flyover|flies\\s+over|sweeps?\\s+over|soars?\\s+over|overhead)`

const MOVE_MATCHERS: readonly MoveMatcher[] = [
  matcher('quick push-in', ['(push|dolly|zoom)[- ]?in'], true),
  matcher('snap zoom', ['snap[- ]?zoom'], false),
  matcher('crash zoom', ['crash[- ]?zoom'], false),
  matcher('orbit', [['orbit(s|ing)?', 'arc(s|ing)?\\s+(around|past)', '(camera|we|lens)\\s+arcs?'].join('|')], true),
  matcher('drone fly-by', [FLY_BY], false),
  matcher('drone fly-over', [FLY_OVER], false),
  // A subject who whips or pushes through is acting, not the camera: those need the camera as the subject.
  matcher('whip pan', ['whip[- ]?pan|(camera|we|lens)\\s+whips?\\s+(to|into|across)'], false),
  matcher('low-angle rise', ['low[- ]angle\\s+(rise|rising|tilt)|rises?\\s+from\\s+(a\\s+)?low\\s+angle'], true),
  matcher('tracking shot', ['tracking\\s+(shot|camera)|camera\\s+tracks|(we|lens)\\s+tracks?'], true),
  matcher(
    'top-down crane',
    [
      [
        'top[- ]?down\\s+(crane|shot|move|drop|push|drift|view\\s+(drops|pushes|drifts))',
        'crane\\s+(drift|shot|down|up)',
        'overhead\\s+crane',
      ].join('|'),
    ],
    true,
  ),
  matcher('selfie-cam', ['selfie[- ]?cam|selfie\\s+shot|arm[- ]extended'], false),
  matcher('dolly-through', ['dolly[- ]?through|dollies?\\s+through|(camera|we|lens)\\s+push(es)?\\s+through'], true),
]

/**
 * The first allowed camera move named in a prompt, or null when it names none, names a move that can
 * be slow without a speed word, or asks for a static or slow camera.
 */
export function cameraMoveIn(prompt: string): CameraMove | null {
  const text = prompt.replace(NEGATED_VETO, ' ')
  if (STATIC_CAMERA.test(text) || SLOW_CAMERA.test(text)) return null
  const fast = SPEED_WORD.test(text)
  for (const candidate of MOVE_MATCHERS) {
    if (candidate.needsSpeed && !fast) continue
    if (candidate.test.every((pattern) => pattern.test(text))) return candidate.move
  }
  return null
}

/** Verbs a subject performs. Words that read as nouns as often as verbs (lights, hands, waves) are left out. */
// Everyday subject actions, in third person and -ing forms. Deliberately NOT here because they are
// nouns at least as often: lights, hands, points, presents, tears, waves, hits, shots, rolls, crosses
// (the entering-event pattern owns "crosses"), and the camera-move words (stripped before counting).
// Too narrow a list refused real prompts ("drops her phone, rubs her eyes, looks up and exhales"
// counted zero on 2026-10-02, Max's first phone test), and every false refusal costs a retry.
const ACTION_VERB_SOURCE = [
  // Body and gesture
  'leans?|leaning', 'lunges?|lunging', 'thrusts?|thrusting', 'reaches|reaching', 'stretches|stretching',
  'turns?|turning', 'spins?|spinning', 'twists?|twisting', 'nods?|nodding', 'shakes?|shaking', 'tilts?|tilting',
  'bows?|bowing', 'kneels?|kneeling', 'stands?\\s+up|standing\\s+up', 'sits?\\s+(up|down)|sitting\\s+(up|down)',
  'rises?|rising', 'jumps?|jumping', 'leaps?|leaping', 'dives?|diving', 'kicks?|kicking', 'dances|dancing',
  'claps?|clapping', 'cheers?|cheering', 'waving|waved', 'pointing|pointed', 'gestures?|gesturing',
  'raises|raising', 'lifts?|lifting', 'drops?|dropping|dropped', 'lowers?|lowering', 'hugs?|hugging',
  'holds?|holding', 'carries|carrying', 'swings?|swinging', 'flips?|flipping', 'rolls\\s+(over|up|out)',
  // Hands and objects
  'grabs?|grabbing', 'snatches|snatching', 'catches|catching', 'throws?|throwing', 'tosses|tossing',
  'pulls?|pulling', 'pushes|pushing', 'opens|opening', 'closes|closing', 'slams?|slamming', 'pours?|pouring',
  'slides|sliding', 'picks?\\s+up|picking\\s+up', 'sets?\\s+down|setting\\s+down', 'taps?|tapping',
  'swipes?|swiping', 'scrolls?|scrolling', 'types|typing', 'grips?|gripping', 'rubs?|rubbing', 'wipes?|wiping',
  'splashes|splashing', 'sprays?|spraying', 'scatters?|scattering', 'plants?|planting', 'rips?|ripping',
  'tears?\\s+(open|off|through)', 'strikes?|striking', 'punches|punching', 'hammers?|hammering', 'paints?|painting',
  'writes?|writing', 'draws?|drawing', 'cooks?|cooking', 'flips?\\s+(a|the)', 'serves?|serving',
  'presents?\\s+(a|the|it|his|her|their)',
  'hands?\\s+(a|the|it|him|her|them|over)',
  // Locomotion
  'runs?|running', 'sprints?|sprinting', 'dashes|dashing', 'races|racing', 'rushes|rushing', 'charges|charging',
  'walks?|walking', 'strides?|striding', 'steps?|stepping', 'climbs?|climbing', 'crawls?|crawling',
  'enters?|entering', 'exits?|exiting', 'storms?\\s+(in|out|off)', 'bursts?|bursting', 'erupts?|erupting',
  'explodes|exploding', 'crashes|crashing', 'spills?|spilling', 'tumbles?|tumbling', 'flies|flying|flew',
  // Face and voice, toward the lens
  'looks?|looking', 'glances|glancing', 'stares?|staring', 'smiles?|smiling', 'grins?|grinning',
  'laughs?|laughing', 'winks?|winking', 'gasps?|gasping', 'exhales|exhaling', 'breathes|breathing',
  'sighs?|sighing', 'yawns?|yawning', 'shouts?|shouting', 'yells?|yelling', 'whispers?|whispering',
  'sings?|singing', 'speaks?|speaking', 'talks?|talking', 'mouths|mouthing', 'cries|crying', 'prays?|praying',
  // Reveals
  'reveals|revealing|revealed', 'unveils?|unveiling', 'unwraps?|unwrapping', 'whips',
].join('|')
// Concatenation, not a template literal (see SPEED_WORD above). String.prototype.match with a global
// regex resets lastIndex, so one shared instance is safe.
const ACTION_VERBS = new RegExp('\\b(' + ACTION_VERB_SOURCE + ')\\b', 'gi')

/** The prompt with every matched camera-move phrase and speed word removed: what is left is the subject's. */
function withoutCameraPhrases(prompt: string): string {
  let text = prompt
  for (const candidate of MOVE_MATCHERS) {
    for (const pattern of candidate.strip) text = text.replace(pattern, ' ')
  }
  return text.replace(SPEED_WORD_ALL, ' ')
}

/** One verb per two seconds, so a 4 s beat needs two. Camera moves and speed words never count as verbs. */
export function actionVerbCount(prompt: string): number {
  const text = withoutCameraPhrases(prompt)
  return (text.match(ACTION_VERBS) ?? []).length
}

export function requiredActionVerbs(beatSeconds: number): number {
  return Math.min(3, Math.max(1, Math.ceil(beatSeconds / 2)))
}

/** A motion verb in any form, optionally carried in, through, past or out of the frame. */
const MOTION_INTO_FRAME =
  '(walk|run|step|slid|drop|fall|toss|throw|jump|div|roll|swing|rush|burst|pour|crash|slam|storm|charg|sprint|leap)' +
  '(e|es|ed|s|ing|ped|ping|ning|med|ming)?\\s+(in|into|through|past|across|onto|out)'
const FLY_INTO_FRAME = 'fl(y|ies|ew|ying)\\s+(in|into|through|past|across|onto|out)'
const CHANGES_IN_FRAME = [
  'falls?', 'falling', 'rains?', 'raining', 'rises?', 'rising', 'lights?\\s+up', 'comes?\\s+on', 'flares?', 'flaring',
  'ignites?', 'igniting', 'appears?', 'appearing', 'fills?', 'filling', 'reveals?', 'revealing', 'erupts?', 'erupting',
  'explodes?', 'exploding', 'bursts?', 'bursting', 'crosses', 'crossing', 'enters?', 'entering', 'lands?', 'landing',
  'arrives?', 'arriving',
].join('|')
const ENTERS_OR_CHANGES = new RegExp(
  '\\b(' +
    [
      MOTION_INTO_FRAME,
      FLY_INTO_FRAME,
      CHANGES_IN_FRAME,
      'into\\s+(the\\s+)?(frame|shot|view)',
      'from\\s+(above|below|behind|off[- ]screen)',
    ].join('|') +
    ')\\b',
  'i',
)

/** Whether something enters or changes the frame: a prop dropped in, a person walking in, steam crossing. */
export function hasEnteringEvent(prompt: string): boolean {
  return ENTERS_OR_CHANGES.test(withoutCameraPhrases(prompt))
}

function tablesFor(lengths: readonly AdLength[]): string {
  return AD_FORMATS.flatMap((format) =>
    lengths.map((length) => {
      const sequence = templateFor(length, format)
        .map((beat) => {
          const swap = beat.alt ? ` (or ${beat.alt})` : ''
          return `${beat.type}${swap} ${beat.seconds}s${beat.captions ? ' +captions' : ''}`
        })
        .join(' > ')
      return `${format} ${length} s: ${sequence}`
    }),
  ).join('\n')
}

/** The three 60 s tables, in the recipe's draft step; renderGrammarForModel carries only 15 s and 30 s. */
export function renderSixtySecondTables(): string {
  return tablesFor([60])
}

/**
 * The prompt beat's timing, one answer for the storyboard note and the composition. The whole prompt always types
 * in: at the reading pace when the beat has room, faster when it does not. The send button pops in 0.1 s after the
 * last character and the cursor presses it 0.2 s before the beat ends.
 */
export function promptTiming(
  seconds: number,
  chars: number,
): { charsPerSecond: number; typeSeconds: number; sendAt: number; pressAt: number } {
  const typeSeconds = Math.max(0.8, Math.min(seconds - 0.9, chars / MOTION.typewriterCharsPerSecond))
  const charsPerSecond = Math.max(MOTION.typewriterCharsPerSecond, chars / typeSeconds)
  return { charsPerSecond, typeSeconds, sendAt: typeSeconds + 0.1, pressAt: seconds - 0.2 }
}

/** What the recipe quotes to the model. Bound by the OpenAI wording rules: no plan, price or vendor words. */
export function renderGrammarForModel(): string {
  const beats = BEAT_TYPES.filter((beat) => beat !== 'lockup' && beat !== 'demo')
    .map((beat) => {
      const range = BEAT_RANGES[beat]
      return `"${beat}" ${range.min} to ${range.max} s`
    })
    .join('; ')
  return [
    'Formats, decided from what the ad is about and stated in one line before drafting: ' +
      '"demo" (an app, software, a service, a connector; the interface carries the ad, footage is the host and the ' +
      'bookends), "promo" (a series, an event, a film, a ministry, a book; footage carries it, every card moves), ' +
      '"spokesperson" (a person talking to camera with captions, cut against interface or title beats).',
    `Beats: ${beats}. "lockup" and "demo" are older names for "title" and "agent".`,
    'Tables, in this order and these lengths per format (the only swap allowed is the one shown; +captions marks ' +
      'a footage beat that shows word-timed captions from the voiceover):',
    tablesFor([15, 30]),
    '60 s tables are in the make-an-ad recipe; a wrong order is answered with the exact table.',
    'Storyboard content per canvas beat: "title" has text (the headline) and may have kicker and ' +
      'partner ("x <name>"); ' +
      `"prompt" has text, what the person would type, ${MOTION.promptWordsMin} to ${MOTION.promptWordsMax} words; ` +
      `"agent" has lines, ${MOTION.agentStepsMin} to ${MOTION.agentStepsMax} steps of at most ` +
      `${MOTION.agentStepWordsMax} words each; ` +
      `"results" has ${MOTION.resultsMin} to ${MOTION.resultsMax} imageIds or clipVideoIds ` +
      "(their own generations); pickIndex counts imageIds first, then clipVideoIds; " +
      '"device" has frame "phone" or "laptop" and inner "prompt", "agent" or "results" with that beat\'s content; ' +
      '"approve" has text (the button, default "Approve") and subtitle (what is approved); ' +
      `"kinetic" is ${MOTION.kineticWordsMin} to ${MOTION.kineticWordsMax} words; ` +
      '"proof" is a number or a line, "line | source".',
    'A footage beat with captions true shows the voiceover that covers it as word-timed captions, ' +
      `${MOTION.captionWordsMin} to ${MOTION.captionWordsMax} words at a time; ` +
      `captionAccent names up to ${MOTION.captionAccentMax} words in the brand color.`,
    'Footage (every "open", "live" and "end" clip): name a camera move from this list with a speed word: ' +
      `${CAMERA_MOVES.join(', ')}. ` +
      'Never static, never slow, unless the beat is marked as the punchline. ' +
      'Give the subject one action and one thing entering or changing frame for every 2 seconds. ' +
      'A character looks at the lens and gestures. Name the foreground, the subject and the background. ' +
      'End the shot on its peak.',
    `Clips are generated at the beat length plus ${CLIP.handleSeconds} s, never under ${CLIP.minSeconds} s, ` +
      'always with their own audio.',
    'Sound: one music track for the whole length (musicTempo "slow", "mid" or "fast" sets the grid text lands on), ' +
      `ducked ${SOUND.musicDuckDb} dB under voiceover; ` +
      `voiceover is optional and covers at most ${Math.round(SOUND.voiceoverMaxShare * 100)}% of the runtime.`,
  ].join('\n')
}
