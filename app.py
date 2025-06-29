from flask import Flask, render_template
from weather.forecast import get_forecast
from weather.warning import get_weather_warnings
from weather.earthquake import get_earthquake_warnings

app = Flask(__name__)

@app.route("/")
def index():
    forecast = get_forecast()
    warnings = get_weather_warnings()
    earthquake = get_earthquake_warnings()
    return render_template("index.html", forecast=forecast, warnings=warnings, earthquake=earthquake)

if __name__ == "__main__":
    app.run(debug=True)