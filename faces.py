def main():
    message_1 = input('How are you feeling? ') #prompt user input that uses emoticons
    message_2 = convert(message_1) #convert input to message with emojis by calling the convert func
    print(message_2) #display the message with emojis


def convert(message_1):     #define function called convert with the input message as the string
    message_smile = message_1.replace(':)', '🙂') #Replace the smile emoticon with smile emoji
    message_frown = message_smile.replace(':(', '🙁') #Replace the frown emoticon with frown emoji
    return message_frown #Return value to function

main()

'''
Line 8

I could have said :
message_smile = message_1.replace(':)', '🙂').replace(':(', '🙁')

To avoid creating too many variables. But then ... breakdown for understanding

'''
