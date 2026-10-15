# AI — evaluating LLM features

How to know whether an AI feature in a product works — reports written by a
model, a Claude-written profile, a Gemini review step — and keep it working
as prompts, code and models change. For agents that do the studio's own
work, see [agents.md](agents.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Practitioner
method from Lenny's Newsletter guest posts collected in the `lenny-skills`
repo — chiefly Hamel Husain and Shreya Shankar, who also sell an evals
course. Splits and sizes are theirs.

---

## Start from real failures

- **MUST start from real traces, not generic metrics.** Read whole traces
  (prompt, tool calls, retrieved context, output) and write down where it
  goes wrong before building any automated test.
- **Open coding:** sample ~100 interactions (random at first); for each,
  pass or fail plus a critique detailed enough to brief a new hire or reuse
  as a few-shot example. Short critiques are the usual mistake.
- **Axial coding:** group the critiques into fewer than ten failure modes
  and count them. A model may draft the grouping; a person reviews it.
- **One domain expert owns the quality labels**, not a committee. Keep the
  loop cheap enough to repeat.
- Later rounds: pull 20–50 low-scoring examples per segment, worst segments
  first, into a table — pattern, description, frequency, impact, fix.

## Choosing evaluators

- **Per failure mode:** objective (valid JSON, an ID present, the code runs)
  → a code assertion; subjective (tone, relevance) → a model judge. Code
  checks are cheaper and deterministic.
- DON'T report off-the-shelf "hallucination" or "toxicity" scores as product
  metrics; at most, sort traces by them and read both ends.

## Model judges

- **SHOULD: one failure mode per judge, binary pass/fail.** No 1–5 scales —
  the gap between 3 and 4 is inconsistent; nuance goes in the critique.
  (Banded scores still fit lead scoring —
  [agents.md](agents.md#classifying-at-volume).)
- Judge prompt in four parts: the role, the data (`{text}`), the goal with
  pass and fail defined, your own terms defined — plus one or two good and
  bad examples.
- **MUST validate the judge against expert labels before trusting it.**
  Split labelled data roughly 10–20% train (few-shot examples), 40–45% dev
  (iterate the prompt), 40–45% held-out test.
- Measure the judge by its true-positive and true-negative rates, not overall
  accuracy, and pick which matters by the cost of each error (harmful advice
  → catch every fail; creative output → don't reject good work). Study the
  disagreements, not the agreement rate.
- The judge runs in a separate context from the thing it judges.

## Datasets and CI

- **Start with a reference set of 20–100 examples**: input, expected output,
  notes, and whether it came from logs or was written. Cover the main uses
  before edge cases.
- **The golden set is built on purpose**, not sampled: core features, edge
  cases from error analysis, and **one regression case per significant bug
  fixed**. Run it with code checks on every prompt, code or model change;
  fail the build on a regression. A pass means no known failure came back —
  not that the output is good.
- **Before swapping models**, run the same set through the new model and
  compare.
- In production: log full traces; run validated judges on samples
  asynchronously; every new failure joins the golden set.
- Synchronous guardrails only for critical failures — mostly fast
  deterministic checks with a very low false-positive rate. Blocking a good
  answer is a bug.

## Diagnosing pipelines

- **Retrieval (RAG):** score the retriever (recall of the right documents in
  the top k — the source suggests k of 3–5 for facts, 10–20 for synthesis)
  separately from the generator (faithful, relevant). Fix retrieval first.
- **Multi-step agents:** tabulate failed traces by last successful step ×
  failing step; fix the most frequent transition.
- **Chat:** judge whole sessions. When one fails, repeat the failing
  question as a single turn — if it still fails, the cause is knowledge or
  retrieval, not conversation memory.

## Shipping an AI feature

- **Earn autonomy step by step:** v1 suggests or routes; v2 drafts something
  a person edits; v3 acts, with a human fallback. Each step earned with
  evals; every human correction logged as eval data.
- **Before a version ships:** a scoped capability, a reference set, logging
  of inputs, outputs and user actions, a way for a person to take over, evals
  run, a small first cohort.
- **Design for the error rate.** If one output in five is good, show several.
- DON'T open with an empty prompt box: give starting points, options, and
  ways to adjust the output.
- Prototype for feasibility first — is it possible, is it actually good? —
  before designing the interface.
- DON'T rely on prompt instructions against prompt injection ("ignore
  malicious instructions"), separators or blocklists. Limit what the model
  can do instead (Sander Schulhoff).

## Sources

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15): `ai-evals` (`references/artifacts.md`: "Building eval systems
that improve your AI product", "Beyond vibe checks", "Why your AI product
needs a different development lifecycle"), `ai-native-ux`,
`ai-product-strategy`. The repo files newsletter guest posts under Lenny's
name; check bylines before quoting.

AI practice moves fast; re-read when this file is more than six months old.
