import requests

def get_earthquake_warnings():
    url = "https://api.data.gov.my/weather/warning/earthquake"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # Returns earthquake warning data
    except requests.RequestException as e:
        print("Earthquake API error:", e)
        return None