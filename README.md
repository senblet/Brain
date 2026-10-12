# brain

My go-to knowledge base. Each file distills articles, docs and guides I found
worth keeping into rules I can act on — the files I open (or hand to an agent)
when starting a new project.

## Index

| Topic | File | What it covers |
|---|---|---|
| SEO | [seo/google-search.md](seo/google-search.md) | Google's crawling, indexing, content, structured data and spam rules; AI search crawlers |
| Checklist | [checklists/new-project.md](checklists/new-project.md) | What to set up when starting a new project, distilled from the topic files |

## Structure

```
brain/
├── README.md              ← this index
├── CLAUDE.md              ← how new articles get folded in
├── <topic>/               ← one folder per domain (seo, development, ai…)
│   └── <subtopic>.md      ← split a topic only when one file gets too long
└── checklists/
    └── new-project.md     ← the "starting something" file
```

## How notes are written

- **Merged, not appended.** A new article updates the existing file: new points
  are added where they belong, contradictions are flagged, superseded points
  are removed. No file is a stack of article summaries.
- **Tagged by strength:**

  | Tag | Meaning |
  |---|---|
  | **MUST** | Required, or breaks things if ignored |
  | **SHOULD** | Best practice with a real effect |
  | **DON'T** | Actively harmful |
  | **Skip** | Effort that isn't worth it |

- **Sourced and dated.** Every file ends with a Sources list, with the date
  each source was read. Fast-moving topics (SEO, AI tooling) get rechecked
  when a file is more than a year old.
- **Checklists follow the topics.** When a topic file changes, the matching
  section of `checklists/new-project.md` is updated too.
