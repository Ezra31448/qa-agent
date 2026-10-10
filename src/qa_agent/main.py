"""Entry point ของ QA agent — รันด้วย `qa-agent` หรือ `python -m qa_agent`"""

import sys

from dotenv import load_dotenv

from qa_agent.agent import run_qa_agent

load_dotenv()


def main() -> None:
    question = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "What is LangGraph?"
    )
    print(f"\n❓ Question: {question}\n")
    answer = run_qa_agent(question)
    print(f"\n✅ Final answer:\n{answer}\n")


if __name__ == "__main__":
    main()
