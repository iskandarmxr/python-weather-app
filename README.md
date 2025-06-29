# 🇲🇾 Malaysia Weather Web App

A simple and responsive weather web application built with **Python Flask** and **Bootstrap**, using real-time data from the [Malaysia Data.gov.my Weather APIs](https://api.data.gov.my/).  
This app displays:

- 📡 General weather forecasts  
- ⚠️ Weather warnings  
- 🌍 Earthquake warnings  

The app is suitable for anyone looking to integrate real-world API data into a modern web interface using Python.

---

## 🧩 Features

- ✅ Real-time weather forecast data
- ✅ Tabular view of forecast by area
- ✅ Card-based display of weather warnings and earthquake alerts
- ✅ Bootstrap-powered responsive design
- ✅ Clean Jinja2 templating and modular Python structure

---

## 🚀 Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Backend       | Python 3.13.1      |
| Web Framework | Flask              |
| Frontend      | HTML + Bootstrap 5 |
| API Source    | data.gov.my        |

---

## 🛠️ Project Structure
weather_app/
├── app.py # Main Flask app
├── requirements.txt # Python dependencies
├── weather/ # API modules
│ ├── forecast.py
│ ├── warning.py
│ └── earthquake.py
├── templates/
│ └── index.html # HTML layout (Bootstrap + Jinja2)
└── static/ # (Optional) Static files

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather_app.git
cd weather_app
```
### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---
▶️ Running the App
```bash
python app.py
```
Then open your browser and go to:
👉 http://127.0.0.1:5000



