# Product — marketplaces

For two-sided products — buyers and sellers, clients and providers, like
`auralyx-platform` and `music-home`: which side to build first, how to
launch, the metrics that matter, take rates, leakage and trust. General
product rules are in [strategy.md](strategy.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). From Lenny's
research on marketplaces (17 successful marketplaces; 35+ take rates) and
operators on his podcast, via the `lenny-skills` repo. Small samples; treat
numbers as directional.

---

## Getting started

- **Give one side value on its own first** ("single-player mode"). OpenTable
  sold restaurants software to run the restaurant; online bookings were a
  small part of the pitch.
- **Supply first by default** — 14 of the 17 successful marketplaces grew
  supply first. Demand first only when supply is trivial to get or is public
  data. If neither side depends on the other, it may be a platform, not a
  marketplace.
- **Launch narrow:** one city for in-person services, one category for
  everything else.
- **Pick two or three ways to grow supply and go deep.** Across the 17, the
  median was two; direct sales was the most common (~60%), then referrals and
  recruiting from an existing network (~33% each).
- **Seed supply by hand at the quality bar you want.** Behance interviewed
  100 creatives it admired and built their portfolios for them.
- Referral rewards are paid only after the referred user activates (first
  sale, first booking); referrals often work best on the supply side.

## Metrics

- DON'T say "liquidity" — measure it:
  - **Fill rate:** the share of sessions with real intent (define the
    signal, e.g. a search with dates) that end in a transaction. It ranges
    from under 5% to over 80% across businesses, so track your own trend,
    not a benchmark.
  - **Time to match.**
- Count **activated supply** (first sale or booking), not sign-ups, and
  time-to-activation.
- The core four: fill rate, bookings (the north star), activated supply,
  GMV (transactions × average order value). Add month 1/3/6 retention for
  buyers and for suppliers separately.
- **True buyer acquisition cost** = buyer CAC + supplier CAC × suppliers
  needed per buyer (Dan Hockenmaier).

## Take rate

- Take rate ≈ convenience + demand you bring − competition.
- **Starting points:** ~10% for a platform that provides tools; ~20% for a
  marketplace that brings demand; adjust from there. Observed ranges:
  platforms 5–15%, marketplaces 10–50% (e.g. Gumroad 8.5%, Etsy ~8%, Airbnb
  15%).
- To charge less on transactions, add a subscription (Shopify, Gumroad).
  A zero-commission model, like `auralyx-platform`'s, lives on the
  subscription.
- DON'T raise the take rate before you can prove you bring demand.
- Change fees and incentives lightly and watch for months — effects show
  late, and every change creates winners and losers.

## Leakage and trust

- **Leakage** — deals moving off the platform — is contained by convenience
  (doing it on-platform is easier), obfuscation (hiding direct contact until
  a booking) and protection (payments, disputes, guarantees). A handoff to
  WhatsApp, as in `music-home`'s MVP, leaks by design; measure the tracked
  intent and decide consciously when to close the gap.
- **Trust:** reviews beyond stars, verified supply, a look of quality
  (Airbnb paid for professional photos), guarantees.
- **Protect new sellers from one early bad review** — hide ratings until
  there are several, or blend them with a prior. One negative review cost
  new eBay sellers 8% of revenue (cited in the source).

## Sources

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15): `marketplace-fundamentals`, `supply-demand-balance`,
`marketplace-liquidity-take-rates`, `referrals-word-of-mouth` — SKILL.md and
`references/artifacts.md` (Lenny's newsletter research; Ramesh Johari, Dan
Hockenmaier, Scott Belsky, Matt Bendett).

Re-read when this file is more than a year old.
