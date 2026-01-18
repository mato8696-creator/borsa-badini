import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="📊")

st.title("📊 بۆڕسا مەتین - هەنگاڤ ب هەنگاڤ")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 157.5 # بهایێ نێزیکی دهۆکێ (1467.50)
except:
    dhok_rate = 1467.50 

# ٣. هەنگاڤا ١: هەلبژارتنا جورێ کارەکێ
st.markdown("### ١. چ تە دڤێت بکەی؟")
choice = st.radio("", ["بینینا بهایێ گشتی", "حاسیبەیێ پارەی (دۆلار بۆ دینار)"], label_visibility="collapsed")

st.write("---")

# ٤. جێبەجێکرنا هەنگاڤا ٢
if choice == "بینینا بهایێ گشتی":
    st.subheader("بهایێ دۆلاری ل بازارێ دهۆکێ:")
    col1, col2 = st.columns(2)
    col1.metric("بهایێ ١ دۆلار", f"{dhok_rate:,.0f} IQD")
    col2.metric("بهایێ ١٠٠ دۆلار", f"{dhok_rate * 100:,.0f} IQD")

else:
    st.subheader("٢. بڕێ
