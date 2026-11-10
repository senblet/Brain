# AI — choosing a Claude model and effort

Which model to build with, when to raise effort instead of switching, how to
mix models across an agent and its subagents, and what breaks when you
migrate. Applies to Claude Code sessions and to products that call the
Claude API (`astro`, `fondoabierto`, `jarvis`). For agent practice in
general, see [agents.md](agents.md); for testing a feature before and after
a change, [evals.md](evals.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). From a
guide on claude.dev, linked from Anthropic's Claude developer account and
pointing to Anthropic's own docs — treated as vendor documentation. Its
benchmarks are the vendor's own; prices are as of the read date. **Models
and prices change every few months: recheck before relying on a number.**

---

## Start here

- **Default: Opus 5.5 at `medium` effort** (Claude Code's default). Move
  down for simpler work, up for the hardest; when unsure, stay here.
- **Effort is the finer control. Try it before switching models.** Higher
  effort helps when the model needs to think longer, call more tools or
  check its own work; it adds latency. It cannot add knowledge or skill the
  model lacks — for that, move up a model.

| Work | Model and effort |
|---|---|
| Classification, routing, tagging, high-volume extraction | Haiku 5.5, `medium` |
| Subagents that find files, read logs, summarise, run tests | Haiku 5.5 or Sonnet 5.5 |
| Chat and interactive sessions | Sonnet 5.5 `low`/`medium`; Haiku for simple high-volume chat |
| Well-scoped coding: bug fixes, iterations, spec-driven work | Sonnet 5.5 `medium`, then `high` |
| Everyday engineering, debugging, multi-PR features | Opus 5.5 `medium`, then `high` |
| Repeated agent tasks: investigation, review, drafting | Sonnet 5.5 `medium` |
| Documents, slides, spreadsheets | Sonnet 5.5 `high`; Opus for complex models or large source piles |
| Computer use, vision-heavy work | Opus 5.5 `medium` |
| Major refactors, migrations, architecture, leading many subagents; deep research | Fable 5.2 `medium`, then `high` |

A clear spec doesn't make a task easy: migrations and performance work can
still need Opus or Fable.

## When a model falls short

In this order:

1. **Give it a way to verify its own work** — a test, a build, a script
   that calls the endpoint.
2. **Raise effort one level.**
3. **Move to the next model up, at a lower effort** than you used on the
   smaller one.

Past `high`, one more effort level can cost as much as the next model: on
the vendor's coding benchmark, Opus 5.5 at `xhigh` scored ~1.4 points above
`high` at 2.5× the cost, while Fable 5.2 at `high` matched Opus at `max`
for about half the cost per task. Test the bigger model before pushing
effort past `high`.

## Cost

- **Run cheap, re-run failures dear.** When outcomes can be checked
  automatically, run everything at `low` and re-run only the failures at
  `high`: ~97% of tasks passed at ~$0.17 each, against 95.3% at $0.29 with
  everything at `high` (vendor benchmark). Same idea as "cheap model
  first" for classifiers ([agents.md](agents.md#classifying-at-volume)).
- **Price the hardest tasks, not the typical ones**: on one 20-problem
  benchmark, two problems were 43% of the spend.
- **Keep the expensive model's context lean.** Every turn resends the
  context, mostly billed as cache reads; the bigger the main model, the
  more a lean context matters. Keep the main context for decisions and let
  cheaper subagents do the verbose reading.
- **Switching models mid-session costs a cache rewrite** and can lose the
  earlier reasoning (a model reads only some other models' thinking).
  Compact first, or start a fresh session from a written plan.
- Prices per million tokens, input / output, as read: Haiku 5.5 $0.10 /
  $0.50 (prompts ≤ 100K), Sonnet 5.5 $2 / $10, Opus 5.5 $4 / $20, Fable 5.2
  $8 / $40. All have a 1M context window.

## Mixing models

- **Small models for reading, the main model for edits and judgement.** Put
  subagents that search, read logs or run tests on Haiku or Sonnet (set
  `model:` in the subagent definition, or a default for all subagents).
  **Decided:** the Workflow reference in Claude Code says to leave the
  model override off unless confident; this guide, with measurements,
  says to put verbose reading on small models. Both hold — mechanical
  reading with checkable output is the case to be confident about;
  judgement, synthesis and code edits stay on the main model.
- **The built-in Explore subagent runs on the session's model**; to keep
  exploration cheap, define your own `Explore` subagent with
  `model: haiku`.
- **Many cheap workers under one strong lead** pay off on broad, splittable
  work (an Opus lead with up to 25 Sonnet workers cost about a third less
  than Opus alone on a large code search, same score); skip it for one
  dependent chain or work that fits one context.
- Skip routing code edits to a smaller model by default (the `opusplan`
  alias does the opposite of the rule above) and the "advisor" pairing,
  whose gain was within run-to-run noise — measure first.

## Migrating an API product

Check before switching a product's model:

- Opus 5.5 and Fable 5.2 always think; turning thinking off is an error.
  Read response blocks by `type`.
- `tool_choice` of `any` or a named tool returns 400 on Sonnet 5.5, Opus 5.5
  and Fable 5.2: send `auto`, mark the tool `strict: true`, and say in the
  prompt when to use it.
- Fable 5.2 keeps its thinking: if earlier content changes, the request
  fails — keep conversation history append-only.
- Haiku 4.5 → 5.5: effort replaces `budget_tokens`; non-default sampling
  parameters error; messages must end with a user turn.
- Run the product's eval set on the new model before switching
  ([evals.md](evals.md#datasets-and-ci)).

## Measuring on your own work

1. Collect real tasks with outcome checks (tests pass, ticket closed, right
   row count).
2. Run each candidate model at two or three effort levels, each in its own
   session, and record the cost per task.
3. Plot score against spend; keep a multi-model setup only if it beats
   every single-model point.
4. Shadow the winner on real traffic before cutting over.

Quick version in Claude Code: run one backlog task on two models and
compare the usage.

## Sources

Addy Osmani, "Which Claude model should you build with? Fable, Opus, Sonnet,
or Haiku", claude.dev (2026-11-09),
`https://claude.dev/blog/which-claude-model-should-you-build-with`, via
`https://x.com/claudedevs/status/2119898687803621427` (read 2026-11-10;
key passages checked verbatim).

Re-read when this file is more than six months old.
