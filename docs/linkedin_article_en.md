# 🤖 Build Your Own Local AI Chatbot in Minutes: Python + Ollama + Gemma

Are you worried about data privacy when using AI? Or do you simply want an intelligent assistant that runs 100% offline on your laptop?

I've recently been experimenting with running **LLMs (Large Language Models)** locally, and the results are surprising. In this article, I want to share how you can build your own chatbot using **Gemma** (Google's open model), **Ollama**, and **Streamlit**.

## Why Local?

Beyond the hype, running models on your own infrastructure (or laptop) has clear advantages:
- **Total Privacy**: Your data never leaves your machine. Ideal for consulting or handling sensitive information.
- **Zero Cost**: No API bills per token.
- **Latency**: Immediate response without depending on your internet connection.

## The Tech Stack

For this project, I used:
1.  **[Ollama](https://ollama.com)**: The ultimate tool for managing and running LLMs locally (Windows/Mac/Linux).
2.  **[Gemma:2b](https://blog.google/technology/developers/gemma-open-models/)**: The lightweight version of Google's model, optimized to run on consumer hardware.
3.  **Python + Streamlit**: To create the chat interface in less than 50 lines of code.

## Step by Step

### 1. Preparing the Engine: Ollama
First, install Ollama and download the model. From your terminal:

```bash
ollama pull gemma:2b
```

This command downloads the model (about 1.7GB) and gets it ready to use.

### 2. The Code (Python)

The magic happens in a very simple Python script. We use the official `ollama` Python library and `streamlit` for the UI.

Here is the basic structure of `chatbot_app.py`:

```python
import streamlit as st
import ollama

st.title("🤖 Gemma Local Chatbot")

# Initialize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input
if prompt := st.chat_input("Write your message..."):
    # Save and display user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Call Ollama in stream mode
        stream = ollama.chat(
            model='gemma:2b',
            messages=st.session_state['messages'],
            stream=True,
        )
        
        for chunk in stream:
            content = chunk['message']['content']
            if content:
                full_response += content
                message_placeholder.markdown(full_response + "▌")
                
        message_placeholder.markdown(full_response)
    
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
```

### 3. Run it!

With a simple line in the terminal, your chatbot comes to life:

```bash
streamlit run chatbot_app.py
```

## Results

Using the `gemma:2b` model, the speed is impressive even on computers without a powerful dedicated GPU. The reasoning capability is sufficient for assistance tasks, summarization, and creative text generation.

This small project demonstrates that **Sovereign AI** is accessible today for any developer. We no longer rely exclusively on big APIs to integrate intelligence into our applications.

---
Have you tried running models locally? What use would you give it in your professional environment? 👇

#AI #LocalLLM #Python #Ollama #Gemma #DataPrivacy #DevCommunity
