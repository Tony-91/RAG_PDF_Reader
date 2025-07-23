import streamlit as st
import requests
import os
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App title and description
st.set_page_config(page_title="PDF Ai Agent", page_icon="📄")
st.title("📄 PDF Ai Agent")
st.markdown("Upload PDF and ask questions about it")

# Sidebar for API configuration
with st.sidebar:
    st.header("Settings")
    n8n_webhook_url = st.text_input(
        "n8n Webhook URL",
        value=os.getenv("N8N_WEBHOOK_URL", "http://n8n:5678/webhook-test/rag-pdf"),
        help="URL of your n8n webhook endpoint"
    )

# File upload section
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about the PDF"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare data for n8n webhook
    data = {
        "fields": {
            "choose pdf": [
                {
                    "name": uploaded_file.name if uploaded_file else None,
                    "type": "application/pdf",
                    "data": base64.b64encode(uploaded_file.getvalue()).decode('utf-8') if uploaded_file else None
                }
            ]
        },
        "question": prompt
    }
    
    # Show loading indicator
    with st.chat_message("assistant"):
        with st.spinner("Analyzing document..."):
            try:
                # Call n8n webhook
                response = requests.post(n8n_webhook_url, json=data)
                response.raise_for_status()
                
                # Display assistant response
                response_data = response.json()
                assistant_response = response_data.get("output", response_data.get("answer", "I couldn't find an answer in the document."))
                
                # Extract text if the response is a dictionary with a text field
                if isinstance(assistant_response, dict) and 'text' in assistant_response:
                    assistant_response = assistant_response['text']
                
                st.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
