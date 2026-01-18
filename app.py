import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایل بۆ لادانا نیشانا 🔗 و پاقژکرنا شاشێ
st.markdown("""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکی */
    .stApp a.header-anchor { display: none !important; }
    header, [data-testid="stHeader"] { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #fcf6ba !important; text-align: center; }
    .card {
        background: rgba(30, 30, 30, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 15px;
    }
    .btn-link {
        display: block;
        text-align: center;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        color: white !important;
        border: 1px solid #fff;
    }
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ زمانان
if st.session_state.language is None:
    st.markdown("<br><h1>بۆڕسا دهۆک | Duhok Borsa</h1>", unsafe_allow_html=True)
    if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 5. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "wa": "واتسئاپ", "tg": "تلیگرام"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "wa": "واتساب", "tg": "تيليجرام"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Rate (100$)", "wa": "WhatsApp", "tg": "Telegram"}
}

# 6. وەرگرتنا نرخ
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 7. شاشا سەرەکی
sel_t = t[st.session_state.language]
st.markdown(f"<h1>{sel_t['title']}</h1>", unsafe_allow_html=True)

# وێنەیێ دۆلاری
st.image("https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=500", use_container_width=True)

st.markdown(f"""
<div class="card">
    <p>{sel_t['usd']}</p>
    <h1 style="color: #00FF00 !important; font-size: 45px; margin:0;">{iqd_100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 8. حسابکرن
st.write("---")
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0)
st.markdown(f"<h2 style='color:#00FF00;'>{usd_val * one_usd:,.0f} IQD</h2>", unsafe_allow_html=True)

# 9. لینکێن پەیوەندیێ
st.markdown(f'<a href="https://wa.me/9647503233348" class="btn-link" style="background:#25D366;">💬 {sel_t["wa"]}</a>', unsafe_allow_html=True)
st.markdown(f'<a href="https://t.me/matin_borsa" class="btn-link" style="background:#0088cc;">✈️ {sel_t["tg"]}</a>', unsafe_allow_html=True)

# 10. Sidebar (Matin Control)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
