#

greeting = input ('Type a greeting to start chat: ') #Prompt user for a greeting
greeting_2 = greeting.strip().lower()  #Remove leading whitespace and convert to lower case

if greeting_2.startswith('hello'):
    print('$0')
elif greeting_2.startswith('h'):
    print('$20')
else:
    print('$100')
