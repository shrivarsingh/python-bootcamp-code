class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # Default value is zero
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ. {self.question_number}: {current_question.text}\n(True/False)> ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == "":
            print("That is incorrect.")
        elif user_answer[0].lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
