"""Tools ที่ agent ใช้ได้"""

from langchain_core.tools import tool

KNOWLEDGE_BASE: dict[str, str] = {
    "langgraph": (
        "LangGraph is a framework for building stateful, multi-actor "
        "applications with LLMs. It models agent workflows as a graph of "
        "nodes and edges, with built-in support for cycles, persistence "
        "(checkpointing), and human-in-the-loop."
    ),
    "langchain": (
        "LangChain is a framework for developing applications powered by "
        "large language models. It provides abstractions for models, "
        "prompts, output parsers, tools, retrieval, and agents."
    ),
}


@tool
def search_docs(query: str) -> str:
    """Search internal documentation for a given topic.

    Use this to answer questions about LangChain or LangGraph.

    Args:
        query: The topic or keyword to search for in the docs.
    """
    query_lower = query.lower()
    for keyword, answer in KNOWLEDGE_BASE.items():
        if keyword in query_lower:
            return answer
    return f'No documentation found for "{query}".'
