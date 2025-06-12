
import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objs as go
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

st.set_page_config(layout="wide")
st.title("📊 Business Financial KPI Predictive Dashboard")

# Load dataset
df = pd.read_csv("data/sample_financial_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# KPI Selection
kpi_options = ['Revenue', 'Expenses', 'Profit', 'CashFlow']
selected_kpi = st.selectbox("Select KPI to Analyze", kpi_options)

# Date Range Filter
min_date = df['Date'].min()
max_date = df['Date'].max()
start_date, end_date = st.date_input("Filter by Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter Data
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
filtered_df = filtered_df.rename(columns={'Date': 'ds', selected_kpi: 'y'})

# Prophet Forecast
model = Prophet()
model.fit(filtered_df)
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Anomaly Detection (Z-score)
df_stats = filtered_df.copy()
df_stats['z_score'] = (df_stats['y'] - df_stats['y'].mean()) / df_stats['y'].std()
df_stats['anomaly'] = np.where(abs(df_stats['z_score']) > 2, 'Yes', 'No')

# Log anomalies
anomalies = df_stats[df_stats['anomaly'] == 'Yes']
if not anomalies.empty:
    log_df = pd.read_csv("logs/anomalies.csv")
    for _, row in anomalies.iterrows():
        log_df.loc[len(log_df)] = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            selected_kpi,
            row['ds'].strftime("%Y-%m-%d"),
            row['y'],
            row['z_score']
        ]
    log_df.to_csv("logs/anomalies.csv", index=False)

    # Send Email Alert (placeholder credentials)
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "your_email@example.com"
        receiver_email = "receiver@example.com"
        password = "your_app_password"

        subject = "🚨 KPI Anomaly Alert"
        body = f"Anomalies detected in {selected_kpi} data:\n\n" + anomalies[['ds', 'y', 'z_score']].to_string(index=False)

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        st.warning(f"Email not sent: {e}")

# Plot chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=filtered_df['ds'], y=filtered_df['y'], mode='lines+markers', name='Actual'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))

if not anomalies.empty:
    fig.add_trace(go.Scatter(
        x=anomalies['ds'], y=anomalies['y'],
        mode='markers',
        marker=dict(color='red', size=10),
        name='Anomaly'
    ))

fig.update_layout(title=f'{selected_kpi} Forecast with Anomaly Alerts',
                  xaxis_title='Date',
                  yaxis_title=selected_kpi)

st.plotly_chart(fig, use_container_width=True)

# Display anomaly log
if not anomalies.empty:
    st.subheader("⚠️ Detected Anomalies")
    st.dataframe(anomalies[['ds', 'y', 'z_score']])
else:
    st.success("No anomalies detected for the selected range.")
