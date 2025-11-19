from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from ..config import LLM_MODEL, GROQ_API_KEY
from ..rag.vectorstore import get_retriever
from .state import AgentState

# Initialize the LLM
llm = ChatGroq(model=LLM_MODEL, groq_api_key=GROQ_API_KEY)

# 1. Planner
planner_prompt = ChatPromptTemplate.from_template(
    """You are an expert planner. Your job is to create a step-by-step plan to answer a complex question based on a set of documents.
    Question: {question}
    Plan:"""
)
planner = planner_prompt | llm | StrOutputParser()

# 2. Retriever
def retrieve(state: AgentState):
    retriever = get_retriever()
    documents = retriever.get_relevant_documents(state["question"])
    return {"documents": documents, "question": state["question"]}

# 3. Reasoning
reasoning_prompt = ChatPromptTemplate.from_template(
    """You are an expert researcher. Your job is to analyze a set of documents and a question, and then generate a detailed reasoning that will help answer the question.
    Question: {question}
    Documents:\n{documents}
    Reasoning:"""
)
reasoning_chain = reasoning_prompt | llm | StrOutputParser()

# 4. Answer
answer_prompt = ChatPromptTemplate.from_template(
    """You are an expert writer. Your job is to write a clear and concise answer to a question based on a set of documents and a reasoning.
    Question: {question}
    Documents:\n{documents}
    Reasoning:\n{reasoning}
    Answer:"""
)
answer_chain = answer_prompt | llm | StrOutputParser()

# 5. Critique
critique_prompt = ChatPromptTemplate.from_template(
    """You are an expert critic. Your job is to critique a draft answer to a question based on a set of documents and a reasoning.
    Question: {question}
    Documents:\n{documents}
    Reasoning:\n{reasoning}
    Draft Answer:\n{draft}
    Critique:"""
)
critique_chain = critique_prompt | llm | StrOutputParser()

# 6. Revise
revise_prompt = ChatPromptTemplate.from_template(
    """You are an expert writer. Your job is to revise a draft answer to a question based on a critique.
    Question: {question}
    Draft Answer:\n{draft}
    Critique:\n{critique}
    Revised Answer:"""
)
revise_chain = revise_prompt | llm | StrOutputParser()

# 7. Insights
insights_prompt = ChatPromptTemplate.from_template(
    """You are an expert analyst. Your job is to generate key insights from a revised answer.
    Revised Answer:\n{revised_draft}
    Insights (in bullet points):"""
)
insights_chain = insights_prompt | llm | StrOutputParser()

# 8. Summary
summary_prompt = ChatPromptTemplate.from_template(
    """You are an expert summarizer. Your job is to generate a concise summary of a revised answer.
    Revised Answer:\n{revised_draft}
    Summary:"""
)
summary_chain = summary_prompt | llm | StrOutputParser()

# 9. Research Notes
research_notes_prompt = ChatPromptTemplate.from_template(
    """You are an expert researcher. Your job is to generate research notes from a revised answer and a set of documents.
    Revised Answer:\n{revised_draft}
    Documents:\n{documents}
    Research Notes (in JSON format with 'note' and 'source' keys):"""
)
research_notes_chain = research_notes_prompt | llm | JsonOutputParser()

def plan(state: AgentState):
    plan_str = planner.invoke({"question": state["question"]})
    return {"plan": plan_str}

def reasoning(state: AgentState):
    reasoning_str = reasoning_chain.invoke({"question": state["question"], "documents": state["documents"]})
    return {"reasoning": reasoning_str}

def answer(state: AgentState):
    answer_str = answer_chain.invoke({"question": state["question"], "documents": state["documents"], "reasoning": state["reasoning"]})
    return {"draft": answer_str}

def critique(state: AgentState):
    critique_str = critique_chain.invoke({"question": state["question"], "documents": state["documents"], "reasoning": state["reasoning"], "draft": state["draft"]})
    return {"critique": critique_str}

def revise(state: AgentState):
    revised_draft_str = revise_chain.invoke({"question": state["question"], "draft": state["draft"], "critique": state["critique"]})
    return {"revised_draft": revised_draft_str}

def generate_insights(state: AgentState):
    insights_str = insights_chain.invoke({"revised_draft": state["revised_draft"]})
    return {"insights": insights_str}

def generate_summary(state: AgentState):
    summary_str = summary_chain.invoke({"revised_draft": state["revised_draft"]})
    return {"summary": summary_str}

def generate_research_notes(state: AgentState):
    research_notes_list = research_notes_chain.invoke({"revised_draft": state["revised_draft"], "documents": state["documents"]})
    return {"research_notes": research_notes_list}

def should_continue(state: AgentState):
    if "rework" in state["critique"].lower():
        return "continue"
    else:
        return "end"
