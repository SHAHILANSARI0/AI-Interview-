import streamlit as st
import login

st.set_page_config(
    page_title="AI Interview Preparation",
    page_icon="🤖",
    layout="wide"
)

# ---------- Load CSS ----------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------- Login ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login.login_page()
    st.stop()

user = st.session_state.get("user", "User")

# ---------- Hero ----------
st.markdown(f"""
<div style="
background:linear-gradient(135deg,#090909,#141414);
padding:45px;
border-radius:25px;
border:1px solid #2b2b2b;
box-shadow:0 0 30px rgba(139,92,246,.25);
">

<h1 style="font-size:60px;color:white;text-align:center;margin-bottom:10px;">
🤖 AI Interview Preparation
</h1>

<h3 style="text-align:center;color:#9ca3af;">
Practice • Improve • Get Your Dream Job 🚀
</h3>

<br>

<div style="
background:#101010;
padding:20px;
border-radius:15px;
border:1px solid #8b5cf6;
font-size:24px;
color:white;
">
👋 Welcome Back,
<span style="color:#8b5cf6;font-weight:bold;">
{user}
</span>
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------- Button ----------
col1,col2,col3=st.columns([1,2,1])

with col2:
    if st.button("🚀 Go To Dashboard"):
        st.switch_page("pages/dashboard.py")

st.write("")
st.write("")

# ---------- Cards ----------
c1,c2,c3=st.columns(3)

with c1:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #8b5cf6;
text-align:center;
height:230px;
">
<h2>🎤 Voice Interview</h2>
<p style="color:gray;">
Practice with Speech Recognition
</p>
</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #3b82f6;
text-align:center;
height:230px;
">
<h2>📷 Camera Interview</h2>
<p style="color:gray;">
Face Detection & Confidence
</p>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #10b981;
text-align:center;
height:230px;
">
<h2>📊 AI Feedback</h2>
<p style="color:gray;">
Get Detailed Performance Report
</p>
</div>
""",unsafe_allow_html=True)
