import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - مەتین", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک هەر 60 چرکەیان
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. سیستەمێ ژمارەکەرێ نهێنی
if 'total_visits' not in st.session_state:
    st.session_state.total_visits = 0
st.session_state.total_visits += 1

# --- پشکا پاسۆردێ (تنێ بۆ مەتینی) ---
with st.sidebar:
    st.title("🛠️ کۆنترۆلا مەتینی")
    # ل ڤێرە پاسۆردێ خۆ بنڤیسە دا ژمارێ ببینی
    pass_input = st.text_input("پاسۆردێ بنڤیسە:", type="password")
    
    if pass_input == "matin2026": 
        st.success("بەخێر بێی مەتین گیان")
        st.metric(label="👁️ ژمارا سەردانیکەران", value=st.session_state.total_visits)
    else:
        if pass_input != "":
            st.error("پاسۆرد خەلەتە!")
    st.write("---")
    st.info("ئەڤ بەشە تنێ مەتین دشێت پاسۆردێ لێ بدەت.")

# 4. ستایلێ گشتی
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%; height: 45px;
        border-radius: 10px; font-weight: bold; border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 5. وەرگرتنا بها
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd = 1470.0
    usd_to_try = 31.0
    usd_to_irr = 45000

# 6. دیزاینێ سەرەکی
st.markdown("""
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            دهۆک
        </span>
    </div>
    <div style="text-align: center; color: #00FF00; font-size: 18px; font-weight: bold;">
        زانینا بهایێ دراڤان ل دهۆک 🔄
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 7. حسابکرنا پارەی
currency_type = st.selectbox("دراڤەکێ هەلبژێرە:", ["دۆلار 💵", "لیرەیا تورکی 🇹🇷", "تمەنێ ئیرانی 🇮🇷"])
col1, col2 = st.columns([3, 1])
with col1:
    amount = st.number_input("بڕێ پارەی بنڤیسە:", min_value=0.0, value=100.0, label_visibility="collapsed")
with col2:
    if st.button("Enter"):
        pass

if "دۆلار" in currency_type:
    result = amount * usd_to_iqd
elif "لیرەیا تورکی" in currency_type:
    result = (amount / usd_to_try) * usd_to_iqd
else:
    result = (amount / usd_to_irr) * usd_to_iqd

st.markdown(f"""
    <div style="background-color: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center;">
        <h3 style="color: white; margin: 0;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00; font-size: 45px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #aaaaaa; margin: 0;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 8. پشکا ڕیکلامێ
st.write("")
st.markdown("""
    <div style="background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px dashed #FFD700; text-align: center;">
        <h4 style="color: #FFD700; margin: 0;">📢 جهێ ڕیکلاما تە ل ڤێرێ 📢</h4>
        <a href="https://t.me/badinimatin" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0088cc; color: white; border: none; padding: 8px 15px; border-radius: 8px; cursor: pointer; font-weight: bold; margin-top: 10px;">
                📩 پەیوەندی ب مە بکە
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)
