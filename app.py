import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="🌍", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. سیستەمێ ل بیر مانا زمانێ هەلبژارتی
if 'language' not in st.session_state:
    st.session_state.language = None

# 3. لاپەڕێ هەلبژارتنا زمانی ب ڕەنگێ گەش
if st.session_state.language is None:
    st.markdown("""
    <style>
        .stApp { background-color: #050505; }
        h2, p { color: white !important; text-align: center; }
        div.stButton > button { 
            background-color: #333 !important; 
            color: white !important; 
            border: 1px solid #bf953f !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2>", unsafe_allow_html=True)
    st.markdown("<p>زمانێ خۆ هەلبژێرە | اختر لغتك | Select Language</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("کوردی ☀️"):
            st.session_state.language = "Kurdish"; st.rerun()
    with col2:
        if st.button("العربية 🇮🇶"):
            st.session_state.language = "Arabic"; st.rerun()
    with col3:
        if st.button("English 🇺🇸"):
            st.session_state.language = "English"; st.rerun()
    st.stop()

# 4. وەرگێڕان
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", "gold_label": "بهایێ مسقاڵا زێڕی (عیار ٢١)", 
        "gold_calc": "⚖️ کێشێ زێڕی ب غرام:", "gold_res": "بهایێ غرامان:",
        "conv_title": "کالکۆلێتەرێ دراڤان", "curr_label": "دراڤەکێ هەلبژێرە:", 
        "amt_label": "بڕێ پارەی:", "btn": "حساب بکە", "res_label": "ئەنجام ب دینار:", "change_lang": "گوهۆڕینا زمانی"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", "gold_label": "سعر مثقال الذهب (عيار ٢١)", 
        "gold_calc": "⚖️ وزن الذهب (غرام):", "gold_res": "سعر الغرامات:",
        "conv_title": "محول العملات", "curr_label": "اختر العملة:", 
        "amt_label": "المبلغ:", "btn": "احسب الآن", "res_label": "النتيجة بالدينار:", "change_lang": "تغيير اللغة"
    },
    "English": {
        "title": "Duhok Global Borsa", "gold_label": "Gold Price (21K Mithqal)", 
        "gold_calc": "⚖️ Gold Weight (Gram):", "gold_res": "Total Price:",
        "conv_title": "Currency Converter", "curr_label": "Select Currency:", 
        "amt_label": "Amount:", "btn": "Calculate", "res_label": "Result in IQD:", "change_lang": "Change Language"
    }
}
t = translations[st.session_state.language]

# 5. ستایلێ UI (ڕاستکرنا ڕەنگی)
st.markdown("""
<style>
    /* ڕەنگێ پاشبنەمایێ ڕەش */
    .stApp { background-color: #050505; }
    
    /* سپی کردنا هەمی نڤیسینان */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stSelectbox label {
        color: white !important;
    }
    
    /* ستایلێ کارتێ */
    .card { 
        background-color: #1a1c23; padding: 20px; border-radius: 15px; 
        border: 1px solid #bf953f; text-align: center; margin-bottom: 15px; 
    }
    
    /* ڕەنگێ ئەنجامێ زێڕی */
    .gold-box { 
        background: linear-gradient(45deg, #bf953f, #fcf6ba, #aa771c); 
        color: #000 !important; padding: 15px; border-radius: 12px; 
        font-weight: bold; text-align: center; 
    }

    /* سپی کردنا نڤیسینا ناڤ "Input" و "Selectbox" */
    input, select, .stSelectbox div {
        color: white !important;
        background-color: #262730 !important;
    }

    /* دوکما سۆر */
    div.stButton > button { 
        background: linear-gradient(45deg, #FF0000, #990000) !important; 
        color: white !important; width: 100%; height: 50px; 
        border-radius: 12px; font-weight: bold; border: none; 
    }
</style>
""", unsafe_allow_html=True)

# 6. وەرگرتنا بها
try:
    data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd_rate = data['rates']['IQD'] + 158.5
    try_rate = data['rates']['TRY']
    gold_mithqal = 488000
    gold_gram = gold_mithqal / 5
except:
    iqd_rate, try_rate, gold_mithqal, gold_gram = 1485, 34, 488000, 97600

# 7. ناڤ و نیشان
st.markdown(f"<h1 style='text-align:center; color:#bf953f;'>{t['title']}</h1>", unsafe_allow_html=True)

# 8. پشکا زێڕی
st.markdown(f"""<div class="card"><p style="color:#bf953f !important; margin:0;">{t['gold_label']}</p><h2 style="color:#00FF00 !important; margin:10px;">{gold_mithqal:,.0f} IQD</h2></div>""", unsafe_allow_html=True)

st.write(f"**{t['gold_calc']}**")
gold_w = st.number_input("", min_value=0.0, value=26.0, step=1.0, key="gold_inp", label_visibility="collapsed")
total_g = gold_w * gold_gram
st.markdown(f"""<div class="gold-box">{t['gold_res']} {gold_w} غرام<br><span style="font-size:22px;">{total_g:,.0f} IQD</span></div>""", unsafe_allow_html=True)

# 9. کالکۆلێتەرێ دراڤان
st.write("---")
st.markdown(f"<h3>{t['conv_title']}</h3>", unsafe_allow_html=True)
curr = st.selectbox(t['curr_label'], ["USD 💵", "TRY 🇹🇷"])
amt = st.number_input(t['amt_label'], min_value=0.0, value=100.0)

if st.button(t['btn']): pass

if "USD" in curr: res = amt * iqd_rate
else: res = (amt / try_rate) * iqd_rate

st.success(f"{t['res_label']} {res:,.0f}")

# 10. بنێ سایتی
st.write("---")
c1, c2 = st.columns(2)
with c1:
    if st.button(t['change_lang']):
        st.session_state.language = None; st.rerun()
with c2:
    st.markdown(f"""<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;"><div style="background-color:#0088cc; padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">Telegram</div></a>""", unsafe_allow_html=True)
