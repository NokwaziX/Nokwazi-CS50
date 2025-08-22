# Expects zero or two command-line arguments:
# Zero (commandline args)if the user would like to output text in a random font.
# Two (commandline args)if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

#If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

from pyfiglet import Figlet
import sys          #If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
import random       #Zero if the user would like to output text in a random font.



def main():

    #text = input('User Input: ')
    figlet = Figlet()
    fonts = figlet.getFonts()   #Fonts list


    #Now we check if commandline arg is zero or two:

    if len(sys.argv) == 1:      #If the length of the arg is 1 (just the program name without an arg),
        output1 = random.choice(fonts) #Then output a random font from the fonts list
        figlet.setFont(font = output1)    #Set font - which will be a random font

        #print(figlet.renderText(text))

    elif len(sys.argv) == 3:    #If the length of the arg is 3 (program name & -f & fontname),
        input1 = sys.argv[1]    #'-F' or '--FONT'
        input2 = sys.argv[2]    #FONT NAME

        #Check if user gave 2 args but the first is not '-f' or '--font or if 2nd is not font name. Exit with error msg
        if input1 not in ['-f', '--font']:  #If the first second input is not '-f' or '--font'
            sys.exit('Invalid usage')       #Exit with error msg

        if input2 in fonts:     #If inputted font name is in the fonts list then,
            figlet.setFont(font = input2)   #Set the font to inputted font
        else:
            sys.exit('Invalid usage')   #Otherwise, tell user invalid and exit


    else:
        sys.exit('Invalid usage')


    text = input('User Input: ')
    print(f'Output: {figlet.renderText(text)}')

main()