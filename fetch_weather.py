# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 14:19:01 2025

@author: rajpr
"""

import requests
import pandas as pd

# --- SETTINGS ---
latitude = 51.5074     # example: London
longitude = -0.1278

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&hourly=temperature_2m"
)

# --- FETCH DATA ---
response = requests.get(url)
data = response.json()

# --- CONVERT TO EXCEL ---
times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

df = pd.DataFrame({
    "time": times,
    "temperature_2m": temps
})

df.to_excel("weather.xlsx", index=False)

print("Done! File saved as weather.xlsx")
