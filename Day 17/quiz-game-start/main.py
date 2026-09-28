
from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for things in question_data:
    question_text = things["text"]
    question_answer = things["answer"]
    new_questions = Questions(question_text, question_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was :{quiz.score}/{len(question_bank)}")
