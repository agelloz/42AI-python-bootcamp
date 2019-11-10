import sys
import random

sys.stdout.write('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType \'exit\' to end the game.\nGood luck!\nWhat\'s your guess between 1 and 99?\n>> ')
a = input() 
n = random.randint(1, 99)
i = 0
while (a != n): 
    i += 1
    if (a == "exit"):
        sys.stdout.write("Goodbye!\n")
        exit()
    elif (a.isdigit() == False):
        sys.stdout.write("That\'s not a number.\nWhat\'s your guess between 1 and 99?\n>> ")
        a = input()
    elif (int(a) < n):
        sys.stdout.write("Too low!\nWhat\'s your guess between 1 and 99?\n>> ")
        a = input()
    elif (int(a) > n):
        sys.stdout.write("Too high!\nWhat\'s your guess between 1 and 99?\n>> ")
        a = input()
    elif (int(a) == n):
        if (n == 42):
            sys.stdout.write("The answer to the ultimate question of life, the universe and everything is 42.\n")
        if (i == 1):
            sys.stdout.write("Congratulations! You got it on your first try!\n")
        else :
            sys.stdout.write("Congratulations, you've got it!\nYou won in " + str(i)  + " attempts!\n")
        exit()
