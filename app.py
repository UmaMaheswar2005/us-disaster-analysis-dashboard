import streamlit as st
from data_engine import load_data, get_filtered_data
from styles import apply_styles
import visuals

st.set_page_config(page_title="USND Dashboard", layout="wide")
apply_styles()
df_raw = load_data()

# Sidebar
st.sidebar.title("🛡️ Controls")
years = st.sidebar.slider("Timeline", 1953, 2017, (2000, 2017))
state = st.sidebar.selectbox("State Filter", ["All States"] + sorted(df_raw['state'].unique().tolist()))
df = get_filtered_data(df_raw, years, state)

# Header
st.title("🌪️ U.S. Natural Disaster Intelligence")

# Row 1: KPI Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Records", f"{len(df):,}")
m2.metric("Major Incident", df['incidentType'].mode()[0] if not df.empty else "N/A")
m3.metric("PA Aid Activations", int(df['paProgramDeclared'].sum()))
m4.metric("IH Aid Activations", int(df['ihProgramDeclared'].sum()))

# Row 2: Maps and Trends
c1, c2 = st.columns([1.5, 1])
with c1:
    st.plotly_chart(visuals.plot_map(df), use_container_width=True)
with c2:
    st.plotly_chart(visuals.plot_timeline(df), use_container_width=True)

# Row 3: Distribution Analysis
c3, c4, c5 = st.columns(3)
with c3:
    st.plotly_chart(visuals.plot_incidents(df), use_container_width=True)
with c4:
    st.plotly_chart(visuals.plot_top_states(df), use_container_width=True)
with c5:
    st.plotly_chart(visuals.plot_seasonality(df), use_container_width=True)

# Row 4: Financial Aid
st.plotly_chart(visuals.plot_aid_split(df), use_container_width=True)