# Rain Detector

## About the Project

Rain Detector is a Python script that checks the weather for a configured location and sends an SMS through Twilio when the returned weather code indicates rain or another precipitation condition.

The project practices working with a weather API, reading JSON responses, and sending messages with the Twilio API.

## How It Works

`main.py` sends the latitude and longitude to OpenWeatherMap, checks the weather code in the response, and sends an SMS if the code is below `700`. The script then prints the SMS status and message SID.

The location, phone numbers, and SMS body are configured in `main.py`.

## Requirements

- Python 3
- An OpenWeatherMap API key
- A Twilio account SID and auth token
- A Twilio phone number with SMS capability
- The Python packages listed in `requirements.txt`

Install the packages from the project folder:

```bash
pip install -r requirements.txt
```

## Credentials

Copy `.env.example` to `.env` and fill in your own OpenWeatherMap and Twilio credentials. `main.py` loads these values with `python-dotenv` and `os.getenv()`. The `.env` file is ignored by Git; keep it private and never commit it.

## How to Run

From this folder, run:

```bash
python main.py
```

The script needs an internet connection and valid API credentials. If rain is detected, Twilio sends an SMS to the configured recipient.

## Project Structure

```text
Day 36 --Rain Detector/
├── main.py
├── .env.example
└── requirements.txt
```

## What I Learned

- Making HTTP requests with `requests`
- Passing query parameters to an API
- Handling JSON API responses
- Using weather codes to make a decision
- Sending SMS messages with Twilio
