#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.

#Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
#Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


def main():

    #List given data
    amount_due = 50
    coins = [5, 10, 25]

    while amount_due > 0:          #Use WHILE loop as I want the program to iterate until the entire amount is paid. While ad is greater than 0, user must pay.
        print(f'Amount Due: {amount_due}') #Print a.d

        coin = int(input('Insert Coin: '))  #Prompt user for the amount they are paying as an integer so we can do arithmatic operations

        #Check wether the coin inputed is a valid one
        if coin in coins:   #If coin input is in the coins list, then:
            amount_due = amount_due - coin  #New a.d will be original a.d - input amount
    print(f'Change Owed: {abs(amount_due)}')

#Change will be a negative number so we use the abs() method so that user's chnage doesn't print as a negative number

main()


'''
The abs() function in Python is a built-in function that returns the absolute value of a given number.
The absolute value of a number is its distance from zero on the number line, regardless of its sign.
'''