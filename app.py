import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ گشتی و پاقژکرنا نیشانێن 🔗
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071"
st.markdown(f"""
<style>
    .stApp a.header-anchor {{ display: none !important; }}
    header, [data-testid="stHeader"], #MainMenu, footer {{ visibility: hidden; }}
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-position: center; background-attachment: fixed; }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-align: center; }}
    .card {{ background-color: rgba(20, 20, 20, 0.9); padding: 30px; border-radius: 15px; border: 2px solid #bf953f; text-align: center; margin-bottom: 15px; }}
    div.stButton > button {{ background: linear-gradient(45deg, #FF0000, #990000) !important; color: white !important; font-weight: bold !important; width: 100%; border-radius: 10px; border: 1px solid #fff; height: 50px; font-size: 20px !important; }}
    .result-box {{ background-color: rgba(0,255,0,0.1); padding: 15px; border-radius: 10px; text-align: center; border: 2px solid #00FF00; margin-top: 15px; }}
    .tele-btn {{ display: block; background: #0088cc; color: white !important; text-align: center; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px; border: 1px solid #fff; }}
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 5. شاشا سەرەکی
st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)
st.markdown(f"""<div class="card"><p>بهایێ دۆلاری (١٠٠$)</p><h2
