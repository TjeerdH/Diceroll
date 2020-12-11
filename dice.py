import random
import time

while True:
    rolling_dice = input("Do you want to roll the dice? ")
    if rolling_dice.lower() == "n" or rolling_dice.lower() == "no":
        again = False
        print("Why did you start the program then.....")
        exit()
    elif rolling_dice.lower() == "y" or rolling_dice.lower() == "yes":
        again = True
        break
    else:
        print("Please enter yes or no!")
        continue


while again:
    print("Rolling the dice......")
    time.sleep(1.5)
    print("The value is...")
    time.sleep(0.75)
    print(random.randrange(1,6), end="  ")
    print(random.randrange(1,6))
    rolling_dice = input("Do you want to roll again? ")
    if rolling_dice.lower() == "y" or rolling_dice.lower() == "yes":
        again = True
    else:
        again = False
        print("Thank you for rolling!")
        break

