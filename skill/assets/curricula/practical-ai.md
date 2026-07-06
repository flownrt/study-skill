# Practical AI – a competency ladder

### For anyone who wants to get real work done with AI – from first prompts to building agentic workflows

AI is a **skill, not just a tool**. Access is nearly universal, so the differentiator is no longer *whether* you use AI but *how well* – and that skill compounds. This is a ladder of things you must be able to *do*, each verified by use; every rung pairs a concept with a "try it now" drill and an observable "you've got it when…" benchmark.

A useful mental image: AI is a *motorcycle for the mind* – enormous power, but someone still has to steer, accelerate, and brake. It is superb at pattern-matching, synthesis, and well-trodden tasks, and weak at embodied judgment, one-shot learning, and big creative leaps. The rider who understands what's under the hood gets more out of it than the one reciting incantations.

**Model-agnostic by design.** Models, products, prices, and names change every few months; this ladder teaches the durable principles and names current tools only as examples. Where something is tied to today's tools it's marked *(time-bound)* – re-test the specifics against whatever is current when you read this. The habits in the practice engine (especially `H4`) are what keep you current.

**Sourcing.** Each rung is tagged with where its guidance comes from.

| Tag | Source |
| --- | --- |
| `[ANTH]` | Anthropic docs & engineering – prompting, building effective agents, Agent Skills, Claude Code |
| `[OAI]` | OpenAI docs – prompting guides, Codex agent |
| `[FW]` | Field notes by Florian Wienert, this repository's author – practitioner principles for agentic workflows |
| `[GEN]` | general, widely-taught practice |

**How the tiers work.** Tier 1 is talking to the model so it actually helps. Tier 2 is not getting burned – verifying and protecting yourself. Tier 3 is folding AI into your real work. Tier 4 is the frontier: building repeatable, safe **agentic workflows** and a lean library of them. The practice engine runs underneath all four.

---

## Tier 1 – Prompt it well

### P1 · Say exactly what you want `[GEN][FW]`
Most disappointing answers come from a vague ask, not a weak model. A reliable scaffold: **objective** (the end goal in one sentence), **context** (background, audience, purpose), **constraints** (tone, length, what must not change), and **output format** (the exact structure you want back). **Try it now:** take a one-line request and rewrite it with those four parts; compare the answers. **Got it when:** your first attempt usually lands without three rounds of clarification.

### P2 · Give it the context it needs `[FW][GEN]`
The model resolves meaning from the words around it – give it clear context and it decides well, starve it and it guesses. Context clarity, not clever phrasing, explains most of why one prompt works and a near-identical one fails. Paste the real material instead of describing it, and for any structured output show 3–5 examples of what you want. **Try it now:** redo a task by attaching the real document and a couple of worked examples. **Got it when:** you stop getting generic answers, because you stopped giving generic prompts.

### P3 · Steer by iterating `[GEN]`
Treat it as a conversation: correct, constrain, ask for alternatives or a critique – don't restart from scratch. A handy habit is to pick a **mode** up front: *clarify* (ask questions first, for ambiguous or sensitive work), *plan* (propose steps and wait for approval, for complex work), or *auto* (just complete well-bounded, low-risk work and report what changed). **Try it now:** drive one mediocre first draft to a good answer over three follow-ups. **Got it when:** you can rescue a weak first answer by steering instead of re-prompting.

### P4 · Make it show its work – when it helps `[GEN][FW]`
For math, logic, multi-step analysis, or debugging, ask the model to think step by step: generating intermediate steps constrains the final answer and measurably improves accuracy. Skip it for simple questions, where it only inflates cost and latency – and note that modern reasoning models already do this internally, so heavy "think step by step" scaffolding is mostly redundant for them and just adds cost. **Try it now:** take one reasoning task and compare an answer-only prompt with a step-by-step one. **Got it when:** you know when stepwise reasoning earns its cost and when it's just noise.

### P5 · Know the edge `[GEN][FW]`
Current models are unreliable at exact arithmetic and counting, very recent or niche facts, perfect consistency over long documents, and anything needing private or live data they don't have. The edge moves, so probe it rather than assuming. **Try it now:** find one task this month's model fails at, and one it surprises you on. **Got it when:** you can usually predict, before asking, whether the model will be reliable for a task.

---

## Tier 2 – Trust but verify

### V1 · Hallucination is structural, not a bug `[FW][GEN]`
The model predicts likely text, and confident-sounding wording exists for both facts and fiction – so it produces both with equal confidence. (Fabricated citations – invented authors, titles, even URLs – are a well-documented failure mode.) This won't be "patched away"; it falls out of how next-token prediction works. Verify anything load-bearing, use low temperature for factual work, and ask the model to flag what it isn't sure of. **Try it now:** ask for three specific facts you can check, and check them. **Got it when:** you never put an unverified AI claim into something that matters.

### V2 · Demand sources and check them `[FW][GEN]`
Ask for citations and actually open them; for research, build in **multi-source cross-checking** and ask the model to flag where sources conflict rather than silently smoothing it over. A cited source can still be invented or misread. **Try it now:** ask a research question, then confirm every cited source exists and says what was claimed. **Got it when:** you've caught at least one fabricated or misquoted citation.

### V3 · Ask for its confidence `[FW]`
Make the uncertainty that already exists *visible*: ask the model to label claims **high / medium / low / speculative**, and to weigh competing answers before settling on one. You're not adding doubt – you're surfacing it so you know what to double-check first. **Try it now:** re-run a recent answer asking for a confidence label on each claim and one alternative hypothesis. **Got it when:** you triage what to verify by confidence instead of trusting fluency.

### V4 · Mind privacy and data hygiene `[GEN]`
Don't paste secrets, personal data, or confidential material into tools that may retain or train on it. Know the tool's data settings and any rules that apply to you. A quick test: would you be comfortable emailing this to a stranger? **Try it now:** before your next paste, decide what to redact or abstract. **Got it when:** sanitising sensitive inputs is automatic, not an afterthought.

### V5 · Keep a human in the loop `[GEN][FW]`
For consequential or irreversible actions – sending, publishing, deleting, spending, or any legal, medical, or financial decision – the model drafts and *you* decide. **Try it now:** write down which actions you will never let an AI take unsupervised. **Got it when:** you have explicit gates rather than a vague sense of caution.

---

## Tier 3 – Work with it

### W1 · Match the tool and model to the task `[GEN][OAI]`
Use fast, cheap models for quick or bulk work; deep reasoning models for genuinely hard problems; multimodal models for images, audio, or screenshots; search-enabled tools for current facts. The trade-off is always capability vs. cost vs. latency – and the names change, so judge by fit, not brand. **Try it now:** run the same task on a quick model and a reasoning model; note where the extra cost earns its keep. **Got it when:** you choose deliberately instead of defaulting to one tool for everything.

### W2 · Put the right things in its working memory `[FW][GEN]`
The context window is the model's working memory – but more is not better. In long windows attention *dilutes*: the model attends strongly to the start and end and skims the middle ("lost in the middle"), then fills gaps with plausible guesses. Give it the relevant material, not everything; signal-to-noise in the window determines output quality, not raw token count. **Try it now:** do a task with curated, relevant excerpts instead of dumping a whole file. **Got it when:** your results are specific and accurate rather than generic or padded with invention.

### W3 · Ground answers in your own documents `[FW][GEN]`
Two ways to work over your material: **long context** (put it all in the prompt – best for bounded data and reasoning *across* documents) versus **retrieval / RAG** (search and inject only the relevant chunks – best for large, dynamic, or auditable corpora). Both reduce hallucination by grounding answers in real sources. Zero-code options exist *(time-bound examples: notebook/project tools such as NotebookLM or Claude Projects)*. **Try it now:** load a document set into a grounding tool and ask questions that demand citations. **Got it when:** you can pick long-context vs. retrieval for a given job and say why.

### W4 · The everyday workflows `[GEN]`
The bread and butter: drafting and editing, research and summarisation, analysing data or documents, coding assistance, brainstorming and critique. Use AI as a tireless first-drafter and a second pair of eyes – not an oracle. **Try it now:** pick one recurring task and run it end-to-end through AI this week. **Got it when:** at least one weekly task is meaningfully faster or better.

### W5 · Stop re-typing – save what works `[ANTH][OAI]`
Save the prompts that work, set custom instructions, use projects or custom assistants. Capturing what works so you don't reinvent it each time is the on-ramp to Tier 4. **Try it now:** turn your single best one-off prompt into a saved, reusable template. **Got it when:** you have a small personal library you actually reach for.

---

## Tier 4 – Build agentic workflows

*The frontier of what current tools do best, and the fastest-moving part of this ladder. It covers: when an agent is worth building at all, giving it tools and your data, building from your agent tool's native primitives, packaging repeatable work as skills (and keeping the library lean), separating roles, defining "done" and verifying with fresh eyes, chaining steps reliably, automating it safely, staying model-agnostic, and improving it from real failures – which, taken together, is how you engineer an agent's **harness**: the scaffolding around the model that turns it into something reliable. Treat the tool names as time-bound examples; the patterns are what last.*

### A1 · Chat vs. agent, and the loop `[ANTH][GEN]`
An agent is a model in a **loop**: it gathers context, takes an action through a tool, checks the result, and repeats until done. Reach for an agent only when a task genuinely needs several steps and tool use; otherwise a plain prompt or an ordinary script is better. And use the **least machinery that works** – prompt → saved skill → script → single agent → multi-agent – because each step up adds capability *and* failure surface, latency, and cost; anything that must be exact (arithmetic, sorting, validation, branching) belongs in code, not the model. **Try it now:** take a multi-step task, mark where it must *act*, and find the simplest rung that solves it. **Got it when:** you can tell before building whether a task even needs an agent.

### A2 · Give it tools and your data `[ANTH][OAI]`
An agent earns its keep by acting on real systems – files, the web, your apps and data. The common way to connect those is an open, vendor-neutral standard (the Model Context Protocol); products usually surface it as "connectors" or tool integrations *(time-bound examples: desktop assistants like Cowork, coding agents like Claude Code and Codex, IDE agents)*. Give it the *fewest* tools the job needs – every extra tool is more to go wrong and more to secure. **Try it now:** connect one tool or data source and have the agent use it on a real task. **Got it when:** your agent does something with your actual data, not just talk about it.

### A3 · Build from your tool's native primitives `[FW][ANTH]`
This is how you *actually* build a workflow today – not a separate automation product, but the composable parts your agent tool already gives you. In a tool like Claude Code or Cowork the pieces are: a **project memory file** the agent reads every session (conventions, commands, context); **skills** – a procedure or domain knowledge written once and invoked by name or automatically; **subagents** – isolated workers with their own context and tools, for parallel or context-heavy subtasks; **slash commands** – on-demand triggers for a workflow you control; **hooks** – code that fires at set points (before/after a tool, on session start) to enforce a rule or run a check; and **plugins** – a bundle of these you install in one click and share. The rule of thumb: a command for a prompt template, a skill for real logic or helper files, a subagent for isolated or parallel work, a hook to enforce a rule in code. You build a workflow by composing these, not by re-typing instructions each time. *(Time-bound: this is the Claude Code / Cowork shape in 2026; Codex and other tools expose similar pieces.)* **Try it now:** rebuild one manual routine from these parts – e.g. a project memory file plus one skill it triggers. **Got it when:** your workflow runs from named, reusable parts instead of a fresh paragraph of instructions every time.

### A4 · Capture repeatable work as skills – and keep the library lean `[FW][ANTH]`
Write a repeatable workflow down **once** as a reusable skill (instructions plus any helper files), and collect your skills into a **repository** you reuse and share (→ A3). The discipline that matters here is *not over-building the repository*: before you create a skill, ask whether it should be one at all – one-off tasks belong in chat; skills are for work that is repeated, context-heavy, and needs consistent standards. Keep each skill small, single-purpose, and clearly named, prune what you don't use, and resist elaborate structure you don't need yet. Many sharp little skills beat one sprawling mega-prompt. **Try it now:** take one workflow you repeat, decide whether it earns a skill, and if so write the smallest version that works. **Got it when:** you reach for skills you wrote weeks ago, and the library stays lean instead of sprawling.

### A5 · Separate the roles: plan, build, check `[FW][ANTH]`
For anything beyond a single step, split the work by role instead of asking one agent to do everything: a **planner** that decides what "done" means and sequences the work (use a plan-first mode so it doesn't rush in and solve the wrong problem), **workers** that each implement one piece from a *clean* context, and **checkers** that verify. This is the orchestrator (or "operator") pattern – one brain directs, specialists execute. Seat the right model in each role, too: planning rewards careful reasoning, implementation rewards fast fluency, checking rewards precise instruction-following, and no single model wins all three. **Try it now:** take a multi-step job and assign each part to a plan / build / check role. **Got it when:** no single context is planning, building, and judging the same work at once.

### A6 · Define "done" first, then verify with fresh, adversarial eyes `[FW][GEN]`
Write the success criteria **before** building – a checklist of what must be true, independent of how it's implemented. (Tests written *after* the fact tend to confirm the code rather than catch its mistakes.) Then have the checking done by a **fresh context with no memory of building it** – a separate subagent, ideally a different model, that sees only the request, the plan, and the output, so it can't rationalise choices it never made. Make it **show evidence** – the command it ran and what came back – rather than just asserting success, and cap rework at a few targeted cycles. **Try it now:** for one task, write the "done" checklist up front, then open a *fresh* chat or subagent to review the result against it. **Got it when:** the fresh-eyes check catches things the builder confidently missed.

### A7 · Chain reliably: write state down `[FW][GEN]`
Across steps, don't trust the agent to *remember* – force an explicit handoff at each transition: what's done, what's left, what was run and its result, any open issues. Reliability over long runs comes from legible written state, not memory. **Serialise** the steps that change things (parallel writers collide and make inconsistent decisions) but **parallelise** read-only work like searching, research, and review (a "split-and-merge" of independent subtasks). Decompose so each step fits comfortably in one context window, and keep a verification gate between stages – a 95%-reliable step run ten times only finishes about 60% of the time, so prefer fewer, fatter, checked steps. **Try it now:** split a workflow into stages with a written handoff and a check between each. **Got it when:** it fails loudly at a checkpoint instead of silently producing garbage at the end.

### A8 · Make it run on its own – and on rails `[FW][ANTH]`
Turn a workflow you run by hand into one that runs itself. The native path is your agent tool's own triggers: a **slash command** or **hook** to fire it, a **scheduled task** to run it on a cadence, or a **headless** run invoked from a script or CI – with dedicated automation platforms (e.g. n8n) as just one option, not the default. Because **human attention is the real bottleneck**, design autonomous runs to surface only the decisions that actually need you. Autonomy demands guardrails: give it the least permissions it needs, sandbox it, require approval for irreversible actions, keep a kill switch, and watch for **prompt injection** – untrusted input (a web page, an email) carrying hidden instructions; the dangerous "lethal trifecta" is untrusted input + tool access + sensitive data in one place. Automate only what you've already run by hand and trust. **Try it now:** take a workflow you trust and put it behind a command or schedule, then list what it may do autonomously vs. what needs your sign-off. **Got it when:** something useful happens without you starting it, and you'd notice and could stop it.

### A9 · Keep it model-agnostic so it improves on its own `[FW][ANTH]`
Put the orchestration logic in **prompts and skills, not hard-coded state machines** that bake in today's model behaviour – then a better model makes the same workflow better without a rewrite, with code left only for thin bookkeeping. The test of a durable agentic design: does it get better *passively* as models improve? Strong structure also lets weaker or open models punch above their weight, so you're never locked to one provider's ceiling. **Try it now:** express one workflow's logic entirely in text and skills, with code only for bookkeeping. **Got it when:** dropping in a better model improves the output with no structural change.

### A10 · Evaluate and iterate `[FW][GEN]`
Treat building a workflow as a loop of its own: test on real cases, watch where it fails, fix one thing, and version your prompts and skills as you go. Have it show its evidence so reviewing is faster than re-doing the work, and don't trust a workflow you haven't watched fail and recover. **Try it now:** collect five real inputs, run your workflow, log the failures, and fix the most common one. **Got it when:** you improve the workflow from evidence rather than from vibes.

### A11 · Engineer the harness, not the model `[ANTH][FW][GEN]`
Step back and name what the rungs above add up to: a **harness**. The working equation is *agent = model + harness*, where the harness is everything around the model – the loop (A1), its tools and your data (A2–A3), the roles and orchestration (A5), the verification (A6), the written state and memory (A7), and the control limits and guardrails (A8). The model supplies the intelligence; the harness supplies the reliability – and the model is the *smallest* part of a working agent system. So the engineering that separates a toy demo from something production-worthy is **harness engineering**, not prompt-tweaking or chasing the latest model: invest in better context, cleaner tools, tighter validation, and clearer stop conditions. Kept model-agnostic (A9), a good harness improves on its own every time the model does. **Try it now:** for one workflow, list its harness parts – loop, tools, context, memory, control, safety – and improve the single weakest one. **Got it when:** your first instinct on a flaky agent is to strengthen the harness around the model, not just reword the prompt.

---

## The practice engine (runs under every tier)

These habits are where the rungs above actually get climbed.

### H1 · Use it daily on real work `[GEN]`
Judgment about what AI is good and bad at comes only from real tasks. Toy prompts teach nothing; your actual work teaches everything.

### H2 · Keep a lean prompt and skill library `[FW][ANTH]`
Your growing **workflow repository**. Save what works, reuse it, refine it – and prune it, so it stays a sharp toolkit rather than a junk drawer (→ A4).

### H3 · Review your failures `[GEN]`
When AI gets something wrong, work out *why* – a vague prompt, missing context, the wrong tool, or a genuine limit. Failures are the syllabus.

### H4 · Re-test your assumptions `[GEN][FW]`
Capabilities, tools, and prices shift fast. What a model couldn't do last quarter it may do now – re-probe the edge instead of trusting old beliefs. This habit is what keeps the rest of the ladder from going stale.

---

## Recommended path

1. **P1, P2 + H1** – clear prompting with real context, used daily; add **P3–P5** (steering, step-by-step, knowing the edge) as you go. This is most of the everyday gain.
2. **V1, V2** – verification, straight away; never let unchecked output do real work.
3. **W1–W5** – fold AI into your actual workflows, ground it in your own materials, and start saving what works.
4. **A1–A3** – your first real agentic workflow: decide it needs an agent, connect one tool/source, and build it from native primitives (a memory file plus one skill).
5. **A4–A7 + V3, V5** – for serious multi-step work: keep the library lean, separate roles, define "done" and verify with fresh eyes, and chain reliably with written handoffs.
6. **A8–A11 + V4** – automate it safely, keep it model-agnostic, improve it from real failures, and recognise the whole thing as a harness you engineer.

Run the **practice engine** (H1–H4) the entire time, from day one.

**You're fluent when** you (a) get useful results on the first or second try, (b) reflexively verify what matters and protect sensitive data, (c) keep a lean library of reusable prompts and skills you actually use, and (d) can build a simple, safe, multi-step agentic workflow from your tool's own parts – with separated roles, a "done" checklist, and fresh-eyes verification – and improve it from its own failures – in short, you engineer the harness, not just the prompt. The frontier keeps moving; `H4` is how you stay on it.

---

**Credits.** Portions of this curriculum – especially Tier 4 and the verification practices – draw on field notes by **Florian Wienert**, this repository's author (tagged `[FW]`).
