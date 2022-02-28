from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start_app():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    caesar(text, shift, direction)
    do_restart = input("Do you want to restart? [y/N] ").lower()
    if do_restart == "y":
        start_app()

def caesar(text, shift, direction):
    output_text = ""
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter)
            if direction == "encode":
                shifted_position = position + shift
                if shifted_position > len(alphabet) - 1:
                    shifted_position -= len(alphabet)
            else:
                shifted_position = position - shift
                if shifted_position < 1:
                    shifted_position += len(alphabet)
            shifted_letter = alphabet[shifted_position]
            output_text += shifted_letter
    print(f"The {direction}d text is {output_text}")

start_app()