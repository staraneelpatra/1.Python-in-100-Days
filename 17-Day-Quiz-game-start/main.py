from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

new_questions = []

for question in question_data:
    new_questions.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(new_questions)

while quiz.still_has_questions():
    quiz.next_question()