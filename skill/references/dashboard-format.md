# Dashboard format (`00-DASHBOARD.html`)

`00-DASHBOARD.html` is the rendered projection of the curriculum (`04-resources/<subject-slug>.md`) – the one screen that answers "where am I?" at a glance. It is strictly derived: it never shows a concept the curriculum doesn't, and a subject too trivial for a curriculum gets no dashboard. It is built with `assets/workspace-styles.css` and the subject's single accent, like every other artifact, and is **regenerated with `assets/render_dashboard.py`** whenever you write a progress record – never edited by hand (see *Generated, not hand-edited* below).

## Required anatomy, top to bottom

1. **Overall-progress summary – always first, never omitted.** The headline the user scans before anything else: a large **percent complete**, the **weighted concept count** ("24.1 of 36 concepts"), the **tally** by state (solid / developing / shaky / not started), and a **pill row** of those four states. This block is mandatory on every dashboard. A dashboard that opens straight into the goal or the concept rows, with no overall figure, is incomplete – it is the single most common thing to get wrong.
2. **Goal** – the goal restated in one line (`.goal` / `.callout`), so progress is read against the point of it.
3. **Provenance note** – one line: that the map is projected from `04-resources/<subject-slug>.md`, the rule that a concept only turns *solid* on real evidence (a chat answer or real-world result, not a read lesson), and an **Updated YYYY-MM-DD** date.
4. **Floor & next step** – what's proven (the floor) and the single next concept; link the delivered-but-unproven lesson if one is pending.
5. **Concept rows, grouped by curriculum tier** – one `.dash .row` per concept: the concept ID in `.cid` (accent) then its short label · `.meter` · state pill, in curriculum order. Use the shared `.dash .row` grid as-is – its name column is sized to hold a short label without wrapping; don't roll a bespoke grid or a custom ID class.

## The four states (fixed)

Each concept is in exactly one state, shown by its pill and meter fill, and carrying a weight that feeds the overall percent:

| State | Pill · meter fill | Meter width | Weight | Meaning |
| --- | --- | --- | --- | --- |
| Solid | `p-solid` · `fill-good` (green) | 100% | 1.0 | proven on the benchmark's verb, by real evidence |
| Developing | `p-dev` · `fill-acc` (accent) | 60% | 0.6 | taught and practised, not yet proven |
| Shaky | `p-shaky` · `fill-warn` (amber) | 30% | 0.3 | proven once, then stumbled on review |
| Not started | `p-none` · `fill-none` (neutral) | 0% | 0 | not yet taught |

**Overall percent = (Σ weights) ÷ (concept count), rounded.** Example: 19 solid + 7 developing + 3 shaky + 7 not-started over 36 concepts → (19 + 4.2 + 0.9) ÷ 36 = 24.1 / 36 = **67%**. Always show the weighted count next to the percent, so the number is legible rather than magic.

## Generated, not hand-edited

The dashboard is **rendered by a script, never edited by hand.** Hand-editing the dozen scattered spots that have to agree (the headline percent, each meter width, the weighted tally, the pill counts, every concept row, the date) is slow and drifts out of sync. Marking a concept proven is instead **one state change plus one script run.**

`assets/render_dashboard.py` is a pure function of three inputs and nothing else:

1. the curriculum `04-resources/<subject-slug>.md` – concept IDs, titles, tier, and order;
2. `02-progress/_state.json` – each concept's status and the human-written prose;
3. `assets/workspace-styles.css` – embedded verbatim (read from the script's own folder, so the style block is always byte-identical to the shared sheet, with no view-time build and no new dependency).

It computes the weighted count and percent from the table above and writes a self-contained `00-DASHBOARD.html` carrying the full anatomy. Run it with the subject directory, or with explicit paths:

```
python assets/render_dashboard.py --subject-dir curricula/<subject-slug>
```

The anatomy, the four states, the weights, and the percent formula above are the spec this script implements – change them here and in the script together. Two invariants the *author* owns, not the script: a concept turns **solid** only on real evidence (you set that status; the script never infers it), and the map stays **strictly derived** (a status for an ID the curriculum lacks is ignored with a warning, never rendered).

### `_state.json`

One small file per subject, the single source of truth the dashboard is rendered from. The narrative (`goal`, `floor`, `next_step`, and the optional per-concept `focus_note`) lives here so it stays human-written and survives every regeneration – it never degrades into generic stamped text.

```json
{
  "subject": "Subject name",
  "accent": "cobalt",
  "language": "en",
  "updated": "2026-06-25",
  "goal": "One line: why this subject matters – shown in the goal box.",
  "floor": "One line: what's proven.",
  "next_step": "One line: the single next concept and why.",
  "pending": null,
  "concepts": {
    "C1": { "status": "solid", "label": "First concept" },
    "C2": { "status": "none",  "label": "Second concept", "focus_note": "start here next" }
  }
}
```

- `status` is one of `solid` / `developing` / `shaky` / `none` (a concept missing from the file is treated as `none`).
- `label` is the short row label; omit it and the row falls back to the curriculum's concept title. `accent` is one of the six accents (default `cobalt`); `language` sets `<html lang>`.
- `goal` / `floor` / `next_step` are optional but recommended; if `next_step` is omitted the script names the next not-started concept and appends its `focus_note`.
- `pending` is the delivered-but-unproven lesson marker (e.g. `"0007 – second concept"`), surfaced in the floor block; it mirrors the marker in `00-PROFILE.md`.

## Rules

- **Lead with the summary.** The overall-progress block is non-negotiable and comes first. Everything below it is detail.
- **Strictly derived.** Every concept on the dashboard exists in the curriculum, by the same stable ID and in the same order. Re-seed from the curriculum whenever it changes; never hand-place a concept the curriculum doesn't have.
- **Solid means proven.** Only real evidence – a chat answer or a reported real-world result – turns a concept solid, never a delivered-but-unproven lesson. A lesson handed over but awaiting evidence is *developing*, with its pending marker in `00-PROFILE.md`.
- **One accent, fixed semantics.** Same accent as the rest of the subject; the green / amber state colours never change with it.
- **A snapshot, not a report.** Summary, goal, next step, the map – all on a glance. If it reads like prose, it has stopped being a dashboard. It prints cleanly; the user returns to it.
- **Generated, not hand-edited.** Render with `assets/render_dashboard.py` from `02-progress/_state.json`; change state there and re-run, never edit `00-DASHBOARD.html` directly.
