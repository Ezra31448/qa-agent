"""QA agent หลัก สร้างด้วย LangChain v1 prebuilt agent (ทำงานบน LangGraph)"""

import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from qa_agent.tools import search_docs

SYSTEM_PROMPT = (
    "You are a helpful QA assistant. "
    "Always use the `search_docs` tool to look up documentation "
    "before answering questions. "
    "If the docs do not contain the answer, say you don't know."
)

# in-memory checkpoint ให้ agent จำสถานะของ conversation ได้ (per thread)
# (ชื่อเดิม MemorySaver ถูกเปลี่ยนเป็น InMemorySaver ใน LangGraph 1.0)
_checkpointer = InMemorySaver()


def create_qa_agent():
    """สร้าง tool-calling agent สำหรับตอบคำถาม (QA agent)"""
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
    )
    return create_agent(
        llm,
        tools=[search_docs],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=_checkpointer,
    )


def run_qa_agent(question: str, thread_id: str = "default-thread") -> str:
    """รัน QA agent ด้วยคำถาม แล้วคืนคำตอบเป็น string

    Args:
        question: คำถามจากผู้ใช้
        thread_id: id ของ conversation thread (สำหรับ persistence)
    """
    agent = create_qa_agent()
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"configurable": {"thread_id": thread_id}},
    )
    return result["messages"][-1].content
