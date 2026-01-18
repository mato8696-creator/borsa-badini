import streamlit as st
import requests

# 1. ڕێکخستنا سەرەکی یا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# 2. وەرگرتنا بهایێ دۆلاری ب شێوەیەکێ پاراستی
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    rate_val = data['rates']['IQD']
    dhok_rate = rate_val + 158.5
except:
    dhok_rate = 1468.50

# 3. ناڤ ونیشان
st.markdown("<h1 style='text-align: center;'>💰 بۆڕسا دهۆک</h1>", unsafe_allow_html=True)
st.write("---")

# 4. خانەیا نڤیسینا دۆلاران
st.subheader("💵 بڕێ دۆلاران بنڤیسە:")
usd_input = st.number_input("بڕی لێرە بنڤیسە:", min_value=0.0, value=100.0, step=1.0, label_visibility="collapsed")

# 5. حسابکرنا ئەنجامی
iqd_result = usd_input * dhok_rate

# 6. نیشاندانا ئەنجامی ب شێوەیەکێ جوان و مەزن
st.success(f"✅ ئەنجام بۆ {usd_input:,.0f} دۆلار دبیتە:")
st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{iqd_result:,.0f} دینار</h1>", unsafe_allow_html=True)

st.write("---")

# 7. **دوکما تێلەگرامێ ب شێوەیەکێ گەلەک دیار و مەزن**
st.markdown("### 📢 بۆ پەیوەندی و زانیاریێن پتر:")
st.link_button("✈️ تێلەگرامێ من (Badini Matin)", "https://t.me/badinimatin", use_container_width=True)

# 8. ناڤێ گەشەپێدەری
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Designed by: Matin Adnan</p>", unsafe_allow_html=True)
