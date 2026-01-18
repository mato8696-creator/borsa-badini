import streamlit as st
import pandas as pd

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="Matin Store", page_icon="👕", layout="wide")

# 2. لیستەیا کەلوپەلان (تو دشێی ئەڤان بگوهۆڕی)
products = [
    {"id": 1, "name": "پێلاڤا Nike", "price": 45000, "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
    {"name": "قەمیسێ نوی", "price": 25000, "img": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400"},
    {"name": "پانتۆڵێ جینز", "price": 30000, "img": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400"}
]

# 3. دیزاینا سەرەکی
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Matin Online Store 🛍️</h1>", unsafe_allow_html=True)
st.write("---")

# 4. نیشاندانا کەلوپەلان ب شێوازێ کارت (Cards)
cols = st.columns(3)
for i, item in enumerate(products):
    with cols[i]:
        st.image(item['img'], use_container_width=True)
        st.subheader(item['name'])
        st.write(f"**نرخ: {item['price']:,} دینار**")
        if st.button(f"تەلەب بکە - Order", key=f"btn_{i}"):
            st.session_state.selected = item['name']
            st.success(f"تە {item['name']} هەلبژارد")

# 5. فۆرمێ کڕینێ (Order Form)
st.write("---")
st.header("📝 زانیاریێن خۆ بنڤیسە بۆ تەلەبکرنێ")
with st.form("my_form"):
    cust_name = st.text_input("ناڤێ سێ یانی:")
    cust_phone = st.text_input("ژمارا تەلەفۆنێ:")
    cust_address = st.text_input("ناڤنیشان (باژێر/گەڕەک):")
    submit = st.form_submit_button("ناردنا تەلەبێ 🚀")
    
    if submit:
        if cust_name and cust_phone:
            st.balloons()
            st.success("دەست خوش! تەلەبا تە گەهشتە مە. دێ پەیوەندیێ ب تە کەین.")
            # ل ڤێرێ تو دشێی زانیاریان پاشکەفت بکەی
