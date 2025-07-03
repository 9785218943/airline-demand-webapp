
import pandas as pd

def analyze_routes(df):
    # Combine departure and arrival to define the route
    df['route'] = df['departure_airport'] + " → " + df['arrival_airport']
    
    # Count most frequent routes
    popular_routes = df['route'].value_counts().reset_index()
    popular_routes.columns = ['Route', 'Frequency']
    
    return popular_routes

def analyze_peak_times(df):
    # Convert time strings to datetime
    df['departure_time'] = pd.to_datetime(df['departure_time'])
    
    # Extract hour of the day
    df['hour'] = df['departure_time'].dt.hour
    
    # Count flights per hour
    hourly_trend = df['hour'].value_counts().sort_index().reset_index()
    hourly_trend.columns = ['Hour of Day', 'Flight Count']
    
    return hourly_trend
