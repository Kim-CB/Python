from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Write a loop to iterate over the question_data
# Create a Question object from each entry in question data
# Append each Question object to the question bank
question_bank = []

for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")