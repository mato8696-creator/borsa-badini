import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر
if 'visits' not in st.session_state: st.session_state.visits = 35
st.session_state.visits += 1

# 3. ستایلێ ئەپلیکەیشن (Modern UI)
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    [data-testid="stMetricValue"] { font-size: 25px !important; color: #00FF00 !important; }
    .card {
        background-color: #1a1c23;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
        margin-bottom: 10px;
    }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important;
        width: 100%; height: 50px; border-radius: 12px; font-weight: bold; border: none;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا بها (دۆلار و زێڕ)
try:
    # بهایێ دراڤان
    curr_data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    iqd_rate = curr_data['rates']['IQD'] + 158.5 # ڕێکخستن بۆ دهۆکێ
    try_rate = curr_data['rates']['TRY']
    
    # حسابکرنا بهایێ زێڕی (نێزیکی بۆ دهۆکێ)
    # ئۆنسە / 31.1 * 21 عیار * بهایێ دۆلاری
    gold_per_gram_usd = 85 # بهایێ تەخمینی یێ گرامێ
    gold_21_duhok = (gold_per_gram_usd * iqd_rate) * 5 # مسقاڵ
except:
    iqd_rate, gold_21_duhok = 1480, 485000

# 5. ناڤ و نیشان
st.markdown("<h1 style='text-align:center; color:#FFD700; margin-bottom:0;'>Duhok Borsa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>بۆڕسا دهۆک یا زیندی</p>", unsafe_allow_html=True)

# 6. پشکا زێڕی (نوی)
st.markdown(f"""
<div class="card">
    <h4 style="color:#FFD700; margin:0;">بهایێ مسقاڵا زێڕی (عیار ٢١)</h4>
    <h2 style="color:#00FF00; margin:10px;">{gold_21_duhok:,.0f} IQD</h2>
</div>
""", unsafe_allow_html=True)

# 7. زمان
lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)

# 8. کالکۆلێتەر
st.write("---")
curr = st.selectbox("دراڤی هەلبژێرە:", ["USD 💵", "TRY 🇹🇷"])
amt = st.number_input("بڕێ پارەی:", min_value=0.0, value=100.0)

if "USD" in curr: res = amt * iqd_rate
else: res = (amt / try_rate) * iqd_rate

st.markdown(f"""
<div style="background-color:#238636; padding:15px; border-radius:10px; text-align:center;">
    <h3 style="color:white; margin:0;">{res:,.0f} دینار</h3>
</div>
""", unsafe_allow_html=True)

# 9. تێلەگرام
st.write("")
st.markdown(f"""
<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;">
    <div style="background-color:#0088cc; padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">
        📩 پەیوەندی ب مە بکە (Telegram)
    </div>
</a>
""", unsafe_allow_html=True)

# 10. Sidebar Admin
with st.sidebar:
    if st.text_input("Password", type="password") == "matin2026":
        st.metric("Views", st.session_state.visits)
