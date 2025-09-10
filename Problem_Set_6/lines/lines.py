'''
implement a program that expects exactly one command-line argument:
 --the name (or path) of a Python file
 --outputs the number of lines of code in that file
 --excluding comments and blank lines.
If the user:
 --does not specify exactly one command-line argument
 --or if the specified file’s name does not end in .py
 --or if the specified file does not exist
The program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
'''

import sys

def main():
    check_command_line_arg()  #We are checking the cla

    #try to open the file
    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()        #Read all lines from file
    #If file cannot be open, means thayt it does not exist
    except FileNotFoundError:
        sys.exit('File does not exist')

    #Now start a loop that checks each line - check if starts with a # or whitespace
    count_lines = 0     #Start number of lines count @ 0
    for line in lines:
        if check_line(line) == False:       #If line is actual code (useful code)
            count_lines = count_lines + 1   #Then increase the count by 1
    print(count_lines)      #Print final count

#********************************************************************************************************************************************

def check_line(line):
    if line.isspace():      #If line contains ONLY whitespace,
        return True         #Ignore the line
    if line.lstrip().startswith('#'):   #If whitespaces have been removed and line starts with '#',
        return True                     #Ignore the line
    return False            #If niether of the above is true - do not ignore line
#***************************************************************************************************************************************

def check_command_line_arg():           #check user command line arg

    #Here we check the how many arguments user input (length). Remember that the file name is an arg
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    #Here we check if it is a Python file
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')



                                        #REFER TO LINE 23#
                #Open the text file by storing it in a variable using the OPEN func.
# ********file = open('hogwarts.txt', 'r')    #hogwarts.txt is the name of the file and 'r' means we can read from the file*******


if __name__ == '__main__':
    main()