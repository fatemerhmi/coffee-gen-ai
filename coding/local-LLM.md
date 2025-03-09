# Local LLMs
here are list of tools you can use to run an LLM locally. 
Reasons for running LLMs locally could be:
* privacy: some LLM providers use the user data to train their models
* Customization Options: cpu threads, temperature, context length, GPU settings
* Cost: free to use if you already have the required hardware
* offline support: whether online or offline your LLM is available

1. [Ollama](https://ollama.com/)

1. [LM Studio](https://lmstudio.ai/)
* can run any model file with the format `gguf`
* chat history: save prompts for later use
* Cross-platform: LM Studio is available on Linux, Mac, and Windows operating systems.
* Local Inference Server for Developers

```
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
```

2. [Jan](https://jan.ai)

3. [Llamafile](https://github.com/Mozilla-Ocho/llamafile/)
* backed by Mozilla

4. [GPT4ALL](https://www.nomic.ai/gpt4all)

6. [LLaMa.cpp](https://github.com/ggml-org/llama.cpp)
inference engine

`brew install llama.cpp`