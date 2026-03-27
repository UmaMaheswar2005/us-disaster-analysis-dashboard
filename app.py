import streamlit as st
from data_engine import load_data
from styles import apply_styles
import visuals

# 1. Setup
st.set_page_config(page_title="USND Intelligence", layout="wide")
apply_styles()
df = load_data()

# 2. Sidebar Navigation
st.sidebar.title("🛡️ Dashboard Navigation")
page = st.sidebar.radio("Go to", ["Overview Dashboard", "Geospatial Analysis", "Assistance Trends"])

# 3. Routing Logic
if page == "Overview Dashboard":
    st.title("🌪️ U.S. Disaster Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(visuals.create_temporal_chart(df), use_container_width=True)
    with col2:
        st.plotly_chart(visuals.create_geo_map(df), use_container_width=True)

elif page == "Geospatial Analysis":
    st.title("🗺️ Regional Deep Dive")
    # You can add much longer, more detailed code here specifically for maps...