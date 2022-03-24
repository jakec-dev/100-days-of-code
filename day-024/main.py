with open("./Input/Names/invited_names.txt") as data:
    names = data.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as sl:
    starting_letter = sl.read()

for name in names:
    formatted_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w")\
            as output:
        output.write(formatted_letter)
