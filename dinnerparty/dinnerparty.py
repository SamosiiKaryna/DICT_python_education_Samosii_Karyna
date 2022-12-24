"""Writing a group cost sharing program equally among all participants."""
import sys
import random


def count(users_num, our_users, total_amount):
    """This is a function that counts the number of numeric values"""
    total_amount /= users_num
    friendly_company = dict.fromkeys(our_users, round(total_amount, 4))
    print(friendly_company)


def yes_choice(our_users, total_amount, users_num):
    """This is a function that selects a random lucky person"""
    lucky = random.choice(our_users)
    print(lucky + " is the lucky one! ")
    new_price = total_amount / (users_num - 1)
    friendly_company = dict.fromkeys(our_users, new_price)
    friendly_company[lucky] = 0
    print(friendly_company)


def check(our_users, users_num):
    """A function that recognizes usernames """
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(users_num):
        our_users.append(str(input("-> ")))
    print("Names:")
    for i in range(len(our_users)):
        print("{" + our_users[i] + "}")
    friendly_company = dict.fromkeys(our_users, 0)
    print(friendly_company)


def luck_choice():
    """A function that provides a choice of """
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    print("[YES]")
    print("[NO]")


def luck_process(user_choice, our_users, total_amount, users_num):
    """A function that indicates the result of an action depending on the choice of """
    while user_choice != "Exit":
        if user_choice == "YES":
            yes_choice(our_users, total_amount, users_num)
            sys.exit("Goodbye!")
            pass
        elif user_choice == "NO":
            print("No one is going to be lucky")
            count(users_num, our_users, total_amount)
            sys.exit("Goodbye!")
            pass
        else:
            print("No one is going to be lucky.")

        luck_choice()
        user_choice = input("Enter your choice:")


def process():
    """User count recognition function"""
    users_num = 0
    while users_num != "users_num":
        our_users = []
        print("Enter the number of friends joining (including you)")
        users_num = int(input("-> "))
        if users_num <= 0:
            print("No one is joining for the party")
            continue
        check(our_users, users_num)
        total_amount = int(input("-> "))
        count(users_num, our_users, total_amount)
        luck_choice()
        user_choice = input("Enter your choice:")
        luck_process(user_choice, our_users, total_amount, users_num)


def menu():
    """Prints for menu function"""
    print("Sharing of common costs")
    print("[1] Enter participants!")
    print("[2] Exit")


    menu()
    user = int(input("Enter your choice:"))
    while user != 0:
        if user == 1:
            process()
            pass
        elif user == 2:
            sys.exit("Goodbye!")
            pass
        else:
            print("No one is joining for the party")

menu()
