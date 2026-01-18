import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="refresh_all")

# 2. مێمۆری
if 'lang' not in st.session_state: st.session_state.lang = None
if 'calc_time' not in st.session_state: st.session_state.calc_time = 0
if 'last_res' not in st.session_state: st.session_state.last_res = ""
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 2064

if 'counted' not in st.session_state:
    st.session_state.visitor_count += 1
    st.session_state.counted = True

# 3. هەلبژارتنا زمانی
if st.session_state.lang is None:
    st.markdown("<style>.stApp{background:#000;text-align:center;} h2{color:#bf953f;}</style>", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک</h2><p style='color:white;'>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.lang = "KU"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان
text = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "c": "حسابکەرا پارەی", "v": "بینەرێن حەقیقی:", "btn": "Enter", "owner": "ب سەرپەرشتیا:", "tele": "کەنالێ مە یێ تێلەگرامێ"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "c": "حاسبة العملات", "v": "الزوار الحقيقيون:", "btn": "تحويل", "owner": "بإشراف:", "tele": "قناتنا على التيليجرام"}
}[st.session_state.lang]

# 5. ستایلێ گشتی و وێنەیێ باکگراوەندی
dollar_img = "https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=2070"
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.88)), url("{dollar_img}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    .owner-tag {{ color: #bf953f; font-weight: bold; font-size: 22px; text-align: center; margin-bottom: 10px; text-shadow: 2px 2px 4px #000; }}
    .price-card {{ background: rgba(30, 30, 30, 0.85); padding: 25px; border-radius: 20px; border: 2px solid #bf953f; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
    h1 {{ color: #00FF00 !important; font-size: 55px !important; font-weight: bold; }}
    p, label, h3 {{ color: white !important; font-family: 'Arial'; }}
    
    /* ستایلێ دوکما تێلەگرامێ وەک کارتەکا دۆلاری */
    .tele-card {{
        display: block;
        background: rgba(0, 136, 204, 0.2);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 20px;
        border-radius: 15px;
        text-decoration: none;
        text-align: center;
        margin-top: 30px;
        transition: 0.3s;
    }}
    .tele-card:hover {{ background: rgba(0, 136, 204, 0.4); transform: translateY(-5px); }}
    .tele-text {{ color: #00ace
