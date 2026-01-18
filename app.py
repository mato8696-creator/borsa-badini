import streamlit as st
import requests

st.set_page_config(page_title="بۆڕسا مەتین", page_icon="💰")

st.title("💰 بۆڕسا بادینی (ئۆتۆماتیک)")
st.subheader("بهایێ دۆلاری ل بازارێ ئازاد یێ عیراقێ")

st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان محمد")
st.link_button("✈️ ناردنا نامەیێ ب تێلەگرامێ", "https://t.me/badinimatin")
st.write("---")

# وەرگرتنا داتایان ژ سایتێ جیهانی یێ Google Finance یان یێ هاوشێوە
try:
    # ئەڤ لینکە بهایێ بازارێ ئازاد (نە یێ فەرمی) یێ عیراقێ نیشان ددەت
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    
    # د جیهانێ دا هندەک جاران بهایێ بازارێ ڕەش داتایێن جودا ددەت
    # ئەگەر بهایێ فەرمی ١٣١٠ بیت، ئەم دشێین ب شێوەیەکێ بیرکاری (Math) نێزیکی بازارێ خۆ بکەین
    # یان ژی داتایێن دروستتر وەربگرین
    iqd_rate = data['rates']['IQD']
    
    # نیشاندانا بهایێ ئۆتۆماتیک
    st.metric(label="بهایێ ١ دۆلاری (ئۆتۆماتیک)", value=f"{iqd_rate:,} IQD")
    
    st.write("---")
    
    # حاسیبەیێ ئۆتۆماتیک
    st.markdown("### 🧮 حاسیبەیێ گوهۆڕینێ")
    amount_usd = st.number_input("ژمارەیا دۆلاران بنڤیسە:", value=100.0)
    
    total_iqd = amount_usd * iqd_rate
    st.success(f"بهایێ {amount_usd:,} دۆلاران دبیتە: **{total_iqd:,.0f}** دینار")

except:
    st.error("کێشەیەک د ئینتەرنێتێ دا هەیە!")

st.info("ئەڤ بهایە ئۆتۆماتیک دهێتە نووکرن، لێ هندەک جاران ژ بازارێ کەفالی یێ عیراقێ جودایە.")
