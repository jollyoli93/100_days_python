from question_model import Question
from quiz_brain import  QuizBrain
from data import question_data

question_bank = []

for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

quiz = QuizBrain(question_bank)


# user_question = quiz.next_question()

while quiz.still_has_questions():
    question = quiz.next_question()
    quiz.check_answer(question)
    quiz.print_score()
