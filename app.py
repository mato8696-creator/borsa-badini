import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
# نووکرنا سایتێ هەر چرکە بۆ دەمژمێرێ
st_autorefresh(interval=1000, limit=None, key="fscounter")

# 2. پاراستنا ئەنجامی د 'session_state' دا دا زوو بەرزە نەبیت
if 'language' not in st.session_state: st.session_state.language = None
if 'calculation_result' not in st.session_state: st.session_state.calculation_result = None
if 'count' not in st.session_state: st.session_state.count = 1760 

st.session_state.count += 1

# 3. لاپەڕێ هەلبژارتنا زمانی
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2 { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; width: 100%; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک", "usd": "بهایێ دۆلاری (١٠٠$)", "calc": "💵 حسابکەرا پارەی", "res": "ئەنجام ب دینار:", "btn": "حساب بکە"},
    "Arabic": {"title": "بورصة دهوك", "usd": "سعر الدولار (١٠٠$)", "calc": "💵 حاسبة العملات", "res": "النتيجة بالدينار:", "btn": "تحويل"}
}[st.session_state.language]

# 5. ستایلێ گشتی
st.markdown("""
<style>
    header, footer { visibility: hidden; }
    .stApp { background: #000; }
    .card { background: rgba(20,20,20,0.9); padding:25px; border-radius:15px; border:2px solid #bf953f; text-align:center; margin-bottom:15px; }
    .price { color: #00FF00 !important; font-size: 55px !important; font-weight: bold; }
    .result-box { background: rgba(0,255,0,0.1); padding:20px; border-radius:12px; border:2px solid #00FF00; text-align:center; margin-top:15px; }
</style>
""", unsafe_allow_html=True)

# 6. دەمێ زیندی
now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>📅 {now.strftime('%Y-%m-%d')} | ⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

# 7. وەرگرتنا نرخ
try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 159.0) * 100
except:
    rate = 151500

st.markdown(f'<div class="card"><p style="color:white;">{t["usd"]}</p><h1 class="price">{rate:,.0f}</h1></div>', unsafe_allow_html=True)

# 8. حسابکەر (چارەسەرکرنا کێشا بەرزەبوونا ئەنجامی)
st.write("---")
st.markdown(f"<h3>{t['calc']}</h3>", unsafe_allow_html=True)
usd_input = st.number_input("$ USD:", min_value=0.0, value=100.0)

if st.button(t['btn']):
    st.session_state.calculation_result = usd_input * (rate / 100)

# نیشاندانا ئەنجامی ئەگەر یێ هەبیت (دێ ل سەر شاشێ مینیت)
if st.session_state.calculation_result:
    st.markdown(f"""
    <div class="result-box">
        <p style="color:white; margin:0;">{t['res']}</p>
        <h2 style="color:#00FF00; margin:0;">{st.session_state.calculation_result:,.0f} IQD</h2>
    </div>
    """, unsafe_allow_html=True)

# 9. تێلەگرام
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:20px;">✈️ کەنالێ تێلەگرامی</a>', unsafe_allow_html=True)
