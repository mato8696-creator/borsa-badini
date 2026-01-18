import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="refresh_all")

# 2. مێمۆری
if 'lang' not in st.session_state: st.session_state.lang = None
if 'calc_time' not in st.session_state: st.session_state.calc_time = 0
if 'last_res' not in st.session_state: st.session_state.last_res = ""
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 2064

if 'counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<style>.stApp{background:#000;text-align:center;} h2{color:#bf953f;}</style>", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.lang = "KU"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
text = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "c": "حسابکەرا پارەی", "v": "بینەرێن حەقیقی:", "btn": "Enter", "owner": ":"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "c": "حاسبة العملات", "v": "الزوار الحقيقيون:", "btn": "تحويل", "owner": "بإشراف:"}
}[st.session_state.lang]

# 5. ستایل و وێنەیێ دۆلاری
dollar_img = "https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=2070"
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{dollar_img}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .owner-tag {{ color: #bf953f; font-weight: bold; font-size: 20px; text-align: center; margin-bottom: 5px; }}
    .price-card {{ background: rgba(20,20,20,0.9); padding: 25px; border-radius: 20px; border: 2px solid #bf953f; text-align: center; }}
    h1 {{ color: #00FF00 !important; font-size: 55px !important; font-weight: bold; }}
    p, label, h3 {{ color: white !important; }}
</style>
""", unsafe_allow_html=True)

# 6. ناڤێ تە ل سەرێ سایتی
st.markdown(f'<div class="owner-tag">{text["owner"]} Matin A. Muhammed</div>', unsafe_allow_html=True)

# 7. نرخێ ئۆتۆماتیک
try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 160.5)
except:
    rate = 1471.5

# 8. شاشا سەرەکی
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="price-card">
    <p>{text['u']}</p>
    <h1>{rate*100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 9. حسابکەرا ١ دەقیقە
st.write("---")
st.markdown(f"<h3>{text['c']}</h3>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD:", min_value=0.0, value=100.0)

if st.button(text['btn']):
    res_iqd = usd_val * rate
    st.session_state.last_res = f"{usd_val:,.0f}$ = {res_iqd:,.0f} IQD"
    st.session_state.calc_time = time.time()

if st.session_state.last_res and (time.time() - st.session_state.calc_time < 60):
    st.success(st.session_state.last_res)
    rem = int(60 - (time.time() - st.session_state.calc_time))
    st.caption(f"⏱️ {rem}")
elif st.session_state.last_res:
    st.session_state.last_res = ""

# 10. بینەر
st.markdown(f"<div style='color:#bf953f; text-align:center; margin-top:40px; border-top:1px solid #333; padding-top:10px;'>👤 {text['v']} {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
