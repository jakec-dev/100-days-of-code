import pandas

phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in
                 phonetic_dataframe.iterrows()}

word = input("Enter a word: ").upper()
phonetic_word = [phonetic_dict[letter] for letter in word]
print(phonetic_word)
