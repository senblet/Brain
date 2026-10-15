# SEO — content

What to write and how: helpful content, E-E-A-T, AI-generated content,
keyword research and choosing pages, ads and interstitials, links (including
earning them) and images.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

## Writing content

### What Google rewards
Easy to read and well organized (paragraphs, sections, headings, no spelling or
grammar errors); **unique** (not copied or lightly rewritten); **up to date**
(revise, or delete what is no longer relevant); **helpful, reliable and
people-first**.

Self-check before publishing. Does it:
- provide original information, research or analysis beyond the obvious?
- describe the topic substantially and completely?
- add real value if it draws on other sources, rather than rewriting them?
- have a title/main heading that summarises it without exaggeration or shock?
- leave the reader able to reach their goal without searching again?
- contain **no easily verified factual errors**?
- look carefully produced, not hasty or mass-produced?

### Warning signs of search-engine-first content (stop and rethink)
Made mainly to attract search visits; lots of topics hoping some rank; heavy
automation across many topics; mainly summarising others; chasing trends
outside the site's purpose; writing to a word count (**there is no preferred
word count**); entering a niche without expertise; promising answers that don't
exist (e.g. unconfirmed release dates); **changing dates to look fresh without
substantial changes**; adding or deleting content in bulk to seem "fresh"
(it doesn't help).

### E-E-A-T and YMYL
- Experience, Expertise, Authoritativeness, **Trust** (the most important).
  E-E-A-T is **not itself a ranking factor**, but systems favour content that
  shows it — especially on **YMYL** topics (health, finance, safety, societal
  welfare), where the bar is higher.
- Show first-hand experience and clear sourcing; cite and link sources.
- *(practitioner)* On YMYL sites, show the qualified person: author name,
  credentials and photo on each article; "reviewed by" with the reviewer's
  name and licence on medical content; a full bio page per professional
  (education, admissions or certifications, years in practice); citations
  to primary sources (laws, court rules, studies, regulators).

### Who / How / Why
- **Who:** make authorship self-evident. Bylines where readers expect them,
  leading to author or About pages with background. Don't invent authors or
  reviewers.
- **How:** explain how content was produced. If automation or AI substantially
  generated it, disclose that where a reader would reasonably wonder, with
  background on how and why it was used.
- **Why:** content must exist primarily to help people. Automation used
  primarily to manipulate rankings is spam.

### AI-generated content
- Allowed, but held to the same standards: **accuracy, quality, relevance** —
  including generated **titles, meta descriptions, structured data and alt
  text**.
- Generating many pages without adding value is **scaled content abuse**
  ([spam policies](overview.md#spam-policies--never-do-these)).
- **Agent rules for SEO work:**
  - MUST NOT invent figures, dates, quotes, studies, credentials, search
    volumes, difficulty scores, rankings or trends. Take numbers from a
    source the user can see (the product's own data, a cited study, Search
    Console, Trends, an export they provide); label anything else as an
    estimate, in the text. Given a field it can't know (a volume, a contact
    email, a Business Profile category), a model fills it with something
    plausible — supply the real list and let it answer "unknown".
  - *(practitioner)* An agent told to duplicate a page for new variants can
    silently drop the one original element (a quiz, a data table) — the
    thing that keeps the page out of scaled-content territory. After any
    duplication, diff for what is *missing*, not only what changed.
  - *(practitioner)* Once an agent publishes outside the CMS, plugins stop
    updating the sitemap. Put "update the sitemap and request indexing" in
    the process file the agent reads before every publish.
  - Deletes, redirects, `robots.txt` and canonical changes go through a
    human, or are blocked in code.
- E-commerce: AI images need IPTC `DigitalSourceType` =
  `TrainedAlgorithmicMedia`; AI product titles/descriptions must be labelled as
  AI-generated (Merchant Center policy).

### Keywords and keyword research
- Think about the words readers actually search — beginners and experts use
  different terms ("cheese board" vs "charcuterie") — and use them naturally in
  prominent places: title, main heading, alt text, link text.
- Don't chase every variation; Google's language matching understands synonyms
  and related concepts.
- **Research with real data**, in this order:
  1. **Search Console** Performance report, Queries tab: the terms the site
     already appears and gets clicks for. Search Console is the source of
     truth for Search performance.
  2. **Google Trends** Explore (up to 5 terms at once): which terms have high
     or rising interest, where they are popular, and the related topics and
     queries (Top and Rising). A rising term that is still little known may be
     less competitive.
  3. **Filter** to terms that fit the business and where the site has
     first-hand experience. Don't write about something only because it is
     trending (warning signs above).
  4. **Check each market separately.** Interest and seasonality differ by
     country; publish seasonal content a little before searches peak.
- Trends is a sample of searches showing interest over time, not exact
  volume; never present it as a search count.
- **One page per topic, not per keyword variant.** Substantially similar pages
  aimed at similar queries (one per city, one per synonym) are doorway abuse
  ([spam policies](overview.md#spam-policies--never-do-these)). Cover close
  variations on one page.

### Choosing what to write (practitioner method)
From SEO consultants running AI-assisted blogs (read 2026-10-12); consistent
with Google's guidance but not from it.

- **Read intent off the results page.** Search the keyword and look at what
  ranks: blog posts and a definition box mean informational; service,
  category and landing pages mean commercial. A young site SHOULD start on
  commercial, specific, low-volume queries ("[competitor] alternative",
  "[service] [suburb]") — the searcher already wants to buy, and the results
  page is thinner.
- **Think in patterns, not keywords.** A pattern is a set of queries with the
  same intent where one word changes ("X vs Y", "best X for [segment]",
  "[service] [city]"). One pattern is a plan for dozens of pages. Every
  variant MUST have something only that variant can say (local facts, prices,
  examples); otherwise it is the doorway pattern above.
- **Cannibalisation check before writing.** Search Console → Performance →
  filter on the exact query → Pages tab. A page already gets clicks: improve
  it. Impressions but few clicks: it is in the top 10, improve it. Nothing:
  create the page. Two pages on one query split the clicks and both lose.
- **Secondary keywords.** Take the page ranking first and list every other
  query that URL ranks for — Google already treats those as one page. Cover
  them on one URL, and let the title cover the main two.
- **Build what the top 3 almost build, plus one thing they don't have.**
  Read the top three: every section all three have, your page needs; what
  only one has, decide if it's worth it; then add one element none of them
  have — a calculator, your own data or numbers, real photos, a short quiz
  that routes the reader — using only what the business can genuinely
  show. Match the order in which the results answer the questions. This is
  the practical form of Google's "original information" self-check above.
  An agent drafting the page marks every fact it couldn't verify `[CHECK]`;
  a person clears every one before publishing.
- **Skip results pages you can't win yet.** If the top 10 are all big
  brands, mark the keyword "later" and pick one where sites your size
  rank.
- **Fix existing pages before publishing more**, in this order:
  1. **Repoint** pages to the queries Google already shows them for (Search
     Console, Pages → Queries). Rewrite the H1, meta description and first
     100 words around that query, then check the body actually answers it.
     Works for pages at positions ~5–15 (sources say 5 or 8 as the lower
     bound), where Google already finds the page relevant. At positions 1–3
     with falling clicks, an AI Overview is probably answering above you and
     a rewrite won't help. Leave any page edited in the last ~60 days alone
     — Google hasn't re-read it yet. A weekly check of the three pages with
     the most impressions in that band is enough.
  2. **Regroup** into topic clusters with a hub page and in-body links
     between members. Slow; compounds.
  3. **Conflict:** one consultant reports cutting 15–20% of zero-click pages
     (no clicks, negligible impressions over 90 days, nothing newer than 3
     months) and seeing traffic rise. Google says bulk deletion to look
     "fresh" doesn't help (warning signs above). The motive differs (quality
     vs freshness) and the evidence is one site. Prune only pages that are
     genuinely thin or wrong, never for the count.
- **Comparison and "best of" pages.** These are what AI search engines
  read for buying questions ([ai-search.md](ai-search.md)). One agency's
  structure *(practitioner; reported to get a client into AI Overviews in
  about six weeks — one case)*:
  1. Author byline (name, photo, profile link), published date, and an
     "updated" date only when the content really changed.
  2. Title and `<h1>`: "Best [category] in [year]: …". A short intro that
     names the top pick.
  3. Key takeaways (a few bullets), then what the category is and is not.
  4. **Methodology:** at least four objective, measurable criteria used to
     rank — this is what makes the list credible to readers and engines.
  5. The ranked list, one `<h3>` per option ("1. X, best for Y"), each with
     specific facts (price, ratings and review counts, results, customers
     served) and who it suits.
  6. A side-by-side comparison **as an HTML table, never an image**, and a
     table mapping options to use cases or industries.
  7. Evidence (case results with numbers), an FAQ of the questions buyers
     ask before deciding, short answers, then one call to action.
  Be honest about the rows where you lose — it is what makes the rest
  believable. **Conflict:** this source puts its own client first on its
  own list and reports being cited; another observed ChatGPT dropping
  self-ranked lists in favour of third-party ones
  ([ai-search.md](ai-search.md#how-ai-assistants-pick-sources-practitioner-observations)).
  The engines may differ (Google AI Overviews vs ChatGPT); being named on
  other people's lists remains the safer bet.
- **Hold a cadence.** Pick a publishing rate and keep it; a burst of 30 pages
  then silence looks like generated content. Practitioners cap a new site at
  roughly one page a day. The ranking effect of volatility itself is their
  guess, not documented.

### Ads and interstitials
- Ads must not become distracting or stop users from reading.
- **Avoid intrusive interstitials:** prefer small **banners** over full-page
  overlays; DON'T cover the whole page; DON'T redirect users to a separate page
  for consent or input. Legally mandatory gates (age, consent) are exempt, but
  overlay them on the content rather than redirecting.

## Links

- **Anchor text** must be descriptive, reasonably concise, and relevant to both
  pages. Read it out of context — if you can't tell where it goes, rewrite it.
  No "click here", "read more", or bare "website".
- No empty anchors. For image links, the `alt` text is the anchor text.
- Give links context (surrounding words matter); don't chain adjacent links.
- Don't cram keywords into anchors — that is keyword stuffing.
- **Internal links:** cross-reference related pages in context. There is no
  ideal number; if it feels like too many, it is.
- **External links:** link out when it helps, especially to cite sources — it
  builds trust. Qualify only when needed:
  - `rel="sponsored"` — paid or advertising links (`nofollow` also accepted);
  - `rel="ugc"` — user-generated links (comments, forums), added automatically;
  - `rel="nofollow"` — sources you don't trust or don't want associated with.
  Don't `nofollow` every external link. For links within your own site, use
  robots.txt `Disallow` instead.

### Earning links (practitioner method)
Google's position: links happen naturally, don't manufacture them, and
buying or exchanging links for ranking is spam
([overview.md](overview.md#spam-policies--never-do-these)). Within that, the
methods below are what link-building consultants report working (read
2026-10-12). Authority scores (DR, Authority Score, Trust Flow) are vendor
estimates, not Google; the scoreboard is Search Console clicks on queries that
matter, judged over months.

**Collect what is already yours, first.**
- **Lost links:** inbound links to pages that now 404. Restore the page or
  301 it to the real replacement — not the homepage, which risks a soft 404
  ([crawling-indexing.md](crawling-indexing.md)).
- **Unlinked mentions:** search `"brand" -site:yoursite` and ask writers to
  add the link so readers can check the source.
- **Link rot elsewhere:** pages in your niche still linking to dead sites;
  offer the page that replaces the dead one.
- **Vendors you pay:** SaaS companies publish customer stories and link to
  the business featured. Write one up with real screenshots and send it.

**Ask only where the ask is reasonable.**
- Sites already ranking where you want to be linked from; roundups that
  rank top 20 for a query you care about, updated in the last year, that
  already include a competitor. Pitch one specific reader need the list
  doesn't cover, with proof. If the publisher asks for money, it is a paid
  placement and MUST carry `rel="sponsored"`.
- **Give before asking:** a correction sheet for their page (old sentence,
  what changed, source, replacement sentence in their voice), reshot
  screenshots for an outdated tutorial, a diagram of a process they
  describe in text. Send it without a link request. **Every claim on it MUST
  be verified** — one wrong "correction" ends the relationship, and an agent
  will confidently write one it never checked.
- Pace outreach: a handful a day, from a separate sending domain, with one
  or two follow-ups. Volume kills the thing that makes it work.

**Make something citable.** A homepage is not. Your own data beats a free
tool (cloned in a week) beats an infographic. Profiles on authority domains
(one review platform, Reddit, YouTube, LinkedIn articles) rank where your
site can't.

**Trades.** A few swaps between businesses that belong together are an
editorial decision; a ring of reciprocal links is a footprint. Test: would
you include them if they had nothing to offer back?

**DON'T buy.** A paid link that passes ranking credit is a policy violation
on both sides; a compliant one carries `sponsored`/`nofollow` and passes
nothing. "€7 placements for AI citations" and "safe dofollow" are the same
violation with a nicer name.

**Anchor footprint** (practitioner observation): from other sites, anchors
are mostly the brand, the URL or plain words ("this study"). Exact-match
keyword anchors on most inbound links, a single TLD, zero `nofollow` links
and all-WordPress sources are what a built profile looks like. Roughly two
thirds of earned links disappear over time; plan for that.

## Images

- Embed with **`<img src>`** (inside `<picture>` is fine). **CSS background
  images are not indexed.** Always give `srcset`/`<picture>` a fallback `src`.
- Formats: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; the extension should match the
  type.
- **Alt text** on every meaningful image: short, descriptive, in context of the
  page ("Dalmatian puppy playing fetch", not "puppy" and never a keyword list).
  For inline SVG use `<title>`. It serves accessibility first.
- Sharp, high-quality images **near relevant text**, on relevant pages.
- Short descriptive filenames (`black-kitten.jpg`, not `IMG00023.JPG`);
  translate them when localising.
- Optimise for speed (images are usually the heaviest assets); responsive
  images; reference each image by one consistent URL.
- **Preferred preview image** via `og:image` or schema.org
  `primaryImageOfPage` / `image`: relevant and representative, **not a logo**,
  **no text in the image**, no extreme aspect ratio, high resolution.
- Image sitemaps may list images on other domains (CDNs).

## Sources

Google Search Central, `https://developers.google.com/search/docs/`:
`fundamentals/seo-starter-guide` · `fundamentals/creating-helpful-content` ·
`fundamentals/using-gen-ai-content` ·
`appearance/avoid-intrusive-interstitials` ·
`crawling-indexing/links-crawlable` · `crawling-indexing/qualify-outbound-links`
· `appearance/google-images` (read 2026-09-22).

Keyword research adds Google's Trends and Search Console pages (read
2026-10-06): `monitor-debug/trends-start` · `monitor-debug/search-console-start`
· `monitor-debug/google-analytics-search-console`.

Practitioner sections (choosing what to write, agent rules marked
*(practitioner)*, earning links),
read 2026-10-12 — vendor-affiliated, one-company evidence, kept where they
operationalise Google's guidance:
- Nicholas Dulait (ChatSEO), "How to use Claude Opus 5.5 for SEO",
  `https://x.com/nicholasdulait/status/2108212094214529135`, and "0 to 3,000
  organic visits a month", `https://x.com/NicholasDulait/status/2107767940971991254`.
- Borja (Distribb), "My Chief of SEO Backlinks",
  `https://x.com/borjafat/status/2106860317481525608`.
- Nicholas Dulait (ChatSEO), "Ultimate Claude Opus 5.5 Starter Pack For
  SEO", `https://x.com/nicholasdulait/status/2110275229108818335` (read
  2026-10-15) — reading the top three, `[CHECK]` markers, skipping
  big-brand results, the 5–15 band and the 60-day rule. Its on-page
  checklist repeats `overview.md` except "title under 60 characters" and
  "FAQ markup", both rejected ([appearance.md](appearance.md)).
- Rob Hoffman, "Best [product]" page structure,
  `https://x.com/RobHoffman_/status/2110083165306155141` (read 2026-10-14;
  agency post, one client case). Conversion-widget tips left out.
- BowTiedBills, "The Most Valuable SEO Article Ever Written",
  `https://x.com/bowtiedbills/status/2109881300890816850` (read 2026-10-14)
  — YMYL author and reviewer details.

Google updates these pages; re-read them when this file is more than a year old.
