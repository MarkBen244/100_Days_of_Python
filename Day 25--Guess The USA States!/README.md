# US States Game

## About the Project

A Python geography quiz that challenges players to identify all 50 states of the United States on a map.

The game uses Turtle to display the map and Pandas to read state names and their coordinates from a CSV file. Each correct guess is displayed in its corresponding location on the map.

### Features
- Interactive map of the United States
- Tracks correctly guessed states out of 50
- Prevents duplicate guesses from increasing the score
- Saves unguessed states to `states_to_learn.csv` when the game ends
- Supports exiting the game early

### Technologies Used
- Python
- Turtle
- Pandas
- pathlib

### How to Run

1. Make sure Python is installed.
2. Install Pandas if you haven't already:

   ```bash
   pip install pandas
   ```

3. Ensure the following files are in the same folder as `main.py`:
   - `blank_states_img.gif`
   - `50_states.csv`

4. Open a terminal in the project folder and run:

   ```bash
   python main.py
   ```

5. Enter state names in the input box. Type `Exit` to finish early.

### Project Structure

```text
Day25--Panda Library/
├── main.py
├── blank_states_img.gif
├── 50_states.csv
├── states_to_learn.csv
└── README.md
```

`states_to_learn.csv` is generated when the game ends if any states remain unguessed.

## Author

**Mark Bernard**

- GitHub: [MarkBen244](https://github.com/MarkBen244)