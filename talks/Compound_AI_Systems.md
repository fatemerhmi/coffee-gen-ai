# Compound AI Systems  
*By [Fatemeh Rahimi](https://www.linkedin.com/in/fatemehrahimi/), Senior NLP Scientist at Pythonic AI*  
*Presented March 2025 • [Halihax](https://www.halihax.com/)*

Large Language Models (LLMs) have already reshaped how we think about artificial intelligence. Their headline-grabbing feats—fluent conversation, crisp summarization, even full-stack code generation—are remarkable. Yet the spotlight on individual models can distract us from a more important shift that’s happening right now:

> We're moving from **stand-alone models** to **compound AI systems**—cohesive pipelines where multiple models, tools, and feedback loops work together to solve real-world problems end-to-end.

This post explores what compound systems look like, why they matter, and how you can start building them without losing control of complexity.

<img src="../images/talks/Compound_AI_Systems/1.png"
     alt="Collage of LLM launch headlines (GPT-4o, Gemini 2.0, Claude 3.7, PaLM 2) — each headline shows the word 'model' boxed in red"
     title="Model announcements still centre on the word 'model'"
     style="width:80%;display:block;margin:0 auto;" />


Let's start with a simple question: **What *is* an AI model?**  
At its core, a model is just a function—you hand it an input prompt, it hands you an output. For language models, that usually boils down to “predict the next token” over and over. Bolt on a sampling strategy (greedy decoding, top-p, beam search—pick your flavour) and you get what is called a **minimal system**: the bare-bones model plus just enough logic to turn predictions into fluent text.

<img src="../images/talks/Compound_AI_Systems/2.png"
     alt="Schematic of a minimal system: an input prompt enters the model (stack of blue blocks); arrows show token predictions flowing through layers; a sampling method converts logits to tokens; the final output is labelled “Answer”."
     title="Minimal system = model + sampling"
     style="width:50%;display:block;margin:0 auto;" />

     
### A quick toy example

Say we feed our minimal system the prompt:

> **“Halifax has a beautiful …”**

In more technical terms, the decoder emits a probability distribution over the entire vocabulary, and the sampling step (greedy, in this illustration) simply selects the token with the highest likelihood—here, harbour.
> **Output:** “**…harbour!**”

You can visualise it like a bar chart where *harbour* towers over the rest. The point: at this level, all the “intelligence” we see is just one function picking the most likely next word.

<!-- centre the diagram at 50 % width -->
<img src="../images/talks/Compound_AI_Systems/3.png"
     alt="Bar chart of candidate next tokens after the prompt 'Halifax has a beautiful …'; 'harbour' has the highest probability and is selected."
     title="Sampling selects the top-probability token"
     style="width:90%;display:block;margin:0 auto;" />

So far, so good—but that **minimal system** is still just smart autocomplete.  
It can’t pull in new facts, run live calculations, or trigger side-effects—it only parrots whatever was baked into its weights at training time.

To get something *useful* we wrap the model in an **advanced system** that can reach for external tools whenever its own knowledge runs out.

<!-- 50 % width, centred -->
<img src="../images/talks/Compound_AI_Systems/4.png"
     alt="Diagram labelled “Advanced System”. Inside a purple box, a female agent stands between a book (parametric knowledge) and a toolbox. Outside the box, icons for a terminal, calculator, web search, and database represent callable tools the agent can use."
     title="Model + tools = advanced system"
     style="width:70%;display:block;margin:0 auto;" />

Think of the **book** as everything the model already “knows,”  
and the **toolbox** as runtime helpers—code execution, a calculator, web search, a company database, you name it.  
When you ask ChatGPT to *“plot me a sine wave”* and it spits back a chart, that’s the toolbox at work: the model writes code, the system runs it, then pipes the result back to you. Suddenly we’re miles beyond plain text completion—and firmly in *compound-system* territory.


## Why systems are important?

### 1. Some tasks are solved at the **system** level  
Cranking up model size or token budgets is pricey—and it's not always the shortest path to better results.   
Take **AlphaCode 2**: instead of training a gargantuan new network, the team wrapped a mid-sized model in a clever pipeline—massive candidate generation → clustering → execution-based filtering—and jumped **≈ 40 %** in competition ranking.  

Likewise, the *Small but Mighty AI* trend report shows enterprises flocking to compact models because lower latency ≠ lower capability **if** you design the surrounding system well.

### 2. Systems can be **dynamic**  
A frozen LLM can’t pull in fresh data. A system can. Plug in retrieval, web search, code execution—suddenly your agent reacts to the world in real time.

<!-- 60 % width, centred -->
<img src="../images/talks/Compound_AI_Systems/5.png"
     alt="Slide titled 'Systems can be dynamic'. A user avatar asks, 'Why was my last bill higher than usual?'. An agent at a workstation queries live data and replies: 'Your bill for March increased by $20 due to international calling charges…'."
     title="Dynamic system = model + live data access"
     style="width:90%;display:block;margin:0 auto;" />

### 3. Safety, control, and trust  
“Just tune the network to be safe” is easier said than done. Systems give us *hooks*:  
* post-filters to catch disallowed content,  
* tool routing to pass tricky queries to a verified service,  
* confidence thresholds that trigger a human-in-the-loop.  

In short, compound systems let us build **trustworthy** AI, not merely *smart* AI.


## Compound-System Components  
*It starts with the prompt and ends with the answer, but the journey in between is anything but trivial.*

### 1&nbsp;·&nbsp;Sampling matters  
The decoder is not a black box—you choose how it samples.  
Greedy, top-p, beam search, *diverse-beam*, “valid-JSON-only”… each policy can steer the very same model toward wildly different outputs. Picking (or mixing) the right strategy is part of system design.

<!-- 60 % width · centred -->
<img src="../images/talks/Compound_AI_Systems/6.png"
     alt="Slide titled ‘Minimal Systems’. Left: a bullet list of sampling methods—Greedy, Top-p, Beam Search, Token Diversity, Valid JSON. Right: a diagram showing Halifax has a beautiful … flowing through the model; a bar graph of vocabulary logits highlights ‘harbour’ as the selected token."
     title="Different sampling rules → different answers"
     style="width:60%;display:block;margin:0 auto;" />

---

### 2&nbsp;·&nbsp;Let the model explore before you decide  
Another view of sampling is to treat each completion as a *reasoning path*.  
Generate many paths, keep the ones that agree, and suddenly a mid-sized model can solve problems it missed on the first try.

<!-- 60 % width · centred -->
<img src="../images/talks/Compound_AI_Systems/7.png"
     alt="Diagram titled ‘Majority completion strategies’. A single prompt fans out to four reasoning paths, producing answers A / B / A / C. A majority vote returns Answer A."
     title="Majority-of-thought = cheap ensemble"
     style="width:60%;display:block;margin:0 auto;" />

You can even hide this ensemble trick from users so it *looks* like one fast response.

---

### 3&nbsp;·&nbsp;Prompting is the heart of system design  
Prompting is programming in natural language—tiny tweaks can swing accuracy by double-digit percentages.  
The paper *Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design* reminds us that a single misplaced colon can move accuracy **≈ +80 %**.  
Stable prompting + robust sampling = the backbone of any compound system.

So next time you browse a leaderboard, pause for a second:

<!-- 60 % width · centred -->
<img src="../images/talks/Compound_AI_Systems/8.png"
     alt="Screenshot of the Chatbot Arena leaderboard; a caption on the right reads: ‘Let’s think deeper… Is this what we want to be evaluating?’"
     title="Are we ranking models or whole systems?"
     style="width:60%;display:block;margin:0 auto;" />

Are those scores ranking *models*, or the clever input engineering, sampling rules, and post-processing wrapped around them?  
When you benchmark your own use-case, vary **all** the knobs—not just the model-of-the-week.

---

## Building in the Real World

### Compose, don't monolith  
A production system is a *pipeline* of interchangeable parts:

| Layer | Typical tools |
|-------|---------------|
| **Prompt templates** | Jinja / LangChain / guidance |
| **LLM “brain”** | GPT-4o, Claude-3.7, Gemma-2B, … |
| **Tool calls** | `python` interpreter, calculator, shell |
| **Knowledge** | Retrieval-Augmented Generation (RAG), vector DB |
| **Media** | Image generators, TTS / STT |
| **Safety & validation** | JSON schema, regex filters, human-in-the-loop |

> **Good practice**  
> * reusable prompt libraries  
> * inference-time tool execution  
> * layered validation & fallback

> **Anti-patterns**  
> * hand-editing prompts in prod  
> * hard-coding business logic inside the prompt  
> * betting everything on one “perfect” model

Engineers and data scientists have to co-own this stack: software quality meets prompt craft.

---

Next up we’ll dig into **evaluation harnesses**—how to test the *system*, not just the network.



## Enter the AI **Agent**

<!-- 60% width, centred -->
<img src="../images/talks/Compound_AI_Systems/9.png"
     alt="Venn diagram showing 'AI Agents' as a subset within 'Compound AI Systems'. The outer circle is labelled 'Compound Systems (RAG, tools, validation)' and the inner circle is labelled 'AI Agents (multi-step reasoning)'"
     title="Agents are a subset of compound systems"
     style="width:80%;display:block;margin:0 auto;" />


A particularly ambitious flavour of compound system is the **AI agent**: an LLM wired to a toolbox and empowered to take *multi-step* actions.  
Agentic apps are trendy, but they’re also harder to build, tune, and evaluate—and, frankly, overkill for many problems.

Picture an assistant that can

* 🔎 **search** the web  
* 🐍 **write & run code**  
* 🌐 **call external APIs**  
* ✅ **double-check** its own answers  
* 🌍 **translate** outputs for different audiences  

That isn’t mere text completion; it’s goal-directed reasoning with a full suite of tools.

---

## Challenges in Compound AI Systems

### 1&nbsp;·&nbsp;Retrieval-Augmented Generation (RAG)  
Pick a retriever, an LLM, and some post-processing… then realise each swap changes quality.  
Query expansion, re-ranking, answer validation—every knob matters and they all interact.

### 2&nbsp;·&nbsp;Co-optimisation  
Classic ML pipelines are differentiable end-to-end; you back-prop once and call it a day.  
A compound system mixes neural nets **and** hard-coded tools, so we have to tune modules heuristically (or with reinforcement / black-box search). No free gradients here.

### 3&nbsp;·&nbsp;Operational complexity  
Forget the neat rows of a traditional MLOps dashboard. Agents branch, loop, and call tools in unpredictable orders.

Next-gen MLOps needs to cover:

| Operational need | Why it matters |
|------------------|----------------|
| **Traceable tool calls** | Reproduce or debug multi-step chains |
| **Vector-DB lifecycle** | Versioning, warm-up, freshness guarantees |
| **Security & compliance** | PII leaks, jailbreak filters, tool-scope isolation |

Building compound systems is rewarding—but only if we respect the extra moving parts.

## Conclusion · From **Model-centric** to **System-centric** Thinking

If you remember just one thing, make it this:

> **Small, well-designed systems can beat even the biggest LLMs.**

Choosing a strong base model is only the *first* step. Real-world performance comes from the *system* wrapped around that model—dynamic, tool-aware, and safety-checked.

---

### Quick recommendations

| Goal | Try this first | Why |
|------|----------------|-----|
| **Prompt optimisation** | [`DSPy`](https://github.com/stanfordnlp/dspy) | Auto-tunes prompts & sampling knobs with minimal boilerplate |
| **Building agents** | LangGraph · SmolAgent · AutoGen | Each gives you structured, multi-step tool orchestration |
| **Library shopping list** | [`llm-engineer-toolkit`](https://github.com/KalyanKS/llm-engineer-toolkit) | Curated cheatsheet of RAG, eval, and Ops utilities |

---

## Let’s build real-world systems

Compound AI isn’t a hype term; it’s the next baseline for production AI.  
Whether you’re shipping a chatbot, coding copilot, or medical triage assistant, *system design* is as critical as model choice.

So let’s shift our mindset.  
Let’s architect smarter systems.  
And let’s build them together—scientists **and** engineers, hand in hand.

🔗 Stay in touch:   
 [fatemerhmi.github.io/coffee-gen-ai/talks](https://fatemerhmi.github.io/coffee-gen-ai/talks)  
 [LinkedIn](https://www.linkedin.com/in/fatemehrahimi/)


Resources:
Stanford Webinar - Large Language Models Get the Hype, but Compound Systems Are the Future of AI, [video](https://www.youtube.com/watch?v=vRTcE19M-KE&ab_channel=StanfordOnline)
The Shift from Models to Compound AI Systems, Zaharia et al, [blog](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/)
What are compound AI systems and AI agents? By Microsoft, [blog](https://learn.microsoft.com/en-us/azure/databricks/generative-ai/agent-framework/ai-agents)