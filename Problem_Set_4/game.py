'''
#Prompts the user for a level, n.
 If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and n, inclusive, using the random module.
#Prompts the user to guess that integer.
 If the guess is not a positive integer, the program should prompt the user again.

 IF:
#Guess smaller than integer, Ouput: 'Too small!' and prompt again
#Guess larger than integer, Ouput: 'Too big!' and prompt again
#Guess same as integer, Ouput: 'Just right!' and exit
'''

import random


def main():

    #PROMPT USER FOR LEVEL, IN POSTIVE INT.
    while True:
        try:
            n = int(input('Level: '))   #prompt user for level(integer)
            if n > 0:       #If user inputs int larger than zero, don't prompt again
                break
        except ValueError:      #But if user inputs int less than zero(negative), prompt again
            continue

    num = random.randint(1, n)  #randomly generate int between 1 and n, inclusive

    #PROMPT USER TO GUESS INT, POSITIVE INT.
    while True:         #Create infinite loop to set me up to be able to prompt user again if they enter wrong things
        try:
            guess = int(input('Guess: '))

            if guess <= 0:              #if user guess negative number or a str, prompt again
                continue
            elif guess < num:             #if guess smaller than int, print and prompt again
                print('Too small!')
            elif guess > num:           #if guess larger than int, print and prompt again
                print('Too large!')
            else:                       #Otherwise, #if guess equal to int, print and exit
                print('Just right!')
                break

        except ValueError:
                continue




main()