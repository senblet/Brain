# Marketing — outbound

Cold outbound as a system: who to contact, in what order, how to get into the
inbox, what to write, how to handle replies, and how to test. Built for B2B,
and for tools like the studio's `scout` that automate parts of it. The rules
for agents that classify or draft at volume are in
[ai/agents.md](../ai/agents.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Sending
requirements come from Gmail's sender guidelines; reply-rate figures from
one vendor's dataset; everything else is practitioner method from agencies
that sell outbound (read 2026-10-12 and 2026-10-14). Their pipeline and
salary figures are left out.

**Not covered here:** the law. Rules on cold email and personal data differ
by country; check them before sending.

---

## Build in order

The system has layers: list → qualification → contact data → sending →
copy → replies → reporting. Build and verify one layer before the next.
When everything is built at once and the result is zero, you can't tell
which layer caused it. A broken sending setup reads in the reports as "the
copy failed".

## Who to contact

### The ICP, written down
- Start from **closed-won and closed-lost deals**: compare website content,
  open roles and tech stack on both sides. What separates them goes into the
  ideal customer profile (ICP). Add the buyers' own words from calls.
- A usable ICP names: the revenue floor, the function that owns the problem,
  the trigger that signals timing, and the **disqualifiers**. "50–200
  employees in SaaS" is too broad to qualify against.
- Also list: titles by tier, titles you never sell to, size, industries,
  geography, competitors, current customers.
- Keep it in a file, not a static spreadsheet; it changes as you learn.
  Review it every quarter against the last 90 days of results.

### The whole market
- No single database holds a market. Pull from several sources (people
  databases, maps listings for local and owner-run businesses, lookalike
  search from your best customers' websites).
- Merge and dedupe: by domain first, then company name plus region, then
  phone. Any single source's count is a floor for the market's size.

### Who goes first
- **Signals** — recent events that indicate timing: funding, hiring for the
  function you sell into, a new executive in the relevant seat, a pairing
  technology on their stack, headcount or location growth, visits to
  high-intent pages (pricing), engagement with your or a competitor's posts.
  Only recent ones count; re-score on a cycle — a year-old round says
  nothing about this quarter's budget. A signal is a reason to look closer,
  not proof of fit. Sources worth watching on a schedule: job feeds, company
  filings, funding announcements, executive moves, ad libraries.
- **Engagement with competitors** is a weaker signal: people liking a
  competitor's or its employees' posts have the category on their radar.
  Filter to the ICP; it is a better start than a bought list, not intent.
- **Pain segments.** Don't spray the whole market. Group accounts by the
  problem they share, give each segment its own offer, and write to that
  problem.
- **People you already reached** — past campaigns, old CRM leads, the
  newsletter — are the cheapest place to start. Re-engage them with a new
  angle (a launch is one).
- MUST suppress current customers, open deals and anyone already in a live
  campaign. Nobody gets two sequences at once.

## Qualify before you enrich

Order matters more than tools:

1. Source the list broad — every filter at the source removes accounts you
   would have qualified.
2. Read each company's **own website** (home, about, services, careers);
   vendor industry labels are noisy.
3. Summarise what the business actually does, then score it against the ICP
   with the disqualifiers written in. Check a sample by hand — a thin site
   misleads the model.
4. Cut everything below the threshold.
5. **Only then** pay for contacts. Enriching first spends credits on the
   half of the list you were always going to drop.

Then pick the decision maker by company size (practitioner rule of thumb:
owner or founder up to ~50 people; VP or director from ~50–500) and find
emails through a waterfall of providers, each seeing only the contacts the
previous one missed, so nobody is paid for twice.

## Land in the inbox

**Gmail's requirements** (documented):
- All senders: SPF **or** DKIM on the sending domain, TLS, and a spam rate in
  Postmaster Tools **below 0.3%** (Google recommends staying below 0.1%).
- Over 5,000 messages a day to Gmail: SPF **and** DKIM, **DMARC**, and
  one-click unsubscribe plus a visible unsubscribe link on marketing mail.

**Practitioner practice** on top:
- DON'T send cold email from the primary domain. Use secondary domains, so a
  flagged domain or inbox is swapped out without touching the main one.
- Verify every address twice, with two independent verifiers; the
  enrichment vendor's own check doesn't count. Valid → main campaign.
  Catch-all domains → only if the second verifier passes them, in their own
  campaign. Invalid, disposable, unknown → removed.
- Keep volume per inbox low (one agency caps at ~20 a day) and warm-up on
  permanently.
- Open tracking off; no link in the first email.

## The email

**Make it a gift, not a burden.** One offer per pain segment, in the words
buyers used on calls:
- open with a result you got for a company like theirs, in numbers they care
  about;
- offer something small you made for them (a sample list, an audit, a
  mockup) — send it as a reply once they say yes;
- one line on what you do and for whom.

Name a customer only if they agreed; otherwise describe them ("a dental
group in the Midwest").

**What moves reply rate** — Gong's analysis of 85 million cold emails, as
published by 30 Minutes to President's Club. **Correlations in one vendor's
dataset**, not experiments; defaults to test, not laws.

| Fewer replies | | More replies | |
|---|---|---|---|
| Buzzwords ("seamless", "best-in-class") | −57% | A breakup email ending the sequence | +89% |
| Case studies in a follow-up | −47% | Social proof | +41% |
| Asking for a meeting | −44% | Making an offer (free audit, trial, report) | +28% |
| The word "AI" | −36% | Restating the ask in a follow-up | +27% |
| Asking about their problem | −29% | Talking about their priorities | +20% |
| The word "platform" | −26% | "Thoughts?" as a follow-up | +9% |
| ROI claims | −17% | Asking if they're open to learning more | +7% |

Rules that follow (and agree with the gift approach):
- SHOULD lead with their priorities and a concrete offer; DON'T open with a
  meeting request or an ROI number.
- DON'T describe the product with buzzwords, "AI" or "platform" — say what
  it does.
- Follow-ups restate the ask; they don't attach case studies.

**Conflict:** sequence length and the breakup email. Gong's data associates a
breakup email with +89% replies. One outbound agency runs two emails in
total and no breakup email, without giving data. Test both; the Gong figure
is the better evidence but is correlational.

Keep each campaign to ~1,500–2,000 contacts so its result is readable.

Link-building outreach follows the same shape and adds "give something
verified first" — see [seo/content.md](../seo/content.md#earning-links-practitioner-method).

## Replies

- Replies from every channel land in one inbox, classified by intent:
  interested → a task for a named person in the CRM; referral → contact the
  person named; "not now" → a dated follow-up; opt-out → suppressed at once.
- Speed decides the outcome: the same replies produce no closes or several
  depending on how fast a human answers. Aim for **minutes**, and track
  time-to-first-response weekly — it degrades quietly as volume grows.
- An agent may draft replies from the company's context; a human approves
  them unless you have deliberately decided otherwise
  ([ai/agents.md](../ai/agents.md#guardrails-live-in-the-tools-not-the-prompt)).

## Measure and test weekly

- **Funnel maths:** reply → positive reply → meeting → show → close. Each
  ratio points at a different layer; a bad number tells you what to fix.
- Report reply, interested, meeting and pipeline **by segment and persona**.
  The aggregate reply rate is the least useful number — one or two segments
  carry everything and the average hides which.
- Every Monday, per campaign (practitioner thresholds): bounce rate over 3%
  → pause; around 2% → watch; no interested replies in two weeks → new
  angles.
- Each week, one segment gets several new versions; **each changes one
  thing** (subject, first line or offer). Review every version before it
  sends; winners feed the next offer.

## Where AI fits

AI does the volume: reading websites, grouping accounts, scoring, drafting.
A person with taste owns the ICP, the offer and the weekly call on what to
test — LLMs produce the average by default. "AI SDR" tools can run pieces of
this; they don't replace that judgement.

## Sources

- Gmail sender guidelines, `https://support.google.com/a/answer/81126`
  (read 2026-10-14).
- Nick Abraham, chart of Gong / 30MPC "The Ultimate Cold Email Data Report",
  `https://x.com/NickAbraham12/status/2107832346795769865` (read 2026-10-12).
  Original report not read.
- Roman (Gojiberry), competitor-engagement playbook,
  `https://x.com/romanbuildsaas/status/2107909606991081563` (read 2026-10-12).
- Christian (@coldemailchris, gtmu.io), "How To Master GTM Engineering (FULL
  COURSE)", `https://x.com/coldemailchris/status/2101014272021008735` (read
  2026-10-14) — build order, ICP definition, qualify-before-enrich, signals,
  reply speed, reporting by segment, prompts at volume. Sells a community.
- Adam Rahman (RevGrowth), "The Modern Outbound Playbook (FULL COURSE)",
  `https://x.com/AdamrahmanGTM/status/2109752466594287698` (read 2026-10-14)
  — ICP from closed deals, market mapping, pain segments, suppression,
  verification, the gift email, reply routing, weekly tests. Sells the
  service; vendor names left out.

Re-read when this file is more than a year old.
