from fastapi import FastAPI, Query
import requests
from dotenv import load_dotenv
from pathlib import Path
import os
from datetime import datetime, timedelta

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

@app.get("/weather")
def get_weather(city: str = Query(..., description="City to get current weather for")):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            return {
                "response": f"Weather in {city}: {description}, {temperature}°C"
            }
        else:
            return {
                "error": f"Could not retrieve weather for {city}. Reason: {data.get('message', 'Unknown error')}."
            }
    except Exception as e:
        return {
            "error": f"Error occurred while fetching weather data: {str(e)}"
        }

@app.get("/forecast")
def get_forecast(city: str):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
            forecast_list = data["list"]
            result = []
            for entry in forecast_list[:8]:  # First 8 entries (~24 hours)
                utc_time = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
                ist_time = utc_time + timedelta(hours=5, minutes=30)
                result.append({
                    "time (indian)": ist_time.strftime("%Y-%m-%d %I:%M %p IST"),
                    "temperature": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"].capitalize()
                })
            return {"forecast": result}
    else:
        return {"error": f"Could not retrieve weather forecast for {city}. Reason: {data.get('message', 'Unknown error')}."}
