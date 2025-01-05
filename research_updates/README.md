# Research papers

## structure

[Research Updates/](./README.md)
- [models.md](./models.md)
- [benchmarks.md](./benchmarks.md)

## Reinforcement Learning from Human Feedback

* Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback, by Anthropic [Apr 2022] - [source](https://arxiv.org/pdf/2204.05862)

## Multi-Agent

- ChatDev: Communicative Agents for Software Development by Qian et al. [Jun 2024] - [paper](https://arxiv.org/pdf/2307.07924) / [github](https://github.com/OpenBMB/ChatDev)
  - Company Overview: ChatDev is a virtual software company powered by intelligent agents.
  - Agents take on roles such as CEO, CTO, programmer, tester, reviewer, and designer.
  - Organizational Structure: Operates as a multi-agent system collaborating through specialized seminars.
  - Collaboration Tasks: Agents handle designing, coding, testing, and documenting software.
  - Mission: "Revolutionize the digital world through programming."
  - Framework Focus: Offers a user-friendly, customizable, and extendable framework.
  - Technology Basis: Built on large language models (LLMs).
  - Research Purpose: Serves as a platform to study and understand collective intelligence.
  
* Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows? Cao et al. [Jul 2024] - [paper](https://arxiv.org/abs/2407.10956)

* Chain of Agents: Large Language Models Collaborating on Long-Context Tasks, Zhang et al. [Jun 2024] -  [paper](https://arxiv.org/abs/2406.02818)
  - previous work on long context:
    - input reduction: such as Truncation and RAG
    - context extension: Claude-3, Long llama
  - this paper:
    - Stage 1: worker agent: segment comprehension and chain of communication
    - Stage 2: manager agent: information integration and response generation

* Merge, Ensemble, and Cooperate! A Survey on Collaborative Strategies in the Era of Large Language Models, Le et al. [July 2024] [paper](https://arxiv.org/abs/2407.06089)

### Debate

* On scalable oversight with weak LLMs judging
strong LLMs , Kenton et al. [Jul 2024] - [paper](https://arxiv.org/pdf/2407.04622)
  - debate consistently outperforms consultancy across all tasks, previously only shown on a single extractive QA task in [Khan et al.](https://arxiv.org/pdf/2402.06782) (2024).
  - Comparing debate to direct question answering baselines, the results depend on the type of task. In extractive QA tasks with information asymmetry, debate outperforms QA without article as in the single task of Khan et al. (2024), but not QA with article. For other tasks, when the judge is weaker than the debaters (but not too weak), we find either small or no advantage to debate over QA without article.
  - Changes to the setup (number of turns, best-of-N sampling, few-shot, chain-of-thought) seem to have little effect on results.
  - In open consultancy, the judge is equally convinced by the consultant, whether or not the consultant has chosen to argue for the correct answer. Thus, using weak judges to provide a training signal via consultancy runs the risk of amplifying the consultant’s incorrect behavior.
  - In open debate, in contrast, the judge follows the debater’s choice less frequently than in open
consultancy. When the debater chooses correctly, the judge does a bit worse than in open
consultancy. But when the debater chooses incorrectly, the judge does a lot better at discerning
this. Thus, the training signal provided by the weak judge in open debate is less likely to amplify
incorrect answers than in open consultancy.
  - They calculate Elo scores and show that stronger debaters lead to higher judge accuracy (including for a weaker judge) across a range of tasks.

* Multi-LLM Debate: Framework, Principals, and
Interventions, Estornell et al. [Jul 2024] - [paper](https://openreview.net/pdf?id=sy7eSEXdPC)
  - Introduce 3 interventions in the Multi-LLM Debate:
    - Diversity pruning: Delete responses with similar distributions over latent concepts
    - Quality pruning: Delete responses with dissimilarity distributions over latent concepts
    - Misconception pruning: Modify distribution of latent concepts in a reponse
  - Apply interventions: at time t-1 modify reponses before they are used next round



## Agent Frameworks:
- Code Generation with AlphaCodium: From Prompt Engineering to Flow
Engineering, Ridnik et al. (Jan 2024)[[paper](https://arxiv.org/pdf/2401.08500)]
- Reflexion: Language Agents with
Verbal Reinforcement Learning, Shinn et al (Oct 2023) [[paper](https://arxiv.org/pdf/2303.11366)]
- MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action, Yang et al. (March 2023) - [paper](https://arxiv.org/pdf/2303.11381)

## Evaluation

### LLM evaluators (LLM-as-a-Judge)
LLM-as-a-Judge weather as self-evaluator or evaluator of other LLM's generation, it a topic that has been proven to be useful in following scenarios:
- benchmarking LLM's performance
- reward modeling
- constitutional AI
- self-refinemen

Here are some interesting papers on this topic:

* A Survey on LLM-as-a-Judge, Gu et al. [Dec 2024] - [paper](https://arxiv.org/pdf/2411.15594)

* LLM Evaluators Recognize and Favor Their Own Generations, Panickssery et al. [Apr 2024] - [paper](https://arxiv.org/pdf/2404.13076)
  - biases are introduced due to the same LLM acting as both the evaluator and the evaluatee
  - self-preference, where an LLM evaluator scores its own outputs higher than others’ while human annotators consider them of equal quality
  - **findings**:
    - LLMs such as GPT-4 and Llama 2 have non-trivial accuracy at distinguishing themselves from other LLMs and humans
    - They discover a linear correlation between self-recognition capability and the strength of self-preference bias; using controlled experiments, they show that the causal explanation resists straightforward confounders


* Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena by Zheng et al [Dec 2023] - [paper](https://arxiv.org/pdf/2306.05685)
    - Motivation / contribution:
        * **Challenges in Evaluating LLM-Based Chat Assistants**: Traditional benchmarks are inadequate for assessing the broad capabilities of LLM-based chat assistants, especially in measuring human preferences.

        * **Scalability and Explainability**: Human evaluations are expensive and time-consuming. Utilizing LLMs as judges offers a scalable and explainable alternative to approximate human preferences.

        * **Alignment with Human Preferences**: There's a need to ensure that LLMs align with human preferences in open-ended tasks, such as multi-turn dialogues, which traditional benchmarks fail to assess effectively.

        * **Mitigating Biases in LLM Judgments**: The research identifies potential biases in LLM judgments, such as position, verbosity, and self-enhancement biases, and proposes solutions to mitigate them.

        * **Development of New Benchmarks**: The introduction of [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) and [Chatbot Arena](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) aims to provide platforms for evaluating the alignment between LLM judgments and human preferences.

### Evaluation of LLM's

* A Survey on Evaluation of Large Language Models - by YUPENG CHANG et al [Dec 2023] - [paper](https://arxiv.org/pdf/2307.03109)


