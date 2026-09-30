# bhatiapranav.com

A small Flask site that is **frozen to static HTML**. Nothing runs in
production: `freeze.py` renders every route into `build/`, and that folder is
what gets deployed.

Phase 1 is deliberately plain — four HTML files' worth of site. The
over-engineering comes later, on purpose, and is documented at `/lab`.

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python app.py          # dev server at http://127.0.0.1:5002
python freeze.py       # renders build/
```

To preview the frozen output exactly as it will be served:

```bash
cd build && python3 -m http.server 8000
```

## Where things live

| Path | What |
|---|---|
| `app.py` | five routes, one per page |
| `data/content.py` | **all site content** — edit here, never in templates |
| `templates/base.html` | nav, footer, `<head>`; every page extends it |
| `templates/*.html` | one per page |
| `static/style.css` | design tokens at the top; single dark theme |
| `static/keys.js` | keyboard nav (h / p / w / a / l) |
| `freeze.py` | writes `build/` and prints page sizes |
| `content/log/` | learning-log posts (markdown) — not wired up yet |

## Editing

- **The `now` line, projects, writing, timeline:** `data/content.py`.
- **Colours and type:** the `:root` block in `static/style.css`. Changing
  `--accent` restyles the whole site.
- A stale `now` line is worse than no `now` line.

## Deploy

Target is Firebase Hosting (free tier) with `build/` as the public directory,
on the domain bhatiapranav.com (registered at Cloudflare; DNS stays there).

```bash
firebase init hosting     # public dir: build, single-page app: no
firebase deploy
```

## Notes

Frozen-Flask renders through Flask's test client, so no server starts during a
build and the dev port is irrelevant. Routes end in a trailing slash, which
makes each page a `build/<name>/index.html` — served correctly by any static
host without extra configuration.
