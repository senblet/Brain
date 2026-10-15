# Design — frontend

Rules for public pages that look decided rather than generated: process,
copy on the page, type, colour, layout, imagery, motion, states, the tells
of AI-made pages, and how to critique. Written for pages agents help build.
For speed, see
[development/web-performance.md](../development/web-performance.md).

**Tags:** as in the [README](../README.md#how-notes-are-written). Evidence is
marked per rule: **[standard]** matches WCAG, MDN or platform guidance;
**[study]** comes from one designer's survey of 247 award-gallery sites,
scored by a panel of AI models, not people — it measures fashion as much as
quality; everything else is practitioner taste. The same author's blind
tests scored his own skill *below* a no-skill baseline in four of five
rounds, so treat this as a checklist of good habits, not a proven method.

**Scope:** marketing and content pages. Product UI (dashboards, app screens)
keeps its lines, icons and labels — several rules below would hurt it.

---

## Process

- **Claims before sections.** List what the page must prove, one claim per
  section, each with its proof. Delete sections with no claim. This replaces
  the stock hero → logos → features → testimonial → pricing → CTA.
- **Find what only this client has.** List 8–12 specifics — name, street,
  numbers, constraints, materials, rituals, printed artefacts — and build the
  page idea from one. Test: if the idea still works with the nearest
  competitor's name on it, it is a category idea, not this client's.
- **Don't ask an agent to invent a look** — it returns the category default.
  Give it two or three concrete directions to choose from and have it say in
  one line why it chose one.
- Tell the agent which imagery really exists (own photos, real UI, nothing)
  before it plans the layout.
- **Write the whole copy deck as plain text before markup**, every section
  complete (the full menu, every room, every price). Thin sections were the
  commonest reason a clean page lost. Missing facts are `TBD`, never invented
  — sample content, if used to judge density, is marked as sample and
  replaced before launch.

## Copy on the page

- **The first screen says what this is**, in large type — for an event what,
  when and where; for a product what it is and what it does or costs — with
  one primary action as a real button. [study: missing on ~12 of 54 weak
  sites]
- Headlines fit in two lines at 390, 768 and 1440 px; a hero has roughly 32
  characters (characters per line ≈ width ÷ (font size × 0.5)). Cut words
  first, widen the measure second, shrink the type last. [study: gallery
  median 5 words]
- A large intro or quote is a paragraph or blockquote of ≤ ~25 words — set
  bigger, it reads as a second headline.
- **Buttons:** one to three words naming the action or its outcome ("Get my
  quote", never "Submit"); one primary per screen; one label per intent
  across the page (not "Get in touch" and "Contact us"); labels never wrap
  on desktop.
- **Micro-typography:** curly quotes, real ellipsis, en dash for ranges, a
  non-breaking space between number and unit, `tabular-nums` where numbers
  align, `text-wrap: balance` on headings and `pretty` on paragraphs. Nothing
  readable under 13 px; no justified text; no centred paragraph over three
  lines.

## Typography

- **Few sizes, far apart:** at most five; display at least 4× body on
  desktop. [study: median ratio 4.3]
- Display: tracking −0.02 to −0.05em, leading 0.85–1.05. Body: 16–20 px,
  leading 1.45–1.6, measure 45–75 characters set with `max-width` in `ch` on
  the paragraph. [study + standard]
- **One family is normal, two is the limit**, each with one job. No third
  face for labels or numbers; no mixed faces in one headline. [study]
- Space above a heading at least twice the space below it. Gaps between
  sections clearly larger than any gap inside one (~120–220 px desktop,
  ~72–112 px phone).

## Colour

- **Role tokens**, not raw hex: `--bg`, `--surface`, `--ink`, `--muted`,
  `--accent`, `--accent-ink`. No extra greys between roles.
- Ground covers most of the page; accent stays under ~5% of any screen —
  the primary action and at most one recurring element. Headings are ink.
- **MUST:** body text ≥ 4.5:1 contrast, large text ≥ 3:1; check `--muted`
  too. Running text in full ink. [standard: WCAG AA]
- Separate surfaces with a small tone step, not a 1 px line or a shadow;
  shadows only on things that float (menus, dialogs); no nested panels.
  [study: resting shadows on 24% of top sites vs 48% of weak]
- A section may change the whole ground colour with hard edges; neighbouring
  grounds differ in lightness, not only hue.
- **Dark pages:** `color-scheme: dark`, a tinted deep ground and soft light
  ink (not `#fff` on `#000`), depth from a lighter surface, never a glow.
- DON'T put text on a photo without a calm area or a neutral scrim; no
  colour washes over photos.

## Layout

- No reflexive centred 1200 px container: 16–32 px margins, let big things
  run full-bleed, constrain only text measure; cap around 1760–1920 px on very
  wide screens. [study]
- Two or three left edges for text across the page — count them on a
  screenshot.
- Neighbouring sections don't share a layout; repeated modules only for real
  archives (menu, schedule, work index). Carry the page's idea into pricing,
  FAQ and footer. [study: "distinctive hero, then stock blocks" was the
  commonest failure]
- **390 px is its own composition:** re-authored line breaks, portrait crops
  (`object-position`), 16–20 px margins, 16–18 px body, **touch targets ≥ 44
  px**. [standard for targets]
- Navigation: wordmark, three to five plain links, one action, about a tenth
  of the first screen at most. A fixed nav never covers content — check
  every scroll position on a phone.
- Full-height sections use `min-height: 100dvh`, not `100vh`. [standard]

## Imagery

- **One dominant image beats many small ones**; hero media covers at least
  half the first screen. One set of crop ratios and one treatment for the
  page; square corners or one radius everywhere. [study]
- Preference: the project's own pictures → generated → honest open-licence
  pictures of the subject's world → drawn in code → generic stock only where
  generic is honest → type and colour alone.
- **MUST NOT present a found picture as the client's** product, room, dish or
  person. Only licences that allow commercial use (CC0, public domain, CC BY,
  CC BY-SA — not NC or ND); download, don't hotlink; credit title, creator,
  source and licence. [standard: licence terms]
- DON'T use fake dashboards, device mock-ups or browser chrome; show software
  as a real HTML fragment with believable content.
- Meaningful pictures are `<img>`, not CSS backgrounds — backgrounds aren't
  indexed ([seo/content.md](../seo/content.md#images)).
- Decorative video: `muted loop playsinline`, a poster, `preload="metadata"`,
  hidden from assistive tech, stopped under reduced motion; keep it small —
  it competes with the LCP budget.

## Motion

- **MUST:** every animation inside `prefers-reduced-motion: no-preference`,
  so the reduced state is the finished page; hidden-until-revealed states
  only under a `js` class on `<html>`, so content shows if scripts fail.
  [standard]
- SHOULD animate only `transform`, `opacity` and `clip-path`, naming the
  properties (no `transition: all`), and reveal with IntersectionObserver,
  once.
- Don't fade the hero in from invisible — it delays the main content (LCP).
  Reveal two or three sections, not every block.
- Durations: press 100–160 ms, hover 150–200 ms, menus 150–250 ms, dialogs
  250–450 ms, reveals 500–900 ms; exits ~70% of the entry. Ease-out to enter
  and leave, ease-in-out for travel, never ease-in for UI. Nothing that fires
  hundreds of times animates.
- Hover styles behind `@media (hover: hover) and (pointer: fine)`; hover and
  focus raise contrast; weight never changes on hover; menus scale from
  0.95–0.98 at the trigger, never from 0.
- DON'T: the same fade-up on every block, bounce or elastic easing, a lift on
  every card, pointless infinite loops, scroll hijacking, custom cursors,
  heavy parallax.

## States (apps too)

- **SHOULD:** every data view has a loading state (a skeleton shaped like
  the layout), an empty state that says how to fill it, and inline errors —
  no `alert()`. Form rules (labels, contrast, errors):
  [marketing/conversion.md](../marketing/conversion.md#forms-and-signup).
- Buttons flat with one fill; square or fully round, chosen once; one radius
  scale for everything.

## Tells of an AI-made page

DON'T, with how often each appears on top vs weak sites [study]:
icon-topped feature cards (1% vs 28%), pill badges (14% vs 34%), tiny
uppercase letter-spaced labels (16% vs 57%), gradients (22% vs 52%) and
gradient text (2% vs 13%), resting shadows (24% vs 48%), emoji (10% vs 26%).
Also, on taste: violet/indigo palettes, cream with terracotta, glass panels,
floating pill navigation.

Copy tells live with the copy rules:
[marketing/content.md](../marketing/content.md#copy-rules).

- **Skip** banning monospace labels, 01/02/03 numbering or hairlines — the
  same data shows them *more* common on top sites.
- **Removing tells is not enough.** Fill the space with scale, full content,
  real pictures or a flat colour field — never another ornament. A richer
  page with tells beat an empty one without.

## Critique

- Judge from screenshots at 1440, 768 and 390 px, not from code. Passes: the
  one-second glance, squint, cover the logo, count the edges, check spacing,
  the phone, collisions.
- Fix in this order: idea → hierarchy → composition → type → imagery →
  colour → detail → motion. The top three problems per round, three rounds
  at most.
- The critic is a separate context that sees only the screenshots
  ([ai/agents.md](../ai/agents.md#known-failure-modes)).

## Sources

Leonxlnx, `taste-skill` (MIT), `https://github.com/Leonxlnx/taste-skill`,
shared via `https://x.com/lexnlin/status/2110122115240432021` (read
2026-10-15) — `skills/taste-skill/SKILL.md` and `references/` (copy, type,
colour, layout, imagery, motion, tells, critique, research). The repo's
older variants are judged in
[ai/skill-libraries.md](../ai/skill-libraries.md); none are used for these
rules.
Its `research/laziness/` folder has unverifiable citations; not used.

Re-read when this file is more than a year old.
