# Python LangChain Basics — Gemini Agent

A minimal LangChain agent that uses Google Gemini as the LLM and can call simple tools.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy the example env file and add your [Google AI API key](https://aistudio.google.com/apikey):

```bash
cp .env.example .env
```

3. Set `GOOGLE_API_KEY` in `.env`.

## Run

```bash
python agent.py
```

Example prompts:

- `What time is it right now?`
- `What is 15 * 24 + 7?`

## How it works

- **LLM**: `ChatGoogleGenerativeAI` from `langchain-google-genai` (Gemini 2.0 Flash)
- **Agent**: `create_agent` from LangChain — a ReAct-style loop that decides when to call tools
- **Tools**: `get_current_time` and `calculate`
