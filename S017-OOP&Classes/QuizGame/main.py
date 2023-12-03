from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from opentdb_data import opentdb_question_data


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

for opentdb_question in opentdb_question_data:
    opentdb_question_text = opentdb_question["question"]
    opentdb_question_answer = opentdb_question["correct_answer"]
    new_question = Question(q_text=opentdb_question_text, q_answer=opentdb_question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(f"\nQUIZ: {len(quiz.question_list)} Questions.")
while quiz.still_has_questions():
    quiz.next_question()
print("\nYou've completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
print(f"Accuracy: {(quiz.score/len(quiz.question_list))*100:.2f}%")
