import streamlit as st
import subprocess
import sys

st.title("Login to Cyber Attack Prediction System")

# Dummy login credentials
USERNAME = "dark"
PASSWORD = "dark37"

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful! Launching Cyber Attack Prediction System...")
        
        # Launch Tkinter app as a separate Python process
        subprocess.Popen([sys.executable, "cyber_attack_gui.py"])
        
        st.info("GUI should open shortly...")
    else:
        st.error("Invalid username or password")
