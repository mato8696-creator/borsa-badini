import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستن
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایل بۆ لادانا نیشانا 🔗 و پاقژکرنا شاشێ
st.markdown("""
<style>
    .stApp a.header-anchor { display: none !important; }
    [data-testid="stHeader"] { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #fcf6ba !important; text-align: center; }
    .card {
        background: rgba(30, 30, 30, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 15px;
    }
    .btn-link {
        display: block;
        text-align: center;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        color: white !important;
        border: 1px solid #fff;
    }
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ هەلبژارتنا زمان
if st.session_state.language is None:
    st.markdown("<br><h1>بۆڕسا دهۆک | Duhok Borsa</h1>", unsafe_allow_html=True)
    if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 5. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "wa": "واتسئاپ", "tg": "تلیگرام"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "wa": "واتساب", "tg": "تيليجرام"},
    "English": {"
