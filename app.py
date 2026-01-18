import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="🌍", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. سیستەمێ هەلبژارتنا زمانی و ل بیر مانا وێ
if 'language' not in st.session_state:
    st.session_state.language = None

# 3. ژمارەکەرێ سەردانیکەران
if 'visits' not in st.session_state:
    st.session_state.visits = 1150 # دەسپێکەکا بلند بۆ متمانێ
st.session_state.visits += 1

# 4. لاپەڕێ دەسپێکێ (هەلبژارتنا زمانی)
if st.session_state.language is None:
    st.markdown("""
    <style>
        .stApp { background-color: #050505; text-align: center; }
        h2, p { color: white !important; }
        div.stButton > button { 
            background-color: #1a1c23 !important; color: white !important; 
            border: 1px solid #bf953f !important; border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2>", unsafe_allow_html=True)
    st.markdown("<p>زمانێ خۆ هەلبژێرە | اختر لغتك | Select Language</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2:
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3:
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    
    # نیشاندانا ژمارا سەردانیکەران ل ژێر زمانان
    st.markdown(f"<p style='margin-top:50px; color:#555 !important;'>👥 سەردانیکەر: {st.session_state.visits}</p>", unsafe_allow_html=True)
    st.stop()

# 5. وەرگێڕان
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا جیهانی", "gold_label": "بهایێ مسقاڵا زێڕی (عيار ٢١)", 
        "gold_calc": "⚖️ کێشێ زێڕی (غرام):", "gold_res": "بهایێ غرامان:",
        "conv_title": "کالکۆلێتەرێ دراڤان", "curr_label": "دراڤەکێ هەلبژێرە:", 
        "amt_label": "بڕێ پارەی:", "btn": "حساب بکە", "res_label": "ئەنجام ب دینار:",
        "visitors": "👥 ژمارا سەردانیکەران:", "global_rates": "🌍 بهایێ دۆلاری ل جیهانێ (١ دۆلار)"
    },
    "Arabic": {
        "title": "بورصة دهوك العالمية", "gold_label": "سعر مثقال الذهب (عيار ٢١)", 
        "gold_calc": "⚖️ وزن الذهب (غرام):", "gold_res": "سعر الغرامات:",
        "conv_title": "محول العملات", "curr_label": "اختر العملة:", 
        "amt_label": "المبلغ:", "btn": "احسب الآن", "res_label": "النتيجة بالدينار:",
        "visitors": "👥 عدد الزوار:", "global_rates": "🌍 أسعار الدولار عالمياً (١ دولار)"
    },
    "English": {
        "title": "Duhok Global Borsa", "gold_label": "Gold Price (21K Mithqal)", 
        "gold_calc": "⚖️ Gold Weight (Gram):", "gold_res": "Total Price:",
        "conv_title": "Currency Converter", "curr_label": "Select Currency:", 
        "amt_label": "Amount:", "btn": "Calculate", "res_label": "Result in IQD:",
        "visitors": "👥 Visitors Count:", "global_rates": "🌍 Global USD Rates (1 USD)"
    }
}
t = translations[st.session_state.language]

# 6. ستایلێ CSS (ڕەش و سپی و زێڕین)
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    h1, h2, h3, p, label { color: white !important; }
    .card { background-color: #1a1c23; padding: 15px; border-radius: 12px; border: 1px solid #bf953f; text-align: center; margin-bottom: 10px; }
    .gold-box { background: linear-gradient(45deg, #bf953f, #fcf6ba, #aa771c); color: #000 !important; padding: 12px; border-radius: 10px; font-weight: bold; text-align: center; }
    div.stButton > button { background: linear-gradient(45deg, #FF0000, #990000) !important; color: white !important; width: 100%; height: 45px; border-radius: 10px; font-weight: bold; border: none; }
    .global-card { background-color: #111; padding: 10px; border-radius: 8px; border-left: 4px solid #bf953f; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)

# 7. وەرگرتنا بها (Live Data)
try:
    data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd_rate = data['rates']['IQD'] + 158.5
    rates = data['rates']
    gold_mithqal = 488000
    gold_gram = gold_mithqal / 5
except:
    iqd_rate, rates, gold_mithqal, gold_gram = 1485, {}, 488000, 97600

# 8. ناڤ و نیشان و ژمارا سەردانیکەران
st.markdown(f"<h1 style='text-align:center; color:#bf953f;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>{t['visitors']} {st.session_state.visits}</p>", unsafe_allow_html=True)

# 9. پشکا زێڕی
st.markdown(f"""<div class="card"><p style="color:#bf953f !important; margin:0;">{t['gold_label']}</p><h2 style="color:#00FF00 !important; margin:5px;">{gold_mithqal:,.0f} IQD</h2></div>""", unsafe_allow_html=True)
gold_w = st.number_input(t['gold_calc'], min_value=0.0, value=26.0, step=1.0)
st.markdown(f"""<div class="gold-box">{t['gold_res']} {gold_w} غرام = {(gold_w * gold_gram):,.0f} IQD</div>""", unsafe_allow_html=True)

# 10. کالکۆلێتەرێ دراڤان
st.write("---")
st.markdown(f"<h3>{t['conv_title']}</h3>", unsafe_allow_html=True)
curr = st.selectbox(t['curr_label'], ["USD 💵", "TRY 🇹🇷", "EUR 🇪🇺", "IRR 🇮🇷"])
amt = st.number_input(t['amt_label'], min_value=0.0, value=100.0)
if st.button(t['btn']): pass

# حسابکرن
if "USD" in curr: res = amt * iqd_rate
elif "TRY" in curr: res = (amt / rates.get('TRY', 34)) * iqd_rate
elif "EUR" in curr: res = (amt / rates.get('EUR', 0.92)) * iqd_rate
else: res = (amt / rates.get('IRR', 60000)) * iqd_rate
st.success(f"{t['res_label']} {res:,.0f}")

# 11. بهایێ دۆلاری ل جیهانێ (ئەوا تە ڤیای زێدە بکەین)
st.write("---")
st.markdown(f"<h4>{t['global_rates']}</h4>", unsafe_allow_html=True)
global_list = {"EUR 🇪🇺": "EUR", "TRY 🇹🇷": "TRY", "GBP 🇬🇧": "GBP", "SAR 🇸🇦": "SAR", "AED 🇦🇪": "AED"}

for name, code in global_list.items():
    val = rates.get(code, 0)
    st.markdown(f"""<div class="global-card"><p style="margin:0; font-size:14px;">{name}: <span style="color:#00FF00;">{val:,.2f}</span></p></div>""", unsafe_allow_html=True)

# 12. تێلەگرام
st.write("")
st.markdown(f"""<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;"><div style="background-color:#0088cc; padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">Telegram</div></a>""", unsafe_allow_html=True)
