
# 📊 Business Financial KPI Predictive Dashboard

An advanced dashboard to visualize, forecast, and monitor financial KPIs with anomaly detection, email alerts, and multi-KPI filtering.

## 🔧 Features
- Forecast KPIs with Prophet
- Filter by KPI and date range
- Detect anomalies using Z-score
- Log anomalies to CSV
- Trigger email alerts on anomaly detection

## 🗂 KPIs Supported
- Revenue
- Expenses
- Profit

## 📂 Project Structure
```
📁 business-financial-kpi-predictive-dashboard/
├── dashboard/
│   └── app.py
├── data/
│   └── sample_financial_data.csv
├── logs/
│   └── anomalies.csv (auto-generated)
├── utils/
├── README.md
```

## 🚀 Running Locally
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## 📧 Email Alerts Setup
Set these environment variables:
- `ALERT_EMAIL_FROM`
- `ALERT_EMAIL_PASS`
- `ALERT_EMAIL_TO`

Gmail example:
```bash
export ALERT_EMAIL_FROM="your@gmail.com"
export ALERT_EMAIL_PASS="your_app_password"
export ALERT_EMAIL_TO="recipient@gmail.com"
```

## ✅ Dependencies
- streamlit
- pandas
- numpy
- plotly
- prophet
