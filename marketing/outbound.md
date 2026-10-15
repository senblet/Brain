# Marketing — outbound

Cold outbound as a system: the law and LinkedIn limits, the offer, who to
contact and in what order, how to get into the inbox, what to write, how to
handle replies, how to test, and selling the first customers. Built for B2B, and
for tools like the studio's `scout` that automate
parts of it. The rules for agents that classify or draft at volume are in
[ai/agents.md](../ai/agents.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Sending
requirements come from Gmail's sender guidelines; reply-rate figures from
one vendor's dataset; everything else is practitioner method from agencies
that sell outbound (read 2026-10-12 to 2026-10-15). Their pipeline, salary
and reply-rate claims are left out unless marked as theirs.

**The law — a baseline, not advice.** Rules differ by country; check the
ones that apply before sending. As summarised by one practitioner source
(verify each): every cold email carries a plain-text opt-out and a postal
address, and opt-outs are honoured within 10 business days (US CAN-SPAM);
for EU contacts, record the source, date and lawful basis, and tell them
where their data came from by the first message (GDPR Art. 14); don't
cold-email German contacts without consent, B2B included (UWG §7); UK sole
traders need consent (PECR). Chile and other markets: check before the
first campaign.

**DON'T automate LinkedIn.** Its User Agreement forbids bots or automated
methods to add contacts or send messages, scraping profiles and other data,
sharing an account or using someone else's, and false identities. Several
outbound sources rely on exactly these (scraped post engagers, automated
DMs, agencies running clients' profiles); the risk is the account — and
LinkedIn enforces it: it removed the company pages of several automation
and data vendors in 2025–26 and has sued scrapers (as reported in the
`marketingskills` repo). Work LinkedIn by hand from your own account, or
through LinkedIn's own products.

---

## Build in order, diagnose in order

The system has layers: offer → list → qualification → contact data →
sending → copy → replies → reporting. Build and verify one layer before the
next. When everything is built at once and the result is zero, you can't
tell which layer caused it. A broken sending setup reads in the reports as
"the copy failed".

When a campaign stalls, check in the same order — **the offer first, then
the list, copy last**. Rewriting messages that were never the problem is
the usual waste.

| Symptom | Layer to fix |
|---|---|
| Polite "no thanks" replies | The offer |
| "Not relevant" replies | The list — split by pain and rebuild one segment |
| Bounces past the stop-loss threshold | Contact data and verification; check SPF/DKIM/DMARC while paused |
| Nobody can say what's working | Reporting |

## The offer

A stranger has never heard of you; asking for 30 minutes is a big ask. The
offer makes yes easy. Three that work *(practitioner)*:

- **Free value up front:** an audit, a hand-picked list of their dream
  accounts, a small system built for them — useful on its own, with a natural
  next step to a call.
- **A case study from their industry:** what you did for a company just like
  theirs. One agency reports this as its highest-converting lead.
- **A guarantee** that removes the risk (e.g. another month free if the
  agreed number isn't met).

One agency changed only the offer — from "a call to discuss AI automation"
to "a free automation built for your business, demoed on the first call" —
and went from almost nothing to booked calls with the same list and copy
(their numbers).

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
- **One line per segment:** industry, size, team setup, and the one pain you
  can prove you solve. A job-title filter ("VP Sales at SaaS") says almost
  nothing about their problem.
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
  high-intent pages (pricing), engagement with your or a competitor's posts,
  a recent job change or promotion, recent activity on the channel you'll
  use (inactive people never see the message), event attendance, government
  contract or grant wins.
  Only recent ones count; re-score on a cycle — a year-old round says
  nothing about this quarter's budget. Freshness windows *(practitioner)*:
  pricing-page visit ~24 hours; funding 30–60 days; a new leader's first 90
  days; an open job post ~60 days; a champion's job change 30–90 days.
  Record the signal date on every lead. Strength, roughly: your own product
  usage → a past champion's job change → high-intent visits → engagement →
  hiring → funding → tech stack → third-party "intent" data; stack the weak
  ones before acting. A signal is a reason to look closer,
  not proof of fit. Sources worth watching on a schedule: job feeds, company
  filings, funding announcements, executive moves, ad libraries.
  **Keep the watcher dumb:** each signal feed only detects its event and
  writes it, with date and link, onto the account's row. Scoring and the
  decision to act live in one place the whole team can read.
- **Engagement with competitors** is a weaker signal: people liking a
  competitor's or its employees' posts have the category on their radar.
  Filter to the ICP; it is a better start than a bought list, not intent.
  On LinkedIn, collect it by hand — scraping engagers breaches its terms
  (above).
- **DON'T open with the signal** ("Congrats on the raise") or mention that
  you tracked their visit. Write the problem the signal implies.
- **Pain segments.** Don't spray the whole market. Group accounts by the
  problem they share, give each segment its own offer, and write to that
  problem. A segment is real when the value of solving the problem and the
  way to reach the people are both roughly the same across it — and when
  conversion jumps for that persona.
- **People you already reached** — past campaigns, old CRM leads, the
  newsletter — are the cheapest place to start. Re-engage them with a new
  angle (a launch is one).
- MUST suppress current customers, open deals and anyone already in a live
  campaign. Nobody gets two sequences at once — one suppression list keyed on
  email, LinkedIn URL and phone, synced to every sending tool, and one sender
  per account at a time (never a person and an agent together). For client work,
  each client
  also supplies a do-not-contact list (customers, competitors, churned
  accounts), matched on domain before every export.
- **Point ads and outbound at the same accounts,** so a prospect has seen a
  useful post before the first cold email.

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

Then pick two or three people per company — the decision maker plus one or
two around them. By size (practitioner rule of thumb): owner or founder up
to ~50 people; VP or director from ~50–500. Check the first batch of titles
by hand — advisors and former VPs carry the same titles — and check the
person still works there; a mailbox can stay live after someone leaves.

Find emails through a **waterfall** of providers: the next one runs only
when the previous returned nothing usable, so nobody is paid for twice. Keep
each provider's raw result in its own column and pick one final address;
unresolved or risky ones go on hold, not into the send. **Order the
providers by a bake-off:** take ~200 contacts you know are right, strip the
emails, score each provider on found, correct, wrong and cost per correct;
fewest wrong answers first. Repeat quarterly. Re-verify any address not
checked in the last week before it sends — B2B data decays about 2% a month
(vendor estimate).

## Land in the inbox

**Gmail's requirements** (documented):
- All senders: SPF **or** DKIM on the sending domain, TLS, and a spam rate in
  Postmaster Tools **below 0.3%** (Google recommends staying below 0.1%).
- Over 5,000 messages a day to Gmail: SPF **and** DKIM, **DMARC**, and
  one-click unsubscribe plus a visible unsubscribe link on marketing mail.

**Practitioner practice** on top:
- DON'T send cold email from the primary domain. Use spare domains — close
  variants of the main one, with SPF, DKIM and DMARC on each — so a flagged
  domain or inbox is swapped out without touching the main one. Up to ~3
  inboxes per domain, ~20–25 cold emails per inbox per day. Size from the
  volume: 300 a day ÷ 25 = 12 inboxes ÷ 3 = 4 domains.
- Verify every address twice, with two independent verifiers; the
  enrichment vendor's own check doesn't count. Valid → main campaign.
  Catch-all domains → only if the second verifier passes them, in their own
  campaign. Invalid, disposable, unknown → removed.
- **Warm up for 2–4 weeks before the first send** (sources differ) — buy
  the domains on day one — and keep warm-up on permanently. Microsoft
  mailboxes take fewer sends a day than Google ones.
- Keep 10–20% spare domains warmed and idle. DON'T use aliases of one
  mailbox as separate senders, or cheap resold workspace mailboxes (reported
  suspended en masse in 2025).
- **Stop-loss rules, set before launch** *(practitioner)*: bounce rate
  past 2–3% → pause (sources differ; one also lowers the sending tool's
  auto-pause from its 5% default to 2%); reply rate under ~1% after 300+
  sends → stop the campaign; inbox placement under ~70% → pull that mailbox;
  complaints near 0.1% → pause.
- **Choose the channel by account value.** Top-tier accounts (in the
  segment *and* with a live signal) get email plus a manual LinkedIn touch
  and a researched first line; the rest get email only.
- Open tracking off; no link in the first email.

## The email

**Short.** Two lines can be enough: what you did for a company like
theirs, with real numbers; then one yes-or-no question ("Worth it for
{company}?").

**Subject lines** *(vendor datasets: Gong, Lavender)*: 2–4 words,
lowercase, looking like an internal email; no product pitch; no first name
(−12% replies in one dataset — one LinkedIn agency reports the opposite for
InMail, a different channel).

**Relevance over personalisation.** Pasting someone's university into line
one does nothing; a message obviously about their business, role and
current problem does. Use the prospect's own words for the problem — their
website says it.

**Make it a gift, not a burden.** Each pain segment gets its own offer
([above](#the-offer)), written in the words buyers used on calls. A first
email that works:
- the result you got for a company like theirs, in numbers they care about;
- the free piece you made for them — sent as a reply once they say yes;
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
- Follow-ups restate the ask; they don't attach case studies (Gong's
  −47%). Some practitioner sequences put a case study in follow-up 2 or 3;
  the data says otherwise.

**Conflict:** sequence length and the breakup email. Gong's data associates a
breakup email with +89% replies. One outbound agency runs two emails in
total and no breakup email, without giving data. Test both; the Gong figure
is the better evidence but is correlational.

Keep each campaign to ~1,500–2,000 contacts so its result is readable.

**For services (the studio's own outbound) — the teardown play**
*(practitioner)*: email 1 names one specific thing on their site and asks
permission to send the rest, with no link; only after a yes, a 2–4 minute
video with three testable ideas. Around 50 accounts a week; an expert
reviews every teardown before it goes.

Link-building outreach follows the same shape and adds "give something
verified first" — see
[seo/links.md](../seo/links.md#earning-links-practitioner-method).

## Replies

- Replies from every channel land in one inbox, classified by intent:
  interested → a task for a named person in the CRM; referral → contact the
  person named; "not now" → a dated follow-up; opt-out → suppressed at once.
- **A reply on any channel stops every sequence for that lead.** Check the
  setting in each tool; a follow-up after a reply looks careless.
- Speed decides the outcome: the same replies produce no closes or several
  depending on how fast a human answers. One agency reports roughly 45% of
  interested leads booking when answered within 5 minutes, 25% after 30
  minutes, 10% after 2 hours and 3% the next day (their figures). Aim for
  **minutes**, and track time-to-first-response weekly — it degrades
  quietly as volume grows.
- *(practitioner)* A short qualifying phone call before booking — fit,
  objections — raises the share of booked calls that close.
- An agent may draft replies from the company's context; a human approves
  them ([ai/agents.md](../ai/agents.md#guardrails-live-in-the-tools-not-the-prompt)).
  Some practitioner setups let agents send low-tier first touches alone,
  within caps and an approved-claims list; this brain doesn't, until a
  deliberate decision says otherwise.

## Measure and test weekly

- **Funnel maths:** reply → positive reply → meeting → show → close. Each
  ratio points at a different layer; a bad number tells you what to fix.
- Report reply, interested, meeting and pipeline **by segment and persona**.
  The aggregate reply rate is the least useful number — one or two segments
  carry everything and the average hides which.
- Every Monday, per campaign: check the stop-loss rules
  ([above](#land-in-the-inbox)); no interested replies in two weeks → new
  angles *(practitioner)*.
- After every batch, file each angle — signal, persona, first line, replies
  — under "worked" or "went nowhere". The next campaign starts from what
  worked.
- Each week, one segment gets several new versions; **each changes one
  thing** (subject, first line or offer). Review every version before it
  sends; winners feed the next offer.

## First customers

**Sold by hand.** The founder sells the first 20–30, asks for money
explicitly, and personalises every message; scaled outbound comes after
(Pete Kazanjy, Jason Lemkin). Channel order for the first ones: personal
network → places buyers gather → cold outreach.

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
- Dra (Eaglerev), "our $1M cold outbound system… (FULL COURSE)",
  `https://x.com/draprints/status/2110208663608606775` (read 2026-10-15) —
  offer types, diagnose order, signals, short message, reply-speed figures,
  setter call. Sells a course; LinkedIn tactics that breach its terms
  (managed client profiles, automated DMs, search-limit workarounds) left
  out, as is message "spinning" to avoid detection.
- Alex Vacca (Frontal), "The Exact Tech Stack For Running an AI-Native GTM
  Agency", `https://x.com/itsalexvacca/status/2110415145587581023` (read
  2026-10-15) — segments, waterfall rules, inbox maths, warm-up, tiers by
  account value, dumb signal watchers, same-list ads, symptom → layer.
- `coreyhaines31/marketingskills` (MIT),
  `https://github.com/coreyhaines31/marketingskills`, shared via
  `https://x.com/chrissev/status/2110394539953606870` (read 2026-10-15) —
  `cold-email` (`references/deliverability.md`, `subject-lines.md`,
  `outbound-plays.md`), `prospecting` (`references/compliance.md`,
  `signal-plays.md`, `sourcing-and-enrichment.md`). Its LinkedIn automation
  options and case-study follow-ups are not adopted.
- `refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`
  (read 2026-10-15) — `founder-sales`, `first-b2b-customers`, `defining-icp`.
- LinkedIn User Agreement, `https://www.linkedin.com/legal/user-agreement`,
  §2.2 and §8.2 (read 2026-10-15).

Re-read when this file is more than a year old.
