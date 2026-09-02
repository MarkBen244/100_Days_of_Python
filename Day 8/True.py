# def greet(name):
#     print("Hello", name)
#     print("Hows the weather like? ", name)


# surname = input("Whats your surnname")
# greet(surname)

# def greet_with(name, location):
#     print("Hello", name)
#     print("Hows the weather like in", location)


# greet_with(location="USA", name="Mark")

truee = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
true_score = 0
love_score = 0
name1 = "mark bernard"
name2 = "chizzi agullanna"
true_score = 0


def calculate_love_score(name1, name2):
    love_score = 0
    true_score = 0
    # name_1 = list(name1)
    # name_2 = list(name2)
    name3 = name1+name2
    name_3 = list(name3)
    for letter in name3:
        if letter == "t":
            true_score += true_score
        elif letter == "r":
            true_score += true_score
        elif letter == "u":
            true_score += true_score
        elif letter == "e":
            true_score += true_score
    print(true_score, name_3)


calculate_love_score("mark bernard", "mary jane")
