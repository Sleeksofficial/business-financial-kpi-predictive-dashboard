
# 📊 Business Financial KPI Predictive Dashboard

This project is a predictive analytics dashboard designed to monitor, analyze, and forecast financial KPIs using interactive visualizations and machine learning models. Built with Streamlit, Facebook Prophet, and Plotly, it allows for real-time insight and data-driven forecasting.

---

## 🚀 Features

- **📈 Revenue Forecasting**: Uses Facebook Prophet to project future revenue trends.
- **📊 Interactive Dashboard**: Built with Streamlit and Plotly for real-time KPI visualization.
- **🧪 Jupyter Notebook**: For model experimentation and training using historical financial data.
- **📁 Clean Structure**: Modular, scalable project layout ready for development or production.
- **🔁 GitHub Actions CI**: Automatically runs tests on each push to ensure setup consistency.

---

## 🖼 Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

---

## 🗂 Project Structure

```
📦 business-financial-kpi-predictive-dashboard
├── 📊 dashboard/
│   └── app.py                     # Streamlit app
├── 📘 notebooks/
│   └── revenue_forecasting.ipynb  # Prophet model training
├── 📁 data/
│   └── sample_financial_data.csv  # Sample financial dataset
├── 📦 models/                     # Trained models (optional)
├── 🧠 utils/
│   └── forecasting.py             # Forecast logic using Prophet
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 dashboard_preview.png       # Visual preview for README
└── ⚙️ .github/workflows/
    └── python-app.yml             # GitHub Actions CI workflow
```

---

## ⚙️ Getting Started

### 1. Clone and Setup
```bash
git clone https://github.com/Sleeksofficial/business-financial-kpi-predictive-dashboard.git
cd business-financial-kpi-predictive-dashboard
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
streamlit run dashboard/app.py
```

---

## 📘 Model Development

Check out `notebooks/revenue_forecasting.ipynb` for step-by-step development using Facebook Prophet:
- Data preprocessing
- Time series modeling
- Forecast visualization

---

## 🌐 Deployment on Streamlit Cloud

1. Push your project to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app linked to your GitHub repo
4. Set main file as: `dashboard/app.py`
5. Click **Deploy**

---

## ✅ GitHub Actions CI

On every push, this project automatically:
- Installs all dependencies
- Verifies Python and Streamlit setup
(Workflow defined in `.github/workflows/python-app.yml`)

---

## 📄 License

This project is licensed under the MIT License.
