# SEO — crawling and indexing

How Google finds, fetches, renders and indexes pages, and how to control it:
robots.txt, `noindex`, sitemaps, canonicals, redirects, status codes,
JavaScript sites, URL structure and international sites.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

## Crawling and indexing controls

### Discovery
- Google finds pages mainly **through links** from pages it already knows.
  Every page you care about SHOULD be linked from at least one other page on
  the site.
- Check indexing with the `site:example.com` search operator or Search
  Console's URL Inspection tool before "fixing" anything.
- **Triage the Page Indexing report, don't panic at it.** *(practitioner)*
  Export "Why pages aren't indexed" and group the URLs by reason. Most of it
  is normal — redirects, pages you chose to exclude, duplicates pointing to
  their canonical. Only pages a customer should land on need a fix; check
  each by hand before changing anything.

### robots.txt vs `noindex` — they are not interchangeable
- **robots.txt controls crawling, not indexing.** A disallowed URL can still be
  indexed (without a description) if other pages link to it. DON'T use
  robots.txt to hide pages.
- **To keep a page out of Search:** use `<meta name="robots" content="noindex">`
  or the `X-Robots-Tag: noindex` HTTP header (for PDFs, images and other
  non-HTML files) — **and allow crawling**, or Google never sees the rule.
  Password-protect anything that is actually private. Deleting the content
  is the surest removal.
- `noindex` in robots.txt is **not supported**.
- Use robots.txt for: crawl-traffic management, duplicate/unimportant URLs,
  state-changing URLs (add to cart, post comment, create account), infinite
  spaces (search results, calendars, filter combinations), and keeping
  images/video/audio out of results.
- DON'T block resources Google needs to understand the page.
- Combining crawling and indexing rules can cancel them out — a `noindex` on a
  robots.txt-blocked page is never read.
- AI crawlers have their own tokens, and blocking the wrong one removes the
  site from AI search. See [ai-search.md](ai-search.md) before adding any
  AI-related robots.txt rule.

### Sitemaps
- **Optional for small sites.** Likely not needed if the site is ~500 pages or
  fewer that matter, is fully linked from the home page, and has little
  image/video/news content. Likely needed if the site is large, new with few
  external links, or media-heavy.
- If you have one: **UTF-8**, at the **site root**, **absolute URLs**, only
  **canonical URLs you want in results**, max **50,000 URLs / 50 MB**
  uncompressed per file (split with a sitemap index beyond that). URL order
  doesn't matter.
- Generate it from the same data the site renders from; hand-maintain only
  below a few dozen URLs.
- Google **ignores `<priority>` and `<changefreq>`**. It uses `<lastmod>` only
  when it is **consistently and verifiably accurate** — set it to the last
  *significant* change (main content, structured data, links), not a copyright
  year or build time.
- Submit via Search Console's Sitemaps report or a `Sitemap:` line in
  robots.txt. Submission is a hint, not a guarantee.
- Image, video and news sitemap extensions exist for media-heavy sites.

### Duplicates and canonicalization
- Duplicate content is **not a penalty** or spam; it wastes crawl and confuses
  users. Copying *other sites'* content is a different matter
  (see [spam policies](overview.md#spam-policies--never-do-these)).
- Aim for **one URL per piece of content**. Strongest to weakest signals:
  **redirect** → **`rel="canonical"`** → **sitemap inclusion**. They stack.
- `rel="canonical"`: in `<head>`, **absolute URL**, a **self-referencing
  canonical on the canonical page**, one method per page (don't mix header and
  element), same answer across every signal (sitemap, canonical, internal
  links). Link internally to the canonical URL.
- DON'T canonicalize with robots.txt, the URL removal tool, `noindex`, or a URL
  fragment.
- Google prefers **HTTPS** as canonical unless undermined by an invalid
  certificate, insecure dependencies, HTTPS→HTTP redirects, a canonical pointing
  to HTTP, or a certificate for the wrong host. Redirect HTTP→HTTPS; HSTS helps.
- Pick one host variant (`www` or apex) and 301 the others to it.

### Redirects
- **Permanent** (`301`, `308`, instant `meta refresh`): the target shows in
  results. **Temporary** (`302`, `303`, `307`, delayed `meta refresh`): the
  source keeps showing.
- Prefer **server-side** redirects. Use JavaScript `location` redirects only if
  nothing else is possible — they only work if rendering succeeds.
- Moving a page: `301` to its new home. Removed page: return a **real `404`**
  (a friendly 404 page is fine), never a `200` "not found" (a *soft 404*).
- Whole-site moves: redirects + updated sitemap + Search Console's Change of
  Address tool.

### HTTP status codes
- Use meaningful codes: `404` for pages that don't exist, `401` for pages
  behind a login, `301`/`308` for moved pages, `5xx` only for real server errors
  (`500`s tell Google to slow down).
- Pages that aren't `200` may skip rendering entirely.

## JavaScript sites and SPAs

Google renders JavaScript, but rendering is queued and can fail, and not every
bot runs JavaScript. **Server-side rendering or prerendering is still
recommended** — it is faster for users and crawlers alike.

- **Links MUST be `<a href="...">`** with a resolvable URL. Google does not
  reliably follow `onclick`, `routerLink` without `href`, `<span href>`, or
  `href="javascript:…"`. Injecting `<a href>` with JavaScript is fine.
- **Routing MUST use the History API**, not `#fragments`. Google ignores
  fragments; `example.com/#/products` is one URL.
- **Titles, meta descriptions and canonicals** may be set by JavaScript, but
  the canonical is best in the initial HTML, and JavaScript **must not change**
  it to a different value. If it can't be in the HTML, set it only in
  JavaScript. Exactly one canonical per page.
- **Don't ship `noindex` in the initial HTML of a page you want indexed** —
  Google may skip rendering on seeing it, so removing it with JavaScript may
  never be seen. Adding `noindex` via JavaScript (e.g. on an error state) works.
- **Soft 404s in SPAs:** for a missing resource, either redirect with
  JavaScript to a URL that returns a real `404`, or inject
  `<meta name="robots" content="noindex">`.
- **Cache-bust assets with content fingerprints** in filenames
  (`main.2bb85551.js`); Google's renderer may ignore caching headers and use
  stale files otherwise.
- **Web components:** Google indexes the flattened, rendered DOM — use `<slot>`
  so light-DOM content appears.
- **Lazy loading** must follow Google's lazy-loading guidelines so content
  appears without user interaction. **Infinite scroll** needs a paginated,
  linkable equivalent. Multi-page articles need crawlable next/previous links.
- JSON-LD may be injected by JavaScript — test it.
- **Verify with URL Inspection / Rich Results Test** that content, links,
  anchor text and structured data are in the *rendered* HTML.

## URLs and site structure

- **Descriptive, readable words**, in the audience's language:
  `/pets/cats` beats `/2/6772756D707920636174`. Parts of the URL can appear as
  breadcrumbs in results.
- **Hyphens** between words, not underscores or run-together words.
- **URLs are case-sensitive** — `/APPLE` and `/apple` are different URLs. If the
  server treats them the same, normalise to one case.
- **Percent-encode** reserved and non-ASCII characters in `href`s (IETF
  STD 66); use UTF-8.
- Parameters: `key=value` joined by `&`; multiple values with `,`. **Use as few
  parameters as possible**; drop ones that don't change content. No session IDs
  in URLs — use cookies.
- Avoid **infinite URL spaces**: additive filters, sort/referral parameters,
  endless calendars (`nofollow` future-date links), and parent-relative links
  that compound (`../../x`) — use **root-relative** links.
- **Group related pages in directories.** It matters most above a few thousand
  URLs (Google learns change frequency per directory). Don't reorganise a
  working small site just for this.
- Organize logically so users and crawlers can see how pages relate. Don't
  drop everything to restructure — Google understands most sites as they are.

## International and multilingual sites

- **One URL per language version** — not cookies or browser settings.
- Annotate language/region variants with **`hreflang`** (tags, headers or
  sitemap) and keep variants reciprocal. Use `rel="canonical"` + `hreflang` for
  same-language regional duplicates.
- **Don't auto-redirect by guessed language or IP**; link to the other versions
  and let users switch. Don't adapt content by IP — Google crawls mostly from
  the US and won't see the variants.
- Google detects language from **visible content**, not the `lang` attribute or
  URL. One language per page (content *and* navigation); no side-by-side
  translations.
- Geotargeting: ccTLD (`example.de`), subdomain (`de.example.com`) or
  subdirectory (`example.com/de/`); avoid URL parameters (`?loc=de`). Google
  ignores `geo.position` and similar meta tags. Some ccTLDs (`.io`, `.co`,
  `.me`, `.tv`, `.ai`…) and `.eu`/`.asia` are treated as generic.
- **A ccTLD is a strong signal and can only target one country.** A second
  language on a `.fr` or `.cl` still targets France or Chile; practitioners
  confirm it stays stuck there. If the site may serve other markets later,
  SHOULD use a generic TLD with subdirectories per market.

## Sources

Google Search Central, `https://developers.google.com/search/docs/` (read 2026-09-22):
`fundamentals/seo-starter-guide` · `crawling-indexing/sitemaps/overview` ·
`crawling-indexing/sitemaps/build-sitemap` ·
`crawling-indexing/control-what-you-share` · `crawling-indexing/robots/intro` ·
`crawling-indexing/block-indexing` · `crawling-indexing/canonicalization` ·
`crawling-indexing/consolidate-duplicate-urls` ·
`crawling-indexing/301-redirects` · `crawling-indexing/url-structure` ·
`crawling-indexing/links-crawlable` ·
`crawling-indexing/javascript/javascript-seo-basics` ·
`specialty/international/managing-multi-regional-sites` (ccTLD point re-read
2026-10-12; practitioner confirmation from Nicholas Dulait, ChatSEO,
`https://x.com/nicholasdulait/status/2108212094214529135`). Indexing-report
triage: Nicholas Dulait, "Ultimate Claude Opus 5.5 Starter Pack For SEO",
`https://x.com/nicholasdulait/status/2110275229108818335` (read 2026-10-15).

Google updates these pages; re-read them when this file is more than a year old.
