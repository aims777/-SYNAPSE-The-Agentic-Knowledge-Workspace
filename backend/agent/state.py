from typing import List, TypedDict
from langchain_core.documents import Document

class AgentState(TypedDict):
    question: str
    documents: List[Document]
    plan: str
    draft: str
    critique: str
    content: List[str]
    revised_draft: str
    insights: str
    summary: str
    research_notes: List[dict]
