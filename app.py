import streamlit as st
import requests
import os
from streamlit_autorefresh import st_autorefresh

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک - مەتین", page_icon="💰")

# 2. نووکرنا ئۆتۆماتیک هەر 60 چرکەیان
st_autorefresh(interval=60000, limit=100, key="fscounter")

# 3. فۆنکشن بۆ پاراستنا ژمارا سەردانیکەران د فایلەکێ دا (دا سفر نەبیت)
def get_total_visits():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    
    with open(file_path, "r") as f:
        try:
            count = int(f.read())
        except:
            count = 0
    
    count += 1
    with open(file_path, "w") as f:
        f.write(str(count))
    return count

# بانگکرنا ژمارەی تنێ ئێک جار
if 'total_visits_db' not in st.session_state:
    st.session_state.total_visits_db = get_total_visits()

# 4. پشکا پاسۆردێ د Sidebar دا
with st.sidebar:
    st.title("🛠️ کۆنترۆلا مەتینی")
    pass_input = st.text_input("پاسۆردێ بنڤیسە:", type="password")
    if pass_input == "matin2026": 
        st.success("بەخێر بێی مەتین")
        st.metric(label="👁️ ژمارا گشتی یا سەردانیکەران", value=st.session_state.total_visits_db)
    elif pass_input != "":
        st.error("پاسۆرد خەلەتە!")

# 5. ناڤ و نیشان و وەرگرتنا بها
st.markdown('<h1 style="text-align: center; color: #FFD700;">دهۆک</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #00FF00;">زانینا بهایێ دراڤان ل دهۆک 🔄</p>', unsafe_allow_html=True)

try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    usd_to_iqd = data['rates']['IQD'] + 158.5
except:
    usd_to_iqd = 1480.0

# 6. بەشێ حسابکرنا پارەی
amount = st.number_input("بڕێ دۆلاری بنڤیسە ($):", min_value=0.0, value=100.0)
result = amount * usd_to_iqd

st.markdown(f"""
    <div style="background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px solid #00FF00; text-align: center;">
        <h3 style="color: white;">ئەنجام ب دینار:</h3>
        <h1 style="color: #00FF00;">{result:,.0f}</h1>
        <p style="color: #aaaaaa;">مەتین عدنان</p>
    </div>
""", unsafe_allow_html=True)

# 7. پشکا ڕیکلامێ
st.write("---")
st.markdown("""
    <div style="background-color: #333; padding: 15px; border-radius: 10px; text-align: center;">
        <h4 style="color: #FFD700;">📢 جهێ ڕیکلاما تە ل ڤێرێ</h4>
        <a href="https://t.me/badinimatin" target="_blank" style="text-decoration: none; color: #0088cc;">پەیوەندیێ ب مە بکە</a>
    </div>
""", unsafe_allow_html=True)
