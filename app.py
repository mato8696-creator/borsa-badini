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
bg_url = "https://images.unsplash.com/photo-1611974714658-058e11ee5d46?q=80&w=2070"
st.markdown(f"""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکی */
    .stApp a.header-anchor {{ display: none !important; }}
    header, #MainMenu, footer {{ visibility: hidden; }}

    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_url}");
        background-size: cover;
        background-position: center;
    }}
    
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-align: center; }}
    
    .card {{
        background: rgba(30, 30, 30, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 15px;
    }}
    
    .wa-btn {{
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        border: 1px solid #fff;
    }}
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
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "usd": "بهایێ دۆلاری (١٠٠$)", "gold": "بهایێ زێڕی (٢١)", "wa": "پەیوەندی ب واتسئاپێ"},
    "Arabic": {"title": "بورصة دهوك العالمية", "usd": "سعر الدولار (١٠٠$)", "gold": "سعر الذهب (٢١)", "wa": "تواصل عبر الواتساب"},
    "English": {"title": "Duhok Global Borsa", "usd": "USD Rate (100$)", "gold": "Gold Rate (21K)", "wa": "Contact via WhatsApp"}
}[st.session_state.language]

# 6. وەرگرتنا نرخێن ئۆتۆماتیکی
try:
    # وەرگرتنا دۆلاری
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
    
    # حسابکرنا زێڕی ب نێزیکی بۆ بازاڕێ دهۆکێ
    # بهایێ ئۆنسەیا زێڕی دابەشی 31.1 بکە، پاشان زێڕێ 21 حساب بکە
    gold_api = requests.get("https://api.gold-api.com/price/XAU").json()
    ounce_price = gold_api['price']
    gram_24_usd = ounce_price / 31.1
    gram_21_iqd = (gram_24_usd * 0.875) * one_usd # زێڕێ 21
    gold_price_total = gram_21_iqd * 1 # بۆ هەر مسقالەکێ
    # نێزیککرن بۆ بهایێ دهۆکێ
    gold_final = (gold_price_total * 4.48) + 15000 
except:
    iqd_100, gold_final = 151500, 495000

# 7. نیشاندانا بها وەک "کارت"
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
    <p>{t['usd']}</p>
    <h1 style="color: #00FF00 !important; font-size: 45px; margin:0;">{iqd_100:,.0f}</h1>
</div>
<div class="card">
    <p>{t['gold']}</p>
    <h1 style="color: #FFD700 !important; font-size: 45px; margin:0;">{gold_final:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 8. حسابکرن
st.write("---")
usd_val = st.number_input("$ USD Amount:", min_value=0.0, value=100.0)
st.markdown(f"<h2 style='color:#00FF00;'>{usd_val * (iqd_100/100):,.0f} IQD</h2>", unsafe_allow_html=True)

# 9. واتسئاپا تە (07503233348)
st.markdown(f'<a href="https://wa.me/9647503233348" class="wa-btn">💬 {t["wa"]}</a>', unsafe_allow_html=True)

# 10. Sidebar (Matin Control)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
