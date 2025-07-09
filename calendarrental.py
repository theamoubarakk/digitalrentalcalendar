import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mascot Rental Gallery", layout="wide")
st.title("🧸 Baba Jina Mascot Rental Gallery")

# Load the Excel file with error handling
@st.cache_data
def load_data():
    return pd.read_excel("cleaned_rentals.xlsx")

try:
    df = load_data()
except Exception as e:
    st.error(f"❌ Failed to load dataset: {e}")
    st.stop()

# Status color map
status_color = {
    "Available": "✅",
    "Rented": "❌",
    "Reserved": "⏳",
    "Under Repair": "🛠️"
}

# Display mascots in a grid
cols = st.columns(3)
for idx, row in df.iterrows():
    col = cols[idx % 3]
    with col:
        st.markdown(f"### {row['Mascot_Name']}")
        st.markdown(f"**Size**: {row['Size']}")
        st.markdown(f"**Weight**: {row['Weight_kg']} kg")
        st.markdown(f"**Height**: {row['Height_cm']} cm")
        st.markdown(f"**Rent Price**: ${row['Rent_Price']}")
        st.markdown(f"**Status**: {status_color.get(row['Status'], '')} {row['Status']}")
        st.markdown("---")
