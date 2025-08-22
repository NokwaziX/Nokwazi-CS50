#prompts the user for names, one per line,
#until the user inputs control-d.
# Assume that the user will input at least one name.
#Then bid adieu to those names,
#Separating:
#TWO NAMES = ONE AND,
#THREE NAMES with TWO COMMAS and ONE AND
#N names with N-1 COMMAS and ONE AND


import inflect

def main():

    names_list = []

    while True:     #create infinite loop that will keep asking user for names
        try:
            names = input('Name: ') #prompt user for input
            names_list.append(names)    #add
        except EOFError:
            break


    p = inflect.engine()
    mypeople = p.join(names_list)       #Join Words into a List - 'and' for a list
    print(f'Adieu, adieu, to {mypeople}')


main()