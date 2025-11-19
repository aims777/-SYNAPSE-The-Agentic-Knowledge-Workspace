import chromadb
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from typing import List

from .embedder import get_embedding_function
from ..config import VECTOR_STORE_PATH

_embedding_function = get_embedding_function()
_persistent_client = chromadb.PersistentClient(path=VECTOR_STORE_PATH)

_vector_store = Chroma(
    client=_persistent_client,
    collection_name="synapse_collection",
    embedding_function=_embedding_function,
)

def add_documents(documents: List[Document]):
    """Adds documents to the vector store."""
    _vector_store.add_documents(documents)

def get_retriever(k_value: int = 4):
    """Returns a retriever for the vector store."""
    return _vector_store.as_retriever(search_kwargs={"k": k_value})
