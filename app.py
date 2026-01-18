import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="Borsa Duhok", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. زمان و ژمارەکەر (Counter)
if 'lang' not in st.session_state: st.session_state.lang = None
if 'res' not in st.session_state: st.session_state.res = None
if 'count' not in st.session_state: st.session_state.count = 2586

if 'counted' not in st.session_state:
    st.session_state.count += 1
    st.session_state.counted = True

# 3. لاپەڕێ هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️", use_container_width=True):
        st.session_state.lang = "KU"
        st.rerun()
    if st.button("العربية 🇮🇶", use_container_width=True):
        st.session_state.lang = "AR"
        st.rerun()
    st.stop()

# 4. وەرگێڕان
text = {
    "KU": {"t": "بۆڕسا دهۆک", "u": "بهایێ دۆلاری (١٠٠$)", "c": "حسابکەرا پارەی", "b": "حساب بکە", "v": "بینەرێن سایتێ:"},
    "AR": {"t": "بورصة دهوك", "u": "سعر الدولار (١٠٠$)", "c": "حاسبة العملات", "b": "تحويل", "v": "زوار الموقع:"}
}[st.session_state.lang]

# 5. ستایلێ گشتی
st.markdown
