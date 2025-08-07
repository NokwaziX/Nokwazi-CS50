#Implement a program that prompts consumers users to:
#INPUT fruits and OUTPUT number of calories. case-insensitively
#Assume user input exactly as poster


def main():
    fruit = input('Enter fruit name: ').lower() #prompt user to enter fruit name and use .lower() to allow results whether there is upper or lower letter in the input

#Use dict as there are kv pairs. Key - fruit name and Value - Calory count

    fruits = {'apple': 130,
          'avocado': 50,
          'banana': 110,
          'cantaloupe': 50,
          'grapefruit': 60,
          'grapes': 90,
          'honeydew melon': 50,
          'kiwifruit': 90,
          'lemon': 15,
          'nectarine': 60,
          'orange': 80,
          'peach': 60,
          'pear': 100,
          'pineapple': 50,
          'strawberries': 50,
          'sweet cherries': 100,
          'tangerine': 50,
          'watermelon': 80
}
    if fruit in fruits:
        print('Calories', fruits[fruit]) #Print the callories of the fruit thats within the fruits dict

main()