# LLM Architecture – a fluency map

### For someone who needs to reason about, design, and defend LLM systems in technical discussions

This is a tiered map of the concepts that let you hold your own when people argue about how large language models work and how to build with them. The goal is not to train a model from scratch – it is **fluency**: being able to explain each idea plainly, name the design decision it governs, and state the strongest objection to the mainstream take.

**Sourcing.** Each concept is tagged with where its claims come from, so a lesson can cite rather than assert. The map is built from a deliberately broad base – primary research, official lab documentation, respected practitioner explainers, and first-hand interviews with people building frontier systems – cross-checked against general engineering practice. It is not single-sourced.

| Tag | Source |
| --- | --- |
| `[ATT]` | Vaswani et al., *Attention Is All You Need* (2017) – the transformer |
| `[CHIN]` | Hoffmann et al., *Training Compute-Optimal LLMs* (2022) – "Chinchilla" scaling |
| `[MOE]` | *A Survey on Mixture of Experts in LLMs* (TKDE, 2025) |
| `[ATTS]` | *Efficient Attention Mechanisms for LLMs: A Survey* (2025) |
| `[INFE]` | *Inference Economics of Language Models* (2025) |
| `[SYS]` | *The New LLM Bottleneck: Latent Attention and Mixture-of-Experts* (2025) |
| `[DOC]` | Official lab documentation (Anthropic, OpenAI, Google DeepMind) – e.g. prompt caching, context engineering, building agents |
| `[KAR]` | Andrej Karpathy – *Neural Networks: Zero to Hero*, *Deep Dive into LLMs*, public talks |
| `[EXP]` | Practitioner explainers – Cameron R. Wolfe, Maarten Grootendorst's visual guides |
| `[SCALE]` | *How to Scale Your Model* (jax-ml) – systems view of scaling, batching, and the roofline |
| `[INT]` | First-hand interviews with frontier builders (research, inference, hardware) |
| `[GEN]` | General, widely-held engineering practice |

**How the tiers work.** Tier 1 is how the machine works under the hood – skip it and every higher conversation is cargo cult. Tier 2 is the working vocabulary of building LLM systems. Tier 3 is the set of open debates experts reference constantly; you don't need to settle them, but you must recognize them and know the canonical positions.

---

## Tier 1 – Mechanics

### M1 · Pretraining and next-token prediction `[KAR][ATT]`
A base model is made by predicting the next token across an enormous corpus of text. The thing to internalize: this single objective does two jobs at once – it stores knowledge *and* it grows general capability, because predicting the next token well forces the model to build reusable internal machinery for grammar, facts, reasoning, and style. That is why "it's just autocomplete" is a weak argument: the prediction target is the *means*, not the ceiling. Everything else in the stack is built on top of these pretrained representations.

### M2 · Tokens and tokenization `[GEN]`
Models don't see characters or words; they see **tokens** – subword chunks, very roughly three-quarters of an English word each. Three consequences you'll use constantly: pricing and context limits are counted in tokens; non-English text and dense boilerplate tokenize less efficiently (so they cost more and fill the window faster); and character-level tasks (counting letters, exact string surgery) are unreliable because the model literally can't see the characters. The token is the unit of cost, latency, and capacity in every later discussion.

### M3 · The transformer and attention `[ATT][ATTS]`
The transformer moves tokens through stacked layers of **attention** (each token can look back at every earlier token) and feed-forward blocks, glued together by residual connections. Attention itself is order-blind – it sees a *set* of tokens, not a sequence – so position has to be injected explicitly, first through added **positional encodings** and in modern models through **rotary embeddings (RoPE)** applied inside attention. You don't need to derive backpropagation, but you should be able to say where the cost lives: attention compute grows *quadratically* with sequence length, while the per-token memory you must retain grows *linearly*. That asymmetry is the seed of nearly every long-context and inference-cost problem downstream.

### M4 · Context window and the KV cache `[KAR][INFE]`
The cleanest mental model: the **weights** are long-term memory – everything the model absorbed in training, recalled hazily; the **context window** is working memory – whatever is in front of it right now, available at full fidelity. The **KV cache** is the physical implementation of working memory: the per-token state kept around so the model doesn't recompute the whole context for each new token. Because each conversation's cache is unique, it can't be shared across users, which makes it the hard bottleneck of long context. This one idea is why putting the right material *in the context* usually beats hoping the weights "know" it.

### M5 · In-context learning `[KAR][GEN]`
Models adapt to patterns *inside the prompt* – examples, format, terminology – without any change to their weights. This capacity wasn't designed in; it emerged from pretraining. Architecturally it's the cheapest adaptation lever you have, and it's the reason prompt and context design is real engineering rather than superstition: you're programming the model's behavior at runtime through its working memory.

### M6 · Embeddings and representations `[KAR][EXP]`
Embeddings are vectors that place text in a space where *meaning* becomes *distance* – similar things land near each other. They're the basis of semantic search and retrieval (→ C2). The deeper point: rich internal representations are the asset that makes everything else possible. The modern stack works largely because it inherits strong representations from pretraining instead of having to learn them from scratch for each task.

### M7 · Parameters, sparsity, and Mixture-of-Experts `[MOE][SYS][EXP]`
"Model size" splits into *total* and *active* parameters. A **Mixture-of-Experts (MoE)** model routes each token through only a few of its many expert sub-networks, so a very large model activates just a fraction of itself per token – more capacity for a given compute budget, which pays off mainly at high serving volume. The fluency check: you can explain why "how many parameters does it have?" is an ill-posed question for a modern frontier model, and why sparsity is an economics decision as much as an architecture one.

### M8 · Sampling, temperature, and nondeterminism `[GEN]`
A model emits a probability distribution over the next token; **sampling** (temperature, top-p) decides how to pick from it. This is why the same prompt yields different outputs, why even temperature 0 isn't perfectly deterministic on real serving stacks (batching and floating-point quirks), and why every workflow must be designed for output *variance* rather than assuming a fixed answer. Variance is the root cause behind both evaluation methodology (→ C6) and reliability patterns (→ C13).

### M9 · Post-training: SFT, RLHF, RLVR `[KAR][INT][GEN]`
After pretraining, a base model is shaped into an assistant. **SFT** (supervised fine-tuning on curated demonstrations) installs the assistant persona and format. **RLHF** optimizes against a learned model of human preference. **RLVR** (reinforcement learning from *verifiable* rewards – math, code, passing tests) drives today's reasoning models. Fluency means knowing which behavior comes from which stage: knowledge is from pretraining; tone, refusals, and formatting are from post-training. Know the failure modes too – reward hacking, sycophancy, and judges that can be gamed (→ D4).

### M10 · Scaling laws, Chinchilla, and over-training `[CHIN][INT]`
Scaling laws say loss falls predictably as you add compute, parameters, and data. "Chinchilla-optimal" is the classic compute-optimal ratio of data to model size – and frontier models now *deliberately* break it. The reason is serving: a smaller model trained on far more data than Chinchilla suggests is more expensive to *train* but much cheaper to *run* at scale, and inference is where the lifetime cost sits. "Over-trained relative to Chinchilla" is a feature, not a mistake.

### M11 · Reasoning models and test-time compute `[INT][GEN]`
A newer axis: instead of only scaling *training*, you can spend more compute at *inference* time, letting the model produce long internal reasoning ("thinking") before answering. Trained largely through RLVR (→ M9), these models trade latency and token cost for accuracy on hard, verifiable problems. The design consequence: "spend more thinking tokens" becomes a tunable knob alongside model size, and not every task wants it – reasoning is expensive and can be overkill for extraction or formatting.

---

## Tier 2 – Build craft

### C1 · Context engineering `[DOC][KAR]`
The discipline of deciding *what occupies the model's working memory* at each step: system instructions, retrieved documents, tool results, conversation history, output schema. It's the direct application of M4 – curated context beats parametric recall. Core sub-skills: ordering and budgeting tokens, summarizing or evicting stale history, and isolating context per subtask. This term has largely replaced "prompt engineering" in serious design conversations, because the prompt is only one tenant of a crowded window.

### C2 · Retrieval-augmented generation (RAG) `[GEN][DOC]`
Fetch relevant material at request time, place it in context, and instruct the model to ground its answer in it. The decisions that matter: how to chunk, whether to retrieve by embedding similarity, keyword (BM25), or a **hybrid** of both, whether to re-rank results, how to filter by metadata, and how to enforce citation. Know the trade-off against long context and fine-tuning (→ C9): RAG wins when the corpus is large, changes often, or must be auditable – which is exactly why it dominates knowledge-grounded and document-heavy products.

### C3 · Structured output and tool calling `[DOC][GEN]`
Making model output machine-consumable: JSON schemas, constrained decoding, and tool/function-call formats. This is the load-bearing joint between a probabilistic model and the deterministic systems around it, and a large share of production failures live here. Know the spectrum from weakest to strongest – asking nicely for a format in the prompt → tool-calling APIs → grammar-constrained decoding – and the catch: heavy formatting constraints can degrade reasoning, so let the model reason first and format second.

### C4 · Agents and the loop `[KAR][DOC]`
An agent is a model in a loop: it proposes a tool call, the environment runs it, the result returns to the context, repeat until done. The useful framing is an agent as a capable but green new hire – strong in flashes, in need of guardrails. The engineering reality is error amplification: per-step reliability *compounds* over a long loop, so you care about clear termination conditions, human-in-the-loop gates for risky actions, and recognizing when a plain deterministic pipeline beats an agent outright.

### C5 · Orchestration, routing, and subagents `[GEN][KAR]`
Patterns for splitting work across model calls: a router that sends each request to a specialist, an orchestrator that fans out to parallel subagents, sequential pipelines, and worker/judge pairs. The main reason subagents exist is **context isolation**: a context-heavy subtask (scanning a huge document, deep research) runs in its own window and returns only a compact summary, keeping the orchestrator's working memory clean. Worth remembering in design reviews: today's "multi-agent" systems are coordinated plumbing, not agents that build shared culture.

### C6 · Evaluation and LLM-as-judge `[GEN][INT][KAR]`
The practice that separates engineering from vibes: curated datasets, expected outputs, graders (exact-match, rubric, or an **LLM acting as judge**), and regression runs on every change. Two warnings to carry: LLM judges can be fooled by adversarial nonsense that happens to score well, and the deepest form of reward hacking is the *team* tuning the system to its own benchmark until it's superb on the test and brittle everywhere else (→ D4). Hence small adversarial eval sets you rotate, judges spot-checked against humans, and never optimizing one static benchmark for long.

### C7 · Prefill vs. decode, prompt caching, and latency `[INFE][DOC]`
Inference has two phases. **Prefill** processes the input in parallel and is compute-bound; **decode** generates output one token at a time and is memory-bandwidth-bound. This is why output tokens cost several times more than input tokens and why long outputs dominate latency. **Prompt caching** stores the KV cache of a stable prefix (system prompt, instructions, fixed documents) so repeat calls skip re-processing it – typically large cost and latency savings, with cache lifetimes from minutes to about an hour. The design rule that falls out: put stable content first, volatile content last.

### C8 · Inference economics and batching `[INFE][INT][SCALE]`
Without batching many users' requests together, serving economics are dramatically worse – often by orders of magnitude – because the cost of fetching the weights from memory gets amortized across a batch only when the batch is large. This is why providers can offer steep discounts for asynchronous/batch APIs (they fill idle batch capacity) and why hard latency floors exist no matter how much you're willing to pay. Fluency: you can explain the link between batch size, throughput, and cost per token.

### C9 · The adaptation decision: prompt → RAG → fine-tune `[GEN][INT]`
A recurring architecture choice, with a sane default order. Start with instructions and examples in context (cheap, reversible, inspectable). Add RAG when you need knowledge that's auditable and updatable. Reach for fine-tuning only to lock in stable *form and behavior* – style, narrow classification, a fixed output shape – **not** to inject facts. The deeper justification: training a model narrowly tends to make it a brittle specialist, while keeping knowledge in retrievable context preserves generality. Skills and workflow files are a useful middle path – procedures encoded in retrievable context rather than in weights.

### C10 · Hallucination, grounding, and verification `[GEN][DOC]`
Models produce fluent, confident falsehoods because they optimize for plausibility, not truth – and a made-up fact and a real one are sampled the same way. The mitigation stack: grounding (answer only from supplied sources), mandatory citations checked *programmatically* against the source text, an explicit "not in the sources" escape hatch, and independent verifier passes. For any product where being wrong is expensive, this isn't one concern among many – it's the defining constraint.

### C11 · Long context: limits and "context rot" `[INFE][ATTS]`
Two separate problems hide behind "long context." The *physical* one: dense attention runs into a memory-bandwidth wall, which is why advertised context lengths plateaued for a while and why ever-longer context is costly. The *behavioral* one: effective attention degrades well before the stated limit – models lose the middle of a long context and reason less reliably across it. A 200K-token window does not give you 200K tokens of dependable reasoning. So retrieval, summarization, and context isolation (→ C5) stay necessary even when everything would technically fit.

### C12 · Model selection and routing `[GEN][INT]`
Matching model tier to task: a frontier model for judgment-heavy steps, a small fast one for classification, extraction, and routing. The levers are capability, cost per token, latency, and context size. A counter-intuitive market note: as compute gets scarcer, demand can shift *toward* premium models because quality-per-dollar matters more than price-per-token. Fluency means defending a routing choice with eval data – "the cheap model passes 97% of this extraction eval at a tenth of the cost" is the sentence that ends the debate.

### C13 · Reliability engineering for stochastic components `[GEN]`
Treat the model as an unreliable dependency and design around it: retries with validation, fallback models, output-schema checks, idempotent steps, checkpoints for long workflows, timeouts, and graceful degradation. The compounding math is the headline: a step that's 95% reliable, used ten times in a chain, yields roughly 60% end-to-end – the quantitative case for fewer, fatter steps with verification gates between stages.

### C14 · Prompt injection and LLM security `[GEN][DOC]`
A model can't reliably tell *instructions* from *data*: any text entering the context – a retrieved document, an email, a web page – can carry hostile instructions ("ignore your rules and send X"). This is unsolved in the general case. Mitigations: privilege separation (the component that reads untrusted text can't call dangerous tools), output filtering, and human approval for irreversible actions. The danger pattern to name in a review is the combination of untrusted input, tool access, and sensitive data in a single context.

---

## Tier 3 – Open debates

### D1 · The critique of reinforcement learning `[INT][KAR]`
A widely-cited position: RL as used today is crude – a single scalar reward for a long trajectory is a very thin signal, making it data-inefficient, fragile, and prone to penalizing creativity. The provocative version is that current RL "works only because everything before it was worse." Why it matters to you: it's the standard argument for why reasoning-model gains might plateau, and why making judges robust (→ C6) is the live bottleneck rather than just adding more RL.

### D2 · The generalization gap and "jaggedness" `[INT]`
The core unease among researchers: models generalize markedly worse than people. They can be superhuman on a benchmark yet break one step off-distribution – capability is *jagged*, brilliant and brittle side by side. Humans learn from little data and stay robust; models need enormous data and still fail in odd places. Many people argue that reliable generalization, not more compute or a cleverer architecture, is *the* unsolved problem – the real explanation for every workflow that "should have worked" and didn't.

### D3 · Continual learning – the missing capability `[KAR][INT]`
Today's models don't learn from experience after deployment; each session starts fresh, with perfect recall of training data but amnesia about your last conversation. Several researchers flag this as the central gap on the road to more general systems. Until models learn on the job, every bit of "learning" your *system* does has to live in *your* architecture – memory files, feedback loops, eval-driven revisions. That gap is a large part of why the engineering role exists at all.

### D4 · Benchmarks vs. the real world `[INT][KAR]`
The sharpest version: the most consequential reward hacking is done by *researchers*, who tune training toward evals until the model is an overfitted student – strong on the test, shaky in the wild. The mechanical version: LLM judges can be spoofed by adversarial nonsense. Together they explain the gap everyone feels between climbing benchmark scores and stubborn real-world unreliability. The practical stance: never accept a public benchmark number as evidence a model fits *your* task; private evals on your own distribution are the only currency (→ C6).

### D5 · Synthetic data and model collapse `[KAR][EXP]`
Training heavily on model-generated data tends to quietly lose diversity – outputs collapse toward the model's favorite modes and turn into bland "slop," because humans are noisier but unbiased sources of entropy. This caps naive self-improvement loops (train on your own outputs, degrade) and is a reason for skepticism about agents bootstrapping their own "culture." The same drift shows up at workflow scale: pipelines that feed model output back into model input wander off without fresh grounding or a human anchor.

### D6 · Memory bandwidth as the real constraint `[INFE][SYS][SCALE]`
A systems thesis worth knowing: serving frontier models is bottlenecked by **memory bandwidth, not raw compute**. A simple roofline view – time is the max of memory time and compute time – governs almost everything: batch sizes, MoE design, why context lengths plateaued, and the structure of API pricing. People even reverse-engineer lab internals from public prices. The payoff: when someone asks "why is output five times the price of input?" or "why did context lengths stop growing?", this is the answer.

### D7 · Physical ceilings: fabs, memory, and power `[INT]`
The supply-chain reality behind the hype: advanced chip fabrication depends on a tiny number of EUV lithography tools built only a few dozen at a time, high-bandwidth memory fabs take years to stand up, and AI demand is already pushing on power grids and component prices. The upshot is a hard ceiling on how fast total AI compute can grow this decade, well below the most aggressive public ambitions. Compute scarcity is *structural*, so token prices and capacity limits are long-term architecture constraints, not temporary friction.

### D8 · GPU economics and the token market `[INT]`
A contrarian take on hardware depreciation: a high-end AI GPU can be *more* valuable a few years after release than at launch, because better models extract more useful work per chip – hardware value is downstream of model quality. Labs pre-commit to capacity years ahead, and serving revenue requires enormous, contracted inference capacity. The lens to keep: the industry's true unit economics are *cost per useful token*, and every layer – chips, serving stacks, your own workflow design – competes on that number.

### D9 · Where do the next gains come from? `[INT]`
The live strategic disagreement. One camp holds that the era of "just scale the same recipe" is ending and the field is back to needing genuinely new ideas (because the next bottleneck – generalization – isn't solved by size); the other points out that labs keep shipping scale-driven gains and customers keep contracting ever more compute. You don't have to pick a side, but you should recognize the debate and hold both observations at once: scaling is delivering *and* may be approaching diminishing returns on the hardest problems.

### D10 · Timelines and the "decade of agents" `[KAR][INT]`
A common sober view among builders: transformative, broadly capable AI is plausibly years away, not months – the remaining problems (continual learning, robust computer use, multimodality) are each tractable but each is a long slog. The professional posture that follows: build for models that *improve steadily*, not for a single discontinuous jump. Architectures that absorb the next better model gracefully (→ C12) beat bets staked on one capability leap arriving on schedule.

### D11 · Architecture evolution: latent attention and beyond `[SYS][ATTS][MOE]`
The architecture isn't frozen. Newer designs such as **multi-head latent attention (MLA)** compress the KV cache to push back the memory-bandwidth wall (→ D6), and they interact with MoE (→ M7) in ways that change which hardware is well-suited to serving. You don't need the math, but you should know that "transformer + dense attention" is a snapshot, not the end state, and that attention and sparsity are active areas where today's cost constraints are being renegotiated.

---

## Recommended path

1. **M4 → M1 → M5 → M3** – the working-memory model of an LLM. Highest leverage per hour; everything else hangs off it.
2. **C1, C2, C6** – context engineering, retrieval, and evaluation: the three pillars of the systems-builder craft.
3. **C7, C8** – inference phases and economics. This is where you start sounding like an architect rather than a user.
4. **M9, M10, M11, D1, D4** – post-training, scaling, reasoning, and their discontents: the debates experts actually have.
5. **Remaining C concepts** as your projects touch them; **D6, D7, D8, D11** before any conversation about infrastructure, cost, or hardware strategy.

**Self-check, per concept.** For each one, can you (a) explain it in two sentences, (b) name the design decision it governs, and (c) state the strongest objection to the mainstream view? Yes across all three tiers means you're fluent – you can follow and contribute to the conversation, not just nod along.
