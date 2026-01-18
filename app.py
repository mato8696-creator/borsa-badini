import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر (تەنێ مەتین دبینیت)
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و لادانا نیشانێن سیستمێ
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
    .my-anchor {
        font-size: 45px;
        color: #bf953f;
        text-align: center;
        margin: 15px 0;
    }
    .btn-wa {
        display: block;
        background: #25D366;
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        border: 1px solid #fff;
    }
</style>
""", unsafe_allow_html=True)

# 4. شاشا سەرەکی
st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)

# وێنەیێ دۆلاری
st.image("https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=1000", use_container_width=True)

# نیشانا 🔗 یا تە دڤیا
st.markdown('<div class="my-anchor">🔗</div>', unsafe_allow_html=True)

# 5. نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd_100 = (resp['rates']['IQD'] + 158.5) * 100
except:
    iqd_100 = 151500

st.markdown(f"""
<div class="card">
    <p>بهایێ دۆلاری (١٠٠$)</p>
    <h1 style="color: #fcf6ba !important; font-size: 50px; margin:0;">{iqd_100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 6. حسابکرن
st.write("---")
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0)
st.markdown(f"<h2 style='color:#fcf6ba;'>{(usd_val * (iqd_100/100)):,.0f} IQD</h2>", unsafe_allow_html=True)

# 7. دوکما واتسئاپێ ب تەنێ
st.markdown(f'<a href="https://wa.me/9647503233348" class="btn-wa">💬 واتسئاپ</a>', unsafe_allow_html=True)

# 8. Sidebar (Matin Control)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەر", st.session_state.count)
