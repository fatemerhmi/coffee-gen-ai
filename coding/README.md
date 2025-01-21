# Coding

This directory is to store coding samples and projects as well as some libraries and tools that I use.

## Libraries

- [Langchain](https://python.langchain.com/docs/get_started/introduction)

- [LiteLLM](https://github.com/BerriAI/litellm)
    * Translate inputs to provider's completion, embedding, and image_generation endpoints
    * Consistent output, text responses will always be available at ['choices'][0]['message']['content']
    * Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
    * Set Budgets & Rate limits per project, api key, model (LiteLLM Proxy Server (LLM Gateway))[https://docs.litellm.ai/docs/simple_proxy]

- [smolagents](https://github.com/huggingface/smolagents)
    * A framework for building agents with LLMs
    * [Introducing smolagents, a simple library to build agents](https://huggingface.co/blog/smolagents#%F0%9F%A4%94-what-are-agents)

## Model providers

- [Together.ai](https://docs.together.ai/docs/introduction)
    - they provide a variety of models, including open source models - full list [here](https://api.together.xyz/models?filter=serverless)