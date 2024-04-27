import streamlit as st
import os
from groq import Groq

# Load environment variables
GROQ_API_KEY = #"Enter api key"

PRE_PROMPT = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as Assistant."

if not GROQ_API_KEY:
    st.warning("Please add your Groq API key to the .env file.")
    st.stop()

# Connect to Groq
client = Groq(api_key=GROQ_API_KEY)

def render_app():
    # Set up Streamlit app
    st.set_page_config(page_title="LLaMA GPT - 3", page_icon="🦙", layout="wide")

    st.title("LLaMA GPT - 3")

    # reduce font sizes for input text boxes
    custom_css = """
        <style>
            .stTextArea textarea {font-size: 13px;}
            div[data-baseweb="select"] > div {font-size: 13px !important;}
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Left sidebar menu
    st.sidebar.header("LLaMA3 Chatbot")

    # Set config for a cleaner menu, footer & background:
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # container for the chat history
    response_container = st.container()
    # container for the user's text input
    container = st.container()
    # Set up/Initialize Session State variables
    if 'chat_dialogue' not in st.session_state:
        st.session_state['chat_dialogue'] = []
    if not st.session_state['chat_dialogue']:
        st.session_state['chat_dialogue'].append({"role": "assistant", "content": "Hello! I'm LLaMA GPT - 3, an AI assistant. How can I help you today?"})
    if 'temperature' not in st.session_state:
        st.session_state['temperature'] = 0.1
    if 'top_p' not in st.session_state:
        st.session_state['top_p'] = 0.9
    if 'max_seq_len' not in st.session_state:
        st.session_state['max_seq_len'] = 512
    if 'pre_prompt' not in st.session_state:
        st.session_state['pre_prompt'] = PRE_PROMPT
    if 'selected_model' not in st.session_state:
        st.session_state['selected_model'] = 'llama3-70b-8192'

    # Model hyperparameters
    st.session_state['temperature'] = st.sidebar.slider('Temperature:', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    st.session_state['top_p'] = st.sidebar.slider('Top P:', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    st.session_state['max_seq_len'] = st.sidebar.slider('Max Sequence Length:', min_value=64, max_value=4096, value=2048, step=8)

    model_options = ['llama3-70b-8192', 'llama3-8b-8192']
    st.session_state['selected_model'] = st.sidebar.selectbox('Select Model:', model_options, index=0)

    NEW_P = st.sidebar.text_area('Prompt before the chat starts. Edit here if desired:', PRE_PROMPT, height=60)
    if NEW_P != PRE_PROMPT and NEW_P != "" and NEW_P != None:
        st.session_state['pre_prompt'] = NEW_P + "\n\n"
    else:
        st.session_state['pre_prompt'] = PRE_PROMPT

    btn_col1, _ = st.sidebar.columns(2)

    # Add the "Clear Chat History" button to the sidebar
    def clear_history():
        st.session_state['chat_dialogue'] = []
    clear_chat_history_button = btn_col1.button("Clear History",
                                            use_container_width=True,
                                            on_click=clear_history)

    # add links to relevant resources for users to select
    st.sidebar.write(" ")

    logo1 = 'https://storage.googleapis.com/llama2_release/a16z_logo.png'
    logo2 = 'https://storage.googleapis.com/llama2_release/Screen%20Shot%202023-07-21%20at%2012.34.05%20PM.png'

    st.sidebar.write(" ")

    # Display chat messages from history on app rerun
    for message in st.session_state.chat_dialogue:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
             # Accept user input
    if prompt := st.chat_input("Message LLaMA 3x...."):
        # Add user message to chat history
        st.session_state.chat_dialogue.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.chat_dialogue]
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=st.session_state['selected_model'],
                temperature=st.session_state['temperature'],
                top_p=st.session_state['top_p'],
                max_tokens=st.session_state['max_seq_len']
            )
            full_response = chat_completion.choices[0].message.content
            message_placeholder.markdown(full_response)

        # Add assistant response to chat history
        st.session_state.chat_dialogue.append({"role": "assistant", "content": full_response})

render_app()
