import streamlit as st
import requests
from datetime import datetime
import pytz
import streamlit.components.v1 as components

# ١. ڕێکخستنا سەرەکی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. دروستکرنا دەمژمێرا زیندی (Live Clock) ب JavaScript
st.markdown("""
    <div id="clock-container" style="background-color: #1e1e1e; padding: 20px; border-radius: 15px; border: 2px solid #00ff00; text-align: center; box-shadow: 2px 2px 10px rgba(0,255,0,0.2); margin-bottom: 20px;">
        <h1 id="clock" style="color: #00ff00; margin: 0; font-family: 'Courier New', Courier, monospace; font-size: 45px;">00:00:00</h1>
        <p id="date" style="color: #cccccc; margin: 5px; font-size: 18px;"></p>
    </div>

    <script>
    function updateClock() {
        var now = new Date();
        var options = { timeZone: "Asia/Baghdad", hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
        var timeString = now.toLocaleTimeString("en-US", options);
        var dateString = now.toLocaleDateString("en-US", { year: 'numeric', month: 'long', day: 'numeric' });
        
        document.getElementById('clock').innerHTML = "⏰ " + timeString;
        document.getElementById('date').innerHTML = "📅 " + dateString;
    }
    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """, unsafe_allow_html=True)

# ٣. ناڤ و پەیوەندی
st.title("💰 بۆڕسا مەتین (دهۆک)")
st.markdown(f"### 👤 گەشەپێدەر: مەتین عدنان محمد")
st.link_button("✈️ پەیوەندی ب تێلەگرامێ ڤە بکە", "https://t.me/badinimatin")
st.write("---")

# ٤. وەرگرتنا بهایێ دۆلارى
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 157.5 # نێزیکی ١٤٦،٧٥٠
    
    st.metric(label="بهایێ ١ دۆلاری ل دهۆکێ", value=f"{dhok_rate:,.2f} IQD")
    
    st.write("---")
    st.markdown("### 🧮 حاسیبەیێ بازارێ دهۆکێ")
    amount = st.number_input("چەند دۆلار تە هەنە؟", value=100.0, step=1.0)
    total_iqd = amount * dhok_rate
    st.success(f"بهایێ {amount:,} دۆلاران دبیتە: **{total_iqd:,.0f}** دینار")

except:
    st.error("کێشەک هەبوو د وەرگرتنا داتایان دا!")
