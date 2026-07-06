# 04-resources/ format

`04-resources/` holds the curated source material for a subject: its index `resources.md`, the actual files the user provides, and the subject's curriculum `<subject-slug>.md` – the concept map, which is the primary source the tutor teaches from (format: [curriculum-format.md](./curriculum-format.md)). Lessons draw their facts from here, not from unaided recall. Real-world judgment comes from the communities listed here. Better five sharp sources than thirty mediocre ones.

## Structure

```md
# {Subject} resources

## Learn from
- [Course: {title} – {author/institution}]({url})
  {One line: what it covers and when to reach for it.}
- [Paper: {title} – {authors}, {year}]({url})
  {What it establishes; the topics it's the right citation for.}
- Local file: `04-resources/their-syllabus.pdf` (user-provided)
  The user's own syllabus. Use for: grounding the curriculum, sequencing and scoping lessons.

## Practice with (communities)
- [{Forum / subreddit / Discord}]({url})
  {Why it's high-signal; what to use it for – feedback, troubleshooting, critique.}
- Local: {a class, club, or meetup}
  Use for: real-time feedback and the feel you can't get from a screen.
```

## Rules

- **High-trust only.** Prefer primary sources, recognized experts, peer-reviewed work, and well-moderated communities. If something is marketing dressed as teaching, leave it out.
- **User-supplied material ranks first.** A syllabus, document, or transcript the user provides goes at the top of "Learn from" and becomes the backbone of lesson planning.
- **Source files live in the folder.** Save any file the user supplies into `04-resources/` and link it from `resources.md` by relative path; the folder holds both the index and the inputs it points to.
- **The curriculum is the primary source.** The subject's concept map lives here as `<subject-slug>.md` (a bundled curriculum copied in, or one generated/derived) and tops the "Learn from" list; the dashboard projects from it. See [curriculum-format.md](./curriculum-format.md).
- **Annotate every entry.** A bare link is useless in three months. One line: what it covers, when to reach for it.
- **Split learning from practice.** "Learn from" is knowledge; "Practice with" is judgment. A source can sit in just one group.
- **Name the gaps.** If the goal needs an area no good source covers, add a `## Gaps` section listing what is missing. That list drives future searching.
- **Prune without mercy.** A source that turned out shallow, wrong, or off-target gets removed, not buried.
- **Record community preferences.** If the user has opted out of communities, note it here so future sessions stop proposing them.
