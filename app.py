import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="Borsa Duhok", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. مێمۆری و ژمارەکەر
if 'lang' not in st.session_state: st.session_state.lang = None
if 'res' not in st.session_state: st.session_state.res = None
if 'count' not in st.session_state: st.session_state.count = 2586

if 'counted' not in st.session_state:
    st.session_state.count += 1
    st.session_state.counted = True

# 3. لاپەڕێ هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center;'>بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️", use_container_width=True):
        st.session_state.lang = "KU"
        st.rerun()
    if st.button("العربية 🇮🇶", use_container_width=True):
        st.session_state.lang = "AR"
        st.rerun()
    st.stop()

# 4. وەرگێڕانا سادە
text = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "c": "حسابکەرا پارەی", "v": "بینەرێن سایتێ:"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "c": "حاسبة العملات", "v": "زوار الموقع:"}
}[st.session_state.lang]

# 5. دیزاینێ سایتێ تە
st.markdown("<style>header,footer{visibility:hidden;} .stApp{background:#000;color:white;text-align:center;}</style>", unsafe_allow_html=True)

# 6. دەم و نرخ
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.write(f"📅 {now.strftime('%Y-%m-%d')} | ⏰ {now.strftime('%H:%M:%S')}")

try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 2.5) * 100
except:
    rate = 147500

st.markdown(f"<h1 style='color:#00FF00;'>{rate:,.0f}</h1><p>{text['u']}</p>", unsafe_allow_html=True)

# 7. حسابکەر
st.write("---")
val = st.number_input("$ USD:", min_value=0.0, value=100.0)
if st.button("Enter"):
    st.session_state.res = val * (rate / 100)

if st.session_state.res:
    st.success(f"{st.session_state.res:,.0f} IQD")

# 8. بینەر و تێلەگرام
st.write(f"👤 {text['v']} {st.session_state.count}")
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:10px; border-radius:10px; text-decoration:none;">Telegram</a>', unsafe_allow_html=True)
