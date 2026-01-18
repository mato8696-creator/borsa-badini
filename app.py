import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# 2. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5
except:
    dhok_rate = 1468.50

# 3. ناڤ ونیشانێ سایتێ تە
st.title("💰 بۆڕسا مەتین")
st.write("---")

# 4. خانەیا نڤیسینا دۆلاران
st.subheader("💵 بڕێ دۆلاران بنڤیسە:")
usd_input = st.number_input("", min_value=0.0, value=100.0, step=1.0, label_visibility="collapsed")

# 5. رێنمایێ ب کوردی ل بن خانەیێ
st.info("💡 ل سەر کیبۆردێ 'Done' یان 'Enter' لێ بدە دا ئەنجام دیار ببیت")

# 6. حسابکرنا پارەی
iqd_result = usd_input * dhok_rate

# 7. نیشاندانا ئەنجامی ب ڕەنگێ کەسک و ب شێوەیەکێ مەزن
st.write("---")
st.header("✅ زانینا بهایی ب دینار:")
st.subheader(f"💵 {usd_input:,.0f} دۆلار دبیتە:")
st.markdown(f":green[**{iqd_result:,.0
