import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. لاپەڕێ دەسپێکێ
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3: 
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 4. وەرگێڕان (تەنێ دۆلار)
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", "usd_live": "بهایێ دۆلاری (١٠٠$)", 
        "usd_calc": "💵 گوهۆڕینا دۆلاری", "res": "ئەنجام ب دینار:", "tele": "کەنالێ تێلەگرامی", "btn": "Enter"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", "usd_live": "سعر الدولار (١٠٠$)", 
        "usd_calc": "💵 تحويل الدولار", "res": "النتيجة بالدينار:", "tele": "قناة التيليجرام", "btn": "Enter"
    },
    "English": {
        "title": "Duhok Global Borsa", "usd_live": "USD Rate (100$)", 
        "usd_calc": "💵 USD Converter", "res": "Result in IQD:", "tele": "Telegram Channel", "btn": "Enter"
    }
}
t = translations[st.session_state.language]

# 5. ستایلێ گشتی
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071&auto=format&fit=crop"
st.markdown(f"""
<style>
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-position: center; background-attachment: fixed; }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-shadow: 2px 2px 4px #000; }}
    .card {{ background-color: rgba(20, 20, 20, 0.9); padding: 20px; border-radius: 15px; border: 2px solid #bf953f; text-align: center; margin-bottom: 15px; }}
    input {{ background-color: #111 !important; color: white !important; border: 1px solid #bf953f !important; font-size: 20px !important; }}
    div.stButton > button {{ background: linear-gradient(45deg, #FF0000, #990000) !important; color: white !important; font-weight: bold !important; width: 100%; border-radius: 10px; border: 1px solid #fff; height: 50px; font-size: 20px !important; margin-top: 10px; }}
    .result-box {{ background-color: rgba(0,255,0,0.1); padding: 15px; border-radius: 10px; text-align: center; border: 2px solid #00FF00; margin-top: 15px; }}
    [data-testid="stSidebar"] {{ background-color: rgba(0,0,0,0.95) !important; border-right: 1px solid #bf953f; }}
    .tele-btn {{ display: block; background: linear-gradient(45deg, #0088cc, #005580); color: white !important; text-align: center; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold; margin-top: 20px; border: 1px solid #fff; }}
</style>
""", unsafe_allow_html=True)

# 6. وەرگرتنا بها
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 7. شاشا سەرەکی
st.markdown(f"<h1 style='text-align:center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"""<div class="card"><p>{t['usd_live']}</p><h2 style="color:#00FF00 !important; font-size: 45px;">{iqd_100:,.0f}</h2></div>""", unsafe_allow_html=True)

# 8. پشکا دۆلاری دگەل دوکما Enter
st.write("---")
st.markdown(f"<h3>{t['usd_calc']}</h3>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0, step=50.0)

if st.button(t['btn'], key="btn_usd"):
    res_usd = usd_val * one_usd
    st.markdown(f"""<div class="result-box"><p style="margin:0; color:#fff;">{t['res']}</p><h2 style="color:#00FF00 !important; margin:0;">{res_usd:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

# 9. تێلەگرام
st.markdown(f'<a href="https://t.me/badinimatin" target="_blank" class="tele-btn">🔗 {t["tele"]}</a>', unsafe_allow_html=True)

# 10. Sidebar
with st.sidebar:
    st.markdown("<h3 style='color:#bf953f;'>Matin Control</h3>", unsafe_allow_html=True)
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
