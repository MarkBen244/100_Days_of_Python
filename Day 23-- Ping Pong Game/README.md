# 🏓 Ping Pong

## About the Project

Ping Pong is a two-player Pong-style game built with Python using the `turtle` graphics module.

Each player controls a paddle and tries to prevent the ball from passing their side of the screen. The ball becomes faster after each successful paddle hit, making the game progressively more challenging.

This project was built to practice Object-Oriented Programming, inheritance, multiple Python modules, collision detection, keyboard controls, and game loops.

## Features

* 🏓 Two-player Pong gameplay
* 🎮 Keyboard controls
* ⚪ Ball movement and bouncing
* 🧱 Wall collision detection
* 🏓 Paddle collision detection
* 📈 Score tracking
* ⚡ Increasing ball speed
* 🏆 Automatic point detection
* 🖥️ Graphical interface using Turtle

## Controls

### Right Player

| Key           | Action    |
| ------------- | --------- |
| ⬆️ Up Arrow   | Move Up   |
| ⬇️ Down Arrow | Move Down |

### Left Player

| Key | Action    |
| --- | --------- |
| W   | Move Up   |
| S   | Move Down |

## How It Works

### Ball

The `Ball` class controls the ball's movement, direction, speed, and bouncing.

The ball moves continuously across the screen and changes direction when it hits a wall or paddle.

### Paddle

The `Paddle` class creates and controls each player's paddle.

Two paddle objects are created:

* Right paddle
* Left paddle

The paddles are controlled independently using keyboard input.

### Scoreboard

The `Scoreboard` class keeps track of both players' scores and displays them at the top of the screen.

### Main Game

`main.py` controls the game loop and connects the different classes.

It handles:

* Keyboard input
* Ball movement
* Wall collisions
* Paddle collisions
* Scoring
* Ball resets
* Game speed

## Project Structure

```text
ping-pong/
├── main.py
├── ball.py
├── paddle.py
└── scoreboard.py
```

## How to Run

Make sure Python is installed on your computer.

Run the game from the project directory:

```bash
python main.py
```

The game window will open and both players can begin playing.

## Requirements

No external Python packages are required.

The project uses Python's standard library:

* `turtle`
* `time`

## What I Learned

Through this project, I practiced:

* Object-Oriented Programming
* Creating classes and objects
* Inheritance from the `Turtle` class
* Instance attributes and methods
* Working with multiple Python modules
* Importing and connecting classes
* Game loops
* Collision detection
* Keyboard event handling
* Managing object movement
* Tracking game state
* Working with timers and delays
* Updating a graphical interface
* Building a simple two-player game

## Future Improvements

* Add a winning score limit
* Add a start screen
* Add a pause/resume feature
* Add sound effects
* Add different difficulty levels
* Add a restart option
* Add more advanced ball physics
* Add visual effects when a player scores

## Author

**Mark Bernard**
