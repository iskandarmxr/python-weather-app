from weather.forecast import get_forecast
from weather.warning import get_weather_warnings
from weather.earthquake import get_earthquake_warnings
from utils.display import print_section, display_data

def main():
    print_section("📡 Malaysia Weather Forecast")
    forecast = get_forecast()
    display_data(forecast)

    print_section("⚠️ Weather Warnings")
    warnings = get_weather_warnings()
    display_data(warnings)

    print_section("🌏 Earthquake Warnings")
    earthquake = get_earthquake_warnings()
    display_data(earthquake)

if __name__ == "__main__":
    main()