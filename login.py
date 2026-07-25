import streamlit as st
import sqlite3
import hashlib

# ---------- Load CSS ----------
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css() 
import streamlit as st
import sqlite3
import hashlib

# -------------------------
# Database
# -------------------------
conn = sqlite3.connect("database/users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# -------------------------
# Password Hash
# -------------------------
def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------------------------
# Signup
# -------------------------
def signup(name, email, password):
    password = make_hash(password)
    try:
        c.execute(
            "INSERT INTO users(name,email,password) VALUES(?,?,?)",
            (name, email, password)
        )
        conn.commit()
        return True
    except:
        return False

# -------------------------
# Login
# -------------------------
def login(email, password):
    password = make_hash(password)

    c.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    return c.fetchone()

# -------------------------
# Login Page Function
# -------------------------
def login_page():

    st.title("🔐 AI Interview Login")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):

            result = login(email, password)

            if result:
                st.session_state.logged_in = True
                st.session_state.user = result[1]
                st.success(f"Welcome {result[1]} 🎉")
                st.rerun()

            else:
                st.error("Invalid Email or Password")

    with tab2:

        name = st.text_input("Full Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")
        confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")

        if st.button("Signup"):

            if password != confirm:
                st.error("Passwords do not match")

            elif signup(name, email, password):
                st.success("Account Created Successfully ✅")

            else:
                st.error("Email Already Exists")

                print("LOGIN FILE LOADED")
                print("login_page exists:", "login_page" in globals())
                print("AUTH LOADED")
