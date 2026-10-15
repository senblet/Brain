# Operations — specs, scope and decisions

How the studio decides what to build and keeps it small: framing a request,
writing a one-page spec, time budgets instead of estimates, prototypes,
making decisions, and writing so others can act. Applies to client work and
the studio's own products. Coding with agents is in
[ai/agents.md](../ai/agents.md#coding-with-agents).

**Tags:** as in the [README](../README.md#how-notes-are-written). Operator
practice from Lenny's Podcast and newsletter (via `lenny-skills`), named
where attributed; opinion, not data.

---

## From request to spec

- **Frame before shaping.** Turn the raw request ("build a calendar") into a
  bounded problem ("users can't see free slots") before discussing
  solutions (Ryan Singer).
- **A one-page spec:**
  - the problem in one sentence — short, an unmet need, what and why, no
    solution — plus what you are *not* solving;
  - 3–5 data points showing the problem is real;
  - a success metric with a target;
  - a specific audience (rarely "all users");
  - the solution at the detail the builder needs;
  - everything else in an appendix.
- **Fewer than about ten moving pieces** someone can hold in their head;
  more means it's too big or too vague (Ryan Singer).
- DON'T say "this should be quick". Ask "what would need to be true for this
  to be doable in X days?"

## Scope and time

- **Set an appetite, not an estimate:** the most time the work is worth,
  then cut scope to fit. If it won't finish in time, don't extend — send it
  back to shaping and ask what was unclear (the "circuit breaker", Ryan
  Singer).
- Something working that tests the key assumption by about 10% of the time
  budget (Nan Yu).
- **Cut until it breaks:** remove each element and ask "is it still
  useful?" Ship the core that's left; let real complaints choose the next
  week's work.
- **Prototype fidelity matches the audience:** quick and rough for internal
  decisions, polished for clients and users — and say which one it is.
  Prototype code is expected to be thrown away.
- **Build and buy:** buy the 90% that is commodity, build the 10% that makes
  it yours (Austin Hay).

## Decisions

- **Sort by reversibility.** Trivial: just pick. Reversible: decide fast,
  with roughly 70% of the information. Irreversible: slow down and write it
  down — the workspace already asks for a short paragraph on any expensive
  decision.
- **One decisive reason.** If no single reason would justify the decision on
  its own, it isn't justified yet; a pile of weak reasons often hides a
  strong reason against (Rahul Vohra, from Reid Hoffman).
- **Pre-mortem big launches:** "It failed six months from now — why?"
  Everyone writes alone first; sort risks into real threats, overblown ones
  and the unspoken. Set kill criteria with the action for each warning sign
  decided in advance (Shreyas Doshi, Annie Duke).
- For a large build or tech investment, compare all of it now, part now, or
  none — each on time (best and worst case), people, short- and long-term
  impact and risk — and ask what happens if you don't.

## Writing so others can act

- **The answer first**, then "Context:" below. Keep asks and decisions apart
  from information (Wes Kao).
- A recommendation runs **situation → complication → answer**. For a
  trade-off, write "We must choose between X and Y" and lead with an
  opinionated recommendation.
- **AI as editor, not ghostwriter:** "What did I miss? Which claims am I not
  supporting? Which sentences don't sound like me?" (Seth Godin).

## Sources

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15): `writing-prds` (one-pager template, problem-statement
attributes, Ryan Singer), `shipping-velocity`, `ai-assisted-prototyping`,
`high-stakes-decisions`, `evaluating-trade-offs`, `written-communication`,
`executive-communication` — SKILL.md and `references/artifacts.md`.

Re-read when this file is more than a year old.
