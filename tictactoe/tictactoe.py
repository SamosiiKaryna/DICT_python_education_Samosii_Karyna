"""Tic-tac-toe game"""
import sys
import time
import os


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Win = True
Draw = -1
Run = False
Game = Run


def board():
    """In this function, we draw the playing field by adding empty cells from the list to it for future storage
    X or O"""
    print("\n")
    print("\t      |      |")
    print(f"\t   {board[1]}  |  {board[2]}   |  {board[3]}")
    print('\t______|______|______')
    print("\t      |      |")

    print(f"\t   {board[4]}  |  {board[5]}   |  {board[6]}")
    print('\t______|______|______')
    print("\t      |      |")

    print(f"\t   {board[7]}  |  {board[8]}   |  {board[9]}")
    print("\t      |      |")
    print("\n")


def check_win():
    """This function checks if the player has won or not."""
    global Game
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' '
          and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and
          board[8] != ' ' and board[9] != ' '):
        Game = Draw


def pos(x):
    """This function checks if the cell is empty or not"""
    if board[x] == ' ':
        return True
    else:
        print("\nThis cell is occupied! Choose another one!")
        return False


def restart():
    """Game restart function"""
    users_input = input("Do you want to restart the game?Write \"YES\" or \"NO\" >")
    while users_input != 0:
        if users_input == "YES":
            print("Please wait...")
            time.sleep(3)
            os.system("python main.py")
            exit()
        elif users_input == "NO":
            print("Please wait...")
            time.sleep(3)
            sys.exit("Goodbye!")
        else:
            print("Invalid Choice!")


def how_is_winner(player):
    """This function checks the draw and who specifically won"""
    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
            restart()
        else:
            print("Player 2 Won")
            restart()


def process_game():
    """This is the main function of the game, in which there is a change in the course of the players and the right
    to choose a position """
    player = 1
    while Game == Run:
        board()
        if player % 2 != 0:
            print("Player 1's chance")
            mark = 'X'
        else:
            print("Player 2's chance")
            mark = '0'
        try:
            choice = int(input("Enter the position between [1-9] where you want to mark:"))
        except ValueError:
            print("Invalid Input! Try Again")
            continue
        if choice < 1 or choice > 9:
            print("Coordinates should be from 1 to 3!")
            continue
        if pos(choice):
            board[choice] = mark
            player += 1
            check_win()
    board()
    how_is_winner(player)


def menu():
    """Prints for menu function"""
    print("1.Start game")
    print("2.Exit")


menu()
menu_input = int(input("Enter your choice >"))
while menu_input != 0:
    if menu_input == 1:
        print("Please wait...")
        time.sleep(3)
        process_game()
        pass
    elif menu_input == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print("Invalid Choice!")

    menu()
