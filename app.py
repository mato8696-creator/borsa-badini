import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

st.title("💰 حاسیبەیێ بۆڕسا دهۆک")
st.write("---")

# ٢. وەرگرتنا بهایێ دۆلاری یێ نوکە
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    # ڕێکخستنا بهایێ بازارێ دهۆکێ (نێزیکی ١٤٦,٨٥٠ بۆ ١٠٠ دۆلاران)
    dhok_rate = base_rate + 158.5 
except:
    dhok_rate = 1468.50 

# ٣. بەشێ حاسیبەیێ (ئەوێ تە دڤێت)
st.subheader("💵 بڕێ دۆلاران بنڤیسە:")

# ل ڤێرە بکار‌هێنەر دشێت ب کەیفا خۆ هەر ژمارەکێ بنڤیسیت
usd_amount = st.number_input("", min_value=0.0, value=100.0, step=1.0, help="ل ڤێرە ژمارەیا دۆلاران بنڤیسە")

# ٤. حسابکرن و نیشاندانا ئەنجامی ب شێوەیەکێ جوان
iqd_result = usd_amount * dhok_rate

st.write("---")
st.markdown(f"### 🔘 ئەنجام بۆ {usd_amount:,} دۆلار:")
st.success(f"## {iqd_result:,.0f} دینارێن عیراقی")

# ٥. زانیاریێن زێدە
st.write("---")
col1, col2 = st.columns(2)
col1.metric("بهایێ ١ دۆلاری", f"{dhok_rate:,.2f}")
col2.metric("بهایێ ١٠٠ دۆلاری", f"{dhok_rate * 100:,.0f}")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ پەیوەندی ب تێلەگرامێ", "https://t.me/badinimatin")
