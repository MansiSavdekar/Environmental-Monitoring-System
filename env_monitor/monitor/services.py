import requests
import random

def fetch_air_quality(city="Delhi"):
    url = "https://openaqstatus.org/?monitor=service"
    params = {"city": city, "limit": 1}
    res = requests.get(url, params=params, timeout=10).json()

    if not res.get("results"):
        return None

    for m in res["results"][0]["measurements"]:
        if m["parameter"] == "pm25":
            return int(m["value"])
    return None

def fetch_water_quality():
    return round(random.uniform(6.5, 8.5), 2)
