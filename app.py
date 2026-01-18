import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر (تەنێ مەتین دشێت ببینیت)
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و پاقژ و لادانا نیشانێن 🔗
st.markdown("""
<style>
    .stApp a.header-anchor { display: none !important; }
    header, [data-testid="stHeader"], #MainMenu, footer { visibility: hidden; }
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #fcf6ba !important; text-align: center; }
    .card {
        background: rgba(20, 20, 20, 0.9);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 5. شاشا سەرەکی
st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)

# نیشاندانا بهایێ دۆلاری
st.markdown(f'<div class="card"><p>بهایێ دۆلاری (١٠٠$)</p><h1 style="color:#00FF00 !important; font-size:50px;">{iqd_100:,.0f}</h1></div>', unsafe_allow_html=True)

# 6. پشکا حسابکرنێ (Enter)
st.write("---")
usd_input = st.number_input("بڕێ دۆلاری بنڤیسە ($):", min_value=0.0, value=100.0)

if st.button("حساب بکە (Enter) ⚡"):
    res = usd_input * one_usd
    st.markdown(f'<div class="card" style="border-color:#00FF00;"><h2 style="color:#00FF00 !important;">{res:,.0f} IQD</h2></div>', unsafe_allow_html=True)

# 7. دوکمێن پەیوەندیێ
st.markdown('<a href="https://wa.me/9647503233348" style="display:block; background:#25D366; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:20px;">💬 واتسئاپ</a>', unsafe_allow_html=True)
st.markdown('<a href="https://t.me/badinimatin" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px;">✈️ تێلەگرام</a>', unsafe_allow_html=True)

# 8. Sidebar (تەنێ بۆ مەتینی)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
