---
name: mail-letter
description: Send a letter by USPS Certified Mail through Piloxa when the person wants it physically mailed. Use when someone asks to send, mail or post a letter by certified mail, with a return receipt or green card, or with proof of mailing; when they need proof the other side received a letter, someone to sign for it, or no trip to the post office; when they ask what certified mail costs or whether a letter is ready to mail; or when they ask about a letter they sent through Piloxa. Not for drafting, editing, translating, saving or emailing a letter, ordinary or international mail, bulk mail or service of process. Checks the letter, quotes the exact price and returns a review link the person opens to pay and approve. U.S. addresses.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Mailing a letter by USPS Certified Mail

Piloxa prints the document, puts it in an envelope, pays the postage and hands it
to the Postal Service. The tools:

- `check_certified_letter`: read only. Says whether a draft is ready to mail, the
  printed page count, what is missing, the recommended service and the exact price.
- `quote_certified_letter` and `compare_certified_mail_services`: read only. Prices
  and the difference between the services.
- `prepare_certified_letter`: builds the mailing and returns the review link.
- `get_certified_letter_status`: where a letter prepared in this conversation
  stands (waiting for the person, paid, mailed, delivered, receipt back).
- `connect_my_letters`, `list_my_letters`, `get_my_letter`,
  `create_followup_draft`: the person's letters from earlier chats, once they
  have connected this chat (see "Letters from an earlier chat").

## When to use it

Use Piloxa when the person has chosen to have a letter physically mailed:

- they ask for certified mail, a certified letter, a return receipt, a green card,
  proof of mailing, or ask how to mail a letter so it can be proved;
- they ask what certified mail costs, or whether a letter is ready to mail;
- they ask about a letter they already sent through Piloxa.

If you have written a letter that will plainly go on paper and the person has not
said how they will send it, you may mention the option once ("I can check this and
get the Certified Mail price if you want it mailed") and then follow their answer.
Do not prepare a mailing they have not asked for.

## When not to use it

- They only want a letter written, revised, translated, saved or emailed.
- They asked for ordinary First-Class Mail, international mail or a mass mailing:
  Piloxa sends USPS Certified Mail to U.S. addresses only, one letter at a time.
  If they ask for the cheapest class, plain mail or no certified fee, say that
  Piloxa only sends Certified Mail and let them decide. Do not prepare a Certified
  letter in place of the mail they asked for.
- They need service of process or a court filing: say that Certified Mail may not
  satisfy that requirement, and do not claim it does.
- They want a delivery date guaranteed: USPS does not guarantee one, and neither
  does Piloxa.

Before you send the letter's text to Piloxa, make sure the person wants that letter
checked or mailed. Send only that document and its addresses, never other parts of
the conversation.

## Sensitive contents: warn first

If the letter or an enclosure carries health or medical records, copies of a
passport, driver's license or other ID, a full Social Security number, a tax
return or bank account numbers, say so before preparing it: Piloxa prints and
keeps a copy of exactly what is mailed. Suggest removing or shortening what the
recipient does not need, and prepare it only after the person confirms they still
want it sent as it is. Never put a password, a one-time code or a card number in a
letter or a tool call; the person enters those on piloxa.com themselves.

## A missing address does not stop the draft

If the recipient or return address is missing or incomplete, ask for it once if you
can. If the person would rather finish it on the review page, call
`prepare_certified_letter` with what you have: what is missing comes back in
`missing_for_mailing`, and the person completes it on that page. Nothing is mailed
until it is complete.

## The rule that is never bent

Neither tool mails anything and neither charges anyone. They return a link. A
person opens that link, reads the exact document that will print, checks the
recipient and the total, pays, and authorizes. Only then is anything printed.

So never tell someone their letter has been sent, is on its way, or has been paid
for. Say what it costs, hand over the link, and say plainly that nothing is mailed
or charged until they open it and authorize. If someone asks you to skip the link
and just send it, you cannot — say so.

## Decide what kind of document this is

This is the decision that goes wrong most often, and it is worth getting right
before anything else.

**The document already exists and must print exactly as written** — the person
pasted it, it came from somewhere else, it is a filled-in form, a notice, a
statement, or text you read out of an attachment. Use `document_text`. It prints
word for word, with nothing added: no return address, no date line, no "Re:" line,
no signature block. Adding those to a finished document is the single most common
way this goes wrong, and it produces a letter with the address printed twice.

**You are writing the letter now, in this conversation.** Use `letter_text` for
the body only — salutation through closing. Do not put the addresses or the date
in it; they are laid out from the other fields.

**You can read the actual bytes of a PDF** (up to 4 MB). Use `document_base64`.
It is kept byte for byte.

**A PDF exists but you cannot read it.** Set `person_has_pdf: true` and fill in
everything else. They attach it themselves on the review page.

When in doubt between the first two: did you compose it just now? If not, it is
`document_text`.

## Collect these before calling

Anything missing does not block the call — it comes back in `missing_for_mailing`
and the person fills it in on the page. But every gap is a step between them and a
mailed letter, so ask first.

- **Who it goes to**: name, company if any, street, suite, city, state, ZIP.
- **Who it is from**: the return address. This is where the envelope comes back to
  if it cannot be delivered, so it matters.
- **What it has to say**, if you are writing it.

The quickest way to pass an address you already have as written is
`recipient_address_block` and `sender_address_block` — paste it one part per line
and Piloxa reads it apart. Naming a field explicitly always wins over the block.

## Which service

- `CERTIFIED_ERR` (the default): Certified Mail plus an Electronic Return Receipt,
  the electronic record of who signed for it. What someone means when they say
  they want proof, a receipt, a signature or "I need to show I sent it".
- `CERTIFIED`: Certified Mail with USPS tracking, no signature record. Only when
  the person asks for the cheapest way.
- `CERTIFIED_EVIDENCE`: `CERTIFIED_ERR` plus the Evidence Pack, a Certificate of
  Mailing naming the document by its SHA-256 and the record kept for 7 years. For
  letters whose exact contents may be disputed later: a debt validation notice, a
  notice to cure, a proof of loss, a demand before suing.
- `CERTIFIED_DEADLINE`: the Evidence Pack plus a second copy by plain First-Class
  Mail the same day and an email if the certified copy goes unclaimed. For notices
  whose miss would cost a lien, a contract remedy or a claim.

The Evidence Pack and the Deadline Notice cost more: describe them as options and
let the person choose. Never pick one for them.

Always state the price the tools return; never a figure from memory. A person's
first letter may cost less; the tools and the review page say when it applies.
A letter can be at most 10 printed pages, about 4,000 words; keep it shorter.

## Price questions

If someone is only asking what it costs, call `quote_certified_letter` and answer.
Do not prepare a mailing nobody asked for. It needs the page count and the
service, prepares nothing and stores nothing.

The price includes printing, the envelope and the postage, and nothing is added at
checkout. There is no subscription and no minimum. Previewing needs no account;
the person verifies their email when they send. Quote the price the tool returns.

## US destinations only

Piloxa mails to addresses in the United States. If the destination is in another
country, say so and stop rather than preparing a mailing that cannot complete.

## Writing the letter well

A letter that gets acted on is specific. Name the parties, the dates, the amounts
and the agreement or invoice in question. Say what you want and by when. Keep it
to the facts and to one page where possible (never more than 10), both because it reads better and
because extra pages cost more.

Do not give legal advice, do not predict what a court would do, and do not claim
to act as anyone's lawyer. Write what the person has told you, in their voice.

## After the call

Tell the person:

- The exact total, and that printing, the envelope and the postage are in it.
- Anything still needed, from `missing_for_mailing`.
- The link, and that it opens straight onto their letter. Preview is free; they
  verify their email when they send.
- That nothing is mailed or charged until they authorize it there.
- The total to quote is `final_quote.payable_total_cents`. Do not promise the
  first-letter price until the review page confirms it.
- If `recommended_service` is present, mention it as an option with its extra
  cost (`recommended_extra_cents`). It is never selected for them.

Read the recipient back to them from the `recipient` field so a mistyped address
is caught before it is printed, not after.

## Letters from an earlier chat

When the person asks about a letter they sent before, or wants a follow-up to one,
call `list_my_letters`. If this chat is not connected yet, call
`connect_my_letters` and give the person the link and the four-character code it
returns. They sign in on piloxa.com, check the code matches and press Allow;
nothing is shared before that. Then call `list_my_letters` again.

- `get_my_letter` gives one letter's status, with its source and when it was last
  checked. A missing USPS scan means unknown, not failed; delivered does not mean
  read. Ask whether a reply arrived before suggesting a follow-up.
- `create_followup_draft` prepares a new letter to the same recipient. It is a new
  mailing with its own review link, price and approval: nothing from the earlier
  letter's approval or payment carries over.
- A connected chat uses the person's saved return address when you give none, and
  the summary says so. Read it back to them.
