# 00-GOAL.md format

`00-GOAL.md` sits at the root of the subject directory. It records *why* the user is learning this subject and what success actually looks like. Every later decision – what to teach next, which source to reach for, which exercise to set – should be traceable back to this file.

## Template

```md
# Goal: {Subject}

## Why
{One to three sentences. The concrete, real-world reason the user is doing this.
What changes in their work or life once they can do it? Resist abstract framings
like "to understand {subject}" – name the underlying outcome.}

## Success looks like
- {A specific, observable thing the user will be able to do}
- {Another observable capability}
- {…}

## Constraints
- {Time available, budget, deadlines, prior commitments, learning preferences –
  anything that shapes the approach}

## Out of scope
- {Adjacent things the user is deliberately not chasing right now. Protects focus
  and keeps lessons from sprawling.}
```

## Rules

- **One goal per subject directory.** Two unrelated aims means two directories.
- **Concrete beats abstract.** "Play a 15-minute club game without hanging a piece" beats "get good at chess." "Ship a CLI my team installs" beats "learn Rust."
- **Refuse to write a vague goal.** If the user can't say why, interview them first. A misleading goal steers every future session wrong – worse than having none yet.
- **Update it when reality moves.** Aims shift as people learn. When the user's target changes, rewrite this file rather than leaving a stale one in place.
- **Keep it to a screen.** Once the goal reads like a project plan, it has stopped being a compass. Short enough to reread in ten seconds.
