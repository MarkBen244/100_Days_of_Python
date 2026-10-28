
from pathlib import Path

PLACEHOLDER = "[name]"

BASE_DIR = Path(__file__).resolve().parent

names_path = BASE_DIR / "Input" / "Names" / "invited_names.txt"
letter_path = BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
output_dir = BASE_DIR / "Output" / "ReadyToSend"

# Read the invited names
with open(names_path, encoding="utf-8") as name_file:
    names = name_file.readlines()

# Read the starting letter
with open(letter_path, encoding="utf-8") as letter_file:
    letter_content = letter_file.read()

# Create a personalized letter for each person
output_dir.mkdir(parents=True, exist_ok=True)

for name in names:
    stripped_name = name.strip()

    if stripped_name:
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        output_path = output_dir / f"letter_for_{stripped_name}.txt"

        with open(output_path, "w", encoding="utf-8") as completed_letter:
            completed_letter.write(new_letter)
