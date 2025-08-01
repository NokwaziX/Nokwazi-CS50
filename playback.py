#Ask user to input their favourite dessert
dessert = input("What is your favourite dessert? ")


#Make the user slow down
say_dessert = dessert.replace(" ", "...")

#Make user respond slowly
print(say_dessert)

'''
#I could have just skipped to this step but I like to breakdown steps for understanding
#Get the user's slow response
print(dessert.replace(" ", "..."))
'''