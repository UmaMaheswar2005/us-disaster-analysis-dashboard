import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path='usnd_cleaned.csv'):
    """
    Loads, cleans, and standardizes the FEMA dataset.
    Using @st.cache_data ensures the file is only read once, 
    making the dashboard lightning fast.
    """
    try:
        df = pd.read_csv(file_path)
        
        # 1. Standardize Column Names (Renaming from Milestone 1 logic)
        rename_map = {
            'individualsAndHouseholdsProgram': 'ihProgramDeclared',
            'publicAssistanceProgram': 'paProgramDeclared',
            'Incident type': 'incidentType',
            'declarationDate': 'date'
        }
        df = df.rename(columns=rename_map)
        
        # 2. Convert Dates
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            
        # 3. Numeric Mapping for Assistance (Yes/No to 1/0)
        # This allows us to use .sum() in our visualizations
        mapping = {'Yes': 1, 'No': 0}
        for col in ['ihProgramDeclared', 'paProgramDeclared']:
            if col in df.columns:
                # If data is string 'Yes'/'No', map it; otherwise keep as is
                if df[col].dtype == object:
                    df[col] = df[col].map(mapping).fillna(0)
        
        # 4. Ensure Year is Integer for the slider
        if 'year' in df.columns:
            df['year'] = df['year'].astype(int)
            
        return df
    
    except FileNotFoundError:
        st.error(f"Error: {file_path} not found. Please ensure the CSV is in the repository.")
        return pd.DataFrame()

def get_filtered_data(df, year_range, selected_state):
    """
    A helper function to apply sidebar filters to the dataframe.
    """
    # Filter by Year
    mask = (df['year'] >= year_range[0]) & (df['year'] <= year_range[1])
    
    # Filter by State
    if selected_state != "All States":
        mask &= (df['state'] == selected_state)
        
    return df[mask]