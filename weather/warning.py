import requests

def get_weather_warnings():
    url = "https://api.data.gov.my/weather/warning"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Returns weather warning data
    except requests.RequestException as e:
        print("Weather Warning API error:", e)
        return None