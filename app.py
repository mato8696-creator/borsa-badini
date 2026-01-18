import streamlit as st
import requests

st.set_page_config(page_title="بۆڕسا بادینی", page_icon="💰")

st.title("💰 بۆڕسا بادینی")
st.subheader("بهایێ دۆلاری و گوهۆڕینا دراڤی")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان محمد")
st.link_button("✈️ ناردنا نامەیێ ب تێلەگرامێ", "https://t.me/badinimatin")
st.write("---")

# وەرگرتنا داتایان
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    iqd_rate = data['rates']['IQD']
    
    # ١. نیشاندانا بهایێ ئەڤڕۆ
    st.metric(label="بهایێ ١ دۆلاری ب دینارێ عیراقی", value=f"{iqd_rate:,} IQD")
    
    st.write("---")
    
    # ٢. بەشێ حاسیبەیێ (Calculator)
    st.markdown("### 🧮 حاسیبەیێ گوهۆڕینێ")
    amount_usd = st.number_input("ژمارەیا دۆلاران بنڤیسە (بۆ نموونە: 100 یان 30):", min_value=1.0, value=100.0, step=1.0)
    
    # حسایکرنا ئەنجامی
    total_iqd = amount_usd * iqd_rate
    
    st.success(f"بهایێ {amount_usd:,} دۆلاران دبیتە: **{total_iqd:,.0f}** دینارێن عیراقی")

except:
    st.error("کێشەیەک د ئینتەرنێتێ دا هەیە!")

st.info("ئەڤ سایتە ب شێوەیەکێ ڕاستەقینە کار دکەت.")
