
import streamlit as st
import ollama

st.title("Gemma Local Chatbot")

# Set the model
model = "gemma:2b"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Call Ollama API
        try:
            # check if model is available, if not show warning (or it might pull? no, better to rely on pre-pull)
            stream = ollama.chat(
                model=model,
                messages=[{'role': m['role'], 'content': m['content']} for m in st.session_state['messages']],
                stream=True,
            )
            
            for chunk in stream:
                if chunk['message']['content']:
                    full_response += chunk['message']['content']
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error connecting to Ollama: {e}")
            full_response = "Error connecting to local model.\nMake sure Ollama is running and you have pulled the model (`ollama pull gemma:2b`)."

    st.session_state["messages"].append({"role": "assistant", "content": full_response})
