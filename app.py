import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
# نووکرنا سایتێ هەر ١٠ چرکە بۆ هندێ نرخ هەمیشە نوو بیت
st_autorefresh(interval=10000, limit=None, key="fscounter")

# 2. مێمۆری و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'calculation_result' not in st.session_state: st.session_state.calculation_result = None
if 'count' not in st.session_state: st.session_state.count = 2586 

if 'counted' not in st.session_state:
    st.session_state.count += 1
    st.session_state.counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.language is None:
    st.markdown("<style>.stApp{background:#000;text-align:center;} h2{color:#bf953f;}</style>", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    st.stop()

# 4. وەرگێڕان و ڕوونکرنا ل سەرێ سایتی
t = {
    "Kurdish": {
        "info": "🌐 ئەڤ نرخە ئۆتۆماتیکی ژ سیستەمێ بانکی یێ جیهانی دهێت و دگەل بازارێ دهۆک دهێتە گونجاندن",
        "usd": "بهایێ دۆلاری (١٠٠$)", "calc": "💵 حسابکەرا پارەی", "btn": "Enter", "v": "بینەرێن سایتێ:"
    },
    "Arabic": {
        "info": "🌐 يتم تحديث هذه الأسعار تلقائياً من النظام المصرفي العالمي ومطابقتها مع سوق دهوك",
        "usd": "سعر الدولار (١٠٠$)", "calc": "💵 حاسبة العملات", "btn": "Enter", "v": "زوار الموقع:"
    }
}[st.session_state.language]

# 5. ستایلێ گشتی
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071"
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-attachment: fixed; }}
    .info-box {{ background: rgba(191,149,63,0.1); padding:10px; border-radius:10px; border:1px solid #bf953f; color:#fcf6ba; text-align:center; font-size:14px; margin-bottom:20px; }}
    .card {{ background: rgba(20,20,20,0.9); padding:25px; border-radius:15px; border:2px solid #bf953f; text-align:center; }}
    .price {{ color: #00FF00 !important; font-size: 55px !important; font-weight: bold; }}
</style>
""", unsafe_allow_html=True)

# 6. نیشاندانا ڕوونکرنێ ل سەرێ سایتی
st.markdown(f'<div class="info-box">{t["info"]}</div>', unsafe_allow_html=True)

# 7. دەم و نرخێ ئۆتۆماتیک
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>📅 {now.strftime('%Y-%m-%d')} | ⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 158.5) * 100
except:
    rate = 151500

st.markdown(f'<div class="card"><p style="color:white;">{t["usd"]}</p><h1 class="price">{rate:,.0f}</h1></div>', unsafe_allow_html=True)

# 8. حسابکەر و بینەر
st.write("---")
usd_in = st.number_input("$ USD:", min_value=0.0, value=100.0)
if st.button(t['btn']):
    st.session_state.calculation_result = usd_in * (rate / 100)

if st.session_state.calculation_result:
    st.success(f"{st.session_state.calculation_result:,.0f} IQD")

st.markdown(f"<div style='color:#bf953f; text-align:center; margin-top:20px;'>👤 {t['v']} {st.session_state.count}</div>", unsafe_allow_html=
