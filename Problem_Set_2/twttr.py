#When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr.
#In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    text = input('Insert text: ')

    #What data is given to me?
    vowels = ['a', 'e', 'i', 'o','u']

    for letter in text:  #Check ALL letters of the word user inputs
        if letter.lower() in vowels:        #Check if letter is a vowel or not - from the vowel list. Also, use the .lower() to recognize the uppercase letters too
            text = text.replace(letter, '') #If it is, replace letter with empty string
    print(text)


main()
