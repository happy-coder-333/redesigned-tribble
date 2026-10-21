import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

def get_temperature(city:str):
    """Get the weather in any city"""
    return f"It's always sunny in {city}!"

if not os.environ.get("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY is not set in this shell session.")

agent = create_agent(
    ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    tools=[get_temperature],
    system_prompt="You are a Helpful Agent."
)

print(agent.invoke({
    "messages": [{
        "role": "user",
        "content": "What is the weather in delhi"
    }]
})["messages"][-1].content)

def main():
    print("Hello from playground!")



if __name__ == "__main__":
    main()
