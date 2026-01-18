import streamlit as st
import requests
import os
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - مەتین", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. فۆنکشنێ ژمارەکەرێ جێگیر
def get_total_visits():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f:
        try: count = int(f.read())
        except: count = 0
    count += 1
    with open(file_path, "w") as f: f.write(str(count))
    return count

if 'total_visits_db' not in st.session_state:
    st.session_state.total_visits_db = get_total_visits()

# 4. زمانێن سایتی (لیستەکا وەرگێڕانێ)
translations = {
    "Kurdish": {
        "title": "دهۆک", "subtitle": "زانینا بهایێ دراڤان ل دهۆک 🔄",
        "select_lang": "زمانێ هەلبژێرە:", "select_curr": "دراڤەکێ هەلبژێرە:",
        "input_label": "بڕێ پارەی بنڤیسە:", "result_label": "ئەنجام ب دینار:",
        "ad_title": "📢 جهێ ڕیکلاما تە ل ڤێرێ 📢", "contact": "📩 پەیوەندی ب مە بکە"
    },
    "Arabic": {
        "title": "دهوك", "subtitle": "معرفة أسعار العملات في دهوك 🔄",
        "select_lang": "اختر اللغة:", "select_curr": "اختر العملة:",
        "input_label": "أدخل المبلغ:", "result_label": "النتيجة بالدينار:",
        "ad_title": "📢 مكان إعلانك هنا 📢", "contact": "📩 اتصل بنا"
    },
    "English": {
        "title": "Duhok", "subtitle": "Duhok Currency Exchange Rates 🔄",
        "select_lang": "Choose Language:", "select_curr": "Select Currency:",
        "input_label": "Enter Amount:", "result_label": "Result in IQD:",
        "ad_title": "📢 Your Ad Here 📢", "contact": "📩 Contact Us"
    }
}

# 5. هەلبژارتنا زمانی ل سەرێ سایتی
lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)
t = translations[lang]

# 6. ستایلێ CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; }}
    div.stButton > button {{
        background-color: #FF0000 !important; color: white !important;
        width: 100%; height: 45px; border-radius: 10px; font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# 7. پشکا نهێنی (Sidebar)
with st.sidebar:
    st.title("🛠️ Admin Control")
    pass_input = st.text_input("Password:", type="password")
    if pass_input == "matin2026":
        st.metric(label="Total Visitors", value=st.session_state.total_visits_db)

# 8. وەرگرتنا بها
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
    usd_to_try = data['rates']['TRY']
    usd_to_irr = data['rates']['IRR']
except:
    usd_to_iqd, usd_to_try, usd_to_irr = 1480.0, 32.0, 45000

# 9. دیزاینێ سەرەکی ب زمانێ هەلبژارتی
st.markdown(f"""
    <div style="text-align: center; font-weight: bold; font-size: 50px;">
        <span style="background: linear-gradient(to right, #FF0000 33%, #FFD700 33%, #FFD700 66%, #008000 66%); 
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{t['title']}</span>
    </div>
    <div style="text-align: center; color: #00FF00; font-size: 18px; font-weight: bold;">{t['subtitle']}</div>
""", unsafe_allow_html=True)

st.write("---")

# 10. حسابکرنا پارەی
currency_type = st.selectbox(t['select_curr'], ["USD 💵", "TRY 🇹🇷", "IRR 🇮🇷"])
amount = st.number_input(t['input_label'], min_value=0.0, value=100.0)

if "USD" in currency_type: result = amount * usd_to_iqd
elif "TRY" in currency_type: result = (amount / usd_to_try) * usd_to_iqd
else: result = (amount / usd_to_irr) * usd_to_iqd

# 11. نیشاندانا ئەنجامی
st.markdown(f"""
    <div style="background-color: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 15px; border: 2px solid #00FF00; text-align: center;">
        <h3 style="color: white; margin: 0;">{t['result_label']}</h3>
        <h1 style="color: #00FF00; font-size: 45px; margin: 10px;">{result:,.0f}</h1>
        <p style="color: #aaaaaa; margin: 0;">Matin Adnan</p>
    </div>
""", unsafe_allow_html=True)

# 12. ڕیکلام
st.write("")
st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px dashed #FFD700; text-align: center;">
        <h4 style="color: #FFD700; margin: 0;">{t['ad_title']}</h4>
        <a href="https://t.me/badinimatin" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0088cc !important; color: white !important; border: none; padding: 8px 15px; border-radius: 8px; margin-top: 10px; width: auto !important;">{t['contact']}</button>
        </a>
    </div>
""", unsafe_allow_html=True)
