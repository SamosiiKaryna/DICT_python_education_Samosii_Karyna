"""coffee machine simulator"""
import os
import collections
import sys

Usage = collections.namedtuple("Usage", "milk, water, coffee_beans, money, cups")


class CoffeeMachine:
    def __init__(self):
        # coffee machine resources
        self.machine_standard = {
            "money": 550,
            "water": 400,
            "milk": 540,
            "coffee_beans": 120,
            "cups": 9,
        }


    def fill(self):
        """The function of adding consumables to the coffee machine"""
        self.machine_standard['water'] += int(input("Write how many ml of water do you want to add:\n"))
        self.machine_standard['milk'] += int(input("Write how many ml of milk do you want to add:\n"))
        self.machine_standard['coffee_beans'] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.machine_standard['cups'] += int(input("Write how many disposable cups of coffee do you want to add:\n"))


    def take(self):
        """Function of the issuance of money"""
        print(f"I gave you {self.machine_standard['money']}")
        self.machine_standard['money'] = 0


    def status(self):
        """function to display the amount of consumables in the coffee machine at the moment"""
        print("The coffee machine has:")
        print(f"{self.machine_standard['water']} of water")
        print(f"{self.machine_standard['milk']} of milk")
        print(f"{self.machine_standard['coffee_beans']} of coffee beans")
        print(f"{self.machine_standard['cups']} of cups")
        print(f"{self.machine_standard['money']} of money")


    def available_check(self, usage):
        """The function of checking the availability of resources for making coffee, if the result is positive,
         the resources are subtracted"""
        if self.machine_standard['water'] - usage.water < 0:
            print("Sorry, not enough water")
        elif self.machine_standard['milk'] - usage.milk < 0:
            print("Sorry, not enough milk")
        elif self.machine_standard['coffee_beans'] - usage.coffee_beans < 0:
            print("Sorry, not enough coffee beans")
        elif self.machine_standard['cups'] - usage.cups < 0:
            print("Sorry, not enough cups")
        else:
            print("I have enough resources, making you a coffee!")
            self.machine_standard['water'] -= usage.water
            self.machine_standard['milk'] -= usage.milk
            self.machine_standard['coffee_beans'] -= usage.coffee_beans
            self.machine_standard['cups'] -= usage.cups
            self.machine_standard['money'] += usage.money

    def buy(self):
        """The process of buying coffee"""
        buy_input = int(input("What do you want to buy? 1-espresso, 2-latte, 3-cappuccino,back to main menu:\n"))
        espresso = Usage[250, 0, 16, 1, 4]  # water, milk, coffee beans, cups, money
        latte = Usage[350, 75, 20, 1, 7]
        cappuccino = Usage[200, 100, 12, 1, 6]
        usage = {1: espresso, 2: latte, 3: cappuccino}[buy_input]
        self.available_check(usage)
        if buy_input == 'back':
         os.system("python coffeemachine.py")
         exit()


    def action(self):
        """Function for the user with a choice of actions"""
        if user_input == "buy":
            self.buy()
        elif user_input == "fill":
            self.fill()
        elif user_input == "take":
            self.take()
        elif user_input == "remaining":
            self.status()
        elif user_input == "exit":
            sys.exit("Goodbye!")
        else:
            print("Invalid Action")
        return True


# class start
machine = CoffeeMachine()
run = True
while run:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")
    run = machine.action()
