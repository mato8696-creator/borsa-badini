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

# ٣. ناڤ ونیشان
st.markdown("<h1 style='text-align: center; color: white;'>💰 بۆڕسا دهۆک</h1>", unsafe_allow_html=True)
st.write("---")

# ٤. خانەیا نڤیسینا دۆلاران (ب شێوەیەکێ مەزن)
st.markdown("### 💵 بڕێ دۆلاران بنڤیسە:")
usd_input = st.number_input("", min_value=0.0, value=100.0, step=1.0, format="%.f", label_visibility="collapsed")

# ٥. حسابکرنا پارەی
iqd_result = usd_input * dhok_rate

# ٦. نیشاندانا ئەنجامی ب شێوەیەکێ گەلەک جوان و ئۆتۆماتیک ل بن ژمارێ
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 20px; border-radius: 15px; border: 2px solid #4CAF50; text-align: center; margin-top: 20px;">
        <p style="color: #aaaaaa; font-size: 18px; margin-bottom: 5px;">ئەنجام ب دینارێن عیراقی:</p>
        <h1 style="color: #4CAF50; font-size: 45px; margin: 0;">{iqd_result:,.0f}</h1>
        <p style="color: #4CAF50; font-size: 20px; margin-top: 5px;">دینار</p>
    </div>
    """, unsafe_allow_html=True)

# ٧. زانیاریێن گەشەپێدەری
st.write("---")
st.markdown(f"<p style='text-align: center;'>👤 گەشەپێدەر: <b>مەتین عدنان</b></p>", unsafe_allow_html=True)
st.link_button("✈️ پەیوەندی ب تێلەگرامێ", "https://t.me/badinimatin")
