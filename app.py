import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. ژمارەکەر
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ گشتی و پاقژکرنا نیشانێن 🔗
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
    div.stButton > button {{ background: linear-gradient(45deg, #FF0000, #990000) !important; color: white !important; font-weight: bold !important; width: 100%; border-radius: 10px; border: 1px solid #fff; height: 50px; font-size: 18px !important; }}
</style>
""", unsafe_allow_html=True)

# 4. شریتێ لڤۆک
st.markdown('<div class="marquee"><marquee scrollamount="5" direction="right">⚠️ هایداری: بهایێ بازارێ دهۆک یێ جێگیر نینە.. دەمژمێر ب دەمژمێر نوو دبیتەوە</marquee></div>', unsafe_allow_html=True)

# 5. دەمێ زیندی یێ دهۆکێ
duhok_tz = pytz.timezone('Asia/Baghdad')
now = datetime.now(duhok_tz)
date_time = now.strftime("📅 %Y-%m-%d | ⏰ %H:%M:%S")

# 6. شاشا سەرەکی
st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)
st.markdown(f'<div class="live-time">{date_time}</div>', unsafe_allow_html=True)

# وەرگرتنا نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

st.markdown(f"""<div class="card"><p>بهایێ دۆلاری (١٠٠$)</p><h2 style="color:#00FF00 !important; font-size: 50px; margin:0;">{iqd_100:,.0f}</h2></div>""", unsafe_allow_html=True)

# 7. پشکا حسابکرنێ (Enter)
st.write("---")
st.markdown("<h3>💵 گوهۆڕینا دۆلاری</h3>", unsafe_allow_html=True)
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0, step=50.0)

if st.button("حساب بکە (Enter)"):
    res_usd = usd_val * one_usd
    st.markdown(f"""<div style="background-color:rgba(0,255,0,0.1); padding:15px; border-radius:10px; text-align:center; border:2px solid #00FF00; margin-top:15px;"><p style="margin:0; color:#fff;">ئەنجام ب دینار:</p><h2 style="color:#00FF00 !important; margin:0;">{res_usd:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

# 8. دوکمێن پەیوەندیێ
st.markdown('<a href="https://wa.me/9647503233348" style="display:block; background:#25D366; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:20px; border: 1px solid #fff;">💬 واتسئاپ</a>', unsafe_allow_html=True)
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px; border: 1px solid #fff;">✈️ کەنالێ تێلەگرامی</a>', unsafe_allow_html=True)

# 9. Sidebar (Control)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
