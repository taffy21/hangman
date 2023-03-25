from random import choice
import re

words = ["chuck", "aeroplane", "development"]

def wordHider(word):
    count = len(word)
    return ["_"] * count

def combineListLetters(arg):
    word = ""
    for i in arg:
        word += i
    return word

def wordPlayer():

    word = choice(words)
    playing = True
    wrong_count = 0
    complete = wordHider(word)
    selected_word = word
    while playing:
        print(combineListLetters(complete))
        letter = input("Letter: ")
        if letter in selected_word:
            indexes = [i.start() for i in re.finditer(letter, word)]
            for index in indexes:
                complete[index] = letter
            print(combineListLetters(complete))
        else:
            wrong_count += 1

        if selected_word == combineListLetters(complete) or wrong_count == 10:
            playing = False


