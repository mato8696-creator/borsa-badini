import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا مەتین", page_icon="📈")

# 2. دروستکرنا لڤینا دۆلاری ل پشت نڤیسینان (Background Animation)
st.markdown("""
    <style>
    .stApp {
        background: #0e1117;
        overflow: hidden;
    }
    .dollar-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
        pointer-events: none;
    }
    .symbol {
        position: absolute;
        color: rgba(0, 255, 0, 0.1);
        font-size: 24px;
        animation: move 10s linear infinite;
    }
    @keyframes move {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <div class="dollar-bg">
        <div class="symbol" style="left: 10%; animation-delay: 0s;">$</div>
        <div class="symbol" style="left: 20%; animation-delay: 2s;">$</div>
        <div class="symbol" style="left: 40%; animation-delay: 4s;">$</div>
        <div class="symbol" style="left: 60%; animation-delay: 1s;">$</div>
        <div class="symbol" style="left: 80%; animation-delay: 6s;">$</div>
        <div class="symbol" style="left: 90%; animation-delay: 3s;">$</div>
    </div>
""", unsafe_allow_html=True)

# 3. وەرگرتنا بها ب شێوەیەکێ ئۆتۆماتیک
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
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #4CAF50; font-size: 22px; font-weight: bold; margin-top: -10px;">
        زانینا بهایێ دراڤان ل دهۆک 📈
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 5. پشکا حسابکرنێ
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])
amount = st.number_input("بڕی بنڤیسە:", min_value=0.0, value=100.0)

if st.button("Enter / حساب بکە", use_container_width=True):
    pass

# 6. حسابکرنا ئەنجامی
if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

# 7. نیشاندانا ئەنجامی ب شێوەیەکێ جوان
st.write("---")
st.markdown(f"""
    <div style="background-color: rgba(20, 20, 20, 0.8); padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 50px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #4CAF50;">بهایێ ١٠٠$ نوکە: {usd_to_iqd * 100:,.0f}</p>
    </div>
""", unsafe_allow_html=True)

# 8. لینکا تێلەگرامێ
st.write("")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
