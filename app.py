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

# 3. ستایل بۆ لادانا نیشانا 🔗 و ڕەشکرنا پشتخانیێ
st.markdown("""
<style>
    .stApp a.header-anchor { display: none !important; }
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #bf953f !important; }
    .wa-btn {
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ زمانان
if st.session_state.language is None:
    st.markdown("<h2 style='text-align:center;'>Duhok Borsa | بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2:
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3:
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 5. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "wa": "پەیوەندی ب واتسئاپێ"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "wa": "تواصل عبر الواتساب"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Rate (100$)", "wa": "Contact via WhatsApp"}
}[st.session_state.language]

# 6. نرخێن بازار
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 7. نیشاندانا ناڤ و نرخ
st.markdown(f"<h1 style='text-align:center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"""
<div style="background-color: #111; padding: 25px; border-radius: 15px; border: 2px solid #bf953f; text-align: center;">
    <p>{t['usd']}</p>
    <h1 style="color: #00FF00 !important; font-size: 40px;">{iqd_100:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 8. حسابکرنا دۆلاری
st.write("---")
usd_val = st.number_input("$ USD:", min_value=0.0, value=100.0)
res_iqd = usd_val * one_usd
st.markdown(f"<h2 style='text-align:center; color:#00FF00;'>{res_iqd:,.0f} IQD</h2>", unsafe_allow_html=True)

# 9. واتسئاپا تە (07503233348)
st.markdown(f'<a href="https://wa.me/9647503233348" class="wa-btn">💬 {t["wa"]}</a>', unsafe_allow_html=True)

# 10. کۆنترۆڵ (Password: matin2026)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
