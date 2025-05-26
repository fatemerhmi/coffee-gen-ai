# Research papers

## structure

[Research Updates/](./README.md)
- [Models](./models.md)
- [Benchmarks](./benchmarks.md)
- [Research Tools](./research_tools.md)
- [Transformers](./transformers.md)


## Reinforcement Learning from Human Feedback

* Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback, by Anthropic [Apr 2022] - [source](https://arxiv.org/pdf/2204.05862)

## Agent Frameworks:
- Code Generation with AlphaCodium: From Prompt Engineering to Flow
Engineering, Ridnik et al. (Jan 2024)[[paper](https://arxiv.org/pdf/2401.08500)]
- Reflexion: Language Agents with
Verbal Reinforcement Learning, Shinn et al (Oct 2023) [[paper](https://arxiv.org/pdf/2303.11366)]
- MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action, Yang et al. (March 2023) - [paper](https://arxiv.org/pdf/2303.11381)

## Chain of Thought / Thinking
* Understanding Before Reasoning: Enhancing Chain-of-Thought with Iterative Summarization Pre-Prompting, by Zhu et al. [Jan 2025] - [paper](https://arxiv.org/pdf/2501.04341v1)
  - CoT can improve the performance of LLMs on reasoning tasks (often overlook the important step of extracting important information early in the reasoning process)
  - they propose iterative summarization pre-prompting (ISP^2) to enhance CoT 
    - refine LLM reasoning when key information is missing
  - ISP^2 first extract entities and their descriptions to form potential key information pairs using a rating system. 
  - can improve performance (compared to existing CoT methods) by 7.1%

* Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Thought, Xiang et al. [Jan 2025] - [paper](https://arxiv.org/pdf/2501.04682)
  - propose Meta Chain-of-Thought (Meta-CoT), which extends traditional Chain-of-Thought (CoT)

## Human and Agent interaction
- Agents Are Not Enough, Shah, et al. [Dec 2024] - [paper](https://arxiv.org/pdf/2412.05579)
  * Gen AI alone is insufficient to make new generations of agents more successful.
  * to have more effective and sustainable ecosystem needs to includes:
    - **Agents:** Agents are narrow and purpose-driven modules that are trained to do a specific task. Each agent can be autonomous, but with an ability to interface with other agents.
    - **Sims:** Sims are representations of a user. Each Sim is created using a combination of user profile, preferences, and behaviors, and captures an aspect of who the user is. Different Sims can have different privacy and personalization settings. (user persona)
    - **Assistant:** An Assistant is a program that directly interacts with the user, has a deep understanding of that user, and has an ability to call Sims and Agents as needed to reactively or proactively accomplish tasks and sub-tasks for the user.
    The Assistant, with its comprehensive understanding of the user, co-creates and manages Sims with the supervision of the user,

## Agent Computer Interfaces (ACI)

- SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering by Yang et al. [Nov 2024] - [paper](https://arxiv.org/abs/2405.15793) [website](https://swe-agent.com/latest/) - [github](https://github.com/SWE-agent/SWE-agent)
  * investigate how interface design affects the performance of language model agents.
  * Inspired by human-computer interaction (HCI) studies on the efficacy of user interfaces for humans, we investigate whether LM agents could similarly benefit from better-designed interfaces for performing software engineering tasks.

## Multi-Agent

* OPENHANDS: An Open Platform for AI Software Developers as Generalist Agents by wang et al. [Oct 2024] - [Github](https://github.com/All-Hands-AI/OpenHands) / [Paper](https://arxiv.org/pdf/2407.16741)
  - a platform for the development of powerful and flexible AI agents that interact with the world in similar ways to those of a human developer: by writing code, interacting with a command line, and browsing the web

* ChatDev: Communicative Agents for Software Development by Qian et al. [Jun 2024] - [paper](https://arxiv.org/pdf/2307.07924) / [github](https://github.com/OpenBMB/ChatDev)
  - Company Overview: ChatDev is a virtual software company powered by intelligent agents.
  - Agents take on roles such as CEO, CTO, programmer, tester, reviewer, and designer.
  - Organizational Structure: Operates as a multi-agent system collaborating through specialized seminars.
  - Collaboration Tasks: Agents handle designing, coding, testing, and documenting software.
  - Mission: "Revolutionize the digital world through programming."
  - Framework Focus: Offers a user-friendly, customizable, and extendable framework.
  - Technology Basis: Built on large language models (LLMs).
  - Research Purpose: Serves as a platform to study and understand collective intelligence.
  
* Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows? Cao et al. [Jul 2024] - [paper](https://arxiv.org/abs/2407.10956)

* Merge, Ensemble, and Cooperate! A Survey on Collaborative Strategies in the Era of Large Language Models, Le et al. [July 2024] [paper](https://arxiv.org/abs/2407.06089)
  - LLMs show different strengths and weaknesses, leading to challenges in maximizing their overall efficiency and versatility
  - collaborative strategies for LLMs:
    - **Merge**: integrating the parameters of multiple LLMs into a single, unified model, requiring that the parameters are compatible within a linear space
    - **Ensemble**: combines the outputs of various LLMs to generate coherent results
    - **Cooperate**: leverages different LLMs to allow full play to their diverse capabilities for specific tasks.


* Chain of Agents: Large Language Models Collaborating on Long-Context Tasks, Zhang et al. [Jun 2024] -  [paper](https://arxiv.org/abs/2406.02818)
  - previous work on long context:
    - input reduction: such as Truncation and RAG
    - context extension: Claude-3, Long llama
  - this paper:
    - Stage 1: worker agent: segment comprehension and chain of communication
    - Stage 2: manager agent: information integration and response generation

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


## Evaluation

### LLM evaluators (LLM-as-a-Judge)
LLM-as-a-Judge weather as self-evaluator or evaluator of other LLM's generation, it a topic that has been proven to be useful in following scenarios:
- benchmarking LLM's performance
- reward modeling
- constitutional AI, [Bai et al](https://arxiv.org/abs/2212.08073)
- self-refinement

Here are some interesting papers on this topic:

* A Survey on LLM-as-a-Judge, Gu et al. [Dec 2024] - [paper](https://arxiv.org/pdf/2411.15594)

* LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods, Li et al. [Dec 2024] - [paper](https://arxiv.org/pdf/2412.05579)

* From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge, Li et al. [Jan 2025] - [paper](https://arxiv.org/pdf/2412.05579)
  - "LLM-as-ajudge" paradigm, LLMs are leveraged to perform scoring, ranking, or selection across various tasks and applications
  - explore LLM-as-a-judge from three dimensions: what to judge, how to judge and where to judge
    - Attribute: What to judge? helpfulness, harmlessness, reliability, relevance, feasibility and overall quality
    - Methodology: How to judge? prompting techniques for LLMas-a-judge systems, including manually-labeled data, synthetic feedback, supervised fine-tuning, preference learning, swapping operation, rule augmentation, multi-agent collaboration, demonstration, multi-turn interaction and comparison acceleration
    - Application: Where to judge? applications in which LLM-as-a-judge has been employed, including evaluation, alignment, retrieval and reasoning

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


## AI CUDA Engineer

* The AI CUDA Engineer: Agentic CUDA Kernel Discovery, Optimization and Composition [Feb, 2025] - [paper](https://pub.sakana.ai/static/paper.pdf)

## models

[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/pdf/2401.06066) by Deekseek, Jan 2024

[Bite: How Deepseek R1 was trained](https://www.philschmid.de/deepseek-r1) by [Philipp Schmid](https://www.philschmid.de/philipp-schmid) Jan, 2025

[The Illustrated DeepSeek-R1](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1?utm_campaign=post&utm_medium=web) by Jay Alammar Jan, 2025