import streamlit as st
import requests
import time

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا مەتین", page_icon="💰")

# 2. درستکرنا ستایلێ لڤینێ (CSS)
st.markdown("""
    <style>
    /* ئەڤ بەشە دێ پاشبنەمایێ گوهۆڕیت */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
        background-color: #0e1117;
    }
    
    /* ئەنیمەیشنا دۆلارێن لڤۆک */
    @keyframes dollarMove {
        from { transform: translateY(0px); }
        to { transform: translateY(-20px); }
    }
    
    .floating-dollar {
        display: inline-block;
        color: #00FF00;
        font-size: 30px;
        animation: dollarMove 2s ease-in-out infinite alternate;
        opacity: 0.3;
        position: absolute;
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
    <div style="text-align: center; font-weight: bold; font-size: 55px; margin-bottom: 0px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #00FF00; font-size: 20px; font-weight: bold;">
        💵 زانینا بهایێ دراڤان ل دهۆک 💵
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 5. نیشانێن دۆلاری یێن لڤۆک ل ڕەخ و دوورێن پەیجێ
st.markdown('<div class="floating-dollar" style="left:5%; top:10%;"> $ </div>', unsafe_allow_html=True)
st.markdown('<div class="floating-dollar" style="right:10%; top:20%;"> $ </div>', unsafe_allow_html=True)
st.markdown('<div class="floating-dollar" style="left:15%; top:50%;"> $ </div>', unsafe_allow_html=True)
st.markdown('<div class="floating-dollar" style="right:5%; top:70%;"> $ </div>', unsafe_allow_html=True)

# 6. پشکا حسابکرنێ
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])
amount = st.number_input("بڕێ پارەی بنڤیسە:", min_value=0.0, value=100.0)

# 7. حسابکرنا ئەنجامی
if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

# 8. نیشاندانا ئەنجامی د چوارچۆڤەیەکێ گەش دا
st.write("")
st.markdown(f"""
    <div style="background-color: rgba(0, 0, 0, 0.6); padding: 30px; border-radius: 20px; border: 3px solid #00FF00; text-align: center; box-shadow: 0px 0px 20px #00FF00;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 55px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #00FF00; font-weight: bold;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 9. تێلەگرام
st.write("---")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
