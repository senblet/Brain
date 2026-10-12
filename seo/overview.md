# SEO — overview

Project-agnostic rules for building and editing websites so they are easy for
search engines to crawl, index and understand, and worth a searcher's click.
To use them in a project, copy the `seo/` folder in (for example as `docs/seo/`)
and reference `overview.md` from `AGENTS.md` / `CLAUDE.md`; project-specific
facts belong there, not here.

**Where it comes from.** The rules are drawn from Google Search Central
documentation (read in full on 2026-09-22; the SEO Starter Guide itself was
last updated 2025-12-10), Google's AI-features and crawler pages and OpenAI's
crawler documentation (read 2026-10-05), Google's Trends and Search Console
pages (read 2026-10-06), and Google Business Profile help (read 2026-10-12).
On top of that, sections marked *practitioner* hold methods from SEO
consultants (read 2026-10-12); they never override Google's documentation and
their numbers stay theirs. Where Google says something is optional or not
worth worrying about, these files say so too — do not upgrade a "nice to
have" into a rule.

*Started from [senblet/seo-md](https://github.com/senblet/seo-md), which
stays the Google-only public version; these files add the practitioner
sections and `local.md`.*

**How to read it.** **MUST** = required for eligibility or a spam-policy line;
breaking it can keep pages out of Search. **SHOULD** = best practice with real
effect. **DON'T** = actively harmful. **Skip** = effort Google says is wasted.

## Files

| File | What it covers |
|---|---|
| [overview.md](overview.md) | Ground truth, eligibility, spam policies, page experience, promotion, what to skip, monitoring, pre-ship checklist |
| [crawling-indexing.md](crawling-indexing.md) | Discovery, robots.txt and `noindex`, sitemaps, canonicals, redirects, status codes, JavaScript sites, URLs, international sites |
| [content.md](content.md) | Helpful content, E-E-A-T, AI-generated content, keyword research and choosing pages, ads and interstitials, links and earning them, images |
| [appearance.md](appearance.md) | How pages look in results: titles, snippets, video, structured data |
| [ai-search.md](ai-search.md) | Google's AI features, AI crawler tokens (Google, OpenAI), how assistants pick sources |
| [local.md](local.md) | Local businesses: map ranking factors, Business Profile, reviews, the page it points to |

---

## Ground truth

- SEO is helping search engines understand content and helping users decide
  whether to visit. There are no secrets that rank a page first, and
  appearing in Google costs nothing — anyone claiming otherwise is wrong.
- Google works in three stages: **crawl** (discover URLs, fetch, render
  JavaScript in a recent Chrome), **index** (understand the page, cluster
  duplicates, pick a canonical), **serve** (rank for a query). A page can drop
  out at any stage. Meeting every guideline does not guarantee crawling,
  indexing or ranking.
- Canonical preferences and sitemap submissions are **hints**, not commands;
  Google may choose differently.
- Changes take hours to months to show. Wait **a few weeks** before judging an
  SEO change; iterate if needed. Not every change has a visible effect.
  *(practitioner)* A dip right after a change is normal — give it up to ~2
  months before reverting; a new domain takes roughly 6 months before
  anything compounds.
- The single biggest lever is **content people find compelling and useful**.
  Technical SEO removes obstacles; it does not create demand.

## Eligibility — the technical minimum (MUST)

A page is only eligible for indexing if **all three** hold:

1. **Googlebot isn't blocked** — not disallowed in robots.txt, not behind a
   login, not otherwise access-controlled.
2. **It returns HTTP `200`.** 4xx/5xx pages are not indexed.
3. **It has indexable content** — text in a supported file type, not in
   violation of the spam policies.

Also:
- Google must see the page **the way a user does**. Never block the CSS,
  JavaScript or images needed to render it.
- Crawling comes from the **US**, usually without `Accept-Language`. If content
  varies by location or language, make sure what that crawler sees is what you
  want indexed.
- Put key information **in text, not in images**.

## Spam policies — never do these

Violations can demote a page or remove a whole site. **MUST NOT:**

- **Cloaking** — different content for search engines than for users.
  (Paywalls are fine if Google sees the full gated content, per Flexible
  Sampling guidance.)
- **Doorway pages** — near-duplicate pages or domains made to rank for similar
  queries (e.g. one page per city) that funnel to one destination.
- **Expired domain abuse** — buying old domains to host low-value content.
- **Hidden text or links** — same-colour text, off-screen CSS, zero font size
  or opacity, one-character links. (Accordions, tabs, sliders, tooltips and
  screen-reader-only text are fine.)
- **Keyword stuffing** — unnatural repetition, lists of cities or phone numbers.
- **Link spam** — buying, selling or exchanging links for ranking, automated
  links, links required by contract, paid or advertorial links without
  `rel="sponsored"`/`nofollow`, footer/widget link networks, optimized-anchor
  forum signatures.
- **Machine-generated traffic** — automated queries to Google, including
  scraping results for rank checking. *(Agents: never scrape Google Search;
  use Search Console or its API.)*
- **Malicious practices** — malware, unwanted software, **back-button
  hijacking**.
- **Misleading functionality** — promising a tool or service that doesn't work.
- **Scaled content abuse** — many low-value pages for rankings, by AI,
  scraping, stitching, synonymizing or translating. Exclude such content from
  Search if it exists.
- **Scraping** — republishing others' content without added value or citation.
- **Site reputation abuse** — hosting third-party content mainly to exploit the
  host's ranking signals.
- **Sneaky redirects** — sending users somewhere different from what search
  engines see. (Site moves, consolidation and post-login redirects are fine.)
- **Thin affiliation** — affiliate pages copied from the merchant with nothing
  added.
- **User-generated spam** — moderate public areas; qualify UGC links.
- **Policy circumvention** — new subdomains or sites to keep violating.
- **Scams and fraud** — impersonation, fake support, false business details.
- Also watch for **hacked content**: injected code, pages, links or redirects.

## Page experience

- **Core Web Vitals are used by ranking**; aim for good scores, but chasing a
  perfect score purely for SEO is rarely worth it. There is no single "page
  experience signal".
- Serve over **HTTPS**; migrate from HTTP.
- **Mobile-friendly** — Google crawls with a mobile crawler by default.
- No excessive or distracting ads; no intrusive interstitials; make the main
  content clearly distinguishable.
- Tools: PageSpeed Insights, Lighthouse, Search Console's Core Web Vitals and
  HTTPS reports.

## Promotion

- Tell people: social media, communities, ads, offline materials (URL on cards
  and signage), opt-in newsletters. **Word of mouth** is among the most lasting
  channels and grows from genuine community engagement.
- Links from other sites happen naturally over time; don't manufacture them
  ([spam policies](#spam-policies--never-do-these)). Over-promotion can tire
  users and look like manipulation.

## Things not to spend time on (Skip)

- **Meta keywords** — Google doesn't use them.
- **Keywords in the domain or URL path** — hardly any ranking effect beyond
  breadcrumbs. Name the site for the business.
- **TLD choice for ranking** — no effect, with one real exception: a
  country-code TLD (`.cl`, `.fr`) is a strong signal that the site is for that
  country only and cannot target another
  ([crawling-indexing.md](crawling-indexing.md#international-and-multilingual-sites)).
- **Content length** — no minimum or maximum word count.
- **Subdomains vs subdirectories** — do what suits the business.
- **PageRank obsession** — links are one signal among many.
- **The "duplicate content penalty"** — doesn't exist for your own duplicates
  (copying others' content does).
- **Heading count and order** — semantic order helps screen readers; Google
  doesn't depend on it. No ideal number of headings.
- **E-E-A-T as a ranking factor** — it isn't one.
- **Artificial freshness** — changing dates or churning content doesn't help,
  and changing dates without substantial changes is a warning sign of
  search-engine-first content.
- **AI text files and AI markup** (`llms.txt` and the like) — Google says no
  new machine-readable files, AI text files or special schema.org markup are
  needed to appear in AI Overviews or AI Mode.

## Monitoring

- **Search Console:** verify ownership, check the Page Indexing report, submit
  the sitemap, watch the Performance report (queries, pages, countries). Use
  URL Inspection per page (live test, rendered HTML, request indexing).
  Also: Manual Actions, Removals (temporary, ~6 months), Change of Address,
  Security Issues, rich result reports, Core Web Vitals. Monthly checks plus
  after significant changes are enough; Google emails new issues.
- **Tools:** Rich Results Test, PageSpeed Insights, URL Inspection.
- **Measure changes:** compare before/after on stable pages over months
  ([how long to wait](#ground-truth)).
- **AI traffic:** AI Overviews and AI Mode are counted in the Performance
  report under the "Web" search type, not reported separately. ChatGPT search
  adds `utm_source=chatgpt.com` to the links it sends, so analytics can
  separate that traffic.

---

## Agent checklist — before shipping any page or template change

- [ ] Returns `200`; not blocked by robots.txt; no stray `noindex`.
- [ ] robots.txt doesn't block `OAI-SearchBot` or other search crawlers unless
      the owner chose to; any training opt-out was asked for.
- [ ] Main content, links and metadata present in the **server-rendered or
      prerendered HTML**, not only after JavaScript.
- [ ] Unique, descriptive `<title>`; unique meta description; one clear `<h1>`.
- [ ] Self-referencing absolute `rel="canonical"`, consistent with sitemap and
      internal links.
- [ ] Navigation uses `<a href>` with History-API URLs; no fragment routing.
- [ ] Descriptive anchor text; outbound paid/UGC/untrusted links qualified.
- [ ] Every meaningful `<img>` has an `src` and descriptive `alt`.
- [ ] Structured data describes only visible content, has required
      properties, and passes the Rich Results Test.
- [ ] Missing resources return a real `404` (or `noindex` in an SPA).
- [ ] New URL added to the sitemap (if the site has one) with an honest
      `<lastmod>`; removed URL redirected or `404`.
- [ ] Content: factually checked, original, dated honestly, author/process
      clear where readers would expect it; estimates labelled.
- [ ] Nothing from [spam policies](#spam-policies--never-do-these).
- [ ] Mobile-friendly, HTTPS, no intrusive interstitial.

## Sources

Google Search Central, `https://developers.google.com/search/docs/`:
`fundamentals/seo-starter-guide` · `essentials` · `essentials/technical` ·
`essentials/spam-policies` · `fundamentals/how-search-works` ·
`fundamentals/get-started` · `appearance/page-experience` ·
`appearance/ranking-systems-guide` · `appearance/ai-features` ·
`monitor-debug/search-console-start` (read 2026-09-22; `ai-features` read
2026-10-05).

OpenAI: `https://help.openai.com/en/articles/12627856-publishers-and-developers-faq`
(read 2026-10-05).

Google updates these pages; re-read them when this file is more than a year old.
