
from prophet import Prophet
import pandas as pd
import joblib

def train_forecast_model(data_path, save_model_path='models/kpi_forecaster.pkl'):
    df = pd.read_csv(data_path)
    df = df.rename(columns={'Date': 'ds', 'Revenue': 'y'})  # Prophet requires these column names

    model = Prophet()
    model.fit(df)

    joblib.dump(model, save_model_path)
    return model

def make_forecast(model_path='models/kpi_forecaster.pkl', periods=12):
    model = joblib.load(model_path)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
