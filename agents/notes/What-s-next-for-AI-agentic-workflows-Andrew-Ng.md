# What's next for AI agentic workflows - Andrew Ng

Here are some notes based on this [video](https://www.youtube.com/watch?v=sal78ACtGTc&t=4s&ab_channel=SequoiaCapital). 

slide 1:
![Non-agentic workflow (Zero-shot) vs Agentic Workflow](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide1.jpg)
* Agentic workflows are iterative which involves some thinking and revising. 

slide 2:
![Coding benchmark (Human Eval)](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide2.jpg)
* Example of HumanEval benchmark, by openai - [[github](https://github.com/openai/human-eval)] - released 2021

slide 3:
![Coding benchmark (Human Eval)](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide3.jpg)
* Performance of gpt3.5 and gpt-4 on HumanEval benchmark in Zero shot and Agentic settings.

slide 4:
![Agentic reasoning design patterns](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide4.jpg)
* Let's explore these 4 design patterns

slide 5:
![Reflection](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide5.jpg)
* Ask the LLM-itself to critic itself.
* Recommended read: 
    - Self-Refine: Iterative Refinement with Self-Feedback, Maddan et al. (2023) - [[paper](https://arxiv.org/abs/2303.17651)]
    - Reflexion: Language Agents with Verbal Reinforcement Learning, Shinn et al. (2023) - [[paper](https://arxiv.org/abs/2303.11366)]

slide 6:
![Reflection with two agents](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide6.jpg)
* Ask another agent to Critic the first Agent results.

slide 7:
![Tool use](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide7.jpg)

slide 8:
![planning](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide8.jpg)

slide 9:
![Multiagent collaboration](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide9.jpg)

slide 10:
Agentic Reasoning Design Patterns
1. Reflection
    * Self-Refine: Iterative Refinement with Self-Feedback, Madaan et al. (2023)
    * eflexion: Language Agents with Verbal Reinforcement Learning, Shinn et al., (2023)
2. Tool use
    * Gorilla: Large Language Model Connected with Massive APls, Patil et al. (2023)
    * MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action, Yang et al. (2023)
3. Planning
    * Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, Wei et al., (2022)
    * HuggingGPT: Solving Al Tasks with ChatGPT and its Friends in Hugging Face, Shen et al. (2023)
4. Multi-agent collaboration
    * ommunicative Agents for Software Development, Qian et al., (2023)
    * AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation, Wu et al.

slide 11:
![conclusion](../../images/notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng/slide11.jpg)