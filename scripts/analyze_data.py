import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_weather_data(city):
    # Load the data
    data_path = f'data/processed/{city}_weather.csv'
    if not os.path.exists(data_path):
        return {"Error": "Data for the specified city does not exist."}
    
    data = pd.read_csv(data_path)
    
    # Overview of the data
    overview = {
        "Number of Rows": data.shape[0],
        "Number of Columns": data.shape[1],
        "Columns": list(data.columns),
        "Missing Values": data.isnull().sum().to_dict(),
        "Data Types": data.dtypes.to_dict()
    }

    # Data Summary: Basic statistics
    summary = data.describe().to_dict()

    # Generate Data Visualizations and save them to assets/ folder
    visualize_data(data, city)

    return {
        "Overview": overview,
        "Summary": summary,
        "Visualizations": "Generated successfully"
    }

def visualize_data(data, city):
    output_dir = 'assets'
    os.makedirs(output_dir, exist_ok=True)

    # Plot 1: Histogram for temperature
    plt.figure(figsize=(10, 6))
    sns.histplot(data['temperature'], kde=True, color='skyblue')
    plt.title(f'Distribution of Temperature in {city}')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, f'{city}_temperature_distribution.png'))
    plt.close()

    # Plot 2: Pie Chart for Rain Chance Categories
    rain_chance_bins = pd.cut(data['rain_chance'], bins=[0, 25, 50, 75, 100], labels=['Low', 'Moderate', 'High', 'Very High'])
    rain_chance_counts = rain_chance_bins.value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(rain_chance_counts, labels=rain_chance_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Rain Chance Distribution in {city}')
    plt.savefig(os.path.join(output_dir, f'{city}_rain_chance_pie_chart.png'))
    plt.close()

    # Plot 3: Bar plot for wind speed
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.index, y='wind_speed', data=data, color='lightcoral')
    plt.title(f'Wind Speed in {city}')
    plt.xlabel('Day')
    plt.ylabel('Wind Speed (m/s)')
    plt.savefig(os.path.join(output_dir, f'{city}_wind_speed_bar_chart.png'))
    plt.close()
