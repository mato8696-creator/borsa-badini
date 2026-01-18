import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="refresh")

# 2. مێمۆری بۆ حسابکەرێ و بینەران
if 'calc_time' not in st.session_state: st.session_state.calc_time = 0
if 'last_res' not in st.session_state: st.session_state.last_res = ""
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 2064

if 'counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.counted = True

# 3. نرخێ ئۆتۆماتیک (دهۆک)
try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 160.5)
except:
    rate = 1471.5

# 4. دیزاین: وێنەیێ دۆلاری ل پشت نڤیسینان
dollar_bg = "https://images.unsplash.com/photo-1509017174183-0b7e1f48d3f9?q=80&w=2071"
st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url("{dollar_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    header, footer {{ visibility: hidden; }}
    .price-box {{ background: rgba(0,0,0,0.6); padding: 30px; border-radius: 20px; border: 2px solid #bf953f; text-align: center; }}
    h1 {{ color: #00FF00 !important; font-size: 60px !important; text-shadow: 2px 2px 10px #000; }}
    .stNumberInput label {{ color: white !important; font-size: 18px; }}
</style>
""", unsafe_allow_html=True)

# 5. شاشا سەرەکی
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="price-box">
    <p style="color:white; font-size:20px;">بهایێ دۆلاری (١٠٠$)</p>
    <h1>{rate*100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 6. حسابکەرا ئۆتۆماتیک (بۆ ١ دەقە)
st.write("---")
usd_input = st.number_input("💵 بڕێ دۆلاری داخل بکە ($):", min_value=0.0, step=100.0)

if st.button("حساب بکە"):
    res = usd_input * rate
    st.session_state.last_res = f"{usd_input:,.0f}$ = {res:,.0f} IQD"
    st.session_state.calc_time = time.time()

# نیشاندانا ئەنجامی بۆ ماوێ ٦٠ چرکە
if st.session_state.last_res and (time.time() - st.session_state.calc_time < 60):
    st.success(st.session_state.last_res)
    rem = int(60 - (time.time() - st.session_state.calc_time))
    st.caption(f"⏱️ دێ بەرزە بیت پشتی {rem} چرکە")
elif st.session_state.last_res:
    st.session_state.last_res = ""

# 7. بینەر
st.markdown(f"<div style='color:#bf953f; text-align:center; margin-top:50px; font-weight:bold;'>👤 بینەرێن حەقیقی: {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
