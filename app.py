import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا مەتین", page_icon="📈")

# 2. وەرگرتنا بها ب شێوەیەکێ ئۆتۆماتیک
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5  # بهایێ بازاری
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd = 1468.5
    usd_to_try = 30.5
    usd_to_irr = 42000

# 3. ناڤێ دهۆک و تیرێن زیندی (Live Updates)
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px; margin-bottom: 0px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #4CAF50; font-size: 20px; font-weight: bold; margin-top: -10px;">
        زانینا بهایێ دۆلاری ل دهۆک 📈📉
    </div>
    <p style="text-align: center; color: #aaaaaa; font-size: 14px;">(بهایێ نوو یێ زیندی هەر چرکە دگوهۆڕیت)</p>
""", unsafe_allow_html=True)

st.write("---")

# 4. هەلبژارتنا دراڤی
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])

# 5. خانەیا بڕێ پارەی و دوکما سۆر
col1, col2 = st.columns([3, 1])

with col1:
    amount = st.number_input("بڕی لێرە بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")

with col2:
    st.markdown("""<style>div.stButton > button {background-color: #FF0000 !important; color: white !important; width: 100%; height: 45px; border-radius: 10px; font-weight: bold;}</style>""", unsafe_allow_html=True)
    if st.button("Enter"):
        pass

# 6. حسابکرنا ئەنجامی
if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

# 7. نیشاندانا ئەنجامی ب ڕەنگێ کەسکێ نێۆن (Neon Green)
st.write("---")
st.markdown(f"""
    <div style="background-color: #111111; padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center; box-shadow: 0px 0px 15px rgba(0, 255, 0, 0.2);">
        <h3 style="color: white; margin: 0; font-size: 18px;">ئەنجام ب دینارێن عیراقی:</h3>
        <h1 style="color: #00FF00; font-size: 55px; margin: 10px; font-family: sans-serif;">{result:,.0f}</h1>
        <p style="color: #4CAF50; margin: 0; font-weight: bold;">بهایێ ١٠٠$ نوکە: {usd_to_iqd * 100:,.0f}</p>
    </div>
""", unsafe_allow_html=True)

# 8. لینکا تێلەگرامێ
st.write("")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray; font-size: 12px; margin-top: 30px;'>Developed by Matin Adnan</p>", unsafe_allow_html=True)
