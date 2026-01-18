import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - مەتین", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک هەر 60 چرکەیان
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. ستایلێ گشتی و دوکما سۆر
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%; height: 45px;
        border-radius: 10px; font-weight: bold; border: none;
    }
    @keyframes dollarMove {
        from { transform: translateY(0px); opacity: 0.1; }
        to { transform: translateY(-20px); opacity: 0.4; }
    }
    .floating-dollar {
        display: inline-block; color: #00FF00; font-size: 25px;
        animation: dollarMove 2s ease-in-out infinite alternate;
        position: absolute; z-index: 0;
    }
    </style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا بها ژ ئینتەرنێتێ
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd = 1470.0
    usd_to_try = 31.0
    usd_to_irr = 45000

# 5. ناڤ و نیشان و لڤینا دۆلاری
st.markdown('<div class="floating-dollar" style="left:5%; top:10%;"> $ </div>', unsafe_allow_html=True)
st.markdown('<div class="floating-dollar" style="right:10%; top:20%;"> $ </div>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #00FF00; font-size: 18px; font-weight: bold;">
        زانینا بهایێ دراڤان ل دهۆک 🔄
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 6. بەشێ حسابکرنا پارەی
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])
col1, col2 = st.columns([3, 1])
with col1:
    amount = st.number_input("بڕێ پارەی بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")
with col2:
    if st.button("Enter"):
        pass

if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

# 7. نیشاندانا ئەنجامی
st.markdown(f"""
    <div style="background-color: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 50px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #aaaaaa; margin: 0;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 8. پشکا ڕیکلامێ و وەرگرتنا پارەی (Monetization)
st.write("")
st.markdown("""
    <div style="background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px dashed #FFD700; text-align: center;">
        <h4 style="color: #FFD700; margin: 0;">📢 جهێ ڕیکلاما تە ل ڤێرێ 📢</h4>
        <p style="color: white; font-size: 13px; margin: 10px 0;">بۆ بەڵاڤکرنا ڕیکلامێن نڤیسینگەه و کارێن خۆ ل سەر ڤی سایتی، پەیوەندیێ ب مە بکەن.</p>
        <a href="https://t.me/badinimatin" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0088cc; color: white; border: none; padding: 8px 15px; border-radius: 8px; cursor: pointer; font-weight: bold;">
                📩 پەیوەندی ب تێلەگرامی بکە
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# 9. لینکا تێلەگراما شەخسی
st.write("---")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
