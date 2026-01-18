import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر (وەک د وێنەیێ تە دا 1760)
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ پڕۆفیشناڵ (وێنەیێ پشتخانیێ + لادانا نیشانا 🔗)
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071"
st.markdown(f"""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکی */
    .stApp a.header-anchor {{ display: none !important; }}
    header, #MainMenu, footer {{ visibility: hidden; }}

    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url("{bg_img}");
        background-size: cover;
    }}
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-shadow: 2px 2px 4px #000; }}
    .card {{
        background-color: rgba(20, 20, 20, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #bf953f;
        text-align: center;
        margin-bottom: 15px;
    }}
    .wa-btn {{
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 20px;
        border: 1px solid #fff;
    }}
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ هەلبژارتنا زمان (وەک د وێنەیێ تە دا)
if st.session_state.language is None:
    st.markdown("<h2 style='text-align:center;'>بۆڕسا دهۆک | Duhok Borsa</h2>", unsafe_allow_html=True)
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
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "gold": "بهایێ زێڕی (٢١)", "wa": "پەیوەندی ب واتسئاپێ"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "gold": "سعر الذهب (٢١)", "wa": "تواصل عبر الواتساب"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Rate (100$)", "gold": "Gold Rate (21K)", "wa": "Contact via WhatsApp"}
}[st.session_state.language]

# 6. نرخێن نوو
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
    gold_price = 495000
except:
    one_usd, iqd_100, gold_price = 1515, 151500, 495000

# 7. شاشا سەرەکی (ناڤ + کارتێن بها)
st.markdown(f"<h1 style='text-align:center;'>{t['title']}</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="card"><p>{t["usd"]}</p><h2 style="color:#00FF00 !important;">{iqd_100:,.0f}</h2></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="card"><p>{t["gold"]}</p><h2 style="color:#00FF00 !important;">{gold_price:,.0f}</h2></div>', unsafe_allow_html=True)

# 8. حسابکرنا دۆلاری
st.write("---")
usd_val = st.number_input("$ USD:", min_value=0.0, value=100.0)
st.markdown(f"<h2 style='text-align:center; color:#00FF00;'>{usd_val * one_usd:,.0f} IQD</h2>", unsafe_allow_html=True)

# 9. واتسئاپا تە (07503233348)
st.markdown(f'<a href="https://wa.me/9647503233348" class="wa-btn">💬 {t["wa"]}</a>', unsafe_allow_html=True)

# 10. Sidebar (Matin Control)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
