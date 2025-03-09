# Transformers

Transofrmers were first introduced in the paper ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762), Vaswani et al. (2017). This work was published by Google Brain at NeurIPS 2017.

From then this deep leaning architecture has become the main architecutre for many major breakthorughs to date. [Here](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=oR9sCGYAAAAJ&citation_for_view=oR9sCGYAAAAJ:zYLM7Y9cAGgC) is the goole scholar page for this paper, and yet to date still being cited and work as a building block of majority of the NLP research. 

Below are some of the great tutorials I find for learning about this amazing architecutre: 


- [Transformers (how LLMs work) explained visually | DL5](https://www.youtube.com/watch?v=wjZofJX0v4M&ab_channel=3Blue1Brown) by [3 Blue 1 Brown](https://www.youtube.com/@3blue1brown)
    - this video has a great visualization about [temporature](https://youtu.be/wjZofJX0v4M?t=1344).
- [Attention in transformers, step-by-step | DL6](https://www.youtube.com/watch?v=eMlx5fFNoYc&ab_channel=3Blue1Brown) by [3 Blue 1 Brown](https://www.youtube.com/@3blue1brown)


Here are some FAQs I often see people ask when they are introduced to transformers. This is also a great resource if you are trying to learn more about this architecture.

- Why was Transformers paper called "attention is all you need"?   
    The name emphasizes that attention alone is sufficient to achieve state-of-the-art results in various NLP tasks

- What are main ideas behind Transformers?
Main Ideas Behind Transformers:

    - **Self-Attention Mechanism**: Transformers utilize self-attention to weigh the importance of different elements in a sequence, allowing the model to focus on relevant parts when processing data. This mechanism enables the model to capture relationships between all elements, regardless of their position in the sequence.​

    - **Parallel Processing**: Unlike traditional recurrent neural networks (RNNs) that process data sequentially, transformers process all elements of the input simultaneously. This parallelism leads to faster training times and the ability to handle longer sequences effectively.​

    - **Positional Encoding**: they incorporate positional encodings to provide information about the positions of elements in the sequence. These encodings are added to the input embeddings to retain the order information.​

    - **Encoder-Decoder Architecture**: The original transformer model consists of an encoder to process input sequences and a decoder to generate output sequences. The encoder captures the context of the input, while the decoder uses this context to produce the desired output.​

    - **Multi-Head Attention**: Transformers employ multiple attention heads to capture different aspects of relationships within the data. Each head learns to focus on various parts of the input, allowing the model to understand complex patterns.

- What is the difference between the encoder and decoder in a transformer?

    - **Encoder**: Processes the input sequence and generates a continuous representation (context) of the input data.
    - **Decoder**: Takes the encoder's output and generates the target sequence, often used in tasks like machine translation where the model translates input text to another language.