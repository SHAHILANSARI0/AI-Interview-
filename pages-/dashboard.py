import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Login Check
# ---------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("⚠ Please Login First")
    st.stop()

user = st.session_state.get("user", "User")

# ---------------------------
# Hero Section
# ---------------------------
st.markdown(f"""
<div style="
background:linear-gradient(135deg,#090909,#161616);
padding:35px;
border-radius:25px;
border:1px solid #303030;
box-shadow:0px 0px 25px rgba(140,82,255,.25);
">

<h1 style="
text-align:center;
font-size:55px;
color:white;
margin-bottom:10px;">
🤖 AI Interview Dashboard
</h1>

<p style="
text-align:center;
font-size:20px;
color:#bdbdbd;">
Welcome back, <span style="color:#8b5cf6;"><b>{user}</b></span> 👋
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ===============================
# Statistics Cards
# ===============================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #8b5cf6;
text-align:center;
height:180px;
">
<h2>🎤 Interviews</h2>
<h1 style="color:#8b5cf6;">0</h1>
<p>Total Interviews</p>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #3b82f6;
text-align:center;
height:180px;
">
<h2>📊 Average Score</h2>
<h1 style="color:#3b82f6;">0%</h1>
<p>Performance</p>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #10b981;
text-align:center;
height:180px;
">
<h2>🏆 Best Score</h2>
<h1 style="color:#10b981;">0%</h1>
<p>Highest Score</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ===============================
# Interview Setup
# ===============================

left, right = st.columns([2,1])

with left:

    st.markdown("## 🎯 Start New Interview")

    role = st.selectbox(
        "Select Job Role",
        [
            "Python Developer",
            "Java Developer",
            "Data Analyst",
            "AI/ML Engineer",
            "Web Developer"
        ]
    )

    level = st.selectbox(
        "Interview Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    st.session_state.role = role
    st.session_state.level = level

    if st.button("🚀 Start Interview", use_container_width=True):
        st.switch_page("pages/interview.py")

with right:

    st.markdown("""
<div style="
background:#111;
padding:25px;
border-radius:20px;
border:1px solid #8b5cf6;
text-align:center;
height:300px;
">

<h2>👤 User</h2>

<br>

<h3>Logged In</h3>

<p style="color:#8b5cf6;font-size:22px;">
AI Interview Ready 🚀
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

if st.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.switch_page("app.py")
  
