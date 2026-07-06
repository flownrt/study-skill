# Curriculum format (`04-resources/<subject-slug>.md`)

The curriculum lives at `04-resources/<subject-slug>.md` (named for the subject), among the sources it is grounded in. It is the subject's concept map: what the subject is made of, grouped and ordered, so the tutor can sequence lessons deliberately and `00-DASHBOARD.html` has something to project. Build it for any non-trivial subject, grounded in the rest of `04-resources/` – never in unaided recall. If a bundled or user-supplied curriculum already exists, that file *is* the curriculum (adopt it, keep its IDs) – don't generate a second one.

The golden rule: **the curriculum names, orders, and benchmarks concepts; it never explains them.** Each entry is a pointer, not a lesson – the explanation is written, and source-verified, only when that concept is taught. Putting teaching content here would duplicate the lessons and reintroduce the ungrounded, from-memory prose the skill forbids.

## Template

```md
# {Subject} – {one-line aim, tied to 00-GOAL.md}

{1–2 sentences: what fluency or competence in this subject looks like.}

## Sources
| Tag | Source (in 04-resources/) |
| --- | --- |
| `[S1]` | {the first key source} |
| `[S2]` | {…} |

## {Group / Tier 1 – short label}
- **C1 · {concept}** `[S1]` – depends on: none · you've got it when: {observable, verb-based}.
- **C2 · {concept}** `[S1][S2]` – depends on: C1 · you've got it when: {…}.

## {Group / Tier 2 – short label}
- **C3 · {concept}** `[S2]` – depends on: C1 · you've got it when: {…}.

## Recommended path
{The order to teach in, e.g. C1 → C2 → C3, with any branch notes.}
```

## Rules

- **A map, not a book.** Name, place, and benchmark each concept; never write its explanation here. If an entry needs paragraphs, that content is a lesson.
- **Ground the structure.** Concepts and their order come from `04-resources/` – a user's syllabus, a bundled curriculum, or verified research – not from recall. For specialized or fast-moving fields, let the source's own structure drive the order.
- **Stable IDs.** Give each concept a short, stable ID (`C1`, `M3`, …). Progress records and the dashboard refer to concepts by these IDs, so don't renumber on a whim.
- **One benchmark per concept, in a verb.** "Explain…", "apply…", "argue the counter-case", "perform…" – never mere recognition. This is the proof a lesson must reach, and what the dashboard scores.
- **Provisional by design.** The map is a working hypothesis. When a lesson exposes a missing or misplaced concept, or `00-GOAL.md` shifts, revise it – then re-seed `00-DASHBOARD.html` from it.
- **Source precedence.** A curriculum the user supplies outranks a bundled one, which outranks one you generate. Note which it is.
- **Keep it scannable.** One line per concept; a screenful you can take in at a glance, like the bundled curricula in `assets/curricula/`.
