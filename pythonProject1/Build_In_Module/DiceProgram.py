import random

while True:
        print("The Number on Dice is : " ,random.randint(1,6))
        user_input = input("Do you want to continue (Y/N) - ")
        if user_input == 'N':
            print("You have exit the program by your choice ")
            break