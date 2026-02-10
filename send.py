import os
import requests
from datetime import datetime
import pytz

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

tz = pytz.timezone("Europe/Paris")
start_date = tz.localize(datetime(2026, 2, 10))

now = datetime.now(tz)
days = (now.date() - start_date.date()).days + 1

message = f"<@459679133513809951>\n`<@624454617119588363> Today is [{days}] after that threat.`"

requests.post(WEBHOOK_URL, json={"content": message})
