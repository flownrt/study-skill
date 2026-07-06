# Progress record format

Progress records live in `02-progress/` with sequential numbering: `0001-slug.md`, `0002-slug.md`, and so on. Create the directory only when you write the first record.

A progress record captures one thing the user can now demonstrably do, or one piece of prior knowledge they've established. These records are how you decide what to teach next – they mark the floor. Keep them short and decision-grade; they are not a diary.

## Template

```md
# {Short title of what was learned or established}

{One to three sentences: what the user can now do, and why it changes what to
teach next.}
```

That is the entire required format – often a single paragraph. The value is in recording *that* this is now known and *why* it moves the floor, not in filling out fields.

## Optional sections

Add these only when they genuinely earn their place. Most records won't need any.

- **Status** (`active` | `superseded by 0007`) – use when a later, deeper understanding replaces an earlier one.
- **Evidence** – how the user proved it: a question answered cold, an exercise completed, experience cited. Worth noting when the claim might be revisited.
- **Unlocks** – what this makes teachable next, when that isn't obvious.
- **Next review** (`YYYY-MM-DD`) – *only* for subjects whose curriculum opts into per-item spacing (discrete, fast-fading facts like a language's vocabulary or anatomy). One date the tutor surfaces when it comes due, expanding on each success (e.g. 1 day → 3 days → 1 week → 1 month). Most subjects never use this; their retrieval is the scenario review quiz or real-world practice, not a schedule.

## Numbering

Scan `02-progress/` for the highest existing number and add one.

## When to write one

Write a record when any of these is true:

1. **The user proved real understanding of something non-trivial** – not just saw it, but used it correctly. This raises the floor.
2. **The user disclosed prior knowledge** – "I already know X." Record it, with the depth they claim, so you don't re-teach it.
3. **A misconception got corrected** – they believed something wrong and now see why. These are high-value: they predict where related topics will trip them up.
4. **The goal itself shifted** – learning changed what the user cares about. Cross-link to `00-GOAL.md` and update it too.

## What does not qualify

- Material merely covered. Coverage is not learning; wait for evidence.
- A term already defined in the glossary. Don't duplicate it here.
- Session activity logs. These records are insights that change future teaching, not a journal of what happened.

## Superseding

When a newer record contradicts an older one (understanding deepened or got corrected), mark the old one `Status: superseded by NNNN` instead of deleting it. How the user's understanding evolved is itself useful signal.
