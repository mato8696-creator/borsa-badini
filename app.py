import streamlit as st
import requests

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5
except:
    dhok_rate = 1468.50

# ٣. ناڤ ونیشان
st.markdown("<h1 style='text-align: center;'>💰 بۆڕسا مەتین</h1>", unsafe_allow_html=True)
st.write("---")

# ٤. خانەیا نڤیسینا دۆلاران دگەل ڕێنمایا ب کوردی
st.markdown("### 💵 بڕێ دۆلاران بنڤیسە:")
usd_input = st.number_input(
    "Label", 
    min_value=0.0, 
    value=100.0, 
    step=1.0, 
    label_visibility="collapsed"
)

# ل شوینا نڤیسینا ئینگلیزی، ئەڤێ ب کوردی د بن دا بنڤیسە:
st.markdown("<p style='color: gray; font-size: 14px; text-align: right;'>💡 ل سەر کیبۆردێ کلیک ل 'Done' یان 'Enter' بکە</p>", unsafe_allow_html=True)

# ٥. حسابکرنا ئەنجامی
iqd_result = usd_input * dhok_rate

# ٦. نیشاندانا ئەنجامی ب ڕەنگێ کەسکێ گەش (وەک تە ڤیای)
st.write("---")
st.markdown(f"""
    <div style="text-align: center;">
        <h3 style="color: white;">زانینا بهایی ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 55px; font-weight: bold; text-shadow: 2px 2px 10px rgba(0,255,0,0.3);">
            {iqd_result:,.0f}
        </h1>
        <p style="color: #00FF00; font-size: 20px;">دینارێن عیراقی</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ٧. دوکما تێلەگرامێ یا مەزن
st.link_button("✈️ تێلەگرامێ من (Badini Matin)", "https://t.
