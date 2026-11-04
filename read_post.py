"""Print the full text of X posts, including long-form articles and the
code blocks embedded in them, so a source can be read in full before it is
folded in. Standard library only.

    python3 read_post.py https://x.com/user/status/123 [more URLs...]

Uses the public fxtwitter API (no login). Output is plain text: author,
date, the post, any quoted post, the article body, embedded blocks, links
and media URLs. Images are not described — open the printed URL to read
one.
"""

import json
import re
import sys
import urllib.request

API = "https://api.fxtwitter.com/{user}/status/{id}"


def fetch(url):
    m = re.search(r"(?:x|twitter)\.com/([^/]+)/status/(\d+)", url)
    if not m:
        return None, f"not an X post URL: {url}"
    req = urllib.request.Request(
        API.format(user=m.group(1), id=m.group(2)),
        headers={"User-Agent": "brain-reader/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r), None
    except Exception as e:  # network or JSON error: report, keep going
        return None, f"could not fetch {url}: {e}"


def render(data):
    t = data.get("tweet") or {}
    author = (t.get("author") or {}).get("screen_name", "?")
    out = [
        "=" * 78,
        f"@{author} | {t.get('created_at')} | {t.get('url', '')}",
        t.get("text", ""),
    ]
    q = t.get("quote")
    if q:
        out.append(f"--- quoted @{q['author']['screen_name']}: {q.get('text', '')}")
    a = t.get("article")
    if a:
        out.append(f"--- article: {a.get('title')}")
        content = a.get("content") or {}
        for b in content.get("blocks", []):
            text = b.get("text", "")
            if not text.strip():
                continue
            kind = b.get("type", "")
            prefix = "# " if "header" in kind else "- " if "list" in kind else ""
            out.append(prefix + text)
        entities = content.get("entityMap")
        for e in entities if isinstance(entities, list) else []:
            v = e.get("value", e)
            if v.get("type") == "MARKDOWN":
                out.append("[embedded]\n" + v["data"].get("markdown", ""))
            elif v.get("type") == "LINK":
                out.append("[link] " + v["data"].get("url", ""))
    media = (t.get("media") or {}).get("all") or []
    for m in media:
        out.append(f"[{m.get('type')}] {m.get('url')}")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for url in sys.argv[1:]:
        data, err = fetch(url)
        print(render(data) if data else f"!! {err}")
