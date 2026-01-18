import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. لاپەڕێ هەلبژارتنا زمانی (ئێکەم تشت دیار دبیت)
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; width: 100%; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە / اختر لغتك / Choose Language</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("کوردی ☀️"): 
            st.session_state.language = "Kurdish"
            st.rerun()
    with col2:
        if st.button("العربية 🇮🇶"): 
            st.session_state.language = "Arabic"
            st.rerun()
    with col3:
        if st.button("English 🇺🇸"): 
            st.session_state.language = "English"
            st.rerun()
    st.stop()

# 4. وەرگێڕان (تەنێ دۆلار)
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", "usd_live": "بهایێ دۆلاری (١٠٠$)", 
        "news": "⚠️ هایداری: بهایێ بازارێ دهۆک یێ جێگیر نینە",
        "usd_calc": "💵 گوهۆڕینا دۆلاری", "res": "ئەنجام ب دینار:", "tele": "کەنالێ تێلەگرامی", "btn": "حساب بکە (Enter)"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", "usd_live": "سعر الدولار (١٠٠$)", 
        "news": "⚠️ تنبيه: أسعار سوق دهوك غير مستقرة",
        "usd_calc": "💵 تحويل الدولار", "res": "النتيجة بالدينار:", "tele": "قناة التيليجرام", "btn": "تحویل"
    },
    "English": {
        "title": "Duhok Global Borsa", "usd_live": "USD Rate (100$)", 
        "news": "⚠️ Notice: Duhok market rates are unstable",
        "usd_calc": "💵 USD Converter", "res": "Result in IQD:", "tele": "Telegram Channel", "btn": "Calculate"
    }
}
t = translations[st.session_state.language]

# 5. ستایلێ گشتی
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071"
st.markdown(f"""
<style>
    .stApp a.header-anchor {{ display: none !important; }}
    header, [data-testid="stHeader"], #MainMenu, footer {{ visibility: hidden; }}
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}"); background-size: cover; background-position: center; background-attachment: fixed; }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-align: center; }}
    .card {{ background-color: rgba(20, 20, 20, 0.9); padding: 25px; border-radius: 15px; border: 2px solid #bf953f; text-align: center; margin-bottom: 15px; }}
    .live-time {{ font-size: 18px; color: #00FF00 !important; font-weight: bold; margin-bottom: 20px; text-align: center; border: 1px solid #bf953f; padding: 5px; border-radius: 10px; background: rgba(0,0,0,0.5); }}
    .marquee {{ background-color: rgba(191, 149, 63, 0.2); color: #fcf6ba; padding: 10px; font-weight: bold; border-bottom: 1px solid #bf953f; margin-bottom: 20px; }}
    div.stButton > button {{ background: linear-gradient(45deg, #FF0000, #990000) !important; color: white !important; font-weight: bold !important; border-radius: 10px; border: 1px solid #fff; height: 50px; font-size: 18px !important; }}
</style>
""", unsafe_allow_html=True)

# 6. شریتێ لڤۆک
st.markdown(f'<div class="marquee"><marquee scrollamount="5" direction="right">{t["news"]}</marquee></div>', unsafe_allow_html=True)

# 7. دەمێ زیندی یێ دهۆکێ
duhok_tz = pytz.timezone('Asia/Baghdad')
now = datetime.now(duhok_tz)
date_time = now.strftime("📅 %Y-%m-%d | ⏰ %H:%M:%S")

# 8. شاشا سەرەکی
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f'<div class="live-time">{date_time}</div>', unsafe_allow_html=True)

# وەرگرتنا نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

st.markdown(f"""<div class="card"><p>{t['usd_live']}</p><h2 style="color:#00FF00 !important; font-size: 50px; margin:0;">{iqd_100:,.0f}</h2></div>""", unsafe_allow_html=True)

# 9. پشکا حسابکرنێ (Enter)
st.write("---")
st.markdown(f"<h3>{t['usd_calc']}</h3>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0, step=50.0)

if st.button(t['btn']):
    res_usd = usd_val * one_usd
    st.markdown(f"""<div style="background-color:rgba(0,255,0,0.1); padding:15px; border-radius:10px; text-align:center; border:2px solid #00FF00; margin-top:15px;"><p style="margin:0; color:#fff;">{t['res']}</p><h2 style="color:#00FF00 !important; margin:0;">{res_usd:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

# 10. دوکمێن پەیوەندیێ
st.markdown('<a href="https://wa.me/9647503233348" style="display:block; background:#25D366; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:20px; border: 1px solid #fff;">💬 واتسئاپ</a>', unsafe_allow_html=True)
st.markdown(f'<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px; border: 1px solid #fff;">✈️ {t["tele"]}</a>', unsafe_allow_html=True)

# 11. Sidebar
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
