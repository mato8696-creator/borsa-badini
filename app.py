import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. ژمارەکەرێ سادە
if 'visits' not in st.session_state:
    st.session_state.visits = 20
st.session_state.visits += 1

# 4. ستایلێ CSS
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

# 5. زمان و وەرگێڕان
translations = {
    "Kurdish": {"title": "دهۆک", "curr": "دراڤەکێ هەلبژێرە:", "res": "ئەنجام ب دینار:", "tg_btn": "📩 پەیوەندی ب مە بکە (تێلەگرام)"},
    "Arabic": {"title": "دهوك", "curr": "اختر العملة:", "res": "النتيجة بالدينار:", "tg_btn": "📩 اتصل بنا (تيليجرام)"},
    "English": {"title": "Duhok", "curr": "Select Currency:", "res": "Result in IQD:", "tg_btn": "📩 Contact Us (Telegram)"}
}
lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)
t = translations[lang]

# 6. پشکا Sidebar
with st.sidebar:
    st.title("Admin")
    pwd = st.text_input("Password:", type="password")
    if pwd == "matin2026":
        st.metric("Visitors", st.session_state.visits)

# 7. وەرگرتنا بها
try:
    data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd = data['rates']['IQD'] + 158.5
    try_rate = data['rates']['TRY']
    irr_rate = data['rates']['IRR']
except:
    iqd, try_rate, irr_rate = 1500, 34, 55000

# 8. ناڤ و نیشان
st.markdown(f"<h1 style='text-align:center; color:#FFD700;'>{t['title']}</h1>", unsafe_allow_html=True)

# 9. حسابکرن
curr = st.selectbox(t['curr'], ["USD 💵", "TRY 🇹🇷", "IRR 🇮🇷"])
amt = st.number_input("", min_value=0.0, value=100.0)

if st.button("Enter"):
    pass

if "USD" in curr: res = amt * iqd
elif "TRY" in curr: res = (amt / try_rate) * iqd
else: res = (amt / irr_rate) * iqd

# 10. نیشاندانا ئەنجامی
st.success(f"{t['res']} {res:,.0f}")

# 11. ڕیکلام و تێلەگرام (ل شوینا واتسئاپێ)
st.write("---")
st.markdown(f"""
<div style="background-color:#0088cc; padding:15px; border-radius:10px; text-align:center;">
    <a href="https://t.me/badinimatin" target="_blank" style="color:white; text-decoration:none; font-weight:bold; font-size:18px;">
        {t['tg_btn']}
    </div>
</a>
""", unsafe_allow_html=True)
