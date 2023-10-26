import os
import sys

# Stream lit cloud sqlite version upgrade
if sys.platform  != 'darwin':
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from embedchain import App
import streamlit as st




with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/bistecglobal/hello-embedchain/blob/main/app.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/bistecglobal/hello-embedchain?quickstart=1)"

st.title("💬 Focus Digitech Assistant") 

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "I can answer questions about focus digitech"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    os.environ["OPENAI_API_KEY"]  = openai_api_key

    bistec_bot = App()

    bistec_bot.add("https://focusdigitech.com/home")
    bistec_bot.add("https://focusdigitech.com/investors-relations")
    bistec_bot.add("https://focusdigitech.com/grants")
    bistec_bot.add("https://focusdigitech.com/cybersecurity")

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = bistec_bot.query(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)