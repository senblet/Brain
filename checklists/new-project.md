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
- [ ] Domain: a ccTLD (`.cl`) locks the site to one country. If other markets
      are possible later, use a generic TLD with subdirectories.
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

**Content, if the site will publish pages for search**
- [ ] First pages target commercial, specific queries; intent read off the
      live results page, not guessed.
- [ ] Before each new page: cannibalisation check in Search Console
      (query → Pages tab).
- [ ] Each page has one element the top results lack (data, calculator,
      real photos, quiz) — or it isn't shipped.
- [ ] A process file the agent reads before every publish: template, in-body
      internal links from related pages, structured data, sitemap update,
      request indexing. After duplicating a page, diff for what went
      missing.
- [ ] A publishing cadence, written down, held.

**If an agent publishes or edits pages**
- [ ] Permission list in the repo: ALLOW (read, draft) / REQUIRE APPROVAL
      (publish, edit live, titles on pages with clicks, redirects) / BLOCK
      (delete, robots.txt, canonicals, external email, spending). Hard limits
      in code, not prompts — see [marketing/agents.md](../marketing/agents.md).
- [ ] A standards file where every rejected draft leaves a one-line reason.

**Local business** — see [seo/local.md](../seo/local.md)
- [ ] Business Profile: real name, precise address, local phone, as few
      categories as truly fit, every real service, description without links
      or prices, photos.
- [ ] Homepage `<title>`/`<h1>` = primary category + city; address and phone
      character-for-character as on the profile; `LocalBusiness` data.
- [ ] Review request + reply routine, no case details in replies.

**Ongoing**
- [ ] Monthly look at Search Console (indexing, performance, Core Web Vitals).
- [ ] Monthly: repoint pages to the queries Google already shows them for.
- [ ] Monthly, if AI referrals matter: ~10 buyer questions by hand, logged
      out; note which pages get cited and whether you're in them.
- [ ] Wait a few weeks before judging any SEO change; ~2 months for a dip.
