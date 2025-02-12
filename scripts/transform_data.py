import pandas as pd
import numpy as np
import os

def generate_synthetic_data(city, num_days=100):
    dates = pd.date_range(end=pd.to_datetime('today'), periods=num_days)
    temperature = np.random.uniform(low=10, high=30, size=num_days)
    humidity = np.random.uniform(low=30, high=90, size=num_days)
    pressure = np.random.uniform(low=990, high=1020, size=num_days)
    wind_speed = np.random.uniform(low=1, high=10, size=num_days)
    rain_chance = np.random.uniform(low=0, high=100, size=num_days)
    
    weather_info = {
        'date': dates,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'rain_chance': rain_chance
    }
    
    df = pd.DataFrame(weather_info)
    processed_data_path = f'data/processed/{city.lower()}_weather.csv'
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    df.to_csv(processed_data_path, index=False)
    print(f"Synthetic data saved to {processed_data_path}")

if __name__ == "__main__":
    city = 'New York'
    generate_synthetic_data(city)
