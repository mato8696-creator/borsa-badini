import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک | جیهانی", page_icon="🌍", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر
if 'visits' not in st.session_state: st.session_state.visits = 75
st.session_state.visits += 1

# 3. ستایلێ ڕەش و زێڕین (Premium Design)
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .main-card {
        background: linear-gradient(145deg, #1a1a1a, #0a0a0a);
        padding: 20px; border-radius: 20px;
        border: 1px solid #bf953f; text-align: center; margin-bottom: 20px;
    }
    .price-text { color: #fcf6ba; font-weight: bold; font-size: 24px; }
    .label-text { color: #888; font-size: 14px; }
    div.stButton > button {
        background: linear-gradient(45deg, #bf953f, #aa771c) !important;
        color: black !important; width: 100%; height: 45px;
        border-radius: 10px; font-weight: bold; border: none;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا هەمی بهایێن جیهانی
try:
    # دراڤ و کانزا
    data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd = data['rates']['IQD'] + 158.5
    eur = data['rates']['EUR']
    gbp = data['rates']['GBP']
    try_rate = data['rates']['TRY']
    irr = data['rates']['IRR']
    
    # کرێپتۆ (بهایێ سادە)
    crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd").json()
    btc = crypto['bitcoin']['usd']
    eth = crypto['ethereum']['usd']
except:
    iqd, eur, gbp, try_rate, irr, btc, eth = 1485, 0.92, 0.78, 34, 60000, 65000, 35000

# 5. سەرێ سایتی
st.markdown("<h1 style='text-align:center; color:#bf953f;'>DUHOK GLOBAL BORSA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>بۆڕسا دهۆک یا جیهانی - مەتین عەدنان</p>", unsafe_allow_html=True)

# 6. نیشاندانا بهایێن سەرەکی (Row 1: Gold & USD)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="main-card"><p class="label-text">USD / IQD</p><p class="price-text">{iqd*100:,.0f}</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="main-card"><p class="label-text">Gold 21 (Mithqal)</p><p class="price-text">488,000</p></div>', unsafe_allow_html=True)

# 7. بهایێن کرێپتۆ (Row 2: Bitcoin & Ethereum)
col3, col4 = st.columns(2)
with col3:
    st.markdown(f'<div class="main-card"><p class="label-text">Bitcoin (BTC)</p><p class="price-text">${btc:,.0f}</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="main-card"><p class="label-text">Ethereum (ETH)</p><p class="price-text">${eth:,.0f}</p></div>', unsafe_allow_html=True)

# 8. پشکا وەرگێڕانا دراڤان (Converter)
st.write("---")
st.markdown("<h4 style='color:#bf953f;'>کالکۆلێتەرێ جیهانی</h4>", unsafe_allow_html=True)
curr_list = ["USD 💵", "EUR 🇪🇺", "GBP 🇬🇧", "TRY 🇹🇷", "IRR 🇮🇷"]
selected_curr = st.selectbox("دراڤەکێ هەلبژێرە:", curr_list)
amount = st.number_input("بڕێ پارەی:", min_value=0.0, value=100.0)

if st.button("حساب بکە (Enter)"):
    pass

# مەنتقێ حسابێ
if "USD" in selected_curr: res = amount * iqd
elif "EUR" in selected_curr: res = (amount / eur) * iqd
elif "GBP" in selected_curr: res = (amount / gbp) * iqd
elif "TRY" in selected_curr: res = (amount / try_rate) * iqd
else: res = (amount / irr) * iqd

st.success(f"ئەنجام ب دینارێ عیراقی: {res:,.0f} IQD")

# 9. تێلەگرام
st.write("")
st.markdown(f"""
<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;">
    <div style="background: linear-gradient(45deg, #0088cc, #00aaff); padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">
        📩 پەیوەندی ب مە بکە (Telegram)
    </div>
</a>
""", unsafe_allow_html=True)

# 10. Sidebar Admin
with st.sidebar:
    if st.text_input("Admin Password", type="password") == "matin2026":
        st.metric("Total Views", st.session_state.visits)
        st.write("Duhok Market Fix: 158.5")
