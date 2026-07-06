# Lesson interaction design (the in-lesson feedback menu)

Every lesson must make the learner *act* and get feedback, not just read – that is the floor set in `SKILL.md`. This file is the menu of interactions to reach for, organised by what kind of thing is being learned. Its job is to raise the ceiling: so that "build a richer mechanic than a quiz" is a concrete choice rather than a blank page.

Three rules hold across every track:

- **Floor, then ceiling.** Ship at least one interaction per lesson; then reach for the richest one the idea deserves. A concept better *shown* than *tested* gets a built mechanic, not a multiple-choice question.
- **Feedback is not evidence.** Everything in this menu is *learner* feedback – it may reveal its own answers and it stays in the browser. It is separate from the lesson's closing handoff, which carries no answers and routes to chat. Only that handoff (or a reported real-world result) earns a progress record.
- **Match the verb.** Whatever the curriculum's "you've got it when…" benchmark asks – explain, apply, perform – the interaction should rehearse *that* verb, never mere recognition.

The tracks below are chosen by the **concept's** verb, lesson by lesson – not by the subject as a whole. Most subjects borrow from more than one.

## Track A – Knowledge subjects

*The skill is understanding: explaining a mechanism, reasoning with a concept, defending a position. Examples: how LLMs work, a legal doctrine, macroeconomics.*

The learning happens on screen, so the check can too. Reach for, roughly weakest to strongest:

- **Scenario single-choice / multi-choice** – not "what is X?" but "given this situation, which applies?" Mark right/wrong instantly and explain *why* each option is right or wrong. This is the in-lesson check most often lost when quizzes get over-trimmed; it is welcome here.
- **Predict-then-reveal** – make the learner commit to an answer, *then* reveal the result and the reasoning. The forced guess before the payoff is what makes it stick.
- **Manipulable visual** – a slider, toggle, or small simulator where changing an input visibly changes an output (attention weights shifting, a temperature knob reshaping a distribution, a supply curve moving). Showing the mechanism beats describing it.
- **Sort / match / label** – drag concepts into the right buckets, label a diagram, order the steps of a process.

Closing handoff: one open question per distinct idea the lesson taught – usually two or three for a knowledge lesson, one for a single-idea one – each in the benchmark's verb (e.g. "explain why output tokens cost more than input tokens"). Probe what was taught; don't pad to a number.

## Track B – Skills you can simulate in the browser

*The skill is doing something a screen can host: a move, a query, a calculation. Examples: chess, SQL, a snippet of code, reading music, mental arithmetic.*

Don't quiz *about* the skill – build the skill's own surface and let the learner act on it:

- **A live board / canvas** – chess: an interactive board where the learner plays the move and it is checked (a lichess-style position trainer is the model). The board *is* the lesson.
- **A runnable mini-environment** – SQL: a query box over a tiny fixed dataset that runs and shows the result; code: an editable snippet with a "run" that checks the output.
- **Step-through with prediction** – walk a worked example one move at a time, the learner predicting the next step before it is shown.
- **Timed or scored drill** – a short set of positions or queries with immediate scoring, when fluency and speed are the point.

Closing handoff: a "do it and tell me how it went" tied to real practice – e.g. "play three rapid games, paste the one you lost and where you think it turned."

## Track C – Skills that live in the real world

*The skill is embodied or social; a browser can only rehearse it – it is proven by doing it for real. Examples: solving a Rubik's cube in your hands, a yoga pose, a sales call, an instrument.*

The lesson's interactive job is to *rehearse and verify*, then push the learner off-screen:

- **Guided drill / step sequence** – each step written as an action plus an explicit "here's how you know you did it right." Cube: "run the R U R' U' trigger six times; you've got it when your fingers do it without reading the notation."
- **Animated / step-through demonstrator** – a visual that plays the algorithm, pose, or motion the learner is about to copy, scrubbable at their pace. Cube: a move-by-move player or animated net; yoga: an alignment diagram with checkpoints.
- **Self-diagnosis checklist** – turns a real-world rep into something the learner can grade alone: "after the pose, check – knees over ankles? weight in the heels? breath steady?"
- **Between-session assignment** – the real rep, with a concrete target and a report-back: "solve a scrambled cube end to end this week and tell me where you stalled." This is where the skill is actually built; offer a scheduled reminder if they want a rhythm.

Closing handoff: the real-world result reported back. That report *is* the evidence.

## When a lesson would only "tell"

If you cannot find a single interaction for a lesson, the lesson is scoped wrong – too abstract, or trying to cover too much. Split it, or anchor it to a smaller concrete thing the learner can do. A lesson that only tells is not finished.
