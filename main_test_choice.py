import os

def user_input():
    choice = """Please choose the test script you want to run (input 1, 2, 3...)
            1. Adding iphone to cart 
            2. Second script 
            Input: """

    main_choice = input(choice)

    if main_choice == "1":
        print("running script1") #run add iPhone to cart
        False
    elif main_choice == "2":
        print("run script2") #run script2
        False
    else:
        print("Invalid input, please try again")
        True

while True:
    user_input()