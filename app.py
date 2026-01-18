import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا مەتین", page_icon="💰")

# 2. ستایلێ لڤینێ و دوکما سۆر (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    /* ستایلێ دوکما سۆر */
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%;
        height: 45px;
        border-radius: 10px;
        font-weight: bold;
        border: none;
    }
    /* ئەنیمەیشنا دۆلارێن لڤۆک ل پشت نڤیسینێ */
    @keyframes dollarMove {
        from { transform: translateY(0px); opacity: 0.1; }
        to { transform: translateY(-20px); opacity: 0.4; }
    }
    .floating-dollar {
        display: inline-block;
        color: #00FF00;
        font-size: 25px;
        animation: dollarMove 2s ease-in-out infinite alternate;
        position: absolute;
        z-index: 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. وەرگرتنا بها
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd = 1468.5
    usd_to_try = 30.5
    usd_to_irr = 42000

# 4. ناڤێ دهۆک ب ڕەنگێن ئالایێ کوردستانێ
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 55px; position: relative; z-index: 1;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #00FF00; font-size: 18px; font-weight: bold; position: relative; z-index: 1;">
        زانینا بهایێ دراڤان ل دهۆک 📈
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 5. نیشانێن دۆلاری یێن لڤۆک
st.markdown('<div class="floating-dollar" style="left:5%; top:15%;"> $ </div>', unsafe_allow_html=True)
st.markdown('<div class="floating-dollar" style="right:10%; top:25%;"> $ </div>', unsafe_allow_html=True)

# 6. بەشێ هەلبژارتن و خانەیا نڤیسینێ دگەل دوکما سۆر
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])

col1, col2 = st.columns([3, 1])
with col1:
    amount = st.number_input("بڕێ پارەی بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")
with col2:
    # دوکما سۆر ئەوا تە دڤیا
    if st.button("Enter"):
        pass

# 7. حسابکرنا ئەنجامی
if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

# 8. ئەنجامێ جوان
st.write("")
st.markdown(f"""
    <div style="background-color: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center; position: relative; z-index: 1;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 50px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #aaaaaa; margin: 0;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 9. تێلەگرام
st.write("---")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
