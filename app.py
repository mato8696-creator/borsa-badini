import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# --- ئەڤە پشکا گرنگە بۆ ڕێکخستن دگەل بازاڕێ دهۆکێ ---
# ئەگەر بهایێ سایتی یێ نزم بوو، ڤێ ژمارێ زێدە بکە (بۆ نموونە بکە 160 یان 162)
# ئەگەر یێ بلند بوو، کێم بکە (بۆ نموونە بکە 155)
Duhok_Market_Fix = 158.5 
# --------------------------------------------------

if 'visits' not in st.session_state: st.session_state.visits = 30
st.session_state.visits += 1

# ستایل
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%; height: 50px; border-radius: 12px; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

translations = {
    "Kurdish": {"title": "بۆڕسا دهۆک", "curr": "دراڤەکێ هەلبژێرە:", "res": "ئەنجام ب دینار:", "tg_btn": "📩 تێلەگرام بۆ ڕیکلامێ"},
    "Arabic": {"title": "بورصة دهوك", "curr": "اختر العملة:", "res": "النتيجة بالدينار:", "tg_btn": "📩 تيليجرام للإعلان"},
    "English": {"title": "Duhok Exchange", "curr": "Select Currency:", "res": "Result in IQD:", "tg_btn": "📩 Telegram for Ads"}
}
lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)
t = translations[lang]

# Sidebar بۆ مەتینی
with st.sidebar:
    st.title("Admin")
    if st.text_input("Password:", type="password") == "matin2026":
        st.metric("Visitors", st.session_state.visits)
        st.write(f"Current Fix: {Duhok_Market_Fix}")

# وەرگرتنا بها و زێدەکرنا پارێ دهۆکێ
try:
    data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    # ل ڤێرێ بهایێ جیهانی دگەل ژمارا "دهۆکێ" کۆم دبیت
    iqd = data['rates']['IQD'] + Duhok_Market_Fix
    try_rate = data['rates']['TRY']
    irr_rate = data['rates']['IRR']
except:
    iqd, try_rate, irr_rate = 1485, 34, 55000

st.markdown(f"<h1 style='text-align:center; color:#FFD700;'>{t['title']}</h1>", unsafe_allow_html=True)

curr = st.selectbox(t['curr'], ["USD 💵", "TRY 🇹🇷", "IRR 🇮🇷"])
amt = st.number_input("", min_value=0.0, value=100.0)

if st.button("Enter"): pass

if "USD" in curr: res = amt * iqd
elif "TRY" in curr: res = (amt / try_rate) * iqd
else: res = (amt / irr_rate) * iqd

# نیشاندانا ئەنجامێ کۆتایی
st.success(f"{t['res']} {res:,.0f}")

st.write("---")
st.markdown(f"""
<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;">
    <div style="background-color:#0088cc; padding:15px; border-radius:10px; text-align:center; color:white; font-weight:bold;">
        {t['tg_btn']}
    </div>
</a>
""", unsafe_allow_html=True)
