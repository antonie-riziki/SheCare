
#!/usr/bin/env python3
import sys
import streamlit as st


sys.path.insert(1, './modules')

from func import get_gemini_response


st.set_page_config(
    page_title="SheCare",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="center",
    menu_items={
        'Get Help': 'https://wa.me/254743158232',
        'Report a bug': "https://wa.me/254743158232",
        'About': " **SheCare💕** is an AI powered assistant built for women - accessible anytime via Whatsapp. \nWe help you check symptoms, find trusted clinics, and get guidance in private, simple and supportive way. \nNo downloads, No stigma -- Just Care on your terms"
    }
)

st.image("https://www.bbh.com/content/dam/bbh/external/www/capital-partners/private-banking/insights/closing-the-womens-health-gap/Closing%20the%20Womens%20Health%20Gap-Social.jpg", width=900)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "SheCare💕 \nHow may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})







