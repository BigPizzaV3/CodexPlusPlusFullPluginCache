# Research types, streams and batches

What each type is for, and what to report:

| Research type                   | Intended outcome                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ProblemDiscoveryAndValidation` | Findings about customer problems, how much they matter, current alternatives, and assumptions that need more testing. |
| `WinLoss`                       | Findings about buying decisions and the reasons deals were won or lost.                                               |
| `BuyerPersona`                  | Buying insights and an automatically generated Buyer Persona.                                                         |
| `Other`                         | Findings that address the research objective the user stated.                                                         |

## Insight categories

Insight categories differ by type. Problem discovery: Job-to-be-Done, Triggering Events, Desired Outcome, Solution Search and Evaluation, Experience of Using the Chosen Solution, Additional. Win/loss: Product in Focus, Triggering Events, Desired Outcomes, Solution Evaluation and Comparison, Reasons for Winning/Losing, Additional. Report in the categories that answer the question, starting with the summary. No fixed interview count establishes a pattern or validates a claim; explain the sources, contradictions and relevance. Research quality flags leading questions, shallow answers and weak commitments, so use it to improve the next round. Counts of how many interviews support an insight are evidence: report them when returned.

## Streams and batches

For one customer segment, different research types answer different questions, and they keep running side by side, not one after another:

| Stream                          | Question it answers                                                                                        | Cadence                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `ProblemDiscoveryAndValidation` | Is the problem real, important and unsolved for this segment? Which assumptions are wrong?                 | Can start synthetic for a first signal, then keeps taking real interviews. Run it again for each new segment or problem. |
| `BuyerPersona`                  | How do these buyers decide, what do they fear, what proof do they need? Messaging, pricing and objections. | Can also start synthetic. The persona is living: each interview added or removed refreshes it.                           |
| `WinLoss`                       | Why do deals close or fall through?                                                                        | Event-driven: add an interview after each win or loss. It exists once the user is selling.                               |
| `Other`                         | A specific question the three do not cover.                                                                | As needed.                                                                                                               |

- Streams are chosen by what the user needs to learn, not in a fixed order. Problem and buyer research can run at the same time for a segment, and neither has to finish first.
- A segment can have several research projects of the same type. Use them as **batches**: a new research when the user wants a fresh round (each quarter, each month, after a change), and new interviews added to the current research while a round is still running. The cadence is the user's choice. Do not start a new batch on your own initiative, and ask which they want when it is unclear: add to the current research, or start a new batch.
- Each research has its own analysis. To read a stream across batches, read each batch, combine the interview counts de-duplicated by interview ID, and report the batches separately, identified by name and `lastActivity`. `lastActivity` is the last activity, not a reporting period or a start date, so do not infer quarters or historical progress from it. If the user names the period for a batch, use their wording.
- A new `BuyerPersona` batch creates its own Buyer Persona automatically and requires a positive starting balance. No tool automatically links successive personas or compares batches; read each separately. Tell the user before creating one, and be clear which persona later work (asking it questions, positioning) should use.
- Synthetic starts are hypotheses. Add real interviews as they arrive and keep their findings distinct from the synthetic ones. Change which interviews are in a research only when the user asks.
- When the user asks "what next" for a segment, check all streams (`list_research` for the segment), including every batch: which exist, how many real, imported and synthetic completed interviews each holds, and whether analysis is current. Name the stream that is missing or thin and why it matters, even if the user asked about a different one.
- Start win/loss only when the user has real deals to learn from. Do not run it synthetically as a substitute.
