alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    output_text = ""
    for letter in text:
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
    if direction == "encode":
        print_label = "encoded"
    else:
        print_label = "decoded"
    print(f"The {print_label} text is {output_text}")

caesar(text, shift, direction)