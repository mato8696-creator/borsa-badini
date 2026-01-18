import streamlit as st
import requests

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5 # بهایێ بازارێ دهۆکێ
except:
    dhok_rate = 1468.50

# ٣. ناڤ ونیشانێ سایتێ تە
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💰 بۆڕسا مەتین (دهۆک)</h1>", unsafe_allow_html=True)
st.write("---")

# ٤. خانەیا نڤیسینا دۆلاران
st.markdown("### 💵 بڕێ دۆلاران بنڤیسە:")
usd_input = st.number_input("", min_value=0.0, value=100.0, step=1.0, format="%.f", label_visibility="collapsed")

# ٥. حسابکرنا پارەی
iqd_result = usd_input * dhok_rate

# ٦. نیشاندانا ئەنجامی ب شێوەیەکێ جوان
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #00ff00; text-align: center; margin-top: 10px;">
        <p style="color: #aaaaaa; font-size: 18px; margin: 0;">ئەنجام ب دینارێن عیراقی:</p>
        <h1 style="color: #00ff00; font-size: 50px; margin: 10px;">{iqd_result:,.0f}</h1>
        <p style="color: #00ff00; font-size: 20px; margin: 0;">دینار</p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # بۆشایی

# ٧. **دیارکرنا لینکا تێلەگرامێ ب شێوەیەکێ گەلەک دیار**
st.markdown("### 📢 بۆ پەیوەندی و زانیاریێن زێدەتر:")
st.link_button("✈️ تێلەگرامێ من (Badini Matin)", "https://t.me/badinimatin", use_
