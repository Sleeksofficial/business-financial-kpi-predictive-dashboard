import streamlit as st
import pandas as pd
import plotly.express as px

def display_charts():
    st.subheader("Revenue Forecast")
    df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Revenue": [10000, 12000, 13000]})
    fig = px.line(df, x="Month", y="Revenue", title="Monthly Revenue")
    st.plotly_chart(fig)