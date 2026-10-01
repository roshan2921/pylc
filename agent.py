"""Simple LangChain agent powered by Google Gemini."""

import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


def get_current_time() -> str:
    """Return the current date and time in UTC."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def calculate(expression: str) -> str:
    """Evaluate a basic math expression. Supports +, -, *, /, and parentheses."""
    allowed = set("0123456789+-*/(). ")
    if not all(char in allowed for char in expression):
        return "Error: expression contains unsupported characters."
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as exc:
        return f"Error: {exc}"


def build_agent():
    """Create a LangChain agent that uses Gemini as the LLM."""
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0,
    )

    return create_agent(
        model=model,
        tools=[get_current_time, calculate],
        system_prompt=(
            "You are a helpful assistant. Use tools when needed to answer "
            "questions accurately. Keep responses concise."
        ),
    )


def main():
    agent = build_agent()

    query = input("You: ").strip()
    if not query:
        print("Please enter a question.")
        return

    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(f"Agent: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()
