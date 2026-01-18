import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime
import pytz
import os

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="refresh_all")

# 2. سیستەمێ پاشکەفتکرنا بینەران د فایلەکێ دا
counter_file = "visitors.txt"

def get_visitors():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f: f.write("2064")
        return 2064
    with open(counter_file, "r") as f:
        return int(f.read())

def add_visitor():
    count = get_visitors() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

if 'counted' not in st.session_state:
    st.session_state.visitor_count = add_visitor()
    st.session_state.counted = True
else:
    st.session_state.visitor_count = get_visitors()

# 3. هەلبژارتنا زمانی
if 'lang' not in st.session_state: st.session_state.lang = None
if st.session_state.lang is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>بۆڕسا دهۆک</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.lang = "KU"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.lang = "AR"; st.rerun()
    st.stop()

# 4. وەرگێڕان و دیزاین
text = {
    "KU": {"u": "بهایێ دۆلاری (١٠٠$)", "c": "حسابکەرا پارەی", "v": "بینەرێن حەقیقی:", "btn": "حساب بکە", "owner": ":"},
    "AR": {"u": "سعر الدولار (١٠٠$)", "c": "حاسبة العملات", "v": "الزوار الحقيقيون:", "btn": "تحويل", "owner": "بإشراف:"}
}[st.session_state.lang]

dollar_img = "https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=2070"
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{ background-image: linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.88)), url("{dollar_img}"); background-size: cover; background-attachment: fixed; }}
    .owner-tag {{ color: #bf953f; font-weight: bold; font-size: 22px; text-align: center; margin-bottom: 10px; }}
    .price-card {{ background: rgba(30, 30, 30, 0.85); padding: 25px; border-radius: 20px; border: 2px solid #bf953f; text-align: center; }}
    h1 {{ color: #00FF00 !important; font-size: 55px !important; }}
    p, label, h3 {{ color: white !important; }}
</style>
""", unsafe_allow_html=True)

# 5. ناڤ و نرخ
st.markdown(f'<div class="owner-tag">{text["owner"]} Matin A. Muhammed</div>', unsafe_allow_html=True)

try:
    rate = (requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()['rates']['IQD'] + 160.5)
except:
    rate = 1471.5

now = datetime.now(pytz.timezone('Asia/Baghdad'))
st.markdown(f"<p style='color:#bf953f; text-align:center;'>⏰ {now.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

st.markdown(f'<div class="price-card"><p>{text["u"]}</p><h1>{rate*100:,.0f}</h1></div>', unsafe_allow_html=True)

# 6. حسابکەرا ١ دەقیقە
st.write("---")
usd_val = st.number_input("$ USD:", min_value=0.0, value=100.0)
if 'last_res' not in st.session_state: st.session_state.last_res = ""
if 'calc_time' not in st.session_state: st.session_state.calc_time = 0

if st.button(text['btn']):
    st.session_state.last_res = f"{usd_val:,.0f}$ = {usd_val * rate:,.0f} IQD"
    st.session_state.calc_time = time.time()

if st.session_state.last_res and (time.time() - st.session_state.calc_time < 60):
    st.success(st.session_state.last_res)
    st.caption(f"⏱️ {int(60 - (time.time() - st.session_state.calc_time))}")
elif st.session_state.last_res:
    st.session_state.last_res = ""

# 7. نیشاندانا بینەران (ئەوێن کو قەت ڕانەووەستن)
st.markdown(f"<div style='color:#bf953f; text-align:center; margin-top:30px; font-weight:bold; font-size:20px;'>👤 {text['v']} {st.session_state.visitor_count:,}</div>", unsafe_allow_html=True)
st.markdown(f'<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; margin-top:20px;">Telegram Channel</a>', unsafe_allow_html=True)
