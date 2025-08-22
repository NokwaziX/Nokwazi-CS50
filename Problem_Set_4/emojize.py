#Implement a program that prompts the user for a str in English and
#Outputs the “emojized” version of that str
#Converting any codes (or aliases) therein to their corresponding emoji.

import emoji

def main():
    text = input('Provide an emoji name: ')      #Prompt user for str
    print("Surprise ", emoji.emojize(text, language = 'alias'))  #Output emojized version of str


main()
