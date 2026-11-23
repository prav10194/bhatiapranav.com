"""Markdown rendering for the learning log.

Adds terminal-flavoured block types on top of plain Markdown. Everything is
rendered at freeze time, so the deployed pages are static HTML with no script.

Fences
------
```python  optional label        syntax-highlighted code with a label bar
```console optional label        shell session; $ lines are prompts
```diagram optional caption      ASCII art, preserved exactly
```chart   optional caption      same as diagram, semantically a chart
```measured | note | warn        callout; body is Markdown
```key                           first line is a big number, rest is caption
"""

import re
from xml.sax.saxutils import escape

import markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

CALLOUTS = {
    "measured": "measured",
    "note": "note",
    "warn": "careful",
}
VERBATIM = {"console", "diagram", "chart"}

_FENCE = re.compile(r"^```(\w+)(?:\s+(.*?))?\s*$")
_CLOSE = re.compile(r"^```\s*$")
_FORMATTER = HtmlFormatter(nowrap=True)


def _inner_markdown(text):
    return markdown.markdown(text, extensions=["tables"])


def _code_html(lang, label, body):
    try:
        lexer = get_lexer_by_name(lang, stripall=False)
        inner = highlight(body, lexer, _FORMATTER)
    except ClassNotFound:
        inner = escape(body)
    bar = f'<div class="blk-bar">{escape(label)}</div>' if label else ""
    return (f'<div class="blk blk-code">{bar}'
            f'<pre class="hl"><code>{inner}</code></pre></div>')


def _console_html(label, body):
    out = []
    for line in body.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("$ ") or stripped == "$":
            lead = line[: len(line) - len(stripped)]
            out.append(f'{escape(lead)}<span class="c-prompt">$</span>'
                       f'<span class="c-cmd">{escape(stripped[1:])}</span>')
        elif stripped.startswith("#"):
            out.append(f'<span class="c-comment">{escape(line)}</span>')
        else:
            out.append(f'<span class="c-out">{escape(line)}</span>')
    bar = f'<div class="blk-bar">{escape(label)}</div>' if label else ""
    return (f'<div class="blk blk-console">{bar}'
            f'<pre><code>{chr(10).join(out)}</code></pre></div>')


def _verbatim_html(kind, label, body):
    cap = f'<div class="blk-cap">{escape(label)}</div>' if label else ""
    return (f'<div class="blk blk-{kind}">'
            f'<pre><code>{escape(body)}</code></pre>{cap}</div>')


def _callout_html(kind, label, body):
    title = label or CALLOUTS[kind]
    return (f'<aside class="callout callout-{kind}">'
            f'<div class="callout-tag">{escape(title)}</div>'
            f'<div class="callout-body">{_inner_markdown(body)}</div></aside>')


def _key_html(label, body):
    lines = [l for l in body.split("\n") if l.strip()]
    big = lines[0] if lines else ""
    rest = "\n".join(lines[1:])
    cap = f'<div class="key-cap">{_inner_markdown(rest)}</div>' if rest else ""
    tag = f'<div class="key-tag">{escape(label)}</div>' if label else ""
    return (f'<div class="keyblock">{tag}'
            f'<div class="key-num">{escape(big)}</div>{cap}</div>')


class TerminalBlocks(Preprocessor):
    def run(self, lines):
        out, i = [], 0
        while i < len(lines):
            m = _FENCE.match(lines[i])
            if not m:
                out.append(lines[i])
                i += 1
                continue

            kind, label = m.group(1), (m.group(2) or "").strip()
            body, j = [], i + 1
            while j < len(lines) and not _CLOSE.match(lines[j]):
                body.append(lines[j])
                j += 1
            text = "\n".join(body)

            if kind in CALLOUTS:
                html = _callout_html(kind, label, text)
            elif kind == "key":
                html = _key_html(label, text)
            elif kind == "console":
                html = _console_html(label, text)
            elif kind in VERBATIM:
                html = _verbatim_html(kind, label, text)
            else:
                html = _code_html(kind, label, text)

            out.append("")
            out.append(self.md.htmlStash.store(html))
            out.append("")
            i = j + 1
        return out


class TerminalExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(TerminalBlocks(md), "terminal_blocks", 26)


def to_html(text):
    return markdown.markdown(text, extensions=["tables", TerminalExtension()])
