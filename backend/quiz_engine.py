import json
import re
from llm import ask_llm

def generate_quiz(text):
    prompt = f"""
Create 5 MCQ questions from document.

Return ONLY JSON array:
[
 {{
   "question":"...",
   "options":["A","B","C","D"],
   "answer":"..."
 }}
]

{text}
"""

    response = ask_llm(prompt)

    try:
        clean = re.search(r'\[.*\]', response, re.S).group()
        return json.loads(clean)
    except:
        return []