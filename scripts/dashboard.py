# scripts/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts.preprocessing import load_and_clean_data

# Set page title
st.title("E-commerce Analytics Dashboard")

# Load and clean data
df = load_and_clean_data("data/online_retail.csv")

# Convert InvoiceDate to datetime and set as index
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df.set_index('InvoiceDate', inplace=True)

# Monthly Sales Visualization
monthly_sales = df.resample('M').sum()['TotalPrice']
st.subheader("Monthly Sales")
st.line_chart(monthly_sales)

# Top 10 Products Visualization
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
st.subheader("Top 10 Products by Quantity")
fig, ax = plt.subplots(figsize=(10,6))
ax.barh(top_products.index, top_products.values, color='skyblue')
ax.set_xlabel("Quantity Sold")
ax.set_title("Top 10 Products")
st.pyplot(fig)
