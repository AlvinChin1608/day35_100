import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Get your API keys from OpenWeatherMap and Twilio
# Eg, API_KEY = "2134324234"
# I use the env method to retrieve my API key
# instead of hard coded in the main, Google search dotenv
API_KEY = os.getenv("OWN_KEY")
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH')

parameters = {
    "lat": 1.6561,
    "lon": 103.6036,
    "appid": API_KEY,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
weather_data = response.json()
# rain = weather_data["list"][0]["weather"][0]["id"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 600:
        will_rain = True  # check if it will rain in the next 12 hours
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Today is going to rain, remember to bring an umbrella ☔️',
        to='whatsapp:+601111579619'
    )
    print(message.status)
