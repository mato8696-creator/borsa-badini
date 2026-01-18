import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="live_clock") # نووکرن د هەر چرکەیەکێ دا بۆ دەمژمێرێ

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. لاپەڕێ دەسپێکێ
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە</p>", unsafe_allow_html=True)
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
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", "usd_live": "بهایێ دۆلاری (١٠٠$)", "news": "⚠️ هایداری: بهایێ بازارێ دهۆک یێ جێگیر نینە.. دەمژمێر ب دەمژمێر نوو دبیتەوە",
        "usd_calc": "💵 گوهۆڕینا دۆلاری", "res": "ئەنجام ب دینار:", "tele": "کەنالێ تێلەگرامی", "btn": "حساب بکە (Enter)"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", "usd_live": "سعر الدولار (١٠٠$)", "news": "⚠️ تنبيه: أسعار سوق دهوك غير مستقرة.. يتم التحديث ساعة بساعة",
        "usd_calc": "💵 تحويل الدولار", "res": "
