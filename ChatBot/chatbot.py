print("Hello! My name is DICT_Bot.")
print("I was created in 2022")

print("Please, remind me your name")
user_input = input(">")
print("What a great name you have,",user_input,"!")

print("Let me guess your age")
print("Enter remainders of dividing your age by 3,5 and 7.")
remainder3 = input(">")
remainder5 = input(">")
remainder7 = input(">")
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is" ,age, "; that's a good time to start programming!")