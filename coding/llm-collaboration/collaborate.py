import streamlit as st
import asyncio
import os
from together import AsyncTogether, Together
import logging

# Set up the Streamlit app
st.title("LLM Pair Programming App")

# Get API key from environment variable
together_api_key = os.getenv("TOGETHER_API_KEY")

if together_api_key:
    client = Together()
    async_client = AsyncTogether()

    # Define the models for the collaboration
    coder_model = "Qwen/Qwen2-72B-Instruct"
    reviewer_model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"

    # Get user input
    user_prompt = st.text_input("Enter your coding task:")

    async def collaborate_models():
        """
        Facilitate a pair programming session between two models: one writing code and the other reviewing it.
        """
        initial_prompt = user_prompt
        current_response = initial_prompt
        max_iterations = 5
        iteration = 0

        st.subheader("Pair Programming Session:")
        response_container = st.empty()
        full_response = ""

        while iteration < max_iterations:
            # Model 1 writes code
            coder_prompt = f"Write code for the following task: {current_response}"
            try:
                coder_response = await async_client.chat.completions.create(
                    model=coder_model,
                    messages=[
                        {"role": "system", "content": "You are an expert software developer. When given a task, write clean, readable, and well-documented code that solves the problem. Provide ONLY the code implementation without any explanations or markdown. Include helpful comments where needed to explain complex logic."},
                        {"role": "user", "content": coder_prompt}
                    ],
                    temperature=0.8,
                    max_tokens=1024,
                )
                coder_content = coder_response.choices[0].message.content
                full_response += f"**{coder_model} Code:**\n{coder_content}\n\n"
                response_container.markdown(full_response + "▌")
            except Exception as e:
                logging.error(f"Error with {coder_model}: {str(e)}")
                st.error(f"Error with {coder_model}: {str(e)}")
                break

            # Model 2 reviews the code
            reviewer_prompt = f"Review the following code for errors, improvements, and better documentation: {coder_content}"
            try:
                reviewer_response = await async_client.chat.completions.create(
                    model=reviewer_model,
                    messages=[
                        {"role": "system", "content": "You are an expert software developer. When given a code, review it for errors, improvements, and better documentation. Provide ONLY the review comments.If you don't see any issues, just say 'complete'"},
                        {"role": "user", "content": reviewer_prompt}
                    ],
                    temperature=0.8,
                    max_tokens=1024,
                )
                reviewer_content = reviewer_response.choices[0].message.content
                full_response += f"**{reviewer_model} Review:**\n{reviewer_content}\n\n"
                response_container.markdown(full_response + "▌")
            except Exception as e:
                logging.error(f"Error with {reviewer_model}: {str(e)}")
                st.error(f"Error with {reviewer_model}: {str(e)}")
                break

            # Check for consensus or improvements
            set_of_words = ["agree", "good", "correct", "perfect", "excellent", "great", "well done", "well done", "complete"]
            if any(word in reviewer_content.lower() for word in set_of_words):
                full_response += "**Consensus reached.**\n"
                response_container.markdown(full_response)
                break

            # Prepare for next iteration
            current_response = reviewer_content
            iteration += 1

        if iteration == max_iterations:
            full_response += "**Max iterations reached without consensus.**\n"
            response_container.markdown(full_response)

    async def main():
        try:
            if user_prompt:
                await collaborate_models()
            else:
                st.warning("Please enter a coding task.")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

    if st.button("Start Collaboration"):
        asyncio.run(main())

else:
    st.warning("Please ensure you have set your Together API key in the environment variables.")

# Add some information about the app
st.sidebar.title("About this app")
st.sidebar.write(
    "This app is designed to facilitate a pair programming session between two models. "
    "One model writes code, and the other reviews it, suggesting improvements until a consensus is reached."
)

st.sidebar.subheader("How it works:")
st.sidebar.markdown(
    """
    1. The app sends your coding task to two LLMs:
        - Qwen/Qwen2-72B-Instruct
        - deepseek-ai/DeepSeek-V3
    2. The first model writes code.
    3. The second model reviews the code and suggests improvements.
    4. The process continues until a consensus is reached or a maximum number of iterations is completed.
    """
)

st.sidebar.write(
    "This approach allows for a collaborative and iterative refinement of code by leveraging multiple AI models."
)