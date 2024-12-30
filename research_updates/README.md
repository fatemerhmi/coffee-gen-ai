# Research papers

* Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback, by Anthropic [Apr 2022] - [source](https://arxiv.org/pdf/2204.05862)

## Evaluation
* Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena by Zheng et al [Dec 2023] - [paper](https://arxiv.org/pdf/2306.05685)
    - Motivation / contribution:
        * **Challenges in Evaluating LLM-Based Chat Assistants**: Traditional benchmarks are inadequate for assessing the broad capabilities of LLM-based chat assistants, especially in measuring human preferences.

        * **Scalability and Explainability**: Human evaluations are expensive and time-consuming. Utilizing LLMs as judges offers a scalable and explainable alternative to approximate human preferences.

        * **Alignment with Human Preferences**: There's a need to ensure that LLMs align with human preferences in open-ended tasks, such as multi-turn dialogues, which traditional benchmarks fail to assess effectively.

        * **Mitigating Biases in LLM Judgments**: The research identifies potential biases in LLM judgments, such as position, verbosity, and self-enhancement biases, and proposes solutions to mitigate them.

        * **Development of New Benchmarks**: The introduction of [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) and [Chatbot Arena](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) aims to provide platforms for evaluating the alignment between LLM judgments and human preferences.
* A Survey on Evaluation of Large Language Models - by YUPENG CHANG et al [Dec 2023] - [paper](https://arxiv.org/pdf/2307.03109)