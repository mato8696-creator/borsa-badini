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

# 3. ستایل بۆ پاقژکرنا سایتی و لادانا نیشانا 🔗
st.markdown("""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکی */
    .stApp a.header-anchor { display: none !important; }
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #bf953f !important; }

    /* ستایلێ دوکما واتسئاپێ */
    .whatsapp-btn {
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        margin-top: 25px;
        border: 1px solid #fff;
    }
</style>
""", unsafe_allow_html=True)

# 4. هەلبژارتنا زمان
if st.session_state.language is None:
    st.markdown("<h2 style='text-align:center;'>Duhok Borsa | بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 5. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "calc": "گوهۆڕینا دۆلاری", "wa": "پەیوەندی ب واتسئاپێ"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "calc": "تحويل الدولار", "wa": "تواصل عبر الواتساب"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Rate (100$)", "calc": "USD Converter", "wa": "Contact via WhatsApp"}
}[st.session_state.language]

# 6. وەرگرتنا نرخ
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1
