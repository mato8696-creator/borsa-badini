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
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.lang = "KU"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "KU": {
        "info": "🌐 ئەڤ نرخە ئۆتۆماتیکی ژ سیستەمێ بانکی یێ جیهانی دهێت و دگەل بازارێ دهۆک دهێتە گونجاندن",
        "usd_live": "بهایێ دۆلاری (١٠٠$)", "calc_usd": "💵 حسابکەرا دۆلاری (USD -> IQD)", 
        "calc_iqd": "🇮🇶 حسابکەرا دیناری (IQD -> USD)", "btn": "Enter", "v": "بینەرێن سایتێ:"
    },
    "AR": {
        "info": "🌐 يتم تحديث الأسعار تلقائياً من النظام المصرفي العالمي ومطابقتها مع سوق دهوك",
        "usd_live": "سعر الدولار (١٠٠$)", "calc_usd": "💵 حاسبة الدولار (USD -> IQD)", 
        "calc_iqd": "🇮🇶 حاسبة الدينار (IQD -> USD)", "btn": "Enter", "v": "زوار الموقع:"
    }
}[st.session_state.lang]

# 5. ستایلێ گشتی
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071"
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-attachment: fixed; }}
    .info-box {{ background: rgba(191,149,63,0.1); padding:10px; border-radius:10px; border:1px solid #bf953f; color:#fcf6ba; text-align:center; font-size:14px; margin-bottom:20px; }}
    .card {{ background: rgba(20,20,20,0.9); padding:20px; border-radius:15px; border:2px solid #bf953f; text-align:center; margin-bottom:15px; }}
    .price {{ color: #00FF00 !important; font-size: 50px !important; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)

# 6. ڕوونکرن و دەم
st.markdown(f'<div class="info-box">{t["info"]}</div>', unsafe_allow_html=True)
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>📅 {now.strftime('%Y-%m-%d')} | ⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 7. وەرگرتنا نرخ
try:
    one_usd_rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 2.5)
    iqd_100 = one_usd_rate * 100
except:
    one_usd_rate, iqd_100 = 1475.0, 147500

st.markdown(f'<div class="card"><p style="color:white;">{t["usd_live"]}</p><h1 class="price">{iqd_100:,.0f}</h1></div>', unsafe_allow_html=True)

# 8. حسابکەر ١: دۆلار بۆ دینار
st.markdown(f"<h3 style='color:white;'>{t['calc_usd']}</h3>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0, key="usd_in")
if st.button(t['btn'], key="btn1"):
    st.session_state.res_iqd = usd_val * one_usd_rate

if st.session_state.res_iqd:
    st.success(f"Result: {st.session_state.res_iqd:,.0f} IQD")

st.write("---")

# 9. حسابکەر ٢: دینار بۆ دۆلار (نوو)
st.markdown(f"<h3 style='color:white;'>{t['calc_iqd']}</h3>", unsafe_allow_html=True)
iqd_val = st.number_input("🇮🇶 IQD Amount:", min_value=0.0, value=150000.0, step=1000.0, key="iqd_in")
if st.button(t['btn'], key="btn2"):
    st.session_state.res_usd = iqd_val / one_usd_rate

if st.session_state.res_usd:
    st.info(f"Result: ${st.session_state.res_usd:,.2f}")

# 10. بینەر و تێلەگرام
st.markdown(f"<div style='color:#bf953f; text-align:center; margin-top:20px;'>👤 {t['v']} {st.session_state.count}</div>", unsafe_allow_html=True)
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px;">✈️ Telegram Channel</a>', unsafe_allow_html=True)
