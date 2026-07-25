from numpy import random
import streamlit as st

st.markdown("""
<style>

.stApp{
    background:#050505;
    color:white;
}

.main-card{
    background:#121212;
    border:1px solid rgba(139,92,246,.5);
    border-radius:25px;
    padding:35px;
    margin-bottom:25px;
    box-shadow:0 0 30px rgba(139,92,246,.25);
}

.question-card{
    background:#171717;
    border-radius:20px;
    border:1px solid #2b2b2b;
    padding:25px;
    margin-top:20px;
}

.question-card h2{
    color:white;
}

textarea{
    border-radius:15px !important;
    border:1px solid #8B5CF6 !important;
    background:#202020 !important;
    color:white !important;
}

.stProgress > div > div{
    background:linear-gradient(90deg,#8B5CF6,#2563EB);
}

.stButton>button{
    width:100%;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#8B5CF6,#2563EB);
    color:white;
    font-size:18px;
    font-weight:bold;
    padding:12px;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0 0 20px rgba(99,102,241,.5);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Login Check
# -----------------------------
if not st.session_state.get("logged_in", False):
    st.warning("⚠ Please Login First")
    st.stop()

# -----------------------------
# Questions
# -----------------------------
question_bank = {

    "Python Developer": [
        "What is Python?",
        "What is the difference between List and Tuple?",
        "Explain OOP in Python.",
        "What is a Lambda Function?",
        "What are Python Decorators?",
        "Explain Exception Handling.",
        "What is File Handling?",
        "What are Python Modules?",
        "What is Multithreading?",
        "Tell me about your Python project.",
        "What is PIP?",
        "Difference between Deep Copy and Shallow Copy?",
        "What is __name__ == '__main__'?",
        "Explain Dictionary in Python.",
        "What is List Comprehension?"
    ],

    "Java Developer": [
        "What is Java?",
        "Difference between JDK, JRE and JVM?",
        "Explain OOP concepts.",
        "What is Inheritance?",
        "What is Polymorphism?",
        "Difference between Interface and Abstract Class?",
        "Explain Exception Handling.",
        "What is Multithreading?",
        "What is JDBC?",
        "Tell me about your Java project.",
        "What is Spring Boot?",
        "What is Collection Framework?",
        "Difference between Array and ArrayList?",
        "What is Garbage Collection?",
        "What is Method Overloading?"
    ],

    "Web Developer": [
        "What is HTML?",
        "Difference between HTML and HTML5?",
        "What is CSS?",
        "Explain CSS Flexbox.",
        "What is Bootstrap?",
        "What is JavaScript?",
        "Difference between var, let and const?",
        "What is DOM?",
        "Difference between GET and POST?",
        "Tell me about your Web Development project.",
        "What is Responsive Design?",
        "What is React?",
        "What is Node.js?",
        "Explain REST API.",
        "What is JSON?"
    ],

    "Data Analyst": [
        "What is Data Analysis?",
        "What is Pandas?",
        "Difference between Series and DataFrame?",
        "Explain NumPy.",
        "What is Data Cleaning?",
        "Explain SQL JOIN.",
        "What is Power BI?",
        "Difference between Mean and Median?",
        "Explain Data Visualization.",
        "Tell me about your Data Analysis project.",
        "What is Excel Pivot Table?",
        "What is ETL?",
        "Difference between INNER and LEFT JOIN?",
        "What is Correlation?",
        "What is KPI?"
    ],

    "AI/ML Engineer": [
        "What is Artificial Intelligence?",
        "What is Machine Learning?",
        "Difference between AI and ML?",
        "Explain Supervised Learning.",
        "Explain Unsupervised Learning.",
        "What is Deep Learning?",
        "Difference between CNN and RNN?",
        "What is Overfitting?",
        "What is Train-Test Split?",
        "Tell me about your AI/ML project.",
        "What is TensorFlow?",
        "What is Scikit-learn?",
        "Explain Decision Tree.",
        "What is Random Forest?",
        "What is Neural Network?"
    ]        
    
}
import random

role = st.session_state.get("role", "Python Developer")

questions = random.sample(
    question_bank.get(role, question_bank["Python Developer"]),
    10
)


# -----------------------------
# Session State
# -----------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(questions)

# -----------------------------
# Header
# -----------------------------
progress = (st.session_state.current_question + 1)/len(questions)

st.markdown(f"""
<div class="main-card">

<h1 style="text-align:center;font-size:60px;">
🤖 AI Interview 
</h1>

<p style="text-align:center;font-size:22px;color:#bfbfbf;">
Practice • Improve • Get Your Dream Job 🚀
</p>

<br>

<div style="
padding:18px;
border:1px solid #8B5CF6;
border-radius:15px;
background:rgba(255,255,255,.04);
font-size:24px;
">

👋 Welcome Back,
<b style="color:#8B5CF6;">
{st.session_state.get("user","User")}
</b>

</div>

</div>
""", unsafe_allow_html=True)

st.progress(progress)

st.markdown(
f"""
<h2 style='text-align:center;'>
Question {st.session_state.current_question+1} of {len(questions)}
</h2>
""",
unsafe_allow_html=True)

# -----------------------------
# Current Question
# -----------------------------
question = questions[st.session_state.current_question]

st.markdown(f"""
<div class="question-card">

<h2>
💬 {question}
</h2>

</div>
""", unsafe_allow_html=True)

answer = st.text_area(
    "Write Your Answer",
    value=st.session_state.answers[st.session_state.current_question],
    height=180,
    key=f"answer_{st.session_state.current_question}"
)

st.session_state.answers[st.session_state.current_question] = answer

# -----------------------------
# Back & Next Buttons
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Back", use_container_width=True):
        if st.session_state.current_question > 0:
            st.session_state.current_question -= 1
            st.rerun()

with col2:
    if st.button("➡ Next", use_container_width=True):
        if answer.strip() == "":
            st.error("⚠ Please write your answer first.")
        elif st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.warning("⚠ This is the last question. Click Submit below.")

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Submit Button
# -----------------------------
if st.button("🚀 Submit Interview", use_container_width=True):

    if st.session_state.current_question != len(questions) - 1:
        st.warning("⚠ Please go to the last question before submitting.")
    else:

        answered = sum(
            1 for ans in st.session_state.answers
            if ans.strip() != ""
        )

        score = int((answered / len(questions)) * 100)

        st.session_state["score"] = score

        st.session_state.current_question = 0
        st.session_state.answers = [""] * len(questions)

        st.switch_page("pages/feedback.py")
