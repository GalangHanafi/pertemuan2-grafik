import streamlit as st
import pandas as pd
import numpy as np

st.title("Using Chat on Streamlit")
st.write("I am using Streamlit to show a chart")

df_sales = pd.read_csv("./sample-sales-data/sales_data_sample.csv", encoding="iso-8859-1")
st.write(df_sales)

# Get unique product lines
product_lines = df_sales["PRODUCTLINE"].unique()

# Create a DataFrame with ORDERDATE as index and product lines as columns
df_productline_sales = df_sales.pivot_table(values='QUANTITYORDERED', index='ORDERDATE', columns='PRODUCTLINE', fill_value=0)

# Print the DataFrame
print(df_productline_sales)

# Print the DataFrame
st.write(df_productline_sales)

#
# Area Chart
#
st.title("Area Chart")
st.area_chart(df_productline_sales)
st.markdown("---")
