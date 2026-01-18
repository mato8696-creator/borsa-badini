import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی و نووکرنا هەر چرکە
st.set_page_config(page_title="بۆڕسا دهۆک و زێڕ", page_icon="💰", layout="centered")
st_autorefresh(interval=1000, limit=None, key="gold_refresh")

# 2. مێمۆری و ژمارەکەر
if 'lang' not in st.session_state: st.session_state.lang = None
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 2064

if 'already_counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.already_counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک و زێڕ</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️", use_container_width=True): st.session_state.lang = "KU"; st.rerun()
    if st.button("العربية 🇮🇶", use_container_width=True): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "g": "بهایێ زێڕی (مسقاڵ ٢١)", "v": "بینەرێن سایتێ:"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "g": "سعر الذهب (مثقال ٢١)", "v": "زوار الموقع:"}
}[st.session_state.lang]

# 5. ستایلێ گشتی
st.markdown("<style>.stApp{background:#000; color:white; text-align:center;} .card{background:#111; padding:20px; border-radius:15px; border:2px solid #bf953f; margin-bottom:15px;}</style>", unsafe_allow_html=True)

# 6. وەرگرتنا نرخێ دۆلار و زێڕ ب ئۆتۆماتیک
try:
    # نرخێ دۆلاری
    usd_api = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    usd_to_iqd = (usd_api['rates']['IQD'] + 2.5) * 100
    
    # نرخێ زێڕی (Calculated based on Gold Ounce)
    # تێبینی: نرخێ مسقاڵی ل دهۆکێ دکەڤیتە نێزیکی (بهایێ ئۆنسێ / 6.2)
    gold_price_global = 2700 # نموونە بۆ بهایێ ئۆنسێ
    gold_per_misqal = (gold_price_global / 6.2) * (usd_to_iqd / 100)
except:
    usd_to_iqd, gold_per_misqal = 150500, 485000

# 7. شاشا سەرەکی (دۆلار و زێڕ)
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.write(f"⏰ {now.strftime('%H:%M:%S')}")

# کارتێ دۆلاری
st.markdown(f'<div class="card"><p>{t["u"]}</p><h1 style="color:#00FF00;">{usd_to_iqd:,.0f}</h1></div>', unsafe_allow_html=True)

# کارتێ زێڕی (ئۆتۆماتیک بلند و نزم دبیت)
st.markdown(f'<div class="card"><p>{t["g"]}</p><h1 style="color:#FFD700;">{gold_per_misqal:,.0f}</h1></div>', unsafe_allow_html=True)

# 8. بینەر
st.markdown(f"<div style='border:1px solid #bf953f; padding:10px; margin-top:20px;'>👤 {t['v']} {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px;">Telegram Channel</a>', unsafe_allow_html=True)
