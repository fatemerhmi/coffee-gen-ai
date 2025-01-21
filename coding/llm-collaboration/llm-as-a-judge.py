import streamlit as st
import asyncio
import os
from together import AsyncTogether, Together
import logging

# Set up the Streamlit app
st.title("LLM as a Judge App")

# Get API key from environment variable
together_api_key = os.getenv("TOGETHER_API_KEY")

if together_api_key:
    client = Together()
    async_client = AsyncTogether()

    # Define the models
    reference_models = [
        "Qwen/Qwen2-72B-Instruct",
        "deepseek-ai/DeepSeek-V3",
        "mistralai/Mixtral-8x22B-Instruct-v0.1",
        "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    ]
    llm_as_a_judge = "mistralai/Mixtral-8x22B-Instruct-v0.1"

    # Define the aggregator system prompt
    llm_as_a_judge_system_prompt = """You are tasked with evaluating the results produced by other models based on specific criteria. 
    For each criterion, assign a score from 0 to 5, with the following scale:

    0: Critical issue; the result is unusable or fundamentally flawed.
    1: Significant issues; major problems make the result difficult to use.
    2: Moderate issues; noticeable problems that affect usability but can be corrected.
    3: Acceptable; the result meets basic expectations with minor issues.
    4: Good; the result is effective and mostly free of errors.
    5: Excellent; the result is perfect and exemplary.

    Evaluation Criteria:

        Readability:
            Does the result use clear and concise language?
            Is it free of grammatical errors and easy to understand?
            Does it follow logical structure and flow?

        Efficiency:
            Is the result optimal in terms of processing or execution time?
            Does it demonstrate an effective use of resources?
            Does it avoid redundant or unnecessary elements?

        Accuracy:
            Does the result align with the provided input and context?
            Are the facts, calculations, or outputs correct and relevant?

        Creativity/Innovation (Optional, if applicable):
            Does the result demonstrate original thinking or approach?
            Does it bring new insights or add unique value to the task?

        Alignment with Goals:
            Does the result fulfill the intended purpose or objectives outlined in the task?
            Does it address all key points of the input requirements?

    Your Output: For each result provided by the models, include:

        A score (0-5) for each criterion.
        A brief explanation for the score, highlighting strengths and areas for improvement.
        An overall evaluation summary.

    Use the following format for your response:

    Model [X] Evaluation:

        Readability: [Score] - [Explanation]
        Efficiency: [Score] - [Explanation]
        Accuracy: [Score] - [Explanation]
        Creativity/Innovation: [Score] - [Explanation]
        Alignment with Goals: [Score] - [Explanation]

    Overall Summary: [Your concise summary of the model's performance.]. 
    Responses from models:"""

    # Get user input
    user_prompt = st.text_input("Enter your question:")

    async def run_llm(model):
        """
        Run a single LLM call with a reference model asynchronously.
        This function sends a user prompt to the specified model and returns the model's response.
        """
        try:
            response = await async_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0.8,
                max_tokens=1024,
            )
            return model, response.choices[0].message.content
        except asyncio.TimeoutError:
            logging.error(f"Timeout error with model {model}")
            st.error(f"Timeout error with model {model}. Please try again later.")
        except Exception as e:
            logging.error(f"Error with model {model}: {str(e)}")
            st.error(f"Error with model {model}: {str(e)}")
        return model, f"Error: Could not get response from {model}"

    async def gather_model_responses():
        results = await asyncio.gather(*[run_llm(model) for model in reference_models], return_exceptions=True)
        return [(model, response) for model, response in results if not isinstance(response, Exception)]

    async def display_responses(valid_results):
        st.subheader("Individual Model Responses:")
        for model, response in valid_results:
            with st.expander(f"Response from {model}"):
                st.write(response)

    async def aggregate_responses(valid_results):
        # Aggregate responses with better formatting
        st.subheader("LLM as a Judge Response:")
        formatted_responses = "\n\n".join([f"**{model}:**\n{response}" for model, response in valid_results])
        
        try:
            finalStream = client.chat.completions.create(
                model=llm_as_a_judge,
                messages=[
                    {"role": "system", "content": llm_as_a_judge_system_prompt},
                    {"role": "user", "content": formatted_responses},
                ],
                stream=True,
                max_tokens=2048,
                temperature=0.7,
            )
            
            # Display aggregated response
            response_container = st.empty()
            full_response = ""
            for chunk in finalStream:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                response_container.markdown(full_response + "▌")
            response_container.markdown(full_response)
        except asyncio.TimeoutError:
            st.error("Timeout error during aggregation. Please try again later.")
        except Exception as e:
            st.error(f"Error in aggregation: {str(e)}")

    async def main():
        try:
            valid_results = await gather_model_responses()
            if not valid_results:
                st.error("All models failed to respond. Please try again later.")
                return
            await display_responses(valid_results)
            await aggregate_responses(valid_results)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

    if st.button("Get Answer"):
        if user_prompt:
            with st.spinner('Waiting for model responses...'):
                asyncio.run(main())
        else:
            st.warning("Please enter a question.")

else:
    st.warning("Please ensure you have set your Together API key in the environment variables.")

# Add some information about the app
st.sidebar.title("About this app")
st.sidebar.write(
    "This app is designed to have multiple models provide answers to a single question. "
    "The LLM-as-a-Judge then evaluates each of these answers and assigns a score based on specific criteria, "
    "such as readability, accuracy, coherence, and relevance. This approach aims to synthesize the strengths "
    "of various models to deliver a well-rounded and high-quality response."
)

st.sidebar.subheader("How it works:")
st.sidebar.markdown(
    """
    1. The app sends your question to multiple LLMs:
        - Qwen/Qwen2-72B-Instruct
        - deepseek-ai/DeepSeek-V3
        - mistralai/Mixtral-8x22B-Instruct-v0.1
        - meta-llama/Llama-3.3-70B-Instruct-Turbo
    2. Each model provides its own response
    3. The LLM-as-a-Judge then evaluates each of these answers and assigns a score based on the criteria.
    """
)

st.sidebar.write(
    "This approach allows for a more comprehensive and balanced answer by leveraging multiple AI models."
)