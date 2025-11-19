from langchain_community.embeddings import SentenceTransformerEmbeddings
from ..config import EMBEDDING_MODEL

def get_embedding_function():
    """Initializes and returns the embedding function."""
    return SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)
