import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="🌍", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. سیستەمێ زمانان
if 'language' not in st.session_state:
    st.session_state.language = None

# 3. ژمارەکەرێ نهێنی
if 'count' not in st.session_state:
    st.session_state.count = 1320 
st.session_state.count += 1

# 4. لاپەڕێ دەسپێکێ (زمان)
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
    st.markdown("<p>زمانێ خۆ هەلبژێرە | Select Language</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2:
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3:
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 5. وەرگێڕان
translations = {
    "Kurdish": {"title": "بۆڕسا دهۆک یا جیهانی", "gold_label": "بهایێ مسقاڵا زێڕی (٢١)", "gold_calc": "⚖️ کێشێ زێڕی (غرام):", "btn": "حساب بکە", "res": "ئەنجام ب دینار:"},
    "Arabic": {"title": "بورصة دهوك العالمية", "gold_label": "سعر مثقال الذهب (٢١)", "gold_calc": "⚖️ وزن الذهب (غرام):", "btn": "احسب", "res": "النتيجة بالدينار:"},
    "English": {"title": "Duhok Global Borsa", "gold_label": "Gold Price (21K)", "gold_calc": "⚖️ Gold Weight (Gram):", "btn": "Calculate", "res": "Result in IQD:"}
}
t = translations[st.session_state.language]

# 6. ستایلێ ڕەش و نڤیسینا زێڕین (Black & Gold Theme)
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    h1, h2, h3, p, label { color: #fcf6ba !important; } /* هەمی نڤیسین زێڕینن */
    
    /* ڕەشکرنا سایباری و زێڕینکرنا نڤیسینێن تێدا */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #bf953f;
    }
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #bf953f !important;
        font-weight: bold;
    }
    
    /* ست
