import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا مەتین", page_icon="☀️")

# 2. وەرگرتنا بها ب شێوەیەکێ ئۆتۆماتیک (دۆلار، لیرە، تمەن)
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158  # بهایێ دۆلاری ل دهۆک
    usd_to_try = data['rates']['TRY']        # دۆلار بۆ لیرە
    usd_to_irr = data['rates']['IRR']        # دۆلار بۆ تمەن
except:
    usd_to_iqd = 1468
    usd_to_try = 30.5
    usd_to_irr = 42000

# 3. ناڤێ دهۆک ب ڕەنگێن ئالایێ کوردستانێ
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #4CAF50; font-size: 20px; font-weight: bold;">
        زانینا بهایێ دراڤان ل دهۆک
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 4. هەلبژارتنا جورێ دراڤی
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])

# 5. خانەیا بڕێ پارەی و دوکما سۆر
col1, col2 = st.columns([3, 1])

with col1:
    amount = st.number_input("بڕی لێرە بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")

with col2:
    st.markdown("""<style>div.stButton > button {background-color: #FF0000 !important; color: white !important; width: 100%; height: 45px; border-radius: 10px;}</style>""", unsafe_allow_html=True)
    if st.button("Enter"):
        pass

# 6. حسابکرنا ئەنجامی ل دویڤ دراڤی
if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
    text = "دینارێن عیراقی"
elif "لیرەیا تورکی" in currency_type:
    # لیرە بۆ دینار (حسابکرن ل سەر بنەمایێ دۆلاری)
    result = (amount / usd_to_try) * usd_to_iqd
    text = "دینارێن عیراقی"
else:
    # تمەن بۆ دینار
    result = (amount / usd_to_irr) * usd_to_iqd
    text = "دینارێن عیراقی"

st.write("---")
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 45px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: gray; margin: 0;">{text}</p>
    </div>
""", unsafe_allow_html=True)

# 7. لینکا تێلەگرامێ
st.write("")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
