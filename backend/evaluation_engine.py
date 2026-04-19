from llm import ask_llm

def evaluate_answer(question, user_answer, correct_answer):
    prompt = f"""
    You are an expert Finance Tutor AI.

    Evaluate the student's answer.

    Question:
    {question}

    Student Answer:
    {user_answer}

    Correct Answer:
    {correct_answer}

    Return response in format:

    Result: Correct or Incorrect
    Explanation: Detailed explanation
    Learning Tip: Helpful concept tip
    """

    return ask_llm(prompt)