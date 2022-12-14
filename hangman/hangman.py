import random
"""This module add random choices in code"""

words = ('python', 'java', 'javascript', 'php')
word = random.choice(words)
turns = 8
guesses = ''
wrong = []


def menu():
    """Prints for menu function"""
    while True:
        choice = input("1. Play""\n2. exit""\n")
        if choice == '1':
            print("Welcome!\n")
            game(turns, guesses)
        if choice == '2':
            print("See you!")
            return

def game(turns, guesses):
    """Game function that checks for correctness and indicates error information """
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print("char")
            else:
                print("_")
                print(end="")
                failed += 1
        if failed == 0:
            print("You won!")
            print("guessed word:", word)
            break
        print()
        guess = input("Input a letter:>")
        guesses += guess
        if guess.upper():
            print("Please enter a lowercase English letter!")
        if len(guess) > 1:
            print("You should input a single letter.")
        elif guess in wrong:
            print("You've already guessed this letter.")
        else:
            wrong.append(guess)
        if guess not in word:
            turns -= 1
            print("Not right")
            print("You've got left", + turns, 'attempts!')
            if turns == 0:
                print("You lost!")

menu()