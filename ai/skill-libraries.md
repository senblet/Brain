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

## SEO skill libraries

Nine repos from one practitioner's list (read 2026-11-11). Coverage is
uneven: the large ones were read in part, skill files first, with every
skill searched for the known contradictions (character limits, word
counts, keyword density, FAQ/HowTo markup, `llms.txt`, `GPTBot` vs
`OAI-SearchBot`, invented numbers). Scripts were read, not run. A quick
test for any SEO skill: ask which bot decides whether you appear in
ChatGPT search — `OAI-SearchBot`, not `GPTBot`
([seo/ai-search.md](../seo/ai-search.md#googles-ai-features-and-ai-crawlers)).
DON'T trust a 0–100 score from any of them: none of the weights were
checked against rankings or citations. Read the findings, ignore the
number.

**`RomeoSEO/seo-skills`** — MIT, 49 skills. The most careful library: says
"not checked" instead of inventing numbers and gets the bot tokens, FAQ and
HowTo right. Install from the clone, not `install.sh` (which downloads a
zip from the author's site). Footers advertise the author's paid work.

| Use | Skills |
|---|---|
| **Load as-is** | `technical-seo-audit`, `schema-markup`, `xml-sitemap-check`, `seo-change-monitor` (read its script first), `ai-brand-facts`, `ai-prompt-research`, `ai-traffic-analytics`, `query-fan-out-coverage`, `best-of-list-inclusion`, `comparison-page-writer`, `keyword-cannibalization-check`, `search-intent-match`, `site-migration-check`, `hreflang-international`, `backlink-profile-review`, `reddit-quora-answers`, `seo-content-brief` |
| **Load with overrides** | `ai-agent-readiness` (skip the `llms.txt` steps), `on-page-seo-review` and `title-meta-ctr` (ignore character counts), `seo-blog-writer` and `seo-content-qa` (ignore keyword-in-first-100-words and the FAQ-schema check), `ai-citable-pages` and `ai-search-visibility` (ignore the 40–80-word and "~40%" figures), `internal-linking-plan` (ignore links-per-words), `programmatic-seo-plan` (a first batch of 50–200 pages breaks the [cadence](../seo/content.md#cadence-practitioner)) |
| **Don't load** | `dataforseo-ai-tracker` (paid, scrapes ChatGPT through a vendor), `chatgpt-business-profile` (tied to the author's paid MCP), `posthog-change-impact` (not our stack) |

**`AgriciDaniel/claude-seo`** — MIT, 26 skills, 19 agents. Precise on
crawlers, structured data and `robots.txt`; it says "Score only what was
measured" once, then scores everything out of 100 with fixed weights.

| Use | Skills |
|---|---|
| **Load as-is** | `seo-sitemap`, `seo-hreflang` |
| **Load with overrides** | `seo-technical` (ignore the score, URL-length and framework items), `seo-schema` (ignore "recommend freely" for review markup), `seo-geo` (ignore the readiness score, `llms.txt`, FAQ sections and word counts), `seo-page` and `seo-content` (ignore scores, character and word-count gates, heading-order rules), `seo-google` (read-only GSC, PageSpeed, CrUX; not the Indexing API), `seo-drift` (baseline and compare before a deploy) |
| **Don't load** | `seo` hub (makes the agent append a link to the author's paid community after reports), `seo-backlinks` (toxic-link scores, disavow), `seo-competitor-pages` (self first, own review markup), `seo-content-brief`, `seo-plan` and `seo-agentic` (`llms.txt`), `seo-local`, `seo-maps`, `seo-ecommerce`, the paid extensions |

Install cautions: `/seo setup` builds a venv and downloads Chromium;
`install.sh` copies everything into global `~/.claude`; a PostToolUse hook
runs on every edit of `.html`/`.vue`/`.tsx` files and blocks HowTo markup.

**`nowork-studio/notfair-plugin`** — MIT, 45 skills. Every account (Search
Console, GA4, ads, WordPress) connects through the author's hosted OAuth
server, so their data leaves the machine. Current skills are sound on FAQ,
HowTo and bot tokens. **Study** `docs/safety.md` (the rule is in
[agents.md](agents.md#guardrails-live-in-the-tools-not-the-prompt)) and
`seo-drift`; load `meta-tags-optimizer` and `content-writer` only without
their character limits and 1,000-word minimum. Don't connect client
accounts through it.

**`every-app/open-seo`** — MIT. A self-hosted Semrush/Ahrefs alternative
(Docker, ~4 GB RAM) that needs DataForSEO credit and sends anonymous
telemetry unless `OPENSEO_TELEMETRY_DISABLED=1`. Its skills are well
disciplined ("Search volume is not visits", observed vs inferred). Its AI
visibility numbers come from the ChatGPT API, which cites differently from
the app. **Skip the app** unless a project needs rank or backlink data
beyond Search Console and Bing; **study** `seo-audit` and
`ai-prompt-research`.

**`zubair-trabzada/geo-seo-claude`** — MIT. **Don't load.** It says
blocking `GPTBot` removes you from ChatGPT search, treats `ClaudeBot` as
search, scores `llms.txt`, recommends FAQ and HowTo markup and invents
benchmarks; it installs with `curl … | bash` from `main`. Its one good
idea, checking the live `robots.txt` for Cloudflare's managed block, is in
[seo/ai-search.md](../seo/ai-search.md#googles-ai-features-and-ai-crawlers).

**`TheCraigHewitt/seomachine`** — MIT. A blog-writing pipeline. **Don't
load.** It targets 1–2% keyword density, asks for mini-stories with names
"even if fictional", has the editor turn "many businesses" into "73%", and
"scrubs" text so it looks human-written. **Study** the pipeline shape only:
research, section-by-section drafts, a score gate that sends failures to
review, publish as WordPress drafts.

**`Ryze-AI-Adgent/open-seo-mcp-skills`** — MIT, 8 skills. Good rules ("Never
invent volumes", never fabricate link counts), but every skill needs the
vendor's hosted connector, which carries Search Console, GA4 and Ads data.
**Skip**; the read-only Search Console and treg routes cover it.

**`AminForou/mcp-gsc`** — MIT. A local Search Console MCP server: stdio,
`webmasters.readonly` scope, deletes blocked unless `GSC_ALLOW_DESTRUCTIVE`
is set, no telemetry. **Use with care:** pin a reviewed version (`uvx`
pulls the latest release), stdio only (SSE mode has no auth).

**`i365dev/awesome-seo`** — MIT, a reading list. **Study only** its
Cloudflare/CDN and measurement sections; much of the rest is dated.

## Model routing

`Rajvardhman05/claude-model-router` (MIT, one `SKILL.md`, read
2026-11-10): a skill loaded before spawning subagents that picks each one's
model, condensed from the claude.dev model guide. **Load with one fix:** move
"well-scoped edits against a clear spec → sonnet" out of its delegation
table — edits stay on the main model
([models.md](models.md#mixing-models)). It doesn't change the built-in
Explore subagent; add the `Explore` file from that section too.

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
- The nine SEO repos above, listed in TheoAGI's "The only SEO/GEO article
  you need", `https://x.com/theoagi/status/2120163220312699025` (read
  2026-11-11).

Skill libraries change weekly; re-read when this file is more than six
months old.
