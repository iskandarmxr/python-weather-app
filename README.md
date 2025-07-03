# 🇲🇾 Malaysia Weather Web App

A simple and responsive weather web application built with **Python Flask** and **Bootstrap**, using real-time data from the [Malaysia Data.gov.my Weather APIs](https://developer.data.gov.my/realtime-api/weather)
This app displays:

- 📡 General weather forecasts  
- ⚠️ Weather warnings  
- 🌍 Earthquake warnings  

The app is suitable for anyone looking to integrate real-world API data into a modern web interface using Python.

![Screenshot 2025-06-29 230726](https://github.com/user-attachments/assets/5750bfdc-c0cb-4946-811b-2968c9b008ee)

![Screenshot 2025-06-29 230806](https://github.com/user-attachments/assets/e96790c3-fa8d-4756-b531-181b76d331a1)

![Screenshot 2025-06-29 230749](https://github.com/user-attachments/assets/862d2abe-a53f-4062-98af-0625994e15e0)

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
```
weather_app/
│
├── app.py                      ← Main Flask app
├── requirements.txt
│
├── weather/
│   ├── __init__.py
│   ├── forecast.py
│   ├── warning.py
│   └── earthquake.py
│
├── templates/
│   └── index.html              ← HTML view
└── static/
    └── style.css               ← (optional) styling
```

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



