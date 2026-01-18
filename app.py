import streamlit as st
import requests
from datetime import datetime
import pytz # بۆ ڕێکخستنا دەمێ کوردستانێ

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - پاراستی", page_icon="🔐")

# ٢. وەرگرتنا دەمێ دروست یێ کوردستانێ
iq_timezone = pytz.timezone('Asia/Baghdad')
now = datetime.now(iq_timezone)
# کۆد بو داخاز کرنی سەرەدانا تلیکرام بکە (بۆ نموونە: 0520)
dynamic_password = now.strftime("%I%M") 

# ٣. سیستەمێ پشکنینا کۆدی
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == dynamic_password:
        st.session_state["authenticated"] = True
    else:
        st.error(f"❌ کۆد خەلەتە! کۆدێ ڤێ خولەکێ بکاربینە.")

# شاشا چوونەژوورێ (Login Screen)
if not st.session_state["authenticated"]:
    st.title("🔐 سیستەمێ پاراستنا مەتین")
    st.write(f"⏰ دەمێ نوکە ل دهۆکێ: {now.strftime('%I:%M %p')}")
    
    st.text_input("کۆدێ نهێنی (بو دیتنا کودی سەرەدانا تلیگرام بکە) بنڤیسە:", type="password", key="password_input")
    st.button("چوونەژوورێ", on_click=check_password)
st.write("---")
    st.link_button("✈️ Telegram", "https://t.me/badinimatin")    
    
    st.warning("تێبینی: ئەڤ کۆدە هەر خولەکەکێ دگوڕیت. پشتی تو دچیە ژوور، کەس نەشێت کۆدێ تە بکارببیت.")
    st.stop()

# --- ل ڤێرە پڕۆژەیێ تە یێ سەرەکی دەستپێدەکەت ---
st.title("💰 بۆڕسا  (دهۆک)")
st.success("تە ب سەرکەفتی کۆدێ درست لێدا!")

try:
    # وەرگرتنا بهایی و زێدەکرنا فەرقییا دهۆکێ
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 157.5 # دا نێزیکی ١٤٦،٧٥٠ بیت
    
    st.metric(label="بهایێ ١ دۆلاری ل دهۆکێ", value=f"{dhok_rate:,.2f} IQD")
    
    st.write("---")
    st.markdown("### 🧮 حاسیبەیێ بازارێ دهۆکێ")
    amount = st.number_input("چەند دۆلار تە هەنە؟", value=100.0)
    total = amount * dhok_rate
    st.info(f"بهایێ {amount:,} دۆلاران دبیتە: {total:,.0f} دینار")
    
    st.write("---")
    st.link_button("✈️ Telegram", "https://t.me/badinimatin")

except:
    st.error("کێشەک د ئینتەرنێتێ دا هەیە!")
