# New project checklist

What to set up when starting something new. Each section is distilled from a
topic file and links back to it for the reasoning. Sections are added as the
brain grows.

## SEO — public pages

From the [seo/](../seo/overview.md) notes. Skip this section for apps that live
entirely behind a login.

**At setup**
- [ ] Copy the `seo/` folder into the repo (e.g. as `docs/seo/`) and reference
      `overview.md` from `AGENTS.md` / `CLAUDE.md`.
- [ ] HTTPS everywhere; HTTP → HTTPS 301; pick `www` or apex and 301 the other.
- [ ] Server-side rendering or prerendering for public pages.
- [ ] Routing uses the History API (no `#/` URLs); links are real `<a href>`.
- [ ] Readable, hyphenated, lowercase URLs; no session IDs in URLs.
- [ ] Unique `<title>` and meta description per page; one clear `<h1>`.
- [ ] Self-referencing absolute `rel="canonical"` on every indexable page.
- [ ] Real `404` status for missing pages (or `noindex` in an SPA).
- [ ] `robots.txt` doesn't block CSS/JS, `Googlebot` or `OAI-SearchBot`.
      Blocking training crawlers (`GPTBot`, `Google-Extended`) is a business
      decision — decide it explicitly.
- [ ] Sitemap generated from the site's own data, with honest `<lastmod>`
      (optional under ~500 well-linked pages).
- [ ] `Organization` + `WebSite` structured data on the home page.
- [ ] Mobile-friendly; no full-page interstitials.

**At launch**
- [ ] Verify the site in Search Console and submit the sitemap.
- [ ] Check key pages with URL Inspection and the Rich Results Test.
- [ ] Run PageSpeed Insights on the main templates.

**Ongoing**
- [ ] Monthly look at Search Console (indexing, performance, Core Web Vitals).
- [ ] Wait a few weeks before judging any SEO change.
