import streamlit as st
import requests
from datetime import datetime
import pytz

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا دەمێ دروست یێ کوردستانێ
iq_timezone = pytz.timezone('Asia/Baghdad')
now = datetime.now(iq_timezone)
current_time = now.strftime("%I:%M:%S %p")
current_date = now.strftime("%Y-%m-%d")

# ٣. نیشاندانا دەمژمێرێ ب شێوەیەکێ جوان و مەزن
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50; text-align: center;">
        <h1 style="color: #4CAF50; margin: 0;">⏰ {current_time}</h1>
        <p style="color: white; margin: 5px;">📅 {current_date}</p>
    </div>
    """, unsafe_allow_status=True)

st.write("") # بۆشایی

# ٤. ناڤ و پەیوەندی
st.title("💰 بۆڕسا مەتین (دهۆک)")
st.markdown(f"### 👤 گەشەپێدەر: مەتین عدنان محمد")
st.link_button("✈️ پەیوەندی ب تێلەگرامێ ڤە بکە", "https://t.me/badinimatin")
st.write("---")

# ٥. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    
    # ڕێکخستنا بهایێ دهۆکێ (١٤٦،٧٥٠)
    dhok_rate = base_rate + 157.5
    
    st.metric(label="بهایێ ١ دۆلاری ل دهۆکێ (ئەڤڕۆ)", value=f"{dhok_rate:,.2f} IQD")
    
    st.write("---")
    
    # ٦. حاسیبە
    st.markdown("### 🧮 حاسیبەیێ بازارێ دهۆکێ")
    amount = st.number_input("چەند دۆلار تە هەنە؟", value=100.0, step=1.0)
    total_iqd = amount * dhok_rate
    st.success(f"بهایێ {amount:,} دۆلاران دبیتە: **{total_iqd:,.0f}** دینار")

except:
    st.error("کێشەک هەبوو د وەرگرتنا داتایان دا!")

st.info("تێبینی: هەر جارەکا تو 'Refresh' بکەی، دەمژمێر و بها دێ نوو بن.")
