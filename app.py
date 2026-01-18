import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - مەتین", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. سیستەمێ ژمارەکەرێ سادە (دا کۆد پەک نەکەڤیت)
if 'total_visits' not in st.session_state:
    st.session_state.total_visits = 12 # دەسپێک ژ ١٢ کەسان
st.session_state.total_visits += 1

# 4. ستایلێ CSS (بۆ دوکما سۆر و ڕەنگان)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-weight: bold;
        border: none;
    }
    .main-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #00FF00;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 5. زمان و وەرگێڕان
translations = {
    "Kurdish": {
        "title": "دهۆک", "subtitle": "زانینا بهایێ دراڤان ل دهۆک 🔄",
        "select_curr": "دراڤەکێ هەلبژێرە:", "input_label": "بڕێ پارەی بنڤیسە:",
        "result_label": "ئەنجام ب دینار:", "ad_title": "📢 جهێ ڕیکلاما تە ل ڤێرێ 📢",
        "wa_btn": "📩 پەیوەندی ب مە بکە"
    },
    "Arabic": {
        "title": "دهوك", "subtitle": "معرفة أسعار العملات في دهوك 🔄",
        "select_curr": "اختر العملة:", "input_label": "أدخل المبلغ:",
        "result_label": "النتيجة بالدينار:", "ad_title": "📢 مكان إعلانك هنا 📢",
        "wa_btn": "📩 اتصل بنا"
    },
    "English": {
        "title": "Duhok", "subtitle": "Duhok Currency Exchange Rates 🔄",
        "select_curr": "Select Currency:", "input_label": "Enter Amount:",
        "result_label": "Result in IQD:", "ad_title": "📢 Your Ad Here 📢",
        "wa_btn": "📩 Contact Us"
    }
}

lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)
t = translations[lang]

# 6. پشکا نهێنی (Sidebar)
with st.sidebar:
    st.title("Admin")
    pass_input = st.text_input("Password:", type="password")
    if pass_input == "matin2026":
        st.metric(label="Visitors", value=st.session_state.total_visits)

# 7. وەرگرتنا بها
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd, usd_to_try, usd_to_irr = 1500.0, 34.0, 55000

# 8. ناڤ و نیشان
st.markdown(f"""
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000, #FFD700, #008000); 
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{t['title']}</span>
    </div>
    <p style="text-align: center; color: #00FF00; font-weight: bold;">{t['subtitle']}</p>
""", unsafe_allow_html=True)

# 9. کالکۆلێتەر
currency_type = st.selectbox(t['select_curr'], ["USD 💵", "TRY 🇹🇷", "IRR 🇮🇷"])
col1, col2 = st.columns([3, 1])
with col1:
    amount = st.number_input(t['input_label'], min_value=0.0, value=100.0, label_visibility="collapsed")
with col2:
    if st.button("Enter"):
        pass

if "USD" in currency_type: result = amount * usd_to_iqd
elif "TRY" in currency_type: result = (amount / usd_to_try) * usd_to_iqd
else: result = (amount / usd_to_irr) * usd_to_iqd

# 10. نیشاندانا ئەنجامی
st.markdown(f"""
