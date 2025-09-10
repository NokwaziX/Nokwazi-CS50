'''
Implement a program that:
---expects exactly one command-line argument,
---the name (or path) of a CSV file in Pinocchio’s format,
---and outputs a table formatted as ASCII art using tabulate

Format the table using the library’s grid format.

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist:
--- the program should instead exit via sys.exit.

'''
import sys
import csv
from tabulate import tabulate
#import tabulate

def main():
    check_command_line_arg()

    #create variable to store the table data
    table = []

    #try to open the file
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    #if u cannot open, means file doesnt exist
    except FileNotFoundError:
        sys.exit('File does not exist!')

    #print table
    print(tabulate(table[1:], headers=table[0], tablefmt = 'grid')) #table data(everything that is not the first element of the list), header(first element of list)

#*********************************************************************************

def check_command_line_arg():

    #check if the user inputted 1 arg after program name in cmnd line
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments!')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments!')

    #check if user inputted a csv file
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file!')



if __name__ == '__main__':
    main()
