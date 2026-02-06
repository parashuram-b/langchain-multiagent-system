# LangChain Multi-Agent & Conversational AI System

## Overview
This project contains two AI systems built using LangChain and LangGraph.

---

## Task 2: Conversational Knowledge Bot
A RAG-based chatbot using FAISS and Ollama with conversational memory.

### Features
- LangChain ConversationalRetrievalChain
- FAISS vector database
- Ollama local LLM
- Memory support

Folder: task2_knowledge_bot/

---

## Task 1: Multi-Agent System
A LangGraph-based multi-agent workflow.

### Agents
- Planner
- Researcher
- Reasoner
- Responder

Folder: task1_multi_agent/

## Technologies
- Python
- LangChain
- LangGraph
- FAISS
- Ollama


## Architecture Flow
User Query  
→ Intent Routing  
→ Tool Execution (Calculator) **OR** Knowledge Retrieval (FAISS)  
→ LLM Response (Ollama)  
→ Conversation Memory Update

## Enhancements 
- Multi-document knowledge ingestion using DirectoryLoader
- FAISS-based vector store for efficient retrieval
- Tool integration (calculator) for computation-based queries
- Intelligent query routing (tool vs retrieval)
- Modular architecture for future LangGraph-based agent orchestration

## Sample Queries
- What is LangChain?
- Explain LangGraph
- What does this chatbot support?
- Calculate 25 * 4

## Future Scope
- Persistent memory using databases (Redis / SQLite)
- Full LangGraph-based orchestration of the chatbot
- Web UI using Streamlit or Gradio
- Deployment on cloud platforms

## Author
B Parashuram
