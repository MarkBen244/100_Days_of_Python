# 🐢 Turtle Crossing

## About the Project

Turtle Crossing is a Python game built using the Turtle graphics library. The goal is to guide a turtle across the road while avoiding moving cars. Each time the player reaches the finish line, they return to the starting position and advance to the next level, where the cars move faster.

This project demonstrates object-oriented programming, collision detection, game loops, file handling, and difficulty management.

## Features

- **Player Movement:** Move the turtle forward using the Up Arrow key.
- **Random Car Generation:** Cars appear at random vertical positions and in different colors.
- **Collision Detection:** The game ends when the player collides with a car.
- **Level Progression:** Reach the finish line to advance to the next level.
- **Increasing Difficulty:** Cars gradually accelerate as the player progresses.
- **Difficulty Selection:** Choose Easy, Normal, or Hard before starting.
- **Persistent High Score:** Save and load the highest level reached between game sessions.
- **Car Cleanup:** Remove cars that leave the screen to prevent unnecessary objects from accumulating.
- **Visual Feedback:** Display level-up notifications and a game-over summary.

## How It Works

The project is organized into separate modules, each responsible for a specific part of the game:

- `main.py` — Runs the game loop, handles difficulty selection, detects collisions, and manages level progression.
- `player.py` — Controls the player's appearance, movement, and starting position.
- `car_manager.py` — Creates cars, controls their movement, removes off-screen cars, and adjusts their speed.
- `scoreboard.py` — Displays the current level, difficulty, high score, and game-over information.

The high score is stored in a local text file named `high_score.txt` and loaded when the game starts.

## Controls

| Key | Action |
|---|---|
| ⬆️ Up Arrow | Move the turtle forward |

## Project Structure

```text
turtle-crossing/
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
├── high_score.txt
└── README.md
```

**Note:** `high_score.txt` is created when a new high score is saved. It may not exist before the first record is achieved.

## How to Run

**Prerequisites:** Python 3 installed.

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the game:

```bash
python main.py
```

4. Choose a difficulty when prompted.
5. Use the Up Arrow key to cross the road and avoid the cars.

## Requirements

This project uses Python's standard library, including:

- `turtle`
- `time`
- `random`

No external packages are required.

## What I Learned

- Applying object-oriented programming to a game.
- Using classes and inheritance to organize game objects.
- Handling keyboard input with event listeners.
- Detecting collisions between objects.
- Managing game levels and increasing difficulty.
- Reading and writing files to preserve high scores.
- Removing objects dynamically to manage game resources.
- Organizing a multi-file Python project.

## Future Improvements

- Add a restart option without closing the game.
- Introduce additional obstacles and road layouts.
- Add a pause and resume feature.
- Improve the graphics with road markings and animations.

## Author

**Mark Bernard**
