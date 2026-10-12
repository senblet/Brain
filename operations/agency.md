# Operations — running a studio with AI

How a small agency or studio uses AI to run delivery and finances the same
way every week: one context file, single-job prompts that read records you
already keep, a person who checks every output. For the agent setup and
guardrails in general, see [marketing/agents.md](../marketing/agents.md).

**Tags:** **MUST** / **SHOULD** / **DON'T** / **Skip** as elsewhere. One
practitioner source (an agency-operations consultant, read 2026-10-12);
his client figures are anecdotes and are left out.

---

## Principles

- **The data decides, not the prompt.** Output quality follows what the model
  is fed: transcripts, revision comments, briefs, logged hours, contracts.
  Ad-hoc use ("a doc called *AI stuff*") isn't operations; operations is the
  same job done the same way every time.
- **You can't automate a process that doesn't exist yet.** If a prompt needs
  a step the team doesn't do, stop and build the step.
- **A person reads every output before it reaches a client.** Even a small
  error rate is unacceptable from the client's side.
- **Group problems by cause, not by person.** Blame lands on whoever touched
  the work last; the records usually point upstream (brief, onboarding).
- **Arithmetic, not impressions.** Margin "felt" on a retainer and margin
  computed from logged hours routinely disagree by a lot.
- **If someone has to remember to run it, it will stop.** Recurring reviews
  go on a schedule.

## Setup

- One workspace per business (a Claude Project or a repo) with a
  **context file** read before every task:
  services, team roles, ideal client, delivery process (contract → first
  report), voice and banned words, pricing structure, target numbers
  (revision rate, margin, hourly floor, utilisation, churn), and how the
  model must work:
  - cite the file and line behind every finding;
  - if it isn't in the files, write **"not in the data"** — never invent a
    number;
  - draft only: never send, price or decide;
  - when unsure, prepare it and flag it.
- Connect the tools the team works in; anything that can write or send set
  to **needs approval**.
- **Client data:** on a personal plan, MUST turn off model-improvement
  (training on your chats) before any client file goes in. Check what the
  plan's data terms say before uploading client records at all.
- Keep every prompt in one editable place with name, input and output at
  the top. Every error the QA pass catches becomes a line in the context
  file.

## Prompt shape

Each prompt does one job and has a checkable end:

```
ROLE:        one job, and what it must never do
INPUTS:      the exact records it reads
WORKFLOW:    numbered steps
OUTPUT:      fixed sections
TERMINATION: stop when every item is covered or marked "not in the data";
             never guess to fill a gap
```

The termination line is what keeps the output honest: it turns "be
accurate" into a condition the model can check.

## The jobs

| Job | Reads | Produces | Stops when |
|---|---|---|---|
| Revision causes | Last few hundred revision comments, with client, deliverable, editor | Reasons with count, %, two examples; each tagged brief / onboarding / client feedback / skill | Every comment sits under a reason or "unclear" |
| Brief check | One brief + top revision causes | Missing fields, the questions the maker would have to ask, a fixed brief with `[ASK CLIENT]` where only the client knows | Someone could finish the work from the brief alone — test: "what do you need to complete this without messaging anyone?" |
| Call summary | One client-call transcript | 5-line summary, decisions, action items (task, owner, due date, the line it came from), risks | Every action item has an owner and date or says "no owner"; no invented dates |
| QA before sending | A draft + its source data + forbidden patterns | Flagged lines (line, problem, source or "not in the data"), then a clean version | Every number matched to a source or flagged. Catches invented metrics before they reach a proposal |
| First-pass audit | Discovery transcripts + numbers on file | Biggest constraint, then each area scored 1–5 with quotes | Every area scored or "not in the data". Human confirms every call |
| Content ideas | Call transcripts | Up to 5 ideas per call, each with the quote it came from | Nothing that wasn't said on the call |
| Sales call review | Sales call transcripts | 3 things to improve, tied to the moment, with what to say next time | Exactly 3; nothing about the prospect beyond the transcript |
| Hourly rate & utilisation | 30 days of revenue by client, hours by person and client, available hours, targets | Effective rate per client (revenue ÷ hours), utilisation per person, flags below target, the maths on every row | Every client and person has a row or "not tracked"; never estimate hours |
| Scope check | Contracted hours per client, hours logged, overage clause | Logged as % of contract; anyone 20%+ over flagged with the clause and what it would have billed | Every client checked or "not tracked" |
| Weekly ops review | Last week's tasks, hours, revisions, last contact date per client, targets | One page: shipped, at risk, clients not contacted in N days, numbers vs targets | One page; missing numbers stay "not tracked" |

High-volume, simple jobs (call summaries) run fine on a small model; the
audit is the heaviest and deserves the strongest.

**The audit lens** the source uses — one line each, working or broken:
strategy, client management, delivery, team and people, quality and
performance, recruiting and hiring, operations, financials.

## Rollout

- One prompt first (revision causes is a good start); add the rest a few at
  a time, a week each before tuning.
- Cut any part of an output you always skip.
- A new scheduled job runs **two weeks untouched** before you trust the
  schedule; fix the prompt, not the outputs.
- Time saved only sticks when the people saving it see the benefit.

## Sources

Kyle Hunt, "How to use Claude for agency operations so well it feels
illegal (full guide)", `https://x.com/huntkyle/status/2108604316432945232`
(read 2026-10-12). Sells an agency-operations programme; the prompts and
rules are kept, the revenue and client figures are not.
