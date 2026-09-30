"""Render every route to static HTML in build/.

    python freeze.py

Frozen-Flask walks the app's URL map, requests each route through Flask's
test client (no server is started), and writes the response to disk.
"""

import shutil
import time
from pathlib import Path

from flask_frozen import Freezer

from app import app

BUILD = Path(__file__).parent / "build"

app.config["FREEZER_DESTINATION"] = str(BUILD)
app.config["FREEZER_REMOVE_EXTRA_FILES"] = True
app.config["FREEZER_STATIC_IGNORE"] = ["*.map", ".*"]

freezer = Freezer(app)


def size_of(path):
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


if __name__ == "__main__":
    if BUILD.exists():
        shutil.rmtree(BUILD)

    started = time.perf_counter()
    urls = list(freezer.freeze())
    elapsed = time.perf_counter() - started

    pages = sorted(p.relative_to(BUILD) for p in BUILD.rglob("*.html"))
    print(f"\nfroze {len(urls)} urls in {elapsed:.2f}s -> {BUILD}")
    for page in pages:
        kb = (BUILD / page).stat().st_size / 1024
        print(f"  {str(page):<28} {kb:6.1f} KB")
    print(f"\n  total build size: {size_of(BUILD) / 1024:.1f} KB")
