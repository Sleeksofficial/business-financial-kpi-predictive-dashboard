
import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objs as go

st.set_page_config(layout="wide")
st.title("📊 Business Financial KPI Predictive Dashboard")

# Load dataset
df = pd.read_csv("data/sample_financial_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={'Date': 'ds', 'Revenue': 'y'})

# Prophet model
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Plotly chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines+markers', name='Actual'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
fig.update_layout(title='Revenue Forecast',
                  xaxis_title='Date',
                  yaxis_title='Revenue')

st.plotly_chart(fig, use_container_width=True)
