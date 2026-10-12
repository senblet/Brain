# SEO — AI search features and AI crawlers

How Google's AI Overviews and AI Mode pick pages, and which robots.txt
tokens control AI search and AI training crawlers.

**Tags:** **MUST** = required for eligibility or a spam-policy line.
**SHOULD** = best practice with real effect. **DON'T** = actively harmful.
**Skip** = effort Google says is wasted. Ground truth, spam policies and the
pre-ship checklist are in [overview.md](overview.md).

---

- **Google's AI Overviews and AI Mode have no extra requirements.** A page is
  eligible as a supporting link if it is indexed and can be shown in Search
  with a snippet. Everything in the other SEO files applies; no special
  optimization is needed.
- **Google controls:** AI features are part of Search, so robots.txt rules for
  Googlebot are the control. To limit what is shown, use `nosnippet`,
  `data-nosnippet`, `max-snippet` or `noindex` ([appearance.md](appearance.md),
  [crawling-indexing.md](crawling-indexing.md)).
- **`Google-Extended`** is a robots.txt token only, with no user agent of its
  own. It controls whether crawled content trains Gemini models and grounds
  Gemini Apps and Vertex AI. It does **not** affect inclusion or ranking in
  Google Search.
- **OpenAI uses independent tokens:**
  - `OAI-SearchBot` surfaces pages in ChatGPT search. A site that blocks it
    is not shown in ChatGPT search answers (it can still appear as a bare
    link). Changes take about 24 hours to apply.
  - `GPTBot` crawls for model training. Blocking it opts out of training and
    does not affect ChatGPT search.
  - `ChatGPT-User` fetches pages when a user asks; robots.txt may not apply,
    and it is not used to decide what appears in search.
  - A blocked page can still show as a link and title. To keep it out, use
    `noindex` and allow crawling, as with Google.
- **DON'T** add a blanket "block AI bots" robots.txt group. Blocking search
  crawlers (`Googlebot`, `OAI-SearchBot`) costs visibility. Blocking training
  crawlers (`GPTBot`, `Google-Extended`) is a business decision for the site
  owner, not an SEO fix — ask before adding it.

## Sources

Google Search Central, `https://developers.google.com/search/docs/`:
`appearance/ai-features` (read 2026-10-05).

Google crawlers:
`https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers`
(read 2026-10-05).

OpenAI: `https://developers.openai.com/api/docs/bots` ·
`https://help.openai.com/en/articles/12627856-publishers-and-developers-faq`
(read 2026-10-05).

AI tooling moves fast; re-read these pages when this file is more than a year old.
