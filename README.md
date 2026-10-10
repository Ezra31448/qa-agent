# qa-agent

QA agent built with [LangChain](https://python.langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/) (Python).

## Setup

```bash
# สร้าง virtual environment และติดตั้ง dependencies (แนะนำ uv)
uv sync
# หรือด้วย pip
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

> หมายเหตุ: dependencies อยู่ใน `[dependency-groups]` ตาม PEP 735 —
> ถ้าใช้ pip ให้ติดตั้ง dev tools แยกด้วย `pip install ruff pytest`

คัดลอก `.env.example` เป็น `.env` แล้วใส่ `OPENAI_API_KEY`:

```bash
cp .env.example .env
```

## Usage

```bash
# รันด้วยคำถาม default
qa-agent

# หรือส่งคำถามเข้าไป
qa-agent "What is LangChain?"

# หรือรันเป็น module
python -m qa_agent "What is LangGraph?"
```

## Project structure

```
src/qa_agent/
├── __init__.py   # package metadata
├── main.py       # CLI entry point
├── agent.py      # LangChain create_agent (LangGraph runtime)
└── tools.py      # agent tools (@tool)
```

## Development

```bash
ruff check src/     # lint
pytest              # tests (ยังไม่มี test ในตอนนี้)
```
