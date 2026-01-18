import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر (Counter) - دێ ل سەر شاشێ دیار بیت
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و پاقژ
st.markdown("""
<style>
    .stApp a.header-anchor { display: none !important; }
    header, [data-testid="stHeader"], #MainMenu, footer { visibility: hidden; }
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #fcf6ba !important; text-align: center; }
    .card {
        background: rgba(20, 20, 20, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 15px;
    }
    .visitor-box {
        background: #111;
        padding: 10px;
        border-radius: 10px;
        border: 1px dashed #bf953f;
        color: #00FF00;
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 4. پیشاندانا ژمارا بینەران (وەک تە دڤیا)
st.markdown(f'<div class="visitor-box">👁️ ژمارا بینەرێن ئەڤڕۆ: {st.session_state.count}</div>', unsafe_allow_html=True)

st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=1000", use_container_width=True)

# 5. نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

st.markdown(f"""
<div class="card">
    <p>بهایێ دۆلاری (١٠٠$)</p>
    <h1 style="color: #00FF00 !important; font-size: 50px; margin:0;">{iqd_100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 6. پشکا حسابکرنێ دگەل دوکما (Enter)
st.write("---")
st.markdown("### 🧮 حسابکەرێ پارەی")
usd_input = st.number_input("بڕێ دۆلاری بنڤیسە ($):", min_value=0.0, value=100.0)

# دوکما Enter (Calculate)
if st.button("حساب بکە (Enter) ⚡"):
    result = usd_input * one_usd
    st.markdown(f"""
    <div style="background:#222; padding:20px; border-radius:10px; border:1px solid #00FF00;">
        <h2 style="color:#00FF00; margin:0;">{result:,.0f} IQD</h2>
    </div>
    """, unsafe_allow_html=True)

# 7. پەیوەندی
st.markdown(f'<a href="https://wa.me/9647503233348" style="display:block; background:#25D366; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:20px;">💬 واتسئاپ</a>', unsafe_allow_html=True)
