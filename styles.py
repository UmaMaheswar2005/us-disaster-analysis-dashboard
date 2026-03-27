import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp { background-color: #0f172a; color: #f8fafc; }
        [data-testid="stMetric"] {
            background-color: #1e293b;
            border: 1px solid #334155;
            padding: 20px;
            border-radius: 12px;
        }
        .footer {
            position: fixed; left: 0; bottom: 0; width: 100%;
            background-color: #020617; color: #94a3b8;
            text-align: center; padding: 10px; z-index: 100;
        }
        </style>
        <div class="footer">
            Visualizing U.S. Natural Disaster Declarations | <b>Uma Maheswar Reddy V</b> | Infosys Springboard Internship | 2026
        </div>
    """, unsafe_allow_html=True)