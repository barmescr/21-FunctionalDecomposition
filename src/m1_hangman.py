"""
Hangman.

Authors: Cleo Barmes and Alexander Hinojosa.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():
    word = get_word()
    guess_number = get_number_of_guesses()
    board = create_board(word)
    while True:
        guess = get_guess()
        guess_check = check_guess(word, guess)
        if guess_check is True:
            print('You are right')
            board = update_board(word, guess, board)
        else:
            guess_number = guess_number - 1
            print('Try Again, only ', str(guess_number), 'of guesses left')
        print_board(board)

        if guess_number == 0:
            break
        if check_complete(board) == True:
            print('You Win!')
            break


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


def check_guess(word, guess):
    for k in range(len(word)):
        if guess == word[k]:
            return True
    return False

def dashes():
    list = []
    length = len(word_to_list())
    print('-' * length)


def create_board(word):
    board = len(word) * '- '
    board = board.split()
    return board


def update_board(word, guess, board):
    for k in range(len(word)):
        if guess == word[k]:
            board[k] = guess
    return board

def print_board(board):
    string = ''
    for k in range(len(board)):
        string = string + str(board[k])
    print(string)

def check_complete(board):
    for k in range(len(board)):
        if board[k] == '-':
            return False
    else:
        return True















main()