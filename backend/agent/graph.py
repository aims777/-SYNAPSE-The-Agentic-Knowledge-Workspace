from langgraph.graph import StateGraph, END
from .state import AgentState
from .pipeline import (
    plan,
    retrieve,
    reasoning,
    answer,
    critique,
    revise,
    generate_insights,
    generate_summary,
    generate_research_notes,
    should_continue
)

# Create the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("planner", plan)
workflow.add_node("retriever", retrieve)
workflow.add_node("reasoning", reasoning)
workflow.add_node("answer", answer)
workflow.add_node("critique", critique)
workflow.add_node("revise", revise)
workflow.add_node("insights", generate_insights)
workflow.add_node("summary", generate_summary)
workflow.add_node("research_notes", generate_research_notes)

# Build graph
workflow.set_entry_point("planner")
workflow.add_edge("planner", "retriever")
workflow.add_edge("retriever", "reasoning")
workflow.add_edge("reasoning", "answer")
workflow.add_edge("answer", "critique")
workflow.add_conditional_edges(
    "critique",
    should_continue,
    {
        "continue": "revise",
        "end": "insights",
    },
)
workflow.add_edge("revise", "answer")
workflow.add_edge("insights", "summary")
workflow.add_edge("summary", "research_notes")
workflow.add_edge("research_notes", END)

# Compile the graph
app = workflow.compile()
