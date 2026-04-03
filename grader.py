def grade_answer(student_answer, correct_answer):
    if student_answer.lower() == correct_answer.lower():
        return {"score": 100, "feedback": "Correct"}
    return {"score": 60, "feedback": "Partially correct"}
