import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی (Page Config)
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر (وەک د وێنەیێ تە دا 1760)
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ زێڕین و لادانا نیشانا 🔗
bg_img = "https://images.unsplash.com/photo-1611974714658-058e11ee5d46?q=80&w=2070"
st.markdown(f"""
<style>
    /* لادانا نیشانا 🔗 ل هەمی جهەکی */
    .stApp a.header-anchor {{ display: none !important; }}
    header, #MainMenu, footer {{ visibility: hidden; }}

    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("{bg_img}");
        background-size: cover;
        background-position: center;
    }}
    
    h1, h2, h3, p, label {{ color: #fcf6ba !important; text-align: center; font-family: 'Arial'; }}
    
    .price-card {{
        background: rgba(30, 30, 30, 0.9);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #bf953f;
        margin-bottom: 20px;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.5);
    }}
    
    .wa-btn {{
        display: block;
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 15px;
        text-decoration: none;
        font-weight: bold;
        font-size: 20px;
        border: 1px solid #fff;
        margin-top: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# 4. لاپەڕێ زمانان (ب دوکمێن جوان)
if st.session_state.language is None:
    st.markdown("<br><h1 style='color:#bf953f;'>بۆڕسا دهۆک | Duhok Borsa</h1>", unsafe_allow_html=True)
    st.markdown("<p>زمانێ خۆ هەلبژێرە - Select Language</p>", unsafe_allow_html=True)
