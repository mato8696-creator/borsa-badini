import streamlit as st
import requests

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

st.title("💰 حاسیبەیێ بلەز یێ دهۆکێ")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5 
except:
    dhok_rate = 1468.50 

st.write(f"📊 بهایێ ١٠٠ دۆلاران نوکە: **{dhok_rate * 100:,.0f}** دینار")
st.write("---")

# ٣. بەشێ حاسیبەیێ: ل ڤێرە بکار‌هێنەر دشێت ب کەیفا خۆ ژمارەیێ دیار کەت
st.subheader("💵 بڕێ دۆلاران دەستنیشان بکە:")

# من ل ڤێرە Slider بکارئینایە چونکە ئێکسەر ئەنجامی ددەت بێ Enter
usd_amount = st.slider("تبلا خۆ ل سەر ڤێ خەتێ بلەڤینە دا ژمارەیێ هەلبژیری:", min_value=1, max_value=1000, value=100)

# ٤. حسابکرن و نیشاندانا ئەنجامی
iqd_result = usd_amount * dhok_rate

st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #00ff00; text-align: center;">
        <h2 style="color: white; margin: 0;">بهایێ {usd_amount} دۆلاران دبیتە:</h2>
        <h1 style="color: #00ff00; font-size: 50px; margin: 10px;">{iqd_result:,.0f}</h1>
        <h2 style="color: white; margin: 0;">دینارێن عیراقی</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
