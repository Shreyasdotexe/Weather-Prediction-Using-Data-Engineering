import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle
import os

def load_data(city):
    processed_data_path = f'data/processed/{city}_weather.csv'
    return pd.read_csv(processed_data_path)[['temperature']]

def train_model(city):
    data = load_data(city)
    model = ARIMA(data['temperature'], order=(5, 1, 0))
    model_fit = model.fit()

    model_path = f'models/arima_model_{city}.pkl'
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'wb') as f:
        pickle.dump(model_fit, f)
    print(f"Model saved to {model_path}")
