# AI — working with agents

The general rules for putting an AI agent on real work: what it reads, how a
task is written (including classifying at volume), when to use an agent
instead of plain automation, what it may do on its own, how you check it,
the ways it reliably fails, and how to let it run long on one goal. Domain files add only what is specific to them:
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
the business down the way you would for a sharp new hire. Build it by having
the model ask you the questions one at a time and mark anything unanswered
`UNKNOWN` — a context file with invented facts poisons every task after it.
Keep it short enough to stay a set of instructions (one practitioner caps
it at ~200 lines).

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
  top — under version control, so every change has a history. Work you repeat
  becomes a reusable, versioned skill rather than a prompt pasted again.
- High-volume, simple jobs run fine on a small model; judgement-heavy ones
  (audits, synthesis) get the strongest.

### Classifying at volume

When an agent scores or qualifies thousands of records (leads, pages,
tickets), most failures are in the prompt, not the pipeline.

- **Write the disqualifiers as carefully as the criteria.** Without a
  definition of what doesn't qualify, the model invents reasons things do.
- **Specific tests, not categories:** "headcount above 2,000 or a
  procurement department mentioned on the site", not "enterprise".
- **A written reason on every verdict.** Reading the reasons in bulk is how
  you find where the definition is wrong.
- **Forbid invention explicitly.** A model asked to find a signal finds one
  whether it exists or not. Tell it to return "none", and to return no data
  when a page can't be reached.
- **Test on ~50 records before running at volume:** about 10 you would
  definitely take, 10 you would definitely reject, 30 you're unsure of.
  Compare its verdicts with yours.
- **Fix by symptom:**

  | Symptom | Cause |
  |---|---|
  | Keeps records you'd drop | Disqualifiers too vague |
  | Drops records you'd keep | One criterion too narrow — read 20 rejection reasons to find it |
  | Reasons are generic | It isn't reading the source; require it to cite a specific page |
  | Scores bunch around one number | The bands aren't differentiated |

- **Cheap model first.** A small model removes the obvious misses at cents
  per thousand; the strong model scores what survives.

## Automation or agent?

Not every step needs a model. Split by whether the steps can be written down:

| | Automation (a workflow tool or a script) | Agent |
|---|---|---|
| Steps | Written down in advance | Picked at run time |
| When it fails | Stops with an error you can see | No error — the answers just get worse |
| Fits | Routing, syncing, lookups across providers, fixed pipelines | Reading, judging, drafting replies — with approval |

Default to automation for anything you can describe step by step: it is
cheaper by orders of magnitude (one agency estimates its workflow bill at a
small fraction of what the same work would cost through a model) and it
fails loudly. Keep the agent for judgement.

**Choosing tools an agent will use:** prefer tools that expose their work
through an API, can run a whole job from one instruction, and put their
results somewhere the agent can read.

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
- **Agents propose, people apply** for systems of record. An agent reads
  the CRM and posts the updates it wants; a person applies them. Same for
  launches and deletes: staged by the agent, approved by a person.
- **Watch the spend.** One API key per person, spend alerts that fire before
  the invoice, cheap models for cheap tasks, and a monthly look at what each
  person spent next to what they shipped. A single unwatched task can burn
  thousands in credits (one agency's experience) and nobody notices until the
  invoice, because the total is the only number anyone sees.
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

## Long-running goals

An agent can work on one measurable target for hours or days unattended if
the task gives it three things: **the goal, how to measure it, and how hard
to try**. It is the loop pattern — verify gate, persistent state, stop
condition — applied to one number.

- **Goal:** one measurable outcome ("the homepage's LCP under 2 s on a phone",
  "no page scrolls sideways at phone width", "build under a minute").
- **Measure:** the exact procedure, repeated after every change, with noise
  handled (e.g. median of three runs). It only counts as met when the
  measured number meets the goal.
- **Work on a branch.** Change one thing at a time; keep a change only if it
  beats the best result by a set margin (one practitioner uses 5%),
  otherwise revert it. Log every measurement to a file the agent reads first
  on resume, and keep a simple chart so progress is visible at a glance.
- **Hard limits, written into the goal:** never delete features or tests,
  or skip tests, to hit the number — left long enough, it will try. No
  deploys, no data deletion, no secrets. Doubts go into a questions file
  while it works on something else.
- **A stop condition:** a turn or time cap after which it stops and writes
  down where it is stuck.

## Rollout and review

- **One agent, made reliable, before a second.** Several on day one is a
  weekend debugging a group chat. First runs are often ~70% right; fix the
  instruction, save the fix, repeat.
- **Automate a process that exists.** If a task needs a step the team doesn't
  do yet, build the step first.
- **Ten example inputs per agent**, with the expected output, re-run after
  every instruction change so regressions show at once. For classifiers, use
  the larger test set above.
- **A new schedule runs two weeks untouched** before you trust it. Fix the
  instruction, not the outputs. Cut any part of the output you always skip.
- **If someone has to remember to run it, it will stop.** Recurring work goes
  on a schedule.
- **The review queue is the job.** Every item should take under a minute:
  the change, what it touches, the evidence. Longer means the output format
  is wrong. Give agent output its own channel, and a morning digest of what
  happened and what is waiting on a human decision.
- **Review the tools weekly, like teammates:** what did each connection do?
  Where did a person copy and paste anyway? What broke without anyone seeing
  an error?
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

Christian (@coldemailchris), "How To Master GTM Engineering (FULL COURSE)",
`https://x.com/coldemailchris/status/2101014272021008735` (read 2026-10-14) —
classifying at volume.

Voxyz (@Voxyz_ai), goal-loop template quoted in
`https://x.com/voxyz_ai/status/2110083153930920113` (read 2026-10-14) —
long-running goals. The post names a Claude Code `/goal` command; not
verified here, so the pattern is written tool-neutral.

Alex Vacca (Frontal), "The Exact Tech Stack For Running an AI-Native GTM
Agency", `https://x.com/itsalexvacca/status/2110415145587581023` (read
2026-10-15) — automation vs agent, tool test, agents propose / people apply,
spend control, agent channel and digest, weekly tool review, short context
file, versioned prompts and skills.

Nicholas Dulait (ChatSEO), "Ultimate Claude Opus 5.5 Starter Pack For SEO",
`https://x.com/nicholasdulait/status/2110275229108818335` (read 2026-10-15) —
building the context file by questions, `UNKNOWN` for gaps.

All practitioner opinion; re-read when this file is more than six months old.
