import streamlit as st
import re
st.set_page_config(page_title="Password Meter", page_icon="🔒", layout="centered", initial_sidebar_state="expanded")
st.title("Password Meter 🛡️")
st.markdown("This app evaluates the strength of your password.")
password = st.text_input("Enter your password", type="password")

feedback= []
score = 0
if password:
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        score += 1
    if re.search(r"\d", password) is None:
        feedback.append("Password should contain at least one digit.")
    else:
        score += 1
    if re.search(r"[A-Z]", password) is None:
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        score += 1
    if re.search(r"[a-z]", password) is None:
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        score += 1
    if re.search(r"[!@#$%^&*()_+]", password) is None:
        feedback.append("Password should contain at least one special character.")
    else:
        score += 1
    if score == 5:
        feedback.append("✔ Password is strong.")
    st.error("\n".join(feedback)) 
    st.write(f"Password strength: {score}/5")
    
    if feedback:
        st.markdown("### Tips to create a strong password:")
        for tip in feedback:
            st.write(f"- {tip}")