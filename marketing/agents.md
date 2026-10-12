# Marketing — running it with AI agents

How to set up agents that research customers, draft content and outreach,
run tests and report — without them inventing facts, sending things or
quietly degrading. Sits next to `claude-code-loop` in the workspace, which
solves the same problem for code.

**Tags:** **MUST** / **SHOULD** / **DON'T** / **Skip** as in the SEO files.
Most of this is practitioner consensus (read 2026-10-12), not vendor
documentation; it is kept because it matches what the loop templates in this
workspace already learned.

---

## The context folder comes before any agent

Generic output means thin context, not a weak model. Before the first agent,
write the business down the way you would for a sharp new hire. One folder,
a few files, plain Markdown:

- **Start-here** — what the company does, for whom, this quarter's
  priorities, where everything else lives. Every agent reads it first.
- **Customer fit** — who buys, who stays, who you can serve profitably.
  Painfully specific ("Shopify stores at $1–10M where the founder still
  does the books") beats "SMBs".
- **Offers** — what you sell, prices, what you may promise, what needs
  approval before anyone says it.
- **Voice** — not adjectives. Three pieces you loved with one line on why,
  two you rejected with the reason. Agents learn from examples.
- **Founder opinions** — strong takes on the category, customer and
  competition. The one input competitors cannot generate.
- **Failed campaigns / decisions** — one line per lesson that cost money.
- **Evidence/** — where agents write what they find (call summaries, customer
  language reports, guesses).

**Rule:** agents write to `evidence/`; only a human moves something into the
company files. Otherwise one agent's hunch becomes policy.

Every rejection becomes a line in a standards file the agent reads before
every draft. That file ends up being the editorial line, and it outlives
the tool.

## Data and measurement

- Connect where customer truth lives (calls, tickets, CRM, analytics,
  revenue). **Read-only everywhere to start**; write access is earned.
- **One campaign ID carried everywhere**: UTM tags, ad names, email
  sequence names, a field on each deal. One table (spreadsheet is fine) with
  a row per campaign: spend, leads, qualified, deals, revenue, churn. Most
  companies know clicks per campaign and revenue per customer and cannot join
  them; this is the join.
- Name creatives by what they test (`BK014_dinner-angle_ugc_v2`), so a month
  later the lesson is "the dinner angle beat the price angle", not
  "video_final_7 won".
- **Decide the evidence bar before launching**: how much spend, how many
  days, what counts as a win. Without it, 200 tests are 200 inconclusive
  results.
- Wire results through to retention and refunds; cheap customers who churn
  in 60 days look great on an acquisition dashboard.

## Build order

1. **One agent, made reliable, before a second.** Six agents on day one is a
   weekend debugging a group chat.
2. First: the **customer language** agent — reads call transcripts and
   tickets, extracts the exact phrases customers use for their problems.
   Everything else feeds off it. First run is ~70% right; fix the
   instruction, save the fix, repeat three or four times.
3. Then one at a time, each with its own folder, instructions and schedule:
   buying-trigger (watches for events that create demand, drafts one email
   only if it can finish "this event creates this problem, we solve it by
   ..." sharply), search (the questions people ask before buying, from
   Search Console, calls and what AI assistants answer — see
   [seo/ai-search.md](../seo/ai-search.md)), creative, closed-lost (rereads
   lost deals for the real reason and a reopen condition, then watches for
   it), performance (Monday memo, every line ending in keep / kill / change /
   test).
4. Keep **ten example inputs with expected output per agent** and re-run
   them after every instruction change, so regressions show up immediately.
5. If you spend all day fixing output, the problem is upstream: the context
   folder or the agent's contract.

## Guardrails live in the tools, not the prompt

"Always ask me before sending" is a suggestion to a model. Real limits:

- Smallest permissions that do the job. Outreach agent: draft-only email.
  Ads agent: creates paused, budgets stay human.
- Approval steps inside the code (a message with an approve button that the
  action waits on).
- Plain code for exact rules — spend caps, suppression lists, dedupe,
  "never delete a page over N words". The model handles judgement calls
  only.
- A written contract per agent: sources, limits, what "done" means. An agent
  that reports "this source failed today" beats one that silently skips it.
- A permission list written before the first task, for example:

  ```
  ALLOW            read analytics / Search Console / CRM; create drafts; write the log
  REQUIRE APPROVAL publish or edit a live page; change a title that gets clicks; redirects
  BLOCK            delete pages; edit robots.txt or canonicals; send external email; spend
  ```

- Agents never hit send, publish, or pay. A human on the button, always, and
  label AI-generated people and scenes where a platform requires it.

## The weekly loop

Monday: read the performance memo, make keep/kill/change calls. Midweek:
fix the workflows that produced weak work, launch new tests. Talk to sales
and support weekly — next week's ideas are there. Friday: review what agents
made, update the files.

The review queue is the heart. Every item should take under a minute: show
the change, what it touches, the evidence. If reviewing takes longer, the
agent's output format is wrong.

## Creative and social (brief)

- Organic posts are the free test lab: post ten hooks, put money only behind
  what the algorithm already picked up.
- Ask for genuinely different concepts (a worked example, a customer story,
  a raw demo, a founder take), not fifty headlines on one idea. Claimed
  mechanics of ad platforms (e.g. grouping look-alike ads) are from a
  practitioner and unverified; the practice is sound regardless.
- Use AI actors to test scripts, pay a real person to run the winner — it
  performs better and keeps platform labelling rules simple.
- UGC creators: pick by views ÷ followers on recent videos, not follower
  count; small creators whose videos travel 20–50× past their audience are
  the ones to brief. Vet by watching, then brief with what the data found.
  (Cost and ARR claims in the source are unverified.)
- One channel, one job: search answers questions, social starts
  conversations, email arrives at a moment. The same message on five
  channels pays five times for one impression.

## What a marketing engineer needs to know

Marketer half: customer interviews, positioning, an offer that is a reason
to buy, a headline, how each channel chooses who sees what, enough statistics
to tell a result from a fluke. Builder half: writing context an agent can use
(the most underrated skill), reading code well enough to own it, APIs and MCP,
basic SQL, shipping a page, git, test cases, knowing what a run costs.

## Sources

Greg Isenberg, "Marketing Engineers: 100x More Experiments with AI agents",
`https://x.com/gregisenberg/status/2108188646973313195` (read 2026-10-12).
Nicholas Dulait (ChatSEO), "How to use Claude Opus 5.5 for SEO", Part 5
(permission list, standards file),
`https://x.com/nicholasdulait/status/2108212094214529135` (read 2026-10-12).
Shawn (Composio/treg), "How to Copy CalAI's UGC Playbook",
`https://x.com/shawnbuilds/status/2108125367370486060` (read 2026-10-12;
creator-selection ratio only — the post sells treg and its figures are
unsourced).

All practitioner opinion; the tools named in the sources change monthly and
are deliberately left out.
