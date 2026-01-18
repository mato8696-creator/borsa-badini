import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1520
st.session_state.count += 1

# 3. لاپەڕێ دەسپێکێ
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with c2: 
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    with c3: 
        if st.button("English 🇺🇸"): st.session_state.language = "English"; st.rerun()
    st.stop()

# 4. وەرگێڕان
translations = {
    "Kurdish": {"title": "بۆڕسا دهۆک", "gold": "بهایێ زێڕی (٢١)", "calc": "کێشێ زێڕی (غرام):"},
    "Arabic": {"title": "بورصة دهوك", "gold": "سعر الذهب (٢١)", "calc": "وزن الذهب (غرام):"},
    "English": {"title": "Duhok Borsa", "gold": "Gold Price (21K)", "calc": "Gold Weight (Gram):"}
}
t = translations[st.session_state.language]

# 5. ستایلێ وێنەیێ دۆلاری ل پاشبنەمایێ (Background Image)
# ئەڤ لێنکە وێنەیەکێ دۆلاری یێ ڕەش و جوانە
bg_img = "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?q=80&w=2071&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    h1, h2, h3, p, label {{ color: #ffffff !important; text-shadow: 2px 2px 4px #000000; }}
    .card {{ 
        background-color: rgba(20, 20, 20, 0.9); 
        padding: 20px; border-radius: 15px; 
        border: 1px solid #bf953f; text-align: center; margin-bottom: 15px; 
    }}
    div.stButton > button {{ 
        background: linear-gradient(45deg, #bf953f, #aa771c) !important; 
        color: black !important; font-weight: bold; width: 100%; border-radius: 10px; 
    }}
    [data-testid="stSidebar"] {{ background-color: rgba(0,0,0,0.95) !important; border-right: 1px solid #bf953f; }}
</style>
""", unsafe_allow_html=True)

# 6. وەرگرتنا بها
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    gold_mithqal = 495000
    gold_gram = gold_mithqal / 5
except:
    gold_mithqal, gold_gram = 495000, 99000

# 7. ناڤ و نیشان
st.markdown(f"<h1 style='text-align:center; color:#bf953f !important;'>{t['title']}</h1>", unsafe_allow_html=True)

# 8. پشکا زێڕی
st.markdown(f"""<div class="card"><p style="margin:0; color:#bf953f !important;">{t['gold']}</p><h2 style="color:#00FF00 !important;">{gold_mithqal:,.0f} IQD</h2></div>""", unsafe_allow_html=True)
gold_w = st.number_input(t['calc'], min_value=0.0, value=26.0)
st.success(f"Total: {(gold_w * gold_gram):,.0f} IQD")

# 9. تێلەگرام
st.markdown(f"""<a href="https://t.me/badinimatin" target="_blank" style="text-decoration:none;"><div style="background-color:#0088cc; padding:10px; border-radius:10px; text-align:center; color:white; font-weight:bold;">Telegram</div></a>""", unsafe_allow_html=True)

# 10. پشکا نهێنی (Admin)
with st.sidebar:
    st.markdown("<h3 style='color:#bf953f;'>Control</h3>", unsafe_allow_html=True)
    pw = st.text_input("Password:", type="password")
    if pw == "matin2026":
        st.write(f"👥 بینەر: {st.session_state.count}")
