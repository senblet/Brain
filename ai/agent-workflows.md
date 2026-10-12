# AI — multi-agent workflows

How to shape work that spans many agents: what runs in parallel, what waits,
what verifies, what merges. Written against Claude Code's Workflow tool
(orchestration scripts that spawn subagents), but the design rules hold for
any orchestrator. For working with a single agent — context, task shape,
guardrails — see [agents.md](agents.md).

**Tags:** as in the [README](../README.md#how-notes-are-written).

---

## Think in a graph, not a list

- A **node** is one bounded job: one input in, one output out. An **edge**
  exists only when a node reads another node's output.
- "And then" is not an edge. For every step in a linear agent, ask: does it
  read the previous step's output? If not, it doesn't need to wait. Most
  chains have two or three arrows that are only the order things were typed.
- A linear chain is a degenerate graph: slow, and one stall blocks
  everything after it. Cut the non-data arrows and it collapses into
  independent nodes feeding one node that needs them all.
- Orchestration in code costs no model tokens. Moving, flattening, deduping
  and filtering results is an edge — do it in plain code, never with an
  agent.

## Contracts

- Every node MUST get its input passed explicitly, never assumed from a
  shared context.
- Every node SHOULD return a defined shape. In Claude Code, giving `agent()`
  a JSON schema forces the subagent to return validated data; validation
  happens at the tool-call layer and the model retries on mismatch. A node
  whose output only a human can read cannot be wired into a graph.
- Name an edge by the data that crosses it. As long as the shape holds,
  either end can be swapped.

## Topologies

- **Fan out** independent work (N files, N sources, N routes) instead of
  chaining it. Each subagent carries its own context; only its result comes
  back, so the run can hold far more than one context could.
- **Fan in** where a stage truly needs every result at once.
- **Diamond** — split → work in parallel → merge — is the workhorse:
  fan out for breadth, **reduce in code**, synthesize with one final agent.
  It fits audits, reviews, research and market scans with only the prompts
  changed.
- **Route** with a plain `if`/`switch` on a node's validated output
  (classify, then branch; small diff → quick review, large diff → full
  audit). The judgment is the model's; the routing is code, so it runs the
  same way every time.

## Barriers cost wall-clock time

- **SHOULD default to a pipeline**: each item flows through all stages
  independently, so a fast item finishes while a slow one is still in stage
  one.
- A barrier (wait for all, then continue) is justified only when the next
  stage needs the whole set: dedupe across all findings before expensive
  verification, early exit when the total is zero, or a prompt that compares
  against "the other findings".
- DON'T add a barrier because stages "feel separate" or the code looks
  cleaner. Smell test: parallel → transform with no cross-item dependency →
  parallel. That middle step belongs inside a pipeline stage.

## Verification is the point

The value of a graph is less "more agents" than the structure around them
that produces confidence. A verifier sits on the edge and tries to kill each
finding before it reaches the answer.

- **Adversarial verify:** N independent skeptics per finding, each told to
  refute it and to default to "refuted" when unsure; keep it only if a
  majority fail to refute.
- **Perspective-diverse verify:** when a finding can fail more than one way,
  give each verifier a different lens (correctness, security, does it
  reproduce). Diversity catches what N identical checks miss.
- **Judge panel:** N attempts from different angles, scored by parallel
  judges; build on the winner and graft the best of the runners-up. Beats
  iterating one attempt when the solution space is wide.
- **Completeness critic:** a last agent that asks what was missed (a source
  unread, a claim unverified); its answer is the next round of work.
- The studio's `claude-code-loop` template applies the same idea to code: the
  Reviewer runs in a separate context and sees only the diff.

## Failure and isolation

- MUST tolerate missing inputs at every fan-in. In Claude Code, a failed
  agent in `parallel()` resolves to `null` instead of failing the batch —
  always `.filter(Boolean)`.
- Parallel nodes that **write files** can collide. Give each its own git
  worktree only when they actually write in parallel; it is expensive, not a
  default.
- **No silent caps.** If a run limits coverage (top N, sampling, no retry),
  log what was dropped. Silent truncation reads as "covered everything".

## Loops must converge

- For work of unknown size (bug sweeps, edge cases), **loop until dry**:
  keep spawning finders until K consecutive rounds turn up nothing new.
  Counters ("until 10 found") miss the tail.
- MUST dedupe new findings against **everything seen**, not only against
  confirmed results. Otherwise rejected findings come back every round, the
  loop never runs dry, and it pays to rediscover the same dead ends.
- Put a hard cap or a budget guard on every loop.

## Cost

- Subagents inherit the session model unless overridden, so a large run
  bills entirely at the session tier. Check the model before a big run.
- Tier only where you are confident: bounded, repetitive nodes (extract a
  field, classify) can run on a cheaper model or lower effort; synthesis and
  adjudication keep the strong one. Claude Code's own guidance is to leave
  the override off unless sure.
- Topology is the biggest latency lever; model choice is the biggest cost
  lever. Neither changes the graph's shape.

## Claude Code specifics

Fast-moving; recheck against the current docs.

- Workflows are opt-in: the user asks for one in their own words, invokes a
  workflow command, or turns on ultracode. They can spawn many agents and
  cost a lot of tokens.
- Scripts are plain JavaScript (no TypeScript), begin with a pure-literal
  `meta` block, and cannot call `Date.now()` or `Math.random()` (they would
  break resume). Pass timestamps in as arguments.
- Concurrency is capped (min(16, CPUs − 2) per workflow); excess calls
  queue. A run can be resumed: unchanged agent calls return cached results.
- Saved workflows live in `.claude/workflows/`, versioned with the repo and
  runnable by name.
- Good hybrid: scout inline first (list the files, scope the diff) to find
  the work list, then run the workflow over it. Chain single-phase workflows
  (understand → design → implement → review) and read each result before
  the next.

## Sources

0xCodez, "Graph Engineering with Claude: 14-Step roadmap",
`https://x.com/0xCodez/status/2079165300625330317` (published 2026-07-20,
read 2026-10-12). Promotional thread; its technical claims were checked
against the reference below, and two it makes (a bundled `/deep-research`
workflow, a save keybinding) could not be verified and are left out.

Claude Code's built-in workflow-authoring reference and Workflow tool
description, as shipped in Claude Code (read 2026-10-12).

Claude Code changes monthly; re-read when this file is more than six months
old.
