# 🃏 French Flashcard App

## 📌 About the Project

A simple French-English flashcard application built with Python and Tkinter.

The application helps users learn French vocabulary by displaying French words and automatically flipping the flashcards to reveal their English translations after 3 seconds.

Users can:
- View randomly selected French words.
- Reveal English translations automatically.
- Mark words they know using the ✅ button.
- Skip words they haven't learned using the ❌ button.
- Save their learning progress automatically.

Words marked as correct are removed from the learning list and saved to a CSV file, ensuring that learned words are not repeated in future sessions.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **Tkinter** – Graphical User Interface (GUI).
- **Pandas** – Reading, processing, and saving vocabulary data.
- **Random** – Random selection of flashcards.
- **CSV** – Storing French-English vocabulary and learning progress.

## 📂 Project Structure

```text
Day 32--Flashcard App/
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py
└── README.md
```

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd "Day 32--Flashcard App"
   ```

3. Install the required dependency:

   ```bash
   pip install pandas
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## 🎯 Learning Objectives

Through this project, I practised:

- Building graphical interfaces with Tkinter.
- Working with CSV files using Pandas.
- Using dictionaries and lists to manage data.
- Implementing random selection.
- Using functions and global variables.
- Scheduling functions with Tkinter's `after()` method.
- Saving application progress persistently.

## 👨‍💻 Author

**Mark Bernard**

- GitHub: [MarkBen244](https://github.com/MarkBen244)
