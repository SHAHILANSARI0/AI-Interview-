import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Interview Report",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Login Check
# -----------------------------
if not st.session_state.get("logged_in", False):
    st.warning("⚠ Please Login First")
    st.stop()

# -----------------------------
# Get Data
# -----------------------------
user = st.session_state.get("user", "User")
role = st.session_state.get("role", "Not Selected")
level = st.session_state.get("level", "Not Selected")
score = st.session_state.get("score", 0)

# -----------------------------
# Performance & Stars
# -----------------------------
if score >= 90:
    performance = "Excellent ⭐⭐⭐⭐⭐"
    recommendations = [
        "✔ Outstanding performance!",
        "✔ Keep practicing advanced interview questions.",
        "✔ Continue improving communication skills.",
        "✔ Apply for top companies.",
        "✔ Maintain your confidence."
    ]

elif score >= 80:
    performance = "Very Good ⭐⭐⭐⭐"
    recommendations = [
        "✔ Improve coding speed.",
        "✔ Practice DSA regularly.",
        "✔ Learn system design basics.",
        "✔ Improve communication.",
        "✔ Attend mock interviews."
    ]

elif score >= 70:
    performance = "Good ⭐⭐⭐"
    recommendations = [
        "✔ Practice coding daily.",
        "✔ Improve SQL knowledge.",
        "✔ Revise core concepts.",
        "✔ Improve confidence.",
        "✔ Attend mock interviews."
    ]

elif score >= 50:
    performance = "Average ⭐⭐"
    recommendations = [
        "✔ Learn DSA.",
        "✔ Improve communication.",
        "✔ Practice interview questions.",
        "✔ Build more projects.",
        "✔ Solve coding problems daily."
    ]

else:
    performance = "Needs Improvement ⭐"
    recommendations = [
        "✔ Learn programming basics.",
        "✔ Practice Python daily.",
        "✔ Improve communication skills.",
        "✔ Watch interview preparation videos.",
        "✔ Attend mock interviews regularly."
    ]

# -----------------------------
# Report UI
# -----------------------------
st.title("📄 AI Interview Report")

st.success(f"Candidate : {user}")

st.markdown("---")

st.write(f"### 👤 Candidate : {user}")
st.write(f"### 💼 Role : {role}")
st.write(f"### 🎯 Level : {level}")
st.write(f"### 📊 Score : {score}%")
st.write(f"### ⭐ Performance : {performance}")
st.write(f"### 📅 Date : {datetime.now().strftime('%d-%m-%Y %H:%M')}")

st.markdown("---")

st.subheader("💡 Recommendations")

for item in recommendations:
    st.write(item)

# -----------------------------
# Download Report
# -----------------------------
report = f"""
AI INTERVIEW REPORT

Candidate : {user}

Role : {role}

Level : {level}

Score : {score}%

Performance : {performance}

Generated On :
{datetime.now().strftime('%d-%m-%Y %H:%M')}
"""

st.download_button(
    "📥 Download Report",
    report,
    "AI_Interview_Report.txt",
    "text/plain",
    use_container_width=True
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")

with col2:
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
