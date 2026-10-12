# SEO — content

What to write and how: helpful content, E-E-A-T, AI-generated content,
keyword research, ads and interstitials, links and images.

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
- **Agent rule:** never invent figures, dates, quotes, studies or credentials.
  Take numbers from a verifiable source (the product's own data, a cited
  study). If something is an estimate, say so in the text.
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
- **Agent rule:** never invent search volumes, difficulty scores, rankings or
  trends. Use data the user can see (Search Console, Trends, or an export
  they provide) and label anything else as an estimate. Trends is a sample of
  searches showing interest over time, not exact volume.
- **One page per topic, not per keyword variant.** Substantially similar pages
  aimed at similar queries (one per city, one per synonym) are doorway abuse
  ([spam policies](overview.md#spam-policies--never-do-these)). Cover close
  variations on one page.

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

Google updates these pages; re-read them when this file is more than a year old.
