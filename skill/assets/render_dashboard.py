#!/usr/bin/env python3
"""Render a study workspace's ``00-DASHBOARD.html`` from its curriculum + state.

The dashboard is a strictly-derived projection of the curriculum: it is
GENERATED, never hand-edited. This script is that generator. It reads three
inputs and nothing else:

  1. the curriculum  ``04-resources/<slug>.md``   (concept IDs, labels, tier, order)
  2. the state file  ``02-progress/_state.json``  (per-concept status + the prose)
  3. the shared      ``workspace-styles.css``     (embedded verbatim, single file)

It computes the weighted concept count and the overall percent, then writes a
self-contained ``00-DASHBOARD.html`` that follows ``references/dashboard-format.md``.

This runs at AUTHORING time (when the tutor records progress), has no
third-party dependencies, makes no network calls, and is deterministic: the same
inputs always produce byte-identical output. Marking a concept proven becomes
one edit to ``_state.json`` plus one run of this script, in place of hand-editing
the HTML in a dozen scattered spots.

Usage::

    # convenience: everything derived from one subject directory
    python render_dashboard.py --subject-dir curricula/<subject-slug>

    # explicit paths
    python render_dashboard.py \\
        --curriculum 04-resources/<subject-slug>.md \\
        --state 02-progress/_state.json \\
        --out 00-DASHBOARD.html

The CSS is read from this script's sibling ``workspace-styles.css`` unless
``--css`` is given, so the embedded style block is always byte-identical to the
shared sheet (no view-time build, no extra dependency).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

# The four states: weight feeding the overall percent, plus how each one renders.
# Fixed by references/dashboard-format.md; do not change here without changing the spec.
WEIGHT = {
    "solid": Decimal("1.0"),
    "developing": Decimal("0.6"),
    "shaky": Decimal("0.3"),
    "none": Decimal("0"),
}
# status -> (meter fill class, meter width %, pill class, pill text)
RENDER = {
    "solid": ("fill-good", 100, "p-solid", "Solid"),
    "developing": ("fill-acc", 60, "p-dev", "Developing"),
    "shaky": ("fill-warn", 30, "p-shaky", "Shaky"),
    "none": ("fill-none", 0, "p-none", "Not started"),
}
TALLY_ORDER = ["solid", "developing", "shaky", "none"]
ACCENTS = {"cobalt", "teal", "cyan", "indigo", "violet", "slate"}

FONTS = (
    '<link href="https://fonts.googleapis.com/css2?'
    "family=Fraunces:opsz,wght@9..144,400;9..144,600&"
    'family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

# A concept line: "### M3 · The transformer and attention `[ATT][ATTS]`"
CONCEPT_RE = re.compile(r"^###\s+([A-Z]{1,3}\d+)\s+·\s+(.*?)\s*$")
TIER_RE = re.compile(r"^##\s+(.*?)\s*$")
H1_RE = re.compile(r"^#\s+(.*?)\s*$")
TAG_RE = re.compile(r"\s*`[^`]*`\s*$")  # trailing `[SRC]` source tags on a concept title


def parse_curriculum(text: str):
    """Parse a bundled-format curriculum.

    Returns ``(subject, tiers)`` where ``tiers`` is an ordered list of
    ``(tier_label, [(concept_id, title), ...])``. A concept is a
    ``### <ID> · <title> `[tags]` `` line; its tier is the nearest preceding
    ``## `` heading. ``## `` sections that contain no concepts (Sources,
    Recommended path, ...) never appear. Concepts keep curriculum order.
    """
    subject = None
    tiers: list[tuple[str, list[tuple[str, str]]]] = []
    pending_label = "Concepts"
    current: list[tuple[str, str]] | None = None

    for line in text.splitlines():
        if subject is None:
            m = H1_RE.match(line)
            if m:
                subject = re.split(r"\s[–—-]\s", m.group(1), maxsplit=1)[0].strip()
                continue
        m = TIER_RE.match(line)
        if m:
            pending_label = m.group(1).strip()
            current = None  # a tier appears only once a concept lands under it
            continue
        m = CONCEPT_RE.match(line)
        if m:
            cid = m.group(1)
            title = TAG_RE.sub("", m.group(2)).strip()
            if current is None:
                current = []
                tiers.append((pending_label, current))
            current.append((cid, title))

    return subject, tiers


def compute(tiers, state):
    """Fold the curriculum + state into render rows and the headline numbers."""
    concepts = state.get("concepts", {})
    counts = {k: 0 for k in TALLY_ORDER}
    rows_by_tier = []
    flat = []
    for label, items in tiers:
        rows = []
        for cid, title in items:
            info = concepts.get(cid, {})
            status = info.get("status", "none")
            if status not in WEIGHT:
                status = "none"
            counts[status] += 1
            display = info.get("label") or title
            rows.append((cid, display, status))
            flat.append(status)
        rows_by_tier.append((label, rows))

    total = len(flat)
    weighted = sum((WEIGHT[s] for s in flat), Decimal("0"))
    if total:
        pct = int((weighted * 100 / total).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    else:
        pct = 0
    return rows_by_tier, counts, total, weighted, pct


def esc(value) -> str:
    return html.escape(str(value), quote=False)


def render(curriculum_text: str, state: dict, css: str) -> str:
    """Build the full self-contained dashboard HTML string."""
    parsed_subject, tiers = parse_curriculum(curriculum_text)

    subject = state.get("subject") or parsed_subject or "Progress"
    accent = state.get("accent", "cobalt")
    if accent not in ACCENTS:
        accent = "cobalt"
    lang = state.get("language", "en")
    updated = state.get("updated", "")
    slug = state.get("slug") or "<subject-slug>"
    goal = state.get("goal", "")
    floor = state.get("floor", "")
    next_step = state.get("next_step", "")
    pending = state.get("pending")

    rows_by_tier, counts, total, weighted, pct = compute(tiers, state)
    weighted_str = f"{weighted:.1f}"

    # The "Current focus" blurb is human-written and carried in _state.json so it
    # survives regeneration. floor / next_step win; if either is omitted, fall back
    # to derived text (and an optional per-concept focus_note) rather than render
    # an empty block -- never generic stamped prose when the author supplied real text.
    flat_rows = [(cid, disp, st) for _, rows in rows_by_tier for cid, disp, st in rows]
    if not floor:
        proven = [disp for cid, disp, st in flat_rows if st == "solid"]
        floor = "Proven: " + ", ".join(proven) + "." if proven else "Nothing proven yet."
    if not next_step:
        edge = next((r for r in flat_rows if r[2] == "none"), None)
        if edge:
            cid, disp, _ = edge
            note = (state.get("concepts", {}).get(cid) or {}).get("focus_note")
            next_step = f"{cid} · {disp}" + (f" – {note}" if note else "")
        else:
            next_step = "Every concept is in progress or proven."

    out: list[str] = []
    out.append("<!DOCTYPE html>")
    out.append(f'<html lang="{esc(lang)}">')
    out.append("<head>")
    out.append('<meta charset="UTF-8">')
    out.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    out.append(f"<title>{esc(subject)} – progress</title>")
    out.append(FONTS)
    out.append("<style>")
    out.append(css)
    out.append("</style>")
    out.append("<style>")
    out.append("/* dashboard summary layout (artifact-specific; sits below the shared furniture) */")
    out.append(".tally{display:flex;gap:.45rem;flex-wrap:wrap;margin:.55rem 0 .2rem}")
    out.append(".tally .pill{padding:.22rem .6rem}")
    out.append("</style>")
    out.append("</head>")
    out.append(f'<body class="ws" data-accent="{esc(accent)}">')
    out.append("")

    # 1. Overall-progress summary -- always first.
    out.append(f'<p class="kicker">{esc(subject)} · <span class="accent">Progress</span></p>')
    out.append(f"<h1>{pct}% complete</h1>")
    out.append(f'<p class="sub">{weighted_str} of {total} concepts · weighted</p>')
    out.append('<p class="tally">')
    out.append(f'<span class="pill p-solid">{counts["solid"]} Solid</span>')
    out.append(f'<span class="pill p-dev">{counts["developing"]} Developing</span>')
    out.append(f'<span class="pill p-shaky">{counts["shaky"]} Shaky</span>')
    out.append(f'<span class="pill p-none">{counts["none"]} Not started</span>')
    out.append("</p>")
    out.append("")

    # 2. Goal.
    out.append(f'<div class="goal"><b>Goal:</b> {esc(goal)}</div>')
    out.append("")

    # 3. Provenance note + date.
    out.append(
        f'<p class="small">Projected from <code>04-resources/{esc(slug)}.md</code>. '
        f"A concept turns <b>solid</b> only on real evidence – a chat answer or a "
        f"real-world result, never a read lesson. Updated {esc(updated)}.</p>"
    )
    out.append("")

    # 4. Floor & next step.
    floor_html = f"<b>Floor:</b> {esc(floor)} <b>Next:</b> {esc(next_step)}"
    if pending:
        floor_html += f" <b>Pending:</b> lesson {esc(pending)} (delivered, awaiting evidence)."
    out.append(f'<div class="callout"><span class="lbl">Where you are</span>{floor_html}</div>')
    out.append("")

    # 5. Concept rows, grouped by curriculum tier, in curriculum order.
    last = len(rows_by_tier) - 1
    for i, (label, rows) in enumerate(rows_by_tier):
        out.append(f"<h2>{esc(label)}</h2>")
        out.append('<div class="dash">')
        for cid, display, status in rows:
            fill, width, pill_class, pill_text = RENDER[status]
            out.append(
                f'<div class="row"><span class="t"><span class="cid">{esc(cid)}</span> '
                f'{esc(display)}</span><span class="meter">'
                f'<i class="{fill}" style="width:{width}%"></i></span>'
                f'<span class="pill {pill_class}">{pill_text}</span></div>'
            )
        out.append("</div>")
        if i != last:
            out.append("")

    out.append("")
    out.append("</body>")
    out.append("</html>")
    return "\n".join(out) + "\n"


def _resolve_paths(args):
    if args.subject_dir:
        d = Path(args.subject_dir)
        slug = d.name
        curriculum = Path(args.curriculum) if args.curriculum else d / "04-resources" / f"{slug}.md"
        state_path = Path(args.state) if args.state else d / "02-progress" / "_state.json"
        out = Path(args.out) if args.out else d / "00-DASHBOARD.html"
    else:
        if not (args.curriculum and args.state and args.out):
            raise SystemExit("error: provide --subject-dir, or all of --curriculum/--state/--out")
        curriculum = Path(args.curriculum)
        state_path = Path(args.state)
        out = Path(args.out)
        slug = curriculum.stem
    css_path = Path(args.css) if args.css else Path(__file__).resolve().parent / "workspace-styles.css"
    return curriculum, state_path, out, css_path, slug


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Render 00-DASHBOARD.html from a curriculum + _state.json (strictly derived)."
    )
    ap.add_argument("--subject-dir", help="curricula/<slug>/ ; derives curriculum, state and out paths")
    ap.add_argument("--curriculum", help="path to 04-resources/<slug>.md")
    ap.add_argument("--state", help="path to 02-progress/_state.json")
    ap.add_argument("--out", help="path to write 00-DASHBOARD.html")
    ap.add_argument("--css", help="path to workspace-styles.css (default: sibling of this script)")
    args = ap.parse_args(argv)

    curriculum, state_path, out, css_path, slug = _resolve_paths(args)

    curriculum_text = curriculum.read_text(encoding="utf-8")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    css = css_path.read_text(encoding="utf-8").rstrip("\n")
    state["slug"] = slug

    # Strictly derived: a concept the curriculum lacks is never rendered. Warn so a
    # stale ID in _state.json (e.g. after a curriculum revision) is visible, not silent.
    _, tiers = parse_curriculum(curriculum_text)
    curriculum_ids = {cid for _, items in tiers for cid, _ in items}
    extra = sorted(c for c in state.get("concepts", {}) if c not in curriculum_ids)
    if extra:
        print(
            "warning: _state.json has concepts the curriculum lacks (ignored): "
            + ", ".join(extra),
            file=sys.stderr,
        )

    out.write_text(render(curriculum_text, state, css), encoding="utf-8")
    print(f"wrote {out}  ({len(tiers)} tiers, {len(curriculum_ids)} concepts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
