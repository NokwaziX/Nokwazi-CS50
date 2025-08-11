'''
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''


def main():

    while True:
        fraction = input('Insert fraction: ')     #Prompt user for fraction in this format X/Y


        try:
            x, y = fraction.split('/')  #split numerator and denominator with a seperator '/'

            x = int(x)          #x is a positive integer
            y = int(y)          #y is a positive integer

            if x > y:           #If x is greater than y - prompt user again (continue)
                continue

            percentage = round((x / y) * 100)   #Output as percentage rounded to nearest int

            if percentage <= 1:     #If 1% or more remains, output 'E'
                print('E')
            elif percentage >= 99:  #If 99% or more remains, output 'F'
                print('F')
            else:
                print(f'{percentage}%')
            break

        except (ValueError, ZeroDivisionError):
            continue


main()