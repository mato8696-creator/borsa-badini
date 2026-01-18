import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💵", layout="centered")
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 2. زمان و ژمارەکەر (وەک د وێنەیێ تە دا 1760)
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. ستایلێ ڕەش و لادانا نیشانێن زێدە و زێدەکرنا نیشانا 🔗 یا جوان
st.markdown("""
<style>
    /* لادانا ن
