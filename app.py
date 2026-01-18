import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا گشتی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. ژمارەکەر
if 'visits' not in st.session_state: st.session_state.visits = 60
st.session_state.visits += 1

# 3. ستایلێ ئەپلیکەیشنێ
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    .card {
        background-color: #1a1c23; padding: 20px;
        border-radius: 15px; border: 1px solid #30363d;
        text-align: center; margin-bottom: 15px;
    }
    .gold-result {
        background: linear-gradient(45deg, #bf953f, #fcf6ba, #aa771c);
        color: #1a1c23; padding: 15px; border-radius: 12px;
        font-weight: bold; text-align: center; margin-top: 10px;
    }
    div.stButton > button {
        background-color: #FF0000 !important;
        color: white !important; width: 100%; height: 50px;
        border-radius: 12px; font-weight: bold; border: none;
    }
</style>
""", unsafe_allow_html=True)

# 4. وەرگرتنا بها و ڕێکخستنا دهۆکێ
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    # 158.5 فەرەقا دهۆکێ یە
    usd_iqd = resp['rates']['IQD'] + 158.5
    usd_try = resp['rates']['TRY']
except:
    usd_iqd, usd_try = 1485, 34

# بهایێ تەخمینی یێ زێڕی ل دهۆکێ
mithqal_21 = 485000
gram_21 = mithqal_21 / 5

# 5. ناڤ و نیشان
st.markdown("<h1 style='text-align:center; color:#FFD700;'>Duhok Borsa</h1>", unsafe_allow_html=True)

# 6. پشکا زێڕی و حسابکرنا غرامان
st.markdown(f"""
<div class="card">
    <p style="color:#FFD700; margin:0;">بهایێ مسقاڵا زێڕی (عيار ٢١)</p>
    <h2 style="color:#00FF00; margin:5px;">{mithqal_21:,.0f} IQD</h2>
</div>
""", unsafe_allow_html=True)

st.write("⚖️ **کێشێ زێڕێ خۆ بنڤیسە (غرام):**")
input_gold = st.number_input("", min_value=0.0, value=26.0, step=1.0, key="gold_calc")
res_gold = input_gold * gram_21

st.markdown(f"""
<div class="gold-result">
    بهایێ {input_gold} غرامان: <br>
    <span style="font-size:22px;">{res_gold:,.0f} دینار</span>
</div>
""", unsafe_allow_html=True)

# 7. کالکۆلێتەرێ دۆلاری
st.write("---")
lang = st.radio("", ["Kurdish", "Arabic", "English"], horizontal=True)
curr = st.selectbox("دراڤی هەلبژێرە:", ["USD 💵", "TRY 🇹🇷"])

c1, c2 = st.columns([3, 1])
with c1:
    val = st.number_input("بڕێ پارەی:", min_value=0.0, value=100.0, label_visibility="collapsed")
with c2:
    if st.button("Enter"): pass

if "USD" in curr: final_res = val * usd_iqd
else: final_res = (val / usd_try) * usd_iqd

st.success(f"ئەنجام: {final_res:,.0f} دینار")

# 8. تێلەگرام
st.markdown(f"""
<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;">
    <div style="background-color:#0088cc; padding:12px; border-radius:10px; text-align:center; color:white; font-weight:bold;">
        📩 پەیوەندی ب مە بکە (Telegram)
    </div>
</a>
""", unsafe_allow_html=True)

# 9. Sidebar
with st.sidebar:
    if st.text_input("Password", type="password") == "matin2026":
        st.metric("Views", st.session_state.visits)
