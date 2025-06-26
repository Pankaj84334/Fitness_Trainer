from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_swarm
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
import asyncio
import os
from queries import queries
from  tool_wrappers import (
    calculator_agent,weather_agent,general_agent,health_check_agent,
) 
load_dotenv()
async def main():
    query = queries[2]
    messages = [{"role": "user", "content": query}]
    swarm = create_swarm(
        agents=[calculator_agent, weather_agent, general_agent, health_check_agent],
        default_active_agent="calculator_agent"
    ).compile()
    response = await swarm.ainvoke({"messages": messages})
    tool_messages = [m for m in response["messages"] if isinstance(m, ToolMessage)]

    print("Tool used:")
    for t in tool_messages:
        print(t.name)

    print("\nResponse:")
    print(response["messages"][-1].content)

asyncio.run(main())
