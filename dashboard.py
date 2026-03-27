import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Config
st.set_page_config(page_title="US Natural Disaster Dashboard", layout="wide")

st.title("🌪️ US Natural Disaster Analysis (1953-2017)")
st.markdown("### A Comprehensive Study of Temporal, Geographic, and Incident Trends")

# Load Cleaned Data
@st.cache_data
def load_data():
    df = pd.read_csv('usnd_cleaned.csv')
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
selected_year = st.sidebar.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (1990, 2017))
filtered_df = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]

# --- Layout: Milestone 2 & 3 ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Temporal Trends (Milestone 2)")
    yearly_counts = filtered_df.groupby('year').size().reset_index(name='Counts')
    fig_line = px.line(yearly_counts, x='year', y='Counts', title="Disaster Frequency Over Time")
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Geographic Hotspots (Milestone 3)")
    state_counts = filtered_df.groupby('state').size().reset_index(name='Total')
    fig_map = px.choropleth(state_counts, locations='state', locationmode="USA-states", 
                            color='Total', scope="usa", color_continuous_scale="Reds")
    st.plotly_chart(fig_map, use_container_width=True)

# --- Layout: Milestone 4 ---
st.divider()
st.subheader("Incident & Assistance Analysis (Milestone 4)")

col3, col4 = st.columns([1, 2])

with col3:
    incident_counts = filtered_df['incidentType'].value_counts().reset_index()
    fig_tree = px.treemap(incident_counts, path=['incidentType'], values='count', 
                          title="Incident Composition", color='count', color_continuous_scale='RdBu_r')
    st.plotly_chart(fig_tree, use_container_width=True)

with col4:
    # Aggregating assistance for the grouped bar chart
    assist_df = filtered_df.groupby('incidentType')[['ihProgramDeclared', 'paProgramDeclared']].sum().reset_index()
    fig_assist = px.bar(assist_df, x='incidentType', y=['ihProgramDeclared', 'paProgramDeclared'], 
                        barmode='group', title="Public vs Individual Assistance")
    st.plotly_chart(fig_assist, use_container_width=True)