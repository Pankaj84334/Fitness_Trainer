from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.post('/general')
def general_agent(query: str) -> str:
    """Handle general queries that are neither related to arithmetic operations nor related to the weather."""
    
    # You can expand this logic to categorize or forward specific queries
    generic_responses = [
        "This question is outside the scope of math and weather, but I'm a general AI and happy to help!",
        "That doesn't seem related to weather or math — but no worries, I'm equipped to assist with general queries too!",
        "Looks like this isn't a math or weather question. Luckily, I'm a general-purpose AI and can still help you!",
        "Hmm... not a math or weather question. But I'm here for all sorts of questions — let's dive in!",
        "Interesting! It's outside weather and math, but I'm a general AI agent ready to help you anyway!"
    ]

    # For now, just return a placeholder message with a friendly tone
    return random.choice(generic_responses)