
import requests


class WindyFacade:
    def __init__(self, api_key="hHNTDzp8ymOSm2AWOtnyJyg1pj10iuSA"):
        self.api_key = api_key

    def temperatura(self, latitude, longitude):
        data = {
            "lat": latitude,
            "lon": longitude,
            "model": "gfs",
            "parameters": ["temp"],
            "levels": ["surface"],
            "key": self.api_key,
        }
        url = "https://api.windy.com/api/point-forecast/v2"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return str(float(response.json().get("temp-surface")[0]) - 273.15) + "C°"
        else:
            raise ValueError(f"Error: {response.status_code}")
    
    def viento(self, latitude, longitude):
        data = {
            "lat": latitude,
            "lon": longitude,
            "model": "gfs",
            "parameters": ["wind"],
            "levels": ["surface"],
            "key": self.api_key,
        }
        url = "https://api.windy.com/api/point-forecast/v2"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return str(response.json().get("wind_u-surface")[0]) +"m/s"
        else:
            raise ValueError(f"Error: {response.status_code}")


clima = WindyFacade()

temperatura = clima.temperatura(-45.8237,-67.4615)
viento = clima.viento(-45.8237,-67.4615)
print("En Comodoro Rivadavia la temperatura es: "+ temperatura +" y el viento: "+ viento)