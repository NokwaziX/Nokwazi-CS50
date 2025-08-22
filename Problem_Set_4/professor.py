'''
#Prompts the user for a level, n.
 If the user does not input 1, 2, or 3, the program should prompt again.
#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
 digits.
 No need to support operations other than addition (+).
#Prompts the user to solve each of those problems.
 If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
 If the user has still not answered correctly after three tries, the program should output the correct answer.
#The program should ultimately output the user’s score: the number of correct answers out of 10.
'''

'''
PLEASE DO NOT MIND MY EXCESSIVE COMMENTING - ITS FOR MY OWN UNDERSTANDING
'''

import random


def main():
   level = get_level()  #Get the level from user
   score = 0    #Set score to zero as you start the game at zero points
   tries = 0    #Start the game at zero tries - this is the number of tries user has had for a specific question

   for i in range(10):      #Remember, we're asking user 10 questions
       x, y = generate_integer(level), generate_integer(level)
       while tries < 3:
           try:
               answer = int(input(f'{x} + {y} = ')) #Prompt user for an answer of X+Y
           except ValueError:           #If user inputs incorrect answer,
               print('EEE')             #Print this error and prompt again - but they only have 3 tries
               tries = tries + 1        #User has used up one try -- (0 + 1)
               continue                 #Prompt again
           else:
                if answer == (x + y):   #If user's answer is correct,
                    score = score + 1   #Add 1 to the score
                    tries = 0           #Reset the number of tries to zero as user answered correctly
                    break               #Break out of the loop
                else:                   #Otherwise, if answer incorrect,
                    print('EEE')        #Print EEE for error
                    tries = tries + 1   #User has used up one try -- (0 + 1)
                    continue            #Prompt again
       if tries >= 3:
        print(f'{x} + {y} = {x + y}')
        tries = 0
   print(f'Score: {score}')



#========================================================

    #HERE WE GET TO KNOW WHICH LEVEL USER IS PLAYING
def get_level():
    levels = [1, 2, 3]      #There can only be level 1,2,3.

    while True:         #Create infinite loop that will prompt user AGAIN if above conf=dition is not met
        try:            #Use try statement as it possible that user may enter incorrect value
            level = int(input("Level: "))   #Prompt user input(level)

            if level in levels:     #If the LEVEL is in the list of LEVELS then,
                return level        #Return level

        except ValueError:          #If user inputs anything apart from 1,2,3 (value error) then,
            continue                    #CONTINUE prompting using for level till they get it right


#==========================================================

    #HERE WE GENERATE A RANDOM INTEGER FOR X and Y
def generate_integer(level):
    if level == 1:          #If user selects lvl1,
        return random.randint(0, 9) #Return random integer between 0 & 9
    elif level == 2:        #If user selects lvl2,
        return random.randint(10, 99)   #Return random integer between 10 & 99
    elif level == 3:        #If user selects lvl3,
        return random.randint(100, 999) #Return random integer between 100 & 999
    else:           #If user selects ANYTHING ELSE either than 1,2,3 -
        raise ValueError    #Raise value error



if __name__ == "__main__":
    main()

