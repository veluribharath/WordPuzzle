import json
from itertools import permutations
with open('words_dictionary.json') as file:
    eng_dictionary = json.load(file)

def get_dictionary_words(word):
    letters_list = [letter for letter in word]
    english_dict_word = {}
    for n in range(3,len(letters_list)+1):
        english_dict_word[n] = []
        for y in list (permutations(letters_list,n)):
            z = "".join(y)
            if z in eng_dictionary.keys():
                english_dict_word[n].append(z)
        english_dict_word[n] = list(set(english_dict_word[n]))
        english_dict_word[n].sort()
    return english_dict_word