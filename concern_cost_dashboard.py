
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the Excel file
file_path = 'Concerns Register 2025.xlsx'
sheet_name = 'New Reg'

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# Convert 'Date of Concern' to datetime, coerce errors
df['Date of Concern'] = pd.to_datetime(df['Date of Concern'], errors='coerce')

# Filter out rows with invalid dates
df = df.dropna(subset=['Date of Concern'])

# Extract month-year from 'Date of Concern'
df['Month-Year'] = df['Date of Concern'].dt.to_period('M')

# Group by 'Month-Year' and 'External /Internal Concern Type' and sum the 'Total (£)' column
grouped_df = df.groupby(['Month-Year', 'External /Internal Concern Type'])['Total
(£)'].sum().reset_index()

# Convert 'Month-Year' to datetime for plotting
grouped_df['Month-Year'] = grouped_df['Month-Year'].dt.to_timestamp()

# Streamlit app
st.title('Total Cost per Month by External/Internal Concern Type')

# Line chart
fig = px.line(grouped_df, x='Month-Year', y='Total
(£)', color='External /Internal Concern Type',
              title='Total Cost per Month by External/Internal Concern Type')
st.plotly_chart(fig)

# Data table
st.subheader('Data Table')
st.dataframe(grouped_df)
