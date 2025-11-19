import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model configuration
LLM_MODEL = "llama3-70b-8192"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vector store configuration
VECTOR_STORE_PATH = "C:/Users/User/CascadeProjects/synapse/chroma_db"

# RAG configuration
CHUNK_SIZE = 1024
CHUNK_OVERLAP = 128

# API configuration
API_HOST = "0.0.0.0"
API_PORT = 8000
