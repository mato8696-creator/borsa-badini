import streamlit as st
import requests
from datetime import datetime
import pytz
import time

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا دەمێ دروست یێ دهۆکێ
iq_timezone = pytz.timezone('Asia/Baghdad')
now = datetime.now(iq_timezone)

# ٣. نیشاندانا دەمژمێرێ ب شێوەیەکێ مەزن و دیار
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; border: 2px solid #00ff00; text-align: center;">
        <h1 style="color: #00ff00; margin: 0; font-family: monospace;">⏰ {now.strftime('%I:%M:%S %p')}</h1>
        <p style="color: white; margin: 0;">{now.strftime('%Y-%m-%d')}</p>
    </div>
    """, unsafe_allow_html=True)

# ٤. ناڤ و پەیوەندی
st.title("💰 بۆڕسا  (دهۆک)")
st.markdown(f"### 👤 گەشەپێدەر: مەتین عدنان محمد")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
st.write("---")

# ٥. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 157.5 # نێزیکی ١٤٦،٧٥٠
    
    st.metric(label="بهایێ ١ دۆلاری ل دهۆکێ", value=f"{dhok_rate:,.2f} IQD")
    
    st.write("---")
    st.markdown("### 🧮 حاسیبەیێ بازارێ دهۆکێ")
    amount = st.number_input("چەند دۆلار تە هەنە؟", value=100.0)
    total_iqd = amount * dhok_rate
    st.success(f"بهایێ {amount:,} دۆلاران دبیتە: **{total_iqd:,.0f}** دینار")

except:
    st.error("کێشەک هەبوو!")

# ٦. فێڵەکا زەریف بۆ نووکرنا دەمژمێرێ (Refresh)
# ئەڤە دێ هەر ١٠ چرکەیان جارەکێ سایتێ تە نوو کەت دا دەمژمێر نەڕاوەستیت
time.sleep(10)
st.rerun()
