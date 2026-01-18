import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

st.title("💰 حاسیبەیێ بلەز یێ دهۆکێ")
st.write("---")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5 
except:
    dhok_rate = 1468.50 

# ٣. بەشێ حاسیبەیێ ب شێوەیەکێ ئۆتۆماتیک (بێ Enter)
st.subheader("💵 بڕێ دۆلاران لێرە دیار بکە:")

# مە لێرە Slider دانا، ب ڤێ ڕێکێ هەر دەمێ بلەڤینیت، ئەنجام دێ گوهۆڕیت
usd_amount = st.slider("", min_value=1, max_value=1000, value=100, step=1)

# ٤. نیشاندانا ئەنجامی ب شێوەیەکێ زیندی
iqd_result = usd_amount * dhok_rate

st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; border-left: 5px solid #4CAF50;">
        <h3 style="color: #333;">بهایێ {usd_amount} دۆلاران:</h3>
        <h1 style="color: #4CAF50;">{iqd_result:,.0f} دینار</h1>
    </div>
    """, unsafe_allow_html=True)

# ٥. زانیاریێن زێدە
st.write("---")
st.metric("بهایێ بازارێ دهۆکێ (١٠٠$)", f"{dhok_rate * 100:,.0f} IQD")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
