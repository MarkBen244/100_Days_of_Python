# 🐍 Snake Game

## About the Project

Snake Game is a classic arcade-style game built with Python's `turtle` graphics module.

The player controls a growing snake using the arrow keys. The goal is to eat the food, increase the score, and avoid hitting the walls or the snake's own body.

This project was built to practice Object-Oriented Programming, working with multiple Python modules, object interaction, and event-driven controls.

## Features

* 🐍 Controllable snake
* 🍎 Randomly positioned food
* 📈 Score tracking
* 🧱 Wall collision detection
* 💥 Self-collision detection
* ⬆️⬇️⬅️➡️ Arrow-key controls
* 📏 Snake grows after eating food
* 🏆 Game-over detection
* 🖥️ Graphical interface using Turtle

## How It Works

### Snake

The `Snake` class manages the snake's body, movement, growth, and direction.

The snake starts with three segments and adds a new segment whenever it eats food.

### Food

The `Food` class creates the red food object and randomly places it on the game screen.

### Scoreboard

The `Scoreboard` class keeps track of the player's score and displays it on the screen. It also displays the game-over message.

### Main Game

`main.py` controls the game loop and connects the different classes together.

It handles:

* Keyboard input
* Snake movement
* Food collision
* Wall collision
* Self-collision
* Score updates
* Game-over conditions

## Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

## Project Structure

```text
snake-game/
├── main.py
├── snake.py
├── food.py
└── scoreboard.py
```

## How to Run

Make sure Python is installed on your computer.

Run the game from the project directory:

```bash
python main.py
```

The game window will open and you can control the snake using the arrow keys.

## Requirements

No external Python packages are required.

The project uses Python's standard library:

* `turtle`
* `random`
* `time`

## What I Learned

Through this project, I practiced:

* Object-Oriented Programming
* Creating classes and objects
* Inheritance with the `Turtle` class
* Instance attributes and methods
* Working with multiple Python modules
* Importing and connecting classes between files
* Lists of objects
* Loops and conditionals
* Keyboard event handling
* Collision detection
* Random number generation
* Game loops
* Managing object state
* Building a graphical Python application

## Future Improvements

* Add a high-score system
* Prevent food from appearing on the snake
* Add different difficulty levels
* Add a pause/resume feature
* Add sound effects
* Add a start screen
* Add a restart option after game over

## Author

**Mark Bernard**
