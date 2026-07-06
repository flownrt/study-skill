# study

A personal tutor that helps you learn a subject deeply across many sessions. Instead of one-shot answers, `study` builds a persistent workspace on your machine, grounds every lesson in trusted sources and your real goal, and makes you *prove* understanding before moving on – so your learning compounds instead of restarting each time.

## Recommended setup

`study` keeps its workspace as real files on disk and reads them back every session, so it works best where Claude has folder access and can persist work between sessions – **Claude Code** or **Cowork**. The tutoring, curriculum reasoning, and hand-built interactive lessons reward a strong model: **Opus 4.8** with **Max** (or at least **Medium**) reasoning is the recommended default.

## How it works

Each subject gets its own directory:

```
curricula/<subject-slug>/
  00-GOAL.md         # why you're learning this, and what success looks like
  00-PROFILE.md      # your preferences and the tutor's working notes
  00-DASHBOARD.html  # live projection of the curriculum (solid / developing / shaky / not started)
  01-lessons/        # numbered, self-contained interactive HTML lessons
  02-progress/       # short dated records of what you can now demonstrably do
  03-references/     # distilled glossaries, syntax cards, routines for quick lookup
  04-resources/      # sources you learn from + the curriculum <subject-slug>.md (the concept map)
```

On every session the tutor reads this state first, so a returning learner is recognized rather than re-onboarded. For all but the narrowest subjects it first lays out a **curriculum** (`04-resources/<subject-slug>.md`) – a source-grounded map of what to learn and in what order – then teaches at your *learning edge*, taking the next step from that map and the floor of what you've already proven (`02-progress/`), with spaced review to keep it from fading. `00-DASHBOARD.html` renders the curriculum as an at-a-glance map of every concept as solid, developing, shaky, or not started, and updates as you make progress.

## Bundled starter curricula

`study` ships with three ready-made curricula in [`assets/curricula/`](./assets/curricula), built from vetted sources and deliberately different in shape:

- **[`llm-architecture.md`](./assets/curricula/llm-architecture.md)** – a three-tier *fluency map* (Mechanics → Build craft → Open debates) for understanding how large language models actually work, for someone who needs to hold their own in technical discussions. *Knowledge-heavy*: concepts to understand, each with a self-check.
- **[`practical-ai.md`](./assets/curricula/practical-ai.md)** – a model-agnostic *competency ladder* for getting real work done with AI (prompt well → trust but verify → work with it → build agentic workflows). *Skills-heavy*: each rung has a "try it now" drill, and it teaches durable principles rather than today's product names.
- **[`chess.md`](./assets/curricula/chess.md)** – a *competency ladder* (board safety → tactics → endgames & planning) from "knows the moves" to solid intermediate. *Skills-heavy*: each rung is a thing you must be able to *do*, paired with a drill and an observable "you've got it when…" benchmark.

One is a map of ideas, the other two are ladders of abilities (a classic skill, and working with AI itself) – together they show the same teaching engine handles both knowledge-led and practice-led subjects. Bring your own curriculum and it takes priority over any bundled one.

## Reference formats

The conventions the tutor follows for each workspace file live in [`references/`](./references): [`goal-format.md`](./references/goal-format.md), [`curriculum-format.md`](./references/curriculum-format.md), [`resources-format.md`](./references/resources-format.md), and [`progress-format.md`](./references/progress-format.md). How a lesson picks its in-lesson interaction – by subject type – lives in [`lesson-design.md`](./references/lesson-design.md), and the dashboard's required shape – led by an overall-progress summary – in [`dashboard-format.md`](./references/dashboard-format.md).

## Install

Make the skill available to Claude in one of two ways:

1. **As a folder** – copy this `study/` directory into your Claude skills directory.
2. **As a bundle** – zip the folder into a `study.skill` archive and install it through the Claude app's skill installer.

No build step is required – a skill is just `SKILL.md` (YAML frontmatter + instructions) plus the supporting files it references.

## License

Licensed under the [Apache License, Version 2.0](../../LICENSE).
