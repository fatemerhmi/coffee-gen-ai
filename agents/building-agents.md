# Building Agents

* Building effective agents, by Anthropic [Dec 19, 2024] - [[blog post](https://www.anthropic.com/research/building-effective-agents)]
    - Building Effective Agents Cookbook, by Anthropic (Erik Schluntz and Barry Zhang) - [[github](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)]

* Introducing smolagents, a simple library to build agents by HuggingFace [Dec 2024] - [[blog post](https://huggingface.co/blog/smolagents)]

* Google's whitepaper on AI Agents [Sept 2024] - [[whitepaper](https://www.kaggle.com/whitepaper-agents)]

* AI Agents in LangGraph, by Langchain, Tavily, DeepLearning.AI - [[short course](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/1/introduction)]
    - [Build an Agent from scrach](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/2/build-an-agent-from-scratch)
        * Based on: A simple Python implementation of the ReAct pattern for LLMs, by Simon Willison - [blog post](https://til.simonwillison.net/llms/python-react-pattern)
        * ReAct Pattern: Stands for "reasoning plus acting."
            - **Initial Thought**: LLM begins by thinking about what action to take
            - **Action Execution**: The action is executed within an environment.
            - **Observation and Feedback**: Following the action, an observation is returned from the environment.
            - **Repetition and Refinement**: The LLM processes the observation, rethinks, and decides on the next action.
            - **Continuation**: This cycle continues until the LLM decides no further actions are necessary.
    - [LangGraph components](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/3/langgraph-components) 
        * Other frameworks:
            - Reflexion [[paper](https://arxiv.org/pdf/2303.11366)]
            - AlphaCodium[[paper](https://arxiv.org/pdf/2401.08500)]
        * Prompt templates for ReAct [source](https://smith.langchain.com/hub/hwchase17/react)
        * LangGraph have predifined tools, such as: `from langchain_community.tools.tavily_search import TavilySearchResults`
        * LangGraph components:
            - Nodes: Agents or Functions
            - Edges: Connect Nodes
            - conditional edges: decision
            - Entry point: starting node
            - End node (ex: `from langgraph.graph import END`)
            - `AgentState`: Annotated list of messege that we'll add to over time
            
    - [Agentic Search Tools](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/4/agentic-search-tools)
        * Tavily
            - Example of How: break query, to sub queries, Retrieve from different souce, score and filtering, then return top k
            - example: `from tavily import TavilyClient`
    - [Persistance and streaming](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/5/persistence-and-streaming)
    - [Human in the loop](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/6/human-in-the-loop)

* AI Agentic Design Patterns with AutoGen by Microsoft, PennSate, Deepleaning.AI - [shourt course](https://learn.deeplearning.ai/courses/ai-agentic-design-patterns-with-autogen)

* What's next for AI agentic workflows ft. [Andrew Ng](https://www.linkedin.com/in/andrewyng/) of AI Fund [March 2024] - [[youtube](https://www.youtube.com/watch?v=sal78ACtGTc&t=4s&ab_channel=SequoiaCapital)] / [[My notes](notes/What-s-next-for-AI-agentic-workflows-Andrew-Ng.md)]
