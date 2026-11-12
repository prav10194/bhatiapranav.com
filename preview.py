"""Freeze a click-through copy with relative URLs, for sharing as a preview.

    python preview.py

Same pages as freeze.py, but every link is relative, so the build works when
it is served from a subpath instead of a domain root. Not what gets deployed.
"""

import shutil
from pathlib import Path

from flask_frozen import Freezer

from app import app

BUILD = Path(__file__).parent / "preview_build"

app.config["FREEZER_DESTINATION"] = str(BUILD)
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True
app.config["FREEZER_STATIC_IGNORE"] = ["*.map", ".DS_Store"]
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)

if __name__ == "__main__":
    if BUILD.exists():
        shutil.rmtree(BUILD)
    urls = list(freezer.freeze())
    # the artifact's own entry page is a cover, so home moves aside and every
    # link to it is repointed
    (BUILD / "index.html").rename(BUILD / "home.html")
    home = BUILD / "home.html"
    home.write_text(home.read_text().replace('href="index.html"', 'href="home.html"'))
    for page in BUILD.rglob("*/*.html"):
        text = page.read_text()
        page.write_text(text.replace('href="../index.html"', 'href="../home.html"'))
    print(f"froze {len(urls)} urls -> {BUILD}")
    for f in sorted(BUILD.rglob("*")):
        if f.is_file():
            print(" ", f.relative_to(BUILD))
