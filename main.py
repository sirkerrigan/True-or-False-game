from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Your game has finished!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")