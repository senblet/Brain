# Operations — running a studio with AI

How a small agency or studio uses AI to run delivery and finances the same
way every week: single-job tasks that read records you already keep, and a
person who checks every output. The setup — context file, task shape,
guardrails, rollout — is in [ai/agents.md](../ai/agents.md); this file adds
what is specific to studio operations.

**Tags:** as in the [README](../README.md#how-notes-are-written). One
practitioner source (an agency-operations consultant, read 2026-10-12); his
client figures are anecdotes and are left out.

---

## Principles

- **Operations is the same job done the same way every time.** Ad-hoc use
  ("a doc called *AI stuff*") isn't operations.
- **The records already exist:** call transcripts, revision comments, briefs,
  logged hours, contracts, the P&L. Feed those, not descriptions of them.
- **Group problems by cause, not by person.** Blame lands on whoever touched
  the work last; the records usually point upstream (brief, onboarding).
- **Arithmetic, not impressions.** Margin "felt" on a retainer and margin
  computed from logged hours routinely disagree by a lot.

## Context file additions

On top of the general context file ([ai/agents.md](../ai/agents.md#context-before-agents)):

- team roles and who leads what;
- the delivery process, from signed contract to first report;
- pricing structure (retainers, ranges, add-ons);
- target numbers: revision rate, margin, hourly-rate floor, utilisation,
  churn;
- the audit lens below, one line per area: working or broken.

**The audit lens:** strategy, client management, delivery, team and people,
quality and performance, recruiting and hiring, operations, financials.

## The jobs

Each is one task in the shape from [ai/agents.md](../ai/agents.md#writing-a-task).

| Job | Reads | Produces | Stops when |
|---|---|---|---|
| Revision causes | Last few hundred revision comments, with client, deliverable, editor | Reasons with count, %, two examples; each tagged brief / onboarding / client feedback / skill | Every comment sits under a reason or "unclear" |
| Brief check | One brief + top revision causes | Missing fields, the questions the maker would have to ask, a fixed brief with `[ASK CLIENT]` where only the client knows | Someone could finish the work from the brief alone — test: "what do you need to complete this without messaging anyone?" |
| Call summary | One client-call transcript | 5-line summary, decisions, action items (task, owner, due date, the line it came from), risks | Every action item has an owner and date or says "no owner"; no invented dates |
| QA before sending | A draft + its source data + forbidden patterns | Flagged lines (line, problem, source or "not in the data"), then a clean version | Every number matched to a source or flagged |
| First-pass audit | Discovery transcripts + numbers on file | Biggest constraint, then each audit-lens area scored 1–5 with quotes | Every area scored or "not in the data". Human confirms every call |
| Content ideas | Call transcripts | Up to 5 ideas per call, each with the quote it came from | Nothing that wasn't said on the call |
| Sales call review | Sales call transcripts | 3 things to improve, tied to the moment, with what to say next time | Exactly 3; nothing about the prospect beyond the transcript |
| Hourly rate & utilisation | 30 days of revenue by client, hours by person and client, available hours, targets | Effective rate per client (revenue ÷ hours), utilisation per person, flags below target, the maths on every row | Every client and person has a row or "not tracked"; never estimate hours |
| Scope check | Contracted hours per client, hours logged, overage clause | Logged as % of contract; anyone 20%+ over flagged with the clause and what it would have billed | Every client checked or "not tracked" |
| Weekly ops review | Last week's tasks, hours, revisions, last contact date per client, targets | One page: shipped, at risk, clients not contacted in N days, numbers vs targets | One page; missing numbers stay "not tracked" |

Call summaries are high-volume and simple; the audit is the heaviest job.

## Rollout

- Start with revision causes; add the rest a few at a time, a week each
  before tuning. Put the weekly ops review on a schedule last.
- Every error the QA pass catches becomes a line in the context file.
- Time saved only sticks when the people saving it see the benefit.

## Sources

Kyle Hunt, "How to use Claude for agency operations so well it feels
illegal (full guide)", `https://x.com/huntkyle/status/2108604316432945232`
(read 2026-10-12). Sells an agency-operations programme; the prompts and
rules are kept, the revenue and client figures are not.
