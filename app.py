import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5
except:
    dhok_rate = 1468.50

st.title("💰 حاسیبەیێ دهۆکێ")
st.write(f"📊 بهایێ ١٠٠$ نوکە: **{dhok_rate * 100:,.0f}** دینار")
st.write("---")

# ٣. خانەیا نڤیسینێ کو پێدڤی ب Enter نەکەت (بکارئینانا Step)
st.subheader("💵 بڕێ دۆلاران بنڤیسە:")

# ئەڤە خانەیەکە، هەر دەما تو ژمارەکێ بگوهۆڕی یان بنڤیسی، ئێکسەر دێ ئەنجامی دەت
usd_input = st.number_input("", min_value=0.0, value=100.0, step=1.0, format="%.f")

# ٤. نیشاندانا ئەنجامی ب شێوەیەکێ زۆر جوان و ڕوون (بێ تێکەلی)
iqd_result = usd_input * dhok_rate

st.markdown(f"""
    <div style="background-color: #262730; padding: 30px; border-radius: 15px; border: 2px solid #00ff00; text-align: center;">
        <h2 style="color: #ffffff;">ئەنجام ب دینار:</h2>
        <h1 style="color: #00ff00; font-size: 45px;">{iqd_result:,.0f}</h1>
        <h2 style="color: #ffffff;">دینارێن عیراقی</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
