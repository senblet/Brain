# CLAUDE.md — maintaining the brain

This repo is Riccardo's personal knowledge base. He sends articles, docs or
links; your job is to fold what's worth keeping into the right file. Read
`README.md` for the structure and tagging conventions before changing anything.

## Ingesting a new source

1. **Read the whole source.** Skip filler, opinion without evidence, and
   anything already covered.
2. **Pick the destination by topic**, not by the file you last touched. Look
   for an existing file first; create `<topic>/<subtopic>.md` only when nothing
   fits.
3. **Merge, don't append.** Put each new point in the section it belongs to.
   If it contradicts an existing point, decide which is right (newer, more
   authoritative, better evidenced), keep that one, and note the change in the
   commit message. If you can't tell, keep both and mark it
   `**Conflict:**` with both sources.
4. **Write rules, not summaries.** Concrete and actionable, tagged MUST /
   SHOULD / DON'T / Skip. Keep the source's caveats ("optional for small
   sites") — never upgrade a nice-to-have into a rule.
5. **Never invent** numbers, dates, quotes or claims the source doesn't make.
   Estimates are labelled as estimates.
6. **Add the source** to the file's Sources list with the date read.
7. **Update `checklists/new-project.md`** if the change affects what to do when
   starting a project.
8. **Update the README index** if you created a file or the file's scope changed.
9. **Commit** with a message naming the source and what changed
   (e.g. `seo: add INP guidance from web.dev article; supersedes FID notes`).

## Splitting files

Start with one file per topic. Split into subtopic files when a file passes
roughly 600 lines or covers clearly separate concerns, and update links and
the index when you do.

## Tone

Plain, direct English. Short sentences. Code, tags and paths in backticks.
