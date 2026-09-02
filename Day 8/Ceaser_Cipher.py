alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

direction = input(
    "Type 'encode' to encode and 'decode' to decode\n").lower()
text = str(input("Type your message:\n")).lower()
shift = int(input("Type your shift number:\n"))


def ceaser(original_text, shift_amount, encode_decode):
    A = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabets:
            shifted_letter = (alphabets.index(letter) + shift_amount)
            shifted_letter %= len(alphabets)
            A += alphabets[shifted_letter]
        else:
            A += letter
    print(f"Here is the {encode_decode}d message: {A}")


restart = True
while restart:
    direction = input(
        "Type 'encode' to encode and 'decode' to decode\n").lower()
    text = str(input("Type your message:\n")).lower()
    shift = int(input("Type your shift number:\n"))

    ceaser(original_text=text, shift_amount=shift, encode_decode=direction)

    should_continue = input(
        "Type 'yes' if you want to go agian, Otherwise type 'no'\n").lower()

    if should_continue == "no":
        restart == False
        print("Good bye , Have a nice day")
        break
