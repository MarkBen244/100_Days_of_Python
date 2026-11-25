import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("OPENWEATHER_API_KEY")
account_id = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

if not all((api_key, account_id, auth_token)):
    raise RuntimeError(
        "Set OPENWEATHER_API_KEY, TWILIO_ACCOUNT_SID, and TWILIO_AUTH_TOKEN "
        "in Day 36 --Rain Detector/.env"
    )


MY_LAT = 47.181759
MY_LOG = 19.506094
parameters = {
    "lat": MY_LAT,
    "lon": MY_LOG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()


weather_code = weather_data["weather"][0]["id"]
weather_data["weather"][0]["description"]

if weather_code < 700:
    client = Client(account_id, auth_token)
    message = client.messages.create(
        to="+36204473684",
        from_="+4915888623971",
        body="sms_appointment_reminders",
    )

print(message.status)

print(message.sid)
