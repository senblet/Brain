# Product — strategy

Deciding what to build and whether it's working: validating an idea,
product-market fit, retention, pricing, and the metric a product is run by. For
activation, onboarding and lifecycle, see
[growth.md](growth.md); for marketplaces, [marketplaces.md](marketplaces.md);
for pricing *pages* and experiments,
[marketing/conversion.md](../marketing/conversion.md);
for customer interviews and research,
[marketing/research.md](../marketing/research.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Mostly
experienced-operator advice collected from Lenny's Podcast and newsletter
(via the `lenny-skills` repo), plus some survey data and benchmarks — each
number says whose it is. Opinion is not evidence; benchmarks are
directional.

---

## Validating an idea

- **Trust cold signals.** Enthusiasm from friends, investors and warm
  introductions means little; cold outreach response is the cleanest test of
  an idea or a customer profile. (That is for *validating*; to *sell* the
  first customers, start with your network —
  [marketing/outbound.md](../marketing/outbound.md#first-customers).)
- **Look for pull, not praise.** Real signals: people with no tie to you pay
  or offer to; strong emotion (hatred of the current option); cold inbound;
  people keep using a bad prototype. "That's cool, I might buy it" means no.
- **Try to get paid before building.** Send an invoice for early access, or
  deliver the service by hand first (Vanta wrote reports manually until
  people asked to hire them).
- Build only if it visibly shrinks the user's workflow or gives them a
  "superpower" — same time, twice the output (Oji Udezue).
- Name the **why now**: the specific shift in technology, regulation or
  behaviour that makes this possible today (Mike Maples Jr).
- Love-it-or-hate-it reactions beat polite liking; lukewarm means
  incremental (Sam Schillace).

## Product-market fit

- **The survey.** Once you have 100+ active users you can reach, ask "How
  would you feel if you could no longer use this?" — **40% "very
  disappointed"** is the usual threshold (Sean Ellis's number, described as
  directional). Add: how it compares to alternatives, and "last time you did
  X, what did you use and why?"
- **Build for the "very disappointed" segment** and deliberately ignore most
  other early feedback (Rahul Vohra).
- **Cohort retention is the test:** plot monthly cohorts; fit for a segment
  means the curve flattens above zero. DON'T add spend or people before it
  flattens.
- Fit shows when prospects stop asking polite questions and start asking
  about price and start dates.

**Retention benchmarks** — 6-month user retention, good / great (Lenny's
"What is good retention"):

| Type | Good | Great |
|---|---|---|
| Consumer social | ~25% | ~45% |
| Consumer transactional | ~30% | ~50% |
| Consumer subscription | ~40% | ~70% |
| SMB SaaS | ~60% | ~80% |
| Enterprise SaaS | ~70% | ~90% |

**Monthly churn**, good / great: B2C SaaS 3–5% / under 2%; SMB SaaS under
$1k a month 2.5–5% / under 1.5%; enterprise 1–2% / under 0.5%. Lower bars are
fine with low acquisition cost, low cost to serve, or a business that isn't
chasing venture scale. Churn caps how large a business can get; more
acquisition doesn't lift the cap (Jason Cohen).

- Report failed-payment churn apart from cancellations; never mix free and
  paid users in one retention number.

## Pricing

- **Charge sooner and more than feels comfortable**; keep the first pricing
  simple; revisit every 6–12 months (Lenny's interviews with 20+ founders).
- **The value metric first, the number second** — charge on what grows with
  the customer's value (per seat only if value grows with headcount). Never
  gate the feature that delivers the core value.
- **The first price is a bet to learn from.** Settle the order of magnitude
  — roughly $10, $100 or $1,000 a month for individuals, small businesses or
  mid-market — round and slightly high. DON'T start ultra-low.
- **Free plans:** freemium is an acquisition tool, not a pricing strategy.
  Choose a trial instead when the product needs hand-holding, complex setup,
  several decision-makers, a human to convert, or has a high price. Skip
  freemium unless you have a large audience, minutes-to-value, low cost to
  serve and free users who bring others (Bobby Pinero). Most freemium SaaS
  also offers a 7–30 day trial of paid (~90% of ~50 products, Lenny).
- **Card up front?** Decide on visitor-to-paid, not trial-to-paid: card-required
  trials convert far better per trial but get fewer trials (ChartMogul 2026,
  200 B2B products — observational).
- **Discounts:** don't discount to win new customers; discount for upgrades
  or real seasonal windows. Keep any discount modest — one source puts the
  line at 20% and links bigger discounts to churn (its data, not shown). Frame
  annual savings as months free. Show local currency.
- **Price rises:** test on new signups first; move existing customers in
  waves; give months of notice and an option (lock in annual);
  grandfathering is a transition, not forever.
- DON'T trust stated willingness-to-pay surveys on their own — hypothetical
  answers run high. A survey (Van Westendorp) gives an acceptable range, not
  demand; confirm with real prices.
- Price endings (.99) are inconclusive for software; don't bother.

## The metric the product is run by

- **One north star** that counts a value action (bookings, completed
  workouts, reports read), moved through input metrics a quarter's work can
  change, paired with a quality guardrail (Airbnb Experiences used review
  rate). Don't make revenue or retention a team goal — they are outcomes.
- **Activation** is defined from data — see [growth.md](growth.md#activation).
- Size an idea's impact as **lift × share of users who see the flow**
  (Duolingo).
- Whether and how to test changes:
  [marketing/conversion.md](../marketing/conversion.md#experiments).

## Sources

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15): `defining-icp`, `idea-validation`, `evaluating-startup-ideas`,
`measuring-pmf`,
`retention-engagement`, `pricing-strategy`, `north-star-metrics`,
`growth-experimentation` — SKILL.md and `references/artifacts.md`. Guests are
named where the skill attributes them; several sell what they advise on.

`coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills` (read 2026-10-15):
`pricing` (value metric, first price, price rises), `offers` (discounts),
`onboarding/references/activation-models.md` (ChartMogul trial data).

Re-read when this file is more than a year old.
