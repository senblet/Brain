# AI — working with agents

The general rules for putting an AI agent on real work: what it reads, how a
task is written, what it may do on its own, how you check it, and the ways
it reliably fails. Domain files add only what is specific to them:
[marketing/agents.md](../marketing/agents.md) (marketing agents),
[operations/agency.md](../operations/agency.md) (studio operations),
`seo/` (SEO publishing). For orchestrating many agents in one run, see
[agent-workflows.md](agent-workflows.md). The studio's `claude-code-loop`
template applies the same ideas to code.

**Tags:** as in the [README](../README.md#how-notes-are-written). All
practitioner consensus (read 2026-10-12), not vendor documentation; kept
because the sources agree with each other and with what the loop templates in
this workspace already learned.

---

## Context before agents

Generic output means thin context, not a weak model. The data an agent is fed
decides the result more than the prompt does. Before the first agent, write
the business down the way you would for a sharp new hire.

**The context file** — one file (or a small folder) every task reads first:

- **Start here:** what the business does, for whom, this quarter's
  priorities, where everything else lives.
- **Customer fit:** who buys, who stays, who you can serve profitably.
  Painfully specific ("Shopify stores at $1–10M where the founder still does
  the books") beats "SMBs".
- **Offers and pricing:** what you sell, what it costs, what may be promised,
  what needs approval before anyone says it.
- **Voice:** examples, not adjectives — three pieces you loved with one line
  on why, two you rejected with the reason. Plus banned words.
- **Opinions:** the founder's strong takes on the category, the customer and
  the competition. The one input competitors can't generate.
- **Target numbers:** the figures the work is judged against.
- **Lessons:** one line per decision or failure that cost money.
- **How to work:** the rules below, written into the file.

Domain files list the extra sections they need.

**Evidence vs policy.** Agents write findings, summaries and guesses into an
`evidence/` area. Only a human moves something into the context file.
Otherwise one agent's hunch quietly becomes policy.

**Every rejection becomes a line** in a standards file the agent reads before
every draft. Over time that file is the editorial line, and it outlives the
tool.

## Writing a task

One job per prompt, with an end the model can check:

```
ROLE:        one job, and what it must never do
INPUTS:      the exact records it reads
WORKFLOW:    numbered steps
OUTPUT:      fixed sections
TERMINATION: stop when every item is covered or marked "not in the data";
             never guess to fill a gap
```

- MUST give the agent a way to say it doesn't know: **"not in the data"**,
  "not tracked", "unknown". Without one it fills the gap with something
  plausible.
- SHOULD require it to cite the record (file, line, quote) behind every
  finding.
- The termination line turns "be accurate" into a condition the model can
  check.
- Keep every task in one editable place, with name, input and output at the
  top.
- High-volume, simple jobs run fine on a small model; judgement-heavy ones
  (audits, synthesis) get the strongest.

## Guardrails live in the tools, not the prompt

"Always ask me before sending" is a suggestion to a model. Real limits:

- **Read-only to start.** Write access is earned, one tool at a time.
- **Smallest permissions that do the job:** email draft-only, ads created
  paused, budgets human.
- **Approval inside the code:** the action waits on an approve button; a
  tool that can write or send is set to "needs approval".
- **Plain code for exact rules:** spend caps, suppression lists, dedupe,
  "never delete a page over N words". The model handles judgement only.
- **A permission list, written before the first task:**

  ```
  ALLOW            read data sources; create drafts; write to the log / evidence
  REQUIRE APPROVAL publish or edit anything live; anything a client or the public sees
  BLOCK            delete; change config (robots.txt, canonicals, DNS); send externally; spend
  ```

- **A contract per agent:** sources, limits, what "done" means. An agent that
  reports "this source failed today" beats one that silently skips it.
- **Agents never hit send, publish, price or pay.** A person reads every
  output before it reaches a client — even a small error rate is too much
  from the client's side.
- **Client data:** on a personal plan, MUST turn off training on your chats
  before any client file goes in, and check the plan's data terms first.

## Known failure modes

- **Fills blanks.** Asked for a field it can't know — a search volume, a
  contact email, a category, a price — it writes a plausible one. Give it the
  real list or export, and the "not in the data" escape.
- **Invents numbers in drafts.** Proposals and reports pick up metrics no one
  measured. A separate QA pass checks every number against its source before
  anything leaves.
- **Drops what mattered.** Told to duplicate or rewrite, it can silently lose
  the one unique element (a quiz, a data table) and report success. After a
  duplication or rewrite, diff for what is *missing*, not only what changed.
- **Makes irreversible calls.** It will suggest deleting substantial pages.
  Deletes, redirects and config changes go through a human or are blocked in
  code.
- **Verifies its own work too kindly.** Checking belongs in a separate
  context that sees only the output (see
  [agent-workflows.md](agent-workflows.md#verification-is-the-point)).

## Rollout and review

- **One agent, made reliable, before a second.** Several on day one is a
  weekend debugging a group chat. First runs are often ~70% right; fix the
  instruction, save the fix, repeat.
- **Automate a process that exists.** If a task needs a step the team doesn't
  do yet, build the step first.
- **Ten example inputs per agent**, with the expected output, re-run after
  every instruction change so regressions show at once.
- **A new schedule runs two weeks untouched** before you trust it. Fix the
  instruction, not the outputs. Cut any part of the output you always skip.
- **If someone has to remember to run it, it will stop.** Recurring work goes
  on a schedule.
- **The review queue is the job.** Every item should take under a minute:
  the change, what it touches, the evidence. Longer means the output format
  is wrong.
- **Fixing output all day means the problem is upstream** — the context file
  or the agent's contract.

## Sources

Greg Isenberg, "Marketing Engineers: 100x More Experiments with AI agents",
`https://x.com/gregisenberg/status/2108188646973313195` (read 2026-10-12) —
context folder, evidence rule, guardrails, test inputs, review queue.

Kyle Hunt, "How to use Claude for agency operations so well it feels illegal
(full guide)", `https://x.com/huntkyle/status/2108604316432945232` (read
2026-10-12) — context file sections, task shape, "not in the data", QA pass,
client data, rollout.

Nicholas Dulait (ChatSEO), "How to use Claude Opus 5.5 for SEO",
`https://x.com/nicholasdulait/status/2108212094214529135` (read 2026-10-12) —
permission list, standards file, dropped elements, irreversible calls.

All practitioner opinion; re-read when this file is more than six months old.
