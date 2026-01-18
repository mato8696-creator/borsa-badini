import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. سیستەمێ پاراستنێ (بۆ هەتا هەتایێ پشتی جارا ئێکێ)
# مە "sidebar" بکارئینا دا کو شاشا سەرەکی تێک نەچیت
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ئەگەر تە ڤیا کۆدی بگوهۆڕی، ئەڤ "1234" بگوهۆڕە
correct_password = "دهوک"
"کود مە تنی دی جیکەی دهوک"

if not st.session_state["authenticated"]:
    st.title("🔐 چوونەژوورێ بۆ بۆڕسا دهۆک")
    password_input = st.text_input("کۆدێ نهێنی لێ بدە:", type="password")
    if st.button("پەیوەست بوون"):
        if password_input == correct_password:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("کۆد خەلەتە!")
    st.stop()

# --- پشتی لێدانا کۆدی، ئەڤ بەشێ خوارێ دێ هەردەم یێ ڤەکری بیت ---

st.title("💰 بۆڕسا مەتین (دهۆک)")
st.success("سایتی ب سەرکەفتی کار کر")

try:
    # وەرگرتنا بهایێ دۆلاری
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    
    # ڕێکخستنا بهایی بۆ بازارێ دهۆکێ (١٤٦،٧٥٠)
    dhok_rate = base_rate + 157.5
    
    st.metric(label="بهایێ ١ دۆلاری (ئەڤڕۆ)", value=f"{dhok_rate:,.2f} IQD")
    
    st.write("---")
    st.markdown("### 🧮 حاسیبەیێ گوهۆڕینێ")
    amount = st.number_input("چەند دۆلار تە هەنە؟", value=100.0)
    total = amount * dhok_rate
    st.info(f"بهایێ {amount:,} دۆلاران دبیتە: **{total:,.0f}** دینار")
    
    st.write("---")
    st.link_button("✈️ ناردنا نامەیێ (Telegram)", "https://t.me/badinimatin")

except:
    st.error("کێشەک هەبوو!")
