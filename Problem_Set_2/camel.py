#Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
#Assume that the user’s input will indeed be in camel case.

def main():
    word = input('camelCase: ')  #Prompt user for input in camelCase

    for letter in word:            #Check letters in the user's input
        if letter.isupper():        #If a letter is upper case:
            word = word.replace(letter, '_' + letter.lower())  #replace uppercase letter with '_' and lowercase letter. Store the new amendments in a variable
    print('snake_case:', word)


main()

'''

for the second variable "word", I did not change the name of the variable as the changes would have only applied ONLY to the original input.

e.g input: preferredFirstName would have outputted preferredFirst_name had I changed the variable to "word_2"

'''