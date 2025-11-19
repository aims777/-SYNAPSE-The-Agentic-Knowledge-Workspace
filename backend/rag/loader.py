from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
import os
from typing import List

SUPPORTED_DOC_TYPES = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
}

def load_documents(temp_filepath: str) -> List[Document]:
    """Loads documents from a temporary file path."""
    ext = os.path.splitext(temp_filepath)[1].lower()
    if ext not in SUPPORTED_DOC_TYPES:
        raise ValueError(f"Unsupported document type: {ext}")
    
    loader = SUPPORTED_DOC_TYPES[ext](temp_filepath)
    return loader.load()
