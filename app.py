import streamlit as st
import requests

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="📊")

st.title("📊 بۆڕسا مەتین - دهۆک")
st.write("---")

# 2. وەرگرتنا بهایێ نوو (ئەگەر ئینتەرنێت هەبیت)
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 157.5 
except:
    dhok_rate = 1468.50 

# 3. هەنگاڤا ئێکێ: هەلبژارتن
st.subheader("١. چ تە دڤێت بکەی؟")
choice = st.radio("", ["بینینا بهایێ گشتی", "حاسیبەیێ دۆلاری"], label_visibility="collapsed")

st.write("---")

# 4. جێبەجێکرنا بڕیارێ
if choice == "بینینا بهایێ گشتی":
    st.info(f"💵 بهایێ ١٠٠ دۆلاران نوکە: {dhok_rate * 100:,.0f} دینار")
    st.metric("بهایێ ١ دۆلاری", f"{dhok_rate:,.2f} IQD")

else:
    st.subheader("٢. بڕێ دۆلاران هەلبژێرە:")
    
    # بژارەیێن بلەز (٣٠، ٦٠، ١٠٠)
    option = st.selectbox("بڕی دەستنیشان بکە:", ["٣٠ دۆلار", "٦٠ دۆلار", "١٠٠ دۆلار", "بڕەکێ دی"])
    
    if option == "٣٠ دۆلار":
        usd_val = 30.0
    elif option == "٦٠ دۆلار":
        usd_val = 60.0
    elif option == "١٠٠ دۆلار":
        usd_val = 100.0
    else:
        usd_val = st.number_input("بڕێ دۆلاران بنڤیسە:", value=1.0)
    
    # نیشاندانا ئەنجامی
    result = usd_val * dhok_rate
    st.write("---")
    st.success(f"✅ ئەنجام: {usd_val:,} دۆلار دبیتە:")
    st.header(f"{result:,.0f} دینار")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
