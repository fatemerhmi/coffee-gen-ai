# Building Agents related courses

Below are the courses related to building agents along with my notes.

## AI Agents in LangGraph, by Langchain, Tavily, DeepLearning.AI - [[short course](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/1/introduction)]
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
