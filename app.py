import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. سیستەمێ هەژمارتنا بینەران یێ حەقیقی
if 'lang' not in st.session_state: st.session_state.lang = None
if 'res_iqd' not in st.session_state: st.session_state.res_iqd = None
if 'res_usd' not in st.session_state: st.session_state.res_usd = None

# ل ڤێرە ژمارەیا تە یا حەقیقی دپارێزین
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 2064 

if 'already_counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.already_counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️", use_container_width=True):
        st.session_state.lang = "KU"; st.rerun()
    if st.button("العربية 🇮🇶", use_container_width=True):
        st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "c1": "گوهۆڕینا دۆلاری بۆ دیناری", "c2": "گوهۆڕینا دیناری بۆ دۆلاری", "v": "بینەرێن حەقیقی:"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "c1": "تحويل الدولار إلى دينار", "c2": "تحويل الدينار إلى دولار", "v": "الزوار الحقيقيون:"}
}[st.session_state.lang]

# 5. نرخێ بازارێ دهۆک (ئەوێ تو ب خۆ دشێی بگۆهۆڕی)
market_rate = 150.50  # بۆ هەر ١ دۆلارەکێ
iqd_100 = market_rate * 100

# 6. دیزاین و شاشا سەرەکی
st.markdown("<style>.stApp{background:#000; color:white; text-align:center;}</style>", unsafe_allow_html=True)
st.markdown(f"<h1 style='color:#00FF00;'>{iqd_100:,.0f}</h1><p>{t['u']}</p>", unsafe_allow_html=True)

# 7. هەردوو حسابکەر (دۆلار بۆ دینار و بەروڤاژی)
st.write("---")
usd_val = st.number_input("$ USD:", min_value=0.0, value=100.0)
if st.button("حساب بکە (USD -> IQD)"):
    st.session_state.res_iqd = usd_val * market_rate
if st.session_state.res_iqd:
    st.success(f"{st.session_state.res_iqd:,.0f} IQD")

st.write("---")
iqd_val = st.number_input("🇮🇶 IQD:", min_value=0.0, value=150000.0, step=1000.0)
if st.button("حساب بکە (IQD -> USD)"):
    st.session_state.res_usd = iqd_val / market_rate
if st.session_state.res_usd:
    st.info(f"${st.session_state.res_usd:,.2f}")

# 8. نیشاندانا بینەران
st.markdown(f"<div style='border:1px solid #bf953f; padding:10px; margin-top:20px;'>👤 {t['v']} {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
