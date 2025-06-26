# Workout Planner Agent
from fastmcp import FastMCP
mcp=FastMCP("WorkoutPlannerAgent")
@mcp.tool()
def workout_planner_agent(query: str) -> str:
    """Make the schedule for workout for the user according to his demand."""
    return "Here is your workout schedule according to your demand."
if __name__ == "__main__":
    mcp.run(
        transport="stdio"
    )