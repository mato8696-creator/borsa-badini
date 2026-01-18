import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. مێمۆری و ژمارەکەر
if 'lang' not in st.session_state: st.session_state.lang = None
if 'res_iqd' not in st.session_state: st.session_state.res_iqd = None
if 'res_usd' not in st.session_state: st.session_state.res_usd = None
if 'count' not in st.session_state: st.session_state.count = 2586 

if 'counted' not in st.session_state:
    st.session_state.count += 1
    st.session_state.counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<style>.stApp{background:#000;text-align:center;} h2{color:#bf953f;}</style>", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.lang = "KU"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "KU": {
        "usd_live": "بهایێ دۆلاری یێ بازارێ دهۆک (١٠٠$)", 
        "calc_usd": "💵 گوهۆڕینا دۆلاری بۆ دیناری", 
        "calc_iqd": "🇮🇶 گوهۆڕینا دیناری بۆ دۆلاری", "btn": "حساب بکە", "v": "بینەر:"
    },
    "AR": {
        "usd_live": "سعر الدولار في سوق دهوك (١٠٠$)", 
        "calc_usd": "💵 تحويل الدولار إلى دينار", 
        "calc_iqd": "🇮🇶 تحويل الدينار إلى دولار", "btn": "تحويل", "v": "زوار الموقع:"
    }
}[st.session_state.lang]

# 5. ستایلێ گشتی
st.markdown("<style>header,footer{visibility:hidden;} .stApp{background:#000;color:white;text-align:center;} .card{background:rgba(20,20,20,0.9);padding:20px;border-radius:15px;border:2px solid #bf953f;}</style>", unsafe_allow_html=True)

# 6. نرخێ بازارێ ڕەش (ل ڤێرە تو ب خۆ دشێی نرخێ بۆڕسێ دەستکاری بکەی)
# نوکە مە یێ دانای ل سەر ١٥٠،٥٠٠
current_market_rate = 1505 # ئانکو ١٥٠،٥٠٠ بۆ هەر ١٠٠ دۆلاران
iqd_100 = current_market_rate * 100

# 7. شاشا سەرەکی
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.write(f"⏰ {now.strftime('%H:%M:%S')}")
st.markdown(f'<div class="card"><p>{t["usd_live"]}</p><h1 style="color:#00FF00;">{iqd_100:,.0f}</h1></div>', unsafe_allow_html=True)

# 8. حسابکەر ١: دۆلار بۆ دینار
st.write("---")
st.markdown(f"<h4>{t['calc_usd']}</h4>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0, key="u_in")
if st.button(t['btn'], key="b1"):
    st.session_state.res_iqd = usd_val * current_market_rate

if st.session_state.res_iqd:
    st.success(f"{st.session_state.res_iqd:,.0f} IQD")

# 9. حسابکەر ٢: دینار بۆ دۆلار
st.markdown(f"<h4>{t['calc_iqd']}</h4>", unsafe_allow_html=True)
iqd_val = st.number_input("🇮🇶 IQD Amount:", min_value=0.0, value=150000.0, step=1000.0, key="i_in")
if st.button(t['btn'], key="b2"):
    st.session_state.res_usd = iqd_val / current_market_rate

if st.session_state.res_usd:
    st.info(f"${st.session_state.res_usd:,.2f}")

# 10. بینەر
st.write(f"👤 {t['v']} {st.session_state.count}")
