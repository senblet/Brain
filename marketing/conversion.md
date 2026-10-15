# Marketing — conversion and measurement

Turning visits into signups and sales, and knowing what worked: page and
form rules, popups, pricing pages, experiments, and analytics. What happens
after signup is in [product/growth.md](../product/growth.md); page speed in
[development/web-performance.md](../development/web-performance.md); visual
design in [design/frontend.md](../design/frontend.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Mostly
practitioner playbooks from the `marketingskills` repo; the statistics
rules follow the American Statistical Association's statement on p-values
(as relayed by its `ab-testing` skill) and Ronny Kohavi's experiment work.
Uncited benchmarks are left out.

---

## Pages

- Review a page in order of impact: value proposition → headline → call to
  action → hierarchy → trust → objections → friction.
- A paid landing page matches the ad's message and has one call to action;
  consider removing the navigation.
- Button labels: [design/frontend.md](../design/frontend.md#copy-on-the-page).
- **Prices in HTML text** — not an image, a PDF or script-only rendering —
  so people, search engines and AI assistants can read them.

## Forms and signup

- For every field ask: needed before they can use the product? Defer
  company, role and phone to onboarding; infer the company from the email
  domain.
- **MUST:** visible labels above inputs (placeholders only as examples;
  never the label), errors below; paste allowed; correct input types and
  autofill; placeholder, helper and focus colours pass AA contrast.
- SHOULD: one email field, no "confirm email"; password rules shown up
  front; validate on blur; never clear the form on error; focus the first
  error.
- Three fields or fewer: one step. More: steps with a progress bar, easy
  questions first, back navigation, progress kept on refresh.
- Offer Google sign-in (plus Apple for consumer products) or a magic link;
  let people explore before verifying their email.
- **MUST:** account creation never depends on an enrichment lookup
  succeeding — a timeout must not become a silent rejection.
- Measure form start rate, completion, drop-off and errors by field, mobile
  vs desktop.
- **MUST fire the conversion on the confirmed submission**, not the button
  click. At launch, submit every form once and check it arrives; test pages
  in in-app browsers (Instagram, LinkedIn).

## Popups

Within Google's rule against intrusive interstitials
([seo/content.md](../seo/content.md#ads-and-interstitials)):
- Prefer what the user opens (click-triggered), slide-ins and bars. Never
  full-screen on mobile.
- At most once per session; remember a dismissal for 7–30 days; never show
  to people who already converted or during checkout.
- Closes with Esc and a visible ×, works by keyboard, traps focus while
  open; the decline link is neutral ("No thanks").
- DON'T: timed or exit-intent full-screen modals, countdown timers,
  guilt-trip decline links.

## Pricing pages

- Three tiers by default (five or more stalls the decision); mark the
  recommended one; say who each tier is for; a monthly/annual toggle; an FAQ;
  a guarantee near the call to action.
- State each tier's limits in words, and show at least a starting price
  rather than "Contact us" everywhere.
- **Scarcity only when real** — a cohort date, real capacity, a founding
  price that actually rises. A countdown ends on a real date.
- DON'T pre-select paid options or pre-tick consent, show a decoy tier, or
  lead with an inflated anchor price to manipulate.
- How to set the prices themselves:
  [product/strategy.md](../product/strategy.md#pricing).

## Experiments

- **MUST** fix the sample size and the stopping rule before launch, and not
  stop on a peek at a live p-value. Use a calculator (e.g. Evan Miller's),
  not rule-of-thumb tables.
- Run at least a full week (two business cycles for B2B), at most about 4–8
  weeks.
- One primary metric plus guardrails (refunds, support tickets). Report the
  effect size and its confidence interval, not only p. Segment findings you
  didn't plan are exploratory.
- Check the traffic split matches the plan (sample ratio mismatch); treat a
  result that looks too good as a bug until it replicates. Most tests fail —
  ~85% at Bing, 92% at Airbnb (Kohavi).
- **Skip A/B tests at low traffic.** If a test would need more than about
  60 days, raise the minimum effect worth detecting, test earlier in the
  funnel, or decide from qualitative evidence. Example (computed): a 3%
  conversion rate needs roughly 14,000 visitors per arm to detect a 20%
  relative lift at 80% power — most studio sites can't, so they ship
  low-risk changes and test only big ones.
- Hypothesis format: "Because [observation], we believe [change] will cause
  [outcome] for [audience]; we'll know when [metric]." Log every test with
  its sample, result, interval and the lesson.

## Measurement

- **A tracking plan before code.** Every event serves a decision. Names are
  `object_action` in snake_case (`signup_completed`), context in properties;
  keep GA4's built-in names where they exist (`sign_up`, `begin_checkout`,
  `purchase`).
- **MUST NOT put personal data in event properties.** Where consent is
  required, analytics waits for it (Consent Mode with its current
  parameters).
- Filter internal traffic; raise GA4 data retention from the 2-month default
  to 14 months.
- A rate divides a numerator and denominator over the same closed window;
  cohorts still inside their window are pending, not failed.
- **One source of truth for conversions** (the backend or CRM); never add
  up what each ad platform reports.
- Ask "How did you first hear about us?" at conversion (pick-list plus free
  text, including an AI-assistant option) to cross-check attribution, not to
  assign credit.
- Exclude sign-in and checkout referrers (`accounts.google.com`,
  `checkout.stripe.com`) and your own subdomains from referral reports; the
  marketing site and the app share one analytics property; identify the user
  at signup.
- Skip media-mix modelling and data-driven attribution at low volume.
- Campaign IDs across ads, email and CRM:
  [agents.md](agents.md#data-and-measurement).

## Sources

`coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills`, shared via
`https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15): `cro`
(and `references/form.md`), `signup`, `popups`, `pricing`
(`references/pricing-page-teardown.md`, adapted from Kyle Poyar), `offers`
(`references/scarcity-urgency.md`), `ab-testing`, `analytics`, `attribution`,
`launch/references/site-launch-qa.md`. Its popup timing, "psychology" tactics
(pre-selection, decoys, loss framing) and outdated analytics snippets are
not adopted.

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`
(read 2026-10-15): `product-experiments` (Ronny Kohavi; when not to test).

Re-read when this file is more than a year old.
