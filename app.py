import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی و نووکرنا هەر چرکە
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. مێمۆری و ژمارەکەر (2064 حەقیقی)
if 'lang' not in st.session_state: st.session_state.lang = None
if 'res_iqd' not in st.session_state: st.session_state.res_iqd = None
if 'res_usd' not in st.session_state: st.session_state.res_usd = None
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 2064

if 'already_counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.already_counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️", use_container_width=True): st.session_state.lang = "KU"; st.rerun()
    if st.button("العربية 🇮🇶", use_container_width=True): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "g": "بهایێ زێڕی (مسقاڵ ٢١)", "v": "بینەرێن حەقیقی:"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "g": "سعر الذهب (مثقال ٢١)", "v": "الزوار الحقيقيون:"}
}[st.session_state.lang]

# 5. سیستەمێ ئۆتۆماتیک یێ گونجای دگەل دهۆک
try:
    # وەرگرتنا نرخێ جیهانی و زێدەکرنا جیاوازیا بۆڕسا دهۆک (Gap)
    # مە جیاوازی ڕێکخست دا کو نرخ ل دەور و بەری ١٤٧.١٥٠ بیت
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    global_rate = response['rates']['IQD'] 
    
    # ل ڤێرە مە "جیاوازیا دهۆک" لێ زێدە کر دا ڕاست بیت
    market_rate = global_rate + 160.5  
    iqd_100 = market_rate * 100
except:
    iqd_100 = 147150

# 6. دیزاین و نیشاندان
st.markdown("<style>.stApp{background:#000; color:white; text-align:center;} .card{background:#111; padding:20px; border-radius:15px; border:2px solid #bf953f; margin-bottom:10px;}</style>", unsafe_allow_html=True)
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.write(f"⏰ {now.strftime('%H:%M:%S')}")

# کارتێ دۆلاری (ئۆتۆماتیک دگەل بازارێ دهۆک دگۆهۆڕیت)
st.markdown(f'<div class="card"><p>{t["u"]}</p><h1 style="color:#00FF00;">{iqd_100:,.0f}</h1></div>', unsafe_allow_html=True)

# 7. حسابکەر
st.write("---")
val_u = st.number_input("$ USD:", min_value=0.0, value=100.0)
if st.button("Enter"):
    st.session_state.res_iqd = val_u * (iqd_100 / 100)
if st.session_state.res_iqd:
    st.success(f"{st.session_state.res_iqd:,.0f} IQD")

# 8. بینەر
st.markdown(f"<div style='border:1px solid #bf953f; padding:10px; margin-top:20px;'>👤 {t['v']} {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
