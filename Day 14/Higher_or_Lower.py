import random

people = [
    ("Taylor Swift", 200),
    ("Cristiano Ronaldo", 400),
    ("MrBeast", 350),
    ("Elon Musk", 250),
    ("Beyoncé", 600),
    ("Mark", 1000)
]

random.shuffle(people)

score = 0

print("=== HIGHER OR LOWER ===")
print("Guess if the next person's search score is higher or lower.\n")

for i in range(len(people) - 1):

    current_name, current_score = people[i]
    next_name, next_score = people[i + 1]

    print(f"Current person: {current_name}")
    print(f"Next person: {next_name}")

    guess = input("Higher or Lower? ").lower()

    if next_score > current_score:
        correct_answer = "higher"
    else:
        correct_answer = "lower"

    print(f"\n{current_name}: {current_score}")
    print(f"{next_name}: {next_score}")

    if guess == correct_answer:
        score += 1
        print("✅ Correct!")
        print(f"Score: {score}\n")
        print("Moving to the next person...\n")

    else:
        print("❌ Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"\nGame Over! Your final score is {score}.")
        break

else:
    print(f"🎉 You got them all correct!")
    print(f"Final score: {score}/{len(people) - 1}")
