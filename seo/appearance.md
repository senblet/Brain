# SEO — how pages look in results

What shows in a search result and how to influence it: title links,
snippets, other result elements, video features and structured data.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

## Result elements

### Title (`<title>`) — the title link
- **Every page MUST have a `<title>`.** Unique per page, descriptive, concise.
  No hard length limit; results truncate to device width.
- Avoid vague titles ("Home", "Profile"), **keyword stuffing**, repeated or
  boilerplate titles, and titles that vary by one token across many pages.
- Brand concisely: site name at start or end with a delimiter (`-`, `:`, `|`).
  A longer tagline fits the home page; repeated on every page it looks
  repetitive.
- Same **language and script** as the page's main content. Keep dates in titles
  current.
- Make the main title unambiguous: one clearly most prominent heading,
  typically the first visible `<h1>`.
- Google may rewrite the title link from `<h1>`, `og:title`, prominent text,
  anchor text or `WebSite` structured data when the `<title>` is half-empty,
  obsolete, inaccurate or boilerplate.
- *(practitioner)* Shape: the query + a reason to click + the brand (brand
  last unless it is well known). DON'T promise "free", a year or a number
  the page doesn't deliver.
- *(practitioner)* **Low click-through at positions 1–5:** change only the
  title and description, one page at a time, with the baseline recorded;
  judge after 3–4 weeks. If Google keeps rewriting the title, tighten it and
  align it with the `<h1>`.

### Meta description — the snippet
- Snippets come **mainly from page content**; the meta description is used when
  it describes the page better. No length limit.
- **Unique per page**, accurately summarising *this* page: site-level text only
  on the home page or aggregation pages. Prioritise key pages if you can't do
  all of them.
- Can hold structured facts (author, date, price, specs). Programmatic
  generation is fine for large sites if human-readable and varied.
- DON'T write keyword lists, one description for every page, or descriptions
  that don't summarise.
- Controls: `nosnippet`, `max-snippet:[n]`, `data-nosnippet` on elements.
- For "Read more" deep links: keep content visible (not collapsed in
  tabs/accordions), don't force scroll position on load, don't strip the URL
  hash.

### Other result elements
Favicon, site name, visible URL and breadcrumb, byline date, sitelinks,
text-result image, rich attributes. Most are automatic; favicon, site name
(`WebSite` structured data), breadcrumbs and article dates can be provided.

## Video

- Embed with `<video>`, `<embed>`, `<iframe>` or `<object>`; don't load by
  fragment or require user interaction to load it; JavaScript-injected players
  must appear in rendered HTML.
- Video features need a **dedicated watch page** (the video is the main
  purpose) with a unique title and description, an **indexed** page, a
  **valid thumbnail at a stable URL**, and a video not hidden behind other
  elements.
- Provide metadata (`VideoObject` structured data, video sitemap, or OGP);
  keep thumbnail and details identical across all sources. Allow Google to
  fetch the video file for previews and key moments.
- Remove an expired video with a `404` or `noindex` on its watch page, or a
  correct `expires` date.

## Structured data

- **JSON-LD recommended** (Microdata and RDFa also valid). Google's docs, not
  schema.org, define what Search uses.
- **MUST** describe **content visible on that page** — never content hidden
  from users, never on empty pages created to hold markup, never misleading
  (fake reviews, impersonation, misrepresenting ownership or purpose).
- Include **all required properties** for a feature; recommended ones only if
  complete and accurate (fewer correct beats many sloppy). Use the most
  specific types. Image URLs must be crawlable and indexable.
- Duplicate pages carry the same markup as their canonical. Link related items
  with `@id`; include the type that represents the page's main purpose.
- Don't block marked-up pages with robots.txt or `noindex`.
- **Check Google's search gallery before promising a rich result.** Valid
  schema.org markup isn't eligibility. Also retired: HowTo rich results
  (2023) and the sitelinks search box (`WebSite` `SearchAction`, 2024) —
  keep `WebSite` for the site name.
- Detect markup in the **rendered** page (Rich Results Test, URL Inspection);
  JSON-LD injected by JavaScript doesn't show in a raw fetch, so "no schema"
  from `curl` proves nothing.
- **FAQ markup: Skip.** Google limited FAQ rich results to well-known
  government and health sites in 2023 and stopped showing them entirely in
  2026. An FAQ section is still useful to readers; the markup earns nothing.
- **Review stars: DON'T mark up reviews of yourself.** A business that
  controls the reviews about itself — on its own site, in its markup or via
  an embedded widget — is ineligible for star snippets with `LocalBusiness`
  or `Organization` markup.
- **Markup enables a rich result; it never guarantees one.** Violations can
  bring a manual action that removes rich-result eligibility (ranking itself is
  unaffected).
- Validate with the **Rich Results Test** before release; watch Search
  Console's rich result reports after each deploy and template change.
- **Breadcrumbs** (`BreadcrumbList`): at least two `ListItem`s with `position`,
  `name`, `item` (the last may omit `item`). Represent a typical user path rather
  than mirroring the URL structure; the domain and the page itself may be
  omitted.
- **Organization**: on the home page or one About page, not every page. Use
  the most specific subtype (`OnlineStore`, a `LocalBusiness` type). No
  required properties; add those that apply — `name`, `alternateName`, `url`,
  `logo`, `address`, `telephone`, `sameAs` for official profiles. It helps
  Google tell the organization apart from others and pick the logo shown in
  results and the knowledge panel.

## Sources

Google Search Central, `https://developers.google.com/search/docs/` (read
2026-09-22):
`fundamentals/seo-starter-guide` · `appearance/title-link` ·
`appearance/snippet` · `appearance/visual-elements-gallery` · `appearance/video` ·
`appearance/structured-data/intro-structured-data` ·
`appearance/structured-data/sd-policies` ·
`appearance/structured-data/breadcrumb` ·
`appearance/structured-data/organization`. FAQ and review-snippet pages:
`appearance/structured-data/faqpage` · `appearance/structured-data/review-snippet`
(read 2026-10-14).

Title practice, retired features and rendered-markup checks:
`coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills`, shared via
`https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15) —
`schema`, `seo-audit/references/title-tags.md` and `rankings-push.md`. Its
title and description character limits are not adopted.

Google updates these pages; re-read them when this file is more than a year old.
