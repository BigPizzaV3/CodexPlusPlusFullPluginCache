// StratusLIVE's published Nonprofit AI Policy Template rules, packaged for local execution.
// No network calls, lead capture, analytics, or vendor product claims are included.
const REVENUE_BANDS = [{"id":"under-3m","label":"Under $3M"},{"id":"3m-10m","label":"$3M to $10M"},{"id":"10m-15m","label":"$10M to $15M"},{"id":"15m-22m","label":"$15M to $22M"},{"id":"22m-30m","label":"$22M to $30M"},{"id":"over-30m","label":"Over $30M"}];
const isValidRevenueBand = id => typeof id === 'string' && REVENUE_BANDS.some(b => b.id === id);
export const TOOL_VERSION = 1;
export const TOOL_PATH = '/tools/ai-policy-template/';
export const TOOL_URL = `https://stratuslive.com${TOOL_PATH}`;


                     
                    
                     
               
               
           
                  
                
                 
                        
            

                                                                                                          

                                                                                                   

                                                                           

                      
                       
                 
                     
                    
               
            
               
                         
                   

                                                                      

                                                                                 

                                                                         

                                                                            

                               
                 
          
                  
                       
               
         
                
             

                                                                                

                              
             
                   
                      
                          
                            
                                       
                        
                     
                     
                           
                         
                                          
                               
 

                                           
        
                
                
 

export const ORG_TYPES                    = [
  { id: 'human-services', label: 'Human services' },
  { id: 'health-research', label: 'Health, disease, and research' },
  { id: 'education', label: 'Education and youth' },
  { id: 'federated', label: 'United Way or federated campaign' },
  { id: 'faith', label: 'Faith-based' },
  { id: 'arts-culture', label: 'Arts and culture' },
  { id: 'foundation', label: 'Community or private foundation' },
  { id: 'association', label: 'Association or membership' },
  { id: 'environment-animal', label: 'Environment and animal welfare' },
  { id: 'other', label: 'Other' },
];


export const AUTHOR_ROLES                       = [
  { id: 'executive', label: 'Executive Director or CEO' },
  { id: 'fundraising', label: 'Development or advancement' },
  { id: 'finance', label: 'Finance' },
  { id: 'operations', label: 'Operations or data' },
  { id: 'it_security', label: 'IT or security' },
  { id: 'other', label: 'Board member or other' },
];

export const DATA_CATEGORIES                         = [
  { id: 'public', label: 'Public information only', help: 'Websites, 990s, news, published reports.' },
  { id: 'contact', label: 'Constituent contact and relationship records', help: 'Names, addresses, notes, interactions.' },
  { id: 'giving', label: 'Giving history and capacity indicators', help: 'Gifts, pledges, wealth screening results.' },
  { id: 'finance', label: 'Financial and accounting records', help: 'General ledger, batches, reconciliations.' },
  { id: 'program', label: 'Program, client, or patient data', help: 'Service records and outcomes tied to people.' },
  { id: 'hr', label: 'Employee and volunteer records', help: 'Personnel files, applications, evaluations.' },
  { id: 'none', label: 'No personal data of any kind', help: 'AI works only on content that names no one.' },
];

export const SENSITIVE_HANDLING                              = [
  {
    id: 'excluded',
    label: 'Kept out of AI tools entirely',
    help: 'Health, minors, financial account numbers, and similar categories never enter an AI tool.',
  },
  {
    id: 'approved-only',
    label: 'Allowed only inside approved platforms',
    help: 'Permitted where a written agreement covers confidentiality, use, and deletion.',
  },
  { id: 'undecided', label: 'Not decided yet', help: 'The draft starts with the strict rule until the board decides.' },
];

export const WORKFLOWS                     = [
  { id: 'prospect-research', label: 'Prospect research and donor briefings' },
  { id: 'donor-comms', label: 'Drafting donor communications and acknowledgements' },
  { id: 'gift-processing', label: 'Gift entry, coding, and receipting' },
  { id: 'reconciliation', label: 'Reconciliation between fundraising and finance' },
  { id: 'reporting', label: 'Reporting and board materials' },
  { id: 'grants', label: 'Grant research and drafting' },
  { id: 'marketing', label: 'Marketing and campaign content' },
  { id: 'constituent-support', label: 'Constituent and donor support responses' },
  { id: 'internal-ops', label: 'Internal work: notes, summaries, scheduling' },
];

export const AUTONOMY                     = [
  {
    id: 'draft-only',
    label: 'Draft and recommend only',
    help: 'A person reviews and sends, posts, or saves everything AI prepares.',
  },
  {
    id: 'approve-routine',
    label: 'Routine actions after approval',
    help: 'Low-risk actions may run once a person approves the workflow. Anything outbound or financial waits for individual approval.',
  },
  {
    id: 'undecided',
    label: 'Not decided yet',
    help: 'The draft starts at draft-only and asks the board to decide on routine automation.',
  },
];

export const APPROVERS                     = [
  { id: 'executive', label: 'The Executive Director or CEO' },
  { id: 'ai-lead', label: 'A designated AI lead on staff' },
  { id: 'committee', label: 'A cross-functional staff committee' },
  { id: 'board-committee', label: 'A board committee (finance, audit, or governance)' },
];

export const STAFF_REVIEWS                        = [
  { id: 'relationship-owner', label: 'The staff member who owns the relationship' },
  { id: 'supervisor', label: 'A supervisor or second reviewer' },
  { id: 'tiered', label: 'The owner for routine messages; a supervisor for major gifts and grants' },
];

export const DISCLOSURES                       = [
  { id: 'always', label: 'Whenever AI helped produce a communication' },
  { id: 'material', label: 'When AI produced the substance, not just grammar or formatting' },
  { id: 'on-request', label: 'On request, and in public-facing content' },
  { id: 'undecided', label: 'Not decided yet' },
];

export const VENDOR_REQUIREMENTS                              = [
  { id: 'no-training', label: 'Our data is not used to train the vendor’s models' },
  { id: 'soc2', label: 'A current SOC 2 report or an equivalent independent audit' },
  { id: 'named-models', label: 'Named model providers and where processing happens' },
  { id: 'approval-controls', label: 'Human approval controls on the actions AI can take' },
  { id: 'audit-log', label: 'A record of AI actions and who approved them' },
  { id: 'dpa', label: 'A data processing agreement and a subprocessor list' },
  { id: 'off-switch', label: 'The ability to turn AI features off' },
  { id: 'export', label: 'Export and deletion of our data when we leave' },
];

export const REVIEW_CADENCES                          = [
  { id: 'quarterly', label: 'Quarterly' },
  { id: 'semiannual', label: 'Twice a year' },
  { id: 'annual', label: 'Annually' },
  { id: 'on-change', label: 'Annually, and whenever a new tool or data category is proposed' },
];

export { REVENUE_BANDS };


export const STEP_IDS = ['organization', 'data', 'workflows', 'approvals', 'disclosure-review']         ;
export const STEP_TITLES = [
  'Your organization',
  'The data AI may touch',
  'The work AI may assist',
  'Who approves',
  'Disclosure, vendors, and review',
]         ;
export const LAST_STEP = STEP_IDS.length;


const byId =                   (list             ) => new Map(list.map((o) => [o.id, o]         ));
const ORG = byId(ORG_TYPES);
const ROLE = byId(AUTHOR_ROLES);
const DATA = byId(DATA_CATEGORIES);
const SENS = byId(SENSITIVE_HANDLING);
const WORK = byId(WORKFLOWS);
const AUTO = byId(AUTONOMY);
const APPR = byId(APPROVERS);
const REVIEW = byId(STAFF_REVIEWS);
const DISC = byId(DISCLOSURES);
const VEND = byId(VENDOR_REQUIREMENTS);
const CAD = byId(REVIEW_CADENCES);

export const label = {
  orgType: (id         ) => ORG.get(id)?.label ?? id,
  authorRole: (id                        ) => (id ? (ROLE.get(id)?.label ?? id) : 'Not stated'),
  revenueBand: (id        ) => REVENUE_BANDS.find((b) => b.id === id)?.label ?? id,
  data: (id              ) => DATA.get(id)?.label ?? id,
  sensitive: (id                   ) => SENS.get(id)?.label ?? id,
  workflow: (id          ) => WORK.get(id)?.label ?? id,
  autonomy: (id          ) => AUTO.get(id)?.label ?? id,
  approver: (id          ) => APPR.get(id)?.label ?? id,
  staffReview: (id             ) => REVIEW.get(id)?.label ?? id,
  disclosure: (id            ) => DISC.get(id)?.label ?? id,
  vendor: (id                   ) => VEND.get(id)?.label ?? id,
  cadence: (id               ) => CAD.get(id)?.label ?? id,
};


export function approverNoun(id          )         {
  switch (id) {
    case 'executive':
      return 'the Executive Director';
    case 'ai-lead':
      return 'the AI lead';
    case 'committee':
      return 'the AI review committee';
    case 'board-committee':
      return 'the designated board committee';
  }
}


export function cadenceShort(id               )         {
  return id === 'quarterly' ? 'each quarter' : id === 'semiannual' ? 'twice a year' : 'once a year';
}


export function approverTitle(id          )         {
  switch (id) {
    case 'executive':
      return 'Executive Director or CEO';
    case 'ai-lead':
      return 'AI lead';
    case 'committee':
      return 'AI review committee';
    case 'board-committee':
      return 'Designated board committee';
  }
}

export function cadenceNoun(id               )         {
  switch (id) {
    case 'quarterly':
      return 'each quarter';
    case 'semiannual':
      return 'twice a year';
    case 'annual':
      return 'once a year';
    case 'on-change':
      return 'once a year, and whenever a new tool or data category is proposed';
  }
}


                                                                                          

function pickOne                  (v         , list             )           {
  return typeof v === 'string' && list.some((o) => o.id === v) ? (v     ) : null;
}

function pickMany                  (v         , list             )             {
  if (!Array.isArray(v)) return null;
  const out      = [];
  for (const item of v) {
    const id = pickOne(item, list);
    if (!id) return null;
    if (!out.includes(id)) out.push(id);
  }

  return list.map((o) => o.id).filter((id) => out.includes(id));
}

export function parsePolicyInput(raw         )              {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return { ok: false, error: 'Invalid policy data.' };
  }
  const r = raw                           ;
  if (r.version !== 1) return { ok: false, error: 'Unsupported policy version.' };

  const orgType = pickOne(r.orgType, ORG_TYPES);
  if (!orgType) return { ok: false, error: 'Choose your organization type.' };
  if (r.revenueBand !== undefined && !isValidRevenueBand(r.revenueBand)) return { ok: false, error: 'Choose your annual revenue band.' };
  const authorRole = r.authorRole === undefined || r.authorRole === '' ? undefined : pickOne(r.authorRole, AUTHOR_ROLES);
  if (authorRole === null) return { ok: false, error: 'Choose your role, or leave it blank.' };

  const dataScope = pickMany(r.dataScope, DATA_CATEGORIES);
  if (!dataScope || dataScope.length === 0) return { ok: false, error: 'Choose at least one data category.' };
  if (dataScope.includes('none') && dataScope.length > 1) {
    return { ok: false, error: '“No personal data” cannot be combined with other data categories.' };
  }
  const sensitiveHandling = pickOne(r.sensitiveHandling, SENSITIVE_HANDLING);
  if (!sensitiveHandling) return { ok: false, error: 'Choose how sensitive categories are handled.' };

  const workflows = pickMany(r.workflows, WORKFLOWS);
  if (!workflows || workflows.length === 0) return { ok: false, error: 'Choose at least one kind of work.' };
  const autonomy = pickOne(r.autonomy, AUTONOMY);
  if (!autonomy) return { ok: false, error: 'Choose how much AI may do on its own.' };

  const approver = pickOne(r.approver, APPROVERS);
  if (!approver) return { ok: false, error: 'Choose who approves AI tools and uses.' };
  const staffReview = pickOne(r.staffReview, STAFF_REVIEWS);
  if (!staffReview) return { ok: false, error: 'Choose who reviews an AI draft before it reaches a donor or funder.' };

  const disclosure = pickOne(r.disclosure, DISCLOSURES);
  if (!disclosure) return { ok: false, error: 'Choose a disclosure rule.' };
  const vendorRequirements = pickMany(r.vendorRequirements, VENDOR_REQUIREMENTS);
  if (!vendorRequirements || vendorRequirements.length === 0) {
    return { ok: false, error: 'Choose at least one vendor requirement.' };
  }
  const reviewCadence = pickOne(r.reviewCadence, REVIEW_CADENCES);
  if (!reviewCadence) return { ok: false, error: 'Choose a review cadence.' };

  return {
    ok: true,
    input: {
      version: 1,
      orgType,
      ...(r.revenueBand ? { revenueBand: r.revenueBand } : {}),
      ...(authorRole ? { authorRole } : {}),
      dataScope,
      sensitiveHandling,
      workflows,
      autonomy,
      approver,
      staffReview,
      disclosure,
      vendorRequirements,
      reviewCadence,
    },
  };
}


                             
             
  
                 
                  
  
                  
                     
 

                      
                               
                                        
                                         
                                                         
                                   

                                
            
              
                 
 

                                 
                
                   
  
                       
                       
                         
                         
                                  
                     
 

export const DISCLAIMER =
  'This template is a starting point for a board conversation, not legal advice. Review it with counsel before adoption, especially where health, education, employment, or financial regulations apply to your organization.';

const ORG_NOTE                          = {
  'human-services':
    'Because the organization serves people whose circumstances are private, client and case information is treated as a protected category throughout this policy.',
  'health-research':
    'Because the organization holds health and research information, those records are treated as a protected category throughout this policy, and regulatory obligations take precedence over anything written here.',
  education:
    'Because the organization works with students and families, records about minors and educational records are treated as a protected category throughout this policy.',
  federated:
    'Because the organization raises funds on behalf of partner agencies and workplace campaigns, donor and agency data shared with it is treated as held in trust, and this policy governs its use in every AI tool.',
  faith:
    'Because the organization holds information about members, pastoral care, and giving, that information is treated as a protected category throughout this policy.',
  'arts-culture':
    'Because the organization holds member, patron, and donor information, that information is treated as a protected category throughout this policy.',
  foundation:
    'Because the organization holds information about donors, fundholders, and grant applicants, that information is treated as a protected category throughout this policy, and grant decisions remain a human responsibility.',
  association:
    'Because the organization holds member and donor information, that information is treated as a protected category throughout this policy.',
  'environment-animal':
    'Because the organization holds donor, volunteer, and adopter or supporter information, that information is treated as a protected category throughout this policy.',
  other:
    'Personal information about donors, clients, members, and staff is treated as a protected category throughout this policy.',
};

const WORKFLOW_USE                                                   = {
  'prospect-research': {
    use: 'Researching prospective donors and funders from public sources and preparing briefings for gift officers.',
    limit:
      'Capacity and wealth indicators come only from vendors under contract. A person verifies a briefing before it informs an ask.',
  },
  'donor-comms': {
    use: 'Drafting acknowledgements, stewardship messages, appeals, and follow-up notes to donors.',
    limit: 'A named person reviews every draft. The name on a message belongs to a person who read it.',
  },
  'gift-processing': {
    use: 'Preparing gift entries, coding suggestions, and receipts for staff review.',
    limit: 'Gift amounts, designations, and receipts take effect only after a person confirms them.',
  },
  reconciliation: {
    use: 'Matching fundraising records to accounting records and flagging exceptions for finance.',
    limit: 'Journal entries and corrections are posted by finance staff, never by an AI tool on its own.',
  },
  reporting: {
    use: 'Assembling reports, dashboards, and board materials from the organization’s own data.',
    limit: 'Figures presented to the board are checked against the system of record by the person presenting them.',
  },
  grants: {
    use: 'Researching grant opportunities and drafting proposal sections and reports to funders.',
    limit: 'Program staff confirm every factual claim about the organization before anything is submitted.',
  },
  marketing: {
    use: 'Drafting campaign content, web and social copy, and audience segments.',
    limit: 'Communication preferences and consent are honored on every send, and a person approves publication.',
  },
  'constituent-support': {
    use: 'Drafting responses to donor and constituent questions and routing requests to the right person.',
    limit: 'Responses about gifts, personal data, or complaints are reviewed by a person before they go out.',
  },
  'internal-ops': {
    use: 'Summarizing meetings, drafting internal notes, and helping with scheduling.',
    limit: 'Recordings and transcripts follow the same data rules as any other record, and participants are told when a meeting is recorded.',
  },
};

const DATA_PERMITTED                               = {
  public: 'Public information: websites, filings, news, and published reports.',
  contact: 'Constituent contact and relationship records: names, addresses, notes, and interaction history.',
  giving: 'Giving history and capacity indicators, including screening results obtained under contract.',
  finance: 'Financial and accounting records, including ledgers, batches, and reconciliations.',
  program: 'Program, client, or patient information, subject to the sensitive-category rule below.',
  hr: 'Employee and volunteer records, subject to the sensitive-category rule below and to employment law.',
  none: '',
};


const DATA_SHORT                               = {
  public: 'public information',
  contact: 'constituent contact and relationship records',
  giving: 'giving history and capacity indicators',
  finance: 'financial and accounting records',
  program: 'program, client, or patient data',
  hr: 'employee and volunteer records',
  none: 'no personal data',
};


const DISCLOSURE_PHRASE                             = {
  always: 'whenever AI helped produce a communication',
  material: 'when AI produced the substance, not just grammar or formatting',
  'on-request': 'on request, and in public-facing content',
  undecided: 'when AI produced the substance, not just grammar or formatting',
};


const REVIEW_SIGNOFF                              = {
  'relationship-owner': 'The staff member who owns the relationship signs off on donor and funder messages.',
  supervisor: 'A supervisor or second reviewer signs off on donor and funder messages.',
  tiered: 'The relationship owner signs off on routine messages, and a supervisor also approves anything to a major donor or funder.',
};

const VENDOR_ASK                                    = {
  'no-training': 'that the organization’s data, prompts, and outputs are not used to train the vendor’s models or anyone else’s;',
  soc2: 'a current SOC 2 report or an equivalent independent security audit, shared under NDA where needed;',
  'named-models': 'which model providers process the organization’s data and where that processing happens;',
  'approval-controls': 'what actions the AI can take, which of them require a person’s approval, and how the organization configures those controls;',
  'audit-log': 'a record of what the AI proposed, who approved it, and what changed, available to the organization;',
  dpa: 'a data processing agreement and a current list of subprocessors, with notice before it changes;',
  'off-switch': 'the ability to turn AI features off, per feature or entirely, without losing access to the organization’s data;',
  export: 'export of the organization’s data in a usable format and confirmed deletion when the relationship ends;',
};

const POSTURE                                                       = {
  'draft-only': {
    label: 'Draft-only posture',
    summary: 'AI prepares; people decide. Nothing AI produces reaches a donor, a record, or a ledger until a named person approves it.',
  },
  'approve-routine': {
    label: 'Approved-routine posture',
    summary:
      'AI prepares, and approved routine steps may run. Anything outbound, financial, or about an individual still waits for a person.',
  },
  undecided: {
    label: 'Starting posture: draft-only',
    summary: 'AI prepares; people decide. Whether routine, low-risk steps may run under standing approval goes to the board with a recommendation from the approver.',
  },
};

function postureFor(input             )                                     {
  const p = POSTURE[input.autonomy];
  return { label: p.label, summary: p.summary.replace('the approver', approverNoun(input.approver)) };
}

function formatDate(d      )         {
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
}

function joinList(items          )         {
  if (items.length <= 1) return items[0] ?? '';
  if (items.length === 2) return `${items[0]} and ${items[1]}`;
  return `${items.slice(0, -1).join(', ')}, and ${items[items.length - 1]}`;
}

export function buildPolicy(input             , preparedOn       = new Date())                 {
  const org = label.orgType(input.orgType);
  const approver = approverNoun(input.approver);
  const Approver = approver.charAt(0).toUpperCase() + approver.slice(1);
  const cadence = cadenceNoun(input.reviewCadence);
  const cadenceBare = cadenceShort(input.reviewCadence);
  const posture = postureFor(input);
  const noPersonalData = input.dataScope.includes('none');
  const touchesFinance = input.dataScope.includes('finance') || input.workflows.includes('reconciliation') || input.workflows.includes('gift-processing');
  const strictSensitive = input.sensitiveHandling !== 'approved-only';

  const sections               = [];

  sections.push({
    id: 'purpose',
    number: '1',
    heading: 'Purpose and scope',
    summary: `Sets the policy’s reach for a ${org.toLowerCase()} organization: staff, volunteers, contractors, and board members, and every AI tool they use on its behalf.`,
    blocks: [
      {
        type: 'p',
        text: 'This policy sets out how the organization uses artificial intelligence (AI) in its work: what AI tools may and may not touch, who approves their use, how people stay accountable for the results, and how the board stays informed.',
      },
      {
        type: 'p',
        text: 'It applies to staff, volunteers, contractors, and board members who use AI tools on the organization’s behalf, whether the capability is built into a platform the organization already runs or is a standalone service, and whether it is free or paid.',
      },
      { type: 'p', text: ORG_NOTE[input.orgType] },
      {
        type: 'p',
        text: 'Where this policy conflicts with law, a funder agreement, or a more specific policy (privacy, records retention, gift acceptance, personnel), the stricter rule applies.',
      },
    ],
  });

  sections.push({
    id: 'principles',
    number: '2',
    heading: 'Principles',
    summary: 'Six commitments the rest of the policy applies: mission first, human-led, proportionate, transparent, secure, accountable.',
    blocks: [
      { type: 'p', text: 'Every use of AI at the organization is measured against these commitments.' },
      {
        type: 'bullets',
        items: [
          'Mission first. AI is used where it returns time and attention to the people the organization serves and the relationships that sustain it.',
          'Human-led. People remain accountable for every decision, every communication, and every record. AI prepares work; it does not own it.',
          'Proportionate. The organization adopts AI where the benefit is clear and the risk is understood, and declines it where either is not.',
          'Transparent. Donors, clients, members, and partners are told how AI is used when it matters to them, in plain language.',
          'Secure. Personal and financial information stays inside systems the organization has approved and controls.',
          'Accountable. AI use is recorded, reviewable, and reported to the board.',
        ],
      },
    ],
  });

  const uses = input.workflows.map((w) => `${label.workflow(w)}. ${WORKFLOW_USE[w].use} ${WORKFLOW_USE[w].limit}`);
  const notPermitted = [
    'Entering donor, client, member, or employee personal information into any AI tool that is not on the approved register.',
    input.autonomy === 'approve-routine'
      ? 'Allowing an AI tool to send a communication, move money, or change a giving or financial record without a person’s approval of that specific action.'
      : 'Allowing an AI tool to send a communication, change a record, post a financial entry, or take any other action on its own.',
    'Using AI to make or recommend eligibility, employment, discipline, or benefit decisions about an individual.',
    'Generating content that presents itself as written by a real person who did not review it, or that imitates a donor, client, or public figure.',
    'Using AI output as fact without checking it against a source the organization trusts.',
  ];
  sections.push({
    id: 'approved-uses',
    number: '3',
    heading: 'Approved uses',
    summary: `Names the ${input.workflows.length === 1 ? 'one kind' : `${input.workflows.length} kinds`} of work AI may assist, the limit that applies to each, and the uses that are not permitted.`,
    blocks: [
      { type: 'p', text: 'The following uses are approved under this policy, subject to the oversight rules in section 5 and the data rules in section 4. Each approved use carries its own limit.' },
      { type: 'bullets', items: uses },
      { type: 'p', text: `Any use not listed here, including a new feature inside an already-approved tool, requires approval by ${approver} under section 6 before it begins.` },
      { type: 'p', text: 'The following are not permitted under any circumstances:' },
      { type: 'bullets', items: notPermitted },
    ],
  });

  const permitted = input.dataScope.filter((d) => d !== 'none').map((d) => DATA_PERMITTED[d]);
  const excluded = DATA_CATEGORIES.filter((d) => d.id !== 'none' && !input.dataScope.includes(d.id)).map((d) => DATA_SHORT[d.id]);
  const dataBlocks             = [];
  if (noPersonalData) {
    dataBlocks.push({
      type: 'p',
      text: 'AI tools may be used only on content that identifies no individual: public information, the organization’s own published material, and internal documents from which names and identifying details have been removed. No donor, client, member, employee, or volunteer record enters an AI tool.',
    });
  } else {
    dataBlocks.push({ type: 'p', text: 'AI tools approved under section 6 may work with the following categories of the organization’s data, and only within the approved uses in section 3:' });
    dataBlocks.push({ type: 'bullets', items: permitted });
    if (excluded.length > 0) {
      dataBlocks.push({ type: 'p', text: `The following categories are excluded from AI tools until this policy is revised: ${joinList(excluded)}.` });
    }
  }
  dataBlocks.push({
    type: 'p',
    text: strictSensitive
      ? 'Sensitive categories, including health information, information about minors, financial account and payment card numbers, government identifiers, and information about a person’s beliefs or immigration status, are kept out of AI tools entirely.' +
        (input.sensitiveHandling === 'undecided'
          ? ` This is the starting rule; ${approver} will bring a recommendation on whether any sensitive category may be handled inside an approved platform to the board at the next review.`
          : '')
      : 'Sensitive categories, including health information, information about minors, financial account and payment card numbers, government identifiers, and information about a person’s beliefs or immigration status, may be handled only inside platforms approved for that purpose under a written agreement covering confidentiality, use, retention, and deletion, and never in a general-purpose or consumer AI tool.',
  });
  dataBlocks.push({
    type: 'p',
    text: 'Consumer AI tools, meaning any service used under a personal account or without an organizational agreement, may be used only with public information and the organization’s own published material. Personal data of any kind never enters them.',
  });
  dataBlocks.push({
    type: 'p',
    text: 'Communication preferences, do-not-contact requests, and consent recorded on a constituent’s record apply to AI-assisted work exactly as they apply to a person.',
  });
  sections.push({
    id: 'data',
    number: '4',
    heading: 'Data AI may use',
    summary: noPersonalData
      ? 'Restricts AI to content that identifies no one, and keeps every personal record out.'
      : `Permits ${permitted.length} data ${permitted.length === 1 ? 'category' : 'categories'}, excludes the rest, and ${strictSensitive ? 'keeps sensitive categories out of AI tools entirely' : 'confines sensitive categories to approved platforms under agreement'}.`,
    blocks: dataBlocks,
  });

  const oversight             = [{ type: 'p', text: 'AI systems draft, recommend, and prepare. They do not decide, and they do not act in the organization’s name.' }];
  if (input.autonomy === 'approve-routine') {
    oversight.push({
      type: 'p',
      text: 'Routine, low-risk steps, for example logging an activity, tagging a record, or creating a task for a staff member, may run after a person has approved the workflow that produces them and while that approval remains on file. Any communication to a donor, funder, client, member, or the public, any change to a giving or financial record, any action that involves money, and any action about a specific individual’s eligibility or standing waits for a person to approve that specific action.',
    });
  } else {
    oversight.push({
      type: 'p',
      text: 'No communication, record change, financial entry, or other action prepared by an AI tool takes effect until a named person has reviewed it and approved it. Approval means a person read the specific item, not that a workflow was switched on.',
    });
    if (input.autonomy === 'undecided') {
      oversight.push({
        type: 'p',
        text: `This is the starting posture. ${Approver} will bring the board a recommendation on whether routine, low-risk steps may run under standing approval, with the specific steps named, at the next review.`,
      });
    }
  }
  const reviewRule                              = {
    'relationship-owner': 'The staff member who owns the relationship reviews and approves every AI-drafted message to that donor, funder, client, or member before it is sent, and is accountable for its content.',
    supervisor: 'A supervisor or a second reviewer, not the person who requested the draft, reviews and approves every AI-drafted message to a donor, funder, client, or member before it is sent.',
    tiered: 'The staff member who owns the relationship reviews routine AI-drafted messages. Messages to major donors, proposals and reports to funders, and any message about a gift dispute or a sensitive matter are also approved by a supervisor before they are sent.',
  };
  oversight.push({ type: 'p', text: reviewRule[input.staffReview] });
  oversight.push({
    type: 'p',
    text: 'Staff check AI output against the system of record before relying on it, and correct the record when the output was wrong. Where an AI tool shows its sources, staff read the source, not just the summary.',
  });
  if (touchesFinance) {
    oversight.push({
      type: 'p',
      text: 'Gift amounts, designations, receipts, journal entries, and reconciliations are confirmed by the staff member responsible for them. AI may prepare and flag; finance staff post.',
    });
  }
  sections.push({
    id: 'oversight',
    number: '5',
    heading: 'Human oversight and approval of AI output',
    summary: `${posture.label.replace('Starting posture: draft-only', 'Draft-only to start')}. ${label.staffReview(input.staffReview)} signs off before an AI draft reaches a donor or funder.`,
    blocks: oversight,
  });

  const approvalSteps = [
    `The request names the tool, the intended use, the data categories involved, and the actions the tool can take on its own.`,
    `${Approver} checks the request against sections 3 and 4 and against the vendor requirements in section 7, and asks IT or a security advisor to review anything that connects to the organization’s systems.`,
    input.approver === 'board-committee'
      ? 'The committee decides, records its decision, and reports it to the full board at the next meeting.'
      : input.approver === 'executive'
        ? 'The Executive Director decides, records the decision, and reports new approvals to the board at the next meeting.'
        : `${Approver} decides and records the decision. The Executive Director reports new approvals to the board at the next meeting.`,
    'Approved tools and uses are entered in the AI tool register (Appendix A) with the date, the approved uses, the data categories, and the write capability granted.',
    'Approval may be conditional or time-limited, and it is withdrawn if a vendor changes its terms or the tool is used outside its approved scope.',
  ];
  sections.push({
    id: 'approving-tools',
    number: '6',
    heading: 'Approving AI tools and new uses',
    summary: `${Approver} approves every new tool and every new use, records it in the register, and can withdraw approval.`,
    blocks: [
      { type: 'p', text: `Before a new AI tool, or a new use of an existing tool, is adopted, it is approved by ${approver}. The process is:` },
      { type: 'numbered', items: approvalSteps },
      {
        type: 'p',
        text: touchesFinance
          ? 'Any tool that touches gift, receipting, or accounting data is also reviewed by the finance lead before approval.'
          : 'Any tool that later touches financial data is also reviewed by the finance lead before approval.',
      },
    ],
  });

  const asks = input.vendorRequirements.map((v) => VENDOR_ASK[v]);
  asks[asks.length - 1] = asks[asks.length - 1].replace(/;$/, '.');
  sections.push({
    id: 'vendors',
    number: '7',
    heading: 'Vendor and tool requirements',
    summary: `Every AI vendor, and every existing vendor adding AI features, confirms ${asks.length} ${asks.length === 1 ? 'item' : 'items'} in writing before approval.`,
    blocks: [
      { type: 'p', text: 'Before approval, and again when an existing vendor adds AI features to a product the organization already uses, the organization asks the vendor to confirm in writing:' },
      { type: 'bullets', items: asks },
      { type: 'p', text: `Confirmations are kept with the register entry. If a vendor cannot confirm an item, ${approver} decides whether to proceed with a documented, time-limited exception under section 10, or to decline.` },
      { type: 'p', text: 'The same questions are put to any consultant or agency that uses AI tools on the organization’s data.' },
    ],
  });

  const disclosureText                             = {
    always: 'The organization tells the recipient whenever AI helped produce a communication to a donor, funder, client, member, or the public, in a short plain-language line. Internal drafts and grammar or formatting help do not require disclosure.',
    material: 'The organization tells the recipient when AI produced the substance of a communication to a donor, funder, client, member, or the public. Help with grammar, formatting, translation, or summarizing the organization’s own material does not require disclosure. When in doubt, disclose.',
    'on-request': 'The organization describes how it uses AI in its public-facing materials, including its website, and answers any donor, funder, client, or member who asks how AI was involved in a specific communication, fully and promptly. Public content produced substantially by AI is labeled.',
    undecided: 'Until the board decides otherwise, the organization tells the recipient when AI produced the substance of a communication to a donor, funder, client, member, or the public. Help with grammar, formatting, translation, or summarizing the organization’s own material does not require disclosure. When in doubt, disclose.',
  };
  sections.push({
    id: 'disclosure',
    number: '8',
    heading: 'Disclosure',
    summary: `Disclosure rule: ${DISCLOSURE_PHRASE[input.disclosure]}${input.disclosure === 'undecided' ? ' (a starting rule for the board to confirm)' : ''}. A person’s name on a message means that person reviewed it.`,
    blocks: [
      { type: 'p', text: disclosureText[input.disclosure] },
      { type: 'p', text: 'A person’s name on a message means that person reviewed it and stands behind it. AI tools never sign, and the organization does not present AI-generated voices, images, or video as a real person without that person’s consent and a clear label.' },
      { type: 'p', text: 'Grant applications and reports follow the funder’s own disclosure requirements where they are stricter than this section.' },
    ],
  });

  const ownerDuties = 'Owns the AI tool register, approves tools and uses, grants exceptions, receives incident reports, and prepares the board report.';
  const roleRows = [
    ['Board of directors', `Adopts this policy, receives a report ${cadenceBare}, approves material changes, and decides the open questions this draft flags.`],
    ...(input.approver === 'executive'
      ? [['Executive Director or CEO', `${ownerDuties} Accountable to the board for the policy as a whole and for the resources it needs.`]]
      : [
          [approverTitle(input.approver), ownerDuties],
          ['Executive Director or CEO', `Accountable to the board for the policy as a whole, for the resources it needs, and for ${approver}’s decisions.`],
        ]),
    ['Data owners', 'The development, finance, program, and HR leads are each accountable for how their data categories are used in AI tools and for the review rules in section 5.'],
    ['All staff, volunteers, and contractors', 'Use only approved tools within their approved scope, complete training, review AI output before relying on it, and report incidents.'],
  ];
  sections.push({
    id: 'roles',
    number: '9',
    heading: 'Roles and responsibilities',
    summary: `The board adopts and receives reports ${cadenceBare}; ${approver} owns the register and approvals; data owners and staff carry the day-to-day rules.`,
    blocks: [{ type: 'table', header: ['Role', 'Responsibility'], rows: roleRows }],
  });

  sections.push({
    id: 'training-incidents',
    number: '10',
    heading: 'Training, incidents, and exceptions',
    summary: 'Training at onboarding and annually; incidents reported within two business days; exceptions time-limited and logged.',
    blocks: [
      { type: 'p', text: 'Everyone covered by this policy completes a short training on it at onboarding and once a year, covering the approved tools, the data rules, and how to review AI output.' },
      {
        type: 'p',
        text: `An incident is any of the following: personal data entered into a tool that is not on the register; an AI-prepared communication, record change, or financial entry that took effect without the required review; an AI output that was relied on and turned out to be wrong in a way that affected a person; or a vendor security event involving the organization’s data. Incidents are reported to ${approver} within two business days, recorded, and reviewed for what should change.`,
      },
      { type: 'p', text: `Exceptions to this policy are granted in writing by ${approver}, name the reason and the safeguards, expire on a stated date, and are reported to the board at the next review.` },
    ],
  });

  const reportItems = [
    'the AI tool register, including tools added, changed, or withdrawn;',
    'exceptions granted and incidents recorded, with what changed as a result;',
    'the time returned to staff and how it was used, in the organization’s own terms;',
    'donor, client, or member feedback that mentions AI;',
    'open questions for the board, including any change to the oversight posture in section 5.',
  ];
  const openQuestions           = [];
  if (input.autonomy === 'undecided') openQuestions.push('Whether routine, low-risk steps may run under standing approval, and which ones.');
  if (input.sensitiveHandling === 'undecided') openQuestions.push('Whether any sensitive data category may be handled inside an approved platform under agreement.');
  if (input.disclosure === 'undecided') openQuestions.push('Which disclosure rule the organization adopts.');
  sections.push({
    id: 'review',
    number: '11',
    heading: 'Review and reporting',
    summary: `Reviewed ${cadence}, with a standing board report covering the register, exceptions, incidents, and outcomes.`,
    blocks: [
      {
        type: 'p',
        text:
          input.reviewCadence === 'on-change'
            ? 'This policy is reviewed once a year, and again whenever a new tool or a new data category is proposed, when a vendor materially changes its terms, or after a significant incident.'
            : `This policy is reviewed ${cadenceBare}, and sooner when a new category of data or a new category of AI action is proposed, when a vendor materially changes its terms, or after a significant incident.`,
      },
      { type: 'p', text: `${Approver} reports to the board at each review on:` },
      { type: 'bullets', items: reportItems },
      ...(openQuestions.length > 0
        ? [
            { type: 'p', text: 'This draft leaves the following questions for the board to decide at adoption or at the first review:' }            ,
            { type: 'bullets', items: openQuestions }            ,
          ]
        : []),
      { type: 'p', text: 'Adopted by the board of directors on ____________. Policy owner: ____________. Next scheduled review: ____________.' },
    ],
  });

  sections.push({
    id: 'register',
    number: 'Appendix A',
    heading: 'AI tool register',
    summary: 'The one-table record of every approved tool: uses, data, write capability, vendor confirmations, approval, and next review.',
    blocks: [
      { type: 'p', text: 'One row per approved tool or per AI feature inside an existing platform. Kept current by the policy owner; the board sees it at each review.' },
      {
        type: 'table',
        header: ['Tool and vendor', 'Approved uses', 'Data categories', 'Write capability', 'Vendor confirmations on file', 'Approved by and date', 'Next review'],
        rows: [
          ['', '', '', 'Read-only / approval-gated / none', '', '', ''],
          ['', '', '', '', '', '', ''],
          ['', '', '', '', '', '', ''],
        ],
      },
    ],
  });

  sections.push({
    id: 'resolution',
    number: 'Appendix B',
    heading: 'Draft board resolution',
    summary: 'Short resolution language the board can adopt with the policy.',
    blocks: [
      {
        type: 'p',
        text: `RESOLVED, that the Board of Directors adopts the Artificial Intelligence Use Policy dated ____________; directs ${approver} to maintain the AI tool register and to approve tools and uses under it; and requests a report on the organization’s use of AI ${cadence}.`,
      },
      { type: 'p', text: 'FURTHER RESOLVED, that the open questions identified in section 11 be brought to the Board for decision no later than the first scheduled review.' },
    ],
  });

  return {
    title: 'Artificial Intelligence Use Policy',
    subtitle: `Draft for board review · ${org} organization`,
    preparedLine: `Prepared ${formatDate(preparedOn)} with the Nonprofit AI Policy Template`,
    postureLabel: posture.label,
    postureSummary: posture.summary,
    sections,
    boardQuestions: buildBoardQuestions(input),
    disclaimer: DISCLAIMER,
  };
}


export function buildBoardQuestions(input             )                  {
  const approver = approverNoun(input.approver);
  const noPersonalData = input.dataScope.includes('none');
  const permitted = input.dataScope.filter((d) => d !== 'none').map((d) => DATA_SHORT[d]);
  const wantsNoTraining = input.vendorRequirements.includes('no-training');
  const wantsExport = input.vendorRequirements.includes('export');

  return [
    {
      q: 'What are we using AI for today, and who decided?',
      why: 'Boards worry about tools arriving through the side door: a free trial here, a feature switched on there.',
      answer: `Point to the register in Appendix A and name ${approver} as the approver of every tool and every new use. If the register is empty today, say so. An honest empty register is a better answer than a vague full one.`,
    },
    {
      q: 'What donor data can the AI see?',
      why: 'Donor trust is the asset. Directors want to know the boundary, not the feature list.',
      answer: noPersonalData
        ? 'Under this draft, none. AI works only on content that identifies no one. Say that plainly and describe what would have to change, and who would decide, before that boundary moves.'
        : `Name the permitted categories (${joinList(permitted)}) and the excluded ones, then the sensitive-category rule in section 4. Add that communication preferences and do-not-contact requests apply to AI-assisted work exactly as they apply to a person.`,
    },
    {
      q: 'Is our data training somebody else’s model?',
      why: 'This is the question directors have read about, and the one a vendor answer tends to blur.',
      answer: wantsNoTraining
        ? 'The policy requires every vendor to confirm in writing that our data, prompts, and outputs are not used to train their models or anyone else’s. Read the vendor’s written answer to the board, and note any vendor that has not answered.'
        : 'The draft does not yet require vendors to confirm this in writing. Decide with the board whether it should; most boards want it on the list in section 7.',
    },
    {
      q: 'Can the AI send something to a donor without a person seeing it?',
      why: 'One wrong acknowledgement to a major donor is the failure directors picture first.',
      answer:
        input.autonomy === 'approve-routine'
          ? `No. Routine internal steps may run under standing approval, but every message to a donor, funder, client, or member waits for a person. ${REVIEW_SIGNOFF[input.staffReview]} Explain which routine steps you mean, with examples.`
          : `No. Under this draft nothing AI prepares is sent, saved, or posted until a named person approves it. ${REVIEW_SIGNOFF[input.staffReview]}${input.autonomy === 'undecided' ? ' Tell the board you will bring a recommendation on routine automation, so the question is theirs to decide.' : ''}`,
    },
    {
      q: 'Who is accountable when it gets something wrong?',
      why: 'Directors are asking about themselves as much as about staff.',
      answer: `The person who approved the output is accountable for it, the data owner is accountable for the category, and ${approver} is accountable for the tool being on the register at all. Incidents are reported within two business days and reach the board at the next review.`,
    },
    {
      q: 'Will donors know when AI was involved?',
      why: 'Disclosure is where values become visible, and where a board can be embarrassed.',
      answer:
        input.disclosure === 'undecided'
          ? 'The draft starts with disclosure when AI produced the substance of a message, and asks the board to confirm or change that rule. Present the disclosure choices and let the board choose.'
          : `Yes, under the rule in section 8: ${DISCLOSURE_PHRASE[input.disclosure]}. Add the rule that a person’s name on a message means that person reviewed it.`,
    },
    {
      q: 'What happens to our data if we leave the vendor?',
      why: 'Lock-in is a governance risk, and the board owns the organization’s continuity.',
      answer: wantsExport
        ? 'Section 7 requires every vendor to confirm export in a usable format and confirmed deletion at exit. Ask for the answer in writing before the contract, not after.'
        : 'The draft does not yet require exit terms in writing. Consider adding export and deletion to section 7; it costs nothing to ask before signing.',
    },
    {
      q: 'How is this different from staff using a chatbot on their own?',
      why: 'Directors know this is already happening. They want to know the organization has noticed.',
      answer: 'Section 4 answers it: consumer tools under personal accounts may touch only public information and our own published material, never personal data. Pair that with training at onboarding and once a year, and with the register, so staff know which tools are approved.',
    },
    {
      q: 'Does this mean fewer staff?',
      why: 'Some directors hope so; more of them fear it. Both need a straight answer.',
      answer: 'No. The policy is written for human-led work: AI prepares, people decide and stay accountable. The measure of success is time returned to relationships and programs, reported to the board in the organization’s own terms, not headcount.',
    },
    {
      q: 'How will we know it is working, and when do we revisit this?',
      why: 'A policy with no review date is a document, not governance.',
      answer: `The policy is reviewed ${cadenceShort(input.reviewCadence)}, and sooner if a new tool, a new data category, a new kind of action, or an incident arrives. The report covers the register, exceptions and incidents, the time returned and how it was used, and any feedback that mentions AI.`,
    },
  ];
}


export function sampleInput()              {
  return {
    version: 1,
    orgType: 'human-services',
    revenueBand: '10m-15m',
    authorRole: 'executive',
    dataScope: ['public', 'contact', 'giving'],
    sensitiveHandling: 'excluded',
    workflows: ['prospect-research', 'donor-comms', 'reporting'],
    autonomy: 'draft-only',
    approver: 'executive',
    staffReview: 'tiered',
    disclosure: 'material',
    vendorRequirements: ['no-training', 'soc2', 'approval-controls', 'audit-log', 'export'],
    reviewCadence: 'on-change',
  };
}
