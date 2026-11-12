"""bhatiapranav.com — a small Flask site that is frozen to static files.

Nothing here runs in production: `python freeze.py` renders every route to
plain HTML in build/, and that folder is what gets deployed.
"""

from flask import Flask, render_template, abort

from data import content, log
app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Make these available in every template without passing them each time."""
    return {
        "c": content,
        "nav": [
            ("home", "home", "h"),
            ("projects", "projects", "p"),
            ("writing", "writing", "w"),
            ("about", "about", "a"),
            ("lab", "lab", "l"),
            ("books", "books", "b"),
            ("resume", "resume", "r"),
        ],
    }


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects/")
def projects():
    grouped = [
        (status, [p for p in content.PROJECTS if p["status"] == status])
        for status in content.STATUS_ORDER
    ]
    grouped = [(status, items) for status, items in grouped if items]
    return render_template("projects.html", grouped=grouped)


@app.route("/writing/")
def writing():
    by_year = {}
    for post in content.WRITING:
        by_year.setdefault(post["date"][:4], []).append(post)
    years = sorted(by_year.items(), reverse=True)
    return render_template("writing.html", years=years,
                           log_posts=log.load_posts())

@app.route("/writing/<slug>/")
def post(slug):
    match = next((p for p in log.load_posts() if p["slug"] == slug), None)
    if match is None:
        abort(404)
    return render_template("post.html", post=match)

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/lab/")
def lab():
    return render_template("lab.html")


@app.route("/books/")
def books():
    grouped = [
        (status, [b for b in content.BOOKS if b["status"] == status])
        for status in content.BOOK_STATUS_ORDER
    ]
    grouped = [(status, items) for status, items in grouped if items]
    return render_template("books.html", grouped=grouped)


@app.route("/resume/")
def resume():
    return render_template("resume.html")


@app.template_filter("pretty_date")
def pretty_date(iso):
    """2025-09-09 -> sep 09"""
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
    _, month, day = iso.split("-")
    return f"{months[int(month) - 1]} {day}"


if __name__ == "__main__":
    app.run(debug=True, port=5002)
