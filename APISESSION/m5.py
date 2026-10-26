import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("OWN_KEY")
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": "Kolkata,IN", "appid": key, "units": "metric"},
    timeout=10,
)
 
print("HTTP status:", response.status_code)
print("OpenWeather response:", response.text)
