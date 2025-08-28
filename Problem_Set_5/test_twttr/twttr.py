def main():
    text = input('Insert text: ')
    print(shorten(text))
    #(shorten(text))



def shorten(text):
    #What data is given to me?
    vowels = ['a', 'e', 'i', 'o','u']

    for letter in text:  #Check ALL letters of the word user inputs
        if letter.lower() in vowels:        #Check if letter is a vowel or not - from the vowel list. Also, use the .lower() to recognize the uppercase letters too
            text = text.replace(letter, '') #If it is a vowel, replace letter with empty string
    return text

if __name__ == "__main__":
    main()