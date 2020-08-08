import requests
from datetime import timedelta
from datetime import datetime
from pathlib import Path
import json

WEATHER_API = "https://api.weatherbit.io/v2.0/history/hourly"

def get_weather(day, latlongs):

    eday = day + timedelta(days=1)

    for lat, lon in latlongs:
        yield requests.get(WEATHER_API, params={**PARAMS, "lat": lat, "lon": lon, "start_date": day.strftime(DATE_FORMAT), "end_date": eday.strftime(DATE_FORMAT)}).json()

PARAMS = {
         "lat": 36.8617867, 
         "lon": -2.4902473,
         "start_date": None,
         "end_date": None, 
         "tz": "utc",
         "key": "14a346d9bb0a4701b72baf59f2819384",
}
DATE_FORMAT = "%Y-%m-%d"

latlongs = [
    ["36.928026", "-2.687309"],
    ["40.723609", "-5.204659"],
    ["42.210419", "1.240819"],
    ["35.7721", "-78.63861"]
]

input_path = Path("input_data")

end = datetime.now()
begin = end + timedelta(days=-30)

while begin < end:
    output_path = input_path / "weather" / f"date={begin.strftime(DATE_FORMAT)}"
    output_path.mkdir(parents=True, exist_ok=True)

    with (output_path / "data.json").open("w") as f:
        for j in get_weather(begin, latlongs):
            print(json.dumps(j), file=f)
    begin += timedelta(days=1)
