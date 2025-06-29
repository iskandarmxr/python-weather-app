import requests

def get_forecast():
    url = "https://api.data.gov.my/weather/forecast"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Returns forecast data
    except requests.RequestException as e:
        print("Forecast API error:", e)
        return None