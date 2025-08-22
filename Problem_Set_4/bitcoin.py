#User to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy.
#If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#Replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard

import requests
import sys
import json

def main():
    try:
        if len(sys.argv) == 1:  ##if the length of user input is = 1 (program name ONLY, no number of Bitcoins they want to buy)
            print('Missing command-line argument') #Exit with this error
            sys.exit(1)


        #Request for data from this CoinCap API
        request = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=e8fc70ab5c29b001fba1f0e91cfcda764776bb69a06c37da68e7d9173a473b53')
        data = request.json()   #Store data received in variable. Use json to make readable
        #Get current price of one bitcoin
        #Multiply by no. of bicoins user wants
        #Store result in variable 'result' as decimal
        n = float(data['data']['priceUsd']) * float(sys.argv[1])
        print(f"${n:,.4f}") #Print result(price of bitcoins in USD to 4 decimal places and ',' as seperator)

    except ValueError:      #If user insert a value that cannot be converted into a float e.g cat
        print("Command-line argument is not a number")  #Print error and exit
        sys.exit(1)

#Used sys.exit(1) as we are exiting with an error code.

main()