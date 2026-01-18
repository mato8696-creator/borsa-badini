import streamlit as st
import requests

st.set_page_config(page_title="بۆڕسا بادینی", page_icon="💰")

st.title("💰 بۆڕسا بادینی")
st.subheader("بهایێ دۆلاری ب شێوەیەکێ ڕاستەقینە")

# وەرگرتنا داتایان
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    iqd_rate = data['rates']['IQD']
    st.metric(label="بهایێ ١ دۆلاری ب دینارێ عیراقی", value=f"{iqd_rate:,} IQD")
except:
    st.error("کێشەیەک د ئینتەرنێتێ دا هەیە!")

st.info("ئەڤ سایتە ب زمانێ بادینی هاتییە دروستکرن بۆ خزمەتا هەوە.")
st.write("---")
st.markdown("### 👤 گەشەپێدەرێ بەرنامەی:")
st.success("مەتین عدنان محمد: د گەل هەوەیە")
st.write("---")
st.write("بو هەر پسیارەکا تە هەبیت لینکی تلیگرام مە بەردەستە ژ بو گفتو گویئ ")
st.link_button https://t.me/badinimatin
