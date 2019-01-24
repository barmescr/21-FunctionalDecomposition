"""
Hangman.

Authors: Cleo Barmes and Alexander Hinojosa.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():
    print('Game has started!')
    match()
    dashes()


def get_length():
    string = input('Enter minimum word length.')
    integer = int(string)
    print('length of word =', integer)
    return integer


def get_word():
    with open('words.txt') as diction:

        string = diction.read()
        words = string.split()
        length = get_length()

        while True:
            r = random.randrange(0, len(words))
            item = words[r]

            if len(item) >= length:
                print(item)
                return item


def get_number_of_guesses():
    string = input('Enter number of guesses.')
    integer = int(string)
    print('Number of guesses =', integer)
    return integer


def get_guess():
    string = input('Enter a guess.')
    letter = str(string)
    print('Your guess is', letter)
    return letter


def word_to_list():
    word = get_word()
    list = []
    for k in range(len(word)):
        list = list + [word[k]]
    return list


def match():
    word = word_to_list()
    count = get_number_of_guesses()
    while True:
        guess = get_guess()
        for k in range(len(word)):
            if word[k] == guess:
                print('Correct', word[k])
                return
        count = count - 1
        print(count)

def dashes():
    list = []
    length = len(word_to_list())
    print('-' * length)
















main()