import matplotlib.pyplot as plt
import streamlit as st

def plot_forecast(forecast_data):
    temps = [day['main']['temp'] for day in forecast_data['list'][:5]]
    st.line_chart(temps)

def plot_weather_condition_probabilities(forecast_data):
    rain_chances = [day['pop'] * 100 for day in forecast_data['list'][:5]]
    wind_speeds = [day['wind']['speed'] for day in forecast_data['list'][:5]]

    st.bar_chart({
        'Rain Chances (%)': rain_chances,
        'Wind Speed (m/s)': wind_speeds
    })

def plot_data_analysis(city):
    st.write(f"Analyzing data for {city}...")
    # Add relevant data analysis visualizations here
