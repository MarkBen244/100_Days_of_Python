# 🧠 True/False Quiz

A Python command-line True/False quiz built using Object-Oriented Programming.

The project loads questions from a separate data file, converts them into `Question` objects, and uses a `QuizBrain` class to manage the quiz, answers, and score.

## About the Project

This project was created while learning the fundamentals of Object-Oriented Programming in Python.

The program separates the quiz into different components:

- `Question` objects store individual questions and answers.
- `QuizBrain` manages the quiz, tracks the current question, checks answers, and keeps score.
- `data.py` stores the quiz questions.
- `main.py` creates the question objects and runs the quiz.

## Features

- 12 True/False questions
- Interactive command-line quiz
- Automatic answer checking
- Live score tracking
- Final score display
- Questions stored separately from the main program
- Object-oriented quiz management

## Project Structure

```text
true-false-quiz/
├── main.py
├── data.py
├── question_model.py
└── quiz_brain.py
````

### `main.py`

Creates the question objects, builds the question bank, and runs the quiz.

### `data.py`

Contains the quiz questions and their correct answers.

### `question_model.py`

Contains the class used to represent individual quiz questions.

### `quiz_brain.py`

Contains the `QuizBrain` class, which controls the quiz and manages the player's score.

## How It Works

1. Questions are stored in `data.py`.
2. `main.py` loops through the question data.
3. Each question is converted into a `Question` object.
4. The objects are stored in a question bank.
5. `QuizBrain` manages the quiz.
6. The user answers each question.
7. The program checks the answer and updates the score.
8. The final score is displayed when all questions have been answered.

## Example

```text
Q.1: A slug's blood is green. (True/False): True
You got it right
Your score is 1/1

Q.2: The loudest animal is the African Elephant. (True/False): False
You got it right
Your score is 2/2
```

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

No external Python packages are required.

## What I Learned

* Classes
* Objects
* Constructors
* Instance attributes
* Methods
* Object interaction
* Multiple Python modules
* Importing classes
* Lists of objects
* `for` loops
* `while` loops
* Conditional statements
* User input
* Basic program state management

## Future Improvements

* Add more questions
* Randomize the question order
* Add multiple-choice questions
* Improve input validation
* Add different difficulty levels
* Add automated tests

## Author

**Mark Bernard**

