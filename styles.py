import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        
        .stApp {
            background-color: #020617;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        
        /* Glassmorphism Cards */
        [data-testid="stMetric"], .chart-card {
            background: rgba(30, 41, 59, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(12px);
            border-radius: 16px !important;
            padding: 20px !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }

        /* High Visibility Text */
        h1, h2, h3, .stMetric label {
            color: #38bdf8 !important;
            font-weight: 700 !important;
        }

        /* Sticky Footer */
        .footer {
            position: fixed; left: 0; bottom: 0; width: 100%;
            background-color: rgba(2, 6, 23, 0.9);
            color: #94a3b8; text-align: center;
            padding: 15px; font-size: 13px;
            border-top: 1px solid #1e293b; z-index: 1000;
        }
        </style>
        <div class="footer">
            Visualizing U.S. Natural Disaster Declarations | <b>Uma Maheswar Reddy V</b> | Infosys Springboard Internship | 2026
        </div>
    """, unsafe_allow_html=True)