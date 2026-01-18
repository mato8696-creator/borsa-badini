import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

st.title("💰 حاسیبەیێ دۆلارێ دهۆکێ")
st.write("---")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5 # نێزیکی ١٤٦،٨٥٠ بۆ ١٠٠$
except:
    dhok_rate = 1468.50 

# ٣. خانەیا نڤیسینێ (ئەوا تە دڤێت بکارھێنەر ب خۆ بنڤیسیت)
st.subheader("💵 بڕێ دۆلاران بنڤیسە:")

# من number_input بکارئینایە، چونکە ل سەر موبایلێ ئێکسەر کیبۆردێ ژماران ڤەدکەت
usd_amount = st.number_input(
    "ژمارەیەکێ لێرە بنڤیسە (بۆ نموونە: 34 یان 100)",
    min_value=0.0,
    value=100.0,
    step=1.0,
    format="%.f"
)

# ٤. حسابکرن و نیشاندانا ئەنجامی ب شێوەیەکێ مەزن
iqd_result = usd_amount * dhok_rate

st.write("---")
st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #00ff00; text-align: center;">
        <h2 style="color: white; margin: 0;">ئەنجام بۆ {usd_amount:,.0f} دۆلار:</h2>
        <h1 style="color: #00ff00; font-size: 50px; margin: 10px;">{iqd_result:,.0f}</h1>
        <h2 style="color: white; margin: 0;">دینارێن عیراقی</h2>
    </div>
    """, unsafe_allow_html=True)

# ٥. زانیاریێن گشتی
st.write("---")
st.metric("بهایێ بازارێ دهۆکێ (١٠٠$)", f"{dhok_rate * 100:,.0f} IQD")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
