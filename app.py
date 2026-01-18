import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="☀️")

# 2. وەرگرتنا بها ب شێوەیەکێ سادە
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    dhok_rate = data['rates']['IQD'] + 158
except:
    dhok_rate = 1468

# 3. ناڤێ دهۆک ب ڕەنگێن ئالایێ کوردستانێ
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px; line-height: 1.2;">
        <span style="color: #FF0000;">د</span><span style="color: #FF0000;">هـ</span>
        <span style="color: #FFD700;">ۆ</span>
        <span style="color: #008000;">ک</span>
    </div>
    <div style="text-align: center; color: gray; font-size: 18px;">بۆڕسا مەتین عدنان</div>
""", unsafe_allow_html=True)

st.write("---")

# 4. خانەیا دۆلاران و دوکما سۆر ل ڕەخ فە
col1, col2 = st.columns([3, 1])

with col1:
    usd_amount = st.number_input("بڕێ دۆلاران بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")

with col2:
    # دوکما حسابکرنێ ب ڕەنگێ سۆر
    if st.button("حساب بکە", type="primary"):
        pass # دەما کلیک لێ دهێتە کرن پەیج رێفرێش دبیت و حساب دکەت

# 5. حسابکرن و نیشاندانا ئەنجامی
iqd_result = usd_amount * dhok_rate

st.write("---")
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 10px solid #008000; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 45px; margin: 10px;">{iqd_result:,.0f}</h1>
        <p style="color: white; margin: 0;">بهایێ ١٠٠$ ئەڤڕۆ: {dhok_rate * 100:,.0f}</p>
    </div>
""", unsafe_allow_html=True)

# 6. لینکا تێلەگرامێ
st.write("")
st.link_button("✈️ Telegram: Badini Matin", "https://t.me/badinimatin", use_container_width=True)
