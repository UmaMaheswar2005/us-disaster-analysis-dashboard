import plotly.express as px

def get_theme():
    return "plotly_dark"

def plot_timeline(df):
    data = df.groupby('year').size().reset_index(name='Count')
    fig = px.area(data, x='year', y='Count', title="Growth Analysis", template=get_theme(), color_discrete_sequence=['#0ea5e9'])
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig

def plot_map(df):
    data = df.groupby('state').size().reset_index(name='Total')
    fig = px.choropleth(data, locations='state', locationmode="USA-states", color='Total', scope="usa", 
                        color_continuous_scale="Blues", template=get_theme())
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor='rgba(0,0,0,0)')
    return fig

def plot_top_states(df):
    data = df['state'].value_counts().head(10).reset_index()
    return px.bar(data, x='state', y='count', title="Top 10 Risk Zones", template=get_theme(), color_discrete_sequence=['#38bdf8'])

def plot_incidents(df):
    data = df['incidentType'].value_counts().reset_index()
    return px.pie(data, names='incidentType', values='count', hole=0.4, title="Incident Distribution", template=get_theme())

def plot_aid_split(df):
    assist = df.groupby('incidentType')[['ihProgramDeclared', 'paProgramDeclared']].sum().reset_index()
    return px.bar(assist, x='incidentType', y=['ihProgramDeclared', 'paProgramDeclared'], barmode='group', template=get_theme())

def plot_seasonality(df):
    data = df.groupby('month').size().reset_index(name='Count')
    return px.line(data, x='month', y='Count', markers=True, title="Monthly Seasonality", template=get_theme())