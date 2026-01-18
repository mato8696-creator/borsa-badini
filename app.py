import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستن
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. لاپەڕێ هەلبژارتنا زمان (وەک د وێنەیێ تە دا)
if st.session_state.language is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>Duhok Borsa | بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    if st.button("کوردی ☀️"): 
        st.session_state.language = "Kurdish"
        st.rerun()
    if st.button("العربية 🇮🇶"): 
        st.session_state.language = "Arabic"
        st.rerun()
    if st.button("English 🇺🇸"): 
        st.session_state.language = "English"
        st.rerun()
    st.stop()

# 4. وەرگێڕان
t = {
    "Kurdish": {"title": "بۆڕسا دهۆک", "usd": "بهایێ دۆلاری (١٠٠$)", "calc": "گوهۆڕینا دۆلاری", "res": "ئەنجام ب دینار:", "btn": "Enter"},
    "Arabic": {"title": "بورصة دهوك", "usd": "سعر الدولار (١٠٠$)", "calc": "تحويل الدولار", "res": "النتيجة بالدينار:", "btn": "Enter"},
    "English": {"title": "Duhok Borsa", "usd": "USD Rate (100$)", "calc": "USD Converter", "res": "Result in IQD:", "btn": "Enter"}
}[st.session_state.language]

# 5. ستایل
st.markdown("""<style> .stApp { background-color: #000; } h1, h2, h3, p, label { color: #bf953f !important; } 
div.stButton > button { background-color: #FF0000 !important; color: white !important; width: 100%; border-radius: 10px; } </style>""", unsafe_allow_html=True)

# 6. پشکا سپۆنسەری (بۆ پەیداکرنا پارەی)
st.markdown("""<div style="border: 2px solid #bf953f; padding: 15px; border-radius: 15px; text-align: center; margin-bottom: 20px;">
<p style="margin:0;">Sponsor / سپۆنسەر</p>
<h2 style="color: #fff !important; margin: 5px 0;">✨ ناڤێ کۆمپانیا تە ل ڤێرێ ✨</h2>
<p style="color: #00FF00;">📞 0750 XXX XXXX</p></div>""", unsafe_allow_html=True)

# 7. وەرگرتنا نرخ
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    one_usd = resp['rates']['IQD'] + 158.5
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1515, 151500

# 8. نیشاندانا نرخ
st.markdown(f"<h1 style='text-align:center;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"""<div style="background-color: #111; padding: 20px; border-radius: 15px; border: 1px solid #bf953f; text-align: center;">
<p>{t['usd']}</p><h1 style="color: #00FF00 !important;">{iqd_100:,.0f}</h1></div>""", unsafe_allow_html=True)

# 9. پشکا گوهۆڕینا دۆلاری (ئۆتۆماتیکی و Enter)
st.write("---")
st.markdown(f"<h3>{t['calc']}</h3>", unsafe_allow_html=True)
usd_input = st.number_input("$ USD:", min_value=0.0, value=100.0)
if st.button(t['btn']) or usd_input:
    res = usd_input * one_usd
    st.markdown(f"<h2 style='text-align:center; color:#00FF00;'>{res:,.0f} IQD</h2>", unsafe_allow_html=True)

# 10. Sidebar (بینەران)
with st.sidebar:
    st.write("### Matin Control")
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.metric("بینەرێن ئەڤڕۆ", st.session_state.count)
