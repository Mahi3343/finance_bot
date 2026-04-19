from fastapi import FastAPI, UploadFile, File
from pdf_reader import extract_text
from quiz_engine import generate_quiz
from evaluation_engine import evaluate_answer
from pydantic import BaseModel
from vector_store import store_document, search_document
app = FastAPI()
class AnswerRequest(BaseModel):
    question: str
    user_answer: str
    correct_answer: str

@app.get("/")
def home():
    return {"message": "Finance AI Tutor Backend Running"}

@app.post("/upload-report")
async def upload_report(file: UploadFile = File(...)):
    text = extract_text(file)

    quiz = generate_quiz(text)

    return {
        "message": "Quiz generated successfully",
        "quiz": quiz
    }
@app.post("/evaluate-answer")
async def check_answer(data: AnswerRequest):
    result = evaluate_answer(
        data.question,
        data.user_answer,
        data.correct_answer
    )

    return {
        "message": "Evaluation completed",
        "feedback": result
    }