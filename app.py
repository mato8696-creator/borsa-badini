import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی و نووکرنا ئۆتۆماتیک هەر چرکە
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. سیستەمێ زمان و ژمارەکەرێ بینەران (بۆ هندێ زێدەباری بلند نەبیت)
if 'language' not in st.session_state: st.session_state.language = None
if 'calculation_result' not in st.session_state: st.session_state.calculation_result = None

if 'already_counted' not in st.session_state:
    if 'visitor_count' not in st.session_state:
        st.session_state.visitor_count = 1767 # ژمارەیا تە یا دەستپێکێ
    st.session_state.visitor_count += 1
    st.session_state.already_counted = True

# 3. لاپەڕێ هەلبژارتنا زمانی (ئێکەم تشت دیار دبیت)
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2 { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; width: 100%; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "Kurdish": {"
