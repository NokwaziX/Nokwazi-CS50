#Prompt user for items, one per line, until the user inputs control-d.
#output the user’s grocery list in all uppercase,
#Sorted alphabetically by item,
#Prefixing each line with the number of times the user inputted that item.

def main():
    groceries = {}  #Key:Item and Value: number of time it appears

    while True:

        try:
            item = (input('').upper()) #User input in uppercase

        except EOFError:
            print()
            break
        if item in groceries:   #Check if item is in list
            groceries[item] += 1 #If item is in list, increase its count by 1
        else:
            groceries[item] = 1    #Otherwise if item is not in dict, the initial value is == 1

    for item in sorted(groceries):      #print keys of dict and its values and put them in alphabetical order
        print(groceries[item], item)



main()