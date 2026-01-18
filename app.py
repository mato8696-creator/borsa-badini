import streamlit as st
import requests

# ١. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="بۆڕسا دهۆک", page_icon="💰")

# ٢. وەرگرتنا بهایێ دۆلاری
try:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    base_rate = data['rates']['IQD']
    dhok_rate = base_rate + 158.5
except:
    dhok_rate = 1468.50

st.title("💰 حاسیبەیێ ئۆتۆماتیک یێ دهۆکێ")
st.write(f"📊 بهایێ ١٠٠$ نوکە: **{dhok_rate * 100:,.0f}** دینار")
st.write("---")

# ٣. دروستکرنا خانەیا ئۆتۆماتیک ب HTML و JavaScript
# ئەڤ بەشە دێ وا کەت کو هەر ژمارەکا تو بنڤیسی، بێ Enter حساب بکەت
st.markdown(f"""
    <div style="direction: rtl; text-align: right; font-family: sans-serif;">
        <label style="font-size: 20px; font-weight: bold;">💵 بڕێ دۆلاران بنڤیسە:</label><br>
        <input type="number" id="usd_input" value="100" oninput="calculate()" 
            style="width: 100%; padding: 15px; font-size: 25px; border-radius: 10px; border: 2px solid #4CAF50; background-color: #f9f9f9;">
        
        <div style="margin-top: 30px; background-color: #1e1e1e; padding: 25px; border-radius: 15px; border: 2px solid #00ff00; text-align: center;">
            <h2 style="color: white; margin: 0;">ئەنجام ب دینار:</h2>
            <h1 id="iqd_result" style="color: #00ff00; font-size: 50px; margin: 10px;">{(100 * dhok_rate):,.0f}</h1>
            <h2 style="color: white; margin: 0;">دینارێن عیراقی</h2>
        </div>
    </div>

    <script>
    function calculate() {{
        var usd = document.getElementById('usd_input').value;
        var rate = {dhok_rate};
        var result = usd * rate;
        // ڕێکخستنا نیشاندانا ژمارەی ب فاریزە (وەکی 146,850)
        document.getElementById('iqd_result').innerHTML = result.toLocaleString('en-US', {{maximumFractionDigits: 0}});
    }}
    </script>
    """, unsafe_allow_html=True)

st.write("")
st.write("---")
st.markdown("### 👤 گەشەپێدەر: مەتین عدنان")
st.link_button("✈️ Telegram", "https://t.me/badinimatin")
