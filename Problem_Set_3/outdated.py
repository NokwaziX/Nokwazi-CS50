#List months

'''
* Implement a program that prompts the user for a date,
* Month-day-year order,
* Formatted like 9/8/1636 or September 8, 1636,
* Wherein the month in the latter might be any of the values in the list below:
* Then output that same date in YYYY-MM-DD format
* If the user’s input is not a valid date in either format, prompt the user again
* Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days
'''

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#Loop forever
while True:
    date = input('Date (m/d/yyyy or Month d, yyyy) : ').strip()       #prompt user to enter date mm/dd/yy

    #Format1: 9/8/1636
    if "/" in date:                     #If there is a "/" in date then,
        month, day, year = date.split('/')      #split the month, day, year with "/"

    #Format2: September 8, 1636
    elif "," in date:                   #If there is a "," in date then,
        month, day, year = date.split()  #split the month, day, year with "whitespace" since there alredy is a ','


        if month in months:             #If the month is the list of months then,
            month = months.index(month) #Find its index e.g Sep index is 8
            month = month + 1           #So we need to +1 to make it 9
            day = day.strip(',')        #strip the comma from the day
    else:
        continue                        #Otherwise, prompt the user again


    try:
        #Now assume that every month has no more than 31 days
        month = int(month)
        day = int(day)

        if day > 31 or month > 12:     #Error checking: if user inputs day that exceeds 31 or month that exceeds 12
            continue                    #Otherwise, prompt the user again
        else:
            break                       #Break out of loop if user enters date in correct formats
    except ValueError:
        continue

#We use TRY and EXCEPT to help if user inputs incorrect format
print(f'{year}-{month:02}-{day:02}')    #We put :02 next to month and day so it can print TWO DIGITS

