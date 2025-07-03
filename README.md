# airline-demand-webapp
Flight data visualizer using Flask, Plotly, and Aviationstack API
# ✈️ Airline Demand Web App

A data-driven web application that fetches real-time airline flight data using the Aviationstack API, analyzes route and time-based demand, and visualizes insights using interactive charts. Built using Python, Flask, Plotly, and Pandas.

---

## 🚀 Features

- 📡 Fetches live flight data using the **Aviationstack API**
- 🧹 Cleans and processes flight schedules
- 📊 Visualizes:
  - Top 5 busiest airline routes
  - Hourly flight demand
- 🌐 User-friendly web interface using Flask
- 📁 Automatically saves interactive charts as HTML files

---

## 🛠 Tech Stack

- **Python 3.x**
- **Flask** — for the web framework
- **Requests** — to call external APIs
- **Pandas** — for data processing
- **Plotly** — for creating visual charts
- **HTML/CSS** — for UI rendering

---

## 🧪 How It Works

1. The user visits `/` (homepage) and enters a number of flights to analyze.
2. The app calls Aviationstack API to fetch that many live flight records.
3. Data is analyzed:
   - Most frequent routes
   - Flight count per hour of the day
4. Two charts are generated:
   - Bar chart: Top 5 routes
   - Line chart: Hourly flight demand
5. Charts are displayed on the `/results` page.

---



## 📸 Screenshots

### 🏠 Homepage
![Homepage](assets/homepage.png)

### 📊 Results Page
![Results Page](assets/results.png)
Then go to: http://127.0.0.1:5000

🔑 API Key
This app uses the free Aviationstack API.
Create your free API key from: https://aviationstack.com

Then paste it inside the data_fetch.py file:

python
Copy
Edit
API_KEY = "your_api_key_here"
🚧 Folder Structure
php
Copy
Edit
airline_demand_webapp/
│
├── app.py                  # Main Flask app
├── data_fetch.py           # API call and raw data collection
├── data_process.py         # Analyzing routes and time
├── plot_charts.py          # Generates Plotly visualizations
├── requirements.txt
│
├── templates/              # HTML templates
│   ├── index.html
│   └── results.html
└── static/ (optional)      # For CSS/JS (if used)
📈 Future Improvements
Filter data by city, airline, or country

Add map-based visualizations (via Mapbox)

Deploy to Render, Railway, or PythonAnywhere

Store historical data to analyze trends over time

👩‍💻 Developed By
Mausam Sharma
Aspiring Data Analyst | Python Developer | Data Enthusiast
📧 mausam22sharma@gmail.com



