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
         try:
            fraction = input('Insert fraction: ')     #Prompt user for fraction in this format X/Y
            percentage = convert(fraction)
            print(gauge(percentage))
            break                                     #Exit the loop once valid input is received
         except (ValueError, ZeroDivisionError):      #If user provides fraction with 0 as denominator or invalid fraction, prompt again
            continue



            #***************CONVERT FRACTION TO DECIMAL***********************#
def convert(fraction):
    #while True:
    try:
        x, y = fraction.split('/')  #split numerator and denominator with a seperator '/'
        x = int(x)                  #x is a positive integer (numerator)
        y = int(y)                  #y is a positive integer (denominator)

        if y == 0:           #If x is greater than y OR y is equal to zero - prompt user again (raise a Value error)
            raise ZeroDivisionError
        if x < 0 or y < 0:           #If x is greater than y OR y is equal to zero - prompt user again (raise a Value error)
            raise ValueError
        if x > y:           #If x is greater than y OR y is equal to zero - prompt user again (raise a Value error)
            raise ValueError

        s = x / y
        percentage = round(s * 100)   #Output as percentage rounded to nearest int
        return percentage

    except (ValueError, ZeroDivisionError):
        raise


            #********************RETURN PERCENTAGE THAT WILL PRINT IN MAIN()***************#
def gauge(percentage):
    if percentage <= 1:     #If 1% or more remains, return 'E'
        return 'E'
    elif percentage >= 99:  #If 99% or more remains, return 'F'
        return 'F'
    else:                   #Otherwise, return percentage
        return f'{percentage}%'



if __name__ == "__main__":
    main()