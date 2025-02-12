import streamlit as st
import pandas as pd
from scripts.collect_data import fetch_weather_data
from scripts.predict_weather import predict_next_5_days
from scripts.analyze_data import analyze_weather_data

# Page 1: Current Weather
def current_weather_page():
    st.title("🌍 Check Current Weather")
    city = st.text_input("Enter a city name", "New York")
    
    if st.button("Get Weather"):
        try:
            weather_data = fetch_weather_data(city)
            st.write(f"**City**: {weather_data['city']}")
            st.write(f"**Temperature (°C)**: {weather_data['temperature']}")
            st.write(f"**Humidity (%)**: {weather_data['humidity']}")
            st.write(f"**Pressure (hPa)**: {weather_data['pressure']}")
            st.write(f"**Wind Speed (m/s)**: {weather_data['wind_speed']}")
        except Exception as e:
            st.error(f"Error fetching weather data: {str(e)}")

# Page 2: 5-Day Forecast
def forecast_page():
    st.title("📅 5-Day Weather Forecast")
    city = st.text_input("Enter a city name for forecast", "New York")

    if st.button("Get 5-Day Forecast"):
        try:
            forecast_data = predict_next_5_days(city)
            st.write(f"5-Day Forecast for {city}")

            for day in forecast_data:
                date = day['date']
                condition = day['condition']
                rain_chance = day['rain_chance']
                wind_speed = day['wind_speed']

                st.write(f"**Date**: {date}")
                st.write(f"**Condition**: {condition} (Rain Chance: {rain_chance}%, Wind Speed: {wind_speed} m/s)")
                if condition == 'Sunny':
                    st.image("assets/sunny.png")
                elif condition == 'Rainy':
                    st.image("assets/rain.png")
                elif condition == 'Cloudy':
                    st.image("assets/cloudy.png")
                st.write("---")
        except Exception as e:
            st.error(f"Error fetching forecast: {str(e)}")

# Page 3: Data Analysis
def data_analysis_page():
    st.title("📊 Data Analysis of Weather Data")

    city = st.text_input("Enter a city for data analysis", "New York")

    if st.button("Analyze Data"):
        st.write(f"Analyzing data for {city}...")
        try:
            analysis_result = analyze_weather_data(city)
            
            if "Error" in analysis_result:
                st.error(analysis_result["Error"])
            else:
                # Display Data Overview
                st.subheader(f"Data Analysis for {city}")
                st.write("### Overview of the Data")
                
                overview_df = pd.DataFrame(analysis_result["Overview"].items(), columns=["Metric", "Value"])
                st.table(overview_df)

                # Display Data Summary in Table
                st.write("### Summary Statistics")
                summary_df = pd.DataFrame(analysis_result["Summary"])
                st.table(summary_df)

                # Display visualizations
                st.write("### Visualizations")
                st.image(f"assets/{city}_temperature_distribution.png", caption=f"Temperature Distribution in {city}")
                st.image(f"assets/{city}_rain_chance_pie_chart.png", caption=f"Rain Chance Distribution in {city}")
                st.image(f"assets/{city}_wind_speed_bar_chart.png", caption=f"Wind Speed in {city}")
        except Exception as e:
            st.error(f"Error analyzing data: {e}")

# App Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ("Current Weather", "5-Day Forecast", "Data Analysis"))

if page == "Current Weather":
    current_weather_page()
elif page == "5-Day Forecast":
    forecast_page()
elif page == "Data Analysis":
    data_analysis_page()
