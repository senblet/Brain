# AI — external skill libraries

Public skill repositories that have been read in full, and which of their
skills are worth loading for the studio's work. The rules worth keeping are
already folded into the topic files; this file only records the verdict on
each skill, so nobody has to re-read the repos to decide. How to write good
skills: [agents.md](agents.md#writing-skills).

**Tags:** as in the [README](../README.md#how-notes-are-written). Verdicts
are from a full read on the date given; skills change, so recheck before
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

## Sources

- `https://github.com/coreyhaines31/marketingskills` and
  `https://github.com/refoundai/lenny-skills`, shared via
  `https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15).
- `https://github.com/Leonxlnx/taste-skill`, shared via
  `https://x.com/lexnlin/status/2110122115240432021` (read 2026-10-15).

Skill libraries change weekly; re-read when this file is more than six
months old.
