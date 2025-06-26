import subprocess

agents = {
    "calculator_agent": 8001,
    "weather_agent": 8002,
    "health_check_agent": 8003,
    "general_agent": 8004,
}

for agent, port in agents.items():
    subprocess.Popen([
        "uvicorn",
        f"agents.{agent}:app",
        "--host", "127.0.0.1",
        "--port", str(port),
        "--reload",
    ])
