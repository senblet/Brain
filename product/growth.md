# Product — activation and lifecycle

What happens after signup: defining activation, testing the first-use path
before launch, onboarding, upgrade prompts, lifecycle email and messaging,
cancellation and failed payments, and referrals. Signup forms and pages are in
[marketing/conversion.md](../marketing/conversion.md); what to measure and
how to test, there too.

**Tags:** as in the [README](../README.md#how-notes-are-written). Sources:
the `lenny-skills` and `marketingskills` repos (practitioner playbooks;
cited data marked), and Meta's WhatsApp rules as reported by
`marketingskills` — re-verify those against Meta before relying on them.

---

## Activation

- **SHOULD define activation as one user-level action that predicts
  retention** — users who reach it retain at least about twice as well as
  those who don't. Signup is too early, a repeat purchase too late,
  multi-step definitions too complex. Optional time bound: a median of 10
  days in Lenny's survey (mode 7).
- **Find it from data:** signup is time zero; compare actions in an early
  window with retention in a later one; use only fully observed cohorts;
  treat the correlation as a hypothesis until pushing the action is shown to
  raise retention (method from Amplitude's documentation).
- Benchmarks (Lenny's survey, 500+ responses): average activation 34%,
  median 25%; SaaS 36% / 30%.

## Before launch: simulated first users

Real users don't say why they left; simulated ones can show where they would
have. Before a launch, or after a big change to the first-use path:

- **Send several agent "first users" through the real app in a browser**,
  each from the landing page to the first success (the activation event),
  screenshotting every moment they get confused, stuck or annoyed. Personas
  that cover different failures: the impatient one (skims, clicks the first
  button, quits at the first error); the sceptic (reads pricing, terms and
  privacy first); the mobile user (375 px, slow connection); the
  non-native speaker (follows only what the interface literally says); the
  breaker (junk in forms, back mid-flow, double clicks).
- **Merge into one list ranked by how many personas hit each problem**,
  fix, then **rerun the same personas** to prove the fixes — the rerun is
  the verify gate.
- Each persona runs in its own context; the merge only sees their reports
  ([ai/agent-workflows.md](../ai/agent-workflows.md#topologies)).
- This finds friction and bugs, not demand. It doesn't replace activation
  and retention data from real users.
- In this setup the pattern is packaged as the `launch-qa` skill
  (personas, merge, fix, rerun).

## Onboarding

- **Value within the first 30 seconds, no tour first.** On mobile, every
  tap is a cost.
- List every step from signup to first value; cut, defer or pre-fill
  anything not required.
- Replace blank screens with a guided first piece of real work, and push the
  one core action during signup.
- **Empty states** explain the area, show an example and offer one action.
  Checklists have 3–7 items, value first, dismissible. Tours, if any, are
  3–5 steps and skippable.
- The product should get better the more it's used, so leaving costs
  something.

## Upgrade prompts

- Show them after the "aha" moment, at a real limit or a paid feature —
  never during onboarding or mid-task.
- Always offer "continue free", and wait days after a dismissal before
  asking again.
- Warn 7, 3 and 1 days before a trial ends.

## Lifecycle email and messaging

- Every automated sequence states its **trigger, goal and exit conditions**
  (converted, replied, unsubscribed). One job and one call to action per
  email; email reinforces what happens in the product rather than repeating
  it.
- Welcome immediately; nudges for incomplete setup at about 24 h and 72 h.
- Judge sequences on clicks and conversions, not opens — open rates are
  inflated by mail privacy features.

**WhatsApp** (for products that message users there, like `music-home`) —
as reported from Meta's documentation, October 2026; re-verify:
- Free-form messages only within 24 hours of the user's last message;
  otherwise an approved template. Reminders, and anything that mixes in a
  promotion, count as marketing. Billing is per message.
- **MUST:** opt-in names the business and WhatsApp and is unticked by
  default; separate opt-ins for updates and for offers; every marketing
  template carries a stop button. Blocks lower the number's quality rating
  and its sending limit.

## Cancellation and failed payments

- **Cancel flow:** one question with 5–8 reasons → one offer matched to the
  reason (pause, downgrade, help) → clear confirmation. "Continue
  cancelling" is always visible, and cancellation goes through even if the
  save step fails. DON'T use pressure ("this offer expires when you leave").
- **Failed payments:** retry soft declines over 7–10 days, never hard
  declines; dunning emails on days 0, 3, 7 and 10 with a direct card-update
  link; card-expiry reminders; use the billing provider's own retries.

## Referrals and reviews

- Build a referral programme only when most growth is already word of
  mouth, the user base is large (expect under 10% of users to refer
  successfully), the reward matters and users know other potential users.
- Ask, and reward, at the aha moment or a milestone, not at signup; reward
  both sides; one-click sharing with a pre-written message. Products with
  public output (a producer's page) can carry a "made with" link.
- **DON'T ask only happy customers for reviews** (e.g. only high NPS
  scorers) and don't pay for reviews on Google or Trustpilot — invite every
  real customer, neutrally (platform policies).

## Sources

Simulated first users: RoundtableSpace, launch-QA prompt,
`https://x.com/roundtablespace/status/2111717667228770611` (read
2026-10-23).

`refoundai/lenny-skills` (MIT), `https://github.com/refoundai/lenny-skills`,
shared via `https://x.com/chrissev/status/2110394539953606870` (read
2026-10-15): `user-onboarding-activation` (Lenny's activation survey),
`retention-engagement`, `referrals-word-of-mouth`.

`coreyhaines31/marketingskills` (MIT),
`https://github.com/coreyhaines31/marketingskills` (read 2026-10-15):
`onboarding` (activation method citing Amplitude), `paywalls`, `emails`,
`sms/references/whatsapp.md` (Meta rules), `churn-prevention`, `referrals`
(and `references/review-platform-rules.md`). Uncited benchmarks in these
skills are left out.

Re-read when this file is more than a year old.
