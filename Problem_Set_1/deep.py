answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ') #Prompt user to answer the question
answer_1 = answer.lower().strip() #convert user input to lowercase and remove white space incase user inputs spaces before and after text

if answer_1 == '42':
    print ('Yes')
elif answer_1 == 'forty-two':
    print ('Yes')
elif answer_1 == 'forty two':
    print ('Yes')
else:
    print ('No')


'''
Another method you can use is the 'OR' function to shorten your code

if answer_1 == '42' or answer_1 == 'forty-two' or answer_1 == forty two:
    print('Yes')
else:
    print('No')

'''