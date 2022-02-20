import random

generate = random.randint(1,10)

wrong = 0

print("Guess a number in between 1 to 10")

while( wrong < 5):

    guess = int(input("What do you think the numebr is? "))

    if guess == generate:
        print("You win!!")
        break

    if guess >  generate :
        print("Your guess is too high!! ")

    elif guess <  generate :
        print("Your Guess is too low!!")

    wrong = wrong + 1


if not wrong < 5 :
    print("You Lose")


    