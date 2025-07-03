
from flask import Flask, render_template, request
from data_fetch import fetch_flight_data
from data_process import analyze_routes, analyze_peak_times
from plot_charts import plot_routes, plot_peak_times

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    limit = int(request.form['limit'])
    df = fetch_flight_data(limit)
    routes = analyze_routes(df)
    peak_times = analyze_peak_times(df)

    route_chart = plot_routes(routes)
    time_chart = plot_peak_times(peak_times)

    return render_template("results.html",
                           route_chart=route_chart,
                           time_chart=time_chart)

if __name__ == "__main__":
    app.run(debug=True)
