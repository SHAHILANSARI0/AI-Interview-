import streamlit as st

st.markdown("""
<style>

/* CSS yaha paste kar */

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Login Check
# -----------------------------
if "logged_in" not in st.session_state:
    st.warning("⚠ Please Login First")
    st.stop()

# -----------------------------
# Get Score
# -----------------------------
score = st.session_state.get("score", 0)
user = st.session_state.get("user", "User")
st.markdown(f"""
<div class="main-box">

<h1 style="text-align:center;font-size:60px;">
📊 AI Interview Feedback
</h1>

<p style="text-align:center;font-size:22px;color:#bfbfbf;">
Performance Analysis Report
</p>

<br>

<div style="
background:rgba(255,255,255,.05);
padding:18px;
border-radius:15px;
font-size:24px;
border:1px solid #8B5CF6;
">

👤 Welcome <b style="color:#8B5CF6;">{user}</b>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Performance
# -----------------------------
if score>=90:

    st.markdown("""
    <div class="success">

    🌟 Excellent Performance

    </div>
    """,unsafe_allow_html=True)

elif score>=75:

    st.markdown("""
    <div class="warning">

    👍 Good Performance

    </div>
    """,unsafe_allow_html=True)

elif score>=50:

    st.markdown("""
    <div class="warning">

    🙂 Average Performance

    </div>
    """,unsafe_allow_html=True)

else:

    st.markdown("""
    <div class="danger">

    ❌ Needs Improvement

    </div>
    """,unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Skill Ratings
# -----------------------------
st.markdown("""
<div class="card">

<h2>📈 Skill Analysis</h2>

</div>
""",unsafe_allow_html=True)

communication = min(score + 5, 100)
technical = max(score - 5, 0)
confidence = score

st.write("Communication")
st.progress(communication / 100)

st.write("Technical Knowledge")
st.progress(technical / 100)

st.write("Confidence")
st.progress(confidence / 100)

st.markdown("---")

# -----------------------------
# Suggestions
# -----------------------------
st.markdown("""
<div class="card">

<h2>💡 Suggestions</h2>

</div>
""",unsafe_allow_html=True)

suggestions = [
    "✔ Practice Data Structures and Algorithms.",
    "✔ Improve Python programming skills.",
    "✔ Learn SQL queries and database concepts.",
    "✔ Work on communication skills.",
    "✔ Solve coding problems daily.",
    "✔ Practice mock interviews regularly."
]

for item in suggestions:
    st.write(item)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Back to Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")

with col2:
    if st.button("📄 Generate Report", use_container_width=True):
        st.switch_page("pages/report.py")
