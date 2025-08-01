'''
Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
'''


m = int(input('Please enter the mass: ')) #Request from user, assume they will input an integer
c = 300000000  #Value of the speed of light - its a constant
e = m * (c ** 2) #Formula that calculates energy

print('E: ', e)

'''
Alternative:

print(f'E:{e}')

Did not use this as I'm comfortable with f strings yet
'''
