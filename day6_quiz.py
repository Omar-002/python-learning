Rule

Break your program into clear sections: data, logic, loop, output
Functions should do one job each
Keep score outside the loop so it doesn't reset
The final print belongs outside the loop so it runs once

Quiz (least efficient — no functions, no dictionary):
score = 0

answer1 = input("What is 5 + 5? ")
if answer1 == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer2 = input("What language are we learning? ")
if answer2.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer3 = input("What does def do in Python? ")
if answer3.lower() == "creates a function":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"You got {score} out of 3 correct!")


Quiz (most efficient — dictionary + function + loop):
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



