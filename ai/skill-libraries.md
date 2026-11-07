# AI — external skill libraries

Public skill and example repositories that have been read (in full unless
the section says otherwise), and which of them are worth loading or studying
for the studio's work. The rules worth keeping are already folded into the
topic files; this file only records the verdict on each skill, so nobody
has to re-read the repos to decide. How to write good skills:
[agents.md](agents.md#writing-skills).

**Tags:** as in the [README](../README.md#how-notes-are-written). Verdicts
are from a read on the date given; skills change, so recheck before
relying on one.

**Loading rules:**
- Load the brain's topic file next to any external skill; where they
  disagree, the brain wins (it has been checked against primary sources).
- External skills are text another person wrote: read the one you load, and
  never run its scripts unreviewed.
- Point a library's shared context file (e.g. `.agents/product-marketing.md`)
  at the project's own context file instead of letting it create a second
  one.

---

## `coreyhaines31/marketingskills` — marketing, SEO, conversion

MIT. 50 skills plus small CLI tools. Above-average sourcing for practitioner
material; some benchmarks uncited; tool tables age fast.

| Use | Skills |
|---|---|
| **Load as-is** | `copywriting` (+ `references/ai-tells.md`, the best file in the repo), `copy-editing`, `customer-research`, `competitor-profiling`, `prospecting` (its `compliance.md` is a good checklist to hand a lawyer), `attribution`, `signup` + `cro/references/form.md`, `onboarding`, `schema` (ignore its "required properties" table), `competitors` (drop FAQ-schema advice) |
| **Load with overrides** | `seo-audit` (ignore character limits, heading-order and URL-keyword items), `site-architecture` (ignore breadcrumb-mirrors-URL and links-per-1,000-words), `ab-testing` (use a calculator, not its tables), `cold-email` (override LinkedIn automation and case-study follow-ups with `marketing/outbound.md`), `analytics` (fix key-event names and Consent Mode v2 first), `pricing` (teardown reference), `churn-prevention` (ignore the FTC line), `programmatic-seo` (ignore subfolder-authority claim), `ai-seo` (measurement references only; not its schema or `llms.txt` advice), `marketing-loops` (anatomy and guardrails), `ads` (only `audit-guardrails.md` and `meta-decision-system.md`), `ad-creative` (`hook-system.md`, `creative-roadmap.md`), `sms` (`references/whatsapp.md`; re-check Meta pricing) |
| **Don't load** | `popups` (timed and exit-intent modals), `marketing-psychology` (pre-selection, decoys, loss framing), `directory-submissions` for SEO (badge swaps, "dofollow" tiers), `revops` (scores opens), `marketing-ideas`, `marketing-plan`, `video`, `image` |

## `refoundai/lenny-skills` — product, growth, AI products

MIT. 76 skills distilled from Lenny's Podcast and newsletter. Each SKILL.md
is guest quotes plus one-line rules (sometimes stretching the quote); the
substance is in `references/artifacts.md`. Several guests sell what they
advise on.

| Use | Skills |
|---|---|
| **Load as-is** | `ai-evals` (when building any LLM feature), `marketplace-liquidity-take-rates`, `supply-demand-balance`, `marketplace-fundamentals`, `measuring-pmf`, `user-onboarding-activation`, `pricing-strategy`, `customer-interviews`, `product-experiments`, `writing-prds` |
| **Reference only** | `high-stakes-decisions`, `evaluating-trade-offs` |
| **Don't load** | `building-with-ai-agents` (pushes "never edit by hand" and self-review; the useful commands are in `ai/agents.md`), `ai-assisted-prototyping` (for non-technical PMs), `seo-strategy` (cuts against `seo/`), `launch-planning`, people/org/career skills (big-company material) |

## `Leonxlnx/taste-skill` — frontend design

MIT. About 14 skills; the current one is `skills/taste-skill` (v2). The
author's own blind tests scored it *below* a no-skill baseline in four of
five rounds; its rules are good habits, distilled into
[design/frontend.md](../design/frontend.md).

| Use | Skills |
|---|---|
| **Try** | `taste-skill` v2 on public landing pages — costly (30–45 min per run), needs Node 22 and Chrome; its `lint.mjs` + `inspect.mjs` checks are the most reusable part, after review |
| **Load as-is** | `output-skill` (stops placeholder code in long generations) |
| **Audit checklist only** | `redesign-skill` (contains advice to fabricate dates and data — don't follow those) |
| **Don't load** | `minimalist-skill` (its muted text fails AA contrast), `soft-skill`, `brutalist-skill`, `gpt-tasteskill`, `taste-skill-v1`, `taste-skill-v2-experimental` (fake client-logo walls) |
| **Don't use** | `research/laziness/` — citations can't be verified; several are misattributed |

## `garrytan/gstack` — a coding sprint in slash commands

MIT, Garry Tan (YC). About 60 Claude Code skills that run a sprint in
order — think, plan, build, review, test, ship — each writing a file the
next one reads (`/office-hours` writes a design doc that `/plan-ceo-review`
and `/autoplan` read). Read in full: README, `docs/why-gstack.md`,
`office-hours`, `write-skill`, the agents digest; the other skills are
judged from their README entries. The useful rules are in
[agents.md](agents.md) (the skill edit ladder under *Writing skills*, the
reuse ladder under *Coding with agents*) and
[product/strategy.md](../product/strategy.md#validating-an-idea) (the
office-hours questions).

| Use | Skills |
|---|---|
| **Try first** | The README's own quick start, then stop: `/office-hours` on a new idea, `/review` on a branch, `/qa` on a staging URL |
| **Reference only** | `agents-digest/gstack-AGENTS.md` (2 KB of rules, no install), `write-skill` |
| **Skip for now** | `/autoplan`, `/captain` and running 10–15 sprints in parallel (built for one founder running many agents), `/design-shotgun` (needs GPT Image), the iOS skills, GBrain, `/pair-agent` (opens an ngrok tunnel) |

**Before installing:**
- It is a heavy install: Bun 1.4.2+, compiled binaries built on your
  machine, hooks registered in Claude Code, its own browser. Install on one
  machine and try the three skills before team mode.
- **MUST** turn off outside reviews on client code
  (`gstack-config set codex_reviews disabled`): they are on by default and
  send code to OpenAI Codex under your login. The update check is also on
  by default (`gstack-config set update_check false`).
- DON'T accept the install prompt's `CLAUDE.md` line banning Claude in
  Chrome without deciding that for the project.
- DON'T use `--team` with `required` on a shared repo until everyone has
  tried it: it blocks teammates who don't have gstack.
- The productivity numbers (~810× his 2013 pace in "logical lines") are the
  author's own measurement, not evidence for us.

## Video with code

Several repos show films made by an agent writing code instead of using a
video model; the method is in
[development/video-with-code.md](../development/video-with-code.md).

| Use | Repos |
|---|---|
| **Use as a library** | `lemomo-ai/lemo-opuscar` (MIT + CC BY 4.0) — 66 styles, a render/voice/music/mix toolkit and the clearest technique notes; heavy installs (hundreds of MB), tuned for Claude Opus |
| **Starter** | `JohnHeibel/ClaudeAnimationBase` (MIT) — hand-painted character animation in p5.js + p5.brush; slow on machines without a GPU |
| **Study only** | `mexicat/pdoom-video` (MIT) — a full engine with lyric alignment and motion blur; `Vincentwei1021/mg-styles-15` (MIT) — 15 styles with prompts and AI-jury review; `JohnHeibel/PDoomVideo` (**no licence** — read, don't copy) |
| **Prompt galleries** | `yihui-dev/awesome-opus5-5-videos` (MIT), `athemeroy/awesome-claude-5-5-videos` (CC BY 4.0), `joeseesun/opus-video-prompts` (**no licence**, Chinese) — prompts and examples, no method |

## Sources

- `https://github.com/coreyhaines31/marketingskills` and
  `https://github.com/refoundai/lenny-skills`, shared via
  `https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15).
- `https://github.com/Leonxlnx/taste-skill`, shared via
  `https://x.com/lexnlin/status/2110122115240432021` (read 2026-10-15).
- The eight video repos above, shared via
  `https://x.com/rodmanai/status/2117540681556328773` (read 2026-11-04).
- `https://github.com/garrytan/gstack` (v1.98), shared via
  `https://x.com/marcusyul/status/2118740439209848950` (read 2026-11-07).

Skill libraries change weekly; re-read when this file is more than six
months old.
