# Marketing — running it with AI agents

What is specific to marketing agents: the data they need, how to measure
campaigns, which agents to build in what order, and the weekly loop. The
general setup — context file, task shape, guardrails, rollout — is in
[ai/agents.md](../ai/agents.md). What to make and how to test creative is in
[content.md](content.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Practitioner
consensus (read 2026-10-12), not vendor documentation.

---

## Context file additions

On top of the general context file ([ai/agents.md](../ai/agents.md#context-before-agents)):

- the brand's positioning answers ([content.md](content.md#positioning-comes-first));
- failed campaigns, one line each with why ("the free audit attracted
  companies too small to afford us");
- the latest customer-language report, so every agent writes in the
  customers' words.

## Data and measurement

- Connect where customer truth lives: calls, tickets, CRM, analytics,
  revenue. Read-only first.
- **One campaign ID carried everywhere**: UTM tags, ad names, email
  sequence names, a field on each deal. One table (a spreadsheet is fine) with
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

## Which agents, in what order

One at a time, each made reliable before the next
([ai/agents.md](../ai/agents.md#rollout-and-review)), each with its own folder,
instructions and schedule:

1. **Customer language** — reads call transcripts and tickets, extracts the
   exact phrases customers use for their problems. Everything else feeds off
   it.
2. **Buying trigger** — watches for events that create demand (new location,
   funding, a new integration). Drafts one email only if it can finish "this
   event creates this problem, and we solve it by …" sharply; otherwise the
   account waits.
3. **Search** — the questions people ask before buying, from Search Console,
   sales calls and what AI assistants answer
   ([seo/ai-search.md](../seo/ai-search.md)); builds the most useful page for
   each.
4. **Creative** — makes genuinely different concepts from the
   customer-language report and approved claims; uploads ads paused.
5. **Closed-lost** — rereads lost deals for the real reason and a reopen
   condition ("needed SSO", "renews in March"), then watches for it.
6. **Performance** — a Monday memo from the campaign table; every line ends
   in keep, kill, change or test.

## The weekly loop

Monday: read the performance memo, make keep/kill/change calls. Midweek: fix
the workflows that produced weak work, launch new tests. Talk to sales and
support weekly — next week's ideas are there. Friday: review what agents
made, update the files.

## What a marketing engineer needs to know

Marketer half: customer interviews, positioning, an offer that is a reason
to buy, a headline, how each channel chooses who sees what, enough statistics
to tell a result from a fluke. Builder half: writing context an agent can use
(the most underrated skill), reading code well enough to own it, APIs and MCP,
basic SQL, shipping a page, git, test cases, knowing what a run costs.

## Sources

Greg Isenberg, "Marketing Engineers: 100x More Experiments with AI agents",
`https://x.com/gregisenberg/status/2108188646973313195` (read 2026-10-12).

All practitioner opinion; the tools named in the source change monthly and
are deliberately left out.
