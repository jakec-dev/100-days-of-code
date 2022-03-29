import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as data:
    phonetic_array = data.readlines()

phonetic_dataframe = pandas.DataFrame(phonetic_array)

print(phonetic_dataframe)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
