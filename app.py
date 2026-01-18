import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر (1760)
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و لادانا نیشانێن سیستمێ و زێدەکرنا نیشانا 🔗 یا جوان
st.markdown("""
<style>
    /* لادانا نیشانا 🔗 یا سیستمێ کو ل ڕەخ ناڤان دیار دبیت */
    .stApp a.header-anchor { display: none !important; }
    header, [data-testid="stHeader"], #MainMenu, footer { visibility: hidden; }
    
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #fcf6ba !important; text-align: center; }
    
    .card {
        background: rgba(20, 20, 20, 0.9);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #bf953f;
        margin-bottom: 20px;
    }
    
    /* دیزاینا نیشانا 🔗 یا مەتینی */
    .my-anchor {
        font-size: 45px;
        color: #bf953f;
        text-align: center;
        margin: 15px 0;
        text-shadow: 2px 2px 5px #bf953f;
    }
</style>
""", unsafe_allow_html=True)

# 4. شاشا سەرەکی
st.markdown("<h1>بۆڕسا دهۆک یا جیهانی</h1>", unsafe_allow_html=True)

# وێنەیێ دۆلاری ل سەر پاشخانەکا ڕەش
st.image("https://images.unsplash.com/photo-1518458028785-8fbcd101ebb9?q=80&w=1000", use_container_width=True)

# زێدەکرنا
