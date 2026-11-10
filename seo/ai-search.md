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
- **B2B buyers start with AI.** G2's survey of 1,076 B2B software decision
  makers (March 2026): 51% now start their research with an AI chatbot more
  often than with Google (29% a year earlier); 85% think more highly of a
  vendor that AI includes in its answer; 69% ended up choosing a different
  vendor than they planned. (A widely shared "55%" is a misquote.)
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
- **DeepSeek** runs its own search index, open to developers since October
  2026 through Search and Fetch APIs ($0.75 per 1,000 calls each). Its
  documentation names no crawler, user agent or opt-out. One tester found
  its Fetch API used a generic Firefox user agent with a Chinese
  `Accept-Language`, came from Huawei Cloud (Hong Kong) addresses, didn't
  run JavaScript, and returned pages that `robots.txt` disallowed — so
  `robots.txt` can't be counted on to keep it out. Anything that must stay
  private needs authentication, not a disallow line.
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
  review platforms, Reddit threads. A list on your own site with yourself first
  has been observed to
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
- **A page an assistant can quote** *(practitioner; one Italian B2B SaaS
  built this way, results not yet shown)*: headings that are complete claims
  and make sense lifted out alone ("X raises conversion by 8% on average"),
  each followed by two or three factual sentences; an FAQ answering what
  buyers ask before choosing (price, time to go live, integrations, error
  rate); **public, specific prices**, so an assistant can quote them; a
  "category alternative vs us" comparison; and company facts (legal name,
  location, founder, offer) in structured data. Every number on such a page
  needs its source and date — an unsourced claim gives nobody anything to
  cite. **Decided:** the same site uses `FAQPage` markup and a full-content
  `llms.txt`; both stay Skip — Google documents no benefit
  ([overview.md](overview.md#things-not-to-spend-time-on-skip)) and nothing
  shows another engine uses them. Its 80 planned pages for near-zero-volume
  queries are unbuilt and unproven, so the cadence and unique-content rules
  in [content.md](content.md#cadence-practitioner) stand.
- **Fix how directories describe you.** Old or wrong descriptions on tool
  directories and review sites (a mis-filed category, a previous company
  name) are what assistants repeat; correcting them can matter more than
  new pages.
- **What feeds the answers** (practitioner): pages that answer each
  question in the first one or two sentences of a section, then go deeper;
  identical facts (hours, services, address) everywhere the business
  appears; reviews on more than Google — Yelp and industry platforms show up
  often in ChatGPT's local recommendations.
- **Bing matters for ChatGPT** (practitioner, not confirmed by OpenAI's
  documentation): its search is reported to lean on Bing's index. Claim the
  Bing Places listing and verify the site in Bing Webmaster Tools — cheap
  insurance. Its query data also fills gaps in Search Console
  ([content.md](content.md#improving-existing-pages-practitioner)).
- Nothing above changes Google's position: no `llms.txt`, no special markup
  ([overview.md](overview.md#things-not-to-spend-time-on-skip)).

## Measuring AI visibility (practitioner)

- **Measure by hand.** Run ~10 buyer questions logged out, once a month, and
  note whether you are cited and from which page. Cover the question types
  buyers ask: best providers, you vs a named competitor, how to solve the
  problem, cost. Put the results next to incoming leads for the same month;
  site changes take months to show, off-site presence longer (one agency's
  experience).
- Answers vary run to run: ask each question 3–5 times per engine in fresh
  sessions and record a rate with its sample ("3/5").
- Report the ladder separately — cited, mentioned, recommended, recommended
  against — not one "visibility" number.
- The ChatGPT API returns different sources than the web app, so a
  dashboard built on it measures something else.
- **The sources cited for competitors are your target list:** for each
  answer that names a competitor and not you, note the cited pages; those
  are the sites to be on. Keep the results in a dated log.
- **DON'T read Google's Vertex AI Search docs as AI Mode's ranking
  manual.** **Decided:** a widely shared post claims Google "leaked" how AI
  search ranks because its enterprise Vertex AI Search (Discovery Engine)
  documents signals and 500-token chunking. That is a product for
  customers' own sites; Google documents no extra requirements for AI
  Overviews or AI Mode, and the advice drawn from it (clear headings,
  direct answers early) is already here. The post sells FAQ-schema and
  backlink packages; neither is adopted.
- **DeepSeek exposes its own scores.** Its Search API returns, per result,
  an `authority` tier (0–4; 3 or more counts as highly authoritative) and a
  `rerank_score` (0–3; 1.5 or more is high quality) — documented by
  DeepSeek. A `site:yourdomain` query shows your tier cheaply. In one
  tester's sample, authority was set **per host**, not per domain (a
  subdomain scored differently), and user uploads on trusted hosts (spam
  PDFs on a `.gov` site) inherited the top tier — so read the tier as a
  property of where content sits, not of its quality. Pages without a
  machine-readable date dropped out of date-filtered searches.

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

DeepSeek: `https://api-docs.deepseek.com/guides/search` (read
2026-10-23); Suganthan Mohanadasan, "DeepSeek search API" tests,
`https://suganthan.com/blog/deepseek-search-api/`, via
`https://x.com/suganthan/status/2112111235818991962` (read 2026-10-23) —
110 calls from one location; preliminary, his word.

Competitor-citation targets: ChadSE0 (ChatSEO),
`https://x.com/chadse0/status/2115054790002491723` (read 2026-10-28). The Vertex
AI Search claim: Alex
Groberman (SEO Stuff), `https://x.com/alexgroberman/status/2012536184023462013`
(read 2026-10-28), citing Metehan
Yesilyurt's analysis; rejected as above.

G2, "The Answer Economy" (2026-04-15),
`https://company.g2.com/news/g2-research-the-answer-economy` and
`https://learn.g2.com/g2-2026-ai-search-insight-report` (read 2026-11-10).

Quotable-page anatomy and directory consistency: orygo.ai homepage and
`llms.txt` as live examples, `https://orygo.ai/it` (read 2026-11-10), via
Davide Petruzzi's post
`https://it.linkedin.com/posts/davidepetruzzi_geo-canale-super-underrated-per-b2b-saas-activity-7525906658267381760-rUnY`
(read 2026-11-10). Audit question types: Hanami srl, "Visibilità nelle
risposte AI", `https://hanamisrl.com/servizi/visibilita-risposte-ai/` (read
2026-11-10).

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
