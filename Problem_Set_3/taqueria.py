#Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
#After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
#Treat the user’s input case insensitively.
#Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.


def main():


    menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
}

    total_price = 0     #Starts at 0 as no items have been added yet

    while True:
        try:
            item = input('Select item: ').title()       #Prompt user to select items

            if item in menu:        #If item is present in the menu
                price = menu[item] #For price: go to menu and locate the value corresponding to the product(key)
                total_price = total_price + price      #Latest total plus price of next item
                print(f'Total: ${"{:.2f}".format(total_price)}')     #Print total price, prefixed with dollar sign and formatted to 2 decimal places

        except EOFError:
            print()     #Just to add new line so when user stops, folder name doesnt show on prompt
            break           #Break out of loop if you get the EOFError - this is when user clicks cntrl-D


main()