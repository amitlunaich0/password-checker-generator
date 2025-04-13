# app.py
import streamlit as st
from checker import check_password_strength
from generator import generate_password

st.set_page_config(page_title="Password Checker & Generator", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Checker & Generator")
st.markdown("Enter a password to check its strength or generate a secure one below.")

# Password Checker
st.header("🔍 Check Password Strength")
user_input = st.text_input("Enter your password", type="password")

if user_input:
    score, feedback = check_password_strength(user_input)
    st.progress(score * 20)
    st.success(f"Strength Score: {score}/5")
    if feedback:
        st.warning("Suggestions:")
        for tip in feedback:
            st.write(f"👉 {tip}")
    else:
        st.success("Your password is strong!")

# Password Generator
st.header("🛠️ Generate Strong Password")
length = st.slider("Select password length:", min_value=8, max_value=24, value=12)

if st.button("Generate Password"):
    new_password = generate_password(length)
    st.code(new_password, language="text")
st.sidebar.title("👨💻 Amit Lunaich")
