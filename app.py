import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر (وەک د وێنەیێ تە دا 1760)
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایل بۆ لادانا نیشانا 🔗 و جوانکرنا واتسئاپێ
st.markdown("""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکێ سایتی */
    .stApp a.header-anchor { display: none !important; }
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stApp { background-color: #000; }
    h1, h2, h3, p, label { color: #bf953f !important; }

    /* ستایلێ دوکما واتسئاپێ */
    .whatsapp-btn {
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        margin-top: 25px;
        border: 1px solid #fff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ هەلبژارتنا زمان (وەک د وێنەیێ تە دا)
if st.session_state.language is None:
    st.markdown("<h2 style='text-align:center; color:#bf953f;'>Duhok Borsa | بۆڕسا ده
