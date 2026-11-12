# AI — choosing a Claude model and effort

Which model to build with, when to raise effort instead of switching, how to
mix models across an agent and its subagents, how to keep a Claude Code
session's prompt cache warm, and what breaks when you migrate. Applies to Claude Code sessions and to products that call the
Claude API (`astro`, `fondoabierto`, `jarvis`). For agent practice in
general, see [agents.md](agents.md); for testing a feature before and after
a change, [evals.md](evals.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). From a
guide on claude.dev, linked from Anthropic's Claude developer account and
pointing to Anthropic's own docs — treated as vendor documentation. Its
benchmarks are the vendor's own; prices are as of the read date. The
prompt cache section is from Claude Code's own docs. **Models
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
  Compact first, or start a fresh session from a written plan. Other
  cache breakers: [Keeping the prompt cache warm](#keeping-the-prompt-cache-warm).
- Prices per million tokens, input / output, as read: Haiku 5.5 $0.10 /
  $0.50 (prompts ≤ 100K), Sonnet 5.5 $2 / $10, Opus 5.5 $4 / $20, Fable 5.2
  $8 / $40. All have a 1M context window.

## Keeping the prompt cache warm

Every message in Claude Code re-sends the whole conversation. The repeated
part is billed at the cheap cached rate only while the prefix matches
exactly and the cache hasn't expired; break it and the next request pays
full input price for everything. On a long chat that one turn is where a
plan limit goes (one practitioner's estimate on a 100k-token Opus chat:
$0.02 cached against $0.80 rebuilt). A rebuild on a short chat is cheap.

- **SHOULD pick model, effort and fast mode at launch and keep them**
  (`claude --model opus`). Each model has its own cache, and so does each
  speed: turning fast mode on later re-reads the whole chat at fast-mode
  rates. Changing effort keeps the cache on the 5.5 models and Fable 5.1+
  with an API key or subscription; on Bedrock, Google Cloud or a gateway it
  is a full rebuild too. Need another model for one task? Use a subagent or
  a new session. If you must switch, do it after a break, when the cache
  has already expired.
- **Hidden model switches:** a skill or command whose frontmatter sets
  `model:` switches the main session for that turn, and the turn after it
  rebuilds again. **SHOULD** give a skill a `model:` only together with
  `context: fork`, which runs it in a subagent and leaves the main cache
  alone. The `opusplan` alias switches model on every plan-mode toggle;
  automatic model fallback is a switch too.
- **Compact at a natural break, while the cache is warm.** A warm `/compact`
  reads the history from cache; after a break past the cache lifetime it
  re-reads all of it at full price. Say what to keep: `/compact keep
  decisions, file paths, failing tests and open TODOs`. A wrong path is
  better undone with `/rewind`, which returns to a prefix already cached.
  `/clear` for a new task.
- **Cache lifetime:** on a subscription within plan usage the main
  conversation gets one hour; subagents, compaction and everything else
  get five minutes, as does everything on an API key, a cloud provider or
  usage credits. Each hit resets the timer. Set it with `promptCacheTtl`
  and `subagentPromptCacheTtl` (`"5m"` or `"1h"`). Skip `1h` unless the work
  has real gaps: a one-hour cache write costs 2× base input, a five-minute
  one 1.25×. On the hour TTL, Claude Code may compact an idle long chat
  just before the cache expires; `"idleCompaction": false` turns that off.
- **Images:** past the per-request image limit, Claude Code drops the oldest
  batch and rebuilds from the earliest changed message. Crop screenshots to
  what matters; give a screenshot-heavy task its own session.
- **Scope:** the cache belongs to one machine and one directory; parallel
  sessions in the same directory share it. An upgrade usually changes the
  system prompt, so the first session after it starts cold. Updates apply
  only at launch; `DISABLE_AUTOUPDATER=1` in `env` lets you pick when.
- **Tools:** with tool search on (the default on supported models), MCP
  tools are deferred and connecting a server mid-session is safe. With it
  off, a new MCP server or a deny rule on a whole tool (`"Bash"`) rebuilds
  everything. **SHOULD** scope deny rules (`"Bash(rm -rf *)"`,
  `"Bash(git push *)"`, `"Read(./.env)"`): they protect the same commands
  and leave the tool list alone.
- **Behind a gateway or custom `ANTHROPIC_BASE_URL`,** caching depends on the
  gateway forwarding Claude Code's `cache_control` markers. The bad case is
  silent: success responses, whole history billed uncached every turn.
  **SHOULD** test once: run `claude -p "hello" --output-format json | jq
  '.usage | {cache_read_input_tokens, cache_creation_input_tokens}'` twice;
  the second run must show reads.
- **Safe mid-session:** editing repo files, editing `CLAUDE.md` (keeps the
  cache, but applies only after `/clear`, `/compact` or a restart),
  permission mode, output style, invoking skills without `model:`,
  `/recap`, `/rewind`, spawning a subagent.
- **Watch it:** `/usage` shows a `Prompt cache (main)` line — hit ratio,
  misses, warm or cold, and the likely cause of the last miss. A status line
  script can read the same `prompt_cache` object:

  ```bash
  #!/bin/bash
  # ~/.claude/statusline.sh — set "statusLine": {"type": "command",
  # "command": "~/.claude/statusline.sh"} in settings.json
  input=$(cat)
  if [ "$(echo "$input" | jq '.prompt_cache != null')" = "true" ]; then
    WARM=$(echo "$input" | jq -r '.prompt_cache.warm')
    PCT=$(echo "$input" | jq -r '(.prompt_cache.hit_ratio // 0) * 100 | floor')
    COLD_K=$(echo "$input" | jq -r '(.prompt_cache.recache_tokens_if_cold // 0) / 1000 | floor')
    if [ "$WARM" = "true" ]; then echo "cache warm · ${PCT}% hits"
    else echo "cache cold · next message re-reads ~${COLD_K}k tokens"; fi
  else
    echo "cache: waiting for first response"
  fi
  ```

  To audit a setup, ask Claude Code to read the settings files, `.mcp.json`
  and every `SKILL.md` and command file, and flag: skills or commands with
  `model:` and no `context: fork`; whole-tool deny rules; a custom base URL
  or gateway; anything that turns off tool search; the two TTL values.
  Report a table, change nothing.
- A warm cache doesn't make a bloated `CLAUDE.md` or an endless session free:
  cached tokens still count. Keep context lean (above).

## Mixing models

- **Route by delegation; don't switch the main session's model mid-task.**
  The session keeps its model; cheaper work goes to subagents, each with its
  own `model:`. Switching the main model throws away the prompt cache and,
  moving down a tier, the earlier reasoning.
- **Small models for reading, the main model for edits and judgement.** Put
  subagents that search, read logs or run tests on Haiku or Sonnet (set
  `model:` in the subagent definition, or a default for all subagents).
  **Decided:** the Workflow reference in Claude Code says to leave the
  model override off unless confident; this guide, with measurements,
  says to put verbose reading on small models. Both hold — mechanical
  reading with checkable output is the case to be confident about;
  judgement, synthesis and code edits stay on the main model.
- **Don't delegate** one dependent chain of steps, work that fits easily in
  the current context, or a handful of tool calls — coordination costs more
  than it saves. Delegate verbose reading (logs, wide file sweeps) and
  genuinely parallel work, and ask for a short summary back.
- **Small models only where a mistake is cheap to spot.** If a wrong answer
  would pass unnoticed (a judgement call, a subtle edit), keep it on the
  main model. **Decided:** a popular routing skill sends "well-scoped edits
  against a clear spec" to Sonnet subagents; the guide keeps code edits on
  the main model when delegating and warns the `opusplan` alias does the
  reverse. Rejected — Sonnet is fine as a *session* model for well-scoped
  coding (table above), not as a delegate for edits.
- **The built-in Explore subagent runs on the session's model**; to keep
  exploration cheap, define your own. Drop this into a project's
  `.claude/agents/Explore.md`, or `~/.claude/agents/` for every project:

  ```markdown
  ---
  name: Explore
  description: Finds files, code, and usages across the repo and reports
    where things are. Use for any search or "where/how is X done" question
    before reading or editing code.
  tools: Read, Grep, Glob, Bash
  model: haiku
  ---
  Search, don't edit. Return a short report: the files and line numbers
  that answer the question, one line each on what is there, and anything
  you could not find. No code changes, no long quotes.
  ```

  The same pattern fits a test or log reader: read-only tools, `model:
  haiku`, report only what failed and where.
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
key passages checked verbatim). Delegation rules and the edit decision:
`Rajvardhman05/claude-model-router` (MIT),
`https://github.com/Rajvardhman05/claude-model-router` (read 2026-11-10), a
skill that condenses the same guide. Prompt cache: "How Claude Code uses
prompt caching", `https://code.claude.com/docs/en/prompt-caching`, with the
`prompt_cache` status line fields from
`https://code.claude.com/docs/en/statusline` (read 2026-11-12), via
@choopyplug1, "Claude Code Token Usage: How to Stop Burning Your Limit 40x
Faster", `https://x.com/choopyplug1/status/2119833611499127166` (read
2026-11-12; status line script, audit prompt and cost example from the
post, every rule checked against the docs).

Re-read when this file is more than six months old.
