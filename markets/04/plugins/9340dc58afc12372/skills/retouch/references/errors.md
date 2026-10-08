# Failure handling

**Never apply one blanket response to every failure.** Identify which kind it is first.

| Kind | Looks like | What to do |
|---|---|---|
| **Pending** | Job queued or generating | **Wait.** Never resubmit — you will be billed twice for one result. |
| **Technical** | Timeout, 5xx, transport error | Retry **at most twice**, same parameters. Then stop and report. |
| **Unsupported capability** | The tool doesn't accept this input or can't produce this output | Use a supported route, or say plainly it isn't available. Never fake it. |
| **Safety refusal** | Content declined on policy grounds | **Do not route around it.** Tell the user what was declined, in one line, and offer a different subject. |
| **Model restriction** | A specific model won't accept this input class, but others will | Switch, and **say which model you switched to and why**. |
| **Billing / auth** | Subscription, credit or token error | Relay the message verbatim — it carries the fix. Never retry. |

## Safety refusals versus model restrictions

These look similar and are handled differently.

- A **safety refusal** is a judgement about the content. Retrying elsewhere to get around it
  is not acceptable. Report it and offer a different subject.
- A **model restriction** is one model's input policy — for example `seedance-2.5` declines
  human subjects, including illustrated ones, while other models accept them. Switching is
  legitimate, but it is a **material change**: say which model you used instead.

When you cannot tell which one you're facing, treat it as a safety refusal and ask.

## Always disclose material changes

The user must be told, in one short line, when you changed:

- the **model** (different look, different ceiling)
- the **duration** (a model's allow-list forced it)
- the **resolution** (the model couldn't reach what was asked)
- the **number of outputs** (a partial batch)

Silent substitution is how a user ends up confused about why two runs look different.

## Retry budget

**Two attempts per stage, maximum.** After that, stop and report what happened with what
you actually observed. Endless retrying burns credits and hides the real problem.

Track what already succeeded. When a multi-stage pipeline fails at stage two, **do not
re-run stage one** — reuse its output.
