class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, answer):
        question = self.question_list[self.question_number - 1]
        
        if answer == question.answer:
            print(question.answer)
            print("Correct")
            self.score += 1
            return True
        else:
            print(question.answer)
            print("Wrong")
            return False
        
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number} {question.text} (True/False)")
        return users_answer

    def print_score(self):
        print(f"Your score is {self.score}")
