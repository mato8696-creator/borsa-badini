import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1650
st.session_state.count += 1

# 3. لاپەڕێ دەسپێکێ (هەلبژارتنا زمان)
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە | اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3: 
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 4. وەرگێڕان
translations = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "gold": "بهایێ زێڕی (٢١)", "calc": "کێشێ زێڕی (غرام):", "btn": "حساب بکە"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "gold": "سعر الذهب (٢١)", "calc": "وزن الذهب (غرام):", "btn": "احسب الآن"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Price (100$)", "gold": "Gold Price (21K)", "calc": "Gold Weight (Gram):", "btn": "Calculate"}
}
t = translations[st.session_state.language]

# 5. وێنەیێ دۆلاری و ستایلێ گشتی
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071&auto=format&fit=crop"
st.markdown(f"""
<style>
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-position: center; background-attachment: fixed; }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-shadow: 2px 2px 4px
