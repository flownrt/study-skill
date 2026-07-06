# study

**A personal tutor that actually remembers** – an Agent Skill for Claude Code and Cowork.

> ▶ **[Try the live demo](https://flownrt.github.io/study-skill/)** – two sample lessons and the live progress dashboard from an *LLM architecture* curriculum, all produced by the skill.

Most AI help disappears when you close the tab. `study` builds a real learning workspace on your machine – a goal, trusted sources, hand-built interactive lessons, and an evidence-based progress map – so every session continues the last instead of starting from zero.

## What makes it a tutor, not a chatbot

- **Persistent.** Each subject is a folder – goal, sources, lessons, progress, cheat sheets. Close the tab and nothing is lost; the next session reads it back.
- **Grounded.** Lessons cite trusted sources instead of leaning on model memory.
- **Proven, not just read.** You demonstrate a concept in chat before it counts; the dashboard only turns green on real evidence.
- **Interactive.** Every lesson is a hand-built page with something to *do*, not a wall of text.
- **At your edge.** It teaches the next thing just past what you've proven, with spaced review so it sticks.

Ships with starter curricula for LLM architecture, chess, and practical AI. Bring your own and it takes priority.

## Install

```text
/plugin marketplace add flownrt/skills
/plugin install study@skills
```

No marketplace? Download [`study.skill`](https://flownrt.github.io/study-skill/study.skill) and install it via the Claude app's skill installer, or copy the [`skill/`](./skill) folder into your Claude skills directory.

Works best where Claude has folder access and persists files between sessions – Claude Code or Cowork – on Opus with extended reasoning.

## In this repo

- [`skill/`](./skill) – the skill itself (`SKILL.md` + assets + references), install-able as a folder.
- `index.html` + [`demo/`](./demo) – the landing page and its live demo artifacts (two sample lessons + a rendered dashboard).
- `study.skill` – the downloadable bundle.

## About

Part of [**skills**](https://github.com/flownrt/skills), a curated collection of general-purpose Agent Skills. This repo is a standalone mirror of `study`, kept in sync from the collection. Licensed under [Apache-2.0](./LICENSE).
