
alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def caesar(original_text, shift_amount, encode_decode):
    result = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabets:
            shifted_letter = (alphabets.index(letter) +
                              shift_amount) % len(alphabets)
            result += alphabets[shifted_letter]
        else:
            result += letter

    print(f"Here is the {encode_decode}d message: {result}")


restart = True

while restart:
    direction = input(
        "Type 'encode' to encode and 'decode' to decode:\n"
    ).lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type your shift number:\n"))

    caesar(
        original_text=text,
        shift_amount=shift,
        encode_decode=direction
    )

    should_continue = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()

    if should_continue == "no":
        restart = False
        print("Goodbye! Have a nice day.")
