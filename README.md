# Document Reader - automated with n8n

Local and containerized **RAG system** using n8n, Ollama, and Qdrant that ingests PDFs of the Declaration of Independence and provides expert-level answers through a chat interface.

![AI Starter Kit](https://raw.githubusercontent.com/Tony-91/Ai_starter/main/assets/n8n-demo.gif)
# N8n Architecture Overview
![AI Starter Kit](https://github.com/Tony-91/RAG_PDF_Reader/blob/main/assets/n8n.png)
A local, containerized RAG (Retrieval Augmented Generation) system using:
* n8n for workflow automation
* Ollama for local LLM processing
* Qdrant as your vector database
* LangChain for document processing

# Key Components
## 1. Document Ingestion Flow
* Web Form Interface for PDF uploads
* PDF Processing with binary data handling
* Text Splitting (400-character chunks with 100-character overlap)
* Vector Embeddings using mxbai-embed-large model
* Vector Storage in Qdrant collection named "rag_chatbot"
## 2. Chat Interface
* Chat UI for user interactions
* Local LLM using llama3.2 model
* Conversation Memory for context
* Vector Search for document retrieval
## 3. AI Configuration
* System Prompt focused on Declaration of Independence expertise
* Context-aware responses with source document references
* Fallback handling for out-of-scope queries

# Technical Highlights
## Local-First Approach
* All services run in Docker containers
* No external API dependencies
* Full data privacy and control
## Performance Optimizations
* Efficient chunking strategy (400/100)
* Local model inference
* Vector similarity search for relevant context
## User Experience
* Simple web form for document upload
* Natural language chat interface
* Context-aware responses

# Why This Setup Rocks
1. Privacy: All processing happens locally
2. Customization: Fine-tuned for historical documents
3. Scalable: Easy to add more documents or adjust parameters
4. Maintainable: Containerized for simple updates
