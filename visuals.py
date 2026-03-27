import plotly.express as px

def create_temporal_chart(df):
    yearly = df.groupby('year').size().reset_index(name='Count')
    fig = px.area(yearly, x='year', y='Count', title="Annual Declaration Growth",
                  color_discrete_sequence=['#38bdf8'], template="plotly_dark")
    fig.update_layout(hovermode="x unified", plot_bgcolor='rgba(0,0,0,0)')
    return fig

def create_geo_map(df):
    state_counts = df.groupby('state').size().reset_index(name='Total')
    fig = px.choropleth(state_counts, locations='state', locationmode="USA-states", 
                        color='Total', scope="usa", color_continuous_scale="Blues", template="plotly_dark")
    return fig