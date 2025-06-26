from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/health_check")
def health_check_agent(query: str = Query(..., description="Your health-related question")):
    """Provide health tips and advice based on user queries."""
    return {
        "response": "Stay hydrated, eat balanced meals, exercise regularly, and get enough sleep. If you have specific health concerns, please consult a healthcare professional."
    }