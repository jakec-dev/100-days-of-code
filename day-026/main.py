import pandas

phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in
                 phonetic_dataframe.iterrows()}

word = input("Enter a word: ").upper()
try:
    phonetic_word = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please")
else:
    print(phonetic_word)
