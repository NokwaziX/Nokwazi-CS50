'''
                            Implement a program that:

1. Expects the user to provide two command-line arguments:

** The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
** The name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

2. Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
   If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

'''
import sys
import csv

def main():
    check_command_line_arg()
    before = sys.argv[1]            #This is the csv file before, AKA user's input at cmnd line position 2
    after = sys.argv[2]             #This is the csv file after, AKA user's input at cmnd line position 3
    output = []                     #Empty list that stores the amended csv rows

    #try to open the file
    try:
        with open(before, 'r') as file:
            reader = csv.DictReader(file)           #Use csv.DictReader read file as list of dictionaries

            for line in reader:                     #Loop through each row in the csv file
                lastname, firstname = line['name'].strip().split(',')  #Split 'name' into 'lastname' and 'firstname'
                lastname, firstname = lastname.strip(), firstname.strip()
                house = line['house']               #get 'house' field from row
                output.append({'first': firstname, 'last': lastname, 'house': house})   #Create new dict with keys 'first' 'last' 'house' AND ... append amended dict to output list
        #print(original)

    #if u cannot open, means file doesnt exist
    except FileNotFoundError:
        sys.exit(f'Could not read {before}!')

    #Now Write to NEW csv file
    with open(after, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])    #Define a DictWriter with the fieldnames for the new CSV format
        writer.writeheader()                            #Write the header row to the new CSV file
        for line in output:
            writer.writerow(line)                       # Write each transformed row (from output list) to the new CSV file




#*********************************************************************************

def check_command_line_arg():

    #check if the user inputted 2 arg after program name in cmnd line
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments!')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments!')

    #check if user inputted a csv file
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('Not a CSV file!')



if __name__ == '__main__':
    main()