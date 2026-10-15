# CLAUDE.md — maintaining the brain

This repo is Riccardo's personal knowledge base. He sends articles, docs or
links; your job is to fold what's worth keeping into the right file. Read
`README.md` for the structure and tagging conventions before changing anything.

## Ingesting a new source

1. **Read the whole source.** Skip filler, opinion without evidence, and
   anything already covered. A social post earns a place only if it adds a
   rule no file has, or points to a repo or primary source; if it mostly
   repeats the brain, say so and stop — the brain grows by decisions, not
   by volume.
2. **Pick the destination by topic**, not by the file you last touched. Look
   for an existing file first; create `<topic>/<subtopic>.md` only when nothing
   fits.
3. **Merge, don't append.** Put each new point in the section it belongs to.
4. **Resolve contradictions; never leave them open.** When a new point
   contradicts an existing one, decide. Weigh, in order: primary
   documentation beats practitioner claims; measured data beats opinion;
   the studio's own results beat both; newer beats older only if the
   evidence is at least as good. Then write the rule as decided and, in one
   sentence, what was rejected and why, marked `**Decided:**`, so the losing
   source is not lost. If the evidence is genuinely equal, decide anyway on
   what fits the studio's situation (small team, niche products, low
   traffic) and say that is the basis. Note the decision in the commit
   message. `**Conflict:**` is not a valid state to commit.
5. **Write rules, not summaries.** Concrete and actionable, tagged MUST /
   SHOULD / DON'T / Skip. Keep the source's caveats ("optional for small
   sites") — never upgrade a nice-to-have into a rule.
6. **Never invent** numbers, dates, quotes or claims the source doesn't make.
   Estimates are labelled as estimates.
7. **Add the source** to the file's Sources list with the date read.
8. **Update `checklists/new-project.md`** if the change affects what to do when
   starting a project.
9. **Update the README index** if you created a file or the file's scope changed.
10. **Leave the brain organised.** Before committing, re-read every file you
   touched, end to end, and check:
   - **One home per rule.** If the point already exists elsewhere, link to
     it instead of restating it. Rules that apply beyond one domain go in
     the most general file (agent practice → `ai/agents.md`).
   - **Right file, right section.** Each section sits where a reader would
     look for it; no stub sections, no "misc" piles.
   - **Intros and index are true.** Each file's opening paragraph, the
     README index and `seo/overview.md`'s file table describe what is
     actually in the files now.
   - **`seo/` stays self-contained** — no links out of it.
   - **Links resolve**, including `#anchors`.
   - **No open `**Conflict:**`** — every contradiction carries a decision.
   If the answer to any of these is no, fix it in the same commit.
11. **Run `python3 build.py`** to regenerate `brain-map.svg`. It reads the
   `read YYYY-MM-DD` dates and `**Decided:**` markers, so keep those
   formats.
12. **Commit** with a message naming the source and what changed
   (e.g. `seo: add INP guidance from web.dev article; supersedes FID notes`).

## Splitting files

Start with one file per topic. Split into subtopic files when a file passes
roughly 600 lines or covers clearly separate concerns, and update links and
the index when you do.

## Tone

Plain, direct English. Short sentences. Code, tags and paths in backticks.
