# app.py

import streamlit as st
import pandas as pd

# Title
st.title("Rental Calendar Viewer")

# Load Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("cleaned_rentals.xlsx", engine="openpyxl")
    return df

df = load_data()

# Display the full dataset
st.subheader("📅 Full Rentals Table")
st.dataframe(df)

# Date filter
st.subheader("🔎 Filter by Date")
selected_date = st.date_input("Pick a date to filter by:", value=None)

if selected_date:
    filtered_df = df[df['Date'].dt.date == selected_date]
    st.write(f"Showing rentals for **{selected_date}**:")
    st.dataframe(filtered_df)

