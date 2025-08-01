'''
The expression shoyld look like:

x=1  y= +  z=1 (these are the elements)

That would be 1 + 1

Elements are split by a space ['1', '+', '1']
'''

expression = input('Insert Math expression: ')  #prompt user to give an expression
elements = expression.split(' ')

#In Python when we have a list, the first element is indexed at 0. We start counting from 0
#E.g [1, 2, 3] --- 1 is indexed/positioned @ 0

#In this list ['1', '+', '1'] elements are listed as strings so we must convert to ingeters
num1 = int(elements[0])  # '1'
operator = elements[1]   # '+'
num2 = int(elements[2])  # '1'

#
if operator == '+':
    result = num1 + num2    #store the expression into a variable
    print(f'{result:.1f}')  #print the result and format result to 1 decimal place. use f string.
elif operator == '-':
    result = num1 - num2
    print(f'{result:.1f}')
elif operator == '*':
    result = num1 * num2
    print(f'{result:.1f}')
elif operator == '/':
    result = num1 / num2
    print(f'{result:.1f}')

'''
To clean up the code:
indent the print(f'{result:.1f}') to If as it repeats. Like this:

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
print(f'{result:.1f}')

'''
