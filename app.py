import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = "Kurdish"
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و زێڕین و لادانا نیشانێن زێدە
st.markdown("""
<style>
    /* لادانا نیشانا 🔗 یا سیستمێ ل ڕەخ ناڤان */
    .stApp a.header-anchor { display: none !important; }
    header, [data-testid="stHeader"] { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #bf953f !important; text-align: center; }
    
    .card {
        background: #111;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* نیشانا Anchor یا جوان کو تە دڤیا */
    .custom-anchor {
        font-size: 30px;
        color: #bf953f;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "wa": "واتسئاپ", "tg": "تلیگرام"}
}
sel = t["Kurdish"]

# 5. وەرگرتنا نرخێ دۆلاری
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 6. شاشا سەرەکی
st.markdown(f"<h1>{sel['title']}</h1>", unsafe_allow_html=True)

# وێنەیێ دۆلاری ل سەر پاشخانەکا ڕەش
st.image("https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=1000", use_container_width=True)

# نیشانا Anchor یا جوان ل بن وێنەی
st.markdown('<div class="custom-anchor">🔗 ━━━━━━━━━ 🔗</div>', unsafe_allow_html=True)

# کارتا بها
st.markdown(f"""
<div class="card">
    <p>{sel['usd']}</p>
    <h1 style="color: #00FF00 !important; font-size: 50px; margin:0;">{iqd_100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 7. حسابکرن
st.write("---")
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0)
st.markdown(f"<h2 style='color:#00FF00;'>{usd_val * one_usd:,.0f} IQD</h2>", unsafe_allow_html=True)

# 8. دوکمێن پەیوەندیێ
st.markdown(f'<a href="https://wa.me/9647503233348" style="display:block; background:#25D366; color:white; text-align:center; padding:12px; border-radius:10px; text-decoration:none; font-weight:bold; margin-top:10px;">💬 {sel["wa"]}</a>', unsafe_allow_html=True)
st.markdown(f'<a href="https://t.me/matin_borsa" style="display:block; background:#0088cc; color:white; text-align:center; padding:12px; border-radius:10px; text-decoration:none; font-weight:bold; margin-top:10px;">✈️ {sel["tg"]}</a>', unsafe_allow_html=True)

# 9. Sidebar (تەنێ مەتین دشێت بینەران ببینیت)
with st.sidebar:
    st.write("### Matin Private Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        # ڤێرە جهێ دیتنا چەند کەس داخل بووینە
        st.metric("ژمارا بینەرێن ئەڤڕۆ", st.session_state.count)
