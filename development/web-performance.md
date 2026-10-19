# Development — web performance

What to check before shipping a site so it is fast on a real phone, and how
to run that check with agents without breaking anything. The thresholds that
count for search are in [seo/overview.md](../seo/overview.md#page-experience):
LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1.

**Tags:** as in the [README](../README.md#how-notes-are-written). The check
list is from one practitioner post (read 2026-10-14), written for Next.js,
Supabase and Vercel; the general rules apply to any stack, including the
house stack (Vue + Vite, Django + DRF). Stack-specific items are kept
separate.

---

## How to measure

- MUST measure a **production build** (or a preview deploy), never the dev
  server.
- Lighthouse in **mobile** mode, **three runs**, take the median — single
  runs are noisy. Measure the home page and the two or three slowest pages.
- Click through the main flows in Chrome emulating a **low-end Android phone
  on slow 4G**.
- Measure before changing anything and again after; report both numbers.

## What to check

### Images and fonts
- Every image in WebP or AVIF, sized to how large it actually displays,
  with explicit `width` and `height` attributes so the layout doesn't jump
  while it loads (CLS).
- Lazy-load images and video below the fold; load the main image at the top
  of the page first.
- One or two fonts, loaded the way the framework recommends.
- Remove third-party scripts you don't use; load analytics and chat widgets
  after the page has loaded.

### Frontend code
- Run a bundle analyser; where a whole library is imported, import only the
  parts used.
- Load heavy components the first screen doesn't need (charts, editors,
  maps) on demand.
- Fetch the first screen's data on the server, so the page arrives with
  content in it (also what search engines need —
  [seo/crawling-indexing.md](../seo/crawling-indexing.md#javascript-sites-and-spas)).
- Stream AI answers as they generate; show skeletons while data loads.

### Database and APIs
- Index the columns you filter and sort by — including the ones access rules
  filter on (e.g. the user id).
- Find N+1 queries and turn them into one query.
- Paginate long lists.
- Cache responses that are the same for everyone; **never** cache anything
  tied to a logged-in user.
- Move heavy work (sending email, processing images, building reports) to
  background jobs.

### Servers and network
- Run server code in the same region as the database.
- Serve pages whose content rarely changes as static or regenerated pages.
- When a page calls several APIs in sequence, run them in parallel or merge
  them.

### Stack-specific (Next.js / Supabase / Vercel)
- Images through `next/image`, fonts through `next/font`; heavy components
  with dynamic import; static or ISR pages.
- Supabase row-level security: write `auth.uid()` as `(select auth.uid())`
  in policies so it runs once per query, and index the policy columns.
- New Vercel projects run functions in US East by default — move them next
  to the database.

## Running it with agents

- Fan out **read-only**: one subagent per group above, each listing the
  file and page every issue affects, without editing. Give the database
  group more reasoning effort — it has to read queries and choose indexes.
  Then fix from their lists in one pass and measure again
  ([ai/agent-workflows.md](../ai/agent-workflows.md)).
- Limits to write into the task: **don't remove features to gain speed**;
  ask before removing dependencies, changing the deploy region or changing
  the database.
- For a single target ("LCP under 2 s on a phone"), run it as a long goal
  with a measure, a keep-or-revert rule and a stop condition
  ([ai/agents.md](../ai/agents.md#long-running-goals)).

## Sources

Voxyz (@Voxyz_ai), "Claude Code tip: before you ship a vibe-coded site…",
`https://x.com/voxyz_ai/status/2110083153930920113` (read 2026-10-14).
Practitioner list, no measurements behind it; the items are standard
practice. Thresholds from web.dev via [seo/overview.md](../seo/overview.md).
Explicit image dimensions: Connor Showler,
`https://x.com/connorshowler/status/2111150132397818312` (read 2026-10-19).

Re-read when this file is more than a year old.
