import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر
if 'visits' not in st.session_state: st.session_state.visits = 45
st.session_state.visits += 1

# 3. ستایلێ CSS
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    .card {
        background-color: #1a1c23;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
        margin-bottom: 15px;
    }
    .gold-box {
        background: linear-gradient(45deg, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        color: #1a1c23;
        padding: 15px;
        border-radius: 12px;
        font-weight: bold;
        margin-top: 10px;
    }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%; height: 50px; border-radius: 12px; font-weight: bold; border: none;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا بها (دۆلار و زێڕ)
try:
    curr_data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd_rate = curr_data['rates']['IQD'] + 158.5
