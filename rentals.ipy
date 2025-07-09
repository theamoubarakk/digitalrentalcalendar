{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb56ebff-3658-4ea1-b797-85d5c201aefa",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-09 16:45:29.569 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-07-09 16:45:29.569 No runtime found, using MemoryCacheStorageManager\n",
      "2025-07-09 16:45:29.570 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "st.set_page_config(page_title=\"Mascot Rental Gallery\", layout=\"wide\")\n",
    "st.title(\"🧸 Baba Jina Mascot Rental Gallery\")\n",
    "\n",
    "# Load the Excel file\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    return pd.read_excel(\"cleaned_rentals.xlsx\")\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "# Status color map\n",
    "status_color = {\n",
    "    \"Available\": \"✅\",\n",
    "    \"Rented\": \"❌\",\n",
    "    \"Reserved\": \"⏳\",\n",
    "    \"Under Repair\": \"🛠️\"\n",
    "}\n",
    "\n",
    "# Display mascots in a grid\n",
    "cols = st.columns(3)\n",
    "for idx, row in df.iterrows():\n",
    "    col = cols[idx % 3]\n",
    "    with col:\n",
    "        st.markdown(f\"### {row['Mascot_Name']}\")\n",
    "        st.markdown(f\"**Size**: {row['Size']}\")\n",
    "        st.markdown(f\"**Weight**: {row['Weight_kg']} kg\")\n",
    "        st.markdown(f\"**Height**: {row['Height_cm']} cm\")\n",
    "        st.markdown(f\"**Rent Price**: ${row['Rent_Price']}\")\n",
    "        st.markdown(f\"**Status**: {status_color.get(row['Status'], '')} {row['Status']}\")\n",
    "        st.markdown(\"---\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
