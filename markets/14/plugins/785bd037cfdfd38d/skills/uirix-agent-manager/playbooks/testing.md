# Saved test questions

Topic `testing` · version 2026-10-25 · served by `uirix_guide({ "topic": "testing" })`.

Saving the owner's own questions once and asking them again after every change: how to write questions and their checks, how to run them (paid, a dry run for the outside world), how to judge the answers, and how to read what regressed against the run before.

```
GUIDE testing: saved test questions, runs and what changed

GOAL
The owner's own questions are saved once and asked again after every change, so "did this change break anything" is answered by the same questions each time, and a failure is found before a customer finds it.

FACTS THAT MISLEAD
- A test is a dry run for the outside world: the agent's actions (a lead, a ticket, an order, an e-mail) are accepted and NOT carried out, nobody is notified, and test conversations are in no figure of the briefing or the metrics. A custom capability's reads call the owner's API for real (a real lookup); its writes are stand-ins: nothing is sent. The calendar follows the channel of the test: on "phone" the agent has the booking tools the phone has (the owner's policy per channel), a free-time check reads the real calendar and, when the time is free, tells the agent to book it on the customer's yes; the booking is accepted and not written.
- A run costs money all the same: one model conversation per question, billed like chat, two units of the daily chat quota each.
- A run works in the background. run_test_set answers at once with a run id. get_test_run shows the progress and the result.
- Three verdicts. pass: every automatic check holds and nothing is left to judge. fail: a check broke or the agent did not answer. unchecked: the checks hold and the expectation is in words, so a reader must judge it. That reader is you.
- Automatic checks are literal: must_include looks for the phrase itself, in any letter case. "49" also passes on "149".
- An answer in another language than the question fails by itself.
- A review can fail what the checks passed. It cannot pass what a check failed: fix the checks of the question instead.
- A run is compared with the completed run before it. The newest twenty runs of an agent are kept.
- save_test_set with mode replace makes the set exactly the list you send. To add a question use mode append.

READ FIRST
- get_test_set(agent_id): the questions and how the recent runs went.
- get_agent_setup(agent_id) when writing questions: what the agent knows and what it can do on each channel.

CHECKS
- No saved questions: offer to write them.
- Saved questions that never ran, or an agent that changed since the last run: offer a run.
- Failures in the last run on the current version: start from those.

ASK
The owner's own questions first: "What do customers really ask you?" Then the channel when it matters: Website Chat (default), Voice Chat or phone.

APPLY: write the questions
1. Take the owner's questions. Add your own from the knowledge summary and the capabilities until there are five to ten: facts customers ask (price, hours, address), one per action that is switched on ("I want to leave my details"), one the knowledge does not cover (a good answer admits it and offers a next step), one in each language customers use.
2. For each question write what a good answer does (expect). Add automatic checks only where a fact is exact: a price, a phone number or an address in must_include, a promise the agent must never make in must_not_include, the action it must take in must_call.
3. Show the list. Let the owner add, remove and reword. Save with save_test_set after the yes.

APPLY: run and judge
1. Say how many questions will run and that each is billed. Wait for the yes.
2. run_test_set. Then get_test_run every 10 to 15 seconds until the status is completed.
3. Judge every unchecked answer against its expect and against the agent's knowledge, never against what you know yourself. Record the verdicts with judge_test_run, with a one line reason for every fail.
4. Report: passed, failed, and against the run before: what regressed (passed before, fails now) and what was fixed. A table is right here: question, short answer, verdict, why.
5. For every failure propose the fix by its type: a fact goes to the knowledge, a behaviour becomes one improvement rule, an action that was not taken is a setup matter. Fix after a yes, then run only the failed questions again (question_ids).

APPLY: after any change
After a change to the knowledge, the instructions or the capabilities, and after a rebuild: offer to run the saved questions. A regression is a reason to undo the change or to fix it now, before customers meet it.

APPLY: one question now, with test_chat
- test_chat runs a short text conversation and returns the replies: it opens a conversation (the greeting first unless send_greeting is false), sends the messages in order and closes it (end true, default; end false keeps it open for a follow-up with its conversation_id). channel picks the prompt that runs: "chat" (default, the website and API prompt), "voice" or "phone", exercised by text.
- It is a dry run for the outside world, like a saved run: a lead, a ticket, an order, an e-mail or a message is accepted and NOT carried out, nobody is notified, and website search still runs; so a test may safely make the agent "take a lead". live_actions true makes it a REAL conversation (the record is saved, the e-mail sent, webhooks fire, the metrics count it): only to check that one action works end to end, and only after the owner said yes.
- Every turn is billed like a website chat and counts against the daily chat quota: 1 to 5 messages per call, and ask before a longer session. Put the questions of one topic into ONE call (the messages array) and open a new conversation only for a new topic: every conversation sends the whole instructions and knowledge again, so one conversation per question is the most expensive way to test.
- A test conversation is marked as a test (is_test true in list_conversations and get_conversation, its summary status none): it is in no metric, briefing or quality score, fires no webhook and gets no summary. The answer carries conversation_id, the greeting, each question with the agent's reply, its latency and whether it went unanswered, and the token usage.

VERIFY
get_test_run after judging: unchecked is 0, and the counts match what you reported.

MONEY
Paid: run_test_set (every question is a billed conversation: say the number and get a yes). test_chat for one extra question is billed per turn. Free: get_test_set, save_test_set, get_test_run, judge_test_run.

MISTAKES TO PREVENT
- A run without a yes, or a second run "to be sure".
- must_include with a phrase the agent may word differently: it fails good answers. Use expect for that.
- Passing an answer because it sounds right. Check it against the knowledge.
- Replacing the set when the owner asked to add one question.
- Questions only you would ask. The set belongs to the owner.

STOP WHEN
The questions are saved, the last run has no failure the owner cares about, and every unchecked answer was judged.
```
