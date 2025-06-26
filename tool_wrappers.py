from langchain_core.tools import tool
import requests
from langgraph_swarm import create_handoff_tool
from langchain_groq import ChatGroq
groq = ChatGroq(model="qwen-qwq-32b", temperature=0.0)
from langgraph.prebuilt import create_react_agent
# -------------------------------calculator_tool---------------------------------
@tool
def add(a: int, b: int) -> str:
    """Adds two numbers."""
    res = requests.get("http://localhost:8001/add", params={"a": a, "b": b})
    return res.json().get("response", "No response.")
@tool
def subtract(a:int,b:int)-> str:
    """Subtracts two numbers."""
    res = requests.get("http://localhost:8001/subtract", params={"a": a, "b": b})
    return res.json().get("response", "No response.")
@tool
def multiply(a:int,b:int)-> str:
    """Multiplies two numbers."""
    res = requests.get("http://localhost:8001/multiply", params={"a": a, "b": b})
    return res.json().get("response", "No response.")
@tool
def divide(a:int,b:int)-> str:
    """Divides two numbers."""
    res = requests.get("http://localhost:8001/divide", params={"a": a, "b": b})
    return res.json().get("response", "No response.")

# -------------------------------weather_tool---------------------------------
@tool
def get_weather(city: str) -> str:
    """Provides current weather of a city."""
    res = requests.get("http://localhost:8002/weather", params={"city": city})
    return res.json().get("response", "No response.")
@tool
def get_forecast(city: str) -> str:
    """Provides weather forecast of a city."""
    res = requests.get("http://localhost:8002/forecast", params={"city": city})
    return res.json().get("response", "No response.")

# -------------------------------health_check_tool---------------------------------
@tool
def health_check_agent(query: str) -> str:
    """Provides health tips and wellness advice."""
    res = requests.get("http://localhost:8003/health_check", params={"query": query})
    return res.json().get("response", "No response.")

# -------------------------------general_tool---------------------------------
@tool
def general_agent(query: str) -> str:
    """Handles general-purpose queries not specific to math, health, or weather."""
    res = requests.get("http://localhost:8004/general", params={"query": query})
    return res.json().get("response", "No response.")

# -----------------------------------handoff_tools---------------------------------------
to_calculator = create_handoff_tool(
    agent_name="calculator_agent",
    description="Transfer user to the calculator agent.",
)
to_weather = create_handoff_tool(
    agent_name="weather_agent",
    description="Transfer user to the weather agent.",
)
to_health_check = create_handoff_tool(
    agent_name="health_check_agent",
    description="Transfer user to the health check agent.",
)
to_general = create_handoff_tool(
    agent_name="general_agent",
    description="Transfer user to the general agent.",
)
# -----------------------------------agents---------------------------------------
calculator_agent = create_react_agent(
    groq,
    tools=[add, subtract, multiply, divide, to_health_check, to_weather, to_general],
    prompt="You are a calculator agent that can perform basic arithmetic operations. Use the tools provided to answer user queries.",
    name="calculator_agent",
)
weather_agent = create_react_agent(
    groq,
    tools=[get_weather, get_forecast, to_calculator, to_health_check, to_general],
    prompt="You are a weather agent that can provide current weather and forecasts. Use the tools provided to answer user queries.",
    name="weather_agent",
)
health_check_agent = create_react_agent(
    groq,
    tools=[health_check_agent, to_calculator, to_weather, to_general],
    prompt="You are a health check agent that can provide health tips and wellness advice. Use the tools provided to answer user queries.",
    name="health_check_agent",
)
general_agent = create_react_agent(
    groq,
    tools=[general_agent, to_calculator, to_health_check, to_weather],
    prompt="You are a general agent that can handle various queries not specific to math, health, or weather. Use the tools provided to answer user queries.",
    name="general_agent",
)

