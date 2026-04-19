import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

# ---------- Page Config ----------
st.set_page_config(
    page_title="Finance AI Tutor Bot",
    layout="wide"
)

# ---------- Header ----------
st.title("📊 Finance AI Tutor Bot")
st.caption("Upload reports • Take quizzes • Learn with AI")

# ---------- Styling ----------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.quiz-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #1e1e1e;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Upload Section ----------
st.header("📄 Upload PDF Report")

uploaded_file = st.file_uploader("Choose PDF", type=["pdf"])

if uploaded_file:

    if st.button("🚀 Generate Quiz"):

        with st.spinner("Generating AI Quiz..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/upload-report",
                files=files
            )

            if response.status_code == 200:

                data = response.json()

            

                quiz_data = data.get("quiz", [])

                if quiz_data and isinstance(quiz_data, list):

                    st.session_state["quiz"] = quiz_data
                    st.success("Quiz Generated Successfully")

                else:
                    st.error("Quiz data is empty or invalid.")

            else:
                st.error("Backend API failed.")

# ---------- Quiz Section ----------
if "quiz" in st.session_state and st.session_state["quiz"]:

    st.header("🧠 AI Quiz")

    quiz = st.session_state["quiz"]

    for count, q in enumerate(quiz, start=1):

        st.markdown(f"## Question {count}")

        question_text = q["question"]
        options = q["options"]
        correct = q["answer"]

        st.write(question_text)

        selected = st.radio(
            f"Choose Answer {count}",
            options,
            key=f"q_{count}"
        )

        if st.button(f"Submit Q{count}", key=f"btn_{count}"):

            payload = {
                "question": question_text,
                "user_answer": selected,
                "correct_answer": correct
            }

            response = requests.post(
                f"{BACKEND_URL}/evaluate-answer",
                json=payload
            )

            if response.status_code == 200:
                st.success("Checked!")
                st.write(response.json()["feedback"])

            else:
                st.error("Evaluation failed.")

        st.markdown("---")