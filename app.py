import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import pytz

# 1. ڕێکخستنا لاپەڕەی - نووکرنا سایتێ هەر ١ چرکە
st.set_page_config(page_title="بۆڕسا دهۆک لایڤ", page_icon="💵", layout="centered")
st_autorefresh(interval=1000, limit=None, key="live_updates") 

# 2. زمان و ژمارەکەر
if 'language' not in st.session_state: st.session_state.language = None
if 'count' not in st.session_state: st.session_state.count = 1760 
st.session_state.count += 1

# 3. لاپەڕێ هەلبژارتنا زمانی
if st.session_state.language is None:
    st.markdown("""<style> .stApp { background-color: #000; text-align: center; } h2, p { color: #bf953f !important; } 
    div.stButton > button { background-color: #1a1c23 !important; color: white !important; border: 1px solid #bf953f !important; border-radius: 10px; height: 50px; width: 100%; } </style>""", unsafe_allow_html=True)
    st.markdown("<h2>بۆڕسا دهۆک | Duhok Borsa</h2><p>زمانێ خۆ هەلبژێرە / اختر لغتك</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("کوردی ☀️"): st.session_state.language = "Kurdish"; st.rerun()
    with col2:
        if st.button("العربية 🇮🇶"): st.session_state.language = "Arabic"; st.rerun()
    st.stop()

# 4. وەرگێڕان
translations = {
    "Kurdish": {
        "title": "بۆڕسا دهۆک یا زیندی", "usd_live": "بهایێ دۆلاری یێ نوکە (١٠٠$)", 
        "news": "🔴 ئاگاداری: ئەڤ نرخە ئۆتۆماتیکی دگەل بازارێ دهۆک دهێتە گوهۆڕین",
        "usd_calc": "💵 حسابکەرا پارەی", "res": "ئەنجام ب دینار:", "btn": "حساب بکە"
    },
    "Arabic": {
        "title": "بورصة دهوك المباشرة", "usd_live": "سعر الدولار اللحظي (١٠٠$)", 
        "news": "🔴 تنبيه: هذا السعر يتغير تلقائياً مع سوق دهوك",
        "usd_calc": "💵 حاسبة العملات", "res": "النتيجة بالدينار:", "btn": "تحويل"
    }
}
t = translations[st.session_state.language]

# 5. ستایلێ گشتی
st.markdown(f"""
<style>
    header, footer {{ visibility: hidden; }}
    .stApp {{ background: #000; }}
    .card {{ background-color: rgba(20, 20, 20, 0.9); padding: 25px; border-radius: 15px; border: 2px solid #bf953f; text-align: center; margin-bottom: 15px; }}
    .live-price {{ color: #00FF00 !important; font-size: 60px !important; font-weight: bold; }}
    .live-time {{ font-size: 18px; color: #fcf6ba !important; margin-bottom: 20px; text-align: center; }}
</style>
""", unsafe_allow_html=True)

# 6. دەمێ زیندی
duhok_tz = pytz.timezone('Asia/Baghdad')
now = datetime.now(duhok_tz)
date_time = now.strftime("📅 %Y-%m-%d | ⏰ %H:%M:%S")

# 7. وەرگرتنا نرخێ بازارێ نوکە (Live API)
try:
    # ئەڤ لینکا ل خوارێ نرخێ ڕاستەقینە ددەت
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    # زێدەکرنا جیاوازیا بازارێ ناوخۆیی (بۆ نموونە ١٥٩.٥)
    rate = (data['rates']['IQD'] + 159.5) * 100
except:
    rate = 151750 # ئەگەر ئینتەرنێت نەبوو ئەڤە دیار بیت

# 8. شاشا سەرەکی
st.markdown(f"<h1>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown(f'<div class="live-time">{date_time}</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="card">
    <p>{t['usd_live']}</p>
    <h1 class="live-price">{rate:,.0f}</h1>
</div>
""", unsafe_allow_html=True)

# 9. حسابکەر
st.write("---")
usd_in = st.number_input("$ USD Amount:", min_value=0.0, value=100.0)
if st.button(t['btn']):
    res = usd_in * (rate / 100)
    st.success(f"{t['res']} {res:,.0f} IQD")

# 10. دوکما تێلەگرامی
st.markdown(f'<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; margin-top:10px;">✈️ کەنالێ تێلەگرامی</a>', unsafe_allow_html=True)
