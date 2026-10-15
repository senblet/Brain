# Operations — running a studio with AI

How a small agency or studio uses AI to run delivery and finances the same
way every week: one folder per client, single-job tasks that read records
you already keep, a person who checks every output, and hiring by paid
trial. Specs, scope and decisions are in
[product-process.md](product-process.md). The setup — context file, task
shape, guardrails, rollout — is in [ai/agents.md](../ai/agents.md); this
file adds what is specific to studio operations.

**Tags:** as in the [README](../README.md#how-notes-are-written).
Practitioner sources (an agency-operations consultant, a GTM agency,
`lenny-skills`), read 2026-10-12 to 2026-10-15; their client figures are
anecdotes and are left out.

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

On top of the general context file
([ai/agents.md](../ai/agents.md#context-before-agents)):

- team roles and who leads what;
- the delivery process, from signed contract to first report;
- pricing structure (retainers, ranges, add-ons);
- target numbers: revision rate, margin, hourly-rate floor, utilisation,
  churn;
- the audit lens below, one line per area: working or broken.

**The audit lens:** strategy, client management, delivery, team and people,
quality and performance, recruiting and hiring, operations, financials.

## Client work: one folder per client

How a small team runs the same system for many clients *(practitioner — a
GTM agency's layout; the principle fits any client work)*:

```
clients/
  _template/              copied for every new client
  acme/
    CLAUDE.md             standards, tone, rules, guardrails, permissions
    context.md            ICP, positioning, offer
    do-not-contact.csv    customers, competitors, churned accounts
    logs/                 what the agent changed, and why
    results/
      worked/             angles, pages, campaigns that worked
      went-nowhere/       and the ones that didn't
```

- **Every new client starts from `_template`**, so the first piece of work
  starts from everything already learned. Lessons from one client go back
  into the template.
- The agent opens inside the client's folder, so it reads that client's
  rules first and nobody re-explains the client.
- **Permissions per tool are written in the client's file** — e.g. CRM: read
  everything, write drafts only; sending tools: stage, launch needs
  approval; chat: post to the agent channel, never message a client
  directly ([ai/agents.md](../ai/agents.md#guardrails-live-in-the-tools-not-the-prompt)).
- **The working system stays with the client:** build inside their own CRM
  and tools, not yours.
- **Report weekly** on a live dashboard (health of the setup, engagement,
  results, best segments), and hold a review at about day 90 before
  deciding to scale.
- Write the rules down where a person and an agent can both read them;
  rules in one person's head leave with them.

## The jobs

Each is one task in the shape from [ai/agents.md](../ai/agents.md#writing-a-task).

| Job | Reads | Produces | Stops when |
|---|---|---|---|
| Revision causes | Last few hundred revision comments, with client, deliverable, editor | Reasons with count, %, two examples; each tagged brief / onboarding / client feedback / skill | Every comment sits under a reason or "unclear" |
| Brief check | One brief + top revision causes | Missing fields, the questions the maker would have to ask, a fixed brief with `[ASK CLIENT]` where only the client knows | Someone could finish the work from the brief alone — test: "what do you need to complete this without messaging anyone?" |
| Call summary | One client-call transcript | 5-line summary, decisions, action items (task, owner, due date, the line it came from), risks | Every action item has an owner and date or says "no owner"; no invented dates |
| QA before sending | A draft + its source data + forbidden patterns | Flagged lines (line, problem, source or "not in the data"), then a clean version | Every number matched to a source or flagged |
| First-pass audit | Discovery transcripts + numbers on file | Biggest constraint, then each audit-lens area marked working / broken / not in the data, with quotes | Every area marked. Human confirms every call |
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

## Hiring

- **Hire through a paid work trial** on representative, not shippable,
  work. Scope it too big to finish, so how they prioritise shows, and have
  them present the result. (Linear and 37signals pay for multi-day trials,
  per the source.)

## Sources

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15) — `interviewing-evaluating-candidates` (paid work trials; Karri
Saarinen).

Alex Vacca (Frontal), "The Exact Tech Stack For Running an AI-Native GTM
Agency", `https://x.com/itsalexvacca/status/2110415145587581023` (read
2026-10-15) — one folder per client, template, permissions per tool,
reporting and day-90 review.

Kyle Hunt, "How to use Claude for agency operations so well it feels
illegal (full guide)", `https://x.com/huntkyle/status/2108604316432945232`
(read 2026-10-12). Sells an agency-operations programme; the prompts and
rules are kept, the revenue and client figures are not.

Re-read when this file is more than a year old.
