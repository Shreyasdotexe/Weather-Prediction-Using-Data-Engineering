import random
from datetime import datetime, timedelta

def predict_next_5_days(city):
    # Mock prediction data (this would be replaced with a real model's output)
    conditions = ['Sunny', 'Rainy', 'Cloudy']
    
    forecast_data = []
    for i in range(5):
        day_data = {
            "date": (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
            "condition": random.choice(conditions),
            "rain_chance": random.uniform(0, 100),
            "wind_speed": random.uniform(0, 10)
        }
        forecast_data.append(day_data)
    
    return forecast_data
