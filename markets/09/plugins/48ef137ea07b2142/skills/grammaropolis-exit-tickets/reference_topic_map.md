# Topic map

Routes a teacher's request ("an exit ticket on proper nouns," "grade 6 semicolons quiz") to a Grammaropolis department, topic, character, and the grades the topic is taught at. It also says which topics have a free lesson on grammaropolis.com, which decides the one optional pointer at the end of a key.

**Two-mode lookup.** If a Grammaropolis connector or MCP tool is available in this conversation, use it instead of this file; it's always current. This file is the fallback so the skill works with no outside tools.

**The pointer rule, in one place.** A key may end with at most one light pointer.

- **Free topic:** point to that topic's free lesson (URLs below). Frame it as a reteach resource: "If a good part of the class missed the key items, the free lesson at {URL} reteaches this."
- **Any other topic:** point to the department's page on grammaropolis.com (below), framed as "if your class wants more practice."
- Never construct a lesson URL by guessing a slug. Never state prices, discounts, or which grades a workbook covers. Leaving the pointer out is always acceptable.

**Grades taught.** The "Grades" column is where the topic is taught in the Grammaropolis catalog. A teacher can still ask for a check outside that range; write it, say in one line that the topic is usually taught at another grade, and tag the standard honestly.

---

## Parts of Speech

Department page: `https://grammaropolis.com/learn/pos`

| Topic | Character | Grades | Free lesson |
|---|---|---|---|
| Nouns (common and proper, concrete and abstract, collective, singular and plural) | Nelson the Noun | 1-8 | Yes: `https://grammaropolis.com/learn/pos/nelson/g{grade}` (for example `.../nelson/g2`) |
| Action verbs (including verb tense, subject-verb agreement, and verb mood at grade 8) | Vinny the Action Verb | 1-8 | No |
| Linking verbs | Lucy the Linking Verb | 1-8 | No |
| Adjectives (including articles and comparatives) | Jake the Adjective | 1-8 | No |
| Adverbs | Benny the Adverb | 1-8 | No |
| Pronouns (including relative pronouns from grade 4) | Roger the Pronoun | 1-8 | No |
| Conjunctions (FANBOYS, subordinating, correlative) | Connie the Conjunction | 1-8 | No |
| Prepositions | Li'l Pete the Preposition | 1-8 | No |
| Interjections | Izzy the Interjection | 1, 3, 6, 8 | No |

## Punctuation Department

Department page: `https://grammaropolis.com/learn/pd`

| Topic | Character | Grades | Free lesson |
|---|---|---|---|
| End marks (period, question mark, exclamation mark) | Officer Period, Detective Question Mark, Sergeant Exclamation Mark | 1-8 | Yes: `https://grammaropolis.com/learn/pd/end-marks/g{grade}` |
| Commas | Chief Comma | 1-8 | No |
| Capitalization | The Mayor | 1-5 | No |
| Semicolons and colons | Sheriff Semicolon, Deputy Colon | 5-8 | No |
| Apostrophes (contractions and possessives) | Prosecutor Apostrophe | 2-4 | No |
| Quotation marks (dialogue and titles) | Court Reporter Quotation Marks | 3-5 | No |
| Parentheses and brackets | Defense Attorney Parentheses, Assistant Defense Attorney Brackets | 6-8 | No |
| Hyphens and dashes | Hyphen, Dash | 6-8 | No |

## Sentence Factory

Department page: `https://grammaropolis.com/learn/sf`. The Mayor hosts the Sentence Factory; there's no separate character per topic.

| Topic | Grades | Free lesson |
|---|---|---|
| Subjects and predicates | 1-8 | Yes: `https://grammaropolis.com/learn/sf/subject-predicate/g{grade}` |
| Complete sentences, fragments, and run-ons | 1-8 | No |
| Sentence types (declarative, interrogative, imperative, exclamatory) | 1-3 | No |
| Sentence structures (simple, compound, complex, compound-complex) | 3-8 | No |
| Sentence combining | 3-8 | No |
| Sentence objects (direct and indirect objects) | 3-6 | No |
| Sentence complements (predicate nominatives and predicate adjectives) | 4-8 | No |
| Phrases and verbals (gerunds, participles, infinitives) | 4-8 | No |
| Clauses (independent and dependent) | 5-8 | No |

Verbals are Vinny the Action Verb in costume (a gerund is Vinny dressed for a noun's job, a participle is Vinny dressed for an adjective's job), never Nelson or Jake.

## The Writing Company

Department page: `https://grammaropolis.com/learn/wc`

| Topic | Grades | Free lesson |
|---|---|---|
| Specific nouns (trading a vague noun for a precise one) | 1-8 | Yes: `https://grammaropolis.com/learn/wc/specific-nouns` |
| Write a Story (narrative) | 1-8 | No |
| Write to Explain (informative) | 1-8 | No |
| Write to Persuade (opinion and argument) | 1-8 | No |
| Write to Describe (descriptive) | 1-8 | Yes: `https://grammaropolis.com/learn/wc/write-to-describe/g{grade}` |
| Craft moves: strong verbs, show don't tell, sentence variety, formal and informal voice, three-part structure | 1-8 | No |

Writing checks test what has one right answer: which sentence states the opinion, which transition shows contrast, which detail supports the reason, what order the events go in. They never ask which hook or ending is "best," because that's taste. Scoring a student's full piece of writing is rubric work, not an exit ticket.

## Wonderful Words

Department page: `https://grammaropolis.com/learn/ww`

| Topic | Grades | Free lesson |
|---|---|---|
| Smile or Frown (synonyms and antonyms) | 1-8 | Yes: `https://grammaropolis.com/learn/ww/smile-or-frown` |
| Themed vocabulary units | 1-8 | The first unit at each grade: `https://grammaropolis.com/learn/ww/unit-1/g{grade}`; the rest aren't free |
| Word relationships: meaning, word families (prefixes, suffixes, roots), context clues, words with more than one job, formal and informal register, figurative language | 1-8 | No |

This skill doesn't know any unit's word list. For a unit check, ask the teacher for the words; otherwise write the check on the word-relationship skill with your own words.

---

## Quick lookup by common teacher phrasing

| A teacher says... | Route to |
|---|---|
| "nouns," "proper nouns," "plural nouns," "abstract nouns" | Parts of Speech: Nelson (free) |
| "verbs," "action verbs," "verb tense," "irregular verbs," "verb mood," "subjunctive" | Parts of Speech: Vinny |
| "linking verbs," "helping verbs" | Parts of Speech: Lucy (linking); Vinny (helping verbs in a verb phrase) |
| "adjectives," "articles," "comparative and superlative" | Parts of Speech: Jake |
| "adverbs," "good vs. well" | Parts of Speech: Benny |
| "pronouns," "I vs. me," "antecedents," "pronoun case," "relative pronouns," "who, which, that" | Parts of Speech: Roger |
| "conjunctions," "FANBOYS," "either/or" | Parts of Speech: Connie |
| "prepositions," "prepositional phrases" | Parts of Speech: Li'l Pete |
| "interjections" | Parts of Speech: Izzy |
| "end punctuation," "periods and question marks" | Punctuation Department: End Marks (free) |
| "commas," "commas in a series," "comma splices" | Punctuation Department: Commas |
| "capital letters," "capitalization" | Punctuation Department: Capitalization |
| "semicolons," "colons" | Punctuation Department: Semicolons and colons |
| "apostrophes," "contractions," "possessives," "its vs. it's" | Punctuation Department: Apostrophes |
| "quotation marks," "dialogue punctuation," "titles" | Punctuation Department: Quotation marks |
| "parentheses," "brackets" | Punctuation Department: Parentheses and brackets |
| "hyphens," "dashes" | Punctuation Department: Hyphens and dashes |
| "subjects and predicates," "parts of a sentence" | Sentence Factory: Subjects and predicates (free) |
| "subject-verb agreement," "is or are," "agreement" | Parts of Speech: Vinny (subject-verb agreement) |
| "fragments," "run-ons," "complete sentences" | Sentence Factory: Complete sentences |
| "kinds of sentences," "statements, questions, commands" | Sentence Factory: Sentence types |
| "simple, compound, complex sentences" | Sentence Factory: Sentence structures |
| "direct objects," "indirect objects" | Sentence Factory: Objects |
| "gerunds," "participles," "infinitives" | Sentence Factory: Phrases and verbals |
| "misplaced modifiers," "dangling modifiers" | Parts of Speech: Benny (a grade 7 standard) |
| "clauses," "dependent clauses" | Sentence Factory: Clauses |
| "opinion writing," "argument," "persuasive" | Writing Company: Write to Persuade |
| "informative," "expository" | Writing Company: Write to Explain |
| "narrative," "personal narrative," "story writing" | Writing Company: Write a Story |
| "transitions," "linking words" | Writing Company: the matching mode |
| "specific nouns," "precise words" | Writing Company: Specific Nouns (free) |
| "synonyms and antonyms" | Wonderful Words: Smile or Frown (free) |
| "prefixes," "suffixes," "roots," "context clues," "figurative language," "similes and metaphors" | Wonderful Words: the matching word-relationship move |
| "vocabulary," "this week's words" | Wonderful Words: ask for the word list |
| "spelling test," "spelling words" | Outside this skill; say so plainly |
