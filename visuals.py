import plotly.express as px
import plotly.graph_objects as go

def create_temporal_chart(df):
    yearly = df.groupby('year').size().reset_index(name='Count')
    fig = px.area(yearly, x='year', y='Count', 
                  title="📈 Annual Declaration Growth",
                  color_discrete_sequence=['#38bdf8'], template="plotly_dark")
    fig.update_layout(hovermode="x unified", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig

def create_geo_map(df):
    state_counts = df.groupby('state').size().reset_index(name='Total')
    fig = px.choropleth(state_counts, locations='state', locationmode="USA-states", 
                        color='Total', scope="usa", color_continuous_scale="Blues", 
                        template="plotly_dark", title="🗺️ Geographic Risk Density")
    fig.update_layout(geo_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig

def create_top_states_chart(df):
    top_10 = df['state'].value_counts().head(10).reset_index()
    fig = px.bar(top_10, x='state', y='count', color='count', 
                 color_continuous_scale='Blues', template="plotly_dark",
                 title="📊 Top 10 High-Risk States")
    return fig

def create_incident_treemap(df):
    tree_data = df['incidentType'].value_counts().reset_index()
    fig = px.treemap(tree_data, path=['incidentType'], values='count', 
                     color='count', color_continuous_scale='YlGnBu',
                     template="plotly_dark", title="🧩 Incident Composition")
    return fig

def create_aid_comparison(df):
    assist = df.groupby('incidentType')[['ihProgramDeclared', 'paProgramDeclared']].sum().reset_index()
    fig = px.bar(assist, x='incidentType', y=['ihProgramDeclared', 'paProgramDeclared'],
                 barmode='group', title="💰 Federal Aid Allocation",
                 labels={'value': 'Total Activations', 'variable': 'Program'},
                 color_discrete_sequence=['#7dd3fc', '#1e40af'], template="plotly_dark")
    return fig

def create_seasonal_chart(df):
    monthly = df.groupby('month').size().reset_index(name='Count')
    fig = px.line(monthly, x='month', y='Count', markers=True, 
                  title="📅 Monthly Risk Seasonality",
                  color_discrete_sequence=['#fbbf24'], template="plotly_dark")
    return fig