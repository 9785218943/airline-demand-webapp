
import plotly.express as px

def plot_routes(routes_df):
    fig = px.bar(
        routes_df.head(5),
        x='Route',
        y='Frequency',
        title='Top 5 Popular Flight Routes',
        text='Frequency'
    )
    return fig.to_html(full_html=False)

def plot_peak_times(peak_df):
    fig = px.line(
        peak_df,
        x='Hour of Day',
        y='Flight Count',
        title='Flight Demand by Hour',
        markers=True
    )
    return fig.to_html(full_html=False)
