import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = "Kurdish"
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ گشتی
st.markdown("""
<style>
    .stApp { background-color: #000; }
    .ad-box {
        background: linear-gradient(45deg, #1a1a1a, #333);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        text-align: center;
        margin-bottom: 25px;
    }
    .ad-title { color: #bf953f; font-size: 14px; margin-bottom: 5px; }
    .company-name { color: #fff; font-size: 24px; font-weight: bold; }
    .ad-contact { color: #00FF00; font-size: 18px; }
</style>
""", unsafe_allow_html=True)

# 4. پشکا ڕیکلاما کۆمپانیێ (ل ڤێرێ تو دێ پارەی وەرگری)
st.markdown("""
<div class="ad-box">
    <p class="ad-title">Sponsor / سپۆنسەرێ سەرەکی</p>
    <div class="company-name">✨ ناڤێ کۆمپانیا تە ل ڤێرێ ✨</div>
    <p style="color: #ccc;">باشترین خزمەتگوزاری ل دهۆکێ</p>
    <div class="ad-contact">📞 پەیوەندی: 0750 XXX XXXX</div>
</div>
""", unsafe_allow_html=True)

# 5. ناڤ و نیشانێ سایتی
st.markdown("<h1 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)

# 6. وەرگرتنا بها (ب هەمان شێوەیێ جاران)
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    iqd_100 = 151500

# نیشاندانا بهایێ دۆلاری
st.markdown(f"""
<div style="background-color: #111; padding: 20px; border-radius: 15px; border: 1px solid #bf953f; text-align: center;">
    <p style="color: #fff;">بهایێ دۆلاری (100$)</p>
    <h1 style="color: #00FF00;">{iqd_100:,.0f} IQD</h1>
</div>
""", unsafe_allow_html=True)

# 7. Sidebar بۆ کۆنترۆڵێ
with st.sidebar:
    st.write("### Matin Control")
    st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
