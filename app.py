import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بورسا مەتین", page_icon="☀️")

# 2. وەرگرتنا بها ب شێوەیەکێ سادە
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    dhok_rate = data['rates']['IQD'] + 158
except:
    dhok_rate = 1468

# 3. ناڤێ دهۆک ب ڕەنگێن ئالایێ کوردستانێ (پێکڤە)
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px; margin-bottom: 0px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; 
                     -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #4CAF50; font-size: 22px; font-weight: bold; margin-top: -10px;">
        زانینا بهایێ دۆلاری ل دهۆک
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 4. خانەیا دۆلاران و دوکما سۆر ل ڕەخ
col1, col2 = st.columns([3, 1])

with col1:
    usd_amount = st.number_input("Dollar", min_value=0.0, value=100.0, label_visibility="collapsed")

with col2:
    # دوکما سۆر بۆ حسابکرنێ
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #FF0000 !important;
            color: white !important;
            width: 100%;
            height: 45px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    if st.button("Enter"):
        pass

# 5. حسابکرن و نیشاندانا ئەنجامی
iqd_result = usd_amount * dhok_rate

st.write("---")
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 55px; margin: 10px;">{iqd_result:,.0f}</h1>
        <p style="color: gray; margin: 0;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 6. لینکا تێلەگرامێ
st.write("")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
