"""Read the learning log from content/log/*.md.

Each post is one Markdown file with a YAML frontmatter header. The filename
carries the date and the slug: 2026-11-11-what-an-embedding-is.md

This runs at freeze time, not at request time. The deployed site is static.
"""

import re
from pathlib import Path

import frontmatter
import markdown

LOG_DIR = Path(__file__).resolve().parent.parent / "content" / "log"


def load_posts():
    posts = []

    for path in sorted(LOG_DIR.glob("*.md")):
        doc = frontmatter.load(path)

        # 2026-11-11-what-an-embedding-is  ->  what-an-embedding-is
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)

        posts.append({
            "slug": slug,
            # str() because YAML parses a bare date into a date object, and
            # the pretty_date filter expects "2026-11-11".
            "date": str(doc["date"]),
            "title": doc["title"],
            "summary": doc.get("summary", ""),
            "html": markdown.markdown(
                doc.content,
                extensions=["fenced_code", "tables"],
            ),
        })

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts
