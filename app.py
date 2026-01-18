import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1750
st.session_state.count += 1

# 3. لاپەڕێ دەسپێکێ (زمان)
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە | اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3: 
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 4. وەرگێڕان (Enter زێدە کر)
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", 
        "usd_live": "بهایێ دۆلاری (١٠٠$)", 
        "gold_live": "بهایێ زێڕی (٢١)", 
        "usd_calc_title": "💵 گوهۆڕینا دۆلاری بۆ دیناری",
        "usd_amt": "بڕێ دۆلاری ($):",
        "gold_calc_title": "⚖️ حسابکرنا زێڕی (غرام)",
        "gold_amt": "کێشێ زێڕی (غرام):",
        "btn": "Enter"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", 
        "usd_live": "سعر الدولار (١٠٠$)", 
        "gold_live": "سعر الذهب (٢١)", 
        "usd_calc_title": "💵 تحويل الدولار إلى دينار",
        "usd_amt": "أدخل مبلغ الدولار ($):",
        "gold_calc_title": "⚖️ حساب الذهب (غرام)",
        "gold_amt": "أدخل وزن الذهب (غرام):",
        "btn": "Enter"
    },
    "English": {
        "title": "Duhok Global Borsa", 
        "usd_live": "USD Rate (100$)", 
        "gold_live": "Gold Rate (21K)", 
        "usd_calc_title": "💵 USD to IQD Converter",
        "usd_amt": "USD Amount ($):",
        "gold_calc_title": "⚖️ Gold Calculator",
        "gold_amt": "Gold Weight (Gram):",
        "btn": "Enter"
    }
}
t = translations[st.session_state.language]

# 5. ستایلێ گشتی و وێنەیێ پاشبنەمایێ
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071&auto=format&fit=crop"
st.markdown(f"""
<style>
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-position: center; background-attachment: fixed; }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-shadow: 2px 2px 4px #000; }}
    .card {{ background-color: rgba(20, 20, 20, 0.9); padding: 20px; border-radius: 15px; border: 1px solid #bf953f; text-align: center; margin-bottom: 15px; }}
    
    /* دوکما سۆر و نڤیسینا Enter */
    div.stButton > button {{ 
        background: linear-gradient(45deg, #FF0000, #990000) !important; 
        color: white !important; 
        font-weight: bold !important; 
        width: 100%; 
        border-radius: 10px; 
        border: 2px solid #fff; 
        height: 55px; 
        font-size: 22px !important; 
        letter-spacing: 2px;
    }}
    
    input {{ background-color: #111 !important; color: white !important; border: 1px solid #bf953f !important; font-size: 20px !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(0,0,0,0.95) !important; border-right: 1px solid #bf953f; }}
</style>
""", unsafe_allow_html=True)

# 6. وەرگرتنا بهایان
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd_rate = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd_rate * 100
    gold_mithqal = 495000
    gold_gram = gold_mithqal / 5
except:
    one_usd_rate, iqd_100, gold_mithqal, gold_gram = 1515, 151500, 495000, 99000

# 7. شاشا سەرەکی
st.markdown(f"<h1 style='text-align:center;'>{t['title']}</h1>", unsafe_allow_html=True)

# 8. سندوقێن بهایێن زیندی
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""<div class="card"><p style="margin:0;">{t['usd_live']}</p><h2 style="color:#00FF00 !important;">{iqd_100:,.0f}</h2></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="card"><p style="margin:0;">{t['gold_live']}</p><h2 style="color:#00FF00 !important;">{gold_mithqal:,.0f}</h2></div>""", unsafe_allow_html=True)

st.write("---")

# 9. پشکا گوهۆڕینا دۆلاری
st.markdown(f"<h3>{t['usd_calc_title']}</h3>", unsafe_allow_html=True)
usd_input = st.number_input(t['usd_amt'], min_value=0.0, value=100.0, step=50.0)
if st.button(t['btn'], key="usd_btn"):
    result_iqd = usd_input * one_usd_rate
    st.markdown(f"""<div style="background-color:rgba(0,255,0,0.1); padding:15px; border-radius:10px; text-align:center; border:2px solid #00FF00;">
    <h2 style="color:#00FF00 !important; margin:0;">{result_iqd:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

st.write("---")

# 10. پشکا حسابکرنا زێڕی
st.markdown(f"<h3>{t['gold_calc_title']}</h3>", unsafe_allow_html=True)
gold_w = st.number_input(t['gold_amt'], min_value=0.0, value=26.0, step=1.0)
if st.button(t['btn'], key="gold_btn"):
    total_gold = gold_w * gold_gram
    st.markdown(f"""<div style="background-color:rgba(255,255,255,0.1); padding:15px; border-radius:10px; text-align:center; border:2px solid #bf953f;">
    <h2 style="color:#fcf6ba !important; margin:0;">{total_gold:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

# 11. تێلەگرام
st.write("")
st.markdown(f"""<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;"><div style="background-color:#0088cc; padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">Telegram Channel</div></a>""", unsafe_allow_html=True)

# 12. پشکا پاسۆرد (Sidebar)
with st.sidebar:
    st.markdown("<h3 style='color:#bf953f;'>Matin Control</h3>", unsafe_allow_html=True)
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
