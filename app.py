import streamlit as st
import requests

# رێکخستنا لاپەڕەی
st.set_page_config(page_title="Borsa", page_icon="💰")

# وەرگرتنا بها
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    dhok_rate = data['rates']['IQD'] + 158
except:
    dhok_rate = 1468

st.title("💰 Borsa Duhok")

# خانەیا نڤیسینێ
usd = st.number_input("Dollar بنڤیسە", min_value=0.0, value=100.0)

# حسابکرن
iqd = usd * dhok_rate

# ئەنجام ب ڕەنگێ کەسک
st.write("---")
st.subheader("Result (IQD):")
st.success(f"{iqd:,.0f} Dinars")

# لینکا تێلەگرامێ
st.write("---")
st.link_button("Telegram (Badini Matin)", "https://t.me/badinimatin")
