# SEO — AI search features and AI crawlers

How Google's AI Overviews and AI Mode pick pages, which robots.txt tokens
control AI search and AI training crawlers, what practitioners observe about
how assistants choose sources, and how to measure citations.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

## Google's AI features and AI crawlers

- **AI summaries take clicks.** Pew Research tracked 68,879 Google searches
  by 900 US adults in 2025: when an AI summary appeared, people clicked a
  regular result in 8% of visits, against 15% without one, and clicked a link
  inside the summary in 1%. Expect fewer clicks on question searches;
  buying and local searches are less affected.
- **Google's AI Overviews and AI Mode have no extra requirements.** A page is
  eligible as a supporting link if it is indexed and can be shown in Search
  with a snippet. Everything in the other SEO files applies; no special
  optimization is needed.
- **Google controls:** AI features are part of Search, so robots.txt rules for
  Googlebot are the control. To limit what is shown, use `nosnippet`,
  `data-nosnippet`, `max-snippet` or `noindex` ([appearance.md](appearance.md),
  [crawling-indexing.md](crawling-indexing.md)).
- **`Google-Extended`** is a robots.txt token only, with no user agent of its
  own. It controls whether crawled content trains Gemini models and grounds
  Gemini Apps and Vertex AI. It does **not** affect inclusion or ranking in
  Google Search.
- **OpenAI uses independent tokens:**
  - `OAI-SearchBot` surfaces pages in ChatGPT search. A site that blocks it
    is not shown in ChatGPT search answers (it can still appear as a bare
    link). Changes take about 24 hours to apply.
  - `GPTBot` crawls for model training. Blocking it opts out of training and
    does not affect ChatGPT search.
  - `ChatGPT-User` fetches pages when a user asks; robots.txt may not apply,
    and it is not used to decide what appears in search.
  - A blocked page can still show as a link and title. To keep it out, use
    `noindex` and allow crawling, as with Google.
- **Other engines' tokens** (vendor documentation as summarised by a
  practitioner source): Anthropic uses `Claude-SearchBot` (search),
  `Claude-User` (fetches a user asked for) and `ClaudeBot` (training);
  Perplexity uses `PerplexityBot` (search) and `Perplexity-User`, which
  generally ignores `robots.txt`. Decide each by purpose, as with OpenAI.
- **Check the CDN and firewall too.** Many block AI crawlers by default,
  whatever `robots.txt` says.
- **DON'T** add a blanket "block AI bots" robots.txt group. Blocking search
  crawlers (`Googlebot`, `OAI-SearchBot`) costs visibility. Blocking training
  crawlers (`GPTBot`, `Google-Extended`) is a business decision for the site
  owner, not an SEO fix — ask before adding it.

## How AI assistants pick sources (practitioner observations)

Not documented by any vendor. From people who log ChatGPT answers at scale
and from practitioner sources (mostly French data, 2026; read 2026-10-12 to
2026-10-15). Expect it to age within months.

- **Two kinds of answer.** With citations, the assistant searched the web.
  Without, it answered from training data, which lags the web by roughly a
  year or more — a brand launched this year is only reachable through search.
  So **GEO depends on SEO**: if nothing ranks, there is nothing to cite.
- **Query fan-out.** When it searches, ChatGPT rewrites the conversation into
  2–5 short search-engine queries, and they converge regardless of how the
  prompt was phrased: "best [category] [year] [country]", "[brand] reviews",
  "[competitor] alternative", sometimes `site:` on authority domains, and in
  both the user's language and English. The pages ranking for those queries
  — mostly roundups and comparisons — are what gets read.
- **The page types rotate; the method doesn't.** After a ChatGPT model
  update in August 2026, one vendor's data (Peec AI) shows listicles
  falling from about 16% to 8% of ChatGPT citations, comparison pages from
  9% to 6%, and fan-out queries shifting towards `site:` and "official"
  searches. **Decided:** the durable rule is to be named in whatever pages
  the engines cite *this quarter*, found by the monthly check below —
  not to bet on roundups as such. Treat any list of "cited page types" as
  dated the day it is written.
- So the lever is being **named in the pages the engines already cite**
  — at the time of writing: third-party "best of" lists, comparison pages,
  review platforms, Reddit threads. A list on your own site with yourself first has been observed to
  stop being cited; a ranking on someone else's site counts more.
- **Sources rotate** — one prompt draws on tens of sources over time, a
  different subset each month. A citation is a rotation you stay in, not a
  rank you hold. Refresh the lists you appear in yearly (year in the title).
- Authority is not the filter: small sites get cited, large ones get skipped,
  when the small site is on the right page.
- **Reddit's share varies by engine** and has moved by several times within
  a year; check which engine and which threads your buyers' questions
  actually surface before investing. On Reddit, say who you are in the
  first line and include where your product is the wrong choice.
- **What feeds the answers** (practitioner): pages that answer each
  question in the first one or two sentences of a section, then go deeper;
  identical facts (hours, services, address) everywhere the business
  appears; reviews on more than Google — Yelp and industry platforms show up
  often in ChatGPT's local recommendations.
- **Bing matters for ChatGPT** (practitioner, not confirmed by OpenAI's
  documentation): its search is reported to lean on Bing's index. Claim the
  Bing Places listing and verify the site in Bing Webmaster Tools — cheap
  insurance.
- Nothing above changes Google's position: no `llms.txt`, no special markup
  ([overview.md](overview.md#things-not-to-spend-time-on-skip)).

## Measuring AI visibility (practitioner)

- **Measure by hand.** Run ~10 buyer questions logged out, once a month, and
  note whether you are cited and from which page.
- Answers vary run to run: ask each question 3–5 times per engine in fresh
  sessions and record a rate with its sample ("3/5").
- Report the ladder separately — cited, mentioned, recommended, recommended
  against — not one "visibility" number.
- The ChatGPT API returns different sources than the web app, so a
  dashboard built on it measures something else.

## Sources

Google Search Central, `https://developers.google.com/search/docs/`:
`appearance/ai-features` (read 2026-10-05).

Google crawlers:
`https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers`
(read 2026-10-05).

OpenAI: `https://developers.openai.com/api/docs/bots` ·
`https://help.openai.com/en/articles/12627856-publishers-and-developers-faq`
(read 2026-10-05).

Pew Research Center, "Google users are less likely to click on links when
an AI summary appears in the results",
`https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/`
(read 2026-10-14).

Practitioner observations: Nicholas Dulait (ChatSEO), "How to use Claude
Opus 5.5 for SEO", Part 4,
`https://x.com/nicholasdulait/status/2108212094214529135` (read 2026-10-12),
relaying data from Links Garden's monthly ChatGPT prompt logs. One source,
French market; treat as hypotheses to test, not rules. BowTiedBills, "The
Most Valuable SEO Article Ever Written",
`https://x.com/bowtiedbills/status/2109881300890816850` (read 2026-10-14) —
what feeds the answers, Bing.

Other crawler tokens, CDN blocking, measurement and the August 2026
shift: `coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills`, shared via
`https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15) —
`ai-seo/references/platform-ranking-factors.md`,
`agent-readiness.md`, `format-volatility.md`,
`citations-vs-recommendations.md`. Its schema-for-AI and `llms.txt` advice is
not adopted (contradicts Google).

AI tooling moves fast; re-read these pages when this file is more than six
months old.
