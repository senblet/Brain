# SEO — links

How to write links on your own pages, and how to earn links from other
sites without crossing Google's link-spam line.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

## Writing links

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

## Earning links (practitioner method)
Google's position: links happen naturally, don't manufacture them, and
buying or exchanging links for ranking is spam
([overview.md](overview.md#spam-policies--never-do-these)). Within that, the
methods below are what link-building consultants report working (read
2026-10-12 to 2026-10-15). Authority scores (DR, Authority Score, Trust Flow)
are vendor
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
site can't. A statistics roundup on your topic earned backlinks well out of
proportion in one vendor study (Foundation Inc., 2026, B2B SaaS); pair your
own research with one.

**Directories:** judge by real traffic, not authority scores. Verify a
listing's link by inspecting the actual `<a>` and its `rel` (there is no
"dofollow" attribute). DON'T use launch sites that list you in exchange for
a badge or a link back — a reciprocal-link footprint.

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

## Sources

Google Search Central, `https://developers.google.com/search/docs/`:
`crawling-indexing/links-crawlable` · `crawling-indexing/qualify-outbound-links`
· `essentials/spam-policies` (read 2026-09-22).

Earning links (practitioner, read 2026-10-12 — vendor-affiliated):
- Nicholas Dulait (ChatSEO), "How to use Claude Opus 5.5 for SEO",
  `https://x.com/nicholasdulait/status/2108212094214529135`.
- Borja (Distribb), "My Chief of SEO Backlinks",
  `https://x.com/borjafat/status/2106860317481525608`.

Directories and roundups: `coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills`, shared via
`https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15) —
`directory-submissions`,
`content-strategy` (which relays the Foundation Inc. statistics-roundup
study). Its badge-swap, press-release and bookmarking tiers are
not adopted (link spam).

Google updates these pages; re-read them when this file is more than a year old.
