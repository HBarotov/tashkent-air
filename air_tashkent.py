from environs import Env

import requests
import plotly.express as px
import pandas as pd


# Read a token from .env
env = Env()
env.read_env()

# Get the API
url = "http://api.waqi.info/feed/tashkent/?token="
url += env.str("TOKEN")

r = requests.get(url)
response_dict = r.json()

# Extract information from .JSON
city = response_dict["data"]["city"]["name"]
days, avgs, highs, lows = [], [], [], []
for f_dict in response_dict["data"]["forecast"]["daily"]["pm25"]:
    days.append(f_dict["day"])
    avgs.append(f_dict["avg"])
    highs.append(f_dict["max"])
    lows.append(f_dict["min"])

d = {"Date": days}
d["Max"] = highs
d["Average"] = avgs
d["Min"] = lows

# Visualize
df = pd.DataFrame(data=d)
title = f"PM 2.5 Amounts in {city} - (7-day Forecasts)"
labels = {"x": "Date", "y": "PM 2.5 Amounts"}
fig = px.line(df, x="Date", y=["Max", "Average", "Min"], title=title, markers=True)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title="PM 2.5 Amounts",
    yaxis_title_font_size=20,
)

fig.show()
