---
name: finding-contractors
description: Find, filter and inspect the contractors a company pays through Wingspan, including who still has onboarding paperwork outstanding. Use for "who do we pay", "list our contractors", "find [name]", "who has not signed up yet", "who is missing their W-9", "who is blocked by the certificate of insurance", "which contractors are blocked from being paid", "can we pay [name]", "what is [name]'s status", "who is on this engagement".
---

# Finding contractors

The shared rules for every call — ids, paging, previewing a write, what the
tools cannot do — are in the `using-wingspan-tools` skill. Apply them here.

A **contractor** is a person or business the company pays; Wingspan also calls
this a *payee*. An **engagement** is a named working arrangement a contractor
is assigned to. A **requirement** is something a contractor must satisfy before
they can be paid, such as a tax form or an insurance certificate.

Two tools cover this: `search_contractors` lists and filters, and
`get_contractor` reads one contractor in full. Every row a search returns
carries a `contractorId`, and that is the id `get_contractor` takes.

## Listing and searching

`search_contractors` with no arguments lists active contractors, newest first,
25 to a page.

| Argument | What it does |
| --- | --- |
| `query` | Free-text search over name, email, company and your own external id. At least two characters. Results come back by relevance. |
| `status` | Which screen tab to read: `active`, `notSignedUp`, `incomplete`, `complete`, `archived`. |
| `onboarding` | Where the working relationship stands: `Pending`, `Active`, `Inactive`. |
| `eligibility` | `blocked` or `clear`, as reported by the search API. Missing eligibility is neither; use the verification workflow below before concluding nobody is blocked. |
| `engagement` | Only contractors assigned to this engagement, by name or id. |
| `batch` | Only contractors loaded by one bulk import in the Wingspan app, by that import's batch id. |
| `requirement` | Only contractors whose copy of this requirement is in `requirementState`. |
| `requirementState` | Which state that requirement is in. Defaults to `incomplete`. |
| `sortBy` | `createdAt` or `updatedAt`. One field per call. |
| `sortDirection` | `asc` or `desc`. Defaults to `desc`. Refused without `sortBy`. |
| `limit` | Rows per page, 1 to 100. Defaults to 25. |
| `pageToken` | Continue a previous page. Pass the previous result's `pagination.nextPageArgs` back unchanged. |
| `accountId` | Read one child account of an organization instead of the signed-in account. Only when the user names one; `who_am_i` lists them. |

Use the current tool schema for supported filters. Do not invent filters or assume this table is exhaustive.

## Two separate questions, two separate arguments

`status` is the tab strip from the Wingspan app, and it mixes the working
relationship with paperwork: `incomplete` and `complete` are a summary of
requirements, while `notSignedUp` and `archived` are about the relationship.

`onboarding` is the relationship on its own, and every row reports it whatever
you filtered on.

The two combine, so `status: "notSignedUp"` with `onboarding: "Pending"` means
"invited, has not signed up". One pair is refused rather than answered:
`onboarding: "Inactive"` together with `status: "active"`, because `active`
excludes archived contractors and `Inactive` requires them. `status` defaults
to `active`, so leaving it out is the same pair — send `onboarding: "Inactive"`
with `status: "archived"`.

One more thing worth passing on: `onboarding: "Inactive"` matches archived
contractors, but a contractor who only rejected their invite is not matched.
The underlying search cannot express "archived or rejected" in one query, and
the result's `note` says so.

**One kind of contractor no filter finds:** someone archived before any
engagement was assigned to them. Every `status` tab except `active` needs a
paperwork or engagement summary they never got, and `active` excludes anyone
archived — so no combination of `status` and `onboarding` returns them. Read one
with `get_contractor` if you have their `contractorId`; its headline reads
Archived. Every row that does come back carries its own `archived` field,
whatever you filtered on.

## Who is blocked from being paid

Use `search_contractors` with `eligibility: "blocked"` as a candidate search,
not proof that every other contractor is eligible. Preserve the user's account
and roster scope. Do not add an `onboarding: "Active"` filter: a contractor
still onboarding can have a non-eligible engagement.

If the blocked search is empty, fails, or conflicts with the user's observation,
read the roster without the eligibility filter. Also verify individual records
whenever roster rows have `paymentEligibility: null`, empty `engagements`, or
missing requirement summaries. These values mean unknown in search, not clear.
Search has been observed returning no engagements while detail returns actual
assignments; do not recommend assigning an engagement based only on search.

Call `get_contractor` using each candidate or unknown row's `contractorId`.
For a small roster, inspect every returned row when checking a negative result.
For larger rosters, respect paging and the user's requested scope; explicitly
state how many records were checked and whether further pages or unknowns
remain. Never turn a partial check or failed detail call into "nobody is blocked".

For payment eligibility, inspect `engagements[].paymentsEligibility` and the
engagement status. Report `NotEligible` as ineligible for that engagement;
include a `Created` engagement instead of discarding it for not being
`Activated`. An eligible engagement does not cancel out another non-eligible
engagement. Distinguish historical inactive assignments from current work.
Report `Eligible` at the engagement level, not as a guarantee that funds can
be delivered. Missing or unrecognized eligibility remains unknown.

Explain outstanding requirements using `requirementDetails`. Match a
requirement's `engagementIds` to the assignment's `payeeEngagementId`, not the
template `engagementId`. Report the returned statuses, such as
`PendingCompletion`. Separate confirmed engagement ineligibility from the
outstanding requirements: without placement-specific evidence, do not claim
each outstanding requirement independently blocks payment.

Use `alert` for the general onboarding headline, but do not let it override
explicit engagement eligibility. If it says invited or not signed up while
the Sign up requirement is completed, disclose that inconsistency rather
than choosing one as a proven explanation. When search and detail disagree,
report the detail's explicit engagement verdict and explain that the search
missed it. Indexing or mapping issues are hypotheses until independently
confirmed.

Only report no ineligible engagements found after checking the relevant scope;
include any unresolved records and coverage limits. Do not use absence from
the blocked search as evidence that everyone can be paid.

## Who still has a named requirement outstanding

Two calls, in this order.

1. `search_requirements` lists the requirements the company has configured.
   Each carries a `requirementDefinitionId`, the `blocking` value Wingspan
   holds for it, its grace period and how often it expires. Pick the one the
   user named. With no arguments it lists the ones still in use; it also takes
   `type` (one kind of requirement), `includeInactive` (show retired ones too),
   `limit`, `pageToken` and `accountId`, and nothing else.
2. `search_contractors` with `requirement` set to that id; its exact name also
   works, matched case-insensitively and in full, so a partial name will not
   resolve. Set `requirementState` to the state you want.

| `requirementState` | Means |
| --- | --- |
| `incomplete` | Outstanding — the contractor has not finished it. This is the default. |
| `pendingReview` | The contractor submitted something and the company has not reviewed it. |
| `complete` | Satisfied, whether the contractor or the company finished it. |
| `expiring` | Satisfied, but the expiry date is approaching. |
| `expired` | It lapsed and has to be renewed. |

A requirement the company rejected, or one whose underlying record was revoked
or failed, is reopened rather than failed — it reads as outstanding again, with
a reason recorded. There is no failed state. Say "reopened after review" rather
than "never started" when reporting one.

`requirementState` on its own is refused: it needs `requirement`.

Two things to say out loud when reporting the answer:

- **Not every outstanding requirement blocks a payment.** `blocking` on a
  definition is what Wingspan reports for that definition. A contractor's own
  copy can be blocking or not depending on where it was attached.
  `get_contractor` treats every incomplete requirement as blocking and does
  not read that setting; which placement merely tracks a requirement is visible
  only in the Wingspan app.
- **`gracePeriodDays` is a delay on the definition**, not a verdict about a
  person: it is the days from when a requirement is attached to a contractor
  before an outstanding copy starts holding up a payment. Inside that window an
  unfinished requirement does not block.

When interpreting requirement kinds or filtering by `type`, read
[references/requirement-types.md](references/requirement-types.md).

## When to read one contractor in full

Move to `get_contractor` once the question is about one person: "can we pay
them", "what is their status", "what is missing". It returns what the
Contractors detail screen shows. For general onboarding status, lead with
`alert`. For payment eligibility, use the engagement verification workflow
above. The headline can have one of these outcomes:

| `alert` says | Means |
| --- | --- |
| Contractor invited | Invited, has not signed up yet. |
| Tax information not shared | Signed up, but has not shared tax information with the company. |
| Archived | Someone at the company archived them. |
| Contractor is all set for now | Ready to be paid. |
| Payments eligibility pending | Signed up with nothing outstanding, but at least one active assignment is not cleared for payment. |
| Requirements expired | Something already satisfied has lapsed and needs renewing. |
| Requirements expiring soon | Something already satisfied is about to lapse. |
| Requirements incomplete | Something is outstanding. |

Only one applies, and the order above decides which. A contractor who is both
archived and missing tax information reads "Tax information not shared",
because that check comes first. This headline is not a substitute for the
explicit `paymentsEligibility` on each engagement.

"Tax information not shared" does not always mean the contractor must act — a
payer can supply and verify the details itself, in the Wingspan app.

`alert` can also be empty, when none of the checks above fire. Report that as
"nothing flagged" and fall back to the assignments and requirement list in the
same result rather than declaring the contractor payable.

`get_contractor` also returns their tax information and its verification
status, every engagement assignment with a count of outstanding requirements,
the full requirement list with expiry dates, whether they have a payout method
set up (somewhere for the money to land), and your own id for them.

## Two results to read carefully

**Missing search summaries do not prove there are no assignments.**
When search reports no engagements or paperwork summary, verify with
`get_contractor` before explaining the cause or recommending changes. A genuine
absence of assignments is different from missing indexed data.

**An assignment with no requirements shows "None required".** It also shows
whatever eligibility Wingspan reports. Do not infer from it. If such a
contractor cannot be paid, the fix is to attach one requirement in the Wingspan
app and have it completed; nothing else re-evaluates eligibility.

## A search that finds nobody

If a name search returns no rows and archived contractors were excluded, the
result reports how many archived contractors do match. Offer to look there
before telling the user the person does not exist.

## Finish these in the Wingspan app

- Creating or editing engagements, groups, worksites, custom fields and rate
  cards.
- Writing a requirement definition, and attaching one to an engagement or a
  group.
- Approving, rejecting, resetting or renewing one contractor's requirement, and
  extending an expiry date.
- Archiving or restoring a contractor.
- Everything the contractor does themselves: signing up, signing, uploading a
  document, verifying identity, adding a payout method.
- Sharing tax information, which is usually the contractor's step; a company
  that records and verifies a contractor's taxpayer details itself also does
  that in the app.
