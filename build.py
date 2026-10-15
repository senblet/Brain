"""Regenerate brain-map.svg, the map shown at the top of the README.

Reads every topic file, then draws: topics and their files, how fresh each
file's sources are, decisions where sources disagreed, and the most recent reads (taken from the
Sources dates, so the map is current the moment a source is added).
Standard library only. Run after every change: python3 build.py
"""

import re
from datetime import date, timedelta
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "brain-map.svg"
SKIP_DIRS = {".git", "checklists"}

DEFAULT_WINDOW = 365  # days; a file can say otherwise in its Sources section
WINDOW_PATTERNS = [
    (re.compile(r"more than (?:a|one) year old"), 365),
    (re.compile(r"more than six months old"), 182),
    (re.compile(r"more than (\d+) months old"), None),
]

# Layout
WIDTH = 880
PAD = 24
LABEL_W = 120
CARD_W, CARD_H, GAP = 228, 64, 10
PER_ROW = 3


def recheck_window(text):
    for pattern, days in WINDOW_PATTERNS:
        m = pattern.search(text)
        if m:
            return days if days else int(m.group(1)) * 30
    return DEFAULT_WINDOW


def read_file(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    topic = title.split(" — ")[0].strip()
    sources = text.split("\n## Sources", 1)[1] if "\n## Sources" in text else ""
    sources = " ".join(sources.split())  # sentences wrap across lines
    reads = sorted(re.findall(r"read (\d{4}-\d{2}-\d{2})", sources))
    cited = {
        t for t in re.findall(r"`([^`\s]+)`", sources)
        if not t.endswith("/") and not t.startswith("/")
    }
    window = recheck_window(sources)
    oldest = date.fromisoformat(reads[0]) if reads else None
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "name": path.stem,
        "topic": topic,
        "cited": len(cited),
        "oldest": oldest,
        "reads": set(reads),
        "recheck": oldest + timedelta(days=window) if oldest else None,
        "window": window,
        "conflicts": len(re.findall(r"\*\*Decided:", text)),
    }


def status(f, today):
    if not f["recheck"]:
        return "none"
    age = (today - f["oldest"]).days
    if age >= f["window"]:
        return "due"
    if age >= f["window"] / 2:
        return "soon"
    return "fresh"


def latest_reads(files, n=3):
    """The n most recent read dates, each with the files that gained a source."""
    dates = sorted({d for f in files for d in f["reads"]}, reverse=True)[:n]
    return [(d, [f["path"].removesuffix(".md") for f in files if d in f["reads"]]) for d in dates]


def clip(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"


def build():
    today = date.today()
    files = [
        read_file(p)
        for d in sorted(ROOT.iterdir())
        if d.is_dir() and d.name not in SKIP_DIRS
        for p in sorted(d.glob("*.md"))
    ]
    topics = {}
    for f in files:
        topics.setdefault(f["topic"], []).append(f)
    topics = dict(sorted(topics.items(), key=lambda t: (-len(t[1]), t[0])))

    conflicts = sum(f["conflicts"] for f in files)
    rechecks = [f["recheck"] for f in files if f["recheck"]]
    summary = (
        f"{len(files)} files · {len(topics)} topics · "
        f"{conflicts} decision{'s' if conflicts != 1 else ''} where sources disagreed"
        + (f" · next recheck {min(rechecks).isoformat()}" if rechecks else "")
    )

    body = []
    y = PAD
    body.append(f'<text x="{PAD}" y="{y + 20}" class="h1">brain</text>')
    body.append(f'<text x="{PAD + 70}" y="{y + 20}" class="muted">{escape(summary)}</text>')
    y += 44

    for topic, items in topics.items():
        rows = (len(items) + PER_ROW - 1) // PER_ROW
        block_h = rows * CARD_H + (rows - 1) * GAP
        body.append(f'<text x="{PAD}" y="{y + 22}" class="topic">{escape(topic)}</text>')
        for i, f in enumerate(items):
            cx = PAD + LABEL_W + (i % PER_ROW) * (CARD_W + GAP)
            cy = y + (i // PER_ROW) * (CARD_H + GAP)
            st = status(f, today)
            body.append(f'<a href="{escape(f["path"])}"><g>')
            body.append(f'<rect x="{cx}" y="{cy}" width="{CARD_W}" height="{CARD_H}" rx="8" class="card"/>')
            body.append(f'<rect x="{cx}" y="{cy}" width="5" height="{CARD_H}" rx="2" class="s-{st}"/>')
            body.append(f'<text x="{cx + 16}" y="{cy + 22}" class="name">{escape(clip(f["name"], 24))}</text>')
            if f["conflicts"]:
                body.append(
                    f'<text x="{cx + CARD_W - 12}" y="{cy + 22}" class="badge" text-anchor="end">'
                    f'{f["conflicts"]} decided</text>'
                )
            line2 = f'{f["cited"]} cited' + (f' · read {f["oldest"].isoformat()}' if f["oldest"] else "")
            line3 = f'recheck by {f["recheck"].isoformat()}' if f["recheck"] else "no sources"
            body.append(f'<text x="{cx + 16}" y="{cy + 40}" class="small">{escape(line2)}</text>')
            body.append(f'<text x="{cx + 16}" y="{cy + 55}" class="small t-{st}">{escape(line3)}</text>')
            body.append("</g></a>")
        y += block_h + 18

    recent = latest_reads(files)
    if recent:
        y += 6
        body.append(f'<line x1="{PAD}" y1="{y}" x2="{WIDTH - PAD}" y2="{y}" class="rule"/>')
        y += 24
        body.append(f'<text x="{PAD}" y="{y}" class="topic">Latest reads</text>')
        for when, paths in recent:
            lines = [""]
            for p in paths:  # wrap the file list instead of cutting it
                joined = f"{lines[-1]} · {p}" if lines[-1] else p
                if len(joined) > 92 and lines[-1]:
                    lines.append(p)
                else:
                    lines[-1] = joined
            body.append(f'<text x="{PAD + LABEL_W}" y="{y}" class="small mono">{escape(when)}</text>')
            for line in lines:
                body.append(f'<text x="{PAD + LABEL_W + 82}" y="{y}" class="small">{escape(line)}</text>')
                y += 18
            y += 4
        y += 4

    y += 8
    lx = PAD + LABEL_W
    for st, label in (("fresh", "fresh"), ("soon", "past half its recheck window"), ("due", "recheck due")):
        body.append(f'<rect x="{lx}" y="{y - 9}" width="10" height="10" rx="2" class="s-{st}"/>')
        body.append(f'<text x="{lx + 16}" y="{y}" class="small">{label}</text>')
        lx += 32 + len(label) * 5.8
    height = y + PAD

    style = """
    text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; fill: #1f2328; }
    .h1 { font-size: 22px; font-weight: 700; }
    .topic { font-size: 14px; font-weight: 600; }
    .name { font-size: 14px; font-weight: 600; }
    .small { font-size: 12px; fill: #59636e; }
    .muted { font-size: 13px; fill: #59636e; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
    .badge { font-size: 11px; font-weight: 600; fill: #9a6700; }
    .bg { fill: #ffffff; }
    .card { fill: #f6f8fa; stroke: #d1d9e0; }
    .rule { stroke: #d1d9e0; }
    .s-fresh { fill: #1a7f37; } .s-soon { fill: #bf8700; } .s-due { fill: #cf222e; } .s-none { fill: #818b98; }
    .t-soon { fill: #9a6700; } .t-due { fill: #cf222e; font-weight: 600; }
    a:hover .card { stroke: #0969da; }
    @media (prefers-color-scheme: dark) {
      text { fill: #f0f6fc; }
      .small, .muted { fill: #9198a1; }
      .badge, .t-soon { fill: #d29922; }
      .t-due { fill: #f85149; }
      .bg { fill: #0d1117; }
      .card { fill: #151b23; stroke: #3d444d; }
      .rule { stroke: #3d444d; }
      .s-fresh { fill: #3fb950; } .s-soon { fill: #d29922; } .s-due { fill: #f85149; }
      a:hover .card { stroke: #4493f8; }
    }"""

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" '
        f'viewBox="0 0 {WIDTH} {height}" role="img" aria-label="Brain map: {escape(summary)}">\n'
        f"<style>{style}\n</style>\n"
        f'<rect width="{WIDTH}" height="{height}" rx="12" class="bg"/>\n'
        + "\n".join(body)
        + "\n</svg>\n"
    )
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name}: {summary}")


if __name__ == "__main__":
    build()
