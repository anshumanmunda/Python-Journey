"""
Creating a Trivia Game : Steps 

1. Store questions.
2. Store answers.
3. Randomly select questions.
4. Ask the user.
5. Check each answer.
6. Track the score.
7. Display the final score.

""" 


import random 


# List of questions and answers associated with it
questions = {
    "What is the capital of India?": "Delhi",
    "Which planet is known as the Red Planet?": "Mars",
    "Who developed Python?": "Guido Van Rossum",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which animal is known as the King of the Jungle?": "Lion",
    "What is the chemical symbol for gold?": "Au",
    "Which gas do humans need to breathe?": "Oxygen",
    "What is the largest ocean on Earth?": "Pacific",
    "Which country is famous for pyramids?": "Egypt",
    "What is the fastest land animal?": "Cheetah",
    "Which organ pumps blood in the human body?": "Heart",
    "What is the national bird of India?": "Peacock",
    "Which language is mainly used for web page structure?": "HTML",
    "What is H2O commonly called?": "Water",
    "Which planet is closest to the Sun?": "Mercury",
    "What is the largest mammal?": "Whale",
    "Which metal is liquid at room temperature?": "Mercury",
    "How many days are there in a week?": "Seven",
    "Which continent is India located in?": "Asia",
    "What is the opposite of cold?": "Hot"
}

def python_trivia_game():

  # create list of question
  questions_list = list( questions.keys() )


  total_questions = 5
  score = 0

  selected_questions = random.sample(questions_list, total_questions)
  for index, question in enumerate(selected_questions):
    print(f'{index + 1}. {question}')

    user_answer = input('Your answer: ').strip().lower()

    correct_answer = questions[question]

    if user_answer == correct_answer.lower():
      print('Correct ✅\n')
      score += 1
    else:
      print(f'Wrong ❌\nThe correct answer is : {correct_answer}\n')

  print(f'👾 Game Over\nYour Score = {score}/{total_questions}')   


python_trivia_game()