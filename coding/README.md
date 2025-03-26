# Coding

This directory is to store coding samples and projects as well as some libraries and tools that I use.

## Libraries

### libraries to build agents with
- [smolagents](https://github.com/huggingface/smolagents)
    * A framework for building agents with LLMs
    * [Introducing smolagents, a simple library to build agents](https://huggingface.co/blog/smolagents#%F0%9F%A4%94-what-are-agents)

- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
    * AutoGPT is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows.

- [OpenAI Swarm](https://github.com/openai/swarm)

- [LangGraph](https://github.com/langchain-ai/langgraph)


### Other Libraries

- [Langchain](https://python.langchain.com/docs/get_started/introduction)

- [LiteLLM](https://github.com/BerriAI/litellm)
    * Translate inputs to provider's completion, embedding, and image_generation endpoints
    * Consistent output, text responses will always be available at ['choices'][0]['message']['content']
    * Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
    * Set Budgets & Rate limits per project, api key, model (LiteLLM Proxy Server (LLM Gateway))[https://docs.litellm.ai/docs/simple_proxy]


- [dspy](https://github.com/stanfordnlp/dspy)
    * DSPy stands for Declarative Self-improving Python
    * The framework for programming—not prompting—language models
    * iterate fast on building modular AI systems and offers algorithms for optimizing their prompts and weights, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops


## Model providers

- [Together.ai](https://docs.together.ai/docs/introduction)
    - they provide a variety of models, including open source models - full list [here](https://api.together.xyz/models?filter=serverless)