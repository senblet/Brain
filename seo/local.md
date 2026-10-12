# SEO — local businesses

For a business that serves a city or area: how the map results work, the
Google Business Profile, the page the profile points to, and how to measure.
Everything in the other SEO files still applies to the website.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Items marked *(practitioner)* come
from local-SEO consultants, not Google, and are kept where they are
consistent with Google's guidance.

---

## How local results are ranked

Google documents three factors for the map results (the "local pack"):

- **Relevance** — how well the profile matches the search. Complete, detailed
  business information improves it.
- **Distance** — from the searcher to the business. Cannot be changed.
- **Prominence** — how well known the business is: links to it across the
  web, review count and ratings, and its position in web results. More
  reviews and positive ratings help; website SEO feeds this indirectly.

So the two levers are the profile's completeness (relevance) and reviews
plus links (prominence). *(practitioner)* Most competitors filled their
profile once and never returned; completeness alone moves a profile.

## The Business Profile

- **Name** MUST be the real-world name as on the storefront and website — no
  added keywords or city names.
- **Address / service area** accurate and precise. Phone: a local number the
  business controls, not a call-centre line.
- **Categories:** Google says **use as few as possible**, as specific as
  possible, representative of the core business; skip any category redundant
  with a more specific one chosen; don't add one per product or service.
  Categories come from Google's fixed list — never invent one. *(practitioner)*
  Agents hallucinate categories that don't exist; paste the real list (or
  the categories competitors use) and tell the model to choose only from it.
  Practitioners push for several categories; Google's wording wins — add a
  second or third only when each is genuinely a core line of business.
- **Services:** list each real service under the right category, with a short
  description. *(practitioner)* 20+ in a competitive city is common; only
  list what you actually do.
- **Description:** useful information on services, products, mission and
  history. No prices, promotions or links of any kind.
- **Photos, attributes, posts:** fill them. *(practitioner)* 20+ photos and a
  weekly post keep the profile active; AI can draft a month of posts at once
  from real news and services, a human checks and schedules them.
- **Questions:** post the questions customers ask on first contact, with
  short clear answers, yourself.

## Reviews

- Ask when the job is done; send the link, then one or two follow-ups a few
  days apart. *(practitioner)* Ask the customer to mention what was done and
  where — "fixed our water heater same day in Providencia" says more to
  Google and readers than "great service".
- Reply to every review within a couple of days: short, warm, no details of
  the customer's case (public, and for regulated professions possibly a
  confidentiality issue). Negative reviews: calm, short, general; the owner
  reads before posting.
- DON'T buy or script reviews.

## The page the profile links to

Usually the homepage for a single-location business. *(practitioner)*
checklist:

- `<title>` and `<h1>`: primary category + city ("Home" as the title is free
  ground left on the table).
- Secondary categories as `<h2>` sections.
- Address and phone **character-for-character** as on the profile; same on
  every directory listing (a citation audit: search the business name in
  quotes, list every listing, flag any differing detail, fix the prominent
  ones first).
- `LocalBusiness` (or a subtype) structured data with only the details
  given; validate it ([appearance.md](appearance.md)).
- A map embed of the profile and a widget showing the Google reviews.

## Site structure *(practitioner)*

- The site mirrors the profile: one page per category ("drain cleaning
  Santiago") and one per service ("water heater replacement Santiago"), each
  linked from inside a paragraph on the level above. Write them in order of
  real search demand.
- Neighbourhood or suburb pages only once the core pages rank, and each
  about the place (the housing, the common problems there, the route), not
  about you with the name swapped — that is doorway abuse
  ([content.md](content.md#keywords-and-keyword-research)).
- A young business SHOULD target the suburbs and specific services first
  ("emergency plumber [suburb]") rather than "[service] [big city]".

## Measuring *(practitioner)*

- A **rank grid** samples the profile's position from points across the city
  (13×13 is common). Reduce it to one number: the share of points in
  positions 1–3 ("top-3 %"). Position 4 is page two of the map.
- Re-run monthly and after changes. Compare against the 3–4 businesses that
  dominate; their top-3 % is the ceiling. Below roughly a quarter to half of
  it, build pages that answer customers' questions; at or above it, build
  outward into the weak zones.
- Leads from the profile show up within days; rankings take weeks. Don't
  judge in a week.

## Sources

Google Business Profile Help: `https://support.google.com/business/answer/7091`
(local ranking factors) · `.../answer/3038177` (guidelines for representing
your business) · `.../answer/7249669` (categories) — read 2026-10-12.

Practitioner method (read 2026-10-12): BowTiedBills, "The Complete Guide To
Using Claude In SEO", `https://x.com/BowTiedBills/status/2108032319114088824`
(local law firms; sells the service described); Nicholas Dulait (ChatSEO),
"How to use Claude Opus 5.5 for SEO", Module 10,
`https://x.com/nicholasdulait/status/2108212094214529135`. Numeric targets
(photo counts, service counts, thresholds) are theirs, not Google's.

Google updates these pages; re-read them when this file is more than a year old.
