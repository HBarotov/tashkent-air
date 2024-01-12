from pathlib import Path
from datetime import datetime
import csv
import plotly.express as px

# Extract .csv data
path = Path("air_data_tashkent.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header = next(reader)

# Extract dates and PM 2.5 values.
dates, pm2_5 = [], []
for row in reader:
    current_date = datetime.strptime(row[0], "%Y-%m-%d")
    try:
        pm_value = int(row[1])
    except:
        pass
    pm2_5.append(pm_value)
    dates.append(current_date)

# Visualize the results.
title = f"PM 2.5 in Tashkent, 2018-2024. Source: Tashkent, US-Embassy"
labels = {"x": "Date", "y": "Amounts of PM 2.5"}
fig = px.area(x=dates, y=pm2_5, title=title, labels=labels)

fig.update_layout(xaxis=dict(tickformat="%d-%m-%Y"))
fig.show()
