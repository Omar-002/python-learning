correct_answers = {
    "question1": "10",
    "question2": "python",
    "question3": "creates a function"
}

questions = {
    "question1": "What is 5 + 5? ",
    "question2": "What language are we learning? ",
    "question3": "What does def do in Python? "
}

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

score = 0

for key, question in questions.items():
    user_answer = input(question)
    if check_answer(user_answer, correct_answers[key]):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"You got {score} out of {len(questions)} correct!")
