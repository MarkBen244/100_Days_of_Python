import requests
from datetime import datetime

MY_LAT = 47.533340
MY_LOG = 21.625210
parameters = {"lat": MY_LAT, "log": MY_LOG, "formatted": 0}
response = requests.get(
    "https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
